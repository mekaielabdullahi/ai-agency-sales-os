# Internal Business Meetings

**Purpose:** Capture decisions, action items, and roadmap updates from equity partner meetings (Linh, Mikael, and you).

**Source:** Fathom recordings with summaries and transcripts

---

## Directory Structure

```
internal-business-meetings/
├── README.md                          # This file
├── PROCESSING-WORKFLOW.md             # How to process meeting notes
├── TEMPLATE.md                        # Template for raw notes
├── workflows/
│   ├── audio-to-action-items.md      # Audio processing workflow
│   └── action-item-extraction-agent.md  # Agent for extracting todos
├── meetings/                          # All meetings organized by date
│   └── YYYY-MM-DD-meeting-name/
│       ├── 01-raw/
│       │   ├── audio.m4a             # Original recording
│       │   ├── transcript.md         # Auto-generated from Whisper
│       │   ├── fathom-export.md      # Fathom summary (if used)
│       │   └── raw-notes.md          # Manual notes during meeting
│       ├── 02-processed/
│       │   ├── overview.md           # Meeting summary
│       │   ├── action-items.md       # Extracted with owners + deadlines
│       │   ├── decisions.md          # Key decisions made
│       │   └── roadmap-additions.md  # Strategic additions
│       └── 03-integrated/
│           └── system-updates.md     # How items were integrated into OS
├── by-partner/                        # Notes organized by partner
│   ├── linh.md                       # All Linh meetings
│   └── mikael.md                     # All Mikael meetings
├── roadmap-updates/                   # Roadmap additions from meetings
│   └── YYYY-MM.md                    # Monthly roadmap updates
└── action-items/                      # Tracked action items
    └── active-items.md               # Currently active items
```

---

## Quick Start: After Any Partner Meeting

**The Fathom Link → OS System Flow:**

```
1. Meeting ends → Send Fathom link to partner(s)
   ↓
2. Export Fathom summary + transcript
   ↓
3. Save to raw-notes/YYYY-MM-DD-topic.md
   ↓
4. Process with Claude (see PROCESSING-WORKFLOW.md)
   ↓
5. Extract:
   - Action items (with owners + deadlines)
   - Roadmap additions
   - Decisions made
   ↓
6. Update:
   - action-items/active-items.md
   - roadmap-updates/YYYY-MM.md
   - by-partner/[partner].md (if partner-specific)
   ↓
7. Mark raw notes as PROCESSED
```

---

## Equity Partners

### Linh
**Role:** Sales + Relationships
**Meeting types:** Deal reviews, client relationship updates, pipeline discussions
**Typical outputs:** Lead updates, relationship status, next sales actions

### Mikael
**Role:** Outbound + Biz Dev
**Meeting types:** Outreach results, operator relationships, deal pipeline
**Typical outputs:** Outreach metrics, new leads, partnership opportunities

### You (Architect)
**Role:** Technical Strategy + Execution
**Meeting types:** Project status, technical decisions, pricing/scoping
**Typical outputs:** Technical roadmap, delivery timelines, pricing decisions

---

## When to Use This System

✅ **Use for:**
- Weekly/bi-weekly partner syncs
- Deal review meetings
- Strategic planning sessions
- Revenue/pipeline reviews
- Role clarification discussions
- Any meeting where decisions are made

❌ **Don't use for:**
- Quick Slack/text conversations (too lightweight)
- 1:1 coaching calls (use coaching-call-notes instead)
- Client calls (separate system)

---

## Integration with Other Systems

**Daily Planning:**
- Urgent action items → add to daily plan immediately
- Important items → schedule within the week

**Project Management:**
- New projects discussed → create in active-projects/
- Project updates → update project files

**Strategic Objectives:**
- Strategy changes → update strategic-priorities.md
- New goals → add to objectives

**Pipeline:**
- New leads discussed → add to pipeline tracking
- Deal updates → update pipeline status

---

## Success Metrics

You're using this system effectively when:
- ✅ No action items fall through the cracks
- ✅ Partners have clear ownership of tasks
- ✅ Roadmap gets updated with new ideas immediately
- ✅ Decisions are documented (not just remembered)
- ✅ You can reference past meeting decisions easily
- ✅ Strategic alignment stays consistent across partners

---

## Pending Actions

**Setup Complete:** 2025-11-27

**Next Steps:**
- [ ] Use for next partner meeting
- [ ] Refine template based on actual usage

---

**Last Updated:** 2025-11-27
