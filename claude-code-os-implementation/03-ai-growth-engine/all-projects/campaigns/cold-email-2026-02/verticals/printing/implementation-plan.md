# Implementation Plan: Pain Point Hook Sequences

## Overview

This plan deploys 4 new email sequences (A-D) alongside the existing proof-led sequence to A/B test which pain point hooks resonate best with wide-format printer service companies.

---

## Week 1: Setup (Days 1-5)

### Day 1-2: Review & Prepare
- [ ] Review existing campaign in `email-sequence.md`
- [ ] Review pain points documentation in `pain-points-hooks.md`
- [ ] Verify all 4 new sequences (A-D) are ready
- [ ] Align with `PRESALE-EXECUTION-PLAYBOOK.md`

### Day 3-4: Build Target List
- [ ] Apollo/Clay query for 50 contacts (wide-format printer service)
- [ ] Apply ICP filters from `icp-profile.md`
- [ ] Enrich with personalization data
- [ ] Assign to sequences (see distribution below)

### Day 5: Load & Verify
- [ ] Load contacts into n8n workflow
- [ ] Verify personalization variables populate correctly
- [ ] Test send to internal addresses
- [ ] Schedule first sends for Tuesday

---

## Week 2-3: Deploy (Days 6-20)

### Sequence Distribution

| Sequence | Contacts | Hook | File |
|----------|----------|------|------|
| Main (proof-led) | 20 | Plotter Mechanix case study | `email-sequence.md` |
| A (owner bottleneck) | 10 | "If I don't come to work..." | `email-sequences/sequence-a-owner-bottleneck.md` |
| B (communication chaos) | 10 | "10 inboxes, zero sanity" | `email-sequences/sequence-b-communication-chaos.md` |
| C (inventory blindness) | 10 | "Let me check and call you back" | `email-sequences/sequence-c-inventory-blindness.md` |

**Note:** Sequence D (training tax) reserved for Week 3 rotation or winners' pool.

### Send Schedule (All Sequences)

| Email | Day of Week | Time |
|-------|-------------|------|
| Email 1 | Tuesday | 9-11am local |
| Email 2 | Saturday | 9-11am local |
| Email 3 | Wednesday | 9-11am local |
| Email 4 | Sunday | 9-11am local |

### Daily Tracking
- [ ] Check replies in unified inbox
- [ ] Log responses in `outreach-tracker-2026-02.md`
- [ ] Move positive replies to 5 Questions discovery
- [ ] Update `metrics-dashboard.md` with open/reply rates

---

## Week 4+: Optimize

### A/B Test Analysis

| Metric | How to Measure |
|--------|----------------|
| Open rate | Subject line effectiveness |
| Reply rate | Hook resonance |
| Positive sentiment | Quality of responses |
| Discovery calls booked | Conversion to pipeline |

### Optimization Actions

1. **Double down on winners:** Shift more contacts to highest-performing sequence
2. **Refine subject lines:** Test new variants based on open rate data
3. **Combine hooks:** Mix high-performing opener with proof-led close
4. **Add Sequence D:** Rotate training tax sequence into live testing

---

## Target Metrics (From Playbook)

| Metric | Target | Source |
|--------|--------|--------|
| Response rate | 15-20% | PRESALE-EXECUTION-PLAYBOOK |
| Discovery calls booked | 3-5/week | Pipeline goal |
| Printing vertical closed | 1/month | Revenue target |

---

## Integration Points

### 5 Questions Discovery
Move responding leads to discovery call using:
- `discovery-call-guide.md` for call script
- `arise-group-ai-outreach-framework.md` for 5 Questions methodology

### Gold Standard Offer
Include in all sequences:
> "I'll audit your operations and build ONE automation for free. If it saves you time, we talk. If not, we shake hands. Zero risk."

### Case Study Pipeline
Successful closes become future case study content:
- Phase 1 completion → testimonial
- Phase 2 completion → full case study
- Rotate into proof-led sequence

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `email-sequence.md` | Main proof-led sequence |
| `pain-points-hooks.md` | 8 pain points with hooks |
| `email-sequences/` | 4 hook-based sequences |
| `icp-profile.md` | Target company criteria |
| `discovery-call-guide.md` | Post-reply call script |
| `case-study-brief.md` | Plotter Mechanix proof |
| `../../operations/metrics-dashboard.md` | Campaign tracking |
| `../../operations/reply-handling.md` | Response procedures |

---

## Success Criteria

**Week 2:** First responses received, at least 1 discovery call booked
**Week 4:** Clear winner identified among sequences A-D
**Month 2:** 2-4 discovery calls/week, 1 close in pipeline
**Month 3:** Optimized sequence running at scale, 2nd case study in development
