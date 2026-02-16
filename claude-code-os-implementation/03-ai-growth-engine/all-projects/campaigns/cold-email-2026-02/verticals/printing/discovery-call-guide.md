# Discovery Call Guide: Printing Vertical
## Lead with Proof, Phase the Close

---

## Pre-Call Prep (5 min)

- [ ] Research the company website
- [ ] Note which printer brands they service (HP, Canon, Epson)
- [ ] Check for pain signals (hiring posts, reviews mentioning delays, small team)
- [ ] Review the Plotter Mechanix case study brief
- [ ] Have the Phase 1 pricing ready ($5K)

---

## Opening (2 min)

> "Before we start -- I researched [Company]. I noticed [specific detail about their business]. Tell me more about that."

Let them talk. Listen for operational pain points.

---

## The 5 Discovery Questions (15 min)

### Q1: Current State
> "Walk me through what happens when a service call comes in. From the phone ringing to the job being completed -- what does that look like?"

**Listen for:** Manual steps, single points of failure, owner involvement in every step.

### Q2: Quantify the Cost (Critical)
> "How many hours a week would you say you or your team spends on admin -- scheduling, dispatching, quotes, follow-ups -- versus actual service work?"

**Listen for:** Specific hour counts. If vague, probe: "Is it closer to 10 hours or 30 hours?"

### Q3: Previous Attempts
> "Have you tried to fix this before? Hired someone, bought software, anything?"

**Listen for:** What they've tried, why it didn't work, budget they've previously allocated.

### Q4: Cost of Inaction (Critical)
> "If nothing changes in the next 12 months, what does that look like for the business?"

**Listen for:** Burnout, lost revenue, inability to grow, quality issues.

### Q5: Vision
> "If we could cut your admin time in half -- say from [X] hours to [X/2] hours -- what would you do with that time back?"

**Listen for:** Growth ambitions, personal goals, rate increases. This is your selling fuel.

---

## The Bridge (3 min)

> "You sound a lot like Kelsey at Plotter Mechanix. She was the best tech in the shop but was also running scheduling, dispatch, quotes, and customer follow-up. Her admin Alyssa was spending 25 hours a week on manual processing."

> "We built a system that auto-routes calls, creates service tickets, and handles triage. Alyssa got 15 hours back per week. Kelsey went from billing at $175/hr as a technician to transitioning into a $300-500/hr consultant role. The Phase 1 investment was $5K and it generates over $73K annually."

> "Here's how I'd adapt it for [Company]..."

---

## Pricing Approach (Otto Model)

### Step 1: Establish Budget
> "What are you comfortable investing to solve this?"

If they give a number, work within it. If they deflect:

> "For context, Kelsey invested $5K in Phase 1 and the ROI was 1,378%. I'm not suggesting we start there -- I just want to understand what makes sense for you."

### Step 2: Present Phase 1
- Start with **$5K Phase 1 milestone**
- Scope: One core automation (call routing + ticket creation, OR dispatch automation, OR quote workflow)
- Timeline: 2-3 weeks
- Expected result: 10-15 hours/week saved

### Step 3: Let Results Sell Phase 2
- Don't pitch the full $15-42K on the first call
- After Phase 1 delivers results, present expansion options
- Phase 2 scope based on what Phase 1 reveals

---

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We're too small for this" | "Plotter Mechanix is a small shop too. That's actually why it works -- small changes have massive impact when the owner is the bottleneck." |
| "We've tried software before" | "This isn't off-the-shelf software. We custom-build around your existing workflow. What did you try before, and why didn't it work?" |
| "I don't have $5K right now" | "What if we started with the free audit? I'll map your operations and show you exactly where the time savings are. No cost, no commitment." |
| "$5K seems like a lot" | "Kelsey thought the same thing. Her $5K turned into $73K of annual value. What would 15 hours a week back be worth to your business?" |
| "I need to think about it" | "Totally fair. What specifically do you want to think through? I want to make sure you have everything you need." |

---

## Post-Call Actions

- [ ] Send follow-up email within 2 hours summarizing the call
- [ ] Trigger `post_call_followup.json` in n8n
- [ ] If qualified: Build proposal using `proposal_assembly.json`
- [ ] Log ICP data: company, sub-niche, size, pain point (their words), conviction score
- [ ] Update lead tracker status

---

## Reference

- 5 Questions Discovery Script: `ai-agency-sales-os/claude-code-os-implementation/02-operations/discovery-process/templates/5-questions-discovery-call-script.md`
- Outreach Framework: `ai-agency-sales-os/claude-code-os-implementation/03-ai-growth-engine/all-projects/outreach/arise-group-ai-outreach-framework.md`
