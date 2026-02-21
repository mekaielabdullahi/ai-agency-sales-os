# UI Mockup Notes for v0.app Generation

**Purpose:** Prompt and design guidance for generating Agency Operations Dashboard UI in v0.app
**Target:** Phase 1 MVP (Tab 1: Projects & Revenue)
**Created:** December 25, 2025

---

## v0.app Prompt (Primary)

### Initial Prompt

```
Create a React dashboard with Tailwind CSS for an agency operations management tool.

LAYOUT:
- Clean header with "Agency Operations Dashboard" title (left-aligned, large, bold)
- Horizontal tab navigation bar with 7 tabs below header
- Main content area below tabs

TAB NAVIGATION:
- 7 tabs (horizontal): "Projects & Revenue", "Client Process", "Opportunity Matrix", "Pricing", "Objectives", "Dev Kanban", "Validation"
- Active tab has blue underline indicator
- Inactive tabs are gray, clickable
- Smooth transitions between tabs

TAB 1 CONTENT (Projects & Revenue):
The main view should have three sections:

1. REVENUE SUMMARY (top, full width):
   - White card with shadow
   - 3 stat columns in a row:
     * "Received (YTD)" - Large green number ($12,500)
     * "Projected" - Large gray number ($21,500)
     * "Total Potential" - Large blue number ($34,000)
   - Small gray label above each number
   - Equal width columns

2. FILTER BAR (below revenue summary):
   - Left side: "All Projects" text (current filter)
   - Right side: Two dropdown buttons:
     * "Priority" dropdown (All, P0, P1, P2)
     * "Status" dropdown (All, In Progress, Complete, Blocked)
   - Clean, minimal styling

3. PROJECT GRID (main content):
   - 3 columns on desktop (responsive: 2 on tablet, 1 on mobile)
   - Grid gap of 24px
   - Each project card should be a white card with:
     * Colored left border (4px thick) - color indicates risk level:
       - Red = High risk
       - Yellow = Medium risk
       - Green = Low risk
     * Card shadow for depth
     * Rounded corners
     * Padding inside card

PROJECT CARD LAYOUT (each card):
- Top section:
  * Project name (left, large, bold, dark text)
  * Status dot (right, aligned) - colored circle:
    - Green dot = On track
    - Yellow dot = At risk
    - Red dot = Critical/Blocked
    - Blue check = Complete

- Client name (below project name, smaller, gray text)

- Badges section:
  * Phase badge (light blue background, dark blue text, rounded) - "Quick Win", "Phase 2", etc.
  * Priority badge (light purple background, dark purple text, rounded, margin-left) - "P0", "P1", etc.

- Revenue section (border-top, padding-top):
  * Two rows:
    - "Received:" label (left, gray) → Dollar amount (right, bold, green text)
    - "Projected:" label (left, gray) → Dollar amount (right, bold, gray text)

- Footer section:
  * Deadline date (small, gray text)
  * Risk warning if high risk (small, red text with warning icon) - "⚠️ Late delivery = lose ALL future revenue"

DESIGN STYLE:
- Professional, clean, minimal
- Use Tailwind default color palette
- Adequate spacing and padding (not cramped)
- Good visual hierarchy (clear information organization)
- Subtle shadows for depth
- Rounded corners for modern feel

EXAMPLE DATA for 3 cards:
Card 1:
- Name: "Trevor Bradford - IDEA Framework Website"
- Client: "IDEA Brand Coach"
- Phase: "Quick Win (Phase 3 Beta)"
- Priority: "P0"
- Status: Yellow dot (At risk)
- Received: $500
- Projected: $1,500
- Deadline: "Dec 27, 2025"
- Risk: High (red border), "⚠️ Late delivery = lose ALL future revenue"

Card 2:
- Name: "S&S Wolf Sheds - Process Automation"
- Client: "S&S Wolf Sheds"
- Phase: "Discovery Complete"
- Priority: "P0"
- Status: Gray dot (Not started)
- Received: $0
- Projected: $10,000
- Deadline: "Jan 31, 2026"
- Risk: Medium (yellow border), "Discovery complete, need to scope quick win"

Card 3:
- Name: "Plotter Mechanix - Dashboard & Analytics"
- Client: "Plotter Mechanix"
- Phase: "Quick Win (Phase 1)"
- Priority: "P0"
- Status: Green dot (On track)
- Received: $1,250
- Projected: $2,500
- Deadline: "Jan 15, 2026"
- Risk: Low (green border), "Phase 1 paid, on track for Phase 2"
```

---

## Follow-up Prompts (Refinement)

### If spacing is too tight:
```
Increase the padding inside project cards to 24px.
Increase grid gap between cards to 24px.
Make the revenue summary section have more breathing room (32px padding).
```

### If colors need adjustment:
```
Make the status dots larger (12px diameter).
Use more vibrant colors for risk borders:
- High risk: border-red-500
- Medium risk: border-yellow-500
- Low risk: border-green-500

Use softer background colors for badges:
- Phase badge: bg-blue-50 text-blue-700
- Priority badge: bg-purple-50 text-purple-700
```

### If cards look unbalanced:
```
Make project name text-lg font-semibold.
Make client name text-sm text-gray-600.
Ensure all badges are the same height (py-1 px-2).
Align revenue amounts to the right side.
```

### If responsive design needs work:
```
On tablet (768px), make grid 2 columns.
On mobile (below 640px), make grid 1 column.
Ensure cards don't get too wide on desktop (max-width container).
```

---

## Design System Reference

### Colors

**Status Indicators (Dots):**
- 🟢 On track: `bg-green-500`
- 🟡 At risk: `bg-yellow-500`
- 🔴 Critical/Blocked: `bg-red-500`
- ✅ Complete: `bg-blue-500`

**Risk Borders (Left border on cards):**
- High: `border-l-4 border-red-500`
- Medium: `border-l-4 border-yellow-500`
- Low: `border-l-4 border-green-500`

**Badges:**
- Phase: `bg-blue-50 text-blue-700` (or `bg-blue-100 text-blue-800`)
- Priority: `bg-purple-50 text-purple-700` (or `bg-purple-100 text-purple-800`)

**Revenue Text:**
- Received: `text-green-600 font-semibold`
- Projected: `text-gray-700 font-semibold`

**Background:**
- Page: `bg-gray-50`
- Cards: `bg-white`
- Header: `bg-white` or `bg-gray-50`

### Typography

**Header:**
- Title: `text-2xl font-bold text-gray-900`

**Tab Navigation:**
- Active tab: `text-blue-600 border-b-2 border-blue-600 font-medium`
- Inactive tab: `text-gray-600 hover:text-gray-900`

**Project Cards:**
- Project name: `text-lg font-semibold text-gray-900`
- Client name: `text-sm text-gray-600`
- Revenue labels: `text-sm text-gray-600`
- Revenue amounts: `text-sm font-semibold`
- Deadline: `text-xs text-gray-500`
- Risk warning: `text-xs text-red-600`

**Revenue Summary:**
- Labels: `text-sm text-gray-600`
- Numbers: `text-2xl font-bold`

### Spacing

**Container:**
- Max width: `max-w-7xl mx-auto px-4`

**Grid:**
- Desktop: `grid-cols-3 gap-6`
- Tablet: `md:grid-cols-2 gap-6`
- Mobile: `grid-cols-1 gap-4`

**Card Padding:**
- Internal: `p-6`

**Section Spacing:**
- Between major sections: `mb-6` or `mb-8`

### Shadows

**Cards:**
- Default: `shadow` or `shadow-md`
- Hover (optional): `hover:shadow-lg transition-shadow`

---

## Component Hierarchy

```
App
├── Header
│   └── "Agency Operations Dashboard"
├── TabNavigation
│   ├── Tab: "Projects & Revenue" (active)
│   ├── Tab: "Client Process"
│   ├── Tab: "Opportunity Matrix"
│   ├── Tab: "Pricing"
│   ├── Tab: "Objectives"
│   ├── Tab: "Dev Kanban"
│   └── Tab: "Validation"
└── MainContent
    └── ProjectsTab (active)
        ├── RevenueSummary
        │   ├── StatCard: Received
        │   ├── StatCard: Projected
        │   └── StatCard: Total
        ├── FilterBar
        │   ├── FilterLabel: "All Projects"
        │   ├── Dropdown: Priority
        │   └── Dropdown: Status
        └── ProjectGrid
            ├── ProjectCard (Trevor)
            ├── ProjectCard (S&S Wolf)
            ├── ProjectCard (Plotter)
            ├── ProjectCard (Invoice)
            ├── ProjectCard (AntSavvy)
            └── ProjectCard (Goldfinch)
```

---

## Interaction States

### Tabs
- **Default:** Gray text, no underline
- **Hover:** Darker gray, slight transition
- **Active:** Blue text, blue underline (2px), font-medium

### Project Cards
- **Default:** White background, subtle shadow
- **Hover:** Slightly larger shadow (optional: `hover:shadow-lg`)
- **Click:** (Phase 1: no click action, Phase 2+: open detail view)

### Filters/Dropdowns
- **Default:** Button with border, arrow icon
- **Hover:** Slight background color change
- **Open:** Dropdown menu appears below (white background, shadow)

---

## Accessibility Notes

- Ensure color contrast meets WCAG AA standards
- Status dots should have adjacent text labels (not just color)
- Interactive elements should have focus states
- Tab navigation should be keyboard accessible

---

## Export Instructions

Once satisfied with v0.app design:

1. **Export React code** from v0.app
2. **Check exports** include:
   - All component files
   - Tailwind classes intact
   - Responsive breakpoints preserved
3. **Save to** `/src/components/` folder
4. **Note any custom components** that need manual integration

---

## Visual Reference (ASCII Mockup)

```
┌─────────────────────────────────────────────────────────────────┐
│  Agency Operations Dashboard                                     │
├─────────────────────────────────────────────────────────────────┤
│  Projects & Revenue  │  Client Process  │  Opportunity Matrix  │ ...
│  ═══════════════════                                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Revenue Overview                                        │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ Received │  │ Projected│  │  Total   │              │   │
│  │  │  (YTD)   │  │          │  │ Potential│              │   │
│  │  │ $12,500  │  │ $21,500  │  │ $34,000  │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  All Projects    [Priority ▼]  [Status ▼]                      │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │● Trevor      │  │● S&S Wolf    │  │● Plotter     │         │
│  │  IDEA Website│  │  Process Auto│  │  Dashboard   │         │
│  │  IDEA Brand  │  │  S&S Wolf    │  │  Plotter Mech│         │
│  │  [Phase 3] P0│  │  [Discovery]P0│  │  [Phase 1] P0│         │
│  │              │  │              │  │              │         │
│  │  Received:   │  │  Received:   │  │  Received:   │         │
│  │    $500      │  │    $0        │  │    $1,250    │         │
│  │  Projected:  │  │  Projected:  │  │  Projected:  │         │
│  │    $1,500    │  │    $10,000   │  │    $2,500    │         │
│  │              │  │              │  │              │         │
│  │  Dec 27, 2025│  │  Jan 31, 2026│  │  Jan 15, 2026│         │
│  │  ⚠️ Critical │  │  Needs scope │  │  On track    │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Next Step:** Use this prompt in v0.app to generate initial UI, then iterate based on visual output
