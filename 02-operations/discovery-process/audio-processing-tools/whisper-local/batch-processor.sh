#!/bin/bash

# Batch process audio files with local Whisper (no API needed)
# Usage: ./batch-processor.sh /path/to/audio/directory [model]

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default settings
DEFAULT_MODEL="base"  # Options: tiny, base, small, medium, large
PYTHON_VERSION="python3.13"  # Use compatible Python version

# Check arguments
if [ $# -eq 0 ]; then
    echo "Usage: $0 /path/to/audio/directory [model]"
    echo "Models: tiny (fast), base (balanced), large (accurate)"
    exit 1
fi

AUDIO_DIR="$1"
MODEL="${2:-$DEFAULT_MODEL}"
OUTPUT_DIR="$(pwd)/transcripts"

# Validate audio directory
if [ ! -d "$AUDIO_DIR" ]; then
    echo -e "${RED}Error: Directory $AUDIO_DIR not found${NC}"
    exit 1
fi

echo "======================================"
echo "Whisper Batch Audio Processor"
echo "======================================"
echo "Audio Directory: $AUDIO_DIR"
echo "Model: $MODEL"
echo "Output: $OUTPUT_DIR"
echo ""

# Setup virtual environment
VENV_DIR="$(pwd)/whisper-env"
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Creating Python environment...${NC}"
    $PYTHON_VERSION -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install Whisper if needed
if ! python -c "import whisper" 2>/dev/null; then
    echo -e "${YELLOW}Installing Whisper (one-time setup)...${NC}"
    pip install --quiet --upgrade pip
    pip install --quiet openai-whisper
    echo -e "${GREEN}✅ Whisper installed${NC}"
fi

# Check ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo -e "${YELLOW}Installing ffmpeg...${NC}"
    brew install ffmpeg
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Find audio files
echo -e "${GREEN}Searching for audio files...${NC}"
audio_files=()
while IFS= read -r -d '' file; do
    audio_files+=("$file")
done < <(find "$AUDIO_DIR" -type f \( -name "*.wav" -o -name "*.WAV" -o -name "*.mp3" -o -name "*.MP3" -o -name "*.m4a" -o -name "*.M4A" -o -name "*.mp4" -o -name "*.MP4" \) -print0)

if [ ${#audio_files[@]} -eq 0 ]; then
    echo -e "${RED}No audio files found in $AUDIO_DIR${NC}"
    deactivate
    exit 1
fi

echo "Found ${#audio_files[@]} audio files"
echo ""

# Process each file
total=${#audio_files[@]}
current=0

for audio_file in "${audio_files[@]}"; do
    ((current++))
    filename=$(basename "$audio_file")
    name_without_ext="${filename%.*}"

    # Determine speaker from path if possible
    speaker="unknown"
    if [[ "$audio_file" == *"Chris"* ]] || [[ "$audio_file" == *"chris"* ]]; then
        speaker="chris"
    elif [[ "$audio_file" == *"Kelce"* ]] || [[ "$audio_file" == *"kelce"* ]]; then
        speaker="kelce"
    fi

    output_name="${speaker}_${name_without_ext}"

    echo -e "${YELLOW}[$current/$total] Processing: $filename${NC}"
    echo "  Model: $MODEL"
    echo "  Output: $output_name.txt"
    echo -n "  Status: Processing..."

    # Run Whisper
    if whisper "$audio_file" \
        --model "$MODEL" \
        --output_dir "$OUTPUT_DIR" \
        --output_format txt \
        --language en \
        --verbose False \
        2>/dev/null; then

        # Rename output file to include speaker
        if [ -f "$OUTPUT_DIR/${name_without_ext}.txt" ]; then
            mv "$OUTPUT_DIR/${name_without_ext}.txt" "$OUTPUT_DIR/${output_name}.txt"
        fi

        echo -e "\r  Status: ${GREEN}✅ Complete${NC}      "
    else
        echo -e "\r  Status: ${RED}❌ Failed${NC}        "
    fi
    echo ""
done

# Merge transcripts
echo -e "${YELLOW}Merging transcripts...${NC}"
MERGED_FILE="$OUTPUT_DIR/FULL-TRANSCRIPT.md"

echo "# Complete Transcription" > "$MERGED_FILE"
echo "" >> "$MERGED_FILE"
echo "Generated: $(date)" >> "$MERGED_FILE"
echo "Model: $MODEL" >> "$MERGED_FILE"
echo "" >> "$MERGED_FILE"

for txt_file in "$OUTPUT_DIR"/*.txt; do
    if [ -f "$txt_file" ] && [ "$txt_file" != "$OUTPUT_DIR/FULL-TRANSCRIPT.txt" ]; then
        filename=$(basename "$txt_file" .txt)
        echo "## $filename" >> "$MERGED_FILE"
        echo "" >> "$MERGED_FILE"
        cat "$txt_file" >> "$MERGED_FILE"
        echo "" >> "$MERGED_FILE"
        echo "---" >> "$MERGED_FILE"
        echo "" >> "$MERGED_FILE"
    fi
done

# Deactivate virtual environment
deactivate

# Summary
echo ""
echo "======================================"
echo -e "${GREEN}✅ Processing Complete!${NC}"
echo "======================================"
echo ""
echo "📁 Output Location:"
echo "  $OUTPUT_DIR"
echo ""
echo "📊 Files Generated:"
ls -lh "$OUTPUT_DIR"/*.txt 2>/dev/null | wc -l | xargs echo "  Individual transcripts:"
echo "  Merged transcript: FULL-TRANSCRIPT.md"
echo ""
echo "💡 Next Steps:"
echo "  1. Review $OUTPUT_DIR/FULL-TRANSCRIPT.md"
echo "  2. Extract key insights (pain points, budget, timeline)"
echo "  3. Update project documentation with findings"
echo ""