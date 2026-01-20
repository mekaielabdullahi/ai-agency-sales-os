---
name: brand-illustrator
description: Generate complete branded content for AriseGroup.ai - illustrations, post copy, hashtags, and CTAs in the "Warm Tech" style. Creates ready-to-post content packages for LinkedIn, blogs, case studies, and presentations.
---

# AriseGroup.ai Brand Content Generator

## Purpose

Generate complete, on-brand content packages for AriseGroup.ai using the "Warm Tech" visual style and brand voice. This skill produces:
- **Illustration** - Consistent visual in brand style
- **Post Copy** - 2-3 caption variations following brand voice
- **Hashtags** - Strategic tags for discovery
- **CTA** - Engagement prompt matched to content type
- **Content Canvas** - Everything combined in Excalidraw for review

## When to Use This Skill

- Creating LinkedIn posts (visual + copy + hashtags)
- Blog post thumbnails with social promotion copy
- Case study hero images with announcement text
- Presentation graphics
- Any content requiring brand-consistent visual + copy

---

## Skill Workflow

### Phase 1: Project Setup

When invoked, ALWAYS:

1. Create a new project folder in `projects/` named with today's date and a short descriptor:
   ```
   projects/YYYY-MM-DD-[short-topic-name]/
   ```

2. Ask the user for:
   - **Content context**: What is this for? (LinkedIn, blog, case study, etc.)
   - **Topic/subject**: What concept or message should it convey?
   - **Format**: What dimensions? (offer recommendations based on use case)
   - **Goal**: Engagement, education, announcement, or conversion?

### Phase 2: Concept Development

1. Read and internalize visual assets:
   - `assets/visual-world.md` - Objects/scenes in the Arise visual world
   - `assets/topic-mapping.md` - Topic to visual concept mapping
   - `assets/aesthetic-style.md` - "Warm Tech" style guidelines

2. Generate **3 illustration concepts** based on the topic:
   - Each concept should have a clear focal point
   - Each should map to objects/scenes from the visual world
   - Each should work with the specified format

3. Present concepts to user:
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

### Phase 3: Image Generation

Once concept is selected:

1. Read `assets/color-palette.md` for exact color specifications
2. Read `assets/prompts.md` for prompt structure and templates
3. Assemble the generation prompt
4. Save the assembled prompt to the project folder as `prompt.md`

5. Run the generation script with Excalidraw output:
   ```bash
   python scripts/generate.py --project "[project-folder-name]" --provider pollinations --excalidraw --width 1080 --height 1080
   ```

6. If prompt is too long for Pollinations, use a condensed version via `--prompt-text`

### Phase 4: Copy Generation

**NEW - Generate post copy alongside the illustration.**

1. Read content assets:
   - `assets/brand-voice.md` - Tone, personality, language guidelines
   - `assets/post-templates.md` - Post structures and formulas
   - `assets/hashtag-strategy.md` - Hashtag tiers and combinations
   - `assets/cta-library.md` - Engagement and conversion CTAs

2. Select appropriate template based on:
   - Content type (insight, story, how-to, myth-buster, engagement, announcement)
   - Goal (engagement, education, conversion)
   - Topic mapping from `post-templates.md`

3. Generate **2-3 post copy variations**:
   ```
   COPY A: [Template name]
   ---
   [Full post text]

   [Hashtags]
   ---

   COPY B: [Template name]
   ---
   [Full post text]

   [Hashtags]
   ---

   COPY C: [Shorter/alternative version]
   ---
   [Full post text]

   [Hashtags]
   ---
   ```

4. Each variation should include:
   - Hook (first line that stops the scroll)
   - Body (value, insight, or story)
   - CTA (engagement prompt)
   - Hashtags (3-5 strategic tags including #AriseWithAI)

5. Save all copy to `post-copy.md` in the project folder

### Phase 5: Review Options

Create Excalidraw canvas with all copy options for initial review:

```bash
python scripts/create_canvas.py --project "[project-folder-name]"
```

User reviews Copy A, B, C and selects their favorite.

### Phase 6: Generate Final Preview

Once user selects a copy variation (A, B, or C):

```bash
python scripts/create_preview.py --project "[project-folder-name]" --copy A
```

This generates `linkedin-preview-a.png` - a LinkedIn post mockup showing exactly how the post will appear, ready for team approval.

### Phase 7: Team Approval (Optional)

Send the preview to Slack for team sign-off:

```bash
python scripts/send_for_approval.py --project "[project-folder-name]" --copy A --channel "#content-review"
```

Team can respond with:
- ✅ Approved
- ✏️ Needs changes
- ❌ Reject

### Phase 8: Post to LinkedIn

Once approved:

1. Open `post-copy.md` and copy the selected variation text
2. Go to LinkedIn → Start a post
3. Upload the image (`v1.png`)
4. Paste the copy
5. **Schedule or Post** using LinkedIn's native scheduler

### Iteration

If changes needed at any point:

1. **Image refinements**: Modify prompt, regenerate as v2, v3, etc.
2. **Copy refinements**: Edit post-copy.md directly
3. **Regenerate preview**: Run create_preview.py again

---

## Output Files

Each project generates:

```
projects/YYYY-MM-DD-topic-name/
├── prompt.md                    # Image generation prompt
├── post-copy.md                 # All copy variations (A, B, C)
├── v1.png                       # Generated illustration
├── v1.excalidraw                # Image in Excalidraw
├── v1_metadata.txt              # Generation info
├── content-canvas.excalidraw    # Review canvas (all options)
└── linkedin-preview-a.png       # Final preview mockup (selected copy)
```

---

## Reference Files

### Visual Assets
- `assets/visual-world.md` - What to illustrate
- `assets/aesthetic-style.md` - How illustrations look
- `assets/color-palette.md` - Exact colors and gradients
- `assets/topic-mapping.md` - Topic → visual mapping
- `assets/prompts.md` - Image prompt templates

### Content Assets
- `assets/brand-voice.md` - Tone, personality, language
- `assets/post-templates.md` - LinkedIn post structures
- `assets/hashtag-strategy.md` - Hashtag tiers and formulas
- `assets/cta-library.md` - Engagement and conversion CTAs

---

## Format Recommendations

| Use Case | Dimensions | Aspect Ratio |
|----------|------------|--------------|
| LinkedIn post (square) | 1080 x 1080 | 1:1 |
| LinkedIn post (landscape) | 1200 x 627 | 1.91:1 |
| Blog thumbnail | 1200 x 630 | 1.91:1 |
| Case study hero | 1920 x 1080 | 16:9 |
| Presentation slide | 1920 x 1080 | 16:9 |
| Website section | 1200 x 800 | 3:2 |

---

## Post Template Quick Reference

| Content Goal | Best Template | From |
|--------------|---------------|------|
| Share insight | Observation, Contrast | post-templates.md |
| Tell client story | Client Win, Lesson Learned | post-templates.md |
| Challenge myth | The Truth About | post-templates.md |
| Teach something | Quick Guide | post-templates.md |
| Spark discussion | Poll/Question, Unpack This | post-templates.md |
| Announce offer | Soft Launch | post-templates.md |

---

## Quality Checklists

### Illustration Checklist
- [ ] Uses Arise color palette (Amber, Gold, Soft Teal)
- [ ] Follows "Warm Tech" aesthetic
- [ ] Has clear focal point
- [ ] Composition works for format
- [ ] Soft shadows, warm atmosphere

### Copy Checklist
- [ ] Hook stops the scroll (first line compelling)
- [ ] Value clear (insight, story, or practical tip)
- [ ] Sounds human (not generic AI-written)
- [ ] CTA invites engagement
- [ ] Hashtags strategic (3-5, includes #AriseWithAI)

### Content Canvas Checklist
- [ ] Image displays correctly
- [ ] All copy variations included
- [ ] Hashtags visible and grouped
- [ ] Ready for review and posting

---

## Environment Setup

**Python packages:**
```bash
pip install google-generativeai requests python-dotenv Pillow
```

**API Keys** (in `.env` - all optional):
```
GEMINI_API_KEY=
HF_API_KEY=
TOGETHER_API_KEY=
```

**Quick Start:** No setup needed! Use `--provider pollinations` for free image generation.

---

## Example Invocation

**User:** "I need a LinkedIn post about business efficiency"

**Skill Response:**
1. Creates `projects/2026-01-20-business-efficiency-linkedin/`
2. Proposes 3 visual concepts (e.g., transformation view, gears, time savings)
3. User selects concept C
4. Generates illustration with Excalidraw
5. Generates 2-3 post copy variations with hashtags
6. Creates content canvas with everything
7. User reviews, tweaks if needed, posts

**Output:**
- `v1.png` - Ready-to-post image
- `post-copy.md` - Copy options to choose from
- `content-canvas.excalidraw` - Visual review canvas

---

**Ready to create content?**

Tell me:
1. What platform is this for? (LinkedIn, blog, etc.)
2. What topic or concept should it convey?
3. What's the goal? (engagement, education, announcement)
