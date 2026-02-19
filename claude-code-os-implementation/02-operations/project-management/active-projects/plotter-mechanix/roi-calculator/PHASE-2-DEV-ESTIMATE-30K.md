# Phase 2 Dev Estimate — $30K / 8 Weeks

**Date:** February 18, 2026
**Prepared By:** Matthew Kerns
**Dev Team:** Matthew Kerns, Trent Christopher
**Rate:** $50/hr (internal cost)

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Client Price** | $30,000 |
| **Timeline** | 8 weeks |
| **Total Dev Hours** | 292h (pessimistic) |
| **Internal Cost** | $14,600 (@$50/hr) |
| **Margin** | $15,400 (51%) |
| **Weekly Hours** | 36.5h/week (18h/week per dev) |

---

## Capacity Analysis

| Metric | Value |
|--------|-------|
| Timeline | 8 weeks |
| Weekly hours | 36.5h/week |
| **Total capacity** | **292h** |
| Internal cost (@$50/hr) | $14,600 |
| Client price | $30,000 |
| **Margin** | **$15,400 (51%)** |

---

## Scope Summary

### Included Opportunities

| # | Opportunity | Priority | Hours | Cost | ROI Doc |
|---|-------------|----------|-------|------|---------|
| 4 | Quote Generation Automation | Plan Carefully | 44h | $2,200 | OPP-4 |
| 5 | Knowledge Capture | Plan Carefully | 54h | $2,700 | OPP-5 |
| 6 | Contacts Consolidation | Plan Carefully | 46h | $2,300 | OPP-6 |
| — | Voice Assistant | Do First | 12h | $600 | Quick Win |
| — | Quo-Jobber Fixes | Do First | 8h | $400 | Quick Win |

### Excluded from $30K Phase

| Opportunity | Reason | Future Phase |
|-------------|--------|--------------|
| Supplies Workflow Automation | "Maybe Later" - needs Ply status | Phase 3 |
| Enterprise Contracts | Not in matrix | Phase 3+ |
| Remote Consulting Platform | Not in matrix | Phase 3+ |

---

## Milestone 1: Foundation (Weeks 1-2) — 41h

Discovery and planning work. Low dev risk.

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 1 | Workflow Documentation | 2h | 4h | 6h | Interview Alyssa, map her daily tasks minute-by-minute |
| 2 | Data Flow Diagram | 2h | 3h | 5h | Visual map: Quo → Jobber → QuickBooks → Capsule → Outlook |
| 3 | Contact Audit Report | 4h | 6h | 10h | Export all systems, count duplicates, assess data quality |
| 4 | Technical Spec Document | 6h | 10h | 16h | Architecture doc: APIs, data flows, automation rules |
| 5 | Demo Session | 2h | 3h | 4h | Prep + 60-min walkthrough with stakeholders |

**M1 Total:** 16h (opt) / **26h (likely)** / **41h (pess)**
**M1 Cost:** $2,050 (@$50/hr pessimistic)

### M1 Risks
- Low risk milestone
- Main dependency: getting data access and stakeholder time

---

## Milestone 2: Core Systems (Weeks 3-4) — 140h

This is where the real build happens.

### Central Request Inbox (Holding Area) — 51h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 6 | Design UI/workflow | 2h | 4h | 6h | Mockups and flow design |
| 7 | Outlook integration | 4h | 8h | 14h | Microsoft Graph API for email |
| 8 | Quo/SMS integration | 2h | 4h | 6h | Extend Phase 1 for holding area |
| 9 | Website leads integration | 1h | 2h | 3h | Jobber webhook |
| 10 | Build holding area UI | 6h | 10h | 16h | Alyssa's triage interface |
| 11 | Routing logic | 2h | 4h | 6h | Assign to correct person |

**Subtotal:** 17h / **32h** / **51h**

### Quote Workflow Automation (OPP-4) — 23h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 12 | Extend call summarization | 2h | 4h | 6h | Configure Quo to extract: part numbers, pricing, urgency |
| 13 | Quo→Holding Area→Jobber flow | 4h | 8h | 12h | Build automation: call ends → draft → approve → Jobber job |
| 14 | Deposit notification system | 2h | 3h | 5h | QuickBooks webhook: detect payment → notify → update status |

**Subtotal:** 8h / **15h** / **23h**

### Second-Call Job Creation — 9h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 15 | Flag in holding area | 1h | 2h | 3h | "Is this a new opportunity?" UI element for repeat callers |
| 16 | Alyssa workflow | 2h | 4h | 6h | Easy job creation from holding area for second-call opportunities |

**Subtotal:** 3h / **6h** / **9h**

### Contact Sync Engine (OPP-6) — 46h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 17 | Capsule export + cleanup | 3h | 6h | 10h | Export 10,581 contacts, normalize data, dedupe prep |
| 18 | Jobber import | 4h | 8h | 14h | Map fields, batch import, handle API rate limits |
| 19 | QuickBooks sync | 4h | 8h | 12h | Bi-directional sync setup |
| 20 | Duplicate merge rules | 3h | 6h | 10h | Define + implement merge logic |

**Subtotal:** 14h / **28h** / **46h**

### Sona AI Knowledge Base (OPP-5 partial) — 11h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 21 | Doc upload + indexing | 2h | 4h | 6h | Upload 50+ documents, configure KB |
| 22 | Voice/text search config | 2h | 3h | 5h | Enable techs to ask questions, get answers |

**Subtotal:** 4h / **7h** / **11h**

**M2 Total:** 46h (opt) / **88h (likely)** / **140h (pess)**
**M2 Cost:** $7,000 (@$50/hr pessimistic)

### M2 Risks
- **Outlook integration** — Microsoft Graph API can be tricky with auth
- **Contact migration** — Data quality unknown, could be messy
- **Holding area UI** — Custom build, scope creep risk

---

## Milestone 3: Go-Live (Weeks 5-8) — 91h

### Smart Request Form — 12h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 23 | Configure Jobber form | 1h | 2h | 3h | Apply Kelsey's specs |
| 24 | Embed on website | 1h | 2h | 3h | Add to their site |
| 25 | Auto-routing logic | 2h | 4h | 6h | Route by request type |

**Subtotal:** 4h / **8h** / **12h**

### Production Deployment — 16h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 26 | Connect to live systems | 3h | 6h | 10h | Careful cutover from staging to prod |
| 27 | Monitoring setup | 2h | 4h | 6h | Error alerts, logging, dashboard for system health |

**Subtotal:** 5h / **10h** / **16h**

### Training Videos (OPP-5) — 28h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 28 | Script + record (15 videos) | 8h | 12h | 18h | Write scripts, record screencasts |
| 29 | Edit + upload | 4h | 6h | 10h | Polish, add captions, host |

**Subtotal:** 12h / **18h** / **28h**

### WhatsApp Knowledge Group (OPP-5) — 3h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 30 | Setup + seed content | 1h | 2h | 3h | Create team knowledge group |

**Subtotal:** 1h / **2h** / **3h**

### Operations Runbook (OPP-5) — 12h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 31 | Document all workflows | 4h | 8h | 12h | Write SOPs for Alyssa |

**Subtotal:** 4h / **8h** / **12h**

### 30-Day Support Buffer — 20h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 32 | Bug fixes, adjustments | 4h | 10h | 20h | Reserved for post-launch issues |

**Subtotal:** 4h / **10h** / **20h**

**M3 Total:** 30h (opt) / **56h (likely)** / **91h (pess)**
**M3 Cost:** $4,550 (@$50/hr pessimistic)

### M3 Risks
- **Training videos** — Can take longer than expected
- **Production cutover** — Always surprises
- **30-day support** — Could eat hours if systems are shaky

---

## Quick Wins (Do First) — 20h

### After Hours Voice Assistant — 12h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 33 | Quo after-hours config | 1h | 2h | 3h | Configure voice flow: business hours check, message routing |
| 34 | Emergency escalation | 1h | 2h | 3h | Route urgent to on-call, non-urgent to voicemail |
| 35 | Jobber appointment booking | 1h | 2h | 3h | Book appointments directly via Quo → Jobber integration |
| 36 | Notification system | 1h | 2h | 3h | SMS/email alerts for captured leads |

**Subtotal:** 4h / **8h** / **12h**

**Deliverables:**
- Answer calls professionally after hours (6pm-8am, weekends)
- Capture detailed service requests
- Book appointments directly in Jobber
- Route emergency calls appropriately
- Send notifications for urgent issues

### Quo-Jobber Fixes — 8h

| # | Task | Opt | Likely | Pess | Notes |
|---|------|-----|--------|------|-------|
| 37 | Data sync debugging | 1h | 2h | 3h | Identify and fix sync failures between Quo and Jobber |
| 38 | Field mapping improvements | 1h | 1h | 2h | Clean up field mappings so data lands in correct fields |
| 39 | Duplicate handling | 1h | 1h | 2h | Improve logic to detect and merge duplicate contacts |
| 40 | Testing & validation | 0.5h | 1h | 1h | End-to-end test of fixed workflows |

**Subtotal:** 3.5h / **5h** / **8h**

**Quick Wins Total:** 7.5h (opt) / **13h (likely)** / **20h (pess)**
**Quick Wins Cost:** $1,000 (@$50/hr pessimistic)

---

## Grand Total Summary

| Milestone | Optimistic | Likely | Pessimistic | Cost (Pess) |
|-----------|------------|--------|-------------|-------------|
| M1: Foundation | 16h | 26h | 41h | $2,050 |
| M2: Core Systems | 46h | 88h | 140h | $7,000 |
| M3: Go-Live | 30h | 56h | 91h | $4,550 |
| Quick Wins | 7.5h | 13h | 20h | $1,000 |
| **TOTAL** | **99.5h** | **183h** | **292h** | **$14,600** |

---

## By Opportunity (Consolidated View)

| Opportunity | Direct Hours | Shared (33%) | Total | Cost |
|-------------|--------------|--------------|-------|------|
| **OPP-4:** Quote Automation | 32h | 17h | **49h** | $2,450 |
| **OPP-5:** Knowledge Capture | 54h | 17h | **71h** | $3,550 |
| **OPP-6:** Contacts Consolidation | 46h | 17h | **63h** | $3,150 |
| **Quick Wins** (Voice + Fixes) | 20h | — | **20h** | $1,000 |
| **Foundation (M1)** | 41h | — | **41h** | $2,050 |
| **Go-Live Shared** | 48h | — | **48h** | $2,400 |
| **TOTAL** | | | **292h** | **$14,600** |

*Shared = Holding Area (51h) split evenly across 3 opps*

---

## 8-Week Timeline

| Weeks | Focus | Hours | Key Deliverables |
|-------|-------|-------|------------------|
| 1-2 | M1: Foundation + Quick Wins | 61h | Specs, audit, data flow, voice assistant |
| 3-4 | M2: Core Systems | 140h | Holding area, quote flow, contact sync, KB |
| 5-6 | M3: Training + Deployment | 51h | Videos, runbook, form, production setup |
| 7-8 | M3: Go-Live + Support | 40h | Launch, monitoring, 30-day support |
| **TOTAL** | | **292h** | |

**Weekly rate:** 36.5h/week (18h/week per dev)

---

## Margin Analysis

**Client Price:** $30,000

| Scenario | Hours | Internal Cost | Margin | % |
|----------|-------|---------------|--------|---|
| Optimistic (99.5h) | $4,975 | $25,025 | 83% |
| **Likely (183h)** | **$9,150** | **$20,850** | **70%** |
| Pessimistic (292h) | $14,600 | $15,400 | 51% |

### Dev Split (50/50)
- Matthew: 146h (pessimistic) — ~18h/week over 8 weeks
- Trent: 146h (pessimistic) — ~18h/week over 8 weeks

---

## Annual Impact Summary

| Opportunity | Annual LOW | Annual HIGH | ROI |
|-------------|------------|-------------|-----|
| OPP-4: Quote Automation | $67,580 | $103,580 | 36x-56x |
| OPP-5: Knowledge Capture | $215,500 | $299,225 | 80x-111x |
| OPP-6: Contacts Consolidation | $132,770 | $172,845 | 58x-75x |
| Quick Wins (Voice + Fixes) | TBD | TBD | High (low investment) |
| **TOTAL** | **$415,850** | **$575,650** | **14x-19x** |

**Blended ROI:** $30K investment → $416K-$576K annual impact = **14x-19x return**
**Payback:** < 4 weeks

---

## Dependencies & Assumptions

### Dependencies
- **Week 1:** Data access to Capsule, Jobber, QuickBooks, Outlook
- **Week 2:** Stakeholder availability for interviews
- **Week 3:** Phase 1 integration stable for extension
- **Week 5:** Client availability for training/walkthrough

### Assumptions
1. Matthew provides Sona KB content (not dev responsibility)
2. Kelsey has provided website form specs (minimal design work)
3. Data access granted promptly in Week 1
4. Stakeholders available for interviews in M1
5. Phase 1 Quo→Jobber integration is stable and extensible
6. Capsule data is exportable (CSV or API)

---

## Highest Risk Items

| Risk | Hours (Likely) | Hours (Pess) | Mitigation |
|------|----------------|--------------|------------|
| Outlook Integration | 8h | 14h | Start early, test auth separately |
| Contact Migration | 14h | 24h | Get data exports in M1, assess quality early |
| Holding Area UI | 10h | 16h | Lock scope before building, use simple UI |
| 30-Day Support | 10h | 20h | Build solid in M2/M3 to reduce post-launch issues |

---

## Full Line Item Breakdown

| # | Milestone | Category | Task | Opt | Likely | Pess |
|---|-----------|----------|------|-----|--------|------|
| **M1** | **Foundation** | | | **16h** | **26h** | **41h** |
| 1 | M1 | Workflow Documentation | Map Alyssa's daily tasks, document current state | 2h | 4h | 6h |
| 2 | M1 | Data Flow Diagram | Map Quo→Jobber→QuickBooks→Capsule connections | 2h | 3h | 5h |
| 3 | M1 | Contact Audit Report | Export all 4 systems, count dupes, assess quality | 4h | 6h | 10h |
| 4 | M1 | Technical Spec Document | Architecture, API connections, automation rules | 6h | 10h | 16h |
| 5 | M1 | Demo Session | Prep + 60-min walkthrough | 2h | 3h | 4h |
| **M2** | **Core Systems** | | | **46h** | **88h** | **140h** |
| 6 | M2 | Holding Area | Design UI/workflow | 2h | 4h | 6h |
| 7 | M2 | Holding Area | Outlook integration (Microsoft Graph API) | 4h | 8h | 14h |
| 8 | M2 | Holding Area | Quo/SMS integration (extend existing) | 2h | 4h | 6h |
| 9 | M2 | Holding Area | Website leads integration (Jobber webhook) | 1h | 2h | 3h |
| 10 | M2 | Holding Area | Build holding area UI (Alyssa triage interface) | 6h | 10h | 16h |
| 11 | M2 | Holding Area | Routing logic (assign to correct person) | 2h | 4h | 6h |
| 12 | M2 | Quote Workflow | Extend call summarization (pull more fields) | 2h | 4h | 6h |
| 13 | M2 | Quote Workflow | Quo→Holding Area→Jobber flow | 4h | 8h | 12h |
| 14 | M2 | Quote Workflow | Deposit notification system (QuickBooks webhook) | 2h | 3h | 5h |
| 15 | M2 | Second-Call | Flag in holding area ("new opportunity?" UI) | 1h | 2h | 3h |
| 16 | M2 | Second-Call | Alyssa workflow (easy job creation) | 2h | 4h | 6h |
| 17 | M2 | Contact Sync | Capsule export + cleanup | 3h | 6h | 10h |
| 18 | M2 | Contact Sync | Jobber import (map fields, API limits) | 4h | 8h | 14h |
| 19 | M2 | Contact Sync | QuickBooks sync (bi-directional) | 4h | 8h | 12h |
| 20 | M2 | Contact Sync | Duplicate merge rules | 3h | 6h | 10h |
| 21 | M2 | Sona KB | Doc upload + indexing | 2h | 4h | 6h |
| 22 | M2 | Sona KB | Voice/text search config | 2h | 3h | 5h |
| **M3** | **Go Live** | | | **30h** | **56h** | **91h** |
| 23 | M3 | Request Form | Configure Jobber form (Kelsey's specs) | 1h | 2h | 3h |
| 24 | M3 | Request Form | Embed on website | 1h | 2h | 3h |
| 25 | M3 | Request Form | Auto-routing logic (route by type) | 2h | 4h | 6h |
| 26 | M3 | Deployment | Connect to live systems (careful cutover) | 3h | 6h | 10h |
| 27 | M3 | Deployment | Monitoring setup (error alerts, logging) | 2h | 4h | 6h |
| 28 | M3 | Training Videos | Script + record (15 videos) | 8h | 12h | 18h |
| 29 | M3 | Training Videos | Edit + upload | 4h | 6h | 10h |
| 30 | M3 | WhatsApp Group | Setup + seed content | 1h | 2h | 3h |
| 31 | M3 | Operations Runbook | Document all workflows (SOPs for Alyssa) | 4h | 8h | 12h |
| 32 | M3 | Support Buffer | Bug fixes, adjustments (30-day support) | 4h | 10h | 20h |
| **Quick** | **Wins** | | | **7.5h** | **13h** | **20h** |
| 33 | QW | Voice Assistant | Quo after-hours config | 1h | 2h | 3h |
| 34 | QW | Voice Assistant | Emergency escalation | 1h | 2h | 3h |
| 35 | QW | Voice Assistant | Jobber appointment booking | 1h | 2h | 3h |
| 36 | QW | Voice Assistant | Notification system | 1h | 2h | 3h |
| 37 | QW | Quo-Jobber Fixes | Data sync debugging | 1h | 2h | 3h |
| 38 | QW | Quo-Jobber Fixes | Field mapping improvements | 1h | 1h | 2h |
| 39 | QW | Quo-Jobber Fixes | Duplicate handling | 1h | 1h | 2h |
| 40 | QW | Quo-Jobber Fixes | Testing & validation | 0.5h | 1h | 1h |
| | **TOTAL** | | | **99.5h** | **183h** | **292h** |

---

*Estimate generated using WBS methodology with three-point estimation (Optimistic/Likely/Pessimistic)*
*Internal rate: $50/hr | Client price: $30,000 | Margin: 51-83%*
