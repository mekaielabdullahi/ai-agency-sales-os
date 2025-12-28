# agentic-module-sop

Audio transcription and SOP extraction module for Agentic Workspaces.

## Features

- Transcribe audio files using OpenAI Whisper
- Extract structured SOPs from transcripts
- Convert interviews into actionable procedures
- Follow consistent SOP formatting standards

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-sop
```

## Environment Variables

```
OPENAI_API_KEY=sk-your-api-key
```

## Slash Commands

```
/transcribe path/to/audio.mp3
/extract-sop path/to/transcript.md "SOP Title"
```

## CLI Usage

```bash
# Transcribe audio
./run tools/transcribe_audio.py path/to/audio.mp3 --output transcript.md

# Extract SOP from transcript
./run tools/extract_sop.py path/to/transcript.md --title "Equipment Maintenance"
```

## Workflow

1. Record interview or process walkthrough
2. Transcribe with `/transcribe`
3. Extract SOP with `/extract-sop`
4. Review and refine the generated SOP
5. Export to Google Docs with `/md-to-gdoc` (requires md-export module)

## SOP Structure

Generated SOPs follow a consistent format:

- **Purpose**: What the SOP accomplishes
- **Scope**: When and where it applies
- **Procedure**: Step-by-step instructions
- **Edge Cases**: Exception handling
- **Revision History**: Version tracking
