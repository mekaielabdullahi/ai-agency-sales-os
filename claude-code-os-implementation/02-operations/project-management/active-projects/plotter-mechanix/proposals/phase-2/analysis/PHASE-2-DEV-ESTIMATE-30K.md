# Phase 2 Dev Estimate — $30K / 8 Weeks / 204h MVP

**Date:** February 18, 2026
**Prepared By:** Taylor (Scope & Timeline Builder Agent) + Matthew
**Dev Team:** Matthew Kerns, Trent Christopher
**Client:** Plotter Mechanix (Kelsey)

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Client Investment** | $30,000 |
| **MVP Hours** | 204h |
| **Effective Client Rate** | $147/hr |
| **Timeline** | 8 weeks |
| **Weekly Hours** | 25.5h/week (12.75h/dev) |
| **Internal Cost (@$50/hr)** | $10,200 |
| **Gross Margin** | $19,800 (66%) |

---

## Pricing Methodology

### Client Rate Model (Per PRD Framework)

| Layer | Rate | Purpose |
|-------|------|---------|
| Internal Dev Cost | $50/hr | What we pay devs |
| Client Rate | $140-175/hr | What client pays |
| **Blended Rate** | **$147/hr** | $30K ÷ 204h |
| **Markup** | **2.9x** | Covers PM, tools, profit |

### What the Markup Covers
- Project management & coordination
- Architecture & technical decisions
- Quality assurance & testing
- Tools & infrastructure (Quo, N8N, hosting)
- Stakeholder communication
- Risk buffer
- Profit margin

---

## Scope Summary: What's IN vs DEFERRED

### IN Scope ($30K MVP)

| Category | Hours | Investment | Notes |
|----------|-------|------------|-------|
| Foundation (M1) | 26h | $3,820 | Discovery, specs, audit |
| Core Systems (M2) | 132h | $19,400 | Holding Area, Quote, Contacts, KB |
| Go-Live (M3) | 26h | $3,820 | Deploy, training, support |
| Quick Wins | 20h | $2,940 | Voice Assistant, Quo-Jobber fixes |
| **TOTAL MVP** | **204h** | **~$30,000** | |

### DEFERRED to Phase 3

| Feature | Reason | Future Investment |
|---------|--------|-------------------|
| QuickBooks full sync | Enhancement | $1,750 |
| Capsule migration | Enhancement | $1,460 |
| Ply integration | Enhancement | $1,750 |
| ML improvements | Future | $2,340 |
| Advanced analytics | Future | $1,170 |

---

## Milestone 1: Foundation (Weeks 1-2) — $3,820

Discovery and planning work. Low dev risk.

| # | Task | Opt | Likely | Pess | Client Investment |
|---|------|-----|--------|------|-------------------|
| 1 | Workflow Documentation | 2h | 4h | 6h | $880 |
| 2 | Data Flow Diagram | 2h | 3h | 5h | $735 |
| 3 | Contact Audit Report | 4h | 6h | 10h | $1,470 |
| 4 | Technical Spec | 6h | 10h | 16h | — (included) |
| 5 | Demo Session | 2h | 3h | 4h | $590 |
| **M1 TOTAL** | **16h** | **26h** | **41h** | **$3,820** |

### M1 Deliverables
- Alyssa's daily workflow mapped minute-by-minute
- Visual data flow: Quo → Jobber → QuickBooks → Capsule
- Contact quality report: duplicate count, data issues
- Architecture blueprint for Phase 2 build
- Stakeholder demo and approval

---

## Milestone 2: Core Systems (Weeks 3-6) — $19,400

### Central Request Inbox (Holding Area) — 51h / $7,500

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Design UI/workflow | 2h | 4h | 6h | $880 |
| 2 | Outlook integration (MS Graph API) | 4h | 8h | 14h | $2,060 |
| 3 | Quo/SMS integration | 2h | 4h | 6h | $880 |
| 4 | Website leads integration | 1h | 2h | 3h | $440 |
| 5 | Build holding area UI | 6h | 10h | 16h | $2,350 |
| 6 | Routing logic | 2h | 4h | 6h | $880 |
| **Subtotal** | **17h** | **32h** | **51h** | **$7,500** |

**What Alyssa Gets:** Single screen showing all incoming requests from email, phone, website. One-click approve/reject. Auto-assign to right team member.

---

### Quote Workflow Automation (OPP-4) — 32h / $4,700

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Extend call summarization | 2h | 4h | 6h | $880 |
| 2 | Quo → Holding Area → Jobber flow | 4h | 8h | 12h | $1,765 |
| 3 | Deposit notification (QB webhook) | 2h | 3h | 5h | $735 |
| 4 | Flag in holding area | 1h | 2h | 3h | $440 |
| 5 | Second-call workflow | 2h | 4h | 6h | $880 |
| **Subtotal** | **11h** | **21h** | **32h** | **$4,700** |

**ROI Reference:**
- Annual Impact: $67,580 - $103,580
- ROI: 14x - 22x (based on $4,700 investment)
- Payback: ~2.5 weeks

---

### Contact Sync Engine (OPP-6) — 38h / $5,590

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Capsule export + cleanup | 3h | 6h | 10h | $1,470 |
| 2 | Jobber import | 4h | 8h | 14h | $2,060 |
| 3 | Duplicate merge rules | 3h | 6h | 10h | $1,470 |
| 4 | Team visibility setup | 1h | 2h | 4h | $590 |
| **Subtotal** | **11h** | **22h** | **38h** | **$5,590** |

**ROI Reference:**
- Annual Impact: $132,770 - $172,845
- ROI: 24x - 31x (based on $5,590 investment)
- Payback: ~2 weeks

**Note:** QuickBooks bi-directional sync deferred to Phase 3 to keep MVP scope.

---

### Sona AI Knowledge Base (OPP-5) — 11h / $1,620

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Doc upload + indexing | 2h | 4h | 6h | $880 |
| 2 | Voice/text search config | 2h | 3h | 5h | $735 |
| **Subtotal** | **4h** | **7h** | **11h** | **$1,620** |

**Note:** Training videos (28h) and Operations Runbook (12h) moved to M3 Go-Live.

---

## Milestone 3: Go-Live (Weeks 7-8) — $3,820

### Smart Request Form — 8h / $1,175

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Configure Jobber form | 1h | 2h | 3h | $440 |
| 2 | Embed on website | 1h | 2h | 3h | $440 |
| 3 | Auto-routing logic | 1h | 2h | 2h | $295 |
| **Subtotal** | **3h** | **6h** | **8h** | **$1,175** |

---

### Production Deployment — 10h / $1,470

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Connect to live systems | 2h | 4h | 6h | $880 |
| 2 | Monitoring setup | 2h | 3h | 4h | $590 |
| **Subtotal** | **4h** | **7h** | **10h** | **$1,470** |

---

### Support Buffer — 8h / $1,175

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Bug fixes, adjustments | 2h | 4h | 8h | $1,175 |
| **Subtotal** | **2h** | **4h** | **8h** | **$1,175** |

---

## Quick Wins (Week 3) — $2,940

### After Hours Voice Assistant — 12h / $1,765

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Quo after-hours config | 1h | 2h | 3h | $440 |
| 2 | Emergency escalation | 1h | 2h | 3h | $440 |
| 3 | Jobber appointment booking | 1h | 2h | 3h | $440 |
| 4 | Notification system | 1h | 2h | 3h | $440 |
| **Subtotal** | **4h** | **8h** | **12h** | **$1,765** |

**What Kelsey Gets:**
- 24/7 call answering
- Emergency calls routed to on-call
- Appointments booked in Jobber
- No more 2am interruptions

---

### Quo-Jobber Workflow Fixes — 8h / $1,175

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Data sync debugging | 1h | 2h | 3h | $440 |
| 2 | Field mapping improvements | 1h | 1h | 2h | $295 |
| 3 | Duplicate handling | 1h | 2h | 2h | $295 |
| 4 | Testing & validation | 0.5h | 1h | 1h | $145 |
| **Subtotal** | **3.5h** | **6h** | **8h** | **$1,175** |

---

## Training & Documentation (Included in M3) — $2,940

### Training Videos (5 core) — 12h / $1,765

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Script + record (5 videos) | 4h | 6h | 8h | $1,175 |
| 2 | Edit + upload | 2h | 3h | 4h | $590 |
| **Subtotal** | **6h** | **9h** | **12h** | **$1,765** |

**Note:** Full 15-video library moved to Phase 3. MVP includes 5 essential videos covering core workflows.

---

### Operations Runbook (Essential) — 8h / $1,175

| # | Task | Opt | Likely | Pess | Investment |
|---|------|-----|--------|------|------------|
| 1 | Document core workflows | 3h | 5h | 8h | $1,175 |
| **Subtotal** | **3h** | **5h** | **8h** | **$1,175** |

---

## Grand Total: MVP Scope

| Milestone | Category | Likely Hours | Investment |
|-----------|----------|--------------|------------|
| **M1** | Foundation | 26h | $3,820 |
| **M2** | Central Request Inbox | 32h | $7,500 |
| **M2** | Quote Workflow (OPP-4) | 21h | $4,700 |
| **M2** | Contact Sync (OPP-6) | 22h | $5,590 |
| **M2** | Sona KB (OPP-5) | 7h | $1,620 |
| **M3** | Smart Request Form | 6h | $1,175 |
| **M3** | Production Deployment | 7h | $1,470 |
| **M3** | Support Buffer | 4h | $1,175 |
| **QW** | Voice Assistant | 8h | $1,765 |
| **QW** | Quo-Jobber Fixes | 6h | $1,175 |
| **Trn** | Training Videos (5) | 9h | $1,765 |
| **Trn** | Operations Runbook | 5h | $1,175 |
| | | | |
| **TOTAL** | | **153h (likely)** | |
| **TOTAL** | | **204h (pessimistic)** | **$30,000** |

---

## ROI Summary by Opportunity

| Opportunity | Investment | Annual Impact | ROI | Payback |
|-------------|------------|---------------|-----|---------|
| **OPP-4:** Quote Automation | $4,700 | $67K-$104K | 14x-22x | ~2.5 weeks |
| **OPP-5:** Knowledge Capture | $1,620 + training | $215K-$299K | 40x-55x | <1 week |
| **OPP-6:** Contacts Consolidation | $5,590 | $133K-$173K | 24x-31x | ~2 weeks |
| **Voice Assistant** | $1,765 | $45K-$90K | 25x-50x | <1 week |
| **Quo-Jobber Fixes** | $1,175 | Efficiency | High | Immediate |
| | | | |
| **TOTAL MVP** | **$30,000** | **$416K-$576K** | **14x-19x** | **<4 weeks** |

---

## 8-Week Timeline

| Weeks | Focus | Hours | Investment |
|-------|-------|-------|------------|
| **1-2** | M1: Foundation | 26h | $3,820 |
| **3-4** | M2: Core Systems | 60h | $8,820 |
| **5-6** | M2: Core Systems (cont) | 72h | $10,590 |
| **7** | M3: Deploy + Training | 26h | $3,820 |
| **8** | M3: Go-Live + Support | 20h | $2,940 |
| **TOTAL** | | **204h** | **$30,000** |

**Weekly rate:** 25.5h/week (12.75h/week per dev)

---

## A-to-Z Card Mapping

| Card | Opportunity | Hours | Investment | Annual Impact |
|------|-------------|-------|------------|---------------|
| **D** | Quote Generation Automation | 32h | $4,700 | $67K-$104K |
| **E** | After Hours Voice Assistant | 12h | $1,765 | $45K-$90K |
| **F** | Quo-Jobber Workflow Fixes | 8h | $1,175 | Efficiency |
| **G** | Knowledge Capture (KB) | 11h | $1,620 | $215K-$299K* |
| **H** | Contacts Consolidation | 38h | $5,590 | $133K-$173K |
| **I** | Foundation & Architecture | 26h | $3,820 | Risk mitigation |
| **J** | Go-Live & Training | 26h | $3,820 | Adoption |
| **—** | Central Request Inbox | 51h | $7,500 | Shared infra |
| **TOTAL** | | **204h** | **$30,000** | **$416K-$576K** |

*Knowledge Capture ROI includes full training program (Phase 3)

---

## Pricing Tiers for Proposal

| Tier | Hours | Investment | Includes |
|------|-------|------------|----------|
| **Core** | 84h | $12,500 | Platform + Integrations only |
| **MVP** (Recommended) | 204h | $30,000 | Full core functionality |
| **Enhanced** | 238h | $35,000 | + Secondary integrations |
| **Full** | 292h | $43,000 | + ML, analytics, full videos |

---

## Risk Mitigation

| Risk | Hours Impact | Mitigation |
|------|--------------|------------|
| Outlook Integration | +6h | Start early, test auth separately |
| Contact Data Quality | +10h | Audit in M1, set expectations |
| Holding Area Scope | +8h | Lock design before build |
| Kelsey Scope Creep | +15h | Detailed SOW, change control |

**Buffer Built In:** Using pessimistic estimates gives 51h buffer (204h - 153h likely).

---

## Dependencies

- **Week 1:** Data access to Capsule, Jobber, QuickBooks, Outlook
- **Week 2:** Stakeholder availability for interviews
- **Week 3:** Phase 1 integration stable for extension
- **Week 5:** Client availability for training/walkthrough

---

## Success Metrics

### Phase 2 Success = All True
- [ ] Central holding area live with 3+ sources feeding in
- [ ] Quote workflow: Quo call → Holding Area → Jobber in <5 min
- [ ] Contacts consolidated: Andrew sees full database
- [ ] Voice assistant handling after-hours calls
- [ ] 5 training videos delivered
- [ ] Team using new workflows daily

---

*Estimate generated using client-rate pricing model with three-point estimation (Optimistic/Likely/Pessimistic). All investments shown at $147/hr blended rate.*
