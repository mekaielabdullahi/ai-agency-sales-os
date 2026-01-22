# System Status Command

## Purpose
Quick overview of the AI Agency Sales OS state - active projects, pending tasks, content queue, and system health.

## When to Use
- Start of day check-in
- Before weekly planning
- When asking "what's the current state?"
- Quick system health check

## Workflow

### 1. Active Projects Summary

Scan `claude-code-os-implementation/02-operations/project-management/active-projects/` and for each project:

```markdown
## Active Projects ([COUNT])

| Project | Status | Priority | Last Activity |
|---------|--------|----------|---------------|
| [NAME] | [PHASE] | [P0/P1/P2] | [DATE] |
```

**Status Detection:**
- Check for `status/P0-ACTIVE-NOW.md` → "Active (P0)"
- Check README.md for phase indicators
- Check most recent meeting date

### 2. Notion Tasks (Primary Source)

**Fetch tasks directly from Notion using the agentic module.**

**Database ID:** `2d5e7406-6c7d-810e-a1be-c35b71fdf23b`
**Database URL:** https://www.notion.so/2d5e74066c7d810ea1bec35b71fdf23b

**Run the fetch_tasks script to get live tasks:**
```bash
cd agentic && ./run modules/notion/tool/fetch_tasks.py
```

This script:
- Queries the Tasks database directly via Notion API
- Filters out Done and Cancelled tasks
- Groups by Priority (Urgent, High) and Status (In Progress, Blocked, Not Started)
- Formats output for the status display

**Setup Required:**
1. Copy `agentic/.env.example` to `agentic/.env`
2. Add your NOTION_API_KEY (get from https://www.notion.so/my-integrations)
3. Make sure the integration has access to your Tasks database

**Alternative: If Notion MCP is connected, use notion-search tool:**
```
Search in data_source_url: collection://2d5e7406-6c7d-8151-bdda-000b46294153
Filter: Status is NOT "Done" AND Status is NOT "Cancelled"
```

**Display format:**
```markdown
## Notion Tasks ([COUNT])

### 🔥 Urgent
| Task | Project | Due | Assigned |
|------|---------|-----|----------|
| [Task Name] | [Project] | [Due Date] | [Person] |

### 🟠 High Priority
| Task | Project | Due | Assigned |
|------|---------|-----|----------|

### 🟡 In Progress
| Task | Project | Due | Assigned |
|------|---------|-----|----------|

### ⬜ Not Started
| Task | Project | Due | Assigned |
|------|---------|-----|----------|

### 🟣 Blocked
| Task | Project | Due | Assigned |
|------|---------|-----|----------|
```

**Task Schema Reference:**
- **Status**: Not started, In progress, Blocked, To Review, Done, Cancelled
- **Priority**: Urgent, High, Medium, Low
- **Project**: Relation to Projects database
- **Due Date**: Date field
- **Assigned To**: Person field

**Sort Order:**
1. Priority (Urgent → High → Medium → Low)
2. Due Date (soonest first)
3. Status (Blocked → In Progress → Not Started)

### 2b. Local Action Items (Backup)

Also scan local project folders for any action items not yet in Notion:

**Sources:**
- `meetings/*/action-items.md`
- `status/active-items.md`
- `01-executive-office/internal-business-meetings/action-items/active-items.md`

If local items found that aren't in Notion, flag them:
```
⚠️ [X] local action items not synced to Notion
```

### 3. Content Queue

Check brand-illustrator projects folder:

```markdown
## Content Queue

| Content | Status | Created | Platform |
|---------|--------|---------|----------|
| [TITLE] | Draft/Review/Approved | [DATE] | LinkedIn |
```

**Source:** `.claude/skills/brand-illustrator/projects/`

### 4. Pipeline Snapshot

Quick view of sales/client pipeline:

```markdown
## Pipeline

- **Discovery Pending:** [COUNT] leads
- **Proposal Stage:** [COUNT] clients
- **Active Clients:** [COUNT]
- **Completed This Month:** [COUNT]
```

**Sources:**
- Check for discovery folders with no proposal
- Check for proposal folders
- Count active-projects

### 5. System Health

```markdown
## System Health

| Component | Status |
|-----------|--------|
| Notion Sync | ✅ Connected / ⚠️ Check API key |
| Slack | ✅ Connected / ⚠️ Check token |
| Weekly Report | Last run: [DATE] |
| Git Status | Clean / [X] uncommitted changes |
```

**Checks:**
- Verify `.env` files have required keys
- Check git status
- Check last weekly report date

### 6. Quick Actions

Based on status, suggest next actions:

```markdown
## Suggested Next Actions

1. [ACTION based on highest priority item]
2. [ACTION based on stale content]
3. [ACTION based on overdue items]
```

## Output Format

Display all sections in a single, scannable output. Use emoji indicators:
- ✅ Good / Complete
- ⚠️ Needs attention
- 🔥 Urgent / P0
- 📅 Scheduled
- ⏸️ Paused

## Example Output

```
📊 SYSTEM STATUS - 2026-01-22

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Active Projects (3)
🔥 PlotterMechanix     | Phase 1 Build  | P0 | Today
🔨 Wolf Sheds          | Discovery      | P1 | 2 days ago
📋 AriseGroup Internal | Ongoing        | P2 | This week

## Notion Tasks (12 open)

🔥 URGENT (2)
• Finalize API spec for PlotterMechanix | Due: Today | @Trent
• Review voice agent demo | Due: Today | @Mekaiel

🟠 HIGH (3)
• Schedule Wolf Sheds discovery call #2 | Due: Jan 24 | @Chris
• Complete proposal revisions | Due: Jan 25 | @Mekaiel
• Set up n8n webhook for onboarding | Due: Jan 26 | @Trent

🔵 IN PROGRESS (4)
• Build lot assistant prototype | Wolf Sheds | @Trent
• Content calendar for Q1 | AriseGroup | @Mekaiel
• Voice routing implementation | PlotterMechanix | @Trent
• Discovery synthesis | Randy Tech | @Chris

⬜ NOT STARTED (2)
• Create onboarding email templates | Due: Jan 28
• Document API endpoints | Due: Jan 30

🟣 BLOCKED (1)
• Deploy to production | Waiting on: DNS config

## Content Queue (2)
📝 AI Time Savings post | Draft | Jan 19 | LinkedIn
✅ Brand Guidelines | Published | Jan 20 | Internal

## Pipeline
Discovery: 2 | Proposal: 1 | Active: 3 | Completed: 1

## System Health
✅ Git: Clean
✅ Notion: Connected (12 tasks synced)
⚠️ Weekly Report: 5 days ago (run /weekly-report)

## Suggested Actions
1. 🔥 Finalize API spec (Urgent, due today)
2. 🔥 Review voice agent demo (Urgent, due today)
3. 📊 Run /weekly-report (overdue)
```

## Integration

This command is read-only - it gathers and displays information but doesn't modify anything. For actions, it suggests the appropriate skill/command to run.
