# S&S Wolf Sheds - Phase 2 Opportunity Matrix

**Created:** January 3, 2026
**Phase:** 2 of 4 - Core Workflow & Lead Capture
**Investment:** $5,000
**Timeline:** 2 weeks (Month 2)
**Trigger:** Phase 1 complete, second payment received
**Source:** [Phase 1 PRD](../docs-workbook1/PRD-phase-1-database-foundation.md) | [Main Opportunity Matrix](./opportunity-matrix.md)

---

## Executive Summary

Phase 2 builds on the Phase 1 foundation to implement active lead capture and sales workflow tools. The focus shifts from "understanding the business" (Phase 1) to "capturing and converting leads" (Phase 2).

**Phase 1 Delivered:** ROI baseline, website fixes, database foundation, lead qualification form
**Phase 2 Delivers:** On-lot capture system, pricing configurator, CRM pipeline, SOP generator tool

---

## Phase 1 → Phase 2 Handoff Requirements

Before starting Phase 2, confirm:

- [ ] All Phase 1 deliverables complete
- [ ] ROI Calculator populated with validated data
- [ ] Website fixes live and working
- [ ] Lead qualification form capturing and qualifying leads
- [ ] Database foundation in place
- [ ] Initial SOPs created from stakeholder interviews
- [ ] Second payment ($5,000) received
- [ ] Sandy/Chris approve Phase 2 scope

---

## Impact vs Effort Matrix

```
                          IMPACT
                    LOW         HIGH
              ┌───────────┬───────────┐
         LOW  │           │  P2-OPT   │
              │           │  P2-CRM   │
    EFFORT    │           │  ★★★★★   │
              │           │           │
              ├───────────┼───────────┤
              │           │  P2-QR    │
         MED  │           │  P2-PRICE │
              │           │  ★★★★★   │
              └───────────┴───────────┘
```

**All Phase 2 opportunities are HIGH IMPACT.** QR System is the anchor deliverable.

---

## Phase 2 Opportunities

### P2-QR: QR/Slot On-Lot Capture System

**Status:** ★★★★★ PHASE 2 ANCHOR

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Single attendant cannot capture multiple simultaneous visitors; prospects leave without contact captured; 0% capture rate for browsers |
| **Solution** | 20 fixed slot-based QR codes per lot, backend maps slot to current inventory, self-service scan + intake form |
| **Impact** | HIGH - Capture leads from ALL visitors, not just those attendant engages; enable follow-up for browsers |
| **Effort** | MEDIUM - 1-2 weeks for core implementation |
| **Investment** | Part of Phase 2 ($5,000) |
| **Dependencies** | Phase 1 complete (database, form infrastructure) |
| **IP Risk** | MEDIUM - Proprietary capture methodology |
| **Timeline** | Week 1-2 |

#### How It Works

```
Customer walks lot → Scans QR on shed →
    → QR links to slot number (not model ID)
    → Backend maps slot to current inventory
    → Customer sees shed details + intake form
    → Scan event logged (timestamp, slot, session)
    → Lead captured even if customer leaves
```

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| QR Code Generation | 20 codes per lot (60 total for 3 lots) | ⬜ Pending |
| Slot Mapping Backend | Firestore collection mapping slots → inventory | ⬜ Pending |
| Scan Event Tracking | Log all scans with timestamp, slot, session ID | ⬜ Pending |
| Mobile Landing Page | Shed details + intake form per slot | ⬜ Pending |
| Weather-Resistant QR Signage | Physical QR codes for lot deployment | ⬜ Pending |
| Admin Dashboard | View scans, update slot mappings | ⬜ Pending |

#### Success Metrics

- [ ] QR codes deployed at all 3 lots
- [ ] First 50 scans captured
- [ ] Scan-to-submission rate > 20%
- [ ] Lead-to-building tracking working

---

### P2-PRICE: Pricing Lookup Tool (Configurator)

**Status:** ★★★★★ WEEK 2

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Manual price lookups; inconsistent quoting; no self-service for customers |
| **Solution** | Web-based configurator pulling from Master Shed Data (Sheet 1) + Optional Features (Sheet 3) |
| **Impact** | HIGH - Faster quotes, consistent pricing, customer self-service |
| **Effort** | MEDIUM - 1 week |
| **Investment** | Part of Phase 2 ($5,000) |
| **Dependencies** | Sheet 1 (Master Data) + Sheet 3 (Options) complete |
| **IP Risk** | LOW - Standard configurator pattern |
| **Timeline** | Week 2 |

#### How It Works

```
User selects Model ID →
    → VLOOKUP pulls base price from Sheet 1
    → User selects options from Sheet 3
    → Options prices added to base
    → Total Quote Price calculated
    → Quote saved/emailed to customer
```

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Sheet 3: Optional Features Data | Add-on pricing database | ⬜ Pending |
| Model Selection UI | Dropdown/search for shed models | ⬜ Pending |
| Options Selection | Checkboxes for upgrades (metal roof, windows, etc.) | ⬜ Pending |
| Price Calculator | Real-time total with breakdown | ⬜ Pending |
| Quote Output | PDF/email quote generation | ⬜ Pending |

#### Success Metrics

- [ ] All models and options loaded
- [ ] Quote generation < 30 seconds
- [ ] Staff using for customer quotes
- [ ] Customer self-service working

---

### P2-CRM: CRM & Sales Pipeline

**Status:** ★★★★☆ WEEK 2

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Leads captured but not tracked through pipeline; no visibility into deal stages; inconsistent follow-up |
| **Solution** | Lightweight CRM with pipeline stages, lead assignment, follow-up tracking |
| **Impact** | HIGH - Convert more leads, track performance, enable accountability |
| **Effort** | LOW-MEDIUM - 1 week (can use existing Zoho or build lightweight) |
| **Investment** | Part of Phase 2 ($5,000) |
| **Dependencies** | Onboarding form feeding leads, QR system feeding scans |
| **IP Risk** | LOW - Standard CRM pattern |
| **Timeline** | Week 2 |

#### Pipeline Stages

| Stage | Description | Actions |
|-------|-------------|---------|
| **New Lead** | Just captured via form/QR | Auto-assign, notify sales |
| **Contacted** | Initial outreach made | Log contact attempt |
| **Qualified** | Confirmed interest/budget | Schedule lot visit |
| **Quote Sent** | Pricing provided | Follow-up cadence |
| **Negotiating** | Discussing terms | Track objections |
| **Won** | Deal closed | Trigger delivery prep |
| **Lost** | Deal lost | Log reason, archive |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Sheet 4: CRM Pipeline | Lead tracking with stages | ⬜ Pending |
| Data Validation | Dropdowns for Stage, Source | ⬜ Pending |
| Lead Assignment | Route to lot-specific sales rep | ⬜ Pending |
| Follow-up Reminders | Automated task creation | ⬜ Pending |
| Pipeline Dashboard | Visual funnel view | ⬜ Pending |

#### Success Metrics

- [ ] All leads flowing into CRM
- [ ] Pipeline stages being used
- [ ] Follow-up rate improved
- [ ] Conversion rate trackable

---

### P2-OPT: Optional Features Data (Sheet 3)

**Status:** ★★★★★ WEEK 1 (Foundation for Pricing Tool)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No structured database of upgrade options and pricing |
| **Solution** | Firestore collection of all add-ons with prices |
| **Impact** | HIGH - Enables configurator, consistent upgrade pricing |
| **Effort** | LOW - Data entry + structure |
| **Investment** | Part of Phase 2 ($5,000) |
| **Dependencies** | Sheet 1 complete |
| **IP Risk** | LOW - Product catalog data |
| **Timeline** | Week 1 |

#### Data Structure

| Field | Description |
|-------|-------------|
| `option_id` | Unique identifier |
| `option_name` | Display name (e.g., "Metal Roof Upgrade") |
| `option_category` | Category (Roofing, Windows, Doors, Interior, etc.) |
| `option_price` | Price (pure number, no $) |
| `compatible_models` | Which models support this option |
| `description` | Customer-facing description |

#### Success Metrics

- [ ] All options catalogued
- [ ] Prices validated with Sandy
- [ ] Integrated with configurator

---

### P2-SOP: SOP Generator Tool

**Status:** ★★★★★ WEEK 2 (Recurring Revenue Opportunity)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Business can't scale without documented processes; Phase 1 created initial SOPs manually; no way to create/update SOPs independently |
| **Solution** | Client-owned SOP generator tool (Claude skill or custom solution) that allows them to create and maintain their own SOPs |
| **Impact** | HIGH - Enables business scaling, self-service process documentation, recurring support revenue |
| **Effort** | LOW-MEDIUM - 3-5 days |
| **Investment** | Part of Phase 2 ($5,000) |
| **Dependencies** | Initial SOPs from Phase 1 as templates |
| **IP Risk** | MEDIUM - Proprietary tool methodology |
| **Timeline** | Week 2 |

#### How It Works (from Jan 3 Meeting)

```
Client records daily tasks (voice/text) →
    → System processes input
    → Generates draft SOP
    → Client reviews/edits
    → SOP saved to database
    → Updates can be made anytime
```

#### Platform Options Discussed

| Platform | Pros | Cons |
|----------|------|------|
| Claude Desktop + Skills | Already available, powerful | Requires Claude subscription |
| ChatGPT Custom GPT | Client may already have | Less integration capability |
| Custom Solution | Full control | Higher development cost |

#### Recurring Revenue Insight

> "They're not gonna know how to iterate upon it. Like when they need to add another feature or function. They're not gonna know how to do that" - Trent (Jan 3 Meeting)

This creates ongoing support/enhancement opportunities.

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| SOP Generator Tool | Claude skill or custom implementation | ⬜ Pending |
| Template Library | Based on Phase 1 SOPs | ⬜ Pending |
| User Guide | How to use the generator | ⬜ Pending |
| Training Session | Walkthrough with client | ⬜ Pending |

#### Success Metrics

- [ ] Tool deployed and accessible to client
- [ ] Client successfully generates first SOP independently
- [ ] Template library populated with Phase 1 SOPs
- [ ] Training completed with key stakeholders

---

## Phase 2 Consolidated Summary

| ID | Opportunity | Impact | Effort | Week | Priority |
|----|-------------|--------|--------|------|----------|
| **P2-OPT** | Optional Features Data (Sheet 3) | ★★★★★ | LOW | 1 | #1 Foundation |
| **P2-QR** | QR/Slot On-Lot Capture System | ★★★★★ | MED | 1-2 | #2 ANCHOR |
| **P2-PRICE** | Pricing Lookup Tool (Configurator) | ★★★★★ | MED | 2 | #3 Tool |
| **P2-CRM** | CRM & Sales Pipeline | ★★★★☆ | LOW-MED | 2 | #4 Workflow |
| **P2-SOP** | SOP Generator Tool | ★★★★★ | LOW-MED | 2 | #5 Scale Enabler |

**Total Phase 2 Investment:** $5,000
**Timeline:** 2 weeks
**IP Risk:** LOW-MEDIUM
**Recurring Revenue:** SOP Generator creates ongoing support opportunities

---

## Implementation Schedule

### Week 1: Foundation & QR Build

```
Day 1:   Sheet 3 (Options) data entry
Day 1-2: QR code generation (60 codes)
Day 2-3: Slot mapping backend
Day 3-4: Mobile landing pages
Day 4-5: Scan tracking + testing
```

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Sheet 3 data structure | Developer | 1 | ⬜ |
| Options data entry | Sandy/Matthew | 1-2 | ⬜ |
| QR code generation | Developer | 1-2 | ⬜ |
| Slot → Inventory mapping | Developer | 2-3 | ⬜ |
| Mobile landing page | Developer | 3-4 | ⬜ |
| Scan event logging | Developer | 4 | ⬜ |
| QR signage production | AriseGroup | 4-5 | ⬜ |
| Testing | All | 5 | ⬜ |

### Week 2: Tools & Deployment

```
Day 1-2: Pricing configurator build
Day 2-3: CRM pipeline setup
Day 3:   SOP Generator tool setup
Day 3-4: Integration testing
Day 4:   QR deployment to lots
Day 5:   Training + handoff
```

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Configurator UI | Developer | 1-2 | ⬜ |
| Price calculation logic | Developer | 2 | ⬜ |
| Quote generation | Developer | 2-3 | ⬜ |
| CRM pipeline structure | Developer | 2-3 | ⬜ |
| Lead routing logic | Developer | 3 | ⬜ |
| SOP Generator tool setup | Developer | 3 | ⬜ |
| SOP template library | AriseGroup | 3-4 | ⬜ |
| Integration testing | All | 3-4 | ⬜ |
| QR deployment (3 lots) | Sandy/Team | 4 | ⬜ |
| Staff training (tools + SOP gen) | AriseGroup | 5 | ⬜ |
| Handoff | All | 5 | ⬜ |

---

## Dependencies Map

```
P2-OPT (Week 1)
    │
    └──► P2-PRICE (Week 2) - Options data enables configurator

P1-DB (Phase 1)
    │
    ├──► P2-QR (Week 1-2) - Database foundation for scan tracking
    │
    └──► P2-PRICE (Week 2) - Master data enables configurator

P1-FORM (Phase 1)
    │
    ├──► P2-QR (Week 1-2) - Form infrastructure for scan intake
    │
    └──► P2-CRM (Week 2) - Leads flow into CRM

P2-QR (Week 1-2)
    │
    └──► P2-CRM (Week 2) - Scans create leads in CRM
```

---

## Risk Assessment

| Opportunity | Risk Level | Key Risk | Mitigation |
|-------------|------------|----------|------------|
| P2-OPT | LOW | Incomplete options data | Work with Sandy to validate |
| P2-QR | MEDIUM | Low scan adoption | Prominent signage, staff training |
| P2-PRICE | LOW | Complex pricing rules | Start simple, iterate |
| P2-CRM | LOW | Adoption resistance | Involve team in design |

### QR-Specific Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Customers don't scan | No leads captured | Clear signage, incentive option |
| Weather damages QR codes | Codes unreadable | Weather-resistant materials |
| Slot mapping gets stale | Wrong shed info shown | Admin dashboard for updates |
| Cell service issues | Can't load page | Offline fallback with phone number |

---

## Success Criteria

### Phase 2 Complete When:

- [ ] QR codes deployed at all 3 lots
- [ ] First 50 scans captured and tracked
- [ ] Pricing configurator working
- [ ] CRM pipeline tracking leads
- [ ] Staff trained on new tools
- [ ] Measurable improvement in lead capture

### Phase 3 Trigger Metrics:

- [ ] 100+ leads captured via QR system
- [ ] Conversion improvement measurable
- [ ] Client ready for advanced features
- [ ] Kayenta expansion on track

---

## ROI Justification

**Phase 2 ROI Potential:**

| Improvement | Conservative Impact |
|-------------|---------------------|
| QR captures 20 additional leads/month | 20 × $5,000 × 25% = $25,000/month |
| Configurator speeds quotes by 50% | Time savings + faster close |
| CRM improves follow-up rate | 10% more conversions |

**If QR system captures just 10 additional leads that convert:**
```
10 leads × 25% close rate × $5,000 avg sale = $12,500/month
Annual: $150,000 additional revenue
ROI on $5,000 investment = 2,900%
```

---

## Deferred to Phase 3+

| ID | Opportunity | Reason Deferred |
|----|-------------|-----------------|
| SI-2 | Traffic Counting / Analytics | Requires hardware; focus on QR first |
| DEP-1 | AI Chatbot | May not be needed if QR capture works |
| DEP-2 | Paid Ads Resume | Capture first, then drive traffic |
| DEP-3 | Full Analytics Dashboard | Build after data flowing |
| OPSYS-1 | Dealer Accountability App | Parallel track; may be Phase 2.5 |

---

## Related Documents

- [Phase 1 Opportunity Matrix](./phase-1-opportunity-matrix.md)
- [Phase 1 PRD](../docs-workbook1/PRD-phase-1-database-foundation.md)
- [Main Opportunity Matrix](./opportunity-matrix.md)
- [ROI Calculator](./roi-calculator.md)

---

**Last Updated:** January 3, 2026
**Status:** Ready for Phase 1 completion
**Next Action:** Complete Phase 1 → Begin Phase 2

---

## Revision History

| Date | Version | Changes | Source |
|------|---------|---------|--------|
| Jan 3, 2026 | 1.1 | Added P2-SOP (SOP Generator Tool) as new deliverable; Updated P1 references to "Lead Qualification Form"; Added recurring revenue insight | Jan 3 Team Review Huddle |
| Jan 3, 2026 | 1.0 | Initial creation | Phase planning |
