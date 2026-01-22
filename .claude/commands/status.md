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

### 2. Open Action Items

Scan across all projects for uncompleted action items:

```markdown
## Open Action Items ([COUNT])

### P0 - Do Today
- [ ] [Task] | Project: [NAME] | Owner: [OWNER]

### P1 - This Week
- [ ] [Task] | Project: [NAME] | Owner: [OWNER]

### P2 - Backlog
- [ ] [Task] | Project: [NAME] | Owner: [OWNER]
```

**Sources:**
- `meetings/*/action-items.md`
- `status/active-items.md`
- `01-executive-office/internal-business-meetings/action-items/active-items.md`

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

## Open Action Items (7)
🔥 P0: Finalize API spec for PlotterMechanix
📅 P1: Schedule Wolf Sheds discovery call #2
📅 P1: Review proposal draft
...

## Content Queue (2)
📝 AI Time Savings post | Draft | Jan 19 | LinkedIn
✅ Brand Guidelines | Published | Jan 20 | Internal

## Pipeline
Discovery: 2 | Proposal: 1 | Active: 3 | Completed: 1

## System Health
✅ Git: Clean
✅ Notion: Connected
⚠️ Weekly Report: 5 days ago (run /weekly-report)

## Suggested Actions
1. 🔥 Complete PlotterMechanix API spec (P0)
2. 📊 Run /weekly-report (overdue)
3. 📝 Review AI Time Savings content draft
```

## Integration

This command is read-only - it gathers and displays information but doesn't modify anything. For actions, it suggests the appropriate skill/command to run.
