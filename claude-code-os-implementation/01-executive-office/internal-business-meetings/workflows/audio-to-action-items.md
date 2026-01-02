# Audio to Action Items Workflow

## Purpose
Convert raw meeting audio into structured, actionable outputs that integrate with the Claude Code OS.

---

## Overview

```
Audio Recording (.m4a, .mp3, .wav)
    ↓
Whisper Transcription (automated)
    ↓
Claude Processing (extract structure)
    ↓
┌─────────────┬──────────────┬──────────────┬─────────────────┐
│ Action Items│  Decisions   │   Roadmap    │    Overview     │
│ (with owners)│ (documented) │  (strategic) │  (summary)      │
└─────────────┴──────────────┴──────────────┴─────────────────┘
    ↓
Integration into OS
    ↓
Daily Plans / Project Files / Strategic Objectives
```

---

## Phase 1: Raw Capture (During/After Meeting)

### 1.1 Record Audio
**Options:**
- Fathom (auto-records + exports)
- Local recording (QuickTime, Voice Memos)
- Zoom/Slack recording

**Save to:** `meetings/YYYY-MM-DD-meeting-name/01-raw/audio.m4a`

### 1.2 Manual Notes (Optional but Recommended)
During the meeting, capture:
- Key decisions made
- Action items mentioned
- Important quotes
- Questions that need follow-up

**Save to:** `meetings/YYYY-MM-DD-meeting-name/01-raw/raw-notes.md`

---

## Phase 2: Auto-Transcription

### 2.1 Whisper Processing
Uses existing audio processing tools at: `02-operations/project-management/audio-processing-tools/`

**Automatic workflow:**
```bash
# Audio file detected in 01-raw/
# Triggers Whisper transcription
# Outputs to: 01-raw/transcript.md
```

**Manual trigger:**
```bash
cd /Users/matthewkerns/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/audio-processing-tools

# Process single file
./whisper-local/batch-processor.sh /path/to/meeting/01-raw/audio.m4a

# Output automatically saved to same directory as transcript.md
```

### 2.2 Fathom Export (If Using Fathom)
1. Open Fathom recording
2. Copy: Summary + Transcript
3. Save to: `01-raw/fathom-export.md`

---

## Phase 3: Claude Processing

### 3.1 Processing Prompt

```
I have a meeting transcript that needs to be processed into structured outputs.

Meeting Context:
- Date: [YYYY-MM-DD]
- Meeting Name: [e.g., Partner Huddle, Deal Review]
- Attendees: [Names]
- Purpose: [Brief description]

Please analyze the transcript and raw notes to extract:

1. MEETING OVERVIEW
   - Key topics discussed (3-5 bullet points)
   - Duration and attendees
   - Overall meeting purpose

2. ACTION ITEMS
   For each action item:
   - [ ] **[Owner Name]:** [Specific task description]
   - Priority: 🔴 Urgent (0-2 days) | 🟡 Important (this week) | 🟢 Strategic (this month)
   - Deadline: [Date if mentioned, or "TBD"]
   - Context: [Why this matters - 1 sentence]

3. DECISIONS MADE
   For each decision:
   - **Decision:** [What was decided]
   - **Context:** [Why this decision was made]
   - **Implications:** [What changes as a result]
   - **Owner:** [Who owns implementation]

4. ROADMAP ADDITIONS
   For strategic items that should be added to roadmaps:
   | Item | Business Value | Priority | Owner | Timeline |
   |------|---------------|----------|-------|----------|
   | [Description] | [Why it matters] | P[0-5] | [Name] | [When] |

5. FOLLOW-UPS NEEDED
   - Items requiring additional discussion
   - Questions that need answering
   - Dependencies or blockers identified

6. KEY QUOTES (Optional)
   - Memorable quotes that capture key insights
   - Strategic positioning statements
   - Important client/partner feedback

---

TRANSCRIPT:
[Paste transcript here]

RAW NOTES:
[Paste raw notes here if available]
```

### 3.2 Output Structure

Claude outputs should be saved to `02-processed/` folder:

- `overview.md` - Meeting summary
- `action-items.md` - All action items with owners
- `decisions.md` - Key decisions documented
- `roadmap-additions.md` - Strategic additions

---

## Phase 4: System Integration

### 4.1 Action Items → Daily Planning

**Urgent (🔴):**
```bash
# Add to today's daily plan
# File: 01-executive-office/daily-planning/YYYY-MM-DD-daily-plan.md

## Urgent from [Meeting Name]
- [ ] [Action item 1]
- [ ] [Action item 2]
```

**Important (🟡):**
- Add to this week's planning
- Schedule specific days
- Set calendar reminders

**Strategic (🟢):**
- Add to `action-items/active-items.md`
- Track in weekly reviews
- Schedule in monthly planning

### 4.2 Decisions → Integration Log

Document in `03-integrated/system-updates.md`:

```markdown
# System Integration Log

## [Date] - [Meeting Name]

### Action Items Integrated
- [x] Added 3 urgent items to 2025-12-11 daily plan
- [x] Added 5 important items to active-items.md
- [x] Scheduled 2 strategic items for December planning

### Decisions Documented
- [x] Updated strategic-priorities.md with [Decision X]
- [x] Modified project scope in active-projects/[project-name]/
- [x] Communicated decision to team via Slack

### Roadmap Updates
- [x] Added 2 items to roadmap-updates/2025-12.md
- [x] Elevated priority of [Item X] from P3 → P1
- [x] Deferred [Item Y] to 2026-Q1

### Follow-ups Scheduled
- [ ] Meeting with [Partner] on [Date]
- [ ] Review [Topic] in next partner huddle
- [ ] Get [Information] from [Person] by [Date]
```

### 4.3 Roadmap Additions → Strategic Files

Update files:
- `01-executive-office/strategic-alignment/strategic-priorities.md`
- `internal-business-meetings/roadmap-updates/YYYY-MM.md`
- Relevant project files in `02-operations/project-management/active-projects/`

---

## Phase 5: Verification & Cleanup

### 5.1 Integration Checklist

- [ ] All action items have owners
- [ ] All action items have deadlines (even if "TBD")
- [ ] Urgent items added to daily plan
- [ ] Important items scheduled this week
- [ ] Strategic items tracked in active-items.md
- [ ] Decisions documented in relevant files
- [ ] Roadmap updates added to monthly file
- [ ] Follow-ups scheduled or logged
- [ ] Partners notified of their action items

### 5.2 Mark as Processed

In `02-processed/overview.md`, add status:

```markdown
---
**Processing Status:** ✅ Complete
**Processed By:** [Your name]
**Processed Date:** YYYY-MM-DD
**Integration Verified:** [Yes/No]
---
```

---

## Quick Reference: File Locations

| Item | Destination |
|------|-------------|
| Urgent action items | `01-executive-office/daily-planning/YYYY-MM-DD-daily-plan.md` |
| All action items | `internal-business-meetings/action-items/active-items.md` |
| Roadmap additions | `internal-business-meetings/roadmap-updates/YYYY-MM.md` |
| Strategic decisions | `01-executive-office/strategic-alignment/strategic-priorities.md` |
| Project updates | `02-operations/project-management/active-projects/[project]/` |
| Partner-specific | `internal-business-meetings/by-partner/[partner].md` |

---

## Time Budget

| Phase | Time | When |
|-------|------|------|
| Record audio | 0 min | During meeting |
| Manual notes | 5-10 min | During meeting |
| Whisper transcription | Auto | After meeting |
| Claude processing | 10-15 min | Within 24 hours |
| System integration | 15-20 min | Within 24 hours |
| Verification | 5 min | Within 24 hours |
| **Total** | **35-50 min** | **Within 24 hours** |

---

## Automation Opportunities

### Current State
✅ Whisper transcription (automated)
✅ File organization templates
⚠️ Claude processing (manual prompt)
⚠️ System integration (manual updates)

### Future Enhancements
- [ ] Auto-detect audio files in `01-raw/`
- [ ] Auto-trigger Whisper transcription
- [ ] Agent-based action item extraction
- [ ] Auto-routing to daily planning files
- [ ] Slack notifications for action item owners

---

## Related Workflows

- **PROCESSING-WORKFLOW.md** - Original Fathom-based workflow
- **action-item-extraction-agent.md** - Automated extraction agent (to be built)
- **Audio Processing Tools** - `02-operations/project-management/audio-processing-tools/`

---

**Created:** 2025-12-11
**Status:** Active
**Last Updated:** 2025-12-11
