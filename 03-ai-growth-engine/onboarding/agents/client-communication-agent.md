# Client Communication Agent

**Type:** Claude Code Agent
**Status:** Specification
**Created:** 2026-01-18

---

## Purpose

Monitor client communication channels, flag urgent messages, generate progress update drafts, and ensure SLA compliance for response times.

---

## Trigger

- **Scheduled:** 2x daily (12pm PT, 5pm PT)
- **Event-based:** New message in monitored channels (optional real-time)

---

## Responsibilities

### 1. Monitor Client Slack Channels
- Scan all `#clientname` channels for new messages
- Identify messages requiring response
- Track time since last response

### 2. Flag Urgent Messages
- Detect urgency keywords: "urgent", "ASAP", "blocker", "emergency", "critical"
- Detect question patterns requiring immediate response
- Alert via notification if message is > 2 hours without response

### 3. Generate Progress Update Drafts
- Run on Tuesday and Friday at 4pm PT
- Pull recent activity from Notion project records
- Generate structured update following template
- Save as draft for human review before sending

### 4. Track Response Time SLA
- Log response times per client
- Flag SLA violations (> 2 hours during availability window)
- Generate weekly SLA report

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Client Slack Channels | Slack API | Yes |
| Project Status | Notion | Yes |
| Urgency Keywords | Config | Yes |
| SLA Thresholds | Config | Yes |
| Communication Window | Config | Yes |

---

## Outputs

| Output | Destination | Format |
|--------|-------------|--------|
| Urgent Message Alert | Slack DM to team | Notification |
| Progress Update Draft | Notion/Drafts | Markdown |
| SLA Violation Alert | Slack #ops | Notification |
| Weekly SLA Report | Notion | Report document |

---

## Communication Frequency Protocol

### Standard Cadence
| Type | Frequency | Day/Time | Channel |
|------|-----------|----------|---------|
| Progress Update | 2x weekly | Tue & Fri EOD | Slack + Email |
| Slack Availability | Daily | 12-2pm PT | Slack |
| Urgent Response | As needed | < 2 hours | Slack |

### Progress Update Template

```markdown
## Progress Update: {{date}}

### Completed This Period
- {{completed_task_1}}
- {{completed_task_2}}

### In Progress
- {{in_progress_task}} - {{percent_complete}}%

### Blockers (if any)
- {{blocker_description}} - Need: {{what_needed}}

### Next Steps
- {{next_action}}

### Win Condition Progress
{{#each win_conditions}}
- {{name}}: {{status}}
{{/each}}

---
*Next update: {{next_update_date}}*
```

---

## Urgency Detection

### Keywords (Case-Insensitive)
- `urgent`
- `asap`
- `blocker`
- `blocked`
- `emergency`
- `critical`
- `immediately`
- `today`
- `right now`

### Question Patterns
- Ends with `?` and no response > 4 hours
- Contains "when will" or "how long"
- Contains "waiting for" or "still waiting"

### Alert Format

```
:rotating_light: URGENT CLIENT MESSAGE

Client: #{{channel_name}}
Message: "{{message_preview}}"
Time: {{timestamp}} ({{time_ago}})
Link: {{message_link}}

Action needed: Respond within {{sla_remaining}}
```

---

## Implementation

### Scheduled Scan (2x Daily)

```
[Cron: 12pm PT, 5pm PT]
        │
        ▼
[Get All Client Channels]
        │
        ▼
[For Each Channel]
        │
        ├──▶ [Get Messages Since Last Scan]
        │           │
        │           ▼
        │    [Check for Urgency Keywords]
        │           │
        │           ▼
        │    [Check Response Time]
        │           │
        │           ▼
        │    [Flag if Urgent or SLA Violation]
        │
        ▼
[Aggregate Alerts]
        │
        ▼
[Send Consolidated Alert if Any]
```

### Progress Update Generation (Tue/Fri 4pm PT)

```
[Cron: Tue & Fri 4pm PT]
        │
        ▼
[Get Active Projects from Notion]
        │
        ▼
[For Each Project]
        │
        ├──▶ [Get Recent Tasks (Completed/In Progress)]
        │           │
        │           ▼
        │    [Get Win Condition Status]
        │           │
        │           ▼
        │    [Generate Update Draft via Claude]
        │           │
        │           ▼
        │    [Save to Notion Drafts]
        │
        ▼
[Notify: "X progress updates ready for review"]
```

---

## Error Handling

| Error | Action |
|-------|--------|
| Slack API rate limit | Back off, retry in 60 sec |
| Channel not found | Log, skip, alert ops |
| Notion API error | Retry 3x, fallback to cached data |

---

## Monitoring

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Scan completion | 100% | Any failure |
| Urgent messages caught | 100% | Missed urgent |
| Progress updates generated | 100% Tue/Fri | Missing update |
| SLA compliance | > 95% | < 90% |

---

## Configuration

```yaml
client_communication_agent:
  scan_schedule:
    - "0 12 * * *"  # 12pm PT daily
    - "0 17 * * *"  # 5pm PT daily

  progress_update_schedule:
    - "0 16 * * 2"  # 4pm PT Tuesday
    - "0 16 * * 5"  # 4pm PT Friday

  urgency_keywords:
    - urgent
    - asap
    - blocker
    - blocked
    - emergency
    - critical

  sla_thresholds:
    availability_window:
      start: "12:00"
      end: "14:00"
      timezone: "America/Los_Angeles"
    urgent_response: 120  # minutes
    normal_response: 1440  # minutes (24 hours)

  channel_prefix: "#"
  internal_suffix: "-internal"
```

---

## Dependencies

- Slack API with message read permissions
- Notion API for project data
- Claude Code for update generation
- Cron scheduler (n8n or system)
