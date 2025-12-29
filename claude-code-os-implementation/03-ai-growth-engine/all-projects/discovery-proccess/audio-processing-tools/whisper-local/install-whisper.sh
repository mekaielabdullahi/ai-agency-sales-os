#!/bin/bash

# Install Whisper locally for free audio transcription
# No API key needed!

echo "======================================"
echo "Local Whisper Installation"
echo "======================================"
echo ""

# Check Python version
PYTHON_CMD=""
for version in python3.13 python3.12 python3.11 python3; do
    if command -v $version &> /dev/null; then
        PY_VERSION=$($version --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
        MAJOR=$(echo $PY_VERSION | cut -d. -f1)
        MINOR=$(echo $PY_VERSION | cut -d. -f2)

        # Whisper needs Python >= 3.8 and < 3.14
        if [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 8 ] && [ "$MINOR" -lt 14 ]; then
            PYTHON_CMD=$version
            echo "✅ Found compatible Python: $version ($PY_VERSION)"
            break
        fi
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "❌ No compatible Python found (need 3.8-3.13)"
    echo "Install with: brew install python@3.13"
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
$PYTHON_CMD -m venv whisper-env

# Activate environment
source whisper-env/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --quiet --upgrade pip

# Install Whisper
echo "📦 Installing OpenAI Whisper..."
pip install --quiet openai-whisper

# Check installation
echo ""
if python -c "import whisper; print(f'✅ Whisper version {whisper.__version__} installed successfully!')" 2>/dev/null; then
    echo ""
    echo "======================================"
    echo "Installation Complete!"
    echo "======================================"
    echo ""
    echo "Available models:"
    echo "  tiny    - 74 MB  (fastest, least accurate)"
    echo "  base    - 148 MB (good balance) ⭐"
    echo "  small   - 483 MB (better accuracy)"
    echo "  medium  - 1.5 GB (good accuracy)"
    echo "  large   - 3.1 GB (best accuracy)"
    echo ""
    echo "To use Whisper:"
    echo "  source whisper-env/bin/activate"
    echo "  whisper audio.wav --model base --language en"
    echo ""
    echo "Or use the batch processor:"
    echo "  ./batch-processor.sh /path/to/audio [model]"
else
    echo "❌ Installation failed. Please check errors above."
    exit 1
fi

# Deactivate environment
deactivate

# Check ffmpeg
echo ""
echo "Checking ffmpeg (required for audio processing)..."
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  ffmpeg not installed"
    echo "Install with: brew install ffmpeg"
    echo "(This may take a few minutes)"
else
    echo "✅ ffmpeg is installed"
fi

echo ""
echo "Ready to process audio files!"