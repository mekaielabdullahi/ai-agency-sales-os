# Internal Business Meeting Template

## Raw Notes Template

**File:** `raw-notes/YYYY-MM-DD-topic.md`

```markdown
# Internal Meeting: [Topic] - [Date]

**Date:** YYYY-MM-DD
**Attendees:** [Matthew, Linh, Mikael - whoever was present]
**Duration:** [X] minutes
**Meeting Type:** [Weekly Sync / Deal Review / Pipeline Planning / Strategic Planning / Other]
**Status:** [ ] Not Processed
**Fathom Link:** [paste Fathom recording URL]
**Fathom Link Sent To:** [names of people link was sent to]

---

## Meeting Agenda/Purpose

[What was this meeting about?]

---

## Fathom Summary

[Paste Fathom AI summary here]

---

## Key Topics Discussed

[Fathom auto-extracts these - paste here]

---

## Fathom Action Items

[Paste Fathom's extracted action items here]

---

## Full Transcript

[Paste full Fathom transcript here]

---

## Processing Checklist

- [ ] Processed with Claude (extract action items, roadmap, decisions)
- [ ] Urgent action items added to daily planning
- [ ] Important items scheduled for this week
- [ ] Roadmap additions added to roadmap-updates/
- [ ] Decisions documented in by-partner/ files
- [ ] Follow-up meetings scheduled (if applicable)
- [ ] Marked as PROCESSED

**Processed on:** [Date]

---
```

---

## Processed Output Template

After Claude processes the meeting, the output should follow this structure:

```markdown
# Processed: [Meeting Topic] - [Date]

**Original:** `raw-notes/YYYY-MM-DD-topic.md`
**Processed:** YYYY-MM-DD
**Attendees:** [Names]

---

## Action Items

### 🔴 Urgent (Do Today/Tomorrow)

| Owner | Task | Deadline | Status |
|-------|------|----------|--------|
| Matthew | [Task] | YYYY-MM-DD | [ ] |
| Linh | [Task] | YYYY-MM-DD | [ ] |

### 🟡 Important (This Week)

| Owner | Task | Deadline | Status |
|-------|------|----------|--------|
| Mikael | [Task] | YYYY-MM-DD | [ ] |

### 🟢 Strategic (This Month)

| Owner | Task | Deadline | Status |
|-------|------|----------|--------|
| Matthew | [Task] | YYYY-MM-DD | [ ] |

---

## Roadmap Additions

| Addition | Business Value | Priority | Owner |
|----------|---------------|----------|-------|
| [Feature/Initiative] | [Why it matters] | P[X] | [Name] |

**Added to:**
- [ ] strategic-priorities.md
- [ ] Relevant project file
- [ ] roadmap-updates/YYYY-MM.md

---

## Decisions Made

### Decision 1: [Title]
**What:** [The decision]
**Why:** [Reasoning/context]
**Implications:** [What changes as a result]
**Owner:** [Who is responsible for implementation]

---

## Meeting Summary

**Key discussions:**
1. [Topic 1 summary]
2. [Topic 2 summary]

**Open questions:**
- [Question 1]

**Follow-up needed:**
- [Item 1 - who will handle]

---

## Next Meeting

**Date:** [If scheduled]
**Agenda items for next time:**
- [Item 1]

---
```

---

## Partner File Entry Template

**File:** `by-partner/[partner-name].md`

```markdown
---
## [YYYY-MM-DD] - [Meeting Topic]

**Attendees:** [Names]
**Meeting type:** [Type]

**Key Decisions:**
1. [Decision 1]
2. [Decision 2]

**[Partner Name]'s Action Items:**
- [ ] [Task 1] — Deadline: [date]
- [ ] [Task 2] — Deadline: [date]

**Updates from [Partner]:**
- [Update 1 - deals, relationships, etc.]

**Next steps:**
- [Next step 1]

**Raw notes:** [Link to processed raw-notes file]

---
```

---

## Roadmap Updates Entry Template

**File:** `roadmap-updates/YYYY-MM.md`

```markdown
---
## [Date] - [Source Meeting]

### New Items Added

| Item | Why | Priority | Owner | Status |
|------|-----|----------|-------|--------|
| [Item] | [Value] | P[X] | [Name] | [ ] Backlog |

### Items Deprioritized/Removed

| Item | Why Removed | Previous Priority |
|------|-------------|-------------------|
| [Item] | [Reason] | P[X] |

### Priority Adjustments

| Item | Old Priority | New Priority | Reason |
|------|--------------|--------------|--------|
| [Item] | P[X] | P[Y] | [Why] |

---
```

---

## Active Items Entry Template

**File:** `action-items/active-items.md`

```markdown
# Active Action Items from Partner Meetings

**Last Updated:** YYYY-MM-DD

---

## 🔴 Urgent (Do Today/Tomorrow)

| Source Meeting | Owner | Task | Deadline | Status |
|----------------|-------|------|----------|--------|
| YYYY-MM-DD | Matthew | [Task] | YYYY-MM-DD | [ ] |

---

## 🟡 Important (This Week)

| Source Meeting | Owner | Task | Deadline | Status |
|----------------|-------|------|----------|--------|
| YYYY-MM-DD | Linh | [Task] | YYYY-MM-DD | [ ] |

---

## 🟢 Strategic (This Month)

| Source Meeting | Owner | Task | Deadline | Status |
|----------------|-------|------|----------|--------|
| YYYY-MM-DD | Mikael | [Task] | YYYY-MM-DD | [ ] |

---

## Completed (Last 30 Days)

| Source Meeting | Owner | Task | Completed | Outcome |
|----------------|-------|------|-----------|---------|
| YYYY-MM-DD | Matthew | [Task] | YYYY-MM-DD | [Result] |

---
```

---

**Last Updated:** 2025-11-27
