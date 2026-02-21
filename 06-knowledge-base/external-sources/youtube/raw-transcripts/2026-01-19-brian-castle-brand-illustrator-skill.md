# Claude Code Skill: Brand Illustrator - Define Your Visual Brand Identity

**Channel**: Brian Castle / Builder Methods
**URL**: [YouTube - Builder Methods]
**Date Watched**: 2026-01-19
**Length**: ~25 minutes
**Why Watching**: Learning how to build a Claude Code skill for repeatable brand illustration generation

---

## Summary

Brian Castle walks through his process of creating a Claude Code skill that generates consistent brand illustrations. He initially over-engineered the solution with an N8N automation workflow (which took a week and produced poor results), then rebuilt it as a Claude Code skill in 30 minutes with better quality output.

## Key Concepts

### The Problem
- Need for consistent visual brand identity across dozens of images
- AI image generation is good for one-off images but lacks repeatability
- Complex prompts need to be recreated every time
- Manual process doesn't maintain brand aesthetic

### The Solution: Claude Code Skill Structure

```
/brand-illustrator/
├── skill.md              # Core skill definition (read by Claude Opus)
├── /assets/
│   ├── visual-world.md           # Subject matter/object definitions
│   ├── visual-style.md           # Aesthetic guidelines
│   ├── prompts.md                # Prompt templates
│   ├── idea-mapping.md           # Idea-to-illustration mapping guide
│   └── brand-colors.md           # Color definitions
├── /samples/                     # Sample illustrations for training
└── /scripts/
    └── generate.py               # Python script for Gemini API calls
```

### Three Key Artifacts from Brand Development

1. **Visual World Definition**
   - Defines the subject matter (what to illustrate)
   - "Day in the life of a builder" concept
   - Constant elements: home studio, notebook, mug, desk
   - Not about how things look, but what types of objects/scenes exist

2. **Idea-to-Illustration Mapping Guide**
   - Decision process for choosing what to illustrate
   - Takes content topic → suggests illustration concepts
   - Example: "prompt engineering" → "chat interface visual"
   - Example: "spec-driven development" → "blueprint/architectural drawing"

3. **Illustration Aesthetic Guidelines**
   - Locks in exactly how each illustration should look
   - Line thickness, color usage, level of detail
   - Style consistency across all images

### Skill.md Structure

The skill file instructs Claude Opus to:
- Create a project folder for each illustration (named by date)
- Generate 3 concept options
- Wait for user selection
- Reference color system, visual world, aesthetic style
- Execute Python script that hits Google Gemini API
- Save illustration takes to the project folder

### Why N8N Failed vs Claude Code Worked

**N8N Approach** (failed):
- Broke everything into discrete nodes and rigid logic
- Stripped away intelligence - model could only execute predefined steps
- Technically worked but output was garbage
- Complex Slack integration, conditional logic everywhere

**Claude Code Skill Approach** (succeeded):
- Model can actually reason about brand guidelines
- Understands intent and delivers what's needed
- Follows process while maintaining consistency
- Only took 30 minutes vs a week for N8N

### Workflow

1. Invoke skill: `/brand-illustrator`
2. Describe the content/context (e.g., "video about systems mindset, need hero image")
3. Choose color palette (brand colors)
4. Select dimensions
5. Receive 3 concept options (AI generates concepts based on mapping guide)
6. Select concept (A, B, or C)
7. AI generates image via Gemini API
8. Iterate with regeneration if needed
9. Post-process in Photoshop (transparency, light/dark mode versions)

### Key Insights

1. **Claude Code as Application**: Claude Code itself became the application - not building an app, but creating a workflow interface for a repeatable business process

2. **Intelligence Preservation**: The key difference is that Claude Code preserves the AI's reasoning ability while N8N's rigid node-based approach stripped it away

3. **Time Investment in Guidelines**: Significant time was spent developing the brand guidelines through long conversations with Claude before any automation

4. **Multi-Model Architecture**: Uses Claude Opus for interaction/prompting and Gemini API for actual image generation

5. **Iteration is Normal**: Expect to regenerate 3-5+ times to get the illustration just right (fine details, positioning, etc.)

## Technical Details

- **Python script** integrates with Google Gemini API (imageGen/nano)
- **API key** stored in .env file
- **Model**: Claude Opus 4.5 for skill execution
- **Image generation**: Google Gemini (they keep renaming it - imageGen, nano, banana)
- **Post-processing**: Photoshop for transparency and light/dark mode variants

## Applicable Learnings for AriseGroup.ai

### Immediate Applications
1. **Proposal Visuals**: Create consistent visual elements for client proposals
2. **Content Thumbnails**: LinkedIn posts, YouTube thumbnails with brand consistency
3. **Website Graphics**: Hero images, section illustrations
4. **Presentation Decks**: Google Slides visuals for sales presentations

### Implementation Approach
1. Define AriseGroup.ai visual world (what objects/scenes represent the brand)
2. Create aesthetic guidelines (style, colors, line weight, detail level)
3. Build idea-to-illustration mapping for AI agency content
4. Create Claude Code skill structure
5. Add Python script for Gemini API integration

### Skill Structure for AriseGroup.ai Brand Illustrator

Could include:
- **Visual world**: AI workflows, automation dashboards, client meetings, strategy sessions
- **Objects**: Laptops, flowcharts, handshakes, growth charts, gear icons
- **Aesthetic**: Professional, clean lines, brand colors (teal/blue?)
- **Mapping**: AI audit → magnifying glass on process, Automation → connected nodes/workflow

## Quotes

> "Claude code skills might be the most underrated feature in turning AI into repeatable business workflows."

> "I thought incorrectly that I could build in the intelligence into this [N8N] system... by breaking everything into discrete nodes and rigid logic, I stripped away the intelligence that makes AI actually useful."

> "The model couldn't think. It could only execute my predefined steps. But when I moved to the Claude Code skill, the model could actually reason about my brand guidelines."

---

## Source

- **Creator**: Brian Castle
- **Platform**: Builder Methods
- **Topic**: Claude Code Skills, Brand Identity, AI Image Generation
- **Date**: January 2026 (referenced Claude Code version 2.1.2)

---

*Transcript processed for AriseGroup.ai knowledge base - focuses on building repeatable visual brand systems using Claude Code skills*
