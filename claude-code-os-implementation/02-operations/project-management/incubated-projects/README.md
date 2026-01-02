# Incubated Projects

## What is an "Incubated Project"?

Projects with **real potential** but **no closed deal yet**. These are opportunities worth nurturing, but not yet generating revenue.

### Criteria for Incubation

✅ **Belongs in incubated-projects/ if:**
- Real business relationship exists (not cold prospect)
- Discovery call completed with positive outcome
- Client expressed genuine interest
- Problem is well-defined and solvable
- Close probability: 30-70%
- Timeline to close: 2-8 weeks

❌ **Does NOT belong here if:**
- Cold prospect (no relationship)
- Client unresponsive or ghosting
- Problem unclear or unsolvable
- Close probability: <30%
- Timeline to close: >8 weeks (too far out)
- No realistic path to revenue

---

## The Incubation Test

**Ask yourself:**
> "Is there a clear path from here to a signed deal in the next 8 weeks?"

- **YES, with specific next steps** → Incubate here
- **NO, or very uncertain** → Move to cold prospects or delete
- **YES, and deal is >70% likely** → Move to active-projects

---

## Incubation Stages

### Stage 1: Discovery Complete (30-40% Close)
- Had initial discovery call
- Problem identified and scoped
- Client interested but not committed
- **Next step:** Follow-up meeting or proposal

**Example:** Met with client, they said "interesting, send me a proposal"

### Stage 2: Proposal Delivered (40-60% Close)
- Proposal or scope sent
- Client reviewing
- Negotiations may be ongoing
- **Next step:** Follow-up on proposal, address objections

**Example:** Concrete CEO audit proposal sent, waiting for Tyler's response

### Stage 3: High Probability (60-70% Close)
- Client verbally committed
- Working out final details (pricing, timeline, terms)
- Contract draft in progress
- **Next step:** Finalize agreement and move to active-projects

**Example:** Client said "yes, let's do this," negotiating start date

### Stage 4: Stalled (20-30% Close)
- Was progressing, now stuck
- Client went quiet but not dead
- Waiting on external factor (budget approval, timing, etc.)
- **Next step:** Check-in cadence, re-engage strategy

**Example:** Client said "circle back in Q1" - still warm but not moving

---

## Incubation Management Rules

### Maximum Incubation Time: 8 Weeks

**Why 8 weeks?**
- Long enough to close most deals
- Short enough to avoid wasting time on maybes
- Forces you to qualify or disqualify

**After 8 weeks, you must:**
1. **Move to active-projects** (deal closed or >70% likely)
2. **Archive to cold-prospects/** (deal unlikely, client unresponsive)
3. **Delete** (no longer viable)

### Weekly Review Required

Every week, review each incubated project:
- **What's the status?** (changed since last week?)
- **What's the next action?** (specific, time-bound)
- **What's the close probability?** (increasing or decreasing?)
- **When will this close or die?** (set deadline)

**If you can't answer these questions clearly, it's not a real opportunity.**

---

## Folder Structure for Incubated Projects

```
incubated-projects/
├── README.md                    # This file
├── {project-name}/
│   ├── OPPORTUNITY-BRIEF.md     # One-pager: problem, solution, value
│   ├── CLOSE-PLAN.md            # Path to closed deal
│   ├── meetings/
│   │   └── discovery/           # Discovery call notes
│   └── docs/
│       ├── proposal.md          # If sent
│       └── follow-up-notes.md   # Check-in notes
```

**Lighter structure than active-projects:**
- No full PROJECT-OVERVIEW.md (not committed yet)
- Focus on OPPORTUNITY-BRIEF and CLOSE-PLAN
- Track path to closure, not full project management

---

## Templates

### OPPORTUNITY-BRIEF.md Template

```markdown
# {Project Name} - Opportunity Brief

**Client:** {Name}
**Contact:** {Email/Phone}
**Discovery Date:** {Date}
**Close Probability:** {30-70%}
**Expected Close Date:** {Date}
**Expected Value:** ${X,XXX}

---

## The Problem
{2-3 sentences describing client's pain point}

## The Solution
{2-3 sentences describing what you'd deliver}

## The Value
{Why this matters to client - ROI, time savings, revenue impact}

---

## Status
**Stage:** {Discovery Complete / Proposal Delivered / High Probability / Stalled}
**Last Contact:** {Date}
**Next Action:** {Specific next step with deadline}

---

## Close Blockers
{What's preventing this from closing right now?}

---

## Notes
{Any additional context}
```

### CLOSE-PLAN.md Template

```markdown
# Close Plan - {Project Name}

**Goal:** Move from incubation to active-projects by {Date}

---

## Current Status
- Close Probability: {%}
- Stage: {Discovery / Proposal / High Prob / Stalled}
- Days in Incubation: {X}
- Days Remaining: {8 weeks - X}

---

## Path to Close

### Next 7 Days
- [ ] {Specific action with deadline}
- [ ] {Specific action with deadline}

### Next 2 Weeks
- [ ] {Milestone}
- [ ] {Milestone}

### Next 4 Weeks
- [ ] {Milestone - should be "deal closed" or "qualified out"}

---

## Decision Criteria

**Move to active-projects if:**
- [ ] Contract signed
- [ ] Client verbally committed with >70% confidence
- [ ] Payment terms agreed

**Archive to cold-prospects if:**
- [ ] Client unresponsive for 2+ weeks
- [ ] Close probability drops below 30%
- [ ] 8 weeks elapsed with no progress

**Continue incubating if:**
- [ ] Clear next steps defined
- [ ] Client responsive and engaged
- [ ] Close probability 30-70%
- [ ] Still within 8-week window

---

## Weekly Check-ins

| Week | Date | Action Taken | Client Response | Probability | Notes |
|------|------|--------------|-----------------|-------------|-------|
| 1 | {Date} | {Action} | {Response} | {%} | {Notes} |
| 2 | {Date} | {Action} | {Response} | {%} | {Notes} |

---

## Deal Qualification

**Is this a real opportunity?**
- [ ] Client has budget or can get it
- [ ] Client has authority to make decision
- [ ] Client has genuine need (not nice-to-have)
- [ ] Timeline is realistic (2-8 weeks to close)
- [ ] We can deliver the solution

**If you answered "no" to 2+ questions, disqualify and archive.**
```

---

## Current Incubated Projects

| Project | Client | Stage | Probability | Expected Close | Expected Value | Days in Incubation |
|---------|--------|-------|-------------|----------------|----------------|--------------------|
| [Concrete CEO](./concrete-ceo/) | Tyler | Proposal Development | 50% | Jan 15, 2025 | $6K-25K/mo | 0 (just started) |
| [Ascension Capital](./ascension-capital/) | Linh | Bug Fixes → Delivery | 70% | Jan 2025 | $5K (one-time) | ~30 days |
| [AntSavvy](./antsavvy/) | Client | TBD | TBD% | TBD | TBD | TBD |

**Total Pipeline Value:** $11K-30K+
**Average Close Probability:** ~60%
**Expected Revenue (Weighted):** $6.6K-18K+

---

## Incubation vs Active: The Difference

| Factor | Incubated Projects | Active Projects |
|--------|-------------------|-----------------|
| **Revenue Status** | No commitment yet | Money committed or imminent |
| **Folder Structure** | Lightweight (OPPORTUNITY-BRIEF, CLOSE-PLAN) | Full structure (PROJECT-OVERVIEW, etc.) |
| **Management Intensity** | Weekly check-ins | Daily/weekly active work |
| **Close Probability** | 30-70% | >70% or already closed |
| **Timeline** | 2-8 weeks to close | Actively being worked |
| **Action Focus** | Move to close | Deliver and get paid |
| **Max Duration** | 8 weeks, then decide | Until project complete |

---

## Common Mistakes to Avoid

### ❌ Don't Do This:
- **Hoarding "maybe" projects indefinitely** - 8 weeks max, then decide
- **Treating incubated like active** - Don't build before deal is closed
- **Ignoring for weeks** - Weekly check-ins required
- **Moving too early to active** - Wait for real commitment (>70%)
- **Keeping dead deals** - If client ghosted, archive and move on

### ✅ Do This:
- **Qualify ruthlessly** - Is this a real opportunity or wishful thinking?
- **Set clear deadlines** - When will this close or die?
- **Take weekly action** - Every week, move it forward or disqualify
- **Track close probability** - Is it increasing or decreasing?
- **Graduate to active ASAP** - Once >70%, move to active-projects

---

## Graduation Path

```
Cold Prospect
    ↓
Discovery Call (qualify in or out)
    ↓
Incubated Project (30-70% close probability)
    ↓ (weekly actions to increase probability)
    ↓
Active Project (>70% or deal closed)
    ↓
Revenue
```

**Goal:** Spend minimal time in incubation. Get to "yes" or "no" fast.

---

## Weekly Incubation Review (Friday)

**For each incubated project, answer:**

1. **What happened this week?**
2. **Did close probability increase or decrease?**
3. **What's the specific next action?**
4. **When will that happen?**
5. **Should this stay incubated, move to active, or archive?**

**Time limit:** 5 minutes per project
**Action:** Update CLOSE-PLAN.md with answers

---

## The Incubation Mindset

**Incubation is NOT:**
- A place to hide "maybe" deals you're avoiding
- Long-term storage for lukewarm prospects
- An excuse to delay hard qualification decisions

**Incubation IS:**
- Active nurturing of real opportunities
- Short-term holding (8 weeks max)
- A forcing function to close or disqualify
- Pipeline management with discipline

**Remember:** The goal is to **graduate to active-projects or disqualify**, not to incubate forever.

---

## Metrics to Track

**Pipeline Health:**
- Number of incubated projects
- Average close probability
- Average days in incubation
- Graduation rate (incubated → active)
- Disqualification rate (incubated → archived)

**Target Metrics:**
- 3-5 incubated projects at any time (not 20+)
- Average close probability: >45%
- Average time in incubation: <4 weeks
- Graduation rate: >50%

**If you have 10+ incubated projects, you're hoarding. Qualify or disqualify.**

---

## When to Move Projects

### Move to active-projects/ when:
- [x] Deal closes (contract signed)
- [x] Close probability >70%
- [x] Client verbally committed with clear timeline
- [x] Payment terms agreed

### Archive to cold-prospects/ when:
- [x] Client unresponsive for 2+ weeks
- [x] Close probability <30%
- [x] 8 weeks elapsed with no progress
- [x] Client said "not now, maybe later" (revisit in 6+ months)

### Delete when:
- [x] Client said "no" definitively
- [x] Opportunity no longer viable
- [x] You don't want the project anymore

---

## Process Documents

- **[NEW-PROJECT-INITIALIZATION.md](../active-projects/NEW-PROJECT-INITIALIZATION.md)** - When project becomes active, use this
- **Active Projects Criteria** - See [active-projects/README.md](../active-projects/README.md)

---

## Quick Reference

**Create incubated project when:**
- [ ] Discovery call complete with positive outcome
- [ ] Client expressed genuine interest
- [ ] Close probability: 30-70%
- [ ] Clear path to close in 2-8 weeks

**Graduate to active when:**
- [ ] Deal closed or close probability >70%
- [ ] Contract signed or verbally committed

**Archive when:**
- [ ] 8 weeks elapsed with no closure
- [ ] Client unresponsive or close probability <30%
- [ ] No longer viable

---

**Last Updated:** 2024-12-15

**Remember:** Incubation is temporary. Close it or kill it. Don't let it linger.
