---
name: brand-illustrator
description: Generate consistent brand illustrations for AriseGroup.ai using the "Warm Tech" style. Creates on-brand visuals for blog thumbnails, LinkedIn posts, case studies, and presentations.
---

# AriseGroup.ai Brand Illustrator Skill

## Purpose

Generate consistent, on-brand illustrations for AriseGroup.ai content using the "Warm Tech" visual style. This skill ensures every illustration follows brand guidelines while allowing creative flexibility for different topics and formats.

## When to Use This Skill

- Creating blog post thumbnails
- LinkedIn post visuals
- Case study hero images
- Presentation graphics
- Website section illustrations
- Proposal visuals
- Any content requiring brand-consistent imagery

## Skill Workflow

### Phase 1: Project Setup

When invoked, ALWAYS:

1. Create a new project folder in `projects/` named with today's date and a short descriptor:
   ```
   projects/YYYY-MM-DD-[short-topic-name]/
   ```

2. Ask the user for:
   - **Content context**: What is this illustration for? (blog, LinkedIn, case study, etc.)
   - **Topic/subject**: What concept or message should the illustration convey?
   - **Format**: What dimensions? (offer recommendations based on use case)

### Phase 2: Concept Development

1. Read and internalize:
   - `assets/visual-world.md` - What objects/scenes exist in the Arise visual world
   - `assets/topic-mapping.md` - How to map topics to visual concepts
   - `assets/aesthetic-style.md` - The "Warm Tech" style guidelines

2. Generate **3 illustration concepts** based on the topic:
   - Each concept should have a clear focal point
   - Each should map to objects/scenes from the visual world
   - Each should work with the specified format

3. Present concepts to user in this format:
   ```
   CONCEPT A: [Name]
   → Focal element: [main visual]
   → Supporting elements: [secondary visuals]
   → Composition: [layout description]
   → Mood: [emotional tone]

   CONCEPT B: [Name]
   ...

   CONCEPT C: [Name]
   ...
   ```

4. Wait for user selection (A, B, C, or request refinement)

### Phase 3: Prompt Assembly

Once concept is selected:

1. Read `assets/color-palette.md` for exact color specifications
2. Read `assets/prompts.md` for prompt structure and templates
3. Read `assets/aesthetic-style.md` for style enforcement rules

4. Assemble the generation prompt following this structure:
   ```
   [Style foundation from aesthetic-style.md]
   [Color specifications from color-palette.md]
   [Specific concept details from user selection]
   [Format/dimension specifications]
   [Quality and detail requirements]
   ```

5. Save the assembled prompt to the project folder as `prompt.md`

### Phase 4: Image Generation

1. Run the generation script:
   ```bash
   python scripts/generate.py --project "[project-folder-name]" --prompt "[prompt-file-path]"
   ```

2. The script will:
   - Read the prompt from the project folder
   - Call the Gemini API
   - Save the generated image to the project folder as `v1.png`

3. Present the result to the user

### Phase 5: Iteration

If the user wants refinements:

1. Ask what should change (composition, colors, elements, detail level)
2. Modify the prompt accordingly
3. Regenerate as `v2.png`, `v3.png`, etc.
4. Continue until user is satisfied

## Format Recommendations

When user asks for format guidance, recommend:

| Use Case | Dimensions | Aspect Ratio |
|----------|------------|--------------|
| Blog thumbnail | 1200 x 630 | 1.91:1 |
| LinkedIn post (square) | 1080 x 1080 | 1:1 |
| LinkedIn post (landscape) | 1200 x 627 | 1.91:1 |
| Case study hero | 1920 x 1080 | 16:9 |
| Presentation slide | 1920 x 1080 | 16:9 |
| Website section | 1200 x 800 | 3:2 |

## Reference Files

Always consult these files during generation:

- **Visual World**: `assets/visual-world.md`
- **Aesthetic Style**: `assets/aesthetic-style.md`
- **Color Palette**: `assets/color-palette.md`
- **Topic Mapping**: `assets/topic-mapping.md`
- **Prompt Templates**: `assets/prompts.md`
- **Sample Images**: `samples/` (reference for style consistency)

## Quality Checklist

Before presenting final illustration, verify:

- [ ] Uses Arise color palette (Amber, Gold, Soft Teal gradient)
- [ ] Follows "Warm Tech" aesthetic (detailed but warm)
- [ ] Has clear focal point appropriate to topic
- [ ] Composition works for specified format
- [ ] No cold blues/grays (unless intentionally contrasting)
- [ ] Soft shadows, not harsh
- [ ] Appropriate level of detail (not cluttered, not sparse)

## Environment Setup

The generation script requires:

1. **Google Gemini API key** in environment variable `GEMINI_API_KEY` or in `.env` file
2. **Python packages**: `google-generativeai`, `python-dotenv`, `Pillow`

To set up:
```bash
pip install google-generativeai python-dotenv Pillow
```

Create `.env` file in the skill folder with:
```
GEMINI_API_KEY=your_api_key_here
```

## Example Invocation

User: "I need an illustration for a LinkedIn post about how AI audits help businesses identify automation opportunities"

Skill response:
1. Creates `projects/2026-01-19-ai-audit-linkedin/`
2. Proposes 3 concepts based on AI Audits mapping (magnifying glass + system diagram)
3. User selects concept
4. Generates image using Gemini API
5. Saves to project folder
6. Iterates if needed

---

**Ready to create an illustration?**

Tell me:
1. What is this illustration for? (blog, LinkedIn, case study, etc.)
2. What topic or concept should it convey?
3. Any specific requirements or preferences?
