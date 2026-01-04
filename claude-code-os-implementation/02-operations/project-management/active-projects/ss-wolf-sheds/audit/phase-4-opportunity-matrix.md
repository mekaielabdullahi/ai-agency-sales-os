# S&S Wolf Sheds - Phase 4 Opportunity Matrix

**Created:** January 3, 2026
**Phase:** 4 of 4 - Platform Migration & Scale
**Investment:** TBD (estimate $7,500-$15,000)
**Timeline:** 3-4 weeks (Month 4+)
**Trigger:** Phase 3 complete, Kayenta expansion operational, all systems stable
**Framework:** Liam Ottley 3-Step AI Audit (adapted for implementation)
**Source:** [PRD-lot-assistant.md](../docs-workbook1/PRD-lot-assistant.md)

---

## Executive Summary

Phase 4 transforms S&S Wolf Sheds from a single-business solution into a scalable platform. This phase migrates all systems to Firebase, adds intelligent automation (geofencing), and packages the solution for the broader Graceland dealer network.

**Phase 1 Delivered:** ROI baseline, website fixes, database foundation
**Phase 2 Delivered:** QR capture system, pricing configurator, CRM pipeline
**Phase 3 Delivered:** Financial dashboards, delivery intelligence, accountability system
**Phase 4 Delivers:** Full cloud migration, intelligent automation, dealer platform

---

## Liam Ottley Framework Alignment

Phase 4 represents the **Transformation & Scale** stage - moving from client implementation to platform creation.

| Liam's Framework | Our Implementation | Status |
|------------------|-------------------|--------|
| Ops Canvas (3 Engines) | All engines optimized, new platform engine | ✅ Added |
| Opportunity Matrix (2x2) | All High Impact / High Effort (Big Swings) | ✅ Aligned |
| 4 Quadrants | Big Swings for transformation | ✅ Aligned |
| ROI Money Slide | Platform ROI + recurring revenue | ✅ Planned |
| Final Presentation | Complete project summary | ✅ Planned |

---

## 3 Engines Mapping (Ops Canvas)

| Engine | Description | Phase 4 Opportunities |
|--------|-------------|----------------------|
| **ACQUISITION** | How they find and sign customers | P4-GEOFENCE (Automated follow-up) |
| **DELIVERY** | How they deliver product/service | P4-FIREBASE (Platform foundation) |
| **SUPPORT** | Customer questions and post-sale | P4-PLATFORM (Multi-tenant support) |
| **PLATFORM** | New engine: Scalable dealer network | P4-PLATFORM, P4-EXPAND |

### Phase 4 Engine Focus: PLATFORM (New Engine)

```
┌─────────────────────────────────────────────────────────────────┐
│                     PLATFORM ENGINE (NEW)                       │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   Firebase   │───►│ Multi-Tenant │───►│   Dealer     │      │
│  │   Migration  │    │   Platform   │    │   Network    │      │
│  │  P4-FIREBASE │    │  P4-PLATFORM │    │  P4-EXPAND   │      │
│  │  🚀 FOUNDATION│    │  🚀 TRANSFORM│    │  🚀 SCALE    │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              INTELLIGENT AUTOMATION LAYER                       │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │  Geofence    │───►│   Trigger    │───►│   Nurture    │      │
│  │  Detection   │    │   Logic      │    │   Sequence   │      │
│  │ P4-GEOFENCE  │    │              │    │              │      │
│  │  🚀 AUTOMATE │    │              │    │              │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘

🚀 = Big Swing (High Effort, High Impact, Transformational)
```

---

## PRD Mapping - Complete

| PRD Component | Phase | Status |
|---------------|-------|--------|
| Sheet 1: Master Shed Data | Phase 1 | ✅ Complete |
| Sheet 7: CODB Calculator | Phase 1 | ✅ Complete |
| Sheet 3: Optional Features | Phase 2 | ✅ Complete |
| Sheet 2: Pricing Lookup | Phase 2 | ✅ Complete |
| Sheet 4: CRM Pipeline | Phase 2 | ✅ Complete |
| Sheet 5: Customer Profile & Delivery | Phase 3 | ✅ Complete |
| Sheet 6: Financial Dashboard | Phase 3 | ✅ Complete |
| Dealer Accountability App | Phase 3 | ✅ Complete |
| **Firebase Full Migration** | **Phase 4** | ⬜ This Phase |
| **Geofence Triggers** | **Phase 4** | ⬜ This Phase |
| **Graceland Platform** | **Phase 4** | ⬜ This Phase |

---

## Impact vs Effort Matrix

```
                          IMPACT
                    LOW         HIGH
              ┌───────────┬───────────┐
         LOW  │           │           │
              │           │           │
    EFFORT    │           │           │
              │           │           │
              ├───────────┼───────────┤
              │           │ P4-FIRE   │
         HIGH │           │ P4-GEO    │
              │           │ P4-PLAT   │
              │           │  ★★★★★   │
              └───────────┴───────────┘
```

**All Phase 4 opportunities are HIGH IMPACT / HIGH EFFORT.** This is the transformation phase.

---

## Phase 4 Opportunities

### P4-FIREBASE: Full Firebase Migration

**Status:** ★★★★★ PHASE 4 FOUNDATION
**Quadrant:** 🚀 Big Swing (High Effort, High Impact)
**Engine:** DELIVERY → PLATFORM

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Current systems spread across Google Sheets, temporary databases; no unified API; scalability limits |
| **Solution** | Complete migration to Firebase/Firestore with proper collections, security rules, and API endpoints |
| **Impact** | HIGH - Enables real-time sync, mobile apps, third-party integrations, multi-location scale |
| **Effort** | HIGH - 2 weeks |
| **Investment** | Part of Phase 4 |
| **Dependencies** | All Phase 1-3 data structures finalized |
| **IP Risk** | MEDIUM - Core business logic consolidated |
| **Timeline** | Week 1-2 |

#### Migration Architecture

| Collection | Source | Documents | Purpose |
|------------|--------|-----------|---------|
| `products` | Sheet 1 | All shed models | Inventory database |
| `options` | Sheet 3 | All add-ons | Configurator options |
| `leads` | Sheet 4 | All CRM leads | Sales pipeline |
| `customers` | Sheet 5 | Customer profiles | Delivery intelligence |
| `financials` | Sheet 6 + 7 | KPIs + CODB | Business analytics |
| `scans` | QR System | Scan events | Attribution tracking |
| `checklists` | Accountability | Daily tasks | Operations compliance |
| `users` | New | Staff accounts | Auth + permissions |

#### Security Model

```
Firebase Security Rules:
├── Public Read: products, options (pricing)
├── Authenticated Write: leads, scans, checklists
├── Role-Based: customers (sales only)
├── Admin Only: financials, users
└── Owner Only: CODB formulas, profit margins
```

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Firestore Collections | All 8 collections migrated | ⬜ Pending |
| Security Rules | Role-based access control | ⬜ Pending |
| Cloud Functions | Backend business logic | ⬜ Pending |
| API Endpoints | REST API for integrations | ⬜ Pending |
| Data Validation | Input sanitization, type checking | ⬜ Pending |
| Backup System | Automated daily backups | ⬜ Pending |

#### Success Metrics

- [ ] All data migrated to Firestore
- [ ] Security rules tested and deployed
- [ ] API endpoints documented
- [ ] Legacy systems decommissioned
- [ ] Performance benchmarks met (< 200ms queries)

---

### P4-GEOFENCE: Intelligent Geofence Triggers

**Status:** ★★★★★ WEEK 2-3 (Automation Layer)
**Quadrant:** 🚀 Big Swing (High Effort, High Impact)
**Engine:** ACQUISITION (Automated)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No follow-up with lot visitors who leave without engaging; missed sales opportunities |
| **Solution** | Geofence-triggered automated follow-up when customer leaves lot without converting |
| **Impact** | HIGH - Recover lost leads, automated nurturing, competitive differentiator |
| **Effort** | HIGH - 1-2 weeks |
| **Investment** | Part of Phase 4 |
| **Dependencies** | Firebase migration, customer opt-in mechanism, SMS/email automation |
| **IP Risk** | HIGH - Proprietary automation logic |
| **Timeline** | Week 2-3 |

#### How It Works

```
Customer arrives at lot →
    → Scans QR code (opt-in to notifications)
    → System tracks session
    → If customer leaves without purchase:
        → Geofence detects departure
        → Wait 30 minutes (cooling period)
        → Trigger personalized follow-up
        → "Thanks for visiting! Any questions about the [shed they scanned]?"
```

#### Trigger Conditions

| Condition | Action | Timing |
|-----------|--------|--------|
| QR scan + departure | SMS follow-up | 30 min after |
| Multiple scans + no contact | "Comparison" email | 1 hour after |
| Quote requested + no reply | Follow-up SMS | 24 hours after |
| Visited 2+ times | Priority alert to sales | Immediate |
| Won deal + delivery pending | Delivery updates | As status changes |

#### Privacy & Compliance

| Requirement | Implementation |
|-------------|----------------|
| Opt-in | Clear consent during QR scan |
| Opt-out | One-tap unsubscribe |
| Data retention | 90-day active, then archive |
| TCPA compliance | Proper SMS consent language |
| Location data | Never stored, only triggers |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Geofence Setup | Define boundaries for 3 lots | ⬜ Pending |
| Trigger Logic | Cloud Functions for events | ⬜ Pending |
| SMS Integration | Twilio or similar | ⬜ Pending |
| Email Automation | Follow-up sequences | ⬜ Pending |
| Opt-in Flow | Consent collection | ⬜ Pending |
| Analytics | Trigger → conversion tracking | ⬜ Pending |

#### Success Metrics

- [ ] Geofences active at all lots
- [ ] Automated follow-ups sending
- [ ] Opt-in rate > 30% of QR scanners
- [ ] Follow-up → conversion rate measurable
- [ ] Zero privacy complaints

---

### P4-PLATFORM: Graceland Dealer Network Platform

**Status:** ★★★★☆ WEEK 3-4 (Scale Strategy)
**Quadrant:** 🚀 Big Swing (High Effort, High Impact)
**Engine:** PLATFORM

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | S&S solution is custom-built; no way to offer same value to other Graceland dealers |
| **Solution** | Multi-tenant platform with white-label capability for dealer network |
| **Impact** | HIGH - New revenue stream, network effect, competitive moat |
| **Effort** | HIGH - 2 weeks for MVP |
| **Investment** | Part of Phase 4 (may require additional investment) |
| **Dependencies** | Firebase migration complete, S&S systems proven |
| **IP Risk** | VERY HIGH - Core platform IP |
| **Timeline** | Week 3-4 |

#### Platform Architecture

```
Graceland Dealer Platform
├── Tenant System
│   ├── Dealer onboarding
│   ├── Custom branding
│   └── Isolated data
├── Shared Services
│   ├── Product catalog (Graceland models)
│   ├── Pricing engine
│   └── Analytics framework
├── Dealer-Specific
│   ├── Local inventory
│   ├── Staff accounts
│   └── Customer data
└── Admin Portal
    ├── Network overview
    ├── Performance comparison
    └── Best practice sharing
```

#### Multi-Tenant Features

| Feature | Description |
|---------|-------------|
| Dealer Isolation | Each dealer's data completely separate |
| Shared Catalog | Graceland product database shared |
| Custom Branding | Each dealer's logo, colors, domain |
| Role Templates | Standard roles (Owner, Manager, Sales, Driver) |
| Pricing Flexibility | Each dealer sets own margins |
| Network Analytics | Anonymized benchmarking |

#### Revenue Model Options

| Model | Description |
|-------|-------------|
| SaaS Monthly | $500-1,500/month per dealer |
| Revenue Share | 1-2% of platform-attributed sales |
| Setup Fee | $5,000-10,000 onboarding |
| Hybrid | Setup + reduced monthly |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Multi-Tenant Architecture | Isolated dealer environments | ⬜ Pending |
| Dealer Onboarding Flow | Self-service or guided setup | ⬜ Pending |
| White-Label Config | Branding customization | ⬜ Pending |
| Admin Dashboard | Network management | ⬜ Pending |
| Billing System | Subscription management | ⬜ Pending |
| Documentation | Dealer user guides | ⬜ Pending |

#### Success Metrics

- [ ] Platform architecture documented
- [ ] First external dealer onboarded (pilot)
- [ ] White-label branding working
- [ ] Billing system functional
- [ ] S&S operating as "flagship" tenant

---

### P4-EXPAND: Multi-Location Scaling Support

**Status:** ★★★☆☆ OPTIONAL (if Kayenta successful)
**Quadrant:** 🤔 Nice-to-Have (Medium Effort, Medium Impact)
**Engine:** PLATFORM

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Kayenta expansion needs full system support; future lots need repeatable setup |
| **Solution** | Location management system with one-click new lot provisioning |
| **Impact** | MEDIUM-HIGH - Enables rapid expansion |
| **Effort** | MEDIUM - 1 week |
| **Investment** | Part of Phase 4 |
| **Dependencies** | Firebase migration, accountability app |
| **IP Risk** | MEDIUM - Operational methodology |
| **Timeline** | If budget allows |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Location Manager | Add/edit lot configurations | ⬜ Optional |
| Staff Assignment | Assign reps to locations | ⬜ Optional |
| Inventory Routing | Lot-specific inventory | ⬜ Optional |
| Performance Comparison | Lot vs lot analytics | ⬜ Optional |

---

## Phase 4 Consolidated Summary

| ID | Opportunity | Quadrant | Engine | Impact | Effort | Week |
|----|-------------|----------|--------|--------|--------|------|
| **P4-FIREBASE** | Firebase Migration | 🚀 Big Swing | PLATFORM | ★★★★★ | HIGH | 1-2 |
| **P4-GEOFENCE** | Geofence Triggers | 🚀 Big Swing | ACQUISITION | ★★★★★ | HIGH | 2-3 |
| **P4-PLATFORM** | Dealer Platform | 🚀 Big Swing | PLATFORM | ★★★★☆ | HIGH | 3-4 |
| P4-EXPAND | Multi-Location | 🤔 Nice-to-Have | PLATFORM | ★★★☆☆ | MED | Optional |

**Phase 4 = Transformation Phase:** 3 Big Swings + 1 Nice-to-Have

**Total Phase 4 Investment:** $7,500-$15,000 (TBD based on platform scope)
**Timeline:** 3-4 weeks

---

## Implementation Schedule

### Week 1-2: Firebase Migration

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Firestore collection design | Developer | 1 | ⬜ |
| Security rules draft | Developer | 1-2 | ⬜ |
| Products migration | Developer | 2-3 | ⬜ |
| Options migration | Developer | 3 | ⬜ |
| Leads/CRM migration | Developer | 3-4 | ⬜ |
| Customer profiles migration | Developer | 4-5 | ⬜ |
| Financial data migration | Developer | 5-6 | ⬜ |
| Cloud Functions setup | Developer | 6-7 | ⬜ |
| API endpoints | Developer | 7-8 | ⬜ |
| Testing + validation | All | 8-10 | ⬜ |

### Week 2-3: Geofence System

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Geofence boundary definition | Developer | 1 | ⬜ |
| Trigger logic design | Developer | 1-2 | ⬜ |
| SMS provider integration | Developer | 2-3 | ⬜ |
| Email automation setup | Developer | 3-4 | ⬜ |
| Opt-in flow implementation | Developer | 4-5 | ⬜ |
| Privacy compliance review | AriseGroup | 5 | ⬜ |
| Testing | All | 5-7 | ⬜ |

### Week 3-4: Platform Foundation

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Multi-tenant architecture | Developer | 1-2 | ⬜ |
| Dealer isolation implementation | Developer | 2-4 | ⬜ |
| White-label configuration | Developer | 4-5 | ⬜ |
| Admin dashboard | Developer | 5-6 | ⬜ |
| Documentation | AriseGroup | 6-7 | ⬜ |
| Pilot dealer onboarding | All | 7-10 | ⬜ |

---

## Dependencies Map

```
P3-ALL (Phase 3)
    │
    └──► P4-FIREBASE (Week 1-2) - All data structures must be finalized
            │
            ├──► P4-GEOFENCE (Week 2-3) - Requires Firebase for triggers
            │
            └──► P4-PLATFORM (Week 3-4) - Requires migration complete

P3-ACCOUNT (Phase 3)
    │
    └──► P4-EXPAND (Optional) - Accountability system enables scaling

Kayenta Expansion
    │
    └──► P4-PLATFORM - Success validates platform model
```

---

## Risk Assessment

| Opportunity | Risk Level | Key Risk | Mitigation |
|-------------|------------|----------|------------|
| P4-FIREBASE | MEDIUM | Data loss during migration | Comprehensive backups, staged migration |
| P4-GEOFENCE | HIGH | Privacy concerns, opt-in rates | Clear consent, easy opt-out, TCPA compliance |
| P4-PLATFORM | HIGH | Complexity, scope creep | MVP first, iterate based on pilot |
| P4-EXPAND | LOW | Premature scaling | Only after Kayenta success |

### Platform-Specific Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Multi-tenant security breach | CRITICAL | Strict isolation, security audit |
| Feature parity expectations | HIGH | Clear MVP scope, roadmap |
| Support burden | MEDIUM | Self-service docs, tiered support |
| Pricing pushback | MEDIUM | Value-based pricing, ROI calculator |

---

## Success Criteria

### Phase 4 Complete When:

- [ ] All data migrated to Firebase
- [ ] Security rules deployed and tested
- [ ] Geofence triggers operational at all lots
- [ ] Opt-in flow working with compliance
- [ ] Platform MVP deployed
- [ ] First external dealer onboarded (pilot)
- [ ] S&S operating on platform (flagship)

### Full Project Complete When:

- [ ] All 4 phases delivered
- [ ] S&S Wolf Sheds fully operational on platform
- [ ] Measurable ROI achieved (validated by ROI Calculator)
- [ ] Kayenta expansion successful
- [ ] Platform ready for Graceland network rollout

---

## Investment Summary (Full Project)

| Phase | Investment | Focus |
|-------|------------|-------|
| Phase 1 | $5,000 | Foundation (ROI, Website, Database) |
| Phase 2 | $5,000 | Lead Capture (QR, Configurator, CRM) |
| Phase 3 | $5,000-10,000 | Intelligence (Dashboards, Accountability) |
| Phase 4 | $7,500-15,000 | Scale (Firebase, Geofence, Platform) |
| **TOTAL** | **$22,500-35,000** | **Complete Solution** |

---

## ROI Justification (Liam Ottley Method)

### Direct Savings (Time × Rate)

| Solution | Weekly Hours Saved | Hourly Rate | Annual Savings |
|----------|-------------------|-------------|----------------|
| P4-FIREBASE (Unified API) | 6 hrs | $40 | $12,480 |
| P4-GEOFENCE (Auto follow-up) | 10 hrs | $40 | $20,800 |
| P4-PLATFORM (Admin efficiency) | 8 hrs | $40 | $16,640 |
| **TOTAL** | **24 hrs/week** | - | **$49,920** |

### Revenue Uplift (Liam's 50% Rule)

> "50% of time saved goes directly to revenue-generating activities"

| Solution | Impact Type | Calculation | Annual Uplift |
|----------|------------|-------------|---------------|
| P4-GEOFENCE (Recovered leads) | New revenue | 20 recovered/mo × $500 × 12 | $120,000 |
| P4-PLATFORM (New dealers) | Recurring | 5 dealers × $1,000/mo × 12 | $60,000 |
| P4-EXPAND (Kayenta success) | Scale | 50% of S&S revenue on 2nd lot | $150,000* |
| **TOTAL** | - | - | **$330,000** |

*Conservative estimate of Kayenta producing 50% of Flagstaff volume

### Phase 4 ROI Summary (Money Slide Preview)

| Solution | Investment | Direct Savings | Revenue Uplift | Total Value | ROI |
|----------|-----------|----------------|----------------|-------------|-----|
| Firebase Migration | $3,500 | $12,480 | - | $12,480 | 257% |
| Geofence System | $4,000 | $20,800 | $120,000 | $140,800 | 3,420% |
| Dealer Platform | $5,000 | $16,640 | $60,000 | $76,640 | 1,433% |
| Multi-Location | $2,500 | - | $150,000 | $150,000 | 5,900% |
| **TOTAL** | **$15,000** | **$49,920** | **$330,000** | **$379,920** | **2,433%** |

---

## Full Project ROI Summary (Money Slide)

### Complete 4-Phase Investment Analysis

| Phase | Investment | Direct Savings | Revenue Uplift | Total Value |
|-------|-----------|----------------|----------------|-------------|
| Phase 1 (Foundation) | $5,000 | $26,080 | $146,250 | $172,330 |
| Phase 2 (Lead Capture) | $5,000 | $29,120 | $156,000 | $185,120 |
| Phase 3 (Intelligence) | $7,500 | $31,200 | $192,000 | $223,200 |
| Phase 4 (Platform) | $15,000 | $49,920 | $330,000 | $379,920 |
| **TOTAL PROJECT** | **$32,500** | **$136,320** | **$824,250** | **$960,570** |

### ROI Summary

```
Total Investment:      $32,500
Direct Cost Savings:   $136,320/year
Revenue Uplift:        $824,250/year
Total Annual Value:    $960,570

PROJECT ROI:           2,855%
PAYBACK PERIOD:        12 days
```

---

## Final Presentation (Complete Project)

When Phase 4 is complete, deliver a final presentation to Sandy/Chris covering the complete transformation.

### Presentation Outline (5 Slides - Liam's Method)

| Slide | Content |
|-------|---------|
| **1. Scope & Objectives** | What we set out to do, what we delivered |
| **2. Opportunity Matrix** | All opportunities across 4 phases, quadrant distribution |
| **3. Roadmap Summary** | Phase-by-phase journey, key milestones |
| **4. Deep Dive: Top 3** | QR System, Accountability App, Dealer Platform |
| **5. ROI Money Slide** | The table above - full investment/value breakdown |

### Key Talking Points

1. **Transformation Journey**: From spreadsheets → scalable platform
2. **ROI Reality Check**: "Do these numbers match your experience?"
3. **Platform Future**: Graceland network opportunity
4. **Ongoing Partnership**: Maintenance, support, expansion options

---

## Related Documents

- [Phase 1 Opportunity Matrix](./phase-1-opportunity-matrix.md)
- [Phase 2 Opportunity Matrix](./phase-2-opportunity-matrix.md)
- [Phase 3 Opportunity Matrix](./phase-3-opportunity-matrix.md)
- [Main PRD](../docs-workbook1/PRD-lot-assistant.md)
- [ROI Calculator](./roi-calculator.md)
- [Money Slide Template](./money-slide-template.md)

---

**Last Updated:** January 3, 2026
**Status:** Planning (awaiting Phase 3 completion)
**Next Action:** Complete Phase 3 → Begin Phase 4

