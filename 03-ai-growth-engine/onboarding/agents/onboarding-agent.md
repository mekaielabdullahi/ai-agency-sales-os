# Onboarding Agent

**Type:** Claude Code Agent
**Status:** Specification
**Created:** 2026-01-18

---

## Purpose

Orchestrate the immediate post-payment onboarding sequence to minimize buyer remorse and create perception of progress within 5 minutes of payment.

---

## Trigger

- **Primary:** Stripe payment webhook (payment_intent.succeeded)
- **Fallback:** Notion database update → Status = "Paid"

---

## Responsibilities

### 1. Generate Personalized Gratitude Email
- Pull client data from CRM/Notion (name, project type, contact info)
- Personalize greeting and project reference
- Send within 30 seconds of trigger

### 2. Generate Next Steps Email (5-minute delay)
- Include correct calendar link for Logistics Onboarding Call
- Attach platform signup PDF based on project type
- Set expectations for what happens next

### 3. Create Slack Channels
- Create `#clientname` (client-facing)
- Create `#clientname-internal` (team-only)
- Apply correct naming convention (lowercase, hyphens)
- Add default team members

### 4. Update Notion Database
- Set `Onboarding Started` timestamp
- Set `Status` = "Onboarding"
- Link to created Slack channels

### 5. Notify Team
- Post in `#new-clients` with client summary
- Include project type, value, expected timeline

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Client Name | CRM/Notion | Yes |
| Client Email | CRM/Notion | Yes |
| Project Type | CRM/Notion | Yes |
| Project Value | CRM/Notion | No |
| Calendar Link | Config | Yes |
| Platform List | Project Type mapping | Yes |

---

## Outputs

| Output | Destination | Format |
|--------|-------------|--------|
| Gratitude Email | Client inbox | HTML email |
| Next Steps Email | Client inbox | HTML email + PDF |
| Slack Channels | Slack workspace | 2 channels |
| Notion Update | Projects database | Field updates |
| Team Notification | #new-clients | Slack message |

---

## Integration Points

| System | Method | Purpose |
|--------|--------|---------|
| Stripe | Webhook listener | Payment trigger |
| Notion | API | Read client data, write updates |
| Gmail | API | Send emails |
| Slack | API | Create channels, post messages |

---

## Implementation

### n8n Workflow Structure

```
[Stripe Webhook: payment_intent.succeeded]
        │
        ▼
[Get Client Data from Notion]
        │
        ▼
[Generate Gratitude Email]
        │
        ▼
[Send Email via Gmail]
        │
        ▼
[Wait 5 Minutes]
        │
        ▼
[Generate Next Steps Email]
        │
        ▼
[Get Platform PDF based on Project Type]
        │
        ▼
[Send Email with Attachment]
        │
        ▼
[Create Slack Channels]
        │
        ▼
[Update Notion: Onboarding Started]
        │
        ▼
[Post to #new-clients]
```

### Claude Code Enhancement

For email generation, use Claude to personalize:

```markdown
Generate a gratitude email for:
- Client Name: {{name}}
- Project Type: {{project_type}}

Requirements:
- Warm, genuine tone (not corporate)
- 3-4 sentences max
- Mention looking forward to the project
- Sign off with my name

Example tone:
"Hi [Name], thanks for taking care of that invoice so promptly. I'm beyond happy
that we get the chance to work together and excited to nail this for you..."
```

---

## Error Handling

| Error | Action |
|-------|--------|
| Stripe webhook fails | Alert ops team, manual trigger |
| Notion API error | Retry 3x, then alert |
| Email send fails | Retry, fallback to manual |
| Slack channel exists | Append timestamp to name |

---

## Monitoring

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Webhook to first email | < 30 sec | > 2 min |
| Email delivery success | 100% | Any failure |
| Channel creation success | 100% | Any failure |

---

## Testing

### Test Cases
1. New payment triggers full sequence
2. Email contains correct client name
3. Calendar link is correct
4. Slack channels created with correct names
5. Notion updated with timestamps
6. Team notification posted

### Test Client
- Use `test-client@arisegroup.ai`
- Notion record marked as `Test = true`
- Slack channels deleted after test

---

## Dependencies

- n8n instance with Stripe, Notion, Gmail, Slack integrations
- Notion database with required fields
- Gmail account with API access
- Slack workspace with bot permissions
- Platform PDF templates per project type
