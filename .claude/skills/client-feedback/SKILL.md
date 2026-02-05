# Client Feedback Skill

## Purpose

Manage client testing feedback through a standardized Notion-based workflow. Supports submission, triage, response, and resolution tracking for client feedback during testing phases.

## When to Use This Skill

- "New feedback from client"
- "Triage client feedback"
- "Respond to client feedback"
- "Check open client feedback"
- "Client feedback stats"
- "Review feedback queue"
- "What's the status of client feedback?"
- "Mark feedback as resolved"

## Prerequisites

- Notion API key configured in `.env` as `NOTION_API_KEY`
- Client Feedback database ID in `.env` as `CLIENT_FEEDBACK_DB_ID`
- Database shared with Notion integration
- Database schema configured per runbook

## Skill Workflow

### Phase 1: Understand Request

When invoked, determine the action:

| Intent | Action |
|--------|--------|
| Check status/queue | Query open feedback |
| Triage new item | Get item, assign priority |
| Respond to client | Update with response |
| Mark resolved | Add resolution summary |
| Get statistics | Run stats command |

### Phase 2: Execute Action

**Query Open Feedback:**
```bash
./run modules/client-feedback/tool/feedback_api.py query --open
```

**Query by Status:**
```bash
./run modules/client-feedback/tool/feedback_api.py query --status "Submitted"
```

**Triage Feedback:**
```bash
./run modules/client-feedback/tool/feedback_api.py triage <page_id> \
  --priority "High" \
  --notes "Internal notes about triage decision"
```

**Respond to Feedback:**
```bash
./run modules/client-feedback/tool/feedback_api.py respond <page_id> \
  --response "Response text visible to client"
```

**Resolve Feedback:**
```bash
./run modules/client-feedback/tool/feedback_api.py resolve <page_id> \
  --summary "How the issue was resolved"
```

**Get Statistics:**
```bash
./run modules/client-feedback/tool/feedback_api.py stats
```

### Phase 3: Report Results

After executing:
1. Summarize what was done
2. Show relevant counts (open items, by status)
3. Highlight any urgent/critical items
4. Suggest next actions if applicable

## Status Workflow

```
Submitted → Triaging → In Progress → Responded → Resolved → Closed
                ↓              ↑
           Needs Info ─────────┘
```

## Command Reference

### Create Feedback
```bash
./run modules/client-feedback/tool/feedback_api.py create \
  --title "Brief description" \
  --type "Bug" \
  --severity "High" \
  --description "Detailed description" \
  --steps "Steps to reproduce"
```

**Type options:** Urgent Issue, Bug, Change Request, Enhancement, Question
**Severity options:** Critical, High, Medium, Low

### Query Feedback
```bash
./run modules/client-feedback/tool/feedback_api.py query \
  --status "Submitted" \
  --type "Bug" \
  --severity "High" \
  --priority "Urgent" \
  --limit 20 \
  --open
```

### Get Single Item
```bash
./run modules/client-feedback/tool/feedback_api.py get <page_id>
```

### Update Feedback
```bash
./run modules/client-feedback/tool/feedback_api.py update <page_id> \
  --status "In Progress" \
  --priority "High" \
  --internal-notes "Working on fix"
```

### Triage
```bash
./run modules/client-feedback/tool/feedback_api.py triage <page_id> \
  --priority "High" \
  --notes "Root cause analysis notes"
```

### Respond
```bash
./run modules/client-feedback/tool/feedback_api.py respond <page_id> \
  --response "Response text for client" \
  --status "Responded"
```

### Resolve
```bash
./run modules/client-feedback/tool/feedback_api.py resolve <page_id> \
  --summary "Resolution summary"
```

### Link to Task
```bash
./run modules/client-feedback/tool/feedback_api.py link <feedback_id> <task_id>
```

### Statistics
```bash
./run modules/client-feedback/tool/feedback_api.py stats
```

## Triage Decision Guide

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

## Priority Mapping

| Severity (client-set) | Typical Priority (team-set) |
|-----------------------|-----------------------------|
| Critical | Urgent |
| High | High |
| Medium | Medium |
| Low | Low |

Priority may differ from severity based on business impact, deadline, workaround availability.

## Response Template

When responding to clients, include:

```
We've investigated the [issue type] you reported.

**What happened:** [Brief explanation]

**What we did:** [Action taken]

**Status:** [Fixed/Workaround provided/In progress]

[If applicable: Please verify by doing X and let us know if the issue persists.]
```

## Common Workflows

### Morning Triage
1. Query submitted items: `--status "Submitted"`
2. For each: review, assign priority, update status
3. Check needs-info items for responses

### Weekly Review
1. Run stats command
2. Review all open items
3. Follow up on stale items (no update >3 days)

## Error Handling

- **Missing database ID:** Add `CLIENT_FEEDBACK_DB_ID` to `.env`
- **Invalid status/type:** Use exact values from options lists
- **Page not found:** Verify page ID, check database access

## Related Skills

- `/notion-sync` - Push documents to Notion
- `/dashboard` - Weekly metrics including feedback stats
