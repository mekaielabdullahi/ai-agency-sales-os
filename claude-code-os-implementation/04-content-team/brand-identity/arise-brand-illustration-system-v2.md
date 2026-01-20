# AriseGroup.ai Brand Illustration System v2.0

> **Design Thinking Output** | Created through empathy-driven process
> Solves: Inconsistency, Time, Quality, Decision Fatigue

---

## Quick Start: The 60-Second Decision

```
WHAT ARE YOU CREATING?
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│  Is it showing a SYSTEM, PROCESS, or TECHNICAL CONCEPT?    │
│  (automation, workflow, AI architecture, integrations)      │
└─────────────────────────────────────────────────────────────┘
         │ YES                              │ NO
         ▼                                  ▼
   ┌─────────────┐            ┌─────────────────────────────┐
   │  MODE 1:    │            │  Is it TELLING A STORY or   │
   │  SYSTEM     │            │  showing a RELATABLE SCENE? │
   │  (Isometric)│            │  (person working, journey)  │
   └─────────────┘            └─────────────────────────────┘
                                    │ YES           │ NO
                                    ▼               ▼
                              ┌───────────┐   ┌───────────┐
                              │  MODE 2:  │   │  MODE 3:  │
                              │ NARRATIVE │   │   ICON    │
                              │(Editorial)│   │  (Flat)   │
                              └───────────┘   └───────────┘
```

**Still unsure?** Default to **MODE 1: SYSTEM** - it's your hero style.

---

## The Three Modes

### MODE 1: SYSTEM (Primary - Use 60% of time)

**The "Hero" Style** - Isometric technical illustrations

| Attribute | Specification |
|-----------|---------------|
| **Perspective** | Isometric (30° angle) |
| **Outlines** | Black, 2-3px weight |
| **Colors** | Full warm palette |
| **Shadows** | Flat dark shapes |
| **Detail Level** | Medium-high |
| **Background** | Light: Cream / Dark: Deep navy |

**Use For:**
- AI workflows & automation
- Process diagrams
- System architecture
- Technical concepts
- Service explanations

**Reference:** Dribbble #3 (Factory with robot)

---

### MODE 2: NARRATIVE (Secondary - Use 25% of time)

**The "Story" Style** - Editorial line art with character

| Attribute | Specification |
|-----------|---------------|
| **Perspective** | Flat with implied depth |
| **Outlines** | Bold black, consistent weight |
| **Colors** | B&W + accent OR full palette |
| **Shadows** | Halftone textures optional |
| **Detail Level** | High, scene-based |
| **Background** | Light: Off-white / Dark: Charcoal |

**Use For:**
- Blog post headers
- Case study heroes
- Storytelling content
- Relatable work moments
- Team/culture content

**Reference:** Dribbble #2 (Bathtub working scene)

---

### MODE 3: ICON (Tertiary - Use 15% of time)

**The "Quick" Style** - Flat, minimal, fast

| Attribute | Specification |
|-----------|---------------|
| **Perspective** | Completely flat |
| **Outlines** | None (shape-defined) |
| **Colors** | Limited (3-4 max) |
| **Shadows** | Minimal or none |
| **Detail Level** | Low, simplified |
| **Background** | Solid color |

**Use For:**
- LinkedIn quick posts
- Simple concept visuals
- Icon sets
- Social media graphics
- Slide deck icons

**Reference:** Dribbble #1 (Potato illustration)

---

## Color System

### Light Mode Palette

| Color | Hex | CSS Variable | Use |
|-------|-----|--------------|-----|
| Warm Amber | `#E8914F` | `--arise-amber` | Primary accent, warmth |
| Gold | `#F5C26B` | `--arise-gold` | Highlights, success |
| Soft Teal | `#2D7D8A` | `--arise-teal` | Depth, trust |
| Purple | `#8B5CF6` | `--arise-purple` | Premium accent (new) |
| Deep Navy | `#1A2B4A` | `--arise-navy` | Text, outlines |
| Warm White | `#FEFDFB` | `--arise-bg-light` | Primary background |
| Soft Cream | `#FDF8F3` | `--arise-bg-cream` | Secondary background |

### Dark Mode Palette

| Color | Hex | CSS Variable | Use |
|-------|-----|--------------|-----|
| Deep Black | `#0D0D1A` | `--arise-bg-dark` | Primary background |
| Dark Surface | `#1A1A2E` | `--arise-surface-dark` | Card backgrounds |
| Purple Glow | `#8B5CF6` | `--arise-glow` | Primary accent |
| Magenta | `#D946EF` | `--arise-magenta` | Secondary glow |
| Warm Amber | `#E8914F` | `--arise-amber` | Warmth accent |
| Light Text | `#F5F5F5` | `--arise-text-dark` | Primary text |

### The Arise Glow Gradient

```css
/* Light Mode */
background: linear-gradient(90deg, #E8914F 0%, #F5C26B 50%, #2D7D8A 100%);

/* Dark Mode - with glow effect */
background: linear-gradient(90deg, #E8914F 0%, #8B5CF6 50%, #2D7D8A 100%);
filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.5));
```

---

## Recipe Cards

### Recipe Card #1: AI Audit Illustration

```
MODE: System (Isometric)
THEME: Light or Dark

FOCAL ELEMENT:
Magnifying glass examining a system diagram

SUPPORTING ELEMENTS:
- Organized flowchart beneath/through lens
- Glowing discovery points (use Arise Glow)
- Data nodes with connection lines
- Subtle checklist elements

COLORS:
- Magnifying glass: Navy frame, amber/gold lens glow
- System diagram: Teal nodes, navy connections
- Discoveries: Amber → Gold gradient glow
- Background: Warm white or deep black

PROMPT TEMPLATE:
"Warm tech isometric illustration of a magnifying glass examining
a stylized business system diagram. The magnifying glass reveals
glowing amber and gold insights. Clean black outlines, 2-3px weight.
Soft teal (#2D7D8A) for the system nodes, deep navy (#1A2B4A) for
connections. Cream background (#FDF8F3). Detailed but not cluttered.
Professional, approachable, premium feel."
```

### Recipe Card #2: Automation Workflow

```
MODE: System (Isometric)
THEME: Light or Dark

FOCAL ELEMENT:
Interconnected gears with flowing data

SUPPORTING ELEMENTS:
- Data particles flowing through system
- Input/output indicators
- Multiple gear sizes showing process stages
- Efficiency symbols

COLORS:
- Gears: Warm metallic (amber/gold tones)
- Data flow: Arise Glow gradient particles
- Connections: Teal lines
- Background: Cream or deep navy

PROMPT TEMPLATE:
"Warm tech isometric illustration of interconnected gears and
flowing automation processes. Data streams represented by glowing
amber (#E8914F) and gold (#F5C26B) particles flowing through the
system. Clean black outlines. Soft teal (#2D7D8A) connection lines.
Warm cream background. Friendly, efficient, not intimidating.
Detailed machinery with soft shadows."
```

### Recipe Card #3: Blog Story Header

```
MODE: Narrative (Editorial)
THEME: Light preferred

FOCAL ELEMENT:
Person in relatable work scenario

SUPPORTING ELEMENTS:
- Work environment details (desk, laptop, coffee)
- Floating icons showing digital activity
- Cat, plant, or quirky detail for personality
- Papers or sticky notes

COLORS:
- Line work: Black outlines throughout
- Accent color: Amber or Gold (pick one)
- Optional halftone: Gray for texture
- Background: Off-white

PROMPT TEMPLATE:
"Editorial line art illustration of a professional working at their
desk with a laptop. Black outlines, consistent weight. Minimal color -
just black, white, and amber (#E8914F) accents on key elements like
sticky notes. Include quirky details: coffee mug, small plant, papers.
Warm, relatable, slightly whimsical. Clean off-white background."
```

### Recipe Card #4: LinkedIn Quick Concept

```
MODE: Icon (Flat)
THEME: Light or Dark

FOCAL ELEMENT:
Single simplified object representing concept

SUPPORTING ELEMENTS:
- Minimal (1-2 supporting shapes max)
- No scene, just object

COLORS:
- 3 colors maximum from palette
- Shape-defined (no outlines)
- Solid fills, minimal gradients

PROMPT TEMPLATE:
"Flat minimal illustration of [OBJECT]. No outlines - shapes defined
by solid color fills only. Use only 3 colors: warm amber (#E8914F),
gold (#F5C26B), and deep navy (#1A2B4A). Geometric, simplified forms.
Clean cream background (#FEFDFB). Modern, friendly, app-style aesthetic."
```

---

## Component Library

### Objects (Use in illustrations)

| Object | Represents | Mode | Visual Notes |
|--------|------------|------|--------------|
| Magnifying Glass | Discovery, audit | System | Glowing lens, navy frame |
| Gears | Automation | System | Warm metallic, multiple sizes |
| Flowchart | Process | System | Teal nodes, navy lines |
| Compass | Strategy | System | Detailed face, amber needle |
| Graph (ascending) | Growth/ROI | System | Arise Glow gradient fill |
| Laptop | Work/digital | Narrative | Black outline, screen glow |
| Coffee Mug | Relatability | Narrative | Simple, maybe with face |
| Sticky Notes | Organization | Narrative | Amber/gold color |
| Robot (friendly) | AI partner | System | Rounded, warm colors |
| Shield | Security | System | Warm metallic, subtle glow |
| Lightbulb | Ideas | Icon | Simple, amber glow |
| Puzzle Pieces | Integration | Icon | Interlocking, brand colors |

### Characters

| Character | Use | Style Notes |
|-----------|-----|-------------|
| Friendly Robot | AI representation | Rounded shapes, warm colors (coral/amber), expressive |
| Stylized Human | Client/team | Geometric simplification, warm skin tones, confident posture |
| Mascot (TBD) | Brand personality | Could develop unique AriseGroup character |

### Backgrounds

| Background | Hex | When to Use |
|------------|-----|-------------|
| Warm White | `#FEFDFB` | Default light mode |
| Soft Cream | `#FDF8F3` | Light mode with more warmth |
| Light Blue | `#E8F4F8` | Technical/system focus |
| Deep Black | `#0D0D1A` | Dark mode |
| Dark Surface | `#1A1A2E` | Dark mode cards/layers |

---

## Prompt Library (Copy-Paste Ready)

### System Mode Prompts

**Generic System Illustration:**
```
Warm tech isometric illustration showing [SUBJECT]. Clean black outlines
(2-3px weight). Color palette: warm amber (#E8914F), gold (#F5C26B),
soft teal (#2D7D8A), deep navy (#1A2B4A). Cream background (#FDF8F3).
Soft flat shadows for grounding. Detailed but organized, not cluttered.
Professional and approachable. Premium digital illustration quality.

Do NOT include: cold blues, harsh shadows, threatening imagery,
photorealistic elements, cluttered chaos.
```

**Dark Mode System:**
```
Warm tech isometric illustration showing [SUBJECT] on dark background.
Clean black outlines with subtle glow effects. Color palette: amber
(#E8914F), purple (#8B5CF6), soft teal (#2D7D8A). Deep black background
(#0D0D1A) with subtle purple ambient glow. Glassmorphism effects on
surfaces. Premium, sophisticated, tech-forward but warm.

Do NOT include: cold sterile feeling, harsh contrast, threatening AI imagery.
```

### Narrative Mode Prompts

**Blog Header Scene:**
```
Editorial line art illustration of [SCENE DESCRIPTION]. Bold black
outlines throughout, consistent weight. Limited color: black, white,
and [ACCENT COLOR from palette]. High detail, storytelling composition.
Include small quirky details for personality. Off-white background.
Warm, relatable, slightly whimsical but professional.

Do NOT include: photorealistic elements, cold corporate feeling,
overwhelming complexity.
```

### Icon Mode Prompts

**Flat Icon:**
```
Flat minimal illustration of [OBJECT]. No outlines - shapes defined by
color only. Maximum 3-4 colors from: amber (#E8914F), gold (#F5C26B),
teal (#2D7D8A), navy (#1A2B4A). Geometric simplification. Clean solid
background. Modern app-style aesthetic. Friendly and clear.

Do NOT include: gradients, shadows, outlines, complex details.
```

---

## Quality Checklist

Before using any illustration, verify:

### Brand Alignment
- [ ] Uses approved color palette only
- [ ] Follows correct mode specifications
- [ ] Black outlines present (except Icon mode)
- [ ] Warm, not cold color temperature
- [ ] Professional but approachable mood

### Technical Quality
- [ ] Clean, crisp edges
- [ ] Appropriate resolution for use case
- [ ] No artifacts or noise
- [ ] Consistent line weights
- [ ] Proper contrast for readability

### Content Fit
- [ ] Matches the content topic
- [ ] Appropriate detail level for format
- [ ] Works at intended display size
- [ ] Complements rather than competes with text

---

## Team Onboarding

### Learning Path (30 minutes)

1. **Read this document** (10 min)
   - Focus on Decision Tree and 3 Modes

2. **Review Recipe Cards** (10 min)
   - Pick one relevant to your work
   - Note the prompt template

3. **Generate Test Image** (10 min)
   - Use a prompt from the library
   - Compare to reference images
   - Iterate if needed

### Quick Reference Card

```
┌────────────────────────────────────────────────┐
│         ARISEGROUP ILLUSTRATION MODES          │
├────────────────────────────────────────────────┤
│                                                │
│  MODE 1: SYSTEM    → Isometric + Outlines     │
│  (Technical)         Full colors, detailed     │
│                                                │
│  MODE 2: NARRATIVE → Editorial line art       │
│  (Stories)           B&W + accent, scenes      │
│                                                │
│  MODE 3: ICON      → Flat minimal             │
│  (Quick/Simple)      No outlines, 3-4 colors  │
│                                                │
├────────────────────────────────────────────────┤
│  COLORS: Amber #E8914F | Gold #F5C26B         │
│          Teal #2D7D8A  | Purple #8B5CF6       │
│          Navy #1A2B4A  | Cream #FDF8F3        │
├────────────────────────────────────────────────┤
│  DEFAULT: When unsure, use MODE 1 (System)    │
└────────────────────────────────────────────────┘
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Jan 2026 | Initial "Warm Tech" guidelines |
| 2.0 | Jan 2026 | Design Thinking rebuild: 3 modes, dark theme, prompt library, recipe cards |

---

*Created through Design Thinking process based on 5 reference images and team needs analysis.*
