# S&S Wolf Sheds - Phase 3 Opportunity Matrix

**Created:** January 3, 2026
**Phase:** 3 of 4 - Intelligence & Operations
**Investment:** TBD (estimate $5,000-$10,000)
**Timeline:** 2-3 weeks (Month 3)
**Trigger:** Phase 2 complete, QR system generating data
**Source:** [PRD-lot-assistant.md](../docs-workbook1/PRD-lot-assistant.md)

---

## Executive Summary

Phase 3 transforms raw data into actionable intelligence and solves the "last-mile" delivery problem. This phase also introduces the Dealer Accountability App to support multi-location expansion (Kayenta hub).

**Phase 1 Delivered:** ROI baseline, website fixes, database foundation, lead qualification form
**Phase 2 Delivered:** QR capture system, pricing configurator, CRM pipeline, SOP generator tool
**Phase 3 Delivers:** Financial dashboards, delivery intelligence, accountability system, ideal customer profile analytics

**Timeline Context (from Jan 3 Meeting):**
- **March/April:** Major ad campaigns planned - need systems ready to capture and qualify leads
- **4th of July Sale:** Major event - want full system operational and data-informed by then
- Data collection from Phase 1 form provides 2-3 months of baseline before campaigns

---

## PRD Mapping

| PRD Component | Phase | Status |
|---------------|-------|--------|
| Sheet 1: Master Shed Data | Phase 1 | ✅ Complete |
| Sheet 7: CODB Calculator | Phase 1 | ✅ Complete |
| Sheet 3: Optional Features | Phase 2 | ✅ Complete |
| Sheet 2: Pricing Lookup | Phase 2 | ✅ Complete |
| Sheet 4: CRM Pipeline | Phase 2 | ✅ Complete |
| **Sheet 5: Customer Profile & Delivery** | **Phase 3** | ⬜ This Phase |
| **Sheet 6: Financial Dashboard** | **Phase 3** | ⬜ This Phase |
| Secure Driver Access | Phase 3 | ⬜ This Phase |
| Geofence Trigger | Phase 4 | ⏳ Next Phase |

---

## Impact vs Effort Matrix

```
                          IMPACT
                    LOW         HIGH
              ┌───────────┬───────────┐
         LOW  │           │ P3-DASH   │
              │           │  ★★★★☆   │
    EFFORT    │           │           │
              │           │           │
              ├───────────┼───────────┤
              │           │ P3-DELIV  │
         MED  │           │ P3-ACCT   │
              │           │  ★★★★★   │
              └───────────┴───────────┘
```

---

## Phase 3 Opportunities

### P3-DELIVERY: Customer Profile & Delivery Intelligence (Sheet 5)

**Status:** ★★★★★ PHASE 3 PRIORITY

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Drivers lack site specifics; failed deliveries due to access constraints; no systematic delivery prep |
| **Solution** | Customer profile system with delivery notes, secure driver access links |
| **Impact** | HIGH - Reduced failed deliveries, better customer experience, driver efficiency |
| **Effort** | MEDIUM - 1 week |
| **Investment** | Part of Phase 3 |
| **Dependencies** | CRM with customer data (Phase 2) |
| **IP Risk** | LOW - Standard delivery logistics |
| **Timeline** | Week 1 |

#### Data Structure (Sheet 5)

| Field | Description |
|-------|-------------|
| `customer_id` | Links to CRM lead |
| `delivery_address` | Full address |
| `site_map_link` | Google Maps / What3Words |
| `gate_code` | Access codes |
| `site_hazards` | Wash areas, pooling, slopes, overhead lines |
| `access_notes` | Width restrictions, turn requirements |
| `preferred_orientation` | How customer wants shed positioned |
| `contact_phone` | Day-of delivery contact |
| `special_instructions` | Any other notes |

#### Secure Driver Access

```
Delivery assigned → System generates unique link →
    → Link filtered to show ONLY this job's notes
    → Driver sees: address, map, gate code, hazards
    → Driver does NOT see: pricing, customer history, other jobs
    → Link expires after delivery confirmed
```

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Sheet 5: Customer Profile | Delivery notes database | ⬜ Pending |
| Site Info Collection Form | Customer fills during sale | ⬜ Pending |
| Driver Link Generator | Unique filtered links per job | ⬜ Pending |
| Mobile Driver View | Optimized for phone/tablet | ⬜ Pending |
| Delivery Confirmation | Mark complete, trigger follow-up | ⬜ Pending |

#### Success Metrics

- [ ] All deliveries have site profiles
- [ ] Driver access links working
- [ ] Failed delivery rate decreased
- [ ] Scott (driver) using system

---

### P3-DASHBOARD: Financial Performance Dashboard (Sheet 6)

**Status:** ★★★★☆ WEEK 1-2

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No visibility into marketing ROI, cost per lead, acquisition costs; can't optimize spend |
| **Solution** | Automated dashboard calculating CPL, CAC, ROAS from CRM + ad spend data |
| **Impact** | HIGH - Data-driven marketing decisions, prove ROI, optimize spend |
| **Effort** | LOW-MEDIUM - 1 week |
| **Investment** | Part of Phase 3 |
| **Dependencies** | CRM with lead source tracking (Phase 2), ad spend data |
| **IP Risk** | MEDIUM - Proprietary calculations |
| **Timeline** | Week 1-2 |

#### KPI Definitions

| Metric | Formula | Target |
|--------|---------|--------|
| **CPL (Cost Per Lead)** | Ad Spend ÷ Leads Generated | Track by source |
| **CAC (Customer Acquisition Cost)** | Total Sales Cost ÷ Customers Won | < Average Sale Margin |
| **ROAS (Return on Ad Spend)** | Revenue from Ads ÷ Ad Spend | > 3:1 |
| **Conversion Rate** | Won Deals ÷ Total Leads | Track by source |
| **CODB per Sale** | Daily Operating Cost ÷ Units Sold | From Phase 1 |

#### Dashboard Views

| View | Audience | Shows |
|------|----------|-------|
| Executive Summary | Sandy/Chris | Revenue, profit, key KPIs |
| Marketing Performance | Alex | CPL, ROAS by channel |
| Sales Pipeline | Sales team | Funnel, conversion rates |
| Lot Comparison | Management | Performance by location |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Sheet 6: Financial Dashboard | Automated reporting engine | ⬜ Pending |
| Ad Spend Tracking | Integration or manual entry | ⬜ Pending |
| CPL Calculator | By source (Facebook, Google, Walk-in, QR) | ⬜ Pending |
| CAC Calculator | Total cost to acquire customer | ⬜ Pending |
| ROAS Calculator | Revenue attribution to ad spend | ⬜ Pending |
| Visual Dashboard | Charts, graphs, trends | ⬜ Pending |

#### Success Metrics

- [ ] KPIs calculating correctly
- [ ] Dashboard updated automatically
- [ ] Sandy/Chris using for decisions
- [ ] Marketing spend optimized based on data

---

### P3-ACCOUNT: Dealer Accountability App

**Status:** ★★★★★ WEEK 2 (Critical for Expansion)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Multi-location management; staffing quality; no way to verify daily tasks; Sandra "driving her ass off" to check on lots |
| **Solution** | Proprietary app with individual logins, daily checklists, photo verification, deposit tracking |
| **Impact** | HIGH - Scalable operations, quality control, expansion enabler |
| **Effort** | MEDIUM-HIGH - 1-2 weeks |
| **Investment** | Part of Phase 3 (may require additional budget) |
| **Dependencies** | Expansion to Kayenta (happening Feb/March) |
| **IP Risk** | HIGH - Proprietary methodology |
| **Timeline** | Week 2 |

#### Daily Checklist Items (from Dec 30 Meeting)

| Category | Check Item |
|----------|------------|
| **Opening** | Lights on |
| **Opening** | Doors open/accessible |
| **Opening** | Keys put away properly |
| **Maintenance** | Gas check (need gas tomorrow?) |
| **Maintenance** | 1 hour lot cleanup completed |
| **Content** | Good pictures of buildings taken |
| **Content** | 360 images for website |
| **Content** | Social media post (favorite building) |
| **Closing** | Deposit photo before clock-out |
| **Closing** | Security cameras verified |

#### System Features

| Feature | Description |
|---------|-------------|
| Individual Logins | Each rep has own account |
| Location Tracking | Verify they're at the lot |
| Photo Upload | Required for certain tasks |
| Deposit Verification | Photo + amount + camera sync |
| Clock In/Out | Can't clock out without deposit photo |
| Manager Dashboard | See all reps, all locations |
| Performance Scoring | Monthly bonuses based on compliance |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Rep Mobile App | Daily checklist interface | ⬜ Pending |
| Manager Dashboard | Multi-location oversight | ⬜ Pending |
| Photo Upload System | Image capture + storage | ⬜ Pending |
| Deposit Tracking | Amount + photo + verification | ⬜ Pending |
| Performance Reports | Weekly/monthly scoring | ⬜ Pending |
| Alert System | Notify manager of missed tasks | ⬜ Pending |

#### Success Metrics

- [ ] All reps using app daily
- [ ] Checklist completion rate > 90%
- [ ] Deposit verification working
- [ ] Sandra not driving to check on lots daily
- [ ] Ready for Kayenta opening

---

### P3-ICP: Ideal Customer Profile Analytics

**Status:** ★★★★★ WEEK 2 (Marketing Optimization)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No understanding of who the ideal customer is; can't target marketing effectively; don't know which customers buy multiple sheds, biggest purchases, best to work with |
| **Solution** | Analytics dashboard using baseline data collected from lead qualification form + purchase data to identify ideal customer profile |
| **Impact** | HIGH - Target marketing for March/April campaigns, improve ad ROI, focus sales efforts |
| **Effort** | LOW-MEDIUM - 3-5 days |
| **Investment** | Part of Phase 3 |
| **Dependencies** | Lead qualification form data from Phase 1, CRM data from Phase 2 |
| **IP Risk** | MEDIUM - Proprietary customer insights |
| **Timeline** | Week 2 |

#### Data Sources (from Jan 3 Meeting)

> "You should probably collect those questions from every single person that buys a shed, so that when you see these are how they answered it, and they bought this... they were our ideal purchase" - Trent

| Data Source | Insights |
|-------------|----------|
| Lead Qualification Form | Product type, intended use, property access, timeline |
| CRM Pipeline | Close rate by lead type, time to close |
| Purchase History | Average order value, repeat buyers, referral sources |
| Lot Data | Which locations convert best, walk-in vs online |

#### Ideal Customer Profile Dimensions

| Dimension | Questions Answered |
|-----------|-------------------|
| **Demographics** | Who buys? Where are they located? |
| **Product Fit** | What product types do they buy? What sizes? |
| **Buying Behavior** | How quickly do they decide? What's their budget? |
| **Delivery Fit** | Easy access properties? Rural vs suburban? |
| **Value** | Who buys multiple? Who refers others? |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| ICP Dashboard | Visual profile of ideal customer | ⬜ Pending |
| Segment Analysis | Group customers by behavior | ⬜ Pending |
| Lead Scoring Model | Score new leads against ICP | ⬜ Pending |
| Marketing Recommendations | Target audience for March/April ads | ⬜ Pending |

#### Success Metrics

- [ ] ICP clearly defined with data backing
- [ ] Lead scoring working on new leads
- [ ] Marketing recommendations ready for March campaigns
- [ ] Measurable improvement in ad targeting

---

### P3-ANALYTICS: Traffic & Conversion Analytics

**Status:** ★★★☆☆ OPTIONAL (if budget allows)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No measurement of lot traffic vs conversion; can't quantify improvement |
| **Solution** | Camera-based vehicle counting at single entry/exit point |
| **Impact** | MEDIUM-HIGH - Baseline for ROI measurement |
| **Effort** | MEDIUM - Hardware + setup |
| **Investment** | $1,500-$3,000 additional |
| **Dependencies** | Single entry/exit confirmed at lots |
| **IP Risk** | LOW - Standard analytics |
| **Timeline** | If budget allows |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Vehicle Counter | Camera or sensor at entry | ⬜ Optional |
| Daily Count Log | Automatic logging | ⬜ Optional |
| Conversion Calculator | Visitors ÷ Sales | ⬜ Optional |
| Trend Analysis | Week-over-week comparison | ⬜ Optional |

---

## Phase 3 Consolidated Summary

| ID | Opportunity | Impact | Effort | Week | Priority |
|----|-------------|--------|--------|------|----------|
| **P3-DELIVERY** | Customer Profile & Delivery Intel | ★★★★★ | MED | 1 | #1 Operations |
| **P3-DASHBOARD** | Financial Performance Dashboard | ★★★★☆ | LOW-MED | 1-2 | #2 Intelligence |
| **P3-ACCOUNT** | Dealer Accountability App | ★★★★★ | MED-HIGH | 2 | #3 Expansion |
| **P3-ICP** | Ideal Customer Profile Analytics | ★★★★★ | LOW-MED | 2 | #4 Marketing |
| P3-ANALYTICS | Traffic Counting | ★★★☆☆ | MED | Optional | If budget |

**Total Phase 3 Investment:** $5,000-$10,000 (TBD based on accountability app scope)
**Timeline:** 2-3 weeks
**Critical Milestone:** ICP analysis ready for March/April ad campaigns

---

## Implementation Schedule

### Week 1: Delivery & Dashboard

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Sheet 5 data structure | Developer | 1 | ⬜ |
| Site info collection form | Developer | 1-2 | ⬜ |
| Driver link generator | Developer | 2-3 | ⬜ |
| Sheet 6 dashboard setup | Developer | 2-3 | ⬜ |
| KPI calculators | Developer | 3-4 | ⬜ |
| Dashboard visualization | Developer | 4-5 | ⬜ |
| Testing | All | 5 | ⬜ |

### Week 2: Accountability App + ICP Analytics

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| App architecture design | Developer | 1 | ⬜ |
| Rep login system | Developer | 1-2 | ⬜ |
| Daily checklist UI | Developer | 2-3 | ⬜ |
| ICP data analysis | AriseGroup | 2-3 | ⬜ |
| Photo upload system | Developer | 3 | ⬜ |
| Deposit tracking | Developer | 3-4 | ⬜ |
| ICP dashboard build | Developer | 3-4 | ⬜ |
| Lead scoring model | Developer | 4 | ⬜ |
| Manager dashboard | Developer | 4 | ⬜ |
| Marketing recommendations | AriseGroup | 4-5 | ⬜ |
| Testing + training | All | 5 | ⬜ |

---

## Dependencies Map

```
P2-CRM (Phase 2)
    │
    ├──► P3-DELIVERY (Week 1) - Customer data feeds delivery profiles
    │
    └──► P3-DASHBOARD (Week 1-2) - Lead data enables CPL/CAC calculations

P2-QR (Phase 2)
    │
    └──► P3-DASHBOARD (Week 1-2) - Scan data for attribution

P3-DELIVERY (Week 1)
    │
    └──► Scott (Driver) adopts system

P3-ACCOUNT (Week 2)
    │
    └──► Kayenta Expansion (Feb/March) - Required for multi-location
```

---

## Risk Assessment

| Opportunity | Risk Level | Key Risk | Mitigation |
|-------------|------------|----------|------------|
| P3-DELIVERY | LOW | Driver adoption | Involve Scott in design |
| P3-DASHBOARD | LOW | Data accuracy | Validate formulas with Sandy |
| P3-ACCOUNT | MEDIUM | Rep resistance | Tie to bonuses, start simple |
| P3-ANALYTICS | MEDIUM | Hardware complexity | Defer if budget tight |

---

## Success Criteria

### Phase 3 Complete When:

- [ ] Delivery profiles created for all active orders
- [ ] Driver access links working
- [ ] Financial dashboard calculating CPL, CAC, ROAS
- [ ] Accountability app deployed to at least 1 lot
- [ ] Checklist completion rate > 80%

### Phase 4 Trigger:

- [ ] All Phase 3 systems stable
- [ ] Kayenta lot opened
- [ ] Data flowing across all systems
- [ ] Ready for full Firebase migration

---

## Related Documents

- [Phase 1 Opportunity Matrix](./phase-1-opportunity-matrix.md)
- [Phase 2 Opportunity Matrix](./phase-2-opportunity-matrix.md)
- [Main PRD](../docs-workbook1/PRD-lot-assistant.md)
- [Dec 30 Meeting Summary](../meetings/2025-12-30-expansion-strategy/summary.md)

---

**Last Updated:** January 3, 2026
**Status:** Ready for Phase 2 completion
**Next Action:** Complete Phase 2 → Begin Phase 3

---

## Revision History

| Date | Version | Changes | Source |
|------|---------|---------|--------|
| Jan 3, 2026 | 1.1 | Added P3-ICP (Ideal Customer Profile Analytics); Added timeline context for March/April campaigns and 4th of July; Updated Phase 1/2 delivered items | Jan 3 Team Review Huddle |
| Jan 3, 2026 | 1.0 | Initial creation | Phase planning |
