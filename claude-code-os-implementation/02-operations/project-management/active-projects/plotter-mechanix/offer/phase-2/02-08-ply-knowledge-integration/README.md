# Phase 2 Ply Knowledge Integration - February 8, 2026

**Status:** ⚠️ PENDING MEGAN INTERVIEW
**Target Delivery:** Saturday, February 15, 2026 (Kelsey call)
**Impact:** Critical scope validation + pricing refinement

---

## Executive Summary

This folder contains all research, planning, and preparation materials for the Phase 2 scope revision based on the 19-page Ply + Jobber Integration Overview deck.

**Key Findings:**
1. Ply is MORE capable than initially thought (tools tracking, 3K+ suppliers, native Jobber integration)
2. Jobber ↔ Ply integration is NATIVE (real-time webhooks) - we don't need to build this
3. Ply offers $5K+ warehouse audit/implementation service
4. Our $8K "Ply Enhancements" scope overlaps with Ply's native features

**Critical Path:**
- Interview Megan → Determine implementation status → Revise scope → Present Saturday

---

## Documents in This Folder

### 1. `ply-platform-capabilities.md`
**Purpose:** Comprehensive reference documentation of Ply's features
**Use For:**
- Understanding what Ply already provides (avoid duplicating work)
- Technical specs for integration planning
- ROI data and case studies

**Key Sections:**
- Core features (Smart Catalog, Inventory Management, Tools Tracking, etc.)
- Jobber integration details (bidirectional sync, webhooks)
- Implementation services ($5K warehouse audit)
- ROI case study ($60K savings for $3M contractor)

---

### 2. `megan-interview-prep.md`
**Purpose:** Structured interview guide for Megan (Inventory/Operations Lead)
**Use For:**
- Conducting the Megan interview (45-60 min)
- Determining Ply implementation status (0-100%)
- Validating Phase 2 scope assumptions

**Key Sections:**
- Priority-ordered questions (P0 blockers first)
- Implementation status assessment
- Jobber integration validation
- Used parts tracking approach
- Technical integration details (API access, etc.)
- Pain points and gaps

**Success Criteria:**
- ✅ Clear % of Ply implementation completed
- ✅ Jobber ↔ Ply sync status confirmed
- ✅ Used parts tracking approach validated
- ✅ API credentials obtained or path to obtaining confirmed

---

### 3. `phase2-scope-revision-tracker.md`
**Purpose:** Decision framework for revising Phase 2 scope based on findings
**Use For:**
- Tracking scope evolution (Original → Revised)
- Pricing sensitivity analysis ($5K-13K scenarios)
- ROI calculations for Plotter Mechanix
- Decision tree based on Megan interview answers

**Key Sections:**
- Original vs. Revised scope comparison
- 3 scenarios (A/B/C) based on Megan's implementation status
- Decision tree (if YES → do X, if NO → do Y)
- Pricing sensitivity analysis
- ROI justification ($19-25K annual savings projected)
- Competitive positioning (what we provide vs. what Ply provides)

**Scenarios:**
- **Scenario A ($13K):** Megan hasn't purchased Ply audit → recommend Ply's $5K + our $8K
- **Scenario B ($5K):** Megan fully implemented Ply → just build Quo integration
- **Scenario C ($8K - MOST LIKELY):** Partial implementation → complete + integrate

---

### 4. `saturday-call-prep-checklist.md`
**Purpose:** Complete preparation checklist for Saturday's Kelsey call
**Use For:**
- Pre-call task tracking
- Call agenda and talking points
- Handling objections
- Post-call follow-up

**Key Sections:**
- Pre-call checklist (BLOCKING items, high-priority, nice-to-have)
- Call agenda (7-part structure)
- Talking points and scripts
- Objection handling responses
- Questions to ask Kelsey
- Post-call checklist
- Team roles and responsibilities
- Success criteria
- Contingency plans

**Call Structure:**
1. Opening (5 min) - Context setting
2. Ply capabilities overview (5-7 min)
3. The real gap: Quo ↔ Ply integration (10 min)
4. Revised Phase 2 scope & pricing (10-15 min)
5. ROI justification (5-7 min)
6. Questions & discussion (10-15 min)
7. Next steps & close (5 min)

---

## Critical Path Timeline

### TODAY (Feb 8, 2026)
- [x] Review Ply + Jobber Integration deck (COMPLETE)
- [x] Create knowledge base documentation (COMPLETE)
- [x] Prepare Megan interview questions (COMPLETE)
- [ ] **BLOCKING:** Schedule Megan interview (ASAP)

### MONDAY/TUESDAY (Feb 10-11) - TARGET
- [ ] Conduct Megan interview (45-60 min)
- [ ] Compile interview notes
- [ ] Determine Scenario A/B/C

### WEDNESDAY/THURSDAY (Feb 12-13)
- [ ] Draft revised Phase 2 proposal
- [ ] Create ROI slide deck
- [ ] Prepare talking points for Kelsey call
- [ ] Share with team for review (Chris, Mekaiel, Trent)

### FRIDAY (Feb 14)
- [ ] Finalize proposal and slides
- [ ] Rehearse call flow
- [ ] Prepare contingency plans

### SATURDAY (Feb 15)
- [ ] **DELIVER:** Present revised Phase 2 to Kelsey
- [ ] Get buy-in on scope and pricing
- [ ] Schedule Phase 2 kickoff (if approved)

---

## Key Questions to Answer

### From Megan Interview (P0 - BLOCKING)
1. **Did you purchase Ply's $5K+ warehouse audit service?**
   - If YES → Scenario B ($5K scope)
   - If NO → Scenario A ($13K scope)
   - If PARTIAL → Scenario C ($8K scope)

2. **Is Jobber ↔ Ply material sync ACTIVE?**
   - If YES → Remove from scope ($0)
   - If NO → Investigate why (config issue, not custom build)

3. **How are used parts tracked today?**
   - If using Ply Tools feature → Remove from scope ($0)
   - If manual (spreadsheets) → Configure Tools feature ($3K)
   - If not tracked → Design workflow + configure ($5K)

4. **Do you have Ply API access credentials?**
   - If YES → Proceed with Quo integration
   - If NO → Request from Ply support (required for Phase 2)

---

## Scope Validation Matrix

| Feature/Deliverable | Ply Native? | Megan Has It? | Our Scope? |
|---------------------|-------------|---------------|------------|
| Jobber ↔ Ply sync | ✅ YES | ❓ TBD | ❌ NO (if active) |
| Barcode scanning | ✅ YES | ❓ TBD | ⚠️ Maybe (training) |
| Tools tracking | ✅ YES | ❓ TBD | ⚠️ Maybe (config) |
| Used parts workflow | ⚠️ Can use Tools | ❓ TBD | ⚠️ Maybe (design) |
| Quo ↔ Ply integration | ❌ NO | ❌ NO | ✅ YES (core value) |
| Chat agent (inventory lookup) | ❌ NO | ❌ NO | ✅ YES (core value) |

**Legend:**
- ✅ YES = Included/Available
- ❌ NO = Not included/Not available
- ⚠️ Maybe = Depends on Megan's answers
- ❓ TBD = To be determined in interview

---

## ROI Quick Reference

### Ply's Case Study ($3M Contractor)
- Material spend reduced: 22% → 20% (2% improvement)
- Annual savings: $60K (material) + $15-20K (hidden costs) = **$75-80K/year**

### Plotter Mechanix Projections ($700-800K Revenue)
- Material spend: ~$154-176K/year (22% of revenue)
- 2% improvement: **$14-16K/year**
- Additional savings (tech time, emergency purchases): **$5-9K/year**
- **Total: $19-25K/year**

### Payback Period
- Mid-range scenario ($8K): **3-5 months**
- High-end scenario ($13K): **6-8 months**

### 5-Year ROI
- Investment: $8-13K (one-time)
- 5-year savings: $95-125K
- **ROI: 730-960%**

---

## Next Actions

### Immediate (Today)
- [ ] Schedule Megan interview for Monday or Tuesday (BLOCKING)
- [ ] Share this folder with team (Chris, Mekaiel, Trent)
- [ ] Assign interview owner (Matthew or Mekaiel)

### After Megan Interview
- [ ] Update scope revision tracker with findings
- [ ] Lock in Scenario A/B/C
- [ ] Begin proposal drafting

### Before Saturday Call
- [ ] Finalize proposal (1-2 pages)
- [ ] Create ROI slide deck (3-5 slides)
- [ ] Rehearse call flow with team
- [ ] Prepare objection handling responses

---

## Team Responsibilities

| Role | Owner | Tasks |
|------|-------|-------|
| **Interview Lead** | Matthew or Mekaiel | Conduct Megan interview, compile notes |
| **Proposal Author** | Matthew + Mekaiel | Draft revised Phase 2 proposal |
| **ROI Analyst** | Matthew | Create ROI slide deck with projections |
| **Technical Validator** | Matthew or Trent | Confirm Quo ↔ Ply integration feasibility |
| **Call Lead** | Mekaiel | Present to Kelsey, handle objections |
| **Technical Support** | Matthew | Answer technical questions on call |

---

## Risk Assessment

### HIGH RISK
- ⚠️ **Megan interview doesn't happen before Saturday**
  - Mitigation: Schedule ASAP (Monday/Tuesday latest)
  - Backup: Present all 3 scenarios to Kelsey, follow up with final pricing

- ⚠️ **Megan fully implemented Ply (Scenario B)**
  - Impact: Scope drops to $5K (Quo integration only)
  - Mitigation: Position as "fast, focused, high-value integration"

### MEDIUM RISK
- ⚠️ **Kelsey pushes back on pricing**
  - Mitigation: Show ROI (3-5 month payback), offer phased approach

- ⚠️ **Technical blockers in Quo ↔ Ply integration**
  - Mitigation: Review Ply API docs, confirm feasibility before Saturday

### LOW RISK
- ⚠️ **Ply API credentials not available**
  - Mitigation: Request from Ply support during Phase 2 kickoff

---

## Success Metrics

**Minimum Success:**
- ✅ Megan interview completed
- ✅ Scope revision validated
- ✅ Kelsey understands revised proposal

**Target Success:**
- ✅ Kelsey approves Phase 2 scope
- ✅ Proposal signed or agreement to move forward
- ✅ Phase 2 kickoff scheduled

**Stretch Success:**
- ✅ Proposal signed during call
- ✅ Kickoff scheduled for next week
- ✅ Ply API credentials obtained
- ✅ Kelsey excited and confident

---

## References

- **Source Document:** Ply + Jobber Integration Overview (19-page deck)
- **Related Docs:** Phase 1 deliverables, original Phase 2 scope (pre-revision)
- **Team Sync Cards:** `01-executive-office/strategic-alignment/team-sync-cards.md`
- **Active Projects Tracker:** `02-operations/project-management/active-projects/`

---

*Last Updated: February 8, 2026*
*Next Review: After Megan interview*
*Status: ⚠️ PENDING MEGAN INTERVIEW*
