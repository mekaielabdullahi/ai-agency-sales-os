# Dashboard

Generate agency dashboards with comprehensive metrics.

## Arguments

- `$ARGUMENTS`: Optional arguments:
  - `ops` or `operations` - Operations dashboard (tasks, projects, blockers)
  - `exec` or `executive` - Executive dashboard (default)
  - `--format slack` - Output as Slack blocks
  - `--format json` - Output as raw JSON

## Usage Examples

```
/dashboard                    # Executive dashboard (default)
/dashboard ops                # Operations dashboard
/dashboard --format slack     # Executive as Slack blocks
/dashboard ops --format json  # Operations as JSON
```

## Instructions

1. Parse arguments to determine dashboard type and format:
   - If `ops` or `operations` in arguments → type = "ops"
   - If `--format slack` in arguments → format = "slack"
   - If `--format json` in arguments → format = "json"
   - Otherwise → type = "executive", format = "markdown"

2. Run the dashboard generator:
   ```bash
   ./run modules/dashboard/tool/dashboard_api.py --type <TYPE> --format <FORMAT>
   ```

3. Display the output directly - it's already formatted.

## Dashboard Types

### Executive Dashboard
High-level business metrics:
- Tasks overview (open, overdue, blocked)
- Pipeline summary (leads, value by stage)
- Project health (green/yellow/red)
- Priority alerts

### Operations Dashboard
Detailed operational metrics:
- Task status breakdown
- Overdue and blocked task lists
- Project health details
- Action items summary
- Velocity metrics
- Recommendations

## Output Formats

- **markdown** (default): Terminal-friendly tables
- **slack**: Slack Block Kit JSON for posting
- **json**: Raw data for programmatic use
