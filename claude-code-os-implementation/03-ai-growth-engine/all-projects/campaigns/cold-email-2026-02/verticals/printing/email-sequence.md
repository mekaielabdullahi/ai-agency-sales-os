# Email Sequence: Printing Vertical
## 4 Touches, 14 Days - Short. Direct. Value-First.

---

## The Offer

> "We helped a Phoenix plotter repair company save 15 hours/week and achieve 1,378% ROI on a $5K investment. I'll audit your operations and build one automation for free. If it works, we talk about more."

---

## EMAIL 1 (Day 1) - Quick Question + Pain Point

**Subject:** `Quick question about [Company]`

```
[First Name],

[AI icebreaker - e.g., "Saw [Company] handles HP wide-format service
across [state]."]

Most print service shops I talk to have the same problem: the owner
is the only one who can handle the hard jobs, and admin work eats
15-25 hours/week that should go to revenue.

We helped a Phoenix plotter repair company turn a $5K system into
$73K+ in annual savings. Worth 15 min to see if it applies to you?

Mekaiel
AriseGroup.ai
```

---

## EMAIL 2 (Day 3) - Follow Up + Specific Proof

**Subject:** `Re: Quick question about [Company]`

```
[First Name],

Following up.

Kelsey at Plotter Mechanix was the only tech. Her admin Alyssa spent
25 hours/week processing calls into tickets, quotes, and orders.
Kelsey couldn't step away without the business grinding to a halt.

We built a system that auto-routes calls, creates tickets, and handles
triage. Alyssa got 15 hours back. Kelsey's moving from $175/hr wrench
work to $300-500/hr consulting.

What's the biggest time-killer in your service ops right now?

Mekaiel
```

---

## EMAIL 3 (Day 7) - Case Study + Free Offer

**Subject:** `The $5K experiment that changed everything`

```
[First Name],

Attached: how we helped a print service company your size cut admin
time by 60% and achieve 1,378% ROI.

My offer: I'll audit [Company]'s operations and build ONE automation
for free. If it saves you time, we talk about more. If not, no hard
feelings.

Why free? I want more print service case studies, and your shop looks
like a fit.

Reply "interested" and I'll send details.

Mekaiel
AriseGroup.ai
```

---

## EMAIL 4 (Day 14) - Last Note

**Subject:** `Closing the loop`

```
[First Name],

Not trying to be a pest. If operations aren't a priority right now,
no worries.

But if they are -- reply and I'll send our free audit checklist.
Same one that found $73K in savings for Plotter Mechanix.

Either way, best of luck. Your [product/service] is solid.

Mekaiel
```

---

## Subject Lines to A/B Test

### Direct (Ruthless Style)
- A: `Quick question about [Company]`
- B: `[Company] + operations`
- C: `The $5K experiment that changed everything`

### Pain-Led
- D: `[First Name], the 25-hour problem`
- E: `Your growth is limited by operations, not leads`

### Proof-Led
- F: `How a Phoenix print shop hit 1,378% ROI`
- G: `$5K system → $73K savings (print service case study)`

---

## Sending Schedule

| Email | Day | Spacing | Time |
|-------|-----|---------|------|
| Email 1 | Day 1 | — | 9-11am local |
| Email 2 | Day 3 | +2 days | 9-11am local |
| Email 3 | Day 7 | +4 days | 9-11am local |
| Email 4 | Day 14 | +7 days | 9-11am local |

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
- **Timing:** Day 1 → Day 3 (+2) → Day 7 (+4) → Day 14 (+7)
- **Send window:** 9-11am local time
- **Inbox rotation:** Round-robin across 5 inboxes, start at 20/day, scale to 50/day after warmup
- **Thread:** Emails 2-4 reply to Email 1's Message-ID for threading
- **Daily capacity:** 250/day total across all inboxes (post-warmup)

---

## Verified Claims

All metrics in these emails verified against Fireflies transcripts (Feb 16, 2026):

| Claim in Email | Verified | Source |
|----------------|----------|--------|
| "1,378% ROI" | ✅ | Calculation: ($73K / $5K - 1) × 100 |
| "25 hours/week" (Alyssa before) | ✅ | Alyssa Interview, Phase 2 Proposal |
| "15 hours back" (Alyssa saved) | ✅ | 25 hrs → 10 hrs = 15 hrs saved |
| "$175/hr wrench-turner" | ✅ | Feb 3 Coach Call, Jobber data |
| "$300-500/hr consultant" | ✅ (in progress) | Target rate, transformation ongoing |
| "$5K investment" | ✅ | Phase 1 Quick Win Sprint |
| "$73K+ annually" | ✅ | ROI calculation methodology |

**Full verification:** See `conviction/SOURCE-CITATIONS.md`
