# Automation Workflows

Specifications for n8n/automation workflows to power the customer journey.

---

## Overview

| Workflow | Trigger | Actions |
|----------|---------|---------|
| Outreach Follow-Up | No response | Send follow-up sequence |
| Discovery Booking | Call booked | Send confirmation + intake form |
| Discovery Reminder | 24hr before call | Send reminder email |
| No-Show Handler | Meeting missed | Send reschedule email |
| Audit Offer Follow-Up | No response to offer | Send follow-up sequence |
| Payment Received | Invoice paid | Trigger onboarding sequence |
| Welcome Sequence | Payment confirmed | Send welcome + onboarding form |
| Kickoff Scheduler | Onboarding form done | Schedule kickoff call |
| Weekly Update Reminder | Every Friday | Remind to send update |
| Check-In Sequence | Post-launch | Send scheduled check-ins |

---

## Workflow 1: Outreach Follow-Up

**Trigger:** Contact added to "Outreach" status, no response

```
TRIGGER: Contact status = "Outreach Sent"
         AND No reply after [X] days

ACTION 1: Send Follow-Up #1
ACTION 2: Wait [X] days
ACTION 3: Check for response
          IF response → Stop workflow
          IF no response → Continue
ACTION 4: Send Follow-Up #2
ACTION 5: Wait [X] days
ACTION 6: Check for response
          IF response → Stop workflow
          IF no response → Move to "Nurture"
```

**n8n Nodes:**
- Trigger: Schedule or Webhook
- CRM: Check contact status
- Wait: Delay node
- Email: Send template
- CRM: Update status

---

## Workflow 2: Discovery Booking Confirmation

**Trigger:** Discovery call booked (Calendly webhook)

```
TRIGGER: Calendly webhook - new booking

ACTION 1: Create/update contact in CRM
ACTION 2: Send booking confirmation email
ACTION 3: Send intake form
ACTION 4: Create calendar event (if not auto)
ACTION 5: Set reminder for 24hr before
ACTION 6: Update CRM status to "Discovery Scheduled"
```

**n8n Nodes:**
- Trigger: Webhook (Calendly)
- CRM: Create/update contact
- Email: Send confirmation
- Forms: Send intake form link
- CRM: Update status

---

## Workflow 3: Payment Received → Onboarding

**Trigger:** Invoice marked paid (Stripe webhook)

```
TRIGGER: Stripe webhook - payment successful

ACTION 1: Update CRM deal status to "Won"
ACTION 2: Send welcome email (handoff)
ACTION 3: Wait 1 hour
ACTION 4: Send welcome packet email
ACTION 5: Send onboarding form
ACTION 6: Create project in PM tool
ACTION 7: Notify delivery team
ACTION 8: Log payment in accounting
```

**n8n Nodes:**
- Trigger: Webhook (Stripe)
- CRM: Update deal status
- Email: Send welcome sequence
- Wait: Delay between emails
- PM Tool: Create project
- Slack: Notify team
- Accounting: Log payment

---

## Workflow 4: Post-Launch Check-In Sequence

**Trigger:** Project marked "Live"

```
TRIGGER: Project status = "Live"

ACTION 1: Wait [X] days (Check-in #1 timing)
ACTION 2: Send Check-in #1 email
ACTION 3: Wait [X] days
ACTION 4: Send Check-in #2 email
ACTION 5: Wait [X] days
ACTION 6: Send Check-in #3 email
ACTION 7: Move to "Retain" stage
ACTION 8: Schedule monthly check-in
```

**n8n Nodes:**
- Trigger: CRM/PM status change
- Wait: Delay nodes
- Email: Send check-in templates
- CRM: Update status
- Calendar: Schedule recurring

---

## Integration Requirements

### Required Connections

| System | Purpose | Auth Type |
|--------|---------|-----------|
| CRM (HubSpot/etc) | Contact + deal management | API Key / OAuth |
| Calendly | Booking management | API Key |
| Stripe | Payment processing | API Key |
| Gmail/SMTP | Email sending | OAuth / SMTP |
| Slack | Team notifications | OAuth |
| Zoom | Meeting links | OAuth |
| Google Drive | Document storage | OAuth |
| PM Tool | Project management | API Key |

### Webhook Endpoints Needed

| Source | Event | Workflow |
|--------|-------|----------|
| Calendly | booking.created | Discovery booking |
| Calendly | booking.canceled | Handle cancellation |
| Stripe | payment_intent.succeeded | Payment received |
| Typeform | form.submitted | Intake/onboarding form |
| CRM | deal.updated | Status changes |

---

## Email Templates in n8n

Store email templates as:
1. **n8n nodes** - HTML in Code node
2. **External** - Google Docs / Notion
3. **Email tool** - SendGrid templates

**Recommended:** Use variables for personalization

```
Variables:
{{contact.firstName}}
{{contact.email}}
{{company.name}}
{{deal.amount}}
{{meeting.date}}
{{meeting.time}}
{{meeting.link}}
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Email fails to send | Retry 3x, then alert team |
| Webhook fails | Log error, retry, alert |
| CRM update fails | Queue for retry, alert |
| Payment webhook duplicate | Check idempotency, skip if exists |

---

## Monitoring

**Track:**
- Workflow execution success rate
- Email delivery rate
- Webhook reliability
- Sequence completion rate

**Alerts:**
- Workflow failure
- High bounce rate
- Missed SLA (response time)

---

## Next Steps

1. [ ] Set up n8n instance
2. [ ] Connect integrations
3. [ ] Build workflows one at a time
4. [ ] Test with sample data
5. [ ] Go live with monitoring
6. [ ] Iterate based on results
