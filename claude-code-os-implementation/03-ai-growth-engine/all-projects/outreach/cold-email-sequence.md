# Arise Group — Cold Email Sequence
**5-Touch Drip | 5 Questions Method**
**Last Updated: March 2026**

---

## Setup Requirements

**Sending domain**: Use a separate domain from arisegroup.ai (e.g., arisegroup.co or meetarise.com)
**Warm up**: 2-3 weeks of warmup before sending cold volume (use Instantly or Mailreach)
**Daily send limit**: Start at 30/day, scale to 100/day after warmup
**Personalization fields**: {{first_name}}, {{company}}, {{industry}}, {{pain_hook}}

---

## Sequence Overview

| Email | Day | Subject | Goal |
|-------|-----|---------|------|
| Email 1 | Day 1 | One question | Open the conversation |
| Email 2 | Day 3 | Re: [their problem] | Deepen if they reply |
| Email 3 | Day 7 | Quick follow-up | Bump |
| Email 4 | Day 12 | The 6-month question | Urgency + consequence |
| Email 5 | Day 16 | Last one | Break-up / final nudge |

---

## Email 1 — Problem Discovery (Day 1)

**Subject:** Quick question, {{first_name}}

```
Hey {{first_name}},

I work with {{industry}} businesses around the $1M-$10M mark — specifically the ones where the founder is still the bottleneck for almost everything.

Before I say anything about what we do, I'm curious:

What's the biggest operational problem slowing {{company}} down right now?

I ask because the answer is usually different than what I'd assume, and I don't want to waste your time.

– Mekaiel
Arise Group | arisegroup.ai
```

**Notes:**
- 5 sentences max
- No pitch, no links (kills deliverability)
- End on a question, not a CTA
- If they reply → move to Email 2 (skip ahead in sequence)

---

## Email 2 — Cost Quantification (Send only if they reply to E1)

**Subject:** Re: {{their_stated_problem}}

```
Got it — {{restate_problem_in_their_words}}.

That tracks. A lot of the founders I work with describe something similar.

Two quick follow-ups so I understand the scope:

1. Rough ballpark — how much is this costing you per month? (lost revenue, staff hours, missed deals — whatever makes sense)

2. How long has this been the situation?

Just trying to figure out if this is urgent or more of a back-burner thing for you.

– Mekaiel
```

**Notes:**
- Only send after they respond to Email 1
- Personalize with their exact words from E1 reply
- Two questions max

---

## Email 3 — Follow-Up Bump (Day 7, if no reply to E1)

**Subject:** Still relevant, {{first_name}}?

```
Hey {{first_name}},

Sent you a note last week — wanted to follow up in case it got buried.

One question I'm genuinely curious about:

What's taking the most time in {{company}}'s operations right now that you wish you could hand off?

If it's nothing — totally fair. Just let me know and I won't follow up again.

– Mekaiel
Arise Group
```

**Notes:**
- Softer than E1 — lowers the bar to reply
- "Just let me know" gives permission to say no = more replies either way
- Different angle on Q1

---

## Email 4 — Consequence + Urgency (Day 12, if still no reply)

**Subject:** The 6-month question

```
{{first_name}},

Last question before I leave you alone:

If the operational drag in {{company}} stays the same for the next 6-12 months — what does that look like for you?

More hiring? Missing growth targets? Still doing everything yourself?

I ask because most founders I talk to know the answer. They just haven't said it out loud yet.

If any of that resonates, worth 20 minutes to map it out?

– Mekaiel
Arise Group | arisegroup.ai
```

**Notes:**
- This is the consequence email (Q4)
- First email to include a soft CTA ("20 minutes")
- Still no calendar link — keep it conversational

---

## Email 5 — Break-Up (Day 16, if still no reply)

**Subject:** Closing the loop

```
{{first_name}},

I've sent a few notes — clearly the timing isn't right or it's just not relevant.

Either way, no hard feelings.

If things change and operational efficiency ever becomes a priority at {{company}}, you know where to find me.

– Mekaiel
Arise Group | arisegroup.ai

P.S. If you know someone in {{industry}} who's dealing with scaling pains — happy to take a look for them too.
```

**Notes:**
- Break-up emails often get the highest reply rate
- P.S. referral line is subtle but effective
- After this: move to nurture list, re-engage in 60-90 days

---

## Angle Variations (A/B Test These)

### Angle A — Social Proof Hook
```
Subject: What [Similar Company] did in 30 days

Hey {{first_name}},

We recently helped a {{industry}} business go from [problem] to [result] in about 30 days.

The fix wasn't a new tool — it was restructuring how their operations ran using AI.

Quick question: what's the biggest time sink in {{company}} right now?

– Mekaiel
```

### Angle B — Contrarian Hook
```
Subject: AI won't help you (yet)

Hey {{first_name}},

Most {{industry}} businesses I talk to have tried AI tools and gotten minimal results.

Not because the tools don't work — but because they added tools to broken processes.

What's the process in {{company}} that breaks most often?

– Mekaiel
```

### Angle C — Direct Pain Point
```
Subject: {{company}} + operational bottlenecks

Hey {{first_name}},

I focus on one thing: helping {{industry}} founders stop being the bottleneck in their own business.

Usually that means automating 2-3 high-friction processes in 30 days.

Is operational bandwidth something you're actively working on at {{company}}?

– Mekaiel
```

---

## Reply Handling

**If they reply with interest:**
```
Thanks for getting back to me.

Based on what you're describing, I think there's something worth exploring.

Here's a link to grab 20 minutes: [calendar link]

In the meantime — can you tell me a bit more about [Q2 or Q3 follow-up]?

– Mekaiel
```

**If they say "not right now":**
```
Understood — timing matters.

Mind if I check back in 60 days? And if anything shifts before then, feel free to reach out directly.

– Mekaiel
```

**If they ask for more info:**
```
Happy to share more.

The short version: we work with {{industry}} businesses to build AI operating systems — automating the recurring tasks that eat founder bandwidth.

Typical engagement: 30-day implementation, then it runs on autopilot.

Would a quick call make more sense than back-and-forth email?

[calendar link]
```

---

## Technical Setup Checklist

**Domain & Email**
- [ ] New sending domain purchased (e.g., arisegroup.co)
- [ ] SPF, DKIM, DMARC configured
- [ ] 2-3 email accounts created on that domain
- [ ] Email warmup started (Instantly or Mailreach) — 2-3 weeks before sending

**Sending Tool (Instantly.ai recommended)**
- [ ] Account created
- [ ] Email accounts connected
- [ ] Warmup enabled on all accounts
- [ ] Sequence uploaded
- [ ] Daily send limit set (30/day to start)

**Lead Import**
- [ ] Apollo export → CSV
- [ ] Emails verified (Apollo or NeverBounce)
- [ ] Personalization fields mapped
- [ ] Pain hook field filled for top prospects

---

## Performance Benchmarks

| Metric | Cold Baseline | Target |
|--------|--------------|--------|
| Open rate | 30-40% | 45%+ |
| Reply rate | 3-5% | 8-12% |
| Positive reply rate | 1-2% | 3-5% |
| Call booked per 100 emails | 1-2 | 3-5 |

**If open rate <25%**: Subject line problem
**If open rate good but reply rate <3%**: Body copy problem
**If replies good but no calls booked**: CTA or qualification problem

---

*Run for 2 weeks → review metrics → optimize the weakest link.*
