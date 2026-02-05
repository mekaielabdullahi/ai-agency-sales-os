# Client Feedback Module

Standardized async feedback system for client testing communication. Replaces mixed channels (Slack, email, calls, texts) with a structured Notion-based workflow.

## Purpose

- Allow clients to submit feedback directly to Notion via forms
- Full triage workflow (Status + Priority + Type + Severity)
- Team transparency via shared database views
- Dev responds via Notion comments
- Scales across multiple clients (5-15 requests/week per client)

## Quick Start

```bash
# Create new feedback entry
./run modules/client-feedback/tool/feedback_api.py create \
  --title "Login button not working" \
  --type "Bug" \
  --severity "High" \
  --client "Plotter Mechanix" \
  --description "Button shows but doesn't respond to clicks"

# Query feedback by client
./run modules/client-feedback/tool/feedback_api.py query --client "Plotter Mechanix"

# Query feedback by status
./run modules/client-feedback/tool/feedback_api.py query --status "Submitted"

# Update feedback status
./run modules/client-feedback/tool/feedback_api.py update <page_id> --status "In Progress"

# Link feedback to task
./run modules/client-feedback/tool/feedback_api.py link <feedback_id> <task_id>
```

## Database Schema

| Field | Type | Options |
|-------|------|---------|
| Title | Title | Brief description |
| Feedback ID | Formula | Auto-generated (FB-YYMMDD-xxxx) |
| Status | Select | Submitted, Triaging, Needs Info, In Progress, Responded, Resolved, Closed |
| Request Type | Select | Urgent Issue, Bug, Change Request, Enhancement, Question |
| Severity | Select | Critical, High, Medium, Low |
| Priority | Select | Urgent, High, Medium, Low (triage-assigned) |
| Client | Relation | Contacts DB |
| Company | Relation | Companies DB |
| Project | Relation | Projects DB |
| Description | Rich Text | Detailed description |
| Steps to Reproduce | Rich Text | For bugs |
| Attachments | Files | Screenshots, videos |
| Assigned To | Person | Team member |
| Response | Rich Text | Official response to client |
| Internal Notes | Rich Text | Team-only (hidden from client view) |
| Related Tasks | Relation | Tasks DB (bidirectional) |
| Resolution Summary | Rich Text | How resolved |

## Status Workflow

```
Submitted → Triaging → In Progress → Responded → Resolved → Closed
                ↓              ↑
           Needs Info ─────────┘
```

## Setup

1. Create "Client Feedback" database in Notion with schema above
2. Share database with your Notion integration
3. Add database ID to `.env`:
   ```
   CLIENT_FEEDBACK_DB_ID=your-database-id-here
   ```
4. Run `/agentic-sync` to update symlinks

## Client Access

Clients submit via Notion Form (shared URL, not database access):
- Form pre-fills Company/Project via URL params
- Client portal page with filtered view shows their submissions only
- Client sees: Feedback ID, Title, Type, Status, Response
- Client hidden: Internal Notes, Assigned To

## Related Modules

- `notion` - Base Notion API operations
- `client-onboarding` - Portal setup during onboarding
- `slack` - Notification automations
