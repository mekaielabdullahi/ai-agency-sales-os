# Pre-Event Email Sequence

**Trigger**: Eventbrite registration
**Duration**: 7 days (until event)
**Goal**: Build anticipation, reduce no-shows, pre-qualify

---

## Sequence Overview

| Email | Timing | Subject | Purpose |
|-------|--------|---------|---------|
| 1 | Immediate | Confirmation + Quick Win | Welcome, set expectations |
| 2 | Day 3 | The Framework Teaser | Build anticipation |
| 3 | Day 5 | Industry-Specific Value | Personalize based on registration |
| 4 | Day 6 | What to Prepare | Pre-work + engagement |
| 5 | Day 7 (D-1) | Final Reminder | Reduce no-shows |

---

## Email 1: Registration Confirmation (Immediate)

**Subject**: You're in! Here's what happens next [Process-First AI Workshop]

**Body**:
```
Hi {{first_name}},

You're registered for "The Process-First Approach to AI" on {{event_date}} at {{event_time}}.

Here's what you'll walk away with:
- A clear framework for evaluating AI opportunities (no more tool overwhelm)
- A self-audit of YOUR business functions
- 2-3 specific AI quick wins you can implement in 30-90 days
- Access to a free AI Readiness Audit (first 5 attendees)

Before the event, here's one question to think about:

"If you could automate ONE thing in your business tomorrow, what would have the biggest impact?"

Save your answer. You'll use it during the workshop.

Looking forward to seeing you there,

Mekaiel
AriseGroup.ai

P.S. Add this to your calendar so you don't miss it: {{calendar_link}}
```

---

## Email 2: The Framework Teaser (Day 3)

**Subject**: Why 70% of AI projects fail (and how to avoid it)

**Body**:
```
Hi {{first_name}},

Quick story before our workshop on {{event_date}}:

Last month, a consulting firm founder told me: "We bought 6 AI tools this year. Only one stuck."

When I asked why, the answer was the same as every failed AI project I've seen:

They started with the tool, not the process.

Here's the truth most AI vendors won't tell you:

The #1 predictor of AI success isn't the tool you choose.
It's whether you've mapped your processes FIRST.

On {{event_date}}, I'll show you exactly how to:
1. Map your business into 10 clear functions
2. Identify which 2-3 functions are AI-ready
3. Avoid the "shiny tool" trap

You'll leave with a framework you can use forever—not just another tool recommendation.

See you there,

Mekaiel

P.S. Still have your answer to "what would you automate first"? Bring it.
```

---

## Email 3: Industry-Specific Value (Day 5)

**Subject**: {{industry}} + AI: What actually works

**Body**:
```
Hi {{first_name}},

Since you're in {{industry}}, I wanted to share what I'm seeing work.

**Most common AI wins in {{industry}}:**

{{#if industry == "Professional Services"}}
- Proposal generation (2-3 hours -> 15 minutes)
- Client onboarding automation (50% time reduction)
- Meeting note summarization + action item extraction
{{/if}}

{{#if industry == "Consulting/Coaching"}}
- Discovery call prep (research + talking points automated)
- Session summary generation (immediate client deliverable)
- Content repurposing (1 insight -> 5 content pieces)
{{/if}}

{{#if industry == "Agency/Creative"}}
- Brief intake automation (no more back-and-forth)
- Project status updates (automated client communication)
- Creative brief generation (first drafts in minutes)
{{/if}}

{{#if industry == "Nonprofit"}}
- Grant application assistance (research + first drafts)
- Donor communication personalization at scale
- Volunteer coordination automation
{{/if}}

{{#default}}
- Email classification + response drafting
- Report generation automation
- Customer inquiry handling
{{/default}}

On {{event_date}}, we'll map YOUR specific opportunities.

Bring your biggest operational frustration—we'll tackle it live.

Mekaiel
```

---

## Email 4: What to Prepare (Day 6)

**Subject**: Tomorrow's workshop: Here's how to get 10x more from it

**Body**:
```
Hi {{first_name}},

Our workshop is TOMORROW ({{event_date}} at {{event_time}}).

To get the most out of it, here's a 5-minute pre-work:

**BEFORE THE SESSION:**

1. Think about your last week. What task(s) felt repetitive?
   Write down 2-3 examples.

2. Open your calendar. Where did your time actually go?
   (Meetings? Admin? Putting out fires?)

3. Identify ONE process that frustrates you.
   This is your "target" for the workshop.

**WHAT TO HAVE READY:**

- Quiet space (you'll be doing exercises)
- Pen/paper or open doc for notes
- The process frustration from #3 above

**THE SESSION LINK:**

Join here: {{zoom_link}}

(Add to calendar: {{calendar_link}})

See you tomorrow,

Mekaiel

P.S. First 5 attendees to book during the session get a free 30-min AI Readiness Audit. Come ready to take action.
```

---

## Email 5: Final Reminder (Day 7 / Event Day)

**Subject**: Starting in 2 hours: [Process-First AI Workshop]

**Body**:
```
Hi {{first_name}},

We're starting in 2 hours.

**Join here:** {{zoom_link}}

**Quick reminders:**
- Have your "most frustrating process" ready
- We'll be doing a live self-audit exercise
- First 5 to book get a free AI Readiness Audit

See you at {{event_time}},

Mekaiel

---

Can't make it? Reply and I'll send you the replay.
```

---

## Automation Notes

### Variables Required
- `{{first_name}}` - From registration
- `{{event_date}}` - From Eventbrite
- `{{event_time}}` - From Eventbrite
- `{{industry}}` - From registration question
- `{{zoom_link}}` - Manual or Eventbrite
- `{{calendar_link}}` - Google/Outlook calendar link

### Conditional Logic
- Email 3 requires industry-based personalization
- If industry is blank, use default content

### Tool Options
- Mailchimp: Use merge tags and conditional content blocks
- ConvertKit: Use liquid tags for conditions
- Gmail + Zapier: Send via Gmail with Zapier delays

---

**Created**: February 12, 2026
**Related**: [[post-event/README.md]]
