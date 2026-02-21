# YouTube Knowledge Base Extraction

## When to Use
- Converting YouTube video content into searchable, structured notes
- Building a knowledge base from educational or technical video content
- Extracting key insights from long-form video content (lectures, podcasts, interviews)
- Processing multiple videos from a playlist into organized KB entries

**Trigger phrases:**
- "extract knowledge from this YouTube video"
- "transcribe and summarize this video"
- "add this video to the knowledge base"
- "youtube-kb"

## Overview

Three-step pipeline: download audio → transcribe locally → compress with Claude into structured markdown.

**Output:** Structured markdown KB entry in `knowledge-base/youtube/{channel}/{date}_{slug}.md`

## Tools

| Tool | Purpose |
|------|---------|
| `tool/fetch_youtube_audio.py` | Download audio + metadata from YouTube via yt-dlp |
| `tool/transcribe_audio.py` | Local transcription with faster-whisper (free, no API) |
| `tool/compress_to_kb.py` | Claude Sonnet summarization into structured markdown |

## Workflow

### Step 1: Download Audio

```bash
./run modules/youtube-kb/tool/fetch_youtube_audio.py "https://youtube.com/watch?v=VIDEO_ID"
```

**What happens:**
- Downloads audio-only as mp3 (via yt-dlp + ffmpeg)
- Extracts video metadata (title, channel, duration, description, upload date)
- Saves files to `.tmp/youtube-kb/{video_id}/`

**Outputs:**
- `.tmp/youtube-kb/{video_id}/audio.mp3`
- `.tmp/youtube-kb/{video_id}/metadata.json`
- JSON manifest printed to stdout

**For playlists:** Each video is processed sequentially. Failed videos are logged but don't stop the pipeline.

### Step 2: Transcribe Audio

```bash
./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/{video_id}/audio.mp3"
```

**What happens:**
- Loads the selected Whisper model (downloads on first run)
- Transcribes audio locally using faster-whisper with VAD filtering
- Auto-detects GPU (CUDA) or falls back to CPU with int8 quantization

**Outputs:**
- `.tmp/youtube-kb/{video_id}/transcript.txt`
- Output path printed to stdout

**Options:**
- `--model large-v3` — use a larger model for better accuracy
- `--timestamps` — include `[HH:MM:SS]` timestamps in output

### Step 3: Compress to Knowledge Base

**Option A — Claude Code compression (no API key needed, default):**
```bash
./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/{video_id}/transcript.txt" --prepare
```
This outputs a JSON payload. Claude Code reads the transcript and writes the KB entry itself using its own LLM capability. Used by the `/youtube-kb` slash command by default.

**Option B — API-based compression (requires ANTHROPIC_API_KEY or OPENAI_API_KEY):**
```bash
./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/{video_id}/transcript.txt"
```
Calls Claude Sonnet or GPT-4o directly. Auto-detects which provider has a valid key. For very long transcripts (4+ hours): chunks and merges summaries.

**What happens:**
- Reads transcript and metadata (auto-detects metadata.json in same directory)
- Compresses into structured KB markdown with frontmatter, summary, topics, notes, quotes, action items

**Outputs:**
- `knowledge-base/youtube/{channel_slug}/{date}_{video_slug}.md`
- Output path printed to stdout

## File Organization

```
.tmp/youtube-kb/
  {video_id}/
    audio.mp3           # Downloaded audio
    metadata.json       # Video metadata
    transcript.txt      # Raw transcript

knowledge-base/youtube/
  {channel-slug}/
    {date}_{video-slug}.md    # Structured KB entry
```

## Model Selection Guide

| Model | Download Size | RAM Usage | Speed (1hr video) | Accuracy | Best For |
|-------|--------------|-----------|-------------------|----------|----------|
| tiny | ~75MB | ~1GB | ~2 min | Basic | Quick previews, testing |
| base | ~150MB | ~1GB | ~5 min | Good | **Default — most videos** |
| small | ~500MB | ~2GB | ~10 min | Better | Important content |
| medium | ~1.5GB | ~5GB | ~20 min | High | Detailed notes needed |
| large-v3 | ~3GB | ~10GB | ~30 min | Best | Critical/technical content |

**Recommendation:** Start with `base`. Only upgrade to `small` or `large-v3` if transcription quality is insufficient. GPU (CUDA) gives ~4-10x speedup.

## Edge Cases

### Very Long Videos (4+ hours)
- Transcription works fine regardless of length
- `compress_to_kb.py` automatically chunks the transcript and merges summaries
- May use more Claude API tokens

### Playlists
- `fetch_youtube_audio.py` handles playlists automatically
- Each video gets its own subdirectory under `.tmp/youtube-kb/`
- Run transcription and compression for each video individually
- Failed downloads don't stop the pipeline

### Non-English Content
- faster-whisper auto-detects language
- Transcription works for 90+ languages
- Claude summarization works best in English — consider adding `--language` hint if needed

### Poor Audio Quality
- Use `--model large-v3` for better accuracy on noisy audio
- VAD filter automatically skips silence
- Very poor audio may produce unreliable transcripts — review before compressing

### Private/Age-Restricted Videos
- yt-dlp may fail on private or age-restricted videos
- For age-restricted: may need browser cookies (see yt-dlp docs)
- Error will be printed to stderr

### No ffmpeg Installed
- `fetch_youtube_audio.py` requires ffmpeg for audio extraction
- Install: `winget install ffmpeg` or `choco install ffmpeg`
- faster-whisper does NOT require ffmpeg separately

## Dependencies

**System:**
- ffmpeg (for yt-dlp audio extraction)

**Python (in requirements.txt):**
- `yt-dlp` — YouTube download
- `faster-whisper` — Local Whisper transcription
- `anthropic` — Claude API client
- `python-dotenv` — Environment variable loading

**Environment variables:**
- `ANTHROPIC_API_KEY` — For API-based compression (Claude Sonnet)
- `OPENAI_API_KEY` — Fallback for API-based compression (GPT-4o)
- `KB_LLM_PROVIDER` — Optional: force `anthropic` or `openai` (auto-detects by default)
- **No API key needed** when using `--prepare` mode (Claude Code does the compression itself)

## Example

```bash
# Full pipeline for a single video
./run modules/youtube-kb/tool/fetch_youtube_audio.py "https://youtube.com/watch?v=dQw4w9WgXcQ"
./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/dQw4w9WgXcQ/audio.mp3"
./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/dQw4w9WgXcQ/transcript.txt"

# Or use the slash command
/youtube-kb https://youtube.com/watch?v=dQw4w9WgXcQ
```
