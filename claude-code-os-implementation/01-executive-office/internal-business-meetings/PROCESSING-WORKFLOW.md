# Internal Business Meetings Processing Workflow

## Purpose

Convert Fathom recordings from equity partner meetings into actionable outputs:
- **Action items** with clear owners and deadlines
- **Roadmap additions** for strategic planning
- **Decision records** for future reference

---

## The Funnel

```
Partner Meeting (with Fathom recording)
    ↓
Send Fathom link to partner(s)
    ↓
Export Fathom summary + transcript
    ↓
Process with Claude (extract & organize)
    ↓
┌─────────────────┬─────────────────┬─────────────────┐
│  Action Items   │ Roadmap Updates │    Decisions    │
│  (with owners)  │  (prioritized)  │  (documented)   │
└─────────────────┴─────────────────┴─────────────────┘
    ↓                   ↓                   ↓
Daily Planning    roadmap-updates/    by-partner/
```

---

## Step 1: Immediate Post-Meeting (within 1 hour)

### 1.1 Send Fathom Link to Partners
- Share the Fathom recording link with all meeting participants
- This allows them to review and verify action items

### 1.2 Export Fathom Notes
1. Open Fathom call recording
2. Copy: Summary, Key Topics, Action Items, Transcript
3. Save to: `raw-notes/YYYY-MM-DD-topic.md`

**File naming:**
- `2025-11-27-weekly-sync.md`
- `2025-11-27-deal-review-linh.md`
- `2025-11-27-pipeline-planning.md`

---

## Step 2: Process with Claude (within 24 hours)

### Prompt Template for Claude:

```
Process these meeting notes and extract:

1. **ACTION ITEMS** - List each with:
   - Task description
   - Owner (Matthew, Linh, or Mikael)
   - Priority: 🔴 Urgent (today/tomorrow), 🟡 Important (this week), 🟢 Strategic (this month)
   - Deadline (if mentioned)

2. **ROADMAP ADDITIONS** - New ideas/features/initiatives discussed that should be added to roadmaps:
   - What: Description of the addition
   - Why: Business value/impact
   - Priority: P0-P5 based on strategic importance
   - Owner: Who will drive this

3. **DECISIONS MADE** - Any decisions reached:
   - Decision: What was decided
   - Context: Why this decision
   - Implications: What changes as a result

4. **KEY DISCUSSIONS** (brief summary):
   - Topics covered
   - Open questions
   - Follow-up needed

[PASTE FATHOM NOTES HERE]
```

### What Claude Should Output:

```markdown
## Action Items

### 🔴 Urgent (Do Today/Tomorrow)
- [ ] **[Owner]:** [Task] — Deadline: [date]

### 🟡 Important (This Week)
- [ ] **[Owner]:** [Task] — Deadline: [date]

### 🟢 Strategic (This Month)
- [ ] **[Owner]:** [Task] — Deadline: [date]

---

## Roadmap Additions

| Addition | Why | Priority | Owner |
|----------|-----|----------|-------|
| [Feature/initiative] | [Business value] | P[X] | [Name] |

---

## Decisions Made

### Decision: [Title]
**What:** [The decision]
**Why:** [Reasoning]
**Implications:** [What changes]

---

## Key Discussion Summary

**Topics covered:**
- [Topic 1]
- [Topic 2]

**Open questions:**
- [Question 1]

**Follow-up needed:**
- [Item 1]
```

---

## Step 3: Update Systems

### 3.1 Action Items → Daily Planning

**Urgent items (🔴):**
- Add to today's or tomorrow's daily plan immediately
- Block time for completion
- Set as P0 priority

**Important items (🟡):**
- Add to this week's plan
- Schedule specific day
- Set reminders if deadline-critical

**Strategic items (🟢):**
- Add to weekly/monthly planning
- Track in active-items.md
- Review in weekly review

**Update file:** `action-items/active-items.md`

### 3.2 Roadmap Additions → Monthly File

Add to `roadmap-updates/YYYY-MM.md`:

```markdown
## [Date] - [Meeting Topic]

### New Roadmap Items

| Item | Why | Priority | Owner | Source Meeting |
|------|-----|----------|-------|----------------|
| [Item] | [Value] | P[X] | [Name] | YYYY-MM-DD |

### Integration Notes
- [ ] Added to strategic-priorities.md
- [ ] Added to relevant project file
- [ ] Communicated to team
```

### 3.3 Decisions → Partner File

Add to `by-partner/[partner].md`:

```markdown
## [Date] - [Meeting Topic]

**Attendees:** [Names]

**Key Decisions:**
1. **[Decision]:** [Details]

**Action Items for [Partner]:**
- [ ] [Task 1]
- [ ] [Task 2]

**Next meeting:** [Date if scheduled]

**Raw notes:** [Link to raw-notes file]
```

---

## Step 4: Mark as Processed

In the raw notes file:
1. Add processing date
2. Mark all checklist items complete
3. Rename to: `YYYY-MM-DD-topic-PROCESSED.md`

---

## Quick Reference Card

```
AFTER MEETING (within 1 hour):
□ Send Fathom link to partners
□ Export Fathom notes
□ Save to raw-notes/YYYY-MM-DD-topic.md

WITHIN 24 HOURS (Processing):
□ Process with Claude using prompt template
□ Extract action items (with owners + priorities)
□ Extract roadmap additions
□ Document decisions

UPDATE SYSTEMS:
□ 🔴 Urgent items → today's daily plan
□ 🟡 Important items → this week's plan
□ 🟢 Strategic items → active-items.md
□ Roadmap additions → roadmap-updates/YYYY-MM.md
□ Decisions → by-partner/[partner].md
□ Mark raw notes as PROCESSED

WEEKLY REVIEW:
□ Review action-items/active-items.md
□ Update completion status
□ Move completed to archive section
□ Review roadmap-updates/ for strategic planning
```

---

## Time Budget

| Task | Time | When |
|------|------|------|
| Send Fathom link | 2 min | Right after call |
| Export Fathom notes | 5 min | Right after call |
| Process with Claude | 10-15 min | Within 24 hours |
| Update daily planning | 5 min | Same day |
| Update other systems | 10 min | Same day |
| **Total per meeting** | **~30 min** | **Within 24 hours** |

---

## Integration Checklist

After processing each meeting, verify:

- [ ] **Action items:** All items have owners and deadlines
- [ ] **Urgent items:** Added to daily plan
- [ ] **Roadmap:** New ideas added to roadmap-updates/
- [ ] **Decisions:** Documented in by-partner/ or meeting file
- [ ] **Follow-ups:** Any follow-up meetings scheduled
- [ ] **Fathom link:** Sent to all participants

---

## Common Meeting Types

### Weekly Partner Sync
**Focus:** Pipeline, priorities, blockers
**Typical outputs:** Updated priorities, removed blockers, aligned focus

### Deal Review (with Linh)
**Focus:** Specific deals, client relationships
**Typical outputs:** Deal strategy, next actions, pricing decisions

### Pipeline Planning (with Mikael)
**Focus:** Outreach, new leads, partnerships
**Typical outputs:** Outreach priorities, new targets, relationship status

### Strategic Planning (all partners)
**Focus:** Quarterly/monthly objectives, resource allocation
**Typical outputs:** Updated strategic-priorities.md, role adjustments

---

**Last Updated:** 2025-11-27
