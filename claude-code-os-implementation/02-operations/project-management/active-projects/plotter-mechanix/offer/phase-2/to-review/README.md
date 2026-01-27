# Phase 2 To-Review Folder

**Status:** Ready for internal team review
**Created:** January 24, 2026
**Next Action:** Mekaiel, Trent, Chris, and Matthew review, then launch validation phase (2-3 weeks before Phase 2 start)

---

## What's In This Folder

### 1. PHASE-2-PROPOSAL.md
**Audience:** Kelsey, Nikki, Megan (final decision makers)
**Purpose:** Clean client-facing proposal with 10x scale framework
**Investment:** $47,000
**Expected ROI:** $116,600/year (248% return, 4.8 month payback)

**Key Sections:**
- Executive Summary (10x scale test)
- 5 Business Problems Menu
- Deliverables breakdown
- Timeline (4-6 weeks)
- How we support Andrew/Megan initiatives
- ROI validation process
- Success metrics
- Pricing justification (AAA framework)

**When to use:** After validation phase complete, present to close Phase 2

---

### 2. VALIDATION-ACTION-PLAN.md
**Audience:** Internal (Matthew, Chris) + Kelsey/team for data collection
**Purpose:** 2-3 week action plan to validate ROI before finalizing Phase 2
**Timeline:** Start immediately, complete before presenting Phase 2 proposal

**Key Sections:**
- What we're validating (time spent, business metrics)
- Time tracking templates (Alyssa 5-activity, Kelsey training time)
- Interview guides (Megan, Andrew, Kelsey, Alyssa)
- Jobber data analysis templates
- Week-by-week execution plan
- Final validation report template

**When to use:** NOW - start setting up time tracking and scheduling interviews

---

## Workflow: From Here to Phase 2 Close

```
┌─────────────────────────────────────────────────────────────┐
│ Week 1-2: Data Collection (VALIDATION-ACTION-PLAN.md)      │
├─────────────────────────────────────────────────────────────┤
│ □ Set up Alyssa's 5-activity time tracking (5 days)        │
│ □ Set up Kelsey's training time tracking (5 days)          │
│ □ Schedule & conduct Megan interview (Ply status, API)     │
│ □ Schedule & conduct Andrew interview (supplies process)   │
│ □ Request Jobber data export                               │
│ □ Request business financials (revenue, customer count)    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Week 2-3: Analysis & ROI Validation                        │
├─────────────────────────────────────────────────────────────┤
│ □ Compile time tracking data                               │
│ □ Analyze Jobber data (contracts, churn, equipment)        │
│ □ Process interview insights                               │
│ □ Calculate validated ROI (replace assumptions)            │
│ □ Adjust pricing if needed (maintain 2.5:1+ ratio)         │
│ □ Update PHASE-2-PROPOSAL.md with validated numbers        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Week 3-4: Client Presentation                              │
├─────────────────────────────────────────────────────────────┤
│ □ Present PHASE-2-PROPOSAL.md with data-backed ROI         │
│ □ Address questions/concerns                               │
│ □ Negotiate if needed (scope or price)                     │
│ □ Close at $42k-$57k (depending on validated ROI)          │
│ □ Sign contract, collect 50% upfront                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Week 4-10: Phase 2 Delivery (4-6 weeks)                    │
├─────────────────────────────────────────────────────────────┤
│ See timeline in PHASE-2-PROPOSAL.md                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Immediate Next Steps

### 1. Internal Team Review
- [ ] **Mekaiel** reviews PHASE-2-PROPOSAL.md (pricing strategy, technical approach)
- [ ] **Trent** reviews business case and ROI calculations
- [ ] **Chris** reviews filming/training deliverables for feasibility
- [ ] **Matthew** reviews VALIDATION-ACTION-PLAN.md and overall process
- [ ] Team confirms developer capacity for $47k scope
- [ ] Team validates margin and timeline
- [ ] Get alignment on "go/no-go" decision

### 2. Start Validation Phase
- [ ] Email Kelsey requesting time tracking participation
- [ ] Email Alyssa with time tracking templates
- [ ] Schedule Megan interview (30-45 min)
- [ ] Schedule Andrew interview (30 min)
- [ ] Request Jobber data export access

### 3. Prepare for Phase 2
- [ ] Confirm budget ceiling with Kelsey/Nikki
- [ ] Research Ply API documentation (if public)
- [ ] Review Quo API capabilities (chat agent integration)
- [ ] Identify developer resources for integration work

---

## Key Decisions Made

### Pricing: $47,000
**Rationale:**
- AAA framework: $153,600 (Year 1 ROI) ÷ 2.5 = $61,440 recommended
- Our price: $47,000 (below formula to account for vendor fatigue)
- Value-to-price ratio: 3.3:1 (client gets $3.30 per $1 invested)
- Exceeds industry standard 2.5:1 ratio

### Timeline: 4-6 Weeks
**Rationale:**
- Compressed delivery (was 8 weeks in earlier draft)
- Parallel execution (training + CRM + chat agent simultaneously)
- Week 6 optional polish (can finish in 4-5 weeks if needed)

### Deliverables: 5 Core Components
1. **Training System** ($18k) - Chris filming, 25-30 videos, knowledge base
2. **Equipment CRM** ($10k) - Customer equipment database, service contract scoring
3. **Unified Chat Agent** ($10k) - Single interface for Ply, Quo, Jobber, QuickBooks
4. **Email Automation** ($5k) - Vendor pricing extraction, RMA routing, PO tracking
5. **Integration Work** ($4k) - Connect all systems, data flows automatically

### Technical Architecture
**Chat Agent Approach** (solves "can't modify Quo UI" constraint):
- Chat agent has tool access to: Ply, Quo, Jobber, QuickBooks, Equipment CRM
- When Quo call starts → webhook → N8N → Chat agent auto-populates customer context
- Alyssa sees equipment, inventory, history WITHOUT switching systems
- Natural language queries: "Do we have T730 maintenance kit?" → instant answer

**Support, Don't Replace:**
- Megan's Ply: We query via API, fill gaps (equipment history, used parts)
- Andrew's supplies: Interview to understand, build tools that FIT his workflow
- Phase 1 foundation: Build on existing Quo→Jobber webhook infrastructure

---

## Open Questions (To Resolve During Validation)

### For Megan (Interview):
1. Does Ply have an API we can use?
2. What's Ply's Jobber integration status?
3. What gaps does Ply NOT cover?
4. How much used parts inventory exists? (estimated $50k)

### For Andrew (Interview):
5. What's your supplies sales process?
6. What tools would help you scale supplies revenue?
7. Where do you track customer relationships?

### For Kelsey/Nikki (Financial):
8. What's the actual annual revenue? (estimated $600k)
9. What's your Phase 2 budget ceiling?
10. What pain points are MOST urgent to solve?

### For Team (Time Tracking):
11. Alyssa's email processing time? (currently unknown)
12. Alyssa's context-switching time? (currently unknown)
13. Kelsey's training time? (estimated 5 hrs/week, needs validation)
14. "Do we have X?" interruptions? (estimated 10/day, needs validation)

---

## Risk Mitigation

### Risk 1: Validated ROI Lower Than Estimated
**Mitigation:** Adjust price or scope to maintain 2.5:1+ value-to-price ratio

### Risk 2: Ply API Doesn't Exist or Is Limited
**Mitigation:** Build standalone inventory lookup tool (Option 2 in `../internal/quo-ply-integration-technical.md`)

### Risk 3: Team Doesn't Adopt New Systems
**Mitigation:**
- Weekly check-ins during delivery
- 30-day validation milestones
- Training and documentation included
- Systems work whether behavior changes or not

### Risk 4: Budget Constraint ($47k Too High)
**Mitigation:** Offer phased delivery (Phase 2A + 2B) or modular approach

---

## Files Referenced

### In This Folder (to-review/):
- `PHASE-2-PROPOSAL.md` - Client-facing proposal
- `VALIDATION-ACTION-PLAN.md` - Internal validation playbook

### In Parent Folder (offer/phase-2/):
- `PHASE-2-PLAN.md` - Technical implementation plan
- `PRICING-ANALYSIS.md` - Internal pricing strategy
- `PRICING-BREAKDOWN.md` - Client-facing pricing document
- `BUSINESS-PROBLEMS-MENU.md` - 10x scale analysis
- `PHASE-2-GAP-ANALYSIS.md` - Draft-02 vs current plan comparison
- `QUO-PLY-INTEGRATION-DETAIL.md` - Technical deep dive on inventory integration

---

## Success Criteria

**Validation Phase Success:**
- ✅ 70%+ of ROI assumptions replaced with validated data
- ✅ Megan and Andrew interviews completed with actionable insights
- ✅ Budget ceiling confirmed with Kelsey/Nikki
- ✅ Updated proposal reflects real business data

**Phase 2 Close Success:**
- ✅ Proposal presented with confidence (data-backed)
- ✅ Client understands value (3.3:1 ratio clear)
- ✅ Contract signed at $42k-$57k (depending on validated scope)
- ✅ 50% deposit collected
- ✅ Delivery timeline agreed (4-6 weeks)

**Phase 2 Delivery Success:**
- ✅ All 5 deliverables working as specified
- ✅ Team trained and confident using systems
- ✅ ROI targets hit within 90 days
- ✅ Ready to hire Steve (new technician)
- ✅ Phase 3 pipeline identified ($20k-80k potential)

---

*Last Updated: January 24, 2026*
*Owner: Matthew Kerns*
*Status: Ready for validation phase kickoff*
