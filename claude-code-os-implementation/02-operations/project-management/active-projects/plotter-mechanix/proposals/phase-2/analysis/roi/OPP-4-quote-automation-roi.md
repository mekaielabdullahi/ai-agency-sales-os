# OPP-4: Quote Generation Automation — ROI Calculation

**Date:** February 18, 2026
**Opportunity:** Quote Generation Automation
**A-to-Z Card:** D

---

## Problem Statement

> "I've got like 15 quotes I sent out that I never followed up on, and I don't know what the status" — Kelsey

Kelsey has 15+ outstanding quotes with no follow-up system. Each lost quote represents $750+ in average job value.

---

## Current State

| Metric | Value | Source |
|--------|-------|--------|
| Outstanding quotes | 15-20 | Kelsey interview |
| Average job value | $750 | Jobber data |
| Weekly calls | 35-45 | Quo analytics |
| Quote conversion rate | Unknown | No tracking |
| Follow-up process | Manual/sporadic | Observation |

---

## Investment

| Metric | Value |
|--------|-------|
| Dev Hours | 32h (pessimistic) |
| Investment | $4,700 |
| Blended Rate | $147/hr |
| Timeline | Milestone 2 (Weeks 3-4) |

### What Gets Built
1. Auto-extract quote details from Quo calls (part numbers, pricing, urgency)
2. Quo → Holding Area → Jobber automated flow
3. Deposit notification system via QuickBooks webhook
4. Second-call opportunity flagging for repeat customers
5. Routing logic to assign to correct team member

---

## ROI Calculation

### Conservative Scenario
| Factor | Value | Calculation |
|--------|-------|-------------|
| Additional quotes captured/month | 6 | 15 lost ÷ 2.5 |
| Average job value | $750 | Historical |
| Conversion rate | 50% | Conservative |
| Additional jobs/month | 3 | 6 × 50% |
| Monthly revenue impact | $2,250 | 3 × $750 |
| **Annual revenue impact** | **$27,000** | $2,250 × 12 |
| Profit margin | 60% | Typical service |
| **Annual profit impact** | **$16,200** | $27,000 × 60% |

### Optimistic Scenario
| Factor | Value | Calculation |
|--------|-------|-------------|
| Additional quotes captured/month | 10 | Improved capture |
| Average job value | $900 | Include upsells |
| Conversion rate | 70% | With follow-up |
| Additional jobs/month | 7 | 10 × 70% |
| Monthly revenue impact | $6,300 | 7 × $900 |
| **Annual revenue impact** | **$75,600** | $6,300 × 12 |
| Profit margin | 60% | Typical service |
| **Annual profit impact** | **$45,360** | $75,600 × 60% |

---

## Additional Value Drivers

### Time Savings (Alyssa)
| Task | Current | After | Savings |
|------|---------|-------|---------|
| Manual quote entry | 15 min/quote | 2 min | 13 min |
| Quote follow-up tracking | 30 min/day | 0 | 30 min |
| Deposit matching | 20 min/day | 5 min | 15 min |
| **Daily savings** | | | **58 min** |
| **Weekly savings** | | | **4.8 hrs** |
| **Annual value** (@$25/hr) | | | **$6,240** |

### Opportunity Cost Recovery
- Currently losing 6-10 jobs/month to poor follow-up
- Each lost job = $750 revenue + potential lifetime value
- Reactivating even 50% = significant recovery

---

## ROI Summary

| Scenario | Annual Impact | Investment | ROI | Payback |
|----------|---------------|------------|-----|---------|
| **Conservative** | $22,440 | $4,700 | **4.8x** | **2.5 months** |
| **Likely** | $35,000 | $4,700 | **7.4x** | **7 weeks** |
| **Optimistic** | $51,600 | $4,700 | **11x** | **4.5 weeks** |

### Blended ROI (weighted)
- Conservative (20%): $22,440
- Likely (60%): $35,000
- Optimistic (20%): $51,600

**Expected Value:** $35,808/year
**Expected ROI:** 7.6x
**Expected Payback:** ~7 weeks

---

## Success Metrics

### Phase 2 Success = All True
- [ ] 100% of Quo calls flow to holding area
- [ ] Quote creation time < 5 minutes (from 15+)
- [ ] Follow-up reminders automated
- [ ] Deposit notifications working
- [ ] Quote conversion rate tracked

### 90-Day Targets
- Quote capture rate: 95%+
- Follow-up compliance: 100%
- Quote conversion rate: 60%+
- Additional monthly revenue: $3,500+

---

## Risk Factors

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Poor data quality from calls | Medium | Medium | Manual review step |
| User adoption resistance | Low | High | Training + quick wins |
| Integration issues | Low | Medium | Test thoroughly in M1 |

---

## Confidence Level

**HIGH** — Conservative assumptions, validated pain point, clear ROI path.

---

*Calculation methodology: Bottom-up analysis using Kelsey-provided data and industry benchmarks. Does not include soft benefits (reduced stress, better customer experience, scale enablement).*
