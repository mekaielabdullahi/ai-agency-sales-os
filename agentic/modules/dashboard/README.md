# Dashboard Module

Comprehensive dashboard system for AriseGroup.ai agency metrics.

## Dashboard Types

| Dashboard | Purpose | Status |
|-----------|---------|--------|
| **Executive** | Leadership snapshot - revenue, pipeline, alerts | Active |
| **Operations** | Delivery health - tasks, projects, blockers | Active |
| Sales | Pipeline & conversion metrics | Planned |
| Marketing | Content performance | Planned |
| Financial | Profitability & cash flow | Planned |
| Support | Client satisfaction | Planned |

## Usage

### CLI

```bash
# Executive dashboard (default)
./run modules/dashboard/tool/dashboard_api.py

# Operations dashboard
./run modules/dashboard/tool/dashboard_api.py --type ops

# Slack format
./run modules/dashboard/tool/dashboard_api.py --format slack

# JSON format
./run modules/dashboard/tool/dashboard_api.py --format json
```

### Slash Commands

```
/dashboard              # Executive dashboard
/dashboard ops          # Operations dashboard
/dashboard --format slack
```

## Data Sources

- **Notion**: Tasks database, Contacts database, Companies database
- **Files**: Active projects folder, weekly reports
- **Slack**: Team channel activity (optional)

## Output Formats

- **Markdown** (default): Terminal-friendly tables and sections
- **Slack**: Block Kit formatted for Slack posting
- **JSON**: Structured data for API consumption

## Module Structure

```
modules/dashboard/
├── tool/
│   ├── dashboard_api.py          # Main orchestrator
│   ├── collectors/               # Data collection
│   │   ├── notion_collector.py
│   │   └── file_collector.py
│   ├── generators/               # Dashboard generation
│   │   ├── executive_dashboard.py
│   │   └── operations_dashboard.py
│   └── formatters/               # Output formatting
│       ├── markdown_formatter.py
│       └── slack_formatter.py
├── runbook/
│   └── dashboard_management.md
├── commands/
│   └── dashboard.md
└── data/                         # Local data storage (future)
```

## Environment Variables

- `NOTION_API_KEY`: Required for Notion data collection
- `SLACK_BOT_TOKEN`: Optional for Slack posting

## Related

- `/status` command for quick health checks
- `/weekly-report` for weekly summaries
- `modules/notion/` for Notion API tools
