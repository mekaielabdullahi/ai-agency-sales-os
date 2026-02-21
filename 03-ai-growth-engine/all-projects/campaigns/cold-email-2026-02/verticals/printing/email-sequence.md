# Email Sequence: Printing Vertical
## 4 Touches, 12 Days - Proof-Led Approach

---

## The Offer

> "We helped a Phoenix plotter repair company save 15 hours/week and achieve 1,378% ROI on a $5K investment. I'll audit your operations and build one automation for free. If it works, we talk about more."

---

## EMAIL 1 (Day 0, Tuesday) - Icebreaker + Loom

**Subject:** `quick q about [Company]'s service ops`

```
Hey [First Name],

[AI icebreaker - e.g., "Saw [Company] handles HP wide-format service
across [state] -- keeping those machines running is no joke."]

I work with print service companies on automation. Nothing fancy --
just systems that handle the scheduling, dispatch, and customer
follow-up your team is probably doing by hand.

I recorded a 3-minute video showing what we built for a plotter
repair shop in Phoenix (1,378% ROI on their first project):

[Loom link]

No pitch, no call needed.

Mekaiel
AriseGroup.ai
```

---

## EMAIL 2 (Day 4, Saturday) - Pain Point + Social Proof

**Subject:** `re: quick q about [Company]'s service ops`

```
Hey [First Name],

Following up -- wanted to share one thing.

We worked with Kelsey at Plotter Mechanix in Phoenix. Her admin Alyssa
was spending 25 hours/week just processing calls into service tickets,
quotes, and orders. Kelsey was the only tech and couldn't step away.

We built a system that auto-routes calls, creates tickets, and handles
triage. Alyssa got 15 hours back. Kelsey's moving from $175/hr wrench-
turner to $300-500/hr consultant.

Quick question -- what's the biggest time-killer in your service ops?

Mekaiel
```

---

## EMAIL 3 (Day 8, Wednesday) - The Close

**Subject:** `the $5K experiment that changed everything`

```
[First Name],

Last one unless you want me to keep going.

Kelsey at Plotter Mechanix invested $5K in Phase 1. The system now saves
$73K+ annually. That's 1,378% ROI.

My offer: I'll audit [Company]'s operations and build ONE automation --
free. If it saves you time, we talk about a full engagement. If not,
we shake hands.

Zero risk. I eat the cost.

Why free? Your shop looks like a perfect fit for what we build, and
I want more print service case studies.

Reply "interested" and I'll send details.

Mekaiel
AriseGroup.ai
```

---

## EMAIL 4 (Day 12, Sunday) - Breakup

**Subject:** `closing the loop`

```
Hey [First Name],

Haven't heard back -- totally fine. You're busy fixing printers.

If timing is ever better: mekaiel@arisegroup.ai

The free operations audit offer stands whenever you're ready.

All the best,
Mekaiel
```

---

## Subject Lines to A/B Test

### Suvam Style (Humble/Curious)
- A: `quick q about [Company]'s service ops`
- B: `saw [Company] services [HP/Canon] -- had a thought`
- C: `[First Name], the 25-hour problem`

### Otto Style (Proof-Led)
- D: `How [Printer Name] solved their operational bottleneck`
- E: `Your growth is limited by operations, not leads`

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
| `[First Name]` | Lead sheet | Kelsey |
| `[Company]` | Lead sheet | Plotter Mechanix |
| `[AI icebreaker]` | Perplexity -> ChatGPT pipeline | "Saw your team handles HP DesignJet service across Arizona -- keeping those machines running is no joke." |
| `[HP/Canon/Epson]` | Company website | HP and Canon |
| `[state]` | Lead sheet | Arizona |
| `[Loom link]` | Static | Printing vertical Loom video URL |

---

## n8n Send Node Configuration

- **Trigger:** Google Sheet row with Status = "Ready to Send" and Vertical = "Printing"
- **Email number:** Based on `Last Email Sent` column (1-4)
- **Timing:** Cron Tue-Thu 9-11am, respects day gaps between emails
- **Inbox rotation:** Round-robin across 15 inboxes, max 30/inbox/day
- **Thread:** Emails 2-4 reply to Email 1's Message-ID for threading
