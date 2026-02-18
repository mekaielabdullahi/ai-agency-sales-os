# n8n Cold Email Engine Spec
## Matthew's Build Spec

---

## Overview

Matthew builds the n8n cold email engine during Week 0-1 (2/16 - 2/28). Five core workflows:

1. **Inbox Rotation** - Round-robin sending across 15 accounts
2. **Warmup Workflow** - Build inbox reputation before cold sends
3. **Send Scheduler** - Timed campaign sends from Google Sheet
4. **Bounce Handler** - Auto-detect and manage bounces
5. **Reply Detector** - Classify and route replies

---

## Workflow 1: Inbox Rotation

**Purpose:** Distribute sends evenly across 15 inboxes to stay under per-inbox limits.

**Logic:**
1. Receive send request (lead email, subject, body, vertical)
2. Query inbox status tracker (Google Sheet or internal state)
3. Select next available inbox (round-robin, skip any paused for bounce rate)
4. Send via SMTP using selected inbox credentials
5. Log: inbox used, timestamp, lead ID, message-id
6. Increment daily send count for that inbox

**Configuration:**
| Parameter | Value |
|-----------|-------|
| Total inboxes | 15 |
| Max sends per inbox per day | 30 |
| Max total sends per day | 450 |
| Rotation method | Round-robin |
| Pause trigger | Bounce rate > 5% for that inbox |

**SMTP Credentials (15 accounts):**
Store in n8n credentials manager. Each inbox needs:
- SMTP host: smtp.gmail.com
- SMTP port: 587 (TLS)
- Username: [inbox email]
- Password: [app password]

---

## Workflow 2: Warmup

**Purpose:** Build inbox reputation over 14 days before cold sends.

**Logic:**
1. Cron trigger: Run every 2 hours during business hours
2. For each inbox pair (15 inboxes = many pairs):
   - Send a conversational email from Inbox A to Inbox B
   - After 5-15 min delay: Inbox B opens and replies
   - Both mark the thread as important
3. Gradually increase volume:

| Days | Emails per inbox per day |
|------|-------------------------|
| 1-3 | 5 |
| 4-7 | 10 |
| 8-11 | 20 |
| 12-14 | 30 |

**Email content:** Use varied, natural-sounding email templates (not identical). Mix of:
- Meeting scheduling
- Project updates
- Quick questions
- File sharing references

**Completion criteria:** 14 days at increasing volume with no spam flags.

---

## Workflow 3: Send Scheduler

**Purpose:** Pull leads from Google Sheet and send campaign emails on schedule.

**Logic:**
1. Cron trigger: Tue-Thu, 9:00-11:00 AM (run every 15 min during window)
2. Query Google Sheet for rows where:
   - Status = "Ready to Send"
   - Next Email Date <= today
   - Vertical matches current batch (printing)
3. For each qualifying row:
   - Determine email number (1-4) from "Last Email Sent" column
   - Load corresponding email template
   - Merge personalization variables (First Name, Company, Icebreaker, etc.)
   - Pass to Inbox Rotation workflow
   - Update Google Sheet: Last Email Sent, Last Send Date, Status, Message-ID
4. For emails 2-4: Set In-Reply-To header to Email 1's Message-ID (threading)

**Google Sheet Columns:**
| Column | Description |
|--------|-------------|
| Lead ID | Unique identifier |
| First Name | Prospect first name |
| Company | Company name |
| Email | Prospect email |
| Vertical | "Printing" |
| Icebreaker | AI-generated personalized opener |
| Status | New / Ready to Send / Sent-1 / Sent-2 / Sent-3 / Sent-4 / Reply / Bounce / Opted Out |
| Last Email Sent | 0-4 |
| Last Send Date | Date of last email |
| Next Email Date | Calculated: Last Send Date + gap days |
| Message-ID | Email 1 Message-ID for threading |
| Inbox Used | Which inbox sent |
| Notes | Manual notes |

**Gap between emails:**
| From | To | Gap |
|------|----|-----|
| Email 1 | Email 2 | 4 days |
| Email 2 | Email 3 | 4 days |
| Email 3 | Email 4 | 4 days |

---

## Workflow 4: Bounce Handler

**Purpose:** Detect bounces and protect inbox reputation.

**Logic:**
1. IMAP listener on all 15 inboxes (check every 5 min)
2. Detect bounce emails by:
   - Subject contains "Undeliverable", "Delivery Status Notification", "Mail Delivery Failed"
   - From contains "mailer-daemon", "postmaster"
3. On bounce detected:
   - Extract original recipient email
   - Update Google Sheet: Status = "Bounce"
   - Increment bounce counter for sending inbox
   - If inbox bounce rate > 5%: **Pause that inbox** (set status to "Paused" in inbox tracker)
4. Alert (Slack/email to Mekaiel) when:
   - Any inbox is paused
   - Overall bounce rate exceeds 3%
   - 5+ bounces in a single day

**Bounce Rate Calculation:**
`Bounce Rate = (Bounces from Inbox / Total Sends from Inbox) * 100`

Calculated on a rolling 7-day window.

---

## Workflow 5: Reply Detector

**Purpose:** Detect, classify, and route replies to appropriate follow-up workflows.

**Logic:**
1. IMAP listener on all 15 inboxes (check every 5 min)
2. Detect reply emails (In-Reply-To matches a sent Message-ID)
3. Classify sentiment using `sales_interaction_agent.json`:
   - **Positive:** Interested, wants to talk, asks questions about the offer
   - **Neutral:** Asks a question, not clearly interested or uninterested
   - **Negative:** Not interested, unsubscribe request, angry
4. Route based on classification:

| Classification | Action |
|---------------|--------|
| Positive | Alert Mekaiel immediately (Slack + email). Trigger `pre_meeting_sequence.json`. Update Sheet: Status = "Positive Reply" |
| Neutral | Alert Mekaiel. Add to `nurture_sequence.json` (60-day cycle). Update Sheet: Status = "Neutral Reply" |
| Negative | Remove from all sequences. Update Sheet: Status = "Opted Out". Never contact again. |

**Response time target:** Mekaiel responds to positive replies within 1 hour.

---

## Google Sheet Structure

### Tab 1: Dashboard
- Total leads by vertical
- Emails sent this week
- Open rate (if tracking pixels used)
- Reply rate
- Bounce rate
- Positive reply %
- Inbox health (sends per inbox, bounce rate per inbox)

### Tab 2: Lead Tracker
- All lead data + email status columns (see Send Scheduler section)

### Tab 3: ICP Refinement
- Logged after every positive reply: Company, sub-niche, size, revenue, responder title, pain point (their words), outcome

### Tab 4: Deliverability
- Per-inbox stats: sends, bounces, bounce rate, status (active/paused/warming)

---

## Existing n8n Workflows to Integrate

| Workflow | File | Integration Point |
|----------|------|-------------------|
| Nurture Sequence | `nurture_sequence.json` | Neutral replies and no-reply-after-4 leads |
| Pre-Meeting Sequence | `pre_meeting_sequence.json` | Positive replies |
| Post-Call Follow-up | `post_call_followup.json` | After discovery calls |
| Proposal Assembly | `proposal_assembly.json` | Qualified leads after discovery |
| Sales Interaction Agent | `sales_interaction_agent.json` | Reply sentiment classification |

---

## Lead Scraping Workflows (Upstream)

See `n8n-workflow-templates.md` for lead generation workflows that feed into this engine:

| Workflow | Purpose | Output |
|----------|---------|--------|
| Apollo to Airtable | One-click lead scraping | Qualified leads |
| LinkedIn Enrichment Pipeline | Email enrichment | Leads with verified emails |
| Hiring Signals Scraper | Activity detection | Prioritized leads |
| Apollo + Apify Combined | Multi-source enrichment | Fully enriched leads |

**Data flow:** Lead Scraping Workflows → Google Sheet (Tab 2: Lead Tracker) → Send Scheduler

---

## Build Priority Order

| Priority | Workflow | Dependency |
|----------|----------|------------|
| 1 | Warmup | Needs to start Day 1 (14-day warmup period) |
| 2 | Inbox Rotation | Foundation for Send Scheduler |
| 3 | Bounce Handler | Must be active before first cold send |
| 4 | Send Scheduler | Ready by end of Week 1 |
| 5 | Reply Detector | Ready by first campaign launch (2/24) |

---

## Testing Checklist

- [ ] Warmup: 15 inboxes sending/receiving/replying to each other
- [ ] Inbox Rotation: Sends round-robin, respects daily limits, skips paused inboxes
- [ ] Send Scheduler: Pulls "Ready to Send" rows, merges templates, sends on schedule
- [ ] Bounce Handler: Detects bounces, updates sheet, pauses inbox at >5%
- [ ] Reply Detector: Classifies positive/neutral/negative correctly, routes to right workflow
- [ ] End-to-end: New lead added -> personalized -> sent -> reply detected -> routed
