# Eventbrite Setup Guide

**Purpose**: Configure Eventbrite for education event lead funnel
**Event Type**: Tier 1 Free Virtual Workshop

---

## Event Page Configuration

### Basic Information

**Event Title**:
```
AI Didn't Fail. Your Systems Did.
```

**Subtitle** (Tagline):
```
A 90-minute live workshop for business owners who tried AI tools and got nowhere. No recording. No replay. Just answers.
```

**Organizer**: AriseGroup.ai

**Event Type**: Webinar

**Event Category**: Business & Professional > Business

**Tags**: AI for business, Business automation, Small business AI, Process improvement, SOP creation, ChatGPT business, AI implementation, Operations efficiency, Business systems, AI strategy workshop

---

### Event Description (Copy)

```markdown
## Is AI the answer to your operational challenges? Maybe. But not the way most people think.

**The problem**: 70% of AI projects fail. Not because the technology doesn't work—but because businesses start with the wrong question.

They ask: "What AI tools should I use?"

They should ask: "What processes am I trying to improve?"

**This workshop flips the script.**

---

### In 90 minutes, you'll learn:

**The Process-First Framework**
Why starting with tools leads to failure—and what to do instead.

**The 10 Business Functions Model**
A simple way to map your entire operation and identify where AI actually fits.

**Your AI Quick Wins**
We'll do a live self-audit so you leave knowing YOUR top 2-3 opportunities.

**Real Demonstrations**
See actual AI workflows running in real businesses (not hypotheticals).

---

### This workshop is for you if:

- You're overwhelmed by AI options and don't know where to start
- You've tried AI tools but they didn't stick
- Manual processes are eating your time
- You want a systematic approach, not random experiments

---

### What you'll walk away with:

1. A completed self-audit of your business functions
2. Your personalized AI Opportunity Matrix
3. 2-3 specific quick wins you can implement in 30-90 days
4. Access to a free AI Readiness Audit (first 5 attendees)

---

### Your hosts:

**Mekaiel Abdullahi** - AI Implementation Specialist
Founder of AriseGroup.ai. Helps small businesses systematically adopt AI through process-first automation. Built AI operating systems for professional services firms, agencies, and nonprofits.

**Katrina [Last Name]** - Entrepreneur Educator
[Brief bio from Katrina]

---

### The details:

**Date**: [Event Date]
**Time**: [Event Time] [Timezone]
**Duration**: 90 minutes
**Format**: Live Zoom webinar (interactive)
**Price**: Free

**Limited to 150 registrations** to keep it interactive.

---

*Questions? Email mekaiel@arisegroup.ai*
```

---

## Eventbrite Ads (Paid Promotion)

**Budget**: $25/day
**Expected Fill Time**: ~1 week
**Total Spend**: $170-188

**Setup**:
1. Create event first (all details complete)
2. Go to Marketing > Eventbrite Ads
3. Set daily budget: $25
4. Target: Business professionals, entrepreneurs
5. Location: US (or specific markets)

**Action Items**:
- Monitor daily registrations
- Manually STOP ads when 150 cap reached
- Don't overspend - ads auto-continue otherwise

**ROI**: 150 qualified leads for <$200 = ~$1.25/lead

---

## Frequently Asked Questions

**1. Who is this workshop for?**
Business owners and operators (20-100 employees) who want to use AI but don't know where to start—or have tried and failed.

**2. Do I need technical experience?**
No. We focus on business processes, not coding. If you can use email, you can follow along.

**3. Will there be a recording?**
No. This is a live-only event. We do this intentionally to create an interactive experience with Q&A and breakout rooms.

**4. What AI tools will you cover?**
We focus on the framework, not specific tools. But we'll demo ChatGPT, Claude, and simple automations.

**5. Is this a sales pitch?**
No. You'll learn a complete framework. At the end, we offer a free AI Readiness Audit for those who want personalized help.

**6. How interactive is it?**
Very. We do live exercises, Q&A throughout, and breakout room discussions.

**7. What should I prepare?**
Think about your biggest operational frustration. We'll work on it during the session.

**8. Can I ask questions?**
Yes. Chat is open the entire time, and we have dedicated Q&A segments.

**9. What if I can't make the time?**
This is live-only, no recording. If you can't make it, wait for our next event.

**10. What's the next step after the workshop?**
You can implement on your own using our framework, or book a free 30-minute AI Readiness Audit for personalized guidance.

---

### Ticket Configuration

**Ticket Type**: Free Registration

**Settings**:
- Maximum quantity per order: 1
- Show remaining quantity: Yes (creates urgency)
- Ticket sales end: 1 hour before event

**Capacity**: 150 registrations

---

### Registration Questions

**Order Questions** (Asked at checkout):

1. **Company Name** (Required)
   - Type: Text
   - Question: "What's your company name?"

2. **Your Role** (Required)
   - Type: Dropdown
   - Question: "What's your role?"
   - Options:
     - Founder/CEO
     - COO/Operations
     - Department Head
     - Manager
     - Other

3. **Team Size** (Required)
   - Type: Dropdown
   - Question: "How many people work at your company?"
   - Options:
     - Just me (solopreneur)
     - 2-10 employees
     - 11-50 employees
     - 51-100 employees
     - 100+ employees

4. **Industry** (Required)
   - Type: Dropdown
   - Question: "What industry are you in?"
   - Options:
     - Professional services (legal, accounting, consulting)
     - Coaching / training
     - Marketing / creative agency
     - Nonprofit / association
     - Tech / software
     - Healthcare
     - Real estate
     - Other

5. **Biggest Challenge** (Required)
   - Type: Text (long)
   - Question: "What's your biggest operational challenge right now? (1-2 sentences)"

6. **AI Experience** (Required)
   - Type: Dropdown
   - Question: "Have you tried AI tools before?"
   - Options:
     - Yes, with good results
     - Yes, but disappointing results
     - No, haven't tried yet
     - Not sure what counts as AI

---

### Event Settings

**Online Event Settings**:
- Platform: Zoom
- How to join: Add Zoom link after registration
- Include in confirmation email: Yes

**Confirmation Page**:
```
You're registered! Here's what happens next:

1. Check your email for the event details and Zoom link
2. Add the event to your calendar (link below)
3. Watch for pre-event emails with resources to prepare

See you on [Event Date]!

Questions? Email mekaiel@arisegroup.ai
```

**Refund Policy**: N/A (Free event)

---

### Email Settings

**Confirmation Email** (Customize):

Subject: `You're in! Process-First AI Workshop - [Event Date]`

Body: Use Email 1 from pre-event sequence (copy into Eventbrite)

**Reminder Emails**:
- 1 day before: Enable
- 1 hour before: Enable

---

## Zapier Integration Setup

### Zap 1: New Registration -> Notion + Email Sequence

**Trigger**: Eventbrite - New Attendee Registration

**Action 1**: Notion - Create Database Item
- Database: Leads
- Fields to map:
  - Name: `{{Attendee Name}}`
  - Email: `{{Attendee Email}}`
  - Company: `{{Company Name}}` (from order question)
  - Role: `{{Your Role}}` (from order question)
  - Team Size: `{{Team Size}}` (from order question)
  - Industry: `{{Industry}}` (from order question)
  - Challenge: `{{Biggest Challenge}}` (from order question)
  - AI Experience: `{{AI Experience}}` (from order question)
  - Source: "Event: Process-First Workshop Feb 2026"
  - Status: "Registered"
  - Event Date: `{{Event Date}}`

**Action 2**: Gmail/Mailchimp - Add to Sequence
- Sequence: "Pre-Event Nurture"
- Tag: "Event-Feb2026"

---

### Zap 2: Event Check-in -> Update Notion

**Trigger**: Eventbrite - Attendee Checked In

**Action**: Notion - Update Database Item
- Filter: Email = `{{Attendee Email}}`
- Update: Status -> "Attended"

---

### Zap 3: Day After Event -> Process No-Shows

**Trigger**: Schedule - Day after event

**Action**: Notion - Find items where
- Source contains "Event: Process-First Workshop"
- Status = "Registered" (not "Attended")

**Action**: Update Status -> "No-Show"

**Action**: Add to No-Show email sequence

---

## Post-Event Data Export

### What to Export from Eventbrite

1. **Full attendee list** (CSV)
   - Name
   - Email
   - Order questions responses
   - Check-in status

2. **Attendance metrics**
   - Registrations
   - Checked in
   - No-shows

3. **Question responses**
   - Export for analysis
   - Identify patterns

### How to Export

1. Go to Manage Event > Attendee Summary
2. Click "Export" (top right)
3. Select "All Attendee Data"
4. Choose CSV format
5. Save to `/education/events/feb-2026-pilot/attendee-data.csv`

---

## Checklist

### Pre-Event Setup (D-14)
- [ ] Create Eventbrite event page
- [ ] Add all registration questions
- [ ] Configure ticket settings
- [ ] Add event description copy
- [ ] Set up Zapier integrations
- [ ] Test registration flow (use test email)
- [ ] Verify Notion records created correctly
- [ ] Verify email sequence triggers

### Day-Of
- [ ] Check registration count
- [ ] Verify Zoom link is correct
- [ ] Check-in attendees as they join (or use auto check-in)

### Post-Event (D+1)
- [ ] Export full attendee list
- [ ] Verify Notion statuses updated
- [ ] Trigger post-event sequences
- [ ] Review registration question responses

---

## Troubleshooting

### Issue: Zapier not triggering

1. Check Eventbrite connection is active
2. Verify trigger is "New Attendee Registration" not "New Order"
3. Test with a new registration

### Issue: Notion not creating records

1. Check database ID is correct
2. Verify field mappings match Notion schema
3. Check for required fields

### Issue: Email sequence not starting

1. Verify email tool connection
2. Check sequence is active
3. Verify tag/trigger is correct

---

**Created**: February 12, 2026
**Related**: [[PILOT-WORKSHOP-FEB-2026.md]]
