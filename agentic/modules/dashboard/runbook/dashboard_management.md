# Dashboard Management Runbook

## Overview

This runbook covers generating and using agency dashboards for executive and operational visibility.

## Quick Reference

```bash
# Executive dashboard (default)
./run modules/dashboard/tool/dashboard_api.py

# Operations dashboard
./run modules/dashboard/tool/dashboard_api.py --type ops

# Slack format (for posting)
./run modules/dashboard/tool/dashboard_api.py --format slack

# JSON format (for integration)
./run modules/dashboard/tool/dashboard_api.py --format json
```

## Dashboard Types

### Executive Dashboard

**Purpose:** High-level business health for leadership

**Metrics Included:**
- Task summary (total, overdue, blocked, due this week)
- Pipeline overview (leads, total value, by stage)
- Project health (green/yellow/red status)
- Weekly report freshness
- Priority alerts

**When to Use:**
- Daily/weekly business review
- Leadership updates
- Quick health check

### Operations Dashboard

**Purpose:** Detailed operational metrics for delivery

**Metrics Included:**
- Task status breakdown by state
- Overdue and blocked task lists
- Project health with last activity dates
- Action items (open vs completed)
- Velocity metrics (blocked rate, overdue rate)
- Actionable recommendations

**When to Use:**
- Daily standup preparation
- Sprint planning
- Delivery reviews
- Identifying blockers

## Data Sources

| Source | Data Collected |
|--------|----------------|
| Notion Tasks | Task status, priority, due dates, assignments |
| Notion Contacts | Pipeline stages, deal values, last contact |
| Active Projects | Project folders, activity dates, health |
| Weekly Reports | Report freshness, latest report info |
| Action Items | Open/completed items from meeting notes |

## Output Formats

### Markdown (Default)
- Terminal-friendly tables and sections
- Emoji status indicators
- Suitable for viewing in Claude Code

### Slack
- Block Kit JSON format
- Ready to post to Slack channels
- Use with Slack API or copy/paste

### JSON
- Raw structured data
- For programmatic use
- Integration with other tools

## Troubleshooting

### "NOTION_API_KEY not configured"
Ensure `.env` file has valid Notion API key:
```
NOTION_API_KEY=ntn_xxx...
```

### "Database ID not found"
The Notion database IDs are hardcoded. If your workspace has different IDs, update them in:
- `modules/dashboard/tool/collectors/notion_collector.py`

### Missing project data
Ensure active projects folder exists at expected path:
- `claude-code-os-implementation/02-operations/project-management/active-projects/`

### Slack blocks not posting
The Slack format outputs JSON blocks. To post:
1. Copy the JSON output
2. Use Slack API or Block Kit Builder to post

## Related

- `/status` - Quick health check (simpler)
- `/weekly-report` - Weekly summary generation
- `modules/notion/` - Notion API tools
