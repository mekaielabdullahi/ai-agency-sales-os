# AriseGroup.ai Brand Illustrator

A Claude Code skill for generating consistent, on-brand illustrations using the "Warm Tech" visual style.

## Overview

This skill enables repeatable generation of brand-consistent illustrations for:
- Blog thumbnails
- LinkedIn posts
- Case study heroes
- Presentation graphics
- Website visuals
- Proposal materials

## Quick Start

### 1. Install Dependencies

```bash
cd .claude/skills/brand-illustrator
pip install -r requirements.txt
```

### 2. Configure API Keys (Optional)

**No API key needed for testing!** Pollinations.ai works without any setup.

For production use or higher quality:
```bash
cp .env.example .env
# Edit .env and add your API keys (all optional)
```

Get API keys at:
- **Gemini**: https://aistudio.google.com/app/apikey
- **Hugging Face**: https://huggingface.co/settings/tokens (free)
- **Together AI**: https://api.together.xyz/settings/api-keys (free $5 credits)

### 3. Use the Skill

In Claude Code, invoke:
```
/brand-illustrator
```

Or describe what you need:
```
"I need a LinkedIn post illustration about AI automation"
```

## Skill Structure

```
brand-illustrator/
├── SKILL.md              # Core skill definition
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── .env.example          # API key template
├── .env                  # Your API key (create from example)
├── assets/
│   ├── visual-world.md   # What to illustrate (objects, scenes)
│   ├── aesthetic-style.md # How illustrations look (Warm Tech)
│   ├── color-palette.md  # Exact colors and gradients
│   ├── topic-mapping.md  # Topic → visual concept mapping
│   └── prompts.md        # Prompt templates
├── samples/              # Reference illustrations
├── projects/             # Generated illustration projects
└── scripts/
    └── generate.py       # Gemini API integration
```

## How It Works

1. **You describe** what you need (topic, format, context)
2. **Skill proposes** 3 illustration concepts based on brand guidelines
3. **You select** a concept (A, B, or C)
4. **Skill generates** the illustration using Gemini API
5. **You iterate** if needed (regenerate, adjust)

## Brand Guidelines Summary

### The "Warm Tech" Style

- Isometric or subtle 3D perspective
- Detailed but not cluttered
- Soft, diffused shadows
- Warm color temperature (amber, gold, teal)
- Professional but approachable

### Color Palette

| Color | Hex | Use |
|-------|-----|-----|
| Warm Amber | #E8914F | Primary accent |
| Gold | #F5C26B | Highlights |
| Soft Teal | #2D7D8A | Depth |
| Deep Navy | #1A2B4A | Structure |
| Warm White | #FEFDFB | Background |

### Arise Glow Gradient

`Amber (#E8914F) → Gold (#F5C26B) → Soft Teal (#2D7D8A)`

## Supported Formats

| Format | Dimensions | Use Case |
|--------|------------|----------|
| Blog Thumbnail | 1200 x 630 | Article headers |
| LinkedIn Square | 1080 x 1080 | Feed posts |
| LinkedIn Landscape | 1200 x 627 | Wide posts |
| Case Study Hero | 1920 x 1080 | Headers |
| Presentation | 1920 x 1080 | Slides |
| Website Section | 1200 x 800 | Web pages |

## Image Generation Providers

The skill supports multiple providers with automatic fallback:

| Provider | API Key | Models | Best For |
|----------|---------|--------|----------|
| **Gemini** | Required | 2.0 Flash | High quality, paid |
| **Pollinations** | None! | Flux | Free testing, no setup |
| **Hugging Face** | Optional | FLUX, SDXL, SD 1.5 | Free tier, many models |
| **Together AI** | Required | FLUX Schnell | Free $5 credits |

### Provider Selection

```bash
# Quick test - no API key needed!
python scripts/generate.py --project "test" --provider pollinations --prompt-text "A robot"

# Auto mode (default): Try all providers in order
python scripts/generate.py --project "test" --provider auto

# Force specific provider
python scripts/generate.py --project "test" --provider gemini
python scripts/generate.py --project "test" --provider huggingface
python scripts/generate.py --project "test" --provider together
```

### Fallback Order (Auto Mode)

1. **Gemini** (if GEMINI_API_KEY set)
2. **Pollinations** (always available, no key)
3. **Hugging Face** (always available, key optional)
4. **Together AI** (if TOGETHER_API_KEY set)

## Manual Generation

You can also run the script directly:

```bash
python scripts/generate.py \
  --project "2026-01-19-my-illustration" \
  --width 1080 \
  --height 1080 \
  --prompt-text "Your prompt here"
```

Or with a prompt file:

```bash
python scripts/generate.py \
  --project "2026-01-19-my-illustration" \
  --prompt "path/to/prompt.md"
```

With free provider (no setup):

```bash
# Use Pollinations - works immediately, no API key!
python scripts/generate.py \
  --project "2026-01-19-my-illustration" \
  --provider pollinations \
  --prompt-text "Your prompt here"
```

## Troubleshooting

### "No image generated"
- Try `--provider pollinations` (free, no API key needed)
- Check your internet connection
- If using Gemini, verify API quota hasn't been exceeded

### "Hugging Face models loading"
- Wait 20-30 seconds and try again
- Set HF_API_KEY for higher rate limits

### "Module not found"
Run `pip install -r requirements.txt`

## Adding Sample Illustrations

As you create illustrations you're happy with:

1. Copy approved images to `samples/` folder
2. These become style references for future generation
3. Helps maintain consistency over time

## Credits

Based on the brand illustrator skill pattern from Brian Castle (Builder Methods).
Adapted for AriseGroup.ai brand guidelines.
