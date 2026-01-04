# S&S Wolf Sheds - Phase 3 Opportunity Matrix

**Created:** January 3, 2026
**Phase:** 3 of 4 - Intelligence & Operations
**Investment:** TBD (estimate $5,000-$10,000)
**Timeline:** 2-3 weeks (Month 3)
**Trigger:** Phase 2 complete, QR system generating data
**Framework:** Liam Ottley 3-Step AI Audit (adapted for implementation)
**Source:** [PRD-lot-assistant.md](../docs-workbook1/PRD-lot-assistant.md)

---

## Executive Summary

Phase 3 transforms raw data into actionable intelligence and solves the "last-mile" delivery problem. This phase also introduces the Dealer Accountability App to support multi-location expansion (Kayenta hub).

**Phase 1 Delivered:** ROI baseline, website fixes, database foundation
**Phase 2 Delivered:** QR capture system, pricing configurator, CRM pipeline
**Phase 3 Delivers:** Financial dashboards, delivery intelligence, accountability system

---

## Liam Ottley Framework Alignment

This phase maps to **Step 3: Present & Close** of Liam's 3-Step AI Audit Framework, demonstrating clear ROI and expanding operational intelligence.

| Liam's Framework | Our Implementation | Status |
|------------------|-------------------|--------|
| Ops Canvas (3 Engines) | All 3 engines now covered | ✅ Added |
| Opportunity Matrix (2x2) | Impact vs Effort scoring | ✅ Aligned |
| 4 Quadrants | Quick Wins + Big Swings | ✅ Aligned |
| ROI Money Slide | Full ROI breakdown below | ✅ Planned |
| Validation Workshop | Post-Phase 3 review | ✅ Planned |

---

## 3 Engines Mapping (Ops Canvas)

| Engine | Description | Phase 3 Opportunities |
|--------|-------------|----------------------|
| **ACQUISITION** | How they find and sign customers | (Covered in Phase 1-2) |
| **DELIVERY** | How they deliver product/service | P3-DELIVERY (Delivery Intel), P3-ACCOUNT (Accountability) |
| **SUPPORT** | Customer questions and post-sale | P3-DASHBOARD (Analytics), P3-ANALYTICS (Traffic) |

### Phase 3 Engine Focus: DELIVERY (Primary) + SUPPORT (Emerging)

```
┌─────────────────────────────────────────────────────────────────┐
│                     DELIVERY ENGINE                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   Customer   │───►│   Driver     │───►│   Delivery   │      │
│  │   Profile    │    │   Access     │    │   Complete   │      │
│  │  P3-DELIVERY │    │  P3-DELIVERY │    │              │      │
│  │  🟡 Quality  │    │  🟡 Info Gap │    │              │      │
│  │  ★ PRIORITY  │    │              │    │              │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐                          │
│  │  Checklist   │───►│   Deposit    │                          │
│  │  Compliance  │    │   Tracking   │                          │
│  │  P3-ACCOUNT  │    │  P3-ACCOUNT  │                          │
│  │  🟡 Quality  │    │  🟡 Cash Gap │                          │
│  └──────────────┘    └──────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     SUPPORT ENGINE                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │  Financial   │───►│   Marketing  │───►│   Traffic    │      │
│  │   KPIs       │    │   ROI        │    │   Analysis   │      │
│  │ P3-DASHBOARD │    │ P3-DASHBOARD │    │ P3-ANALYTICS │      │
│  │  🟡 Blind    │    │  🟡 Guess    │    │  🟡 Unknown  │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘

🟡 = Time Sink, Quality Risk, or Knowledge Gap (AI/Automation Opportunity)
★ = Priority Deliverable
```

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
**Quadrant:** ⭐ Quick Win (Medium Effort, High Impact)
**Engine:** DELIVERY

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
**Quadrant:** ⭐ Quick Win (Low-Medium Effort, High Impact)
**Engine:** SUPPORT

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
**Quadrant:** 🚀 Big Swing (Medium-High Effort, High Impact)
**Engine:** DELIVERY

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

### P3-ANALYTICS: Traffic & Conversion Analytics

**Status:** ★★★☆☆ OPTIONAL (if budget allows)
**Quadrant:** 🤔 Nice-to-Have (Medium Effort, Medium Impact)
**Engine:** SUPPORT

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

| ID | Opportunity | Quadrant | Engine | Impact | Effort | Week |
|----|-------------|----------|--------|--------|--------|------|
| **P3-DELIVERY** | Delivery Intelligence | ⭐ Quick Win | DELIVERY | ★★★★★ | MED | 1 |
| **P3-DASHBOARD** | Financial Dashboard | ⭐ Quick Win | SUPPORT | ★★★★☆ | LOW-MED | 1-2 |
| **P3-ACCOUNT** | Accountability App | 🚀 Big Swing | DELIVERY | ★★★★★ | MED-HIGH | 2 |
| P3-ANALYTICS | Traffic Counting | 🤔 Nice-to-Have | SUPPORT | ★★★☆☆ | MED | Optional |

**Phase 3 Mix:** 2 Quick Wins + 1 Big Swing + 1 Nice-to-Have

**Total Phase 3 Investment:** $5,000-$10,000 (TBD based on accountability app scope)
**Timeline:** 2-3 weeks

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

### Week 2: Accountability App

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| App architecture design | Developer | 1 | ⬜ |
| Rep login system | Developer | 1-2 | ⬜ |
| Daily checklist UI | Developer | 2-3 | ⬜ |
| Photo upload system | Developer | 3 | ⬜ |
| Deposit tracking | Developer | 3-4 | ⬜ |
| Manager dashboard | Developer | 4 | ⬜ |
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

## ROI Justification (Liam Ottley Method)

### Direct Savings (Time × Rate)

| Solution | Weekly Hours Saved | Hourly Rate | Annual Savings |
|----------|-------------------|-------------|----------------|
| P3-DELIVERY (Delivery Intel) | 4 hrs | $40 | $8,320 |
| P3-DASHBOARD (KPI Analytics) | 3 hrs | $40 | $6,240 |
| P3-ACCOUNT (Accountability) | 8 hrs* | $40 | $16,640 |
| **TOTAL** | **15 hrs/week** | - | **$31,200** |

*Sandra no longer driving to check on lots daily

### Revenue Uplift (Liam's 50% Rule)

> "50% of time saved goes directly to revenue-generating activities"

| Solution | Time Saved | Revenue Time (50%) | Value/Hour | Annual Uplift |
|----------|-----------|-------------------|------------|---------------|
| P3-DELIVERY (No failed deliveries) | 4 hrs/wk | 2 hrs | $500/redeliv | $52,000* |
| P3-DASHBOARD (Optimize marketing) | 3 hrs/wk | 1.5 hrs | 10% better ROAS | $36,000** |
| P3-ACCOUNT (Scale to Kayenta) | 8 hrs/wk | 4 hrs | $500/sale | $104,000*** |
| **TOTAL** | - | - | - | **$192,000** |

*Assumes 2 failed deliveries/month avoided @ $250 each + time cost
**Assumes $30K/month ad spend with 10% improvement
***Kayenta expansion enabled = additional lot revenue

### Phase 3 ROI Summary (Money Slide Preview)

| Solution | Investment | Direct Savings | Revenue Uplift | Total Value | ROI |
|----------|-----------|----------------|----------------|-------------|-----|
| Delivery Intelligence | $2,000 | $8,320 | $52,000 | $60,320 | 2,916% |
| Financial Dashboard | $1,500 | $6,240 | $36,000 | $42,240 | 2,716% |
| Accountability App | $4,000 | $16,640 | $104,000 | $120,640 | 2,916% |
| Traffic Analytics | $2,500 | - | TBD | TBD | Optional |
| **TOTAL** | **$7,500** | **$31,200** | **$192,000** | **$223,200** | **2,876%** |

---

## Validation Workshop (End of Phase 3)

Before moving to Phase 4 (Platform Migration), conduct a comprehensive Validation Workshop.

### Workshop Agenda (45-60 min)

| Topic | Questions | Goal |
|-------|-----------|------|
| **Delivery System** | "Has Scott adopted the driver links? Any delivery failures since?" | Confirm adoption |
| **Dashboard Review** | "Are the KPIs accurate? What decisions have you made using them?" | Validate utility |
| **Accountability App** | "How is rep compliance? Ready to deploy at Kayenta?" | Confirm expansion readiness |
| **ROI Check** | "Do these savings/uplift numbers match your experience?" | Validate ROI claims |

### Critical Validation Questions

- [ ] "Is the delivery failure rate measurably lower?"
- [ ] "Can you see marketing ROI clearly in the dashboard?"
- [ ] "Are reps completing checklists without resistance?"
- [ ] "Is Sandra's lot-checking time reduced as expected?"
- [ ] "Are you confident enough to expand to Kayenta with these systems?"

### Workshop Outputs

1. Phase 3 completion confirmed
2. Kayenta expansion greenlight
3. Validated ROI numbers for Phase 4 proposal
4. Any quick fixes before Phase 4
5. Refined Phase 4 priorities

---

## Related Documents

- [Phase 1 Opportunity Matrix](./phase-1-opportunity-matrix.md)
- [Phase 2 Opportunity Matrix](./phase-2-opportunity-matrix.md)
- [Phase 4 Opportunity Matrix](./phase-4-opportunity-matrix.md)
- [Main PRD](../docs-workbook1/PRD-lot-assistant.md)
- [Dec 30 Meeting Summary](../meetings/2025-12-30-expansion-strategy/summary.md)

---

**Last Updated:** January 3, 2026
**Status:** Ready for Phase 2 completion
**Next Action:** Complete Phase 2 → Begin Phase 3
