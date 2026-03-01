# AI Docs — Living AI Tools Reference

> Auto-updated by `/update-ai-docs`. Last scan: (run your first scan to populate)
> Sources: [LMArena](https://arena.ai) (Tier 1), [TTS Arena V2](https://tts-agi-tts-arena-v2.hf.space) (TTS), [Voice Writer](https://voicewriter.io) (STT) + OpenRouter pricing
> Daily cron detects ranking changes and updates only affected categories.

## Category Leaders

| Category | Leader | Provider | Score | Doc |
|----------|--------|----------|-------|-----|
| **Text LLMs** | (run first scan) | — | — | [text/state-of-the-art.md](text/state-of-the-art.md) |
| **Code** | — | — | — | [code/state-of-the-art.md](code/state-of-the-art.md) |
| **Vision** | — | — | — | [vision/state-of-the-art.md](vision/state-of-the-art.md) |
| **Text-to-Image** | — | — | — | [text-to-image/state-of-the-art.md](text-to-image/state-of-the-art.md) |
| **Image Edit** | — | — | — | [image-edit/state-of-the-art.md](image-edit/state-of-the-art.md) |
| **Search** | — | — | — | [search/state-of-the-art.md](search/state-of-the-art.md) |
| **Text-to-Video** | — | — | — | [text-to-video/state-of-the-art.md](text-to-video/state-of-the-art.md) |
| **Image-to-Video** | — | — | — | [image-to-video/state-of-the-art.md](image-to-video/state-of-the-art.md) |
| **Text-to-Speech** | — | — | — | [text-to-speech/state-of-the-art.md](text-to-speech/state-of-the-art.md) |
| **Speech-to-Text** | — | — | — | [speech-to-text/state-of-the-art.md](speech-to-text/state-of-the-art.md) |

## How This Works

Each category doc (`{category}/state-of-the-art.md`) contains:
- **Quick Pick table** — best model per use case with API IDs and pricing
- **Full Rankings** — top 10-15 models with ELO, vote count, pricing
- **Integration Notes** — API access, SDKs, key considerations
- **Trends** — what's changing in the category

The daily cron (`scripts/scanner.py`, 6:30 AM) pulls rankings from all sources, compares against the DB, and flags categories where rankings changed. Run `/update-ai-docs` to deep-dive changed categories with automated research.

**Tier 1** (8 categories): LMArena ELO scores from arena.ai
**Tier 2** (2 categories): TTS Arena V2 ELO scores (text-to-speech), Voice Writer WER % (speech-to-text)

## Changelog

| Date | Change |
|------|--------|
| — | Initial setup — run `/update-ai-docs` to populate all categories |
