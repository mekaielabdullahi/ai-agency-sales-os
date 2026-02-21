# Meeting to Notion Task Agent

**Purpose:** Convert meeting transcripts into actionable Notion tasks

**Created:** January 11, 2026

---

## Overview

The Meeting to Notion Task Agent processes meeting transcripts and maintains alignment between team discussions, strategic priorities, and executable tasks in Notion. It ensures decisions made in meetings are captured, prioritized correctly, and assigned to the right people based on their role (maker vs manager).

---

## Architecture

```
MEETING TRANSCRIPT (Input)
         ↓
┌────────────────────────────────────────────────────────────┐
│                    PLANNING AGENT                          │
│                                                            │
│  CONTEXT DOCUMENTS (loaded at startup):                    │
│  ├── maker-vs-manager-guide.md                            │
│  ├── prioritization-plan-jan-2026.md (current sprint)     │
│  ├── risk-assessment-jan-2026.md                          │
│  ├── 2026-01-january-team-roles.md                        │
│  └── obg-definition.md (One Big Goal)                     │
│                                                            │
│  NOTION TOOLS:                                            │
│  ├── notion_query_tasks() - Read current task state       │
│  ├── notion_create_task() - Create new tasks              │
│  ├── notion_update_task() - Update existing tasks         │
│  └── notion_get_database_schema() - Validate fields       │
│                                                            │
│  CORE BEHAVIORS:                                          │
│  ├── Extract action items from transcript                 │
│  ├── Validate against role definitions (maker/manager)    │
│  ├── Check priority alignment with OBG                    │
│  ├── Protect maker time (flag violations)                 │
│  └── Create/update Notion tasks with required fields      │
└────────────────────────────────────────────────────────────┘
         ↓
NOTION TASKS (Output) + PRIORITY UPDATES (if needed)
```

---

## When to Use

1. **After planning meetings** - Process transcript, create sprint tasks
2. **After client calls** - Extract action items, assign owners
3. **Daily standups** - Update task statuses, flag blockers
4. **Priority shifts** - Update prioritization docs when strategy changes

---

## What the Agent Does

### 1. Extract Action Items
- Identifies commitments made in the meeting
- Distinguishes between tasks and discussion points
- Captures deadlines mentioned

### 2. Validate Against Roles
- Checks if assigned owner matches the task type
- Flags if a maker is being assigned coordination work
- Flags if a manager is being assigned deep work

### 3. Protect Maker Time
- Warns if tasks would exceed maker meeting budget
- Suggests batching for sync windows
- Flags tasks that would interrupt deep work blocks

### 4. Enforce Notion Standards
- Ensures all required fields are populated
- Validates priority levels (P0-P5)
- Links tasks to correct sprint/project

### 5. Update Strategic Docs (When Needed)
- If priorities shift in meeting, updates prioritization plan
- Documents rationale for changes
- Maintains audit trail

---

## What the Agent Does NOT Do

- Make strategic decisions (only captures and validates)
- Override explicit human decisions
- Create tasks that violate maker time protection without flagging
- Ignore context documents in favor of meeting content

---

## Input Format

The agent expects a meeting transcript with:
- Speaker identification (who said what)
- Timestamp or sequence markers
- Clear discussion of tasks/assignments

Example:
```
[Matthew]: We need to finish S&S Wolf by Tuesday
[Trent]: I can handle the Xigent proposal, I have the drafts
[Mekaiel]: I'll review it for standards before we send
[Chris]: I'll make sure the client experience is consistent
```

---

## Output Format

The agent produces:
1. **Notion Tasks** - Created/updated via API
2. **Summary Report** - What was captured, any flags/warnings
3. **Priority Updates** - If strategic docs need updating

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `README.md` | This overview document |
| `prompt-template.md` | The system prompt for the agent |
| `notion-fields.md` | Required Notion fields and validation rules |

---

## Integration Points

### Notion Workspace
- Database: `Tasks` (or whatever your task database is named)
- Required fields: See `notion-fields.md`
- API: Notion Integration with read/write access

### Meeting Tools
- Fathom or Fireflies transcript export
- Google Meet recording link (for reference)

### Strategic Documents
- Located in `01-executive-office/strategic-alignment/`
- Agent reads these for context, can suggest updates

---

## Example Workflow

```
1. Team has planning meeting (Google Meet + Fathom)
         ↓
2. Fathom generates transcript
         ↓
3. User provides transcript to Meeting to Notion Task Agent
         ↓
4. Agent processes:
   - "Matthew will work on S&S Wolf" → Creates task, assigns Matthew,
     validates he's a maker, checks hours against sprint capacity
   - "Trent leads Xigent" → Creates task, notes domain expertise exception,
     flags reduced Plotter capacity
   - "Quick sync tomorrow" → Checks if within sync windows, warns if not
         ↓
5. Agent creates tasks in Notion with all required fields
         ↓
6. Agent produces summary:
   "Created 4 tasks. 1 warning: Trent's Xigent focus reduces
    Plotter capacity - Matthew may need to support."
```

---

## Maintenance

- Update context documents as strategy evolves
- Review agent outputs weekly for accuracy
- Adjust prompt as team processes mature

---

*See `prompt-template.md` for the full agent system prompt.*
