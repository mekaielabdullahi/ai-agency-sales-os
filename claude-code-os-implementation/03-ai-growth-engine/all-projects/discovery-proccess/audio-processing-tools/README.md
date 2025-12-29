# Audio Processing Tools Library

A collection of reusable audio transcription and processing tools for client discovery calls and meetings.

## 🎯 Purpose

These tools help automate the transcription and analysis of client discovery calls, enabling efficient extraction of insights for AI audits and project scoping.

## 📁 Structure

```
audio-processing-tools/
├── README.md                     # This file
├── whisper-local/               # Local Whisper processing (no API)
│   ├── install-whisper.sh      # Setup script
│   ├── process-audio.py        # Python processor
│   └── batch-processor.sh      # Batch processing script
├── whisper-api/                 # OpenAI Whisper API
│   ├── api-processor.py        # API-based processing
│   └── compress-for-api.sh     # File compression utility
├── transcription-utils/         # Utility scripts
│   ├── merge-transcripts.py    # Combine multiple transcripts
│   ├── extract-insights.py     # Extract key points
│   └── format-transcript.py    # Format for readability
└── templates/                   # Reusable templates
    ├── discovery-analysis.md    # Discovery call template
    └── audit-insights.json      # Structured insights format
```

## 🚀 Quick Start

### Option 1: Local Whisper (Free, No API)
```bash
cd whisper-local
./install-whisper.sh
./batch-processor.sh /path/to/audio/files
```

### Option 2: OpenAI API (Fast, Requires Key)
```bash
export OPENAI_API_KEY='your-key'
cd whisper-api
python api-processor.py /path/to/audio/files
```

## 🔧 Features

### Core Capabilities
- ✅ Process WAV, MP3, MP4, M4A audio files
- ✅ Support for multiple speakers
- ✅ Batch processing of multiple files
- ✅ Automatic transcript merging
- ✅ Key insight extraction
- ✅ Python 3.13 compatibility

### Processing Options
| Method | Speed | Cost | Accuracy | Best For |
|--------|-------|------|----------|----------|
| Local Tiny | Fast | Free | 70% | Quick drafts |
| Local Base | Medium | Free | 85% | Standard calls |
| Local Large | Slow | Free | 95% | Critical content |
| API Whisper | Fast | ~$0.006/min | 90% | Production |

## 📊 Typical Workflow

1. **Record Discovery Call** → Multiple audio files
2. **Process with Whisper** → Individual transcripts
3. **Merge Transcripts** → Combined document
4. **Extract Insights** → Pain points, budget, timeline
5. **Update Audit** → Populate audit.json
6. **Generate Report** → Client deliverables

## 🎙️ Audio File Guidelines

### Optimal Settings
- **Format:** WAV or MP3
- **Sample Rate:** 16kHz-48kHz
- **Channels:** Mono preferred
- **Bitrate:** 64kbps+ for speech
- **File Size:** <25MB for API, unlimited for local

### Large File Handling
```bash
# Compress large WAV to MP3
ffmpeg -i input.wav -acodec mp3 -ab 64k output.mp3

# Split long recordings
ffmpeg -i input.wav -f segment -segment_time 1800 -c copy output%03d.wav
```

## 💡 Best Practices

### Recording Tips
1. Use separate audio tracks per speaker when possible
2. Minimize background noise
3. Test audio levels before important calls
4. Keep files under 2 hours for faster processing

### Processing Tips
1. Start with 'base' model for balance
2. Use 'tiny' for quick tests
3. Reserve 'large' for final versions
4. Process overnight for multiple files

### Organization Tips
1. Name files with speaker and timestamp
2. Keep originals separate from processed
3. Archive transcripts with project
4. Version control transcript edits

## 🔍 Common Issues & Solutions

### Issue: Python version incompatibility
**Solution:** Use Python 3.13 virtual environment
```bash
python3.13 -m venv whisper-env
source whisper-env/bin/activate
```

### Issue: Files too large for API
**Solution:** Compress first
```bash
ffmpeg -i large.wav -acodec mp3 -ab 64k small.mp3
```

### Issue: Poor transcription quality
**Solution:** Try larger model or clean audio
```bash
whisper audio.wav --model large --language en
```

### Issue: Out of memory
**Solution:** Use smaller model or process in chunks
```bash
whisper audio.wav --model tiny --fp16 False
```

## 📈 Performance Benchmarks

| File Size | Model | Processing Time | Accuracy |
|-----------|-------|----------------|----------|
| 100MB WAV | tiny | 10 min | 70% |
| 100MB WAV | base | 20 min | 85% |
| 100MB WAV | large | 60 min | 95% |
| 10MB MP3 | API | 30 sec | 90% |

## 🔗 Integration Examples

### With AI Audit System
```python
from audio_tools import process_discovery_call
from audit_tools import update_audit_json

# Process audio
transcripts = process_discovery_call("client_audio/")

# Extract insights
insights = extract_pain_points(transcripts)

# Update audit
update_audit_json("audit.json", insights)
```

### With Project Management
```bash
# Process client call
./process-client-call.sh "Plotter Mechanix" /path/to/audio

# Output goes to project folder
ls active-projects/plotter-mechanix/transcripts/
```

## 🚦 Tool Status

| Tool | Status | Version | Last Updated |
|------|--------|---------|--------------|
| Local Whisper | ✅ Active | 1.0 | 2025-12-08 |
| API Processor | ✅ Active | 1.0 | 2025-12-08 |
| Batch Processor | ✅ Active | 1.0 | 2025-12-08 |
| Insight Extractor | 🔄 In Dev | 0.5 | 2025-12-08 |

## 📝 License & Credits

- OpenAI Whisper: MIT License
- Scripts: Internal use
- Maintained by: AI Agency Development OS Team

---

**Need help?** Check individual tool READMEs or run with `--help` flag.