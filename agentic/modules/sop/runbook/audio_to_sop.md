# Audio to SOP Extraction

## When to Use
- You have an audio recording of an expert explaining a procedure
- You need to create documentation that can be handed off to clients or technicians
- You want to capture tribal knowledge in a structured, reusable format

**Trigger phrases:**
- "transcribe this audio"
- "extract an SOP from this recording"
- "turn this audio into documentation"
- "create an SOP from this call"

## Overview
This workflow converts audio recordings (phone calls, mic recordings, training sessions) into structured Standard Operating Procedures (SOPs).

**Output:**
- Raw transcript (archived alongside audio file)
- Markdown SOP (internal reference)
- Google Doc SOP (client-facing)

## Tools
| Tool | Purpose |
|------|---------|
| `tools/transcribe_audio.py` | Transcribe audio using OpenAI Whisper |
| `tools/extract_sop.py` | Extract structured SOP from transcript |

## Workflow

### Step 1: Transcribe the Audio
```bash
./run tools/transcribe_audio.py "path/to/recording.mp3"
```

**What happens:**
- Audio is sent to OpenAI Whisper API
- Large files (>25MB) are automatically chunked
- Transcript saved as `{filename}_transcript.txt` in same directory

**Outputs:**
- `{filename}_transcript.txt` - Raw transcription

### Step 2: Identify Topics (Optional)
If the recording covers multiple topics or you're unsure what SOPs can be extracted:

```bash
./run tools/extract_sop.py "path/to/transcript.txt" --list-topics
```

**What happens:**
- GPT-4 analyzes the transcript
- Returns list of potential SOP topics with confidence levels

### Step 3: Extract the SOP
```bash
./run tools/extract_sop.py "path/to/transcript.txt" --topic "topic name"
```

**Options:**
- `--title "Custom Title"` - Override the SOP title
- `--no-gdoc` - Skip Google Doc creation
- `--output path/to/output.md` - Custom output path

**Outputs:**
- `{filename}_sop.md` - Markdown SOP with metadata (internal)
- Google Doc - Clean SOP without metadata (client-facing)

## File Organization

After processing, files will be organized as:
```
recording.mp3                 # Original audio (preserved)
recording_transcript.txt      # Raw transcript (archived)
recording_sop.md              # Extracted SOP (Markdown)
```

Plus a Google Doc in Drive for client delivery.

## Edge Cases

### Large Audio Files
Files over 25MB are automatically split into chunks for transcription. The script handles this transparently - you'll see progress messages for each chunk.

**Requires:** `pydub` and `ffmpeg` installed
```bash
pip install pydub
brew install ffmpeg  # macOS
```

### Multiple Speakers
The extraction handles multi-speaker conversations by:
1. Identifying the expert/instructor voice
2. Focusing on procedural content
3. Ignoring casual conversation and off-topic discussion

### Incomplete Procedures
If the recording doesn't cover a complete procedure, the SOP will be marked with:
- `completeness: partial` or `completeness: minimal`
- Notes about what information is missing

Review these SOPs before distributing.

### Poor Audio Quality
Whisper handles most audio quality issues well, but if transcription is poor:
- Check the raw transcript for errors
- Consider re-recording with better audio
- Edit the transcript manually before SOP extraction

### Multiple SOPs from One Recording
Run `--list-topics` first, then extract each topic separately:
```bash
./run tools/extract_sop.py "transcript.txt" --topic "first procedure" --output "first_sop.md"
./run tools/extract_sop.py "transcript.txt" --topic "second procedure" --output "second_sop.md"
```

## Tips for Better Results

### Recording Quality
- Use a good microphone
- Minimize background noise
- Have the expert speak clearly and at moderate pace
- Ask the expert to verbalize all steps, even "obvious" ones

### During Recording
- Start by stating what procedure is being documented
- Have someone ask clarifying questions
- Ask about common mistakes and troubleshooting
- Request specific measurements, settings, and timing

### After Extraction
- Always review the generated SOP
- Fill in any gaps marked as incomplete
- Add photos or diagrams if helpful
- Test the SOP with someone unfamiliar with the procedure

## Dependencies

Required in `requirements.txt`:
```
openai
google-api-python-client
google-auth-httplib2
google-auth-oauthlib
```

Required system tools:
- `ffmpeg` (for audio chunking): `brew install ffmpeg`

Required credentials:
- `OPENAI_API_KEY` in `.env`
- `credentials.json` for Google Docs (optional)

---

## Related Directives

- `writing_sops.md` - SOP formatting guidelines (Mermaid diagrams, structure)
- `markdown_to_gdoc.md` - Convert extracted SOP to Word document

---

## SOP Pipeline

This directive is the first step in the SOP creation workflow:

```
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│  audio_to_sop   │ ──► │   writing_sops   │ ──► │ markdown_to_gdoc  │
│  (create SOP)   │     │  (format rules)  │     │ (export to Word)  │
└─────────────────┘     └──────────────────┘     └───────────────────┘
        │                        │                        │
   Input: Audio            Reference: How          Output: .docx
   Output: .md             SOPs should look        with diagrams
```

**After extraction:**
1. Review the generated Markdown SOP
2. Add Mermaid diagrams for decision flows (see `writing_sops.md`)
3. Convert to Word document using `md_to_docx.py`

---

## Example

```bash
# 1. Transcribe the recording
./run tools/transcribe_audio.py "Kelce Mic-Dec-3.mp3"
# Output: Kelce Mic-Dec-3_transcript.txt

# 2. See what topics are covered
./run tools/extract_sop.py "Kelce Mic-Dec-3_transcript.txt" --list-topics
# Output: List of topics like "Laminator Setup", "Paper Loading", etc.

# 3. Extract the SOP you need
./run tools/extract_sop.py "Kelce Mic-Dec-3_transcript.txt" --topic "laminator setup" --title "Laminator Setup Guide"
# Output: Kelce Mic-Dec-3_sop.md + Google Doc URL
```
