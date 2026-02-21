# YouTube Knowledge Base Extraction
> Extract knowledge from a YouTube video into a structured markdown KB entry.

## Variables
url: $1

## Instructions
- Read the runbook at `modules/youtube-kb/runbook/youtube_kb_extraction.md` for edge cases
- Run the 3-step pipeline sequentially: download → transcribe → compress
- For playlists, process each video through all 3 steps
- If transcription quality is poor, retry with `--model small` or `--model large-v3`
- The metadata file is auto-detected by compress_to_kb.py if in the same directory

## Run
```bash
# Step 1: Download audio + metadata
./run modules/youtube-kb/tool/fetch_youtube_audio.py "$url"

# Step 2: Transcribe (parse video_id from step 1 output)
./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/{video_id}/audio.mp3"

# Step 3: Compress to KB (use --prepare mode for Claude Code to do compression)
./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/{video_id}/transcript.txt" --prepare
```

## Step 3 — Claude Code Compression

When using `--prepare`, the script outputs a JSON payload with `output_path`, `metadata`, and `transcript_path`. You (Claude Code) then:

1. Parse the JSON from stdout
2. Read the transcript file at `transcript_path`
3. Compress the transcript into a structured KB markdown entry with these sections:
   - YAML frontmatter: source, channel, title, date, duration, extracted
   - `## Executive Summary` — 2-3 sentence overview
   - `## Key Topics` — bullet list of main topics
   - `## Detailed Notes` — subsections per topic with key points
   - `## Key Quotes` — notable direct quotes from the video
   - `## Action Items / Takeaways` — actionable checklist items
4. Write the markdown to the `output_path` from the JSON

Rules for compression:
- Be concise but preserve all important information
- Use clear, scannable structure with headers
- Extract direct quotes that are particularly insightful
- Identify actionable takeaways
- Do NOT invent information not in the transcript
- Write in third person unless quoting directly

### Fallback: API mode
If the user has `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` with credits, step 3 can run without `--prepare`:
```bash
./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/{video_id}/transcript.txt"
```

## Report
- Confirm the KB entry was created
- Report the output file path
- Summarize the key topics extracted
- Note the transcript length and compression ratio
