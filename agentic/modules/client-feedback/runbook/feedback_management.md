# Client Feedback Management

## Purpose

Triage, track, and respond to client testing feedback submitted via Notion. This runbook defines the workflow from submission to resolution, ensuring consistent handling and timely responses.

## When to Use This Directive

**Trigger phrases:**
- "New client feedback came in"
- "Triage client feedback"
- "Check client feedback status"
- "Respond to client feedback"
- "Link feedback to task"
- "Review open feedback"
- "Client feedback statistics"

## Execution Tools

**Location:** `modules/client-feedback/tool/feedback_api.py`

---

## Quick Reference

```bash
# Create feedback
./run modules/client-feedback/tool/feedback_api.py create \
  --title "Issue description" \
  --type "Bug" \
  --severity "High" \
  --description "Detailed description"

# Query open feedback
./run modules/client-feedback/tool/feedback_api.py query --open

# Query by status
./run modules/client-feedback/tool/feedback_api.py query --status "Submitted"

# Triage feedback
./run modules/client-feedback/tool/feedback_api.py triage <page_id> \
  --priority "High" \
  --notes "Root cause identified in auth service"

# Respond to feedback
./run modules/client-feedback/tool/feedback_api.py respond <page_id> \
  --response "We've identified the issue and deployed a fix."

# Resolve feedback
./run modules/client-feedback/tool/feedback_api.py resolve <page_id> \
  --summary "Fixed null pointer in login handler. Deployed v2.3.1"

# Get statistics
./run modules/client-feedback/tool/feedback_api.py stats
```

---

## Status Workflow

```
Submitted → Triaging → In Progress → Responded → Resolved → Closed
                ↓              ↑
           Needs Info ─────────┘
```

### Status Definitions

| Status | Meaning | Next Action |
|--------|---------|-------------|
| **Submitted** | Client submitted, awaiting triage | Team member picks up and triages |
| **Triaging** | Under review, assigning priority | Determine if task needed or quick response |
| **Needs Info** | Question posted to client | Wait for client response |
| **In Progress** | Work actively happening | Complete work, then respond |
| **Responded** | Response provided to client | Wait for client confirmation |
| **Resolved** | Client confirmed resolution | Auto-close after 7 days |
| **Closed** | Feedback cycle complete | Archive |

### Status Transitions

```bash
# Submitted → Triaging (assign priority)
./run modules/client-feedback/tool/feedback_api.py triage <id> --priority "High"

# Triaging → Needs Info (question for client)
./run modules/client-feedback/tool/feedback_api.py update <id> --status "Needs Info"

# Needs Info → In Progress (got answer, working)
./run modules/client-feedback/tool/feedback_api.py update <id> --status "In Progress"

# In Progress → Responded (answer provided)
./run modules/client-feedback/tool/feedback_api.py respond <id> --response "Here's the solution..."

# Responded → Resolved (client confirms)
./run modules/client-feedback/tool/feedback_api.py resolve <id> --summary "Issue resolved by..."
```

---

## Triage SOP

When feedback is submitted:

### 1. Review Submission
```bash
./run modules/client-feedback/tool/feedback_api.py get <page_id>
```

Check:
- Is the description clear enough to understand?
- Is it reproducible (for bugs)?
- Does it need immediate attention (Critical/Urgent)?

### 2. Assign Priority

Map **Severity** (client-assigned) to **Priority** (team-assigned):

| Severity | Typical Priority | Criteria |
|----------|------------------|----------|
| Critical | Urgent | System down, data loss, blocking all work |
| High | High | Major feature broken, workaround difficult |
| Medium | Medium | Feature issue, workaround exists |
| Low | Low | Cosmetic, nice-to-have, minor annoyance |

Priority can differ from severity based on:
- Business impact
- Number of users affected
- Deadline proximity
- Workaround availability

### 3. Triage Decision Tree

```
Is it a question?
  └── Yes → Answer directly → Status: Responded
  └── No ↓

Is more info needed?
  └── Yes → Ask client → Status: Needs Info
  └── No ↓

Is it a quick fix (<30 min)?
  └── Yes → Fix directly → Status: Responded → Resolved
  └── No ↓

Create task → Status: In Progress
```

### 4. Execute Triage

```bash
# Set priority and move to Triaging
./run modules/client-feedback/tool/feedback_api.py triage <page_id> \
  --priority "High" \
  --notes "Auth service issue affecting login. Need to investigate OAuth flow."
```

---

## Task Creation Flow

When feedback requires substantive work (>30 min), create a linked task:

### 1. Create Task in Tasks DB

Use the Notion API or manual creation:
- Title: `[FB-YYMMDD-xxxx] Original feedback title`
- Type: Deep Work
- Priority: Map from feedback priority
- Notes: Include feedback URL and description

### 2. Link Task to Feedback

```bash
./run modules/client-feedback/tool/feedback_api.py link <feedback_id> <task_id>
```

### 3. Update Feedback Status

```bash
./run modules/client-feedback/tool/feedback_api.py update <feedback_id> --status "In Progress"
```

### Priority Mapping

| Feedback Priority | Task Priority |
|-------------------|---------------|
| Urgent | Urgent |
| High | High |
| Medium | Medium |
| Low | Low |

---

## Response Guidelines

### Effective Responses Include:
1. **Acknowledgment** - Confirm you understand the issue
2. **Explanation** - What was happening and why
3. **Resolution** - What was done to fix it
4. **Next steps** - If any further action needed

### Response Template

```
We've investigated the [issue type] you reported.

**What happened:** [Brief explanation]

**What we did:** [Action taken]

**Status:** [Fixed/Workaround provided/In progress]

[If applicable: Please verify by doing X and let us know if the issue persists.]
```

### Response Command

```bash
./run modules/client-feedback/tool/feedback_api.py respond <page_id> \
  --response "We've identified and fixed the login issue. The fix has been deployed. Please try logging in again and let us know if you still experience problems."
```

---

## Module Usage (Python Import)

```python
from modules.client_feedback.tool.feedback_api import FeedbackClient

client = FeedbackClient()

# Create feedback
feedback = client.create_feedback(
    title="Login button not working",
    request_type="Bug",
    severity="High",
    description="Clicking login does nothing"
)

# Query open feedback
open_items = client.get_open_feedback()

# Triage
client.triage_feedback(
    page_id=feedback["id"],
    priority="High",
    internal_notes="Auth service investigation needed"
)

# Respond
client.respond_to_feedback(
    page_id=feedback["id"],
    response_text="Fixed in v2.3.1"
)

# Resolve
client.resolve_feedback(
    page_id=feedback["id"],
    resolution_summary="Null pointer in auth handler fixed"
)

# Get stats
stats = client.get_stats()
print(f"Open: {stats['open']}, Closed: {stats['closed']}")
```

---

## Environment Variables

Required in `.env`:
```
NOTION_API_KEY=secret_xxxxx
CLIENT_FEEDBACK_DB_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### Getting the Database ID

1. Open Client Feedback database in Notion
2. Click Share → Copy link
3. Extract ID from URL: `notion.so/{workspace}/{DATABASE_ID}?v=...`
4. Add to `.env` file

### Database Setup

The Client Feedback database needs these properties:

| Property | Type | Configuration |
|----------|------|---------------|
| Title | Title | - |
| Feedback ID | Formula | `"FB-" + formatDate(prop("Created"), "YYMMDD") + "-" + slice(id(), 0, 4)` |
| Status | Select | Submitted, Triaging, Needs Info, In Progress, Responded, Resolved, Closed |
| Request Type | Select | Urgent Issue, Bug, Change Request, Enhancement, Question |
| Severity | Select | Critical, High, Medium, Low |
| Priority | Select | Urgent, High, Medium, Low |
| Description | Rich Text | - |
| Steps to Reproduce | Rich Text | - |
| Response | Rich Text | - |
| Internal Notes | Rich Text | - |
| Resolution Summary | Rich Text | - |
| Related Tasks | Relation | Link to Tasks DB (two-way) |
| Client | Relation | Link to Contacts DB |
| Company | Relation | Link to Companies DB |
| Project | Relation | Link to Projects DB |
| Assigned To | Person | - |
| Attachments | Files | - |
| Created | Created time | Auto-populated |

---

## Edge Cases & Learnings

### Duplicate Submissions
- Client submits same issue twice
- Solution: Search by title before creating, link duplicates together
- Mark duplicate as Closed with note "Duplicate of FB-XXXXXX"

### Feedback ID Formula
- Uses created date + first 4 chars of page ID
- Format: `FB-260204-a1b2`
- Human-readable, sortable, unique enough for ~16 items/day

### Relation Setup
- Relations to Contacts/Companies/Projects are optional
- Can be populated manually or via form URL params
- Client relation enables filtering portal views

### SLA Tracking
- No built-in SLA field (keeps schema simple)
- Use Created time + Status changes for SLA calculation
- n8n automation checks for overdue items daily

### Client Portal Visibility
- Clients see: Feedback ID, Title, Type, Status, Response
- Clients hidden: Internal Notes, Assigned To, Priority (triage-assigned)
- Create filtered view that excludes these properties

---

## Common Workflows

### Morning Triage

```bash
# Check new submissions
./run modules/client-feedback/tool/feedback_api.py query --status "Submitted"

# Check items needing info response
./run modules/client-feedback/tool/feedback_api.py query --status "Needs Info"

# Overall stats
./run modules/client-feedback/tool/feedback_api.py stats
```

### End of Day Wrap-up

```bash
# Check in-progress items
./run modules/client-feedback/tool/feedback_api.py query --status "In Progress"

# Update any responded items to resolved
./run modules/client-feedback/tool/feedback_api.py resolve <id> --summary "..."
```

### Weekly Review

```bash
# Full statistics
./run modules/client-feedback/tool/feedback_api.py stats

# All open items
./run modules/client-feedback/tool/feedback_api.py query --open
```

---

## Troubleshooting

### "CLIENT_FEEDBACK_DB_ID not configured"
Add the database ID to your `.env` file. Get it from the Notion database URL.

### "Invalid status/type/severity/priority"
Check that the value matches exactly (case-sensitive):
- Status: Submitted, Triaging, Needs Info, In Progress, Responded, Resolved, Closed
- Type: Urgent Issue, Bug, Change Request, Enhancement, Question
- Severity/Priority: Critical, High, Medium, Low

### "Feedback not found"
- Verify the page ID is correct (32-character UUID)
- Check that the page hasn't been deleted
- Ensure your Notion integration has access to the database

### "Relation property not found"
The Related Tasks, Client, Company, Project relations may not be set up yet. These are optional and can be added to the database schema as needed.

---

## Related Directives

- `runbooks/notion_management.md` - General Notion operations
- `runbooks/client_onboarding.md` - Portal setup during onboarding
- `runbooks/slack_management.md` - Slack notifications
