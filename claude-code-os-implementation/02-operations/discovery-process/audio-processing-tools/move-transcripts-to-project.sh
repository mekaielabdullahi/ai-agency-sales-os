#!/bin/bash

# Move completed transcripts to project audit folder
# This script monitors and moves transcripts to the appropriate project folder

# Configuration
WHISPER_OUTPUT="/Users/matthewkerns/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/audio-processing-tools/whisper-local/transcripts"
PLOTTER_AUDIT="/Users/matthewkerns/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/active-projects/plotter-mechanix/audit/transcripts"

echo "======================================"
echo "Moving Transcripts to Project Folder"
echo "======================================"
echo ""

# Create destination directory if it doesn't exist
mkdir -p "$PLOTTER_AUDIT"

# Check if source directory exists
if [ ! -d "$WHISPER_OUTPUT" ]; then
    echo "❌ Source directory not found: $WHISPER_OUTPUT"
    exit 1
fi

# Count transcript files
TRANSCRIPT_COUNT=$(ls -1 "$WHISPER_OUTPUT"/*.txt 2>/dev/null | wc -l)

if [ "$TRANSCRIPT_COUNT" -eq 0 ]; then
    echo "⏳ No transcripts found yet. Whisper may still be processing."
    echo ""
    echo "Monitoring for transcripts..."

    # Wait and check periodically
    for i in {1..360}; do  # Check for up to 6 hours
        sleep 60  # Wait 1 minute

        TRANSCRIPT_COUNT=$(ls -1 "$WHISPER_OUTPUT"/*.txt 2>/dev/null | wc -l)
        if [ "$TRANSCRIPT_COUNT" -gt 0 ]; then
            echo "✅ Found $TRANSCRIPT_COUNT transcript(s)!"
            break
        fi

        if [ $((i % 10)) -eq 0 ]; then
            echo "  Still waiting... ($(date '+%H:%M:%S'))"
        fi
    done
fi

# Move transcripts if found
if [ "$TRANSCRIPT_COUNT" -gt 0 ]; then
    echo "📁 Moving $TRANSCRIPT_COUNT transcript files..."
    echo ""

    # Move each transcript file
    for file in "$WHISPER_OUTPUT"/*.txt "$WHISPER_OUTPUT"/*.md "$WHISPER_OUTPUT"/*.json 2>/dev/null; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            echo "  Moving: $filename"
            cp "$file" "$PLOTTER_AUDIT/"
        fi
    done

    # Also check for the merged transcript
    if [ -f "$WHISPER_OUTPUT/FULL-TRANSCRIPT.md" ]; then
        echo "  Moving: FULL-TRANSCRIPT.md"
        cp "$WHISPER_OUTPUT/FULL-TRANSCRIPT.md" "$PLOTTER_AUDIT/"
    fi

    echo ""
    echo "✅ Transcripts moved successfully!"
    echo ""
    echo "📁 Location: $PLOTTER_AUDIT"
    echo ""
    echo "📊 Files in project folder:"
    ls -lh "$PLOTTER_AUDIT/"

    # Create a summary file
    echo "# Plotter Mechanix Discovery Call Transcripts" > "$PLOTTER_AUDIT/README.md"
    echo "" >> "$PLOTTER_AUDIT/README.md"
    echo "**Date Processed:** $(date)" >> "$PLOTTER_AUDIT/README.md"
    echo "**Model Used:** base (Whisper)" >> "$PLOTTER_AUDIT/README.md"
    echo "**Source:** Dec 3, 2025 Discovery Call" >> "$PLOTTER_AUDIT/README.md"
    echo "" >> "$PLOTTER_AUDIT/README.md"
    echo "## Files" >> "$PLOTTER_AUDIT/README.md"
    echo "" >> "$PLOTTER_AUDIT/README.md"

    for file in "$PLOTTER_AUDIT"/*.txt; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            echo "- $filename" >> "$PLOTTER_AUDIT/README.md"
        fi
    done

    echo "" >> "$PLOTTER_AUDIT/README.md"
    echo "## Next Steps" >> "$PLOTTER_AUDIT/README.md"
    echo "1. Review FULL-TRANSCRIPT.md for complete conversation" >> "$PLOTTER_AUDIT/README.md"
    echo "2. Run insight extraction: \`python extract-insights.py FULL-TRANSCRIPT.md\`" >> "$PLOTTER_AUDIT/README.md"
    echo "3. Update audit.json with findings" >> "$PLOTTER_AUDIT/README.md"
    echo "4. Generate executive report" >> "$PLOTTER_AUDIT/README.md"

    echo ""
    echo "📝 Created README.md in transcripts folder"

else
    echo "❌ No transcripts found after waiting."
    echo "Please check if Whisper is still running:"
    echo "  ps aux | grep whisper"
fi

echo ""
echo "======================================"
echo "Complete!"
echo "======================================"