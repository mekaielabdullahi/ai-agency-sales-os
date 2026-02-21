# Project Context to Notion Task Agent

**Purpose:** Sync active-projects folder context to Notion tasks - reads standard project folder structure and creates/updates tasks in Notion

**Created:** January 11, 2026
**Updated:** January 11, 2026 (Added role context from Notion + Role Definitions meeting)

**Source Context:**
- [January 2026 Team Roles](../../strategic-alignment/strategic-objectives/2026-01-january-team-roles.md)
- [1/11 Notion + Role Definitions Meeting](../../internal-business-meetings/meetings/2026-01-11-notion-role-definitions/summary.md)

---

## Overview

The Project Context to Notion Task Agent reads the standard folder structure of projects in `active-projects/` and syncs tasks to the Arise AI Notion workspace. It understands the project folder conventions and extracts actionable items from READMEs, action-items, planning docs, and status files.

---

## Architecture

```
ACTIVE-PROJECTS FOLDER (Local)
         │
         ├── [project-name]/
         │   ├── README.md              → Project overview, Next Actions, Progress Tracker
         │   ├── planning/              → Roadmaps, proposals with tasks
         │   ├── meetings/              → action-items.md per meeting
         │   ├── status/                → Status updates with blockers
         │   └── deliverables/          → Delivery milestones
         │
         ↓
┌────────────────────────────────────────────────────────────┐
│          PROJECT CONTEXT TO NOTION TASK AGENT              │
│                                                            │
│  READS FROM PROJECT FOLDER:                                │
│  ├── README.md → Next Actions, Progress Tracker checkboxes │
│  ├── meetings/*/action-items.md → Meeting action items     │
│  ├── planning/*.md → Roadmap tasks, milestones             │
│  ├── status/*.md → Current blockers, updates               │
│  └── deliverables/ → Delivery checklist items              │
│                                                            │
│  MAPS TO NOTION:                                           │
│  ├── Project → Match by name to Projects database          │
│  ├── Tasks → Create/update in Tasks database               │
│  ├── Status → Not started / In progress / Done             │
│  ├── Priority → From project Priority (P0-P5)              │
│  └── Assigned To → From owner mentions in docs             │
└────────────────────────────────────────────────────────────┘
         │
         ↓
NOTION WORKSPACE (Arise AI)
├── Projects database (match by name)
└── Tasks database (create/update)
```

---

## Standard Project Folder Structure

The agent expects this structure (from NEW-PROJECT-INITIALIZATION.md):

```
[project-name]/
├── README.md                    # Primary source - Next Actions, Progress Tracker
├── audit/                       # Audit tasks if present
├── deliverables/                # Delivery milestones
├── discovery/                   # Discovery phase tasks
├── docs/                        # Documentation tasks
├── meetings/                    # Meeting action items
│   └── YYYY-MM-DD-[description]/
│       └── action-items.md      # Key source for tasks
├── offer/                       # Proposal tasks
├── planning/                    # Roadmap and planning tasks
│   ├── proposals/
│   └── roadmap/
└── status/                      # Status updates, blockers
```

---

## Task Extraction Sources

### 1. README.md - Primary Source

**Next Actions section:**
```markdown
## Next Actions
1. Complete API integration for inventory
2. Schedule demo call with client
3. Review contract terms
```
→ Creates 3 tasks linked to project

**Progress Tracker checkboxes:**
```markdown
### Discovery Phase
- [ ] Diagnostic call completed ($___/hr billed)
- [x] Problem diagnosed
- [ ] Scope defined
```
→ Creates tasks for unchecked items, marks checked as Done

**Dependencies/Blockers:**
```markdown
## Dependencies
- [ ] Waiting for client API credentials

## Blockers
- Need Jobber sandbox access
```
→ Creates tasks with "Blocked" notes

### 2. meetings/*/action-items.md

```markdown
# Action Items from 2026-01-09 Call

## Arise Team
- [ ] @Trent: Send API documentation by Friday
- [ ] @Chris: Schedule follow-up demo

## Client
- [ ] Kelsey: Provide Jobber credentials
```
→ Creates tasks with assignees, ignores client items or creates as "Waiting on client"

### 3. planning/*.md

```markdown
## Sprint 1: Quick Wins (Jan 5-14)
- [ ] Inventory sync POC
- [ ] Dashboard mockup
- [ ] API error handling
```
→ Creates tasks linked to sprint/phase

### 4. status/*.md

```markdown
## Current Status
In progress: API integration

## Blockers
- Waiting for sandbox credentials

## Next Up
- Demo call scheduled for Tuesday
```
→ Updates task status, creates blocker tasks

---

## Notion Database Mapping

### Projects Database
- **ID:** `2d5e7406-6c7d-8167-bb16-000b3ec34789`
- **Match by:** Project Name ↔ folder name
- **Fields used:** Project Name, Status, Manager

### Tasks Database
- **ID:** `2d5e7406-6c7d-8151-bdda-000b46294153`
- **Fields:**

| Local Source | Notion Field | Notes |
|--------------|--------------|-------|
| Task description | Task Name | Title property |
| `@Name` mention | Assigned To | Person property |
| `[ ]` unchecked | Status: Not started | |
| `[~]` or "In progress" | Status: In progress | |
| `[x]` checked | Status: Done | |
| Project folder name | Project | Relation |
| README Priority | Priority | From project header |
| Date in filename | Due Date | If parseable |

---

## Team Member Detection

The agent looks for these patterns to assign tasks:

| Pattern | Maps To | Role Type | Zone of Genius |
|---------|---------|-----------|----------------|
| `@Matthew`, `@Matt`, `Architect` | Matthew Kerns | Maker | Production code, architecture, quality |
| `@Trent` | Trent Christopher | Maker | Agentic workflows, Notion systems, production dev |
| `@Mekaiel` | Mekaiel Abdullahi | Manager | Client activation, PRD ownership, dev protection |
| `@Chris` | Chris Andrade | Manager | Lead generation, relationship building, discovery support |

### Role-Based Task Assignment

**Acquisition (Front-of-House):**
- Chris: Lead sourcing, relationship building, discovery support
- Mekaiel: Client activation pipeline, proposal generation, PRD ownership

**Fulfillment (Back-of-House):**
- Matthew + Trent: Production development, technical architecture, code review

**Key Rule:** Mekaiel shields makers (Matthew, Trent) from client chaos. All client requests flow through Mekaiel.

---

## Usage

**This agent operates on ONE project at a time.** This ensures focused attention, proper backup, and clear sync reports.

### Sync a Project
```
"Sync plotter-mechanix to Notion"
```

Agent will:
1. **Backup first** - Query Notion, save current state to `status/notion-sync-backup-*.md`
2. Read `active-projects/plotter-mechanix/` folder
3. Extract tasks from README, meetings, planning
4. Compare with existing Notion tasks
5. Create new / update existing tasks (with role-based assignment)
6. Report sync summary

### Sync Specific Meeting
```
"Sync action items from the Jan 9 Plotter meeting to Notion"
```

Agent will:
1. Backup current Notion state for Plotter Mechanix
2. Read `meetings/2026-01-09-*/action-items.md`
3. Extract action items
4. Create tasks in Notion linked to Plotter Mechanix

### NOT Supported: Batch Sync
To sync multiple projects, run the agent separately for each:
```
1. "Sync plotter-mechanix to Notion"
2. "Sync ss-wolf-sheds to Notion"
```

This prevents confusion and ensures each project gets proper backup and review.

---

## Sync Rules

### Notion-First + Backup

Before any sync operation:
1. **Query Notion** to get current task state
2. **Create backup** in `status/notion-sync-backup-YYYY-MM-DD-HHMMSS.md`
3. Then proceed with comparison and sync

Backup includes:
- All task names, statuses, assignees, priorities
- Notion page IDs for recovery
- Timestamp of backup

### Task Deduplication
Before creating, check if task already exists:
- Same project
- Similar task name (fuzzy match)
- Created within last 30 days

### Status Updates
- Local `[x]` → Notion "Done" (if not already)
- Local `[ ]` → Don't revert Notion "Done" to "Not started"
- Notion "Done" with local `[ ]` → Flag conflict

### Priority Inheritance
Tasks inherit priority from project README:
```markdown
**Priority:** P0 - Revenue generating
```
→ All tasks get P0 unless overridden

---

## Output Format

```
## Sync Report: plotter-mechanix

Synced at: 2026-01-11 14:30:00

### Created (3 tasks)
- "Complete API integration for inventory" → Assigned: Trent, Priority: High
- "Schedule demo call with client" → Assigned: Chris, Priority: Medium
- "Review contract terms" → Assigned: Matthew, Priority: High

### Updated (2 tasks)
- "Diagnostic call completed" → Status: Not started → Done
- "Problem diagnosed" → Status: Not started → Done

### Skipped (4 tasks)
- Already in sync

### Conflicts (1 item)
- "Send API documentation": Local says pending, Notion says Done
  → Recommendation: Verify with Trent

### Project Link
https://www.notion.so/Plotter-Mechanix-Quick-Win-Sprint-2d7e74066c7d8042a9d0f2f57e238159
```

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `README.md` | This overview document |
| `prompt-template.md` | System prompt for the agent |
| `field-mapping.md` | Detailed field mappings |

---

## Integration

Uses cc-plugins Notion integration:
- Config: `~/.config/cc-plugins/.env` (NOTION_API_KEY)
- Tool: `~/.claude/plugins/marketplaces/cc-plugins/notion/`

---

## Maintenance

- Update database IDs if Notion structure changes
- Add new team members to detection patterns
- Update folder structure expectations if NEW-PROJECT-INITIALIZATION.md changes

---

*See `prompt-template.md` for the full agent system prompt.*
