# Product Requirements Document (PRD)
# PlotterOps Phase 1: Communication Control System

**Project:** Plotter Mechanix Quick Win Sprint
**Version:** 1.1
**Date:** January 5, 2026
**Author:** AriseGroup.ai
**Status:** Active Development

---

## 1. Executive Summary

### 1.1 Overview

PlotterOps Phase 1 is a communication control system that transforms Jobber into the trusted single source of truth for Plotter Mechanix. By automating the capture of all customer communications (calls, texts), we eliminate the manual handoff processes that cause delays, information loss, and trust erosion.

### 1.2 Problem Statement

Plotter Mechanix, a $600K-$750K/year printer service company, suffers from critical communication chaos:

- **Trust Gap:** "My first instinct is not to go to Jobber... I don't fully trust that everything is in there"
- **Screenshot Bombing:** Text messages sent as screenshots, creating hours of delay
- **Phone Tag:** 4-6 daily handoff calls between Kelsey and Alyssa
- **Phone Number Confusion:** Customers confused by multiple business numbers

**Root Cause:** Manual steps between customer contact and Jobber create lag time, errors, and trust erosion.

### 1.3 Investment & Timeline

| Attribute | Value |
|-----------|-------|
| Investment | $5,000 (fixed) |
| Timeline | 30 days |
| Target Delivery | 2 weeks for core functionality |

---

## 2. Use Cases (Problems)

### UC-1: Internal Handoffs (Kelsey → Alyssa)

**Current State:**
- Kelsey calls Alyssa 4-6x/day after completing jobs
- Calls are synchronous — interrupts both people
- Alyssa captures info on sticky notes
- Info can get lost between call and Jobber entry
- Delayed Jobber updates erode trust in the system

**Pain Quantification:**
- 4-6 interruptions/day
- ~30+ minutes/day lost to phone tag
- Information loss leads to billing errors, missed follow-ups

**User Quote:**
> "Every day multiple things come in. Kelsey communicates to Alyssa... she takes notes on that call, then she'll go update Jobber. But some of the stuff will get missed and then they'll be back and forth."

---

### UC-2: Initial Client Calls to Kelsey

**Current State:**
- Customer calls Kelsey directly (often on personal cell)
- Kelsey is in the field, can't immediately enter details
- Details need manual Jobber entry later
- Time lag between call and entry = info loss risk

**Pain Quantification:**
- Every new client call requires manual entry
- Kelsey's time in field is too valuable for data entry
- Leads can fall through the cracks

**User Quote:**
> "They're all confused. They're like, dude, you got this number, that number, this other number"

---

### UC-3: Follow-up Client Calls to Kelsey

**Current State:**
- Existing clients call back with updates, questions, or new requests
- Same issues as UC-2: manual entry, time delays, info loss
- Context scattered across previous interactions
- No single view of client communication history

**Pain Quantification:**
- Repeat calls for same issue due to lost context
- Customer frustration when they have to repeat themselves
- Kelsey's mental load tracking conversations

---

## 3. Solution Summary

### 3.1 Core Approach

Implement **Quo** as the unified phone system to:
1. Consolidate all business calls to a single number
2. Auto-transcribe calls with AI summaries
3. Auto-sync call data to Jobber client records
4. Enable async handoffs via voicemail transcription

### 3.2 Phone Number Architecture (Phase 1)

| # | Number | Purpose | Owner |
|---|--------|---------|-------|
| 1 | Kelsey's Quo Line | Incoming client calls, outbound calls show business number | Kelsey |
| 2 | Voicemail-Only Quo Line | Async updates from Kelsey → auto-transcribe → Jobber Request | Kelsey (internal use) |
| 3 | Alyssa's Quo Line | TBD - depends on whether she takes client calls | Alyssa |
| 4 | Nikki | Probably not needed if no client calls | - |

### 3.3 How Each Use Case is Solved

| Use Case | Current | Solution | Outcome |
|----------|---------|----------|---------|
| UC-1: Internal Handoffs | 4-6 calls/day, sticky notes | Voicemail-only line → auto-transcribe → Jobber Request | Async, no interruptions, structured data |
| UC-2: Initial Client Calls | Manual entry, delays | Quo auto-transcribes + syncs to Jobber | Instant capture, no manual entry |
| UC-3: Follow-up Calls | Scattered context | All calls logged to client record in Jobber | Full history in one place |

### 3.4 Key Quo Features

| Feature | What It Does | Use Case Solved |
|---------|--------------|-----------------|
| Single Business Number | One number for all outbound calls | UC-2, UC-3 |
| iOS Default Calling App | Team calls from business number via personal phones | UC-2, UC-3 |
| Auto-sync to Jobber | Calls/texts → Jobber Requests/notes | UC-1, UC-2, UC-3 |
| AI Call Summaries | Auto-transcribe calls | UC-1, UC-2, UC-3 |
| Voicemail Transcription | Async messages auto-transcribed | UC-1 (handoffs) |
| Unknown Caller Handling | Auto-create Requests for new callers | UC-2 |

---

## 4. Requirements

### 4.1 Functional Requirements

#### FR-1: Unified Phone System (Quo)

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-1.1 | Single business phone number for all outbound calls | Must Have | Pending |
| FR-1.2 | iOS default calling app shows business number | Must Have | Testing |
| FR-1.3 | Auto-transcribe all inbound/outbound calls | Must Have | Testing |
| FR-1.4 | Auto-sync call summaries to Jobber client records | Must Have | Testing |
| FR-1.5 | Auto-create Jobber Request for unknown callers | Must Have | Testing |
| FR-1.6 | SMS sync between Quo and Jobber | Must Have | Testing |
| FR-1.7 | 5-option IVR replicating current Vonage setup | Must Have | Pending |
| FR-1.8 | Voicemail-only line for async handoffs | Should Have | Pending |

#### FR-2: Standard Operating Procedures

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-2.1 | PM-FS-002: Service Call Execution SOP | Must Have | Pending |
| FR-2.2 | PM-OA-002: Invoice Queue Processing SOP | Must Have | Pending |
| FR-2.3 | PM-OA-003: Service Call Dispatch SOP | Must Have | Pending |
| FR-2.4 | PM-FS-005: End-of-Job Handoff Template | Must Have | Pending |

#### FR-3: Communication Protocol

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-3.1 | "5 Rules" one-page document | Must Have | Pending |
| FR-3.2 | Rule 1: Everything Goes in Jobber | Must Have | Pending |
| FR-3.3 | Rule 2: Messages Must Be Actioned | Must Have | Pending |
| FR-3.4 | Rule 3: End-of-Job = Handoff Template | Must Have | Pending |
| FR-3.5 | Rule 4: New Leads = Jobber Entry + Notification | Must Have | Pending |
| FR-3.6 | Rule 5: Daily Check-Ins (4 PM, 5:30 PM) | Should Have | Pending |

### 4.2 Non-Functional Requirements

| ID | Requirement | Target | Priority |
|----|-------------|--------|----------|
| NFR-1 | Quo-Jobber sync reliability | >95% | Must Have |
| NFR-2 | Call transcript quality | Useful/actionable | Must Have |
| NFR-3 | System uptime | No major downtime | Must Have |
| NFR-4 | Mobile optimization | Works on iPhone | Must Have |
| NFR-5 | A2P 10DLC compliance | Registered | Must Have |

---

## 5. Deprioritized / Phase 2

### 5.1 Email Automation (DEPRIORITIZED)

**Original Plan:** N8N workflow to auto-create Jobber Requests from emails

**Why Deprioritized:**
- Kelsey already ignores email: "I just don't look at the emails anymore"
- 206 unread messages suggests email is not the active communication channel
- Automating ignored channel may add noise to Jobber without solving felt pain
- Phone/SMS is where real customer communication happens

**Recommendation:** Revisit in Phase 2 after phone system proves value. May be more valuable once team trusts Jobber as source of truth.

### 5.2 Other Phase 2+ Items

| Feature | Reason | Phase |
|---------|--------|-------|
| Email → Jobber Automation | Lower priority than phone | Phase 2 |
| Inventory Management | Complexity, needs foundation | Phase 2 |
| QuickBooks Integration | New system Jan 1, needs stabilization | Phase 2 |
| Automated Quote Generation | Requires inventory + pricing | Phase 2 |
| Customer Portal | Self-service | Phase 3 |

---

## 6. User Stories

### 6.1 Kelsey (Owner/Lead Tech)

**US-1:** As Kelsey, I want all my calls and texts to automatically appear in Jobber, so I can trust Jobber has everything without manual entry.

**Acceptance Criteria:**
- [ ] All outbound calls show business number (not personal cell)
- [ ] Call summaries appear on Jobber client record within 5 minutes
- [ ] SMS conversations sync to Jobber
- [ ] No need to screenshot text conversations

**US-2:** As Kelsey, I want to leave a voicemail for Alyssa that automatically becomes a Jobber Request, so I don't have to call her and interrupt her work.

**Acceptance Criteria:**
- [ ] Voicemail-only line available
- [ ] Voicemail auto-transcribed
- [ ] Transcription creates Jobber Request with details
- [ ] Alyssa can process from Jobber queue

### 6.2 Alyssa (Office Manager)

**US-3:** As Alyssa, I want customer communications to appear structured in Jobber, so I can create jobs and invoices without taking notes on sticky notes.

**Acceptance Criteria:**
- [ ] Call transcripts capture key details
- [ ] Handoff template provides structured data
- [ ] 80% reduction in phone tag with Kelsey

**US-4:** As Alyssa, I want Kelsey's job updates to appear in Jobber automatically, so I don't have to take calls while I'm working on invoices.

**Acceptance Criteria:**
- [ ] Voicemail updates create Requests I can process
- [ ] No more sticky notes
- [ ] Can work async on my schedule

### 6.3 Joe (Tech in Training)

**US-5:** As Joe, I want clear SOPs for my assigned work, so I know exactly what to do without interrupting Kelsey.

**Acceptance Criteria:**
- [ ] Service call execution checklist available
- [ ] End-of-job handoff template guides my data entry
- [ ] My work shows up in Jobber schedule

---

## 7. Implementation Plan

### 7.1 Timeline

| Week | Phase | Deliverables |
|------|-------|--------------|
| Week 1 | Testing & Validation | Answer critical questions, GO/NO-GO decision |
| Week 2 | Quo Configuration | IVR setup, iOS apps, A2P registration |
| Week 3 | Voicemail Handoff Setup | Configure async handoff workflow |
| Week 4 | Go-Live & Refinement | Number transition, monitoring, tuning |
| Ongoing | SOPs & Documentation | 4 SOPs, Communication Protocol, Training |

### 7.2 Week 1: Critical Questions

1. Does Quo SMS sync to Jobber well enough to replace screenshot bombing?
2. Does iOS default calling app work reliably?
3. What's the quality of Quo call transcripts?
4. Does auto-Request creation work for unknown callers?
5. Can voicemail transcription quality support async handoffs?
6. How long does A2P 10DLC registration take?
7. What's the current Vonage cost (to calculate savings)?
8. Will team adopt the new workflow?

**GO/NO-GO Criteria:**
- [ ] Quo-Jobber sync works as promised (>90% reliability)
- [ ] iOS default calling app functions correctly
- [ ] Call transcripts are actionable quality
- [ ] Team comfortable with new workflow

---

## 8. Success Metrics

### 8.1 Quantitative Metrics

| Metric | Baseline | Week 2 | Week 4 | 30-Day |
|--------|----------|--------|--------|--------|
| % Communication auto-captured | 0% | 50% | 80% | 90%+ |
| Screenshot handoffs/week | 20+ | 10 | 2 | 0 |
| Phone call handoffs/day | 4-6 | 3-4 | 2 | 1-2 |
| Alyssa manual entry (hrs/day) | 1.5+ | 1.0 | 0.5 | <0.5 |
| Quo-Jobber sync reliability | - | 85% | 90% | 95%+ |

### 8.2 Qualitative Metrics

| Stakeholder | Success Statement | Validated? |
|-------------|-------------------|------------|
| Kelsey | "I trust Jobber has everything" | ☐ |
| Kelsey | "My first instinct is to check Jobber" | ☐ |
| Alyssa | "Morning routine is faster, less chaotic" | ☐ |
| Alyssa | "I don't get interrupted by handoff calls anymore" | ☐ |
| Customers | No confusion about phone numbers | ☐ |

### 8.3 ROI Calculation

**Time Savings:**
- Alyssa: 1.5 hrs/day × 20 days = 30 hrs/mo @ $25/hr = $750/mo
- Kelsey: 0.5 hrs/day × 20 days = 10 hrs/mo @ $100/hr = $1,000/mo
- **Total Monthly Value: $1,750**

**Cost:**
- Quo: +$69-99/mo
- Vonage: -$XX/mo (eliminated)
- N8N: $0
- **Net Cost: ~$70-100/mo**

**ROI: 17-25x return on investment**

---

## 9. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Number porting delays | Medium | High | Start A2P early; test in demo; forwarding fallback |
| Quo adoption resistance | Medium | High | Demo AI summaries wow factor; incremental training |
| Jobber API limitations | Low | Medium | Research API Day 1; polling fallback ready |
| Team overwhelm | Medium | Medium | Train incrementally; one feature at a time |
| Previous vendor PTSD | High | Medium | Fixed price; concrete deliverables; guarantee |

---

## 10. Guarantee

> "If by day 30 you don't feel you have substantially more clarity and at least one live change that makes your day easier, we keep working until you do."

| Malik (Previous) | AriseGroup |
|------------------|------------|
| Weekly rate, no end | Fixed $5,000, 30 days |
| Word salad promises | Concrete deliverables |
| Changed website without communication | Test environment first |
| Made things worse | Build on what works |
| No accountability | Free work until satisfied |

---

## 11. Open Questions

1. **Voicemail-only line:** Is this higher ROI than email automation for solving UC-1?
2. **Alyssa's phone:** Does she need her own Quo line, or just access to view calls/transcripts?
3. **Nikki:** Confirm she doesn't take client calls (no Quo line needed)
4. **IVR options:** What are the current 5 Vonage IVR options to replicate?

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-28 | AriseGroup.ai | Initial PRD created |
| 1.1 | 2026-01-05 | AriseGroup.ai | Restructured around use cases; deprioritized email automation; added voicemail-only handoff option |

---

*This PRD is a living document. Requirements will be refined based on Week 1 testing results and ongoing discovery.*
