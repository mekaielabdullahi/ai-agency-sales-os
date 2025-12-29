# Product Requirements Document (PRD)
# PlotterOps Phase 1: Communication Control System

**Project:** Plotter Mechanix Quick Win Sprint
**Version:** 1.0
**Date:** December 28, 2025
**Author:** AriseGroup.ai
**Status:** Active Development

---

## 1. Executive Summary

### 1.1 Overview

PlotterOps Phase 1 is a communication control system that transforms Jobber into the trusted single source of truth for Plotter Mechanix. By automating the capture of all customer communications (calls, texts, emails), we eliminate the manual handoff processes that cause delays, information loss, and trust erosion.

### 1.2 Problem Statement

Plotter Mechanix, a $600K-$750K/year printer service company, suffers from critical communication chaos:

- **Trust Gap:** "My first instinct is not to go to Jobber... I don't fully trust that everything is in there"
- **Screenshot Bombing:** Text messages sent as screenshots, creating hours of delay
- **Phone Tag:** 4-6 daily handoff calls between Kelsey and Alyssa
- **Email Chaos:** 206 unread messages across 4 inboxes
- **Phone Number Confusion:** Customers confused by multiple business numbers

The root cause: **Manual steps between customer contact and Jobber create lag time, errors, and trust erosion.**

### 1.3 Solution Summary

Implement a unified communication system using:
1. **Quo** - Single business phone number with auto-sync to Jobber
2. **Email Automation** - N8N workflow to create Jobber Requests from emails
3. **Communication Protocols** - Standardized rules to maintain data integrity

### 1.4 Success Criteria

| Metric | Current State | Target |
|--------|---------------|--------|
| Communication in Jobber | Manual, delayed | 90%+ auto-captured within 5 min |
| Screenshot handoffs | Daily bombardment | Eliminated (0/week) |
| Phone call handoffs | 4-6/day | 1-2/day max |
| Email inbox unread | 206 | <20 |
| Alyssa manual entry | 1.5+ hrs/day | <30 min/day |

**Primary Success Test:** Kelsey checks Jobber first thing and trusts it has everything.

---

## 2. Background & Context

### 2.1 Client Profile

| Attribute | Value |
|-----------|-------|
| Company | Plotter Mechanix |
| Owner | Kelsey Andrade |
| Location | Phoenix, AZ Metro Area |
| Industry | Large Format Printer Service & Repair |
| Annual Revenue | $600,000 - $750,000 |
| Team Size | 3 employees + 1 technical consultant |
| Lead Source | Chris (AriseGroup partner) |

### 2.2 Team Structure

| Name | Role | Responsibilities |
|------|------|------------------|
| Kelsey | Owner/Lead Tech | ALL technical work, customer calls |
| Alyssa | Office Manager | Scheduling, invoicing, data entry |
| Joe | Tech in Training | Learning field work, social media |
| Mike | Consultant | Systems engineering, IT advisory |

### 2.3 Current Technology Stack

| Category | Tool | Status |
|----------|------|--------|
| Field Service Management | Jobber ($379/mo) | Primary CRM, underutilized |
| Accounting | QuickBooks | New system Jan 1, 2025 |
| E-commerce | Shopify | Website + POS |
| Business Phone | Vonage | To be replaced by Quo |
| Legacy CRM | Capsule ($30/mo) | Unused, still paying |
| Email | Microsoft 365/Outlook | Multiple inboxes |
| Document Storage | Google Drive/Dropbox | Consolidated recently |

### 2.4 Strategic Context

- **First project from Chris** - high-value partner with many leads
- **Previous failure:** $7,000 paid to Malik for failed API integration
- **Change fatigue:** Client needs to SEE results, not hear promises
- **Phase 2 opportunity:** $15K-$30K inventory/operations system

---

## 3. Problem Analysis

### 3.1 Communication Flow (Current State)

```
Customer Has Problem
        ↓
   [Where They Call]
   ↙    ↓    ↓    ↘
Cell  Office Jobber Email
(60%)  (30%)  (5%)  (5%)
  ↓      ↓     ↓      ↓
Kelsey Alyssa  ?   Ignored
  ↓      ↓
[Information Scatter]
        ↓
[Manual Consolidation Attempt]
        ↓
[Lost Information] → $10K/year lost
```

### 3.2 Pain Point Quantification

| Pain Point | Weekly Hours Lost | Revenue Impact |
|------------|-------------------|----------------|
| Kelsey-only technical work | 40+ | -$12K/week risk |
| Communication scatter | 5 | -$10K/year |
| No inventory tracking | 10 | -$3K/week |
| Manual invoicing | 5 | Cash flow delays |
| No training system | 20 | Can't scale |
| Commute time | 10 | -$3-4K/week |

**Total Weekly Impact:** 70+ hours of inefficiency

### 3.3 Root Cause Analysis

```
Kelsey doesn't trust Jobber
        ↑
Information is incomplete/delayed
        ↑
Manual data entry creates lag
        ↑
Screenshot bombing (texts → Alyssa → Jobber)
        ↑
Communication channels fragmented
        ↑
No unified phone system + email ignored
```

**Core Insight:** The manual handoff between customer contact and Jobber entry is the bottleneck. Eliminate manual steps = restore trust = Jobber becomes source of truth.

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
| FR-1.5 | Auto-create Jobber Request for unknown callers | Should Have | Testing |
| FR-1.6 | SMS sync between Quo and Jobber | Must Have | Testing |
| FR-1.7 | 5-option IVR replicating current Vonage setup | Must Have | Pending |
| FR-1.8 | Call routing by type (service, sales, supplies) | Should Have | Pending |

#### FR-2: Email Automation

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-2.1 | Monitor 4 email inboxes (service, sales, supplies, accounting) | Must Have | Pending |
| FR-2.2 | Auto-create Jobber Request from customer emails | Must Have | Pending |
| FR-2.3 | Spam filtering to prevent noise | Must Have | Pending |
| FR-2.4 | Parse email subject, body, sender, attachments | Should Have | Pending |
| FR-2.5 | Tag Requests by inbox source category | Should Have | Pending |
| FR-2.6 | Error logging for failed Request creation | Should Have | Pending |

#### FR-3: Standard Operating Procedures

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-3.1 | PM-FS-002: Service Call Execution SOP | Must Have | Pending |
| FR-3.2 | PM-OA-002: Invoice Queue Processing SOP | Must Have | Pending |
| FR-3.3 | PM-OA-003: Service Call Dispatch SOP | Must Have | Pending |
| FR-3.4 | PM-FS-005: End-of-Job Handoff Template | Must Have | Pending |
| FR-3.5 | Passive Knowledge Capture Workflow | Should Have | Pending |

#### FR-4: Communication Protocol

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-4.1 | "5 Rules" one-page document | Must Have | Pending |
| FR-4.2 | Rule 1: Everything Goes in Jobber | Must Have | Pending |
| FR-4.3 | Rule 2: Messages Must Be Actioned | Must Have | Pending |
| FR-4.4 | Rule 3: End-of-Job = Handoff Template | Must Have | Pending |
| FR-4.5 | Rule 4: New Leads = Jobber Entry + Notification | Must Have | Pending |
| FR-4.6 | Rule 5: Daily Check-Ins (4 PM, 5:30 PM) | Should Have | Pending |

### 4.2 Non-Functional Requirements

| ID | Requirement | Target | Priority |
|----|-------------|--------|----------|
| NFR-1 | Quo-Jobber sync reliability | >95% | Must Have |
| NFR-2 | Call transcript quality | Useful/actionable | Must Have |
| NFR-3 | Email automation accuracy | >80% real vs spam | Must Have |
| NFR-4 | System uptime | No major downtime | Must Have |
| NFR-5 | Mobile optimization | Works on iPhone | Must Have |
| NFR-6 | A2P 10DLC compliance | Registered | Must Have |

### 4.3 Integration Requirements

| System | Integration Type | Requirements |
|--------|-----------------|--------------|
| Quo | Native to Jobber | Call/SMS sync, Request creation |
| Jobber | API | Request creation, client lookup |
| Email (IMAP) | N8N webhook | Monitor 4 inboxes |
| Vonage | Port or Forward | Transfer 602-606-XXXX number |

---

## 5. User Stories

### 5.1 Kelsey (Owner/Lead Tech)

**US-1:** As Kelsey, I want all my calls and texts to automatically appear in Jobber, so I can trust Jobber has everything without manual entry.

**Acceptance Criteria:**
- [ ] All outbound calls show business number (not personal cell)
- [ ] Call summaries appear on Jobber client record within 5 minutes
- [ ] SMS conversations sync to Jobber
- [ ] No need to screenshot text conversations

**US-2:** As Kelsey, I want to check Jobber first thing in the morning and see all pending work, so I can plan my day without checking texts/email.

**Acceptance Criteria:**
- [ ] Jobber shows all new Requests from overnight
- [ ] Email inquiries appear as Requests
- [ ] No critical information stuck in email/text

### 5.2 Alyssa (Office Manager)

**US-3:** As Alyssa, I want customer communications to appear structured in Jobber, so I can create jobs and invoices without taking notes on sticky notes.

**Acceptance Criteria:**
- [ ] Call transcripts capture key details
- [ ] Email content parsed into Request notes
- [ ] Handoff template provides structured data
- [ ] 80% reduction in phone tag with Kelsey

**US-4:** As Alyssa, I want email inquiries to auto-create Jobber Requests, so I don't have to manually check 4 email inboxes.

**Acceptance Criteria:**
- [ ] Real customer emails become Requests
- [ ] Spam filtered out
- [ ] Inbox drops from 206 unread to <20

### 5.3 Joe (Tech in Training)

**US-5:** As Joe, I want clear SOPs for my assigned work, so I know exactly what to do without interrupting Kelsey.

**Acceptance Criteria:**
- [ ] Service call execution checklist available
- [ ] End-of-job handoff template guides my data entry
- [ ] My work shows up in Jobber schedule

---

## 6. Technical Architecture

### 6.1 System Diagram

```
[Customer Contact]
    ↓
┌───────────────────────────────────────────────┐
│                  QUO                           │
│  ┌──────────────────────────────────────────┐ │
│  │ Phone Calls    SMS Messages              │ │
│  │      ↓              ↓                    │ │
│  │ AI Transcription  Auto-Sync              │ │
│  └──────────────────────────────────────────┘ │
└───────────────────────────────────────────────┘
                     ↓
              [Quo-Jobber API]
                     ↓
┌───────────────────────────────────────────────┐
│                 JOBBER                         │
│  ┌──────────────────────────────────────────┐ │
│  │ Requests  │  Jobs  │  Clients  │  Notes  │ │
│  └──────────────────────────────────────────┘ │
└───────────────────────────────────────────────┘
                     ↑
              [N8N Webhook]
                     ↑
┌───────────────────────────────────────────────┐
│              EMAIL (IMAP)                      │
│  service@ │ sales@ │ supplies@ │ accounting@  │
└───────────────────────────────────────────────┘
```

### 6.2 Data Flow: Phone Call

```
1. Customer calls business number (Quo)
2. IVR routes to appropriate person
3. Call answered and completed
4. Quo AI transcribes call
5. Quo generates call summary
6. Quo API → Jobber
7. Summary attached to client record (or new Request if unknown)
8. Team can review in Jobber
```

### 6.3 Data Flow: Email

```
1. Customer sends email to service@plottermechanix.com
2. N8N monitors inbox (IMAP/webhook)
3. Spam filter checks sender/content
4. If valid: Parse subject, body, sender
5. Jobber API: Lookup client by email
6. If found: Create Request linked to client
7. If not found: Create new client + Request
8. Tag Request with source (service inbox)
9. Alyssa reviews and converts to Job
```

### 6.4 Technology Stack

| Component | Technology | Notes |
|-----------|-----------|-------|
| Phone System | Quo (formerly OpenPhone) | $69-99/mo for 3 users |
| CRM | Jobber | Existing, $379/mo |
| Automation | N8N | Self-hosted, $0 additional |
| Email Integration | IMAP / Gmail API | Native to N8N |
| SMS Compliance | A2P 10DLC | Required for business SMS |

---

## 7. Implementation Plan

### 7.1 Timeline

| Week | Phase | Deliverables |
|------|-------|-------------|
| Week 1 | Testing & Validation | Answer 10 critical questions, GO/NO-GO decision |
| Week 2 | Quo Configuration | IVR setup, iOS apps, A2P registration |
| Week 3 | Email Automation | N8N workflow, spam filtering, testing |
| Week 4 | Go-Live & Refinement | Number transition, monitoring, tuning |
| Ongoing | SOPs & Documentation | 4 SOPs, Communication Protocol, Training Videos |

### 7.2 Week 1: Testing & Validation (Dec 23-30)

**Critical Questions to Answer:**

1. Does Quo SMS sync to Jobber well enough to replace screenshot bombing?
2. Does iOS default calling app work reliably?
3. What's the quality of Quo call transcripts?
4. Does auto-Request creation work for unknown callers?
5. What's the spam-to-real email ratio?
6. Can we reliably filter spam?
7. How long does A2P 10DLC registration take?
8. What's the current Vonage cost (to calculate savings)?
9. Will team adopt the new workflow?
10. Is Jobber texting feature redundant with Quo?

**GO/NO-GO Decision Criteria:**
- [ ] Quo-Jobber sync works as promised (>90% reliability)
- [ ] iOS default calling app functions correctly
- [ ] Call transcripts are actionable quality
- [ ] Team comfortable with new workflow

### 7.3 Week 2: Quo Configuration (Dec 30 - Jan 6)

| Task | Owner | Status |
|------|-------|--------|
| Configure 5-option IVR | Matthew | ☐ |
| Install Quo on Kelsey's iPhone | Kelsey | ☐ |
| Install Quo on Alyssa's iPhone | Alyssa | ☐ |
| Install Quo on Joe's iPhone | Joe | ☐ |
| Set as default calling app (all 3) | Team | ☐ |
| Submit A2P 10DLC registration | Matthew | ☐ |
| Team training on Quo app | Matthew | ☐ |

### 7.4 Week 3: Email Automation (Jan 6-13)

| Task | Owner | Status |
|------|-------|--------|
| Analyze email volume/spam patterns | Matthew | ☐ |
| Build N8N email monitoring workflow | Dev | ☐ |
| Implement spam filtering rules | Dev | ☐ |
| Test Request creation accuracy | Matthew | ☐ |
| Train Alyssa on reviewing auto-Requests | Matthew | ☐ |

### 7.5 Week 4: Go-Live (Jan 13-20)

| Task | Owner | Status |
|------|-------|--------|
| Port Vonage number to Quo (or forward) | Matthew | ☐ |
| Enable email automation (monitored) | Dev | ☐ |
| Daily check-ins with team | Matthew | ☐ |
| Document edge cases | Team | ☐ |
| Tune settings based on usage | Dev | ☐ |
| Baseline 30-day success metrics | Matthew | ☐ |

---

## 8. Success Metrics

### 8.1 Quantitative Metrics

| Metric | Baseline | Week 2 | Week 4 | 30-Day |
|--------|----------|--------|--------|--------|
| % Communication auto-captured | 0% | 50% | 80% | 90%+ |
| Screenshot handoffs/week | 20+ | 10 | 2 | 0 |
| Phone call handoffs/day | 4-6 | 3-4 | 2 | 1-2 |
| Email inbox unread | 206 | 150 | 50 | <20 |
| Alyssa manual entry (hrs/day) | 1.5+ | 1.0 | 0.5 | <0.5 |
| Quo-Jobber sync reliability | - | 85% | 90% | 95%+ |

### 8.2 Qualitative Metrics

| Stakeholder | Success Statement | Validated? |
|-------------|-------------------|------------|
| Kelsey | "I trust Jobber has everything" | ☐ |
| Kelsey | "My first instinct is to check Jobber" | ☐ |
| Alyssa | "Morning routine is faster, less chaotic" | ☐ |
| Joe | "I know where to check for my jobs" | ☐ |
| Customers | No confusion about phone numbers | ☐ |

### 8.3 ROI Calculation

**Time Savings:**
- Alyssa: 1.5 hrs/day × 20 days = 30 hrs/mo @ $25/hr = **$750/mo**
- Kelsey: 0.5 hrs/day × 20 days = 10 hrs/mo @ $100/hr = **$1,000/mo**
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
| Email spam creates noise | Medium | Medium | Conservative filtering; Alyssa review process |
| Team overwhelm | Medium | Medium | Train incrementally; one feature at a time |
| Previous vendor PTSD | High | Medium | Fixed price; concrete deliverables; guarantee |

---

## 10. Out of Scope (Phase 2+)

| Feature | Reason | Phase |
|---------|--------|-------|
| Inventory Management | Complexity, needs foundation | Phase 2 |
| QuickBooks Integration | New system Jan 1, needs stabilization | Phase 2 |
| Automated Quote Generation | Requires inventory + pricing | Phase 2 |
| Full SOP Library (equipment-specific) | Time-intensive | Phase 2 |
| Unified Operations Dashboard | Build on Phase 1 foundation | Phase 2 |
| Multi-Technician Operations | Scale readiness | Phase 3 |
| Customer Portal | Self-service | Phase 3 |
| PlotterOps Product | Industry SaaS | Phase 4+ |

---

## 11. Guarantee

> "If by day 30 you don't feel you have substantially more clarity and at least one live change that makes your day easier, we keep working until you do."

**Comparison to Previous Vendor (Malik):**

| Malik | AriseGroup |
|-------|------------|
| Weekly rate, no end | Fixed $5,000, 30 days |
| Word salad promises | Concrete deliverables |
| Changed website without communication | Test environment first |
| Made things worse | Build on what works |
| No accountability | Free work until satisfied |

---

## 12. Appendices

### A. Access Requirements Checklist

**Immediate (Week 1):**
- [x] Quo account created
- [x] Matthew has Quo access
- [x] Matthew has Jobber access
- [ ] Vonage account number (for porting)

**Later (Week 2-3):**
- [ ] Email credentials (4 inboxes)
- [ ] A2P registration info (EIN, legal name)

**Phase 2 Prep:**
- [ ] Plotter training videos
- [ ] Capsule CRM access
- [ ] QuickBooks access (after Jan 1)

### B. Related Documentation

- [Client Intake Form](./client-intake-form-filled.md)
- [Overall Roadmap](./deliverables/overall-roadmap.md)
- [Phase 1 Detailed Plan](./deliverables/phase-1-quick-win-sprint.md)
- [Option 4c Technical Spec](./deliverables/option-4c-recommended-approach.md)
- [Week 1 Testing Checklist](./deliverables/week-1-testing-checklist.md)
- [Process Map](./audit/process-map.md)
- [Discovery Findings](./discovery/DISCOVERY-FINDINGS.md)

### C. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-28 | AriseGroup.ai | Initial PRD created from project documentation |

---

**Document Owner:** AriseGroup.ai
**Last Updated:** December 28, 2025
**Next Review:** End of Week 1 Testing (Dec 30, 2025)

---

*This PRD is a living document. Requirements will be refined based on Week 1 testing results and ongoing discovery.*
