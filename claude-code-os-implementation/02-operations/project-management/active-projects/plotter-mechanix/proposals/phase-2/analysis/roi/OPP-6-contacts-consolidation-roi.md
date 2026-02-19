# OPP-6: Contacts Consolidation — ROI Calculation

**Date:** February 18, 2026
**Opportunity:** Contact Database Consolidation
**A-to-Z Card:** H

---

## Problem Statement

> "Andrew can only see 2 contacts while I have 10,581. The team can't access customer info." — Kelsey

A 5,290:1 contact visibility gap is blocking supplies sales, customer service, and team efficiency.

---

## Current State

| Metric | Value | Source |
|--------|-------|--------|
| Kelsey's contacts | 10,581 | Capsule count |
| Andrew's contacts | 2 | Capsule count |
| Data silos | 4 | Capsule, Jobber, QB, Outlook |
| Duplicate rate | Unknown | Estimated 20-40% |
| Time finding contacts | 10-15 min/lookup | Observation |
| Missed sales opportunities | Weekly | Andrew feedback |

---

## Investment

| Metric | Value |
|--------|-------|
| Dev Hours | 38h (pessimistic) |
| Investment | $5,590 |
| Blended Rate | $147/hr |
| Timeline | Milestone 2 (Weeks 3-4) |

### What Gets Built
1. Capsule export + cleanup (10,581 contacts normalized)
2. Jobber import as master source of truth
3. Duplicate merge rules and deduplication
4. Team-wide contact visibility
5. QuickBooks sync (Phase 3 enhancement)

---

## ROI Calculation

### Andrew Supplies Sales Unlock

| Factor | Before | After | Impact |
|--------|--------|-------|--------|
| Contacts visible | 2 | 10,000+ | +5,000x |
| Outreach capacity | 2/day | 20/day | +900% |
| Sales calls/week | 10 | 100 | +90 |
| Conversion rate | 5% | 5% | Maintained |
| New customers/month | 2 | 20 | +18 |
| Avg. supplies order | $150 | $150 | Maintained |
| **Monthly supplies revenue** | $300 | **$3,000** | **+$2,700** |
| **Annual supplies revenue** | $3,600 | **$36,000** | **+$32,400** |

### Supplies Margin Impact
- Supplies margin: 40-60% (wholesale to retail)
- Annual profit impact: $32,400 × 50% = **$16,200**

### Time Savings (All Staff)

| Task | Current | After | Weekly Savings |
|------|---------|-------|----------------|
| Contact lookup | 15 min | 2 min | 65 min/day |
| Duplicate resolution | 30 min/day | 5 min | 125 min/wk |
| Data entry across systems | 45 min/day | 10 min | 175 min/wk |
| AR research | 1 hr/day | 15 min | 225 min/wk |
| **Weekly time savings** | | | **9.8 hrs** |
| **Annual time savings** | | | **510 hrs** |
| **Value (@$25/hr)** | | | **$12,750** |

### AR Recovery Potential

| Factor | Value |
|--------|-------|
| Estimated AR overdue | $50,000+ |
| Contacts with bad info | 15% |
| Recoverable with good data | $7,500 |
| Collection rate | 60% |
| **One-time AR recovery** | **$4,500** |

### Marketing Foundation
- Clean contact database enables email marketing
- 10,000 contacts × 2% response × $200 avg = $40,000 potential
- **Phase 3 revenue potential:** $40,000+/year

---

## Comprehensive Annual Impact

### Conservative Scenario
| Component | Annual Value |
|-----------|--------------|
| Andrew supplies increase | $16,200 |
| Time savings | $12,750 |
| AR recovery (one-time) | $4,500 |
| **Total Conservative** | **$33,450** |

### Optimistic Scenario
| Component | Annual Value |
|-----------|--------------|
| Andrew supplies increase | $32,400 |
| Time savings | $20,000 |
| AR recovery | $7,500 |
| Marketing foundation | $20,000 |
| **Total Optimistic** | **$79,900** |

---

## ROI Summary

| Scenario | Annual Impact | Investment | ROI | Payback |
|----------|---------------|------------|-----|---------|
| **Conservative** | $33,450 | $5,590 | **6x** | **8 weeks** |
| **Likely** | $50,000 | $5,590 | **9x** | **6 weeks** |
| **Optimistic** | $79,900 | $5,590 | **14x** | **4 weeks** |

---

## Strategic Value

### Immediate
- Andrew can sell to anyone, not just 2 people
- Team has single source of truth
- Customer service improves dramatically

### Long-term
- Marketing campaigns possible
- Business intelligence enabled
- Scale to multiple salespeople
- Business valuation increases

---

## Success Metrics

### Phase 2 Success = All True
- [ ] All 10,581 contacts imported to Jobber
- [ ] Duplicates reduced by 80%+
- [ ] Andrew sees full database
- [ ] Lookup time < 30 seconds
- [ ] Team accessing contacts daily

### 90-Day Targets
- Andrew supplies sales: +300%
- Contact lookup time: -85%
- Duplicate contacts: < 500
- Weekly outreach: 50+ contacts

---

## Risk Factors

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Data quality issues | High | Medium | Audit in M1, set expectations |
| Import complications | Medium | Medium | Test with subset first |
| User adoption | Low | Medium | Training + quick wins |

---

## Confidence Level

**MEDIUM-HIGH** — Contact gap is real and quantified. Supplies revenue assumption needs validation with Andrew.

---

## Dependencies

- Capsule data exportable (confirmed)
- Jobber import API available (confirmed)
- Andrew available for training (needs scheduling)

---

*Calculation methodology: Bottom-up analysis using actual contact counts and industry sales metrics. Supplies revenue based on conservative outreach-to-sale conversion rates.*
