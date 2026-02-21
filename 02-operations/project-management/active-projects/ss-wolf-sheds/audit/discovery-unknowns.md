# S&S Wolf Sheds - Discovery Unknowns

**Created:** December 28, 2025
**Source:** Discovery Call Analysis - December 22, 2025
**Updated:** December 28, 2025 (Post-Discovery Working Session)
**Status:** Partially Resolved, New Questions Added

---

## Purpose

This document tracks information gaps identified during discovery that need validation or additional data collection before finalizing scope and pricing.

**Anti-Hallucination Rule:** We do NOT fabricate data. These unknowns must be resolved through direct client communication.

---

## Resolution Summary (Post Dec 28 Session + Transcript Analysis)

| Category | Original Count | Resolved | New | Current Open |
|----------|---------------|----------|-----|--------------|
| Critical | 3 | 3 | 2 | 2 |
| Important | 3 | 4 | 3 | 2 |
| Nice-to-Know | 3 | 5 | 1 | 2 |

**Transcript Analysis Update:** Additional items resolved from 113-minute transcript review.

---

## Critical Unknowns (Block Implementation)

### CU-1: MVP Budget and Timeline

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| What is the MVP budget? | Scoping and pricing | Chris Andrade | **NEW - OPEN** |
| Is "MVP by Friday" realistic? | Timeline commitment | Team discussion | **NEW - OPEN** |
| Who approves MVP spend? | Procurement process | Chris | **NEW - OPEN** |

**Impact if Unknown:** Cannot finalize proposal or commit to timeline.

---

### CU-2: 300-Page SOT Processing ~~Time Drain Quantification~~ - PARTIALLY RESOLVED (from Transcript)

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| What's in the 300-page SOT v1? | Scope definition | Chris/AI processing | **PARTIALLY RESOLVED** |
| Which sections are MVP-relevant? | Avoid scope creep | Team review | STILL OPEN |
| Is document indexed/structured? | Processing ease | Chris | **RESOLVED - YES, has TOC + page numbers** |
| ~~How many hours/week on FAQs?~~ | ~~Chatbot ROI~~ | - | ~~DEPRIORITIZED~~ |

**Impact if Unknown:** Risk of building wrong thing or scope explosion.

**From Transcript:** SOT v1 "Keys to the Castle" is ~295-300 pages, 4 years of work by Chris. Has indexed table of contents with page numbers. Contains: prompt breakdowns, master sheets, project summary, marketing research, engineered question sets for customer profiling, full conversation transcripts. Team tested uploading to Google AI Studio during call - created mind map visualization. Plan: use embeddings/RAG for semantic search.

**Note:** Original CU-1 (FAQ time drain) deprioritized - chatbot is now Phase 2.

---

### CU-3: ~~Lead Volume Baseline~~ PARTIALLY RESOLVED

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| Historical sales data available? | Baseline comparison | Chris confirmed | **RESOLVED - YES** |
| 2-3 years of data accessible? | Trend analysis | Chris confirmed | **RESOLVED - YES** |
| ~~Monthly lead volume pre-October?~~ | - | - | DEPRIORITIZED |
| ~~Lead sources breakdown?~~ | - | - | DEPRIORITIZED |

**Resolution:** Chris confirmed 2-3 years of historical sales data available. Focus shifted from lead volume to on-lot capture. Lead source attribution less critical for MVP.

---

### CU-4: ~~Revenue & Margin Data~~ DEFERRED

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| Average order value? | ROI calculation | Sales records | **DEFERRED - Phase 2** |
| $400/day operating cost? | Break-even | Sandra | **DEFERRED - Phase 2** |

**Note:** Revenue/margin data useful but not blocking for MVP. Focus is on capture, not ROI calculation yet.

---

## Important Unknowns (Affect Scope)

### IU-1: Website & Tech Access - PARTIALLY RESOLVED

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| WordPress admin credentials | Website fixes + intake form | Alex | **RESOLVED - "Ready whenever"** |
| Hosting provider details | Diagnose instability | Alex | STILL OPEN |
| Facebook page admin access | Future - not MVP | - | DEFERRED |
| Google Analytics access | Phase 2 dashboard | - | DEFERRED |

**Resolution:** Chris confirmed website access ready "whenever." Need to get actual credentials.

---

### IU-2: Excel/Inventory System Details - NEW

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| Does SNS Excel have external refs/macros? | Migration risk | Matthew | **NEW - OPEN** |
| Can we migrate to Sheets? | Online collaboration | Matthew | **NEW - OPEN** |
| Current slot-to-building mapping format? | QR system design | Chris | **NEW - OPEN** |
| How often does inventory change slots? | Maintenance frequency | Chris | **NEW - OPEN** |

**Impact if Unknown:** May complicate inventory tracking integration.

---

### IU-3: QR/Slot System Design - PARTIALLY RESOLVED (from Transcript)

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| Preferred QR management tool? | Tech selection | Team research | STILL OPEN (Bitly/Dubb-like discussed) |
| Physical QR placement/signage? | User experience | Chris/lot attendants | STILL OPEN |
| Intake form question set? | Lead qualification | Chris | **PARTIALLY RESOLVED - 7 questions** |
| Notification preferences (SMS/email/push)? | Attendant workflow | Chris | **RESOLVED - Low-latency all channels** |
| Slot count per lot? | System design | Chris | **RESOLVED - 20 slots max** |
| Incentive strategy? | User adoption | Chris | **PARTIALLY RESOLVED - $50 off for 7 questions** |

**From Transcript:** Chris confirmed 20 buildings max per lot = 20 fixed slot QR codes. Notification preference: "instantaneous" - email/SMS/push all discussed. Graceland's new commission structure enables $50 off incentive for completing 7 engineered questions. Trent suggested dynamic QR codes (Bitly/Dubb-like) for backend remapping. Matthew demoed Bolt.new intake form prototype during call with 10% off offer, contact capture, building type, size, timeline, consultation CTA.

**Impact if Unknown:** Design decisions delayed.

---

### IU-4: ~~Custom Order Process~~ Delivery Handoff - MODIFIED

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| What site info does driver need? | Handoff artifact design | Scott | **MODIFIED - OPEN** |
| Current delivery failure rate? | Baseline for improvement | Scott | **NEW - OPEN** |
| How does customer provide site info today? | Current workflow | Chris | **NEW - OPEN** |
| ~~Order spec format?~~ | - | - | DEPRIORITIZED |

**Note:** Focus shifted from order verification (Phase 2+) to delivery handoff (Phase 1.5).

---

## Nice-to-Know Unknowns (Optimization)

### NK-1: Platform Viability - PARTIALLY RESOLVED (from Transcript)

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| How many dealers in Graceland AZ network? | Platform opportunity size | Chris | **RESOLVED - ~6 key players** |
| Who decides dealer recommendations? | Go-to-market for platform | Chris | STILL OPEN |
| What would make compelling demo for dealers? | Case study design | Chris | STILL OPEN |
| Graceland corporate involvement needed? | Platform approval path | Chris | STILL OPEN |
| Does Chris know the other dealers? | Warm intro potential | Chris | **RESOLVED - Knows all 6 personally** |
| Arizona-specific challenges? | Differentiation | Chris | **RESOLVED - Hard ground/terrain unique** |

**From Transcript:** Chris confirmed ~6 key Graceland dealers in Arizona, knows all personally. Arizona/New Mexico have unique terrain challenges (hard ground) that require extra Graceland investment. 50-mile radius territory rule exists. Strategy: prove value at S&S first, then leverage for network rollout.

---

### NK-2: ~~Competitive Landscape~~ Marketing Services - PARTIALLY RESOLVED (from Transcript)

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| Krista Green white-label pricing/terms? | Marketing upsell | Review sheet | **RESOLVED - $1k/mo 12 posts, $2.5k website** |
| Marketing budget for promo ($2.5k/mo mentioned)? | Scope potential | Chris | **RESOLVED - Comfortable with spend** |
| Content assets available? | Production readiness | Chris | **RESOLVED - 30 hrs drone/delivery footage** |
| ~~Main competitors?~~ | - | - | DEFERRED |

**From Transcript:** Chris expressed immediate interest in 12-post/month plan: "I will pay for that 12th post, like right, like tomorrow." Has 30 hours of drone footage, delivery videos, and pictures ready. Wholesale: $1k/mo for 12 posts, $2.5k for 8-page website. Suggested resale: $1.2-2.8k/mo and $6-10k respectively.

---

### NK-3: Growth Plans - UNCHANGED

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| Expansion beyond 3 lots? | Scalability requirements | Sandra | DEFERRED |
| Hiring plans? | Training needs | Sandra | DEFERRED |
| Seasonal demand patterns? | Campaign timing | Sales records | DEFERRED |

---

### NK-4: Scheduling Platform - NEW

| Question | Why It Matters | Source to Validate | Status |
|----------|----------------|-------------------|--------|
| Cal.com vs Calendly preference? | Team scheduling | Team research | **NEW - OPEN** |
| Integration requirements? | Tooling decisions | Team | **NEW - OPEN** |

---

## Data Collection Plan (Updated)

### Before MVP Kickoff (REQUIRED)

| Data Point | Owner | Method | Deadline |
|------------|-------|--------|----------|
| Website admin credentials | Alex → Matthew | Shared login | Before build starts |
| Slot-to-building mapping (current format) | Chris | Excel export | Before QR design |
| MVP budget confirmation | Chris | Verbal or email | Before proposal final |
| Top 5 intake form questions | Chris | Discussion | Dec 29 sync |
| Notification preferences | Chris | Discussion | Dec 29 sync |

### During Sprint 1 (Can Gather While Building)

| Data Point | Owner | Method | Deadline |
|------------|-------|--------|----------|
| Excel external refs check | Matthew | Open and inspect | Week 1 |
| QR tool selection | Team | Research | Week 1 |
| Signage/placement plan | Chris + attendants | Site visit | Week 1 |
| Historical sales baseline | Chris | Data export | Week 1 |

### Before Phase 2 (Required for Expansion)

| Data Point | Owner | Method | Deadline |
|------------|-------|--------|----------|
| Delivery failure rate baseline | Scott | Interview | Before handoff build |
| Site info collection workflow | Chris | Process doc | Before handoff build |
| Traffic counting requirements | Team | Research | Before Phase 2 |
| Platform opportunity sizing | Chris | Graceland network info | After MVP success |

---

## Follow-Up Questions for Dec 29 6am Sync

### MVP Scope Questions
1. What's the budget envelope for the MVP?
2. Is "by Friday" still the target, or is next week more realistic?
3. What 5 questions should the intake form ask to qualify leads?
4. Do you prefer SMS, email, or both for attendant notifications?

### Technical Questions
1. Can Matthew get website access today?
2. Does the SNS Excel file have any external references or macros?
3. What's the current format for slot-to-building mapping?
4. How often does a building move from one slot to another?

### SOT Processing
1. Can you share the SOT v1 document to Slack?
2. Which sections are most relevant to the on-lot capture MVP?
3. Is there a table of contents or summary we can use?

---

## Resolution Tracking (Updated with Transcript Analysis)

| Unknown ID | Status | Resolved Date | Resolution Notes |
|------------|--------|---------------|------------------|
| CU-1 (FAQ hours) | DEPRIORITIZED | Dec 28 | Chatbot is Phase 2 |
| CU-2 (Lead baseline) | PARTIALLY RESOLVED | Dec 28 | Historical sales confirmed available |
| CU-3 (Revenue data) | DEFERRED | Dec 28 | Not needed for MVP |
| IU-1 (Website access) | PARTIALLY RESOLVED | Dec 28 | "Ready whenever" - need credentials |
| IU-2 (Order specs) | DEPRIORITIZED | Dec 28 | SOP is Phase 2+ |
| IU-3 (Content) | PARTIALLY RELEVANT | Dec 28 | Intake form questions needed |
| NK-1 (Competitors) | DEFERRED | Dec 28 | Not MVP relevant |
| NK-2 (Growth) | DEFERRED | Dec 28 | Not MVP relevant |
| NK-3 (Graceland demo) | EXPANDED | Dec 28 | Now part of platform vision |

### New Unknowns Added Dec 28

| Unknown ID | Question | Priority |
|------------|----------|----------|
| CU-1 (new) | MVP budget and timeline | CRITICAL |
| CU-2 (new) | 300-page SOT processing | CRITICAL |
| IU-2 (new) | Excel/inventory system details | IMPORTANT |
| IU-3 (new) | QR/slot system design decisions | IMPORTANT |
| IU-4 (mod) | Delivery handoff requirements | IMPORTANT |
| NK-1 (new) | Platform viability questions | NICE-TO-KNOW |
| NK-4 (new) | Scheduling platform choice | NICE-TO-KNOW |

### Additional Items Resolved from Transcript (Dec 28)

| Unknown | Resolution | Source |
|---------|------------|--------|
| SOT document structure | Has TOC, page numbers, indexed | Transcript |
| Arizona dealer count | ~6 key players | Transcript |
| Chris network relationships | Knows all 6 personally | Transcript |
| Arizona terrain challenges | Hard ground, unique to region | Transcript |
| Krista Green pricing | $1k/mo 12 posts, $2.5k website | Transcript |
| Content assets ready | 30 hours drone footage | Transcript |
| Slot count per lot | 20 max | Transcript |
| Notification preference | Low-latency, all channels | Transcript |
| Incentive structure | $50 off for 7 questions | Transcript |
| Graceland commission | New structure enables incentives | Transcript |

---

## Risk of Proceeding Without Answers

| Unknown Category | Risk if Skipped | Recommendation |
|-----------------|-----------------|----------------|
| **MVP Budget** | May underprice or overprice | MUST RESOLVE before proposal |
| **SOT Processing** | Scope creep risk | Process with AI, extract MVP items only |
| **Website Access** | Implementation blocked | GET BEFORE KICKOFF |
| **Excel Dependencies** | Migration problems | Check in Week 1 |
| **Intake Form Questions** | Weak lead capture | Define in Dec 29 sync |
| **Slot Mapping Format** | QR design delayed | Get before QR build |

---

**Last Updated:** December 28, 2025 (Transcript Analysis Complete)
**Next Review:** December 29, 2025 6am sync
**Status:** Ready for follow-up discussion - significant progress from transcript analysis
