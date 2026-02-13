# Post-Event Email Sequence

**Trigger**: Event ends OR "Attended" status in Notion
**Duration**: 14 days
**Goal**: Convert attendees to audits, nurture non-converters

---

## Sequence Overview

| Email | Timing | Subject | Purpose |
|-------|--------|---------|---------|
| 1 | Same day (4hr) | Replay + Resources | Thank you, value delivery |
| 2 | Day 3 | Quick Win | Industry-specific quick win |
| 3 | Day 5 | Case Study | Social proof, results |
| 4 | Day 7 | Audit Reminder | Direct conversion ask |
| 5 | Day 14 | Last Chance | Final push + alternative |

---

## Email 1: Thank You + Replay (Same Day, 4 hours after event)

**Subject**: Workshop replay + the resources you requested

**Body**:
```
Hi {{first_name}},

Thank you for joining today's "Process-First Approach to AI" workshop!

Here's everything you need:

**WORKSHOP REPLAY:**
{{replay_link}}
(Available for 7 days)

**RESOURCES:**
- Business Functions Self-Audit Worksheet: {{worksheet_link}}
- AI Opportunity Matrix Template: {{matrix_link}}
- Quick Win Checklist: {{checklist_link}}

**YOUR NEXT STEP:**

If you identified 2-3 AI opportunities during the session, here's how to move forward:

1. **DIY**: Use the worksheet to map your full operations (takes ~2 hours)
2. **With Help**: Book a free 30-min AI Readiness Audit with me

The audit is what I offered during the session—a focused conversation where I map YOUR specific opportunities and give you a prioritized action plan.

Book here: {{calendly_link}}

(No pitch. Just a framework conversation.)

Questions from today? Just reply to this email.

Mekaiel
AriseGroup.ai
```

---

## Email 2: Quick Win for Your Industry (Day 3)

**Subject**: A quick AI win for {{industry}} (takes 30 min to set up)

**Body**:
```
Hi {{first_name}},

Following up from our workshop—here's a quick win you can implement TODAY.

{{#if industry == "Professional Services"}}
**Quick Win: Automated Meeting Notes**

Tool: Fireflies.ai or Otter.ai (both have free tiers)

What it does:
- Records your calls automatically
- Generates summaries + action items
- Searchable transcript archive

Time to set up: 15 minutes
Time saved per call: 10-15 minutes
Weekly impact: 1-2 hours reclaimed

Implementation: Sign up, connect to Zoom/Teams, done.
{{/if}}

{{#if industry == "Consulting/Coaching"}}
**Quick Win: Client Session Summary Generator**

Tool: Claude (free tier available)

What it does:
- Paste your session notes
- Get a professional client summary in 60 seconds
- Includes key insights + next steps

Prompt to use:
"Summarize this coaching session for my client. Include key insights discussed, action items agreed, and recommended focus areas for next session. Keep it warm but professional, under 300 words."

Time saved per session: 15-20 minutes
Weekly impact: 1-2 hours reclaimed
{{/if}}

{{#if industry == "Agency/Creative"}}
**Quick Win: Project Update Automation**

Tool: Zapier (free tier) + your project management tool

What it does:
- When a task moves to "Complete" status
- Auto-sends client update email
- Includes what was done + what's next

Time to set up: 30 minutes
Time saved per project: 30-60 min/week
Client impact: They feel informed without you doing manual updates
{{/if}}

{{#default}}
**Quick Win: Email Response Drafting**

Tool: Claude (free tier available)

What it does:
- Paste the email you received
- Get 2-3 response options instantly
- Edit and send (60 seconds total)

Prompt to use:
"Draft 3 response options for this email. Keep them professional, concise, and action-oriented. Include a clear next step in each."

Time saved: 5-10 min per complex email
Weekly impact: 1-2 hours reclaimed
{{/default}}

---

This is exactly the kind of opportunity we'd identify together in an AI Readiness Audit.

Want to find more? Book your free 30-min session: {{calendly_link}}

Mekaiel
```

---

## Email 3: Case Study (Day 5)

**Subject**: How [Client] saved 15 hours/week (process-first approach)

**Body**:
```
Hi {{first_name}},

I wanted to share a real example of the process-first approach in action.

**THE CLIENT:**
Plotter Mechanix - Printing equipment service company

**THE CHALLENGE:**
- Technicians spending 45+ min per job on documentation
- Customer communication delays (follow-ups falling through cracks)
- Quoting process taking 2-3 hours per quote

**THE APPROACH (What We Did):**

1. Mapped their 10 business functions
2. Identified 3 high-impact opportunities
3. Started with the QUICKEST win (not the biggest)

**THE RESULTS (Phase 1 - 6 weeks):**

| Before | After |
|--------|-------|
| 45 min/job documentation | 5 min (AI-assisted) |
| 2-3 hour quoting | 15 min (template + AI) |
| Manual follow-up tracking | Automated reminders |

**ROI:** $47K projected annual savings (validated by CFO)

**THE KEY INSIGHT:**

We didn't start with the "big strategic AI project."

We started with the frustrating manual task that happened EVERY DAY.

That's the process-first approach.

---

**Want to identify YOUR version of this?**

Book a free 30-min AI Readiness Audit: {{calendly_link}}

We'll map your operations and find your "every day" opportunity.

Mekaiel
```

---

## Email 4: Audit Reminder (Day 7)

**Subject**: Quick question about your AI priorities

**Body**:
```
Hi {{first_name}},

It's been a week since our workshop.

Quick question: Did you have a chance to complete the self-audit exercise?

**If yes:** You probably identified 2-3 opportunities. Ready to validate them and prioritize?

**If no:** Totally understand—you're busy running your business. That's exactly why the audit exists.

Here's the offer:

**Free 30-Minute AI Readiness Audit**

What you get:
- I map your operations (the exercise you didn't have time for)
- We identify your top 3 AI opportunities
- You leave with a prioritized action plan

What it's NOT:
- A sales pitch
- A generic recommendations list
- A waste of your time

I've done 50+ of these. Most clients walk away saying "I finally have clarity on where to start."

Book here: {{calendly_link}}

If you have questions first, just reply.

Mekaiel

P.S. If an audit doesn't make sense, no worries. I'll keep sharing insights that might help. But if you're ready to move faster, this is the best next step.
```

---

## Email 5: Last Chance / Alternative Path (Day 14)

**Subject**: Two paths forward (pick one)

**Body**:
```
Hi {{first_name}},

Final follow-up on our workshop from two weeks ago.

You have two paths forward:

---

**PATH 1: DIY (Free)**

Use the resources I sent:
- Business Functions Worksheet
- AI Opportunity Matrix
- Quick Win Checklist

Block 2 hours on your calendar. Map your operations. Identify your opportunities.

This works—it just takes YOUR time.

---

**PATH 2: GUIDED (Also Free)**

Book a 30-min AI Readiness Audit with me.

I do the mapping during our call. You get the same outcome in 30 minutes instead of 2 hours.

Plus: You get an outside perspective on your blind spots.

Book here: {{calendly_link}}

---

Either path works. The wrong move is doing nothing.

AI is moving fast. Your competitors are figuring this out.

Pick a path.

Mekaiel

P.S. No more emails on this topic after today. But I'll keep sharing insights on LinkedIn if you want to stay connected: {{linkedin_link}}
```

---

## No-Show Sequence

**For registrants who didn't attend:**

### No-Show Email 1 (Same day, 4 hours after event)

**Subject**: Missed you today—here's the replay

**Body**:
```
Hi {{first_name}},

I noticed you couldn't make it to today's workshop.

No worries—life happens.

Here's everything you missed:

**WORKSHOP REPLAY:** {{replay_link}}
(Available for 7 days)

**KEY TAKEAWAYS:**
1. Why 70% of AI projects fail (and the one thing that prevents it)
2. The 10 Business Functions framework
3. How to find YOUR AI quick wins

**RESOURCES:** {{resources_link}}

If you watch the replay and have questions, just reply.

Or if you'd rather skip to the personalized version:
Free AI Readiness Audit: {{calendly_link}}

Mekaiel
```

### No-Show Email 2 (Day 7)

**Subject**: Still relevant? (AI workshop follow-up)

**Body**:
```
Hi {{first_name}},

Quick check-in on the workshop replay I sent.

If AI for your business is still on your radar, I'm happy to:

A) Answer questions about the content (just reply)
B) Do a live version just for you (30-min audit call)

If it's not a priority right now, totally fine. I'll stop following up.

Just reply "not now" and I'll check back in 3 months.

Mekaiel
```

---

## Automation Notes

### Segmentation Required
- **Attended** -> Main sequence (Emails 1-5)
- **No-Show** -> No-show sequence
- **Booked Audit** -> Remove from sequence, add to audit prep sequence

### Variables Required
- `{{first_name}}` - From registration
- `{{industry}}` - From registration question
- `{{replay_link}}` - Manual (Zoom recording link)
- `{{worksheet_link}}` - Google Drive / Notion link
- `{{matrix_link}}` - Google Drive / Notion link
- `{{checklist_link}}` - Google Drive / Notion link
- `{{calendly_link}}` - Audit booking link
- `{{linkedin_link}}` - Mekaiel's LinkedIn

### Stop Conditions
- If recipient books audit -> Stop sequence
- If recipient replies "not interested" -> Stop sequence
- If recipient unsubscribes -> Stop sequence

---

**Created**: February 12, 2026
**Related**: [[pre-event/README.md]]
