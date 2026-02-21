# agentic-module-youtube-kb

YouTube knowledge base extractor — download, transcribe, and compress YouTube videos into structured markdown notes.

## Features

- Download audio from YouTube videos, playlists, or URL files via yt-dlp
- Local transcription with faster-whisper (no API cost, runs on CPU or GPU)
- Claude-powered summarization into structured knowledge base markdown
- Automatic file organization by channel and date

## Installation

```bash
# System dependency: ffmpeg (needed by yt-dlp for audio extraction)
# Windows: winget install ffmpeg  OR  choco install ffmpeg

# Python dependencies (into agentic venv):
pip install yt-dlp faster-whisper anthropic
```

## Environment Variables

```
ANTHROPIC_API_KEY=sk-ant-your-api-key
```

## Slash Commands

```
/youtube-kb https://youtube.com/watch?v=VIDEO_ID
```

## CLI Usage

```bash
# Step 1: Download audio + metadata
./run modules/youtube-kb/tool/fetch_youtube_audio.py "https://youtube.com/watch?v=ABC123"

# Step 2: Transcribe locally
./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/ABC123/audio.mp3"

# Step 3: Compress to knowledge base
./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/ABC123/transcript.txt" \
  --metadata ".tmp/youtube-kb/ABC123/metadata.json"

# With better model for accuracy
./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/ABC123/audio.mp3" --model large-v3

# With timestamps
./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/ABC123/audio.mp3" --timestamps

# Playlist
./run modules/youtube-kb/tool/fetch_youtube_audio.py "https://youtube.com/playlist?list=..."
```

## Workflow

1. Provide a YouTube URL (video or playlist)
2. Download audio with `/youtube-kb` or `fetch_youtube_audio.py`
3. Transcribe locally with `transcribe_audio.py`
4. Compress into structured KB entry with `compress_to_kb.py`
5. Find the output in `knowledge-base/youtube/{channel}/{date}_{slug}.md`

## Model Selection (Transcription)

| Model | Size | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| tiny | ~75MB | Fastest | Basic | Quick previews |
| base | ~150MB | Fast | Good | Default, most videos |
| small | ~500MB | Medium | Better | Important content |
| medium | ~1.5GB | Slow | High | Detailed notes needed |
| large-v3 | ~3GB | Slowest | Best | Critical/technical content |

## Output Structure

Generated KB entries include:
- YAML frontmatter (source, channel, date, duration)
- Executive summary
- Key topics list
- Detailed notes by topic
- Key quotes
- Action items / takeaways
