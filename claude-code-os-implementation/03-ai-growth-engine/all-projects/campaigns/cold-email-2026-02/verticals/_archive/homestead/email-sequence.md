# Email Sequence: Homestead Vertical
## 4 Touches, 12 Days - Zero-Risk / Case Study Approach

---

## The Offer

> "I'm building case studies in the homestead space. I'll audit your operations and build one working automation -- completely free. If it saves you time, we talk. If not, we shake hands. I just want the permission to reference your company."

---

## EMAIL 1 (Day 0, Tuesday) - Icebreaker + Loom

**Subject:** `[First Name], had a thought about [Company/Brand]`

```
Hey [First Name],

[AI icebreaker - e.g., "Saw your latest post about spring seed
starting -- your community clearly loves what you're building."]

I help small business owners automate the backend stuff -- order
processing, customer follow-up, inventory -- so they can spend
more time on the work they actually love.

Put together a quick 3-minute video showing what I mean for a
business like yours:

[Loom link]

No pitch, no call. Just thought it might be useful.

Mekaiel
AriseGroup.ai
```

---

## EMAIL 2 (Day 4, Saturday) - Pain Point + Empathy

**Subject:** `re: [First Name], had a thought about [Company/Brand]`

```
Hey [First Name],

Following up with one thought.

Most homestead business owners I've talked to started because they
love [the land/teaching/the lifestyle]. But now they're spending
half their time on order emails, DMs, spreadsheets, and scheduling.

We recently helped a small business owner go from 25+ hours of
manual admin per week to under 10. The work they actually care
about got their full attention back.

What's the one thing eating most of your time right now that
has nothing to do with [homesteading/your actual craft]?

Mekaiel
```

---

## EMAIL 3 (Day 8, Wednesday) - Zero Risk Offer

**Subject:** `a weird offer for [Company]`

```
[First Name],

Last email unless you tell me otherwise.

I'm building out case studies in the homestead space because I
genuinely think these businesses are underserved by technology.

Here's my offer: I will look at [Company]'s operations and build
ONE working automation -- completely free. Could be order processing,
customer follow-up, inventory tracking, whatever eats most of your
time.

If it helps, we talk about doing more. If it doesn't, we shake hands
and part ways. The only thing I ask is permission to reference
[Company] when I reach out to other homestead businesses.

Zero risk. Zero cost. I eat the hours.

Reply "sure" or "tell me more" and I'll explain how it works.

Mekaiel
AriseGroup.ai
```

---

## EMAIL 4 (Day 12, Sunday) - Breakup

**Subject:** `closing the loop`

```
Hey [First Name],

Reached out a few times -- no worries if it's not the right time.

If you ever want a free second opinion on how to get some of your
time back from the admin side of things, the offer stands:
mekaiel@arisegroup.ai

Keep building something awesome.

Mekaiel
```

---

## Subject Lines to A/B Test

- A: `[First Name], had a thought about [Company/Brand]`
- B: `a weird offer for [Company]`
- C: `[First Name], noticed something about your shop`

---

## Sending Schedule

| Email | Day | Day of Week | Time |
|-------|-----|-------------|------|
| Email 1 | Day 0 | Tuesday | 9-11am local |
| Email 2 | Day 4 | Saturday | 9-11am local |
| Email 3 | Day 8 | Wednesday | 9-11am local |
| Email 4 | Day 12 | Sunday | 9-11am local |

---

## Personalization Variables

| Variable | Source | Example |
|----------|--------|---------|
| `[First Name]` | Lead sheet | Sarah |
| `[Company/Brand]` | Lead sheet | Heritage Homestead Co |
| `[AI icebreaker]` | Perplexity -> ChatGPT pipeline | "Saw your latest post about spring seed starting -- your community clearly loves what you're building." |
| `[the land/teaching/the lifestyle]` | Research | teaching others to homestead |
| `[homesteading/your actual craft]` | Research | growing and shipping heritage seeds |
| `[Loom link]` | Static | Homestead vertical Loom video URL |

---

## n8n Send Node Configuration

- **Trigger:** Google Sheet row with Status = "Ready to Send" and Vertical = "Homestead"
- **Email number:** Based on `Last Email Sent` column (1-4)
- **Timing:** Cron Tue-Thu 9-11am, respects day gaps between emails
- **Inbox rotation:** Round-robin across 15 inboxes, max 30/inbox/day
- **Thread:** Emails 2-4 reply to Email 1's Message-ID for threading

---

## Note on Approach

Until the first homestead case study is published (target: S&S Wolf Sheds), use the **zero-risk / case study offer** rather than proof-led messaging. Once you have a published case study, update Email 2 and Email 3 with specific metrics (like the printing vertical uses Plotter Mechanix).
