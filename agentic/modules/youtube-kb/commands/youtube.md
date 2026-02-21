# YouTube Summarizer
> Summarize a YouTube video directly in chat and save to the knowledge base.

## Variables
url: $ARGUMENTS

## Instructions
- Run the 3-step pipeline: download → transcribe → compress
- Use `--prepare` mode so you (Claude Code) do the compression — no API key needed
- After compression, print the full summary in chat AND save it to the knowledge base
- If transcription quality is poor, retry with `--model small` or `--model large-v3`
- For edge cases (playlists, long videos, non-English), see `modules/youtube-kb/runbook/youtube_kb_extraction.md`

## Run
```bash
# Step 1: Download audio + metadata
./run modules/youtube-kb/tool/fetch_youtube_audio.py "$url"

# Step 2: Transcribe (use video_id from step 1 output)
./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/{video_id}/audio.mp3"

# Step 3: Prepare for compression (outputs JSON payload)
./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/{video_id}/transcript.txt" --prepare
```

## Compression

After step 3 outputs the JSON payload with `output_path`, `metadata`, and `transcript_path`:

1. Read the transcript file at `transcript_path`
2. Compress into a structured markdown KB entry:
   - YAML frontmatter: source, channel, title, date, duration, extracted
   - `## Executive Summary` — 2-3 sentence overview
   - `## Key Topics` — bullet list of main topics covered
   - `## Detailed Notes` — subsections per topic with key points
   - `## Key Quotes` — notable direct quotes from the video
   - `## Action Items / Takeaways` — actionable checklist items
3. Write the markdown to `output_path`
4. Print the full summary in chat so the user sees it immediately

Rules:
- Be concise but preserve all important information
- Use clear, scannable structure with headers
- Extract direct quotes that are particularly insightful
- Identify actionable takeaways
- Do NOT invent information not in the transcript
- Write in third person unless quoting directly

## Report
- Print the full summary directly in chat
- Confirm the KB entry was saved and show the file path
- Note transcript length and compression ratio
