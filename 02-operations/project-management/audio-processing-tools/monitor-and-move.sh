#!/bin/bash

# Monitor Whisper processing and automatically move completed transcripts
# to the Plotter Mechanix audit folder

WHISPER_OUTPUT="/Users/matthewkerns/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/audio-processing-tools/whisper-local/transcripts"
PLOTTER_AUDIT="/Users/matthewkerns/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/active-projects/plotter-mechanix/audit/transcripts"

echo "======================================"
echo "Auto-Moving Transcripts to Plotter Mechanix"
echo "======================================"
echo ""
echo "Source: $WHISPER_OUTPUT"
echo "Destination: $PLOTTER_AUDIT"
echo ""

# Create destination directory
mkdir -p "$PLOTTER_AUDIT"

# Monitor and move files as they appear
echo "📊 Monitoring for completed transcripts..."
echo "Press Ctrl+C to stop monitoring"
echo ""

MOVED_FILES=()

while true; do
    # Check for new transcript files
    for file in "$WHISPER_OUTPUT"/*.txt; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")

            # Check if we've already moved this file
            if [[ ! " ${MOVED_FILES[@]} " =~ " ${filename} " ]]; then
                echo "✅ Found new transcript: $filename"
                cp "$file" "$PLOTTER_AUDIT/"
                echo "   Moved to project folder"
                MOVED_FILES+=("$filename")
            fi
        fi
    done

    # Check for FULL-TRANSCRIPT.md
    if [ -f "$WHISPER_OUTPUT/FULL-TRANSCRIPT.md" ]; then
        if [[ ! " ${MOVED_FILES[@]} " =~ " FULL-TRANSCRIPT.md " ]]; then
            echo "✅ Found merged transcript: FULL-TRANSCRIPT.md"
            cp "$WHISPER_OUTPUT/FULL-TRANSCRIPT.md" "$PLOTTER_AUDIT/"
            echo "   Moved to project folder"
            MOVED_FILES+=("FULL-TRANSCRIPT.md")

            echo ""
            echo "======================================"
            echo "All transcripts appear to be complete!"
            echo "======================================"
            echo ""
            echo "📁 Files in Plotter Mechanix audit folder:"
            ls -lh "$PLOTTER_AUDIT/"*.txt "$PLOTTER_AUDIT/"*.md 2>/dev/null
            echo ""
            echo "✅ Transcripts successfully moved to:"
            echo "   $PLOTTER_AUDIT"
            echo ""
            echo "Next steps:"
            echo "1. Review transcripts"
            echo "2. Extract insights"
            echo "3. Update audit.json"
            break
        fi
    fi

    # Wait before checking again
    sleep 30
done