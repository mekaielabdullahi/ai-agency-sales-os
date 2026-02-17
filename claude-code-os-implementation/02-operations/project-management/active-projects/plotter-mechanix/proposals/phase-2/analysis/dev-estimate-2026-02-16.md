# Phase 2 Dev Estimate — Work Breakdown Structure

**Date:** February 16, 2026
**Prepared By:** Taylor (Scope & Timeline Builder Agent) + Matthew
**Dev Team:** Matthew Kerns, Trent Christopher
**Proposal Reference:** phase-2-proposal-2026-02-13-polished.md

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Proposal Price** | $28,000 |
| **Likely Dev Hours** | 170h |
| **Effective Rate** | $165/hr |
| **Timeline** | 6 weeks |
| **Weekly Hours (total)** | ~28h/week |
| **Weekly Hours (per dev)** | ~14h/week each |

---

## Key Technical Decisions

| Component | Decision | Rationale |
|-----------|----------|-----------|
| **Email Provider** | Outlook | Multiple addresses: service@, supplies@, sales@, etc. |
| **SMS** | Quo | Already integrated from Phase 1 |
| **Website Form** | Jobber request form | Kelsey provided specs, minimal custom work |
| **Holding Area** | Custom build | Jobber limitations for multi-call workflows |
| **Second-call Detection** | Manual (Alyssa reviews) | Holding area + human judgment, not automated |
| **Contact Source of Truth** | Jobber (after migration) | Capsule contacts → Jobber, then deprecate Capsule |
| **Sona KB Content** | Matthew uploads | Dev configures, Matthew provides content |

---

## Milestone 1: Foundation (Weeks 1-2) — $10,000

Discovery and planning work. Low dev risk.

| Deliverable | Tasks | Opt | Likely | Pess | Notes |
|-------------|-------|-----|--------|------|-------|
| **Workflow Documentation** | Map Alyssa's daily tasks, document current state | 2h | 4h | 6h | Interview + write-up |
| **Data Flow Diagram** | Map Quo→Jobber→QuickBooks→Capsule connections | 2h | 3h | 5h | Visual + gaps analysis |
| **Contact Audit Report** | Export all 4 systems, count dupes, assess quality | 4h | 6h | 10h | Depends on data access |
| **Technical Spec Document** | Architecture, API connections, automation rules | 6h | 10h | 16h | The real deliverable |
| **Demo Session** | Prep + 60-min walkthrough | 2h | 3h | 4h | |

**Milestone 1 Total:** 16h (opt) / **26h (likely)** / 41h (pess)

### Risks
- Low risk milestone
- Main dependency: getting data access and stakeholder time

---

## Milestone 2: Core Systems (Weeks 3-4) — $10,000

This is where the real build happens.

### Central Request Inbox (Holding Area)

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Design UI/workflow | 2h | 4h | 6h | Mockups, flow design |
| Outlook integration | 4h | 8h | 14h | Microsoft Graph API |
| Quo/SMS integration | 2h | 4h | 6h | Extend existing for holding area |
| Website leads integration | 1h | 2h | 3h | Jobber webhook |
| Build holding area UI | 6h | 10h | 16h | Custom build - Alyssa's triage interface |
| Routing logic | 2h | 4h | 6h | Assign to correct person |

**Subtotal:** 17h / **32h** / 51h

### Quote Workflow Automation

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Extend call summarization | 2h | 4h | 6h | Pull more fields for quotes, build on Phase 1 |
| Quo→Holding Area→Jobber flow | 4h | 8h | 12h | Streamline quote creation |
| Deposit notification system | 2h | 3h | 5h | QuickBooks webhook |

**Subtotal:** 8h / **15h** / 23h

### Second-Call Job Creation

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Flag in holding area | 1h | 2h | 3h | "Is this a new opportunity?" UI element |
| Alyssa workflow | 2h | 4h | 6h | Easy job creation from holding area |

**Subtotal:** 3h / **6h** / 9h

### Contact Sync Engine

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Capsule export + cleanup | 3h | 6h | 10h | Export, normalize, dedupe prep |
| Jobber import | 4h | 8h | 14h | Map fields, import contacts, watch API limits |
| QuickBooks sync | 4h | 8h | 12h | Bi-directional sync setup |
| Duplicate merge rules | 3h | 6h | 10h | Define + implement logic |

**Subtotal:** 14h / **28h** / 46h

### Sona AI Knowledge Base

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Doc upload + indexing | 2h | 4h | 6h | Matthew provides docs, dev configures KB |
| Voice/text search config | 2h | 3h | 5h | Configure Sona interface |

**Subtotal:** 4h / **7h** / 11h

**Milestone 2 Total:** 46h (opt) / **88h (likely)** / 140h (pess)

### Risks
- **Outlook integration** — Microsoft Graph API can be tricky with auth
- **Contact migration** — Data quality unknown, could be messy
- **Holding area UI** — Custom build, scope creep risk

---

## Milestone 3: Go Live (Weeks 5-6) — $8,000

### Smart Request Form

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Configure Jobber form | 1h | 2h | 3h | Apply Kelsey's specs |
| Embed on website | 1h | 2h | 3h | Add to their site |
| Auto-routing logic | 2h | 4h | 6h | Route by request type |

**Subtotal:** 4h / **8h** / 12h

### Production Deployment

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Connect to live systems | 3h | 6h | 10h | Careful cutover from test to prod |
| Monitoring setup | 2h | 4h | 6h | Error alerts, logging |

**Subtotal:** 5h / **10h** / 16h

### Training Videos (15)

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Script + record | 8h | 12h | 18h | 15 videos @ ~30min production each |
| Edit + upload | 4h | 6h | 10h | Polish + host |

**Subtotal:** 12h / **18h** / 28h

### WhatsApp Knowledge Group

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Setup + seed content | 1h | 2h | 3h | Create group, add initial tips |

**Subtotal:** 1h / **2h** / 3h

### Operations Runbook

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Document all workflows | 4h | 8h | 12h | Written SOPs for Alyssa |

**Subtotal:** 4h / **8h** / 12h

### 30-Day Support Buffer

| Task | Opt | Likely | Pess | Notes |
|------|-----|--------|------|-------|
| Bug fixes, adjustments | 4h | 10h | 20h | Unknown unknowns, included in estimate |

**Subtotal:** 4h / **10h** / 20h

**Milestone 3 Total:** 30h (opt) / **56h (likely)** / 91h (pess)

### Risks
- **Training videos** — Can take longer than expected
- **Production cutover** — Always surprises
- **30-day support** — Could eat hours if systems are shaky

---

## Total Estimate Summary

| Milestone | Optimistic | **Likely** | Pessimistic |
|-----------|------------|------------|-------------|
| M1: Foundation | 16h | **26h** | 41h |
| M2: Core Systems | 46h | **88h** | 140h |
| M3: Go Live | 30h | **56h** | 91h |
| **TOTAL** | **92h** | **170h** | **272h** |

---

## Margin Analysis

**Proposal Price:** $28,000

| Scenario | Hours | Effective Rate | Assessment |
|----------|-------|----------------|------------|
| Optimistic (92h) | $304/hr | Excellent margin |
| **Likely (170h)** | **$165/hr** | Solid margin |
| Pessimistic (272h) | $103/hr | Tight but acceptable |

### Dev Split (50/50)
- Matthew: 85h (likely) — ~14h/week over 6 weeks
- Trent: 85h (likely) — ~14h/week over 6 weeks

---

## Highest Risk Items

| Risk | Hours (Likely) | Hours (Pess) | Mitigation |
|------|----------------|--------------|------------|
| Outlook Integration | 8h | 14h | Start early, test auth separately |
| Contact Migration | 14h | 24h | Get data exports in M1, assess quality early |
| Holding Area UI | 10h | 16h | Lock scope before building, use simple UI |
| 30-Day Support | 10h | 20h | Build solid in M2/M3 to reduce post-launch issues |

---

## Assumptions

1. Matthew provides Sona KB content (not dev responsibility)
2. Kelsey has provided website form specs (minimal design work)
3. Data access granted promptly in Week 1
4. Stakeholders available for interviews in M1
5. Phase 1 Quo→Jobber integration is stable and extensible
6. Capsule data is exportable (CSV or API)

---

## Dependencies

- **Week 1:** Data access to Capsule, Jobber, QuickBooks, Outlook
- **Week 2:** Stakeholder availability for interviews
- **Week 3:** Phase 1 integration stable for extension
- **Week 5:** Client availability for training/walkthrough

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
| | **TOTAL** | | | **92h** | **170h** | **272h** |

---

*Estimate generated using WBS methodology with three-point estimation (Optimistic/Likely/Pessimistic)*
