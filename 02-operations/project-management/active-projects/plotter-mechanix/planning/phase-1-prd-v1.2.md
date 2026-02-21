# Product Requirements Document (PRD)
# PlotterOps Phase 1: Communication Control System

**Project:** Plotter Mechanix Quick Win Sprint
**Version:** 1.2
**Date:** January 15, 2026
**Author:** AriseGroup.ai
**Status:** Active Development

---

## 1. Executive Summary

### 1.1 Overview

PlotterOps Phase 1 is a communication control system that transforms Jobber into the trusted single source of truth for Plotter Mechanix. By automating the capture of all customer communications (calls, texts, voicemails), we eliminate the manual handoff processes that cause delays, information loss, and trust erosion.

### 1.2 Problem Statement

Plotter Mechanix, a $600K-$750K/year printer service company, suffers from critical communication chaos:

- **Trust Gap:** "My first instinct is not to go to Jobber... I don't fully trust that everything is in there"
- **Screenshot Bombing:** Text messages sent as screenshots, creating hours of delay
- **Phone Tag:** 4-6 daily handoff calls between Kelsey and Alyssa
- **Data Loss Risk:** Alyssa may be deleting Requests after conversion, losing call history
- **Phone Number Confusion:** Customers confused by multiple business numbers (Vonage + Kelsey's cell)

**The root cause:** Manual steps between customer contact and Jobber create lag time, errors, and trust erosion.

### 1.3 Current State (As of Jan 15, 2026)

| Component | Status | Notes |
|-----------|--------|-------|
| Quo Phone System | Live | Kelsey receiving calls, ~20 calls/day |
| N8N Workflow | Deployed | Quo → Jobber Request automation active |
| Native Quo-Jobber | Insufficient | Shows phone numbers in brackets, no names, no voicemails |
| Vonage | Decommissioning | Only 8 calls in 3 months, number port in progress |
| Alyssa SOP | Complete | Request processing workflow documented |

---

## 2. Phase 1 Requirements

### 2.1 Priority 1 (P1) - MUST DELIVER

These are the core deliverables that define Phase 1 success.

#### P1.1: Quo-to-Jobber Parity Plus

**Goal:** Match native Quo-Jobber integration capabilities, then exceed them.

| Requirement | Native Quo | Our Solution | Status |
|------------|------------|--------------|--------|
| Call transcripts in Jobber | Yes | Yes | ✅ Working |
| Contact names (not just phone numbers) | NO - shows brackets | Extract from transcript via AI | 🔄 In Progress |
| Voicemail capture | NO | Capture and transcribe | 📋 Planned |
| Text message capture | NO | Capture message content | 📋 Planned |
| Call history preserved on conversion | User error prone | SOP + workflow safeguards | ✅ SOP Complete |
| Equipment/printer model extraction | NO | Extract from transcript via AI | 📋 Planned |

**Success Criteria:**
- Contact names properly assigned (not "[480-555-1234]")
- Voicemails captured and transcribed to Jobber
- Text messages logged to Jobber
- Call history preserved when Requests → Jobs/Quotes

#### P1.2: AI-Enhanced Call Summaries

**Goal:** Provide actionable call summaries that save Alyssa time.

| Feature | Description | Status |
|---------|-------------|--------|
| Call Summary | 2-3 sentence overview of what was discussed | 🔄 Testing |
| Next Steps | Action items mentioned on the call | 📋 Planned |
| Equipment Mentioned | Printer/plotter models discussed | 📋 Planned |
| Caller Info | Name, company, address if mentioned | 🔄 Testing |
| Urgency Detection | Flag urgent equipment failures | 📋 Planned |

**Technical Implementation:**
- Gemini API integration for transcript summarization
- HTTP Request node → Gemini Agent node swap (pending)
- Accuracy target: 97%+ (if <97%, Alyssa double-checks every recording anyway)

#### P1.3: Operational SOP Documentation

**Goal:** Document current workflows to prevent data loss and enable handoff.

| SOP | Purpose | Status |
|-----|---------|--------|
| Alyssa Request Processing | How to handle Quo-generated Requests | ✅ Complete |
| Kelsey Call Routing | Interim call flow until lines ported | 📋 Planned |
| RMA Process | Parts return procedure (from Alyssa interview) | 📋 Deferred |

---

### 2.2 Priority 2 (P2) - SHOULD DELIVER

These enhance the core solution but are not blockers for Phase 1 completion.

#### P2.1: Multi-Call Deduplication

**Goal:** Automatically group multiple calls from same customer.

| Scenario | Current Behavior | Target Behavior |
|----------|-----------------|-----------------|
| Customer calls twice before Request processed | Creates 2 Requests | Adds note to existing open Request |
| Same phone, different contact | May create duplicate client | Prompt for verification |

**Logic:** Search for open Requests matching phone number before creating new one.

**Status:** Logic implemented, needs production testing.

#### P2.2: Daily Summary Slack Notifications

**Goal:** Team visibility into daily call volume.

| Feature | Description | Status |
|---------|-------------|--------|
| Daily Digest | Posts to Slack at 6 PM EST | ✅ Working |
| Metrics | Total transcripts, unique callers | ✅ Working |
| Error Alerts | Notification on workflow failures | ✅ Working |

---

### 2.3 Priority 3 (P3) - NICE TO HAVE

These can be added if time permits or carried to Phase 2.

#### P3.1: Webhook Security

- Implement webhook secret validation
- Currently disabled (no authentication on incoming webhooks)
- Risk: Low (internal system, not exposed)

#### P3.2: Data Retention Policy

- 30-day log cleanup currently implemented
- Need formal policy discussion before handoff
- Consider compliance/audit requirements

---

## 3. Deferred to Phase 2+

These requirements have been explicitly scoped OUT of Phase 1.

### 3.1 Kelsey Outbound Calls → Capsule

**Source:** Kelsey request during Jan 14 meeting

Kelsey wants outbound calls from Quo to sync to Capsule (CRM). This requires:
- Capsule API integration
- Outbound call event handling
- CRM record matching/creation

**Rationale for Deferral:** Different integration path, not core to Jobber trust goal.

### 3.2 Phone Menu (IVR) System

**Source:** Jan 14 meeting

Full phone menu/IVR replication from Vonage to Quo.

**Rationale for Deferral:**
- Requires all lines (Kelsey, Alyssa, Joe) set up in Quo first
- Number port must complete
- Current interim routing (4 rings → Alyssa) working

### 3.3 Additional Phone Lines (Alyssa/Joe)

**Source:** Jan 14 meeting

Set up dedicated Quo lines for Alyssa and Joe.

**Rationale for Deferral:**
- Depends on number port completion
- Training required
- Not blocking core Quo-Jobber workflow

### 3.4 Email-to-Jobber Automation

**Source:** Original PRD v1.0

N8N workflow to create Jobber Requests from emails.

**Rationale for Deferral:**
- Alyssa manages 10 inboxes manually (working, just inefficient)
- Phone/call automation higher priority
- Can add after phone workflow stabilized

### 3.5 Voice-to-Ticket (Mobile Recording)

**Source:** Original Phase 1 README

Kelsey records voice notes → transcribed → Jobber ticket.

**Rationale for Deferral:**
- Quo already captures calls automatically
- Voicemail feature covers async updates
- Reduced need if Quo-Jobber working well

### 3.6 Customer Status Bot

**Source:** Original Phase 1 README

SMS auto-responder with Jobber status lookup.

**Rationale for Deferral:**
- Separate project scope
- Requires Twilio integration
- Not related to communication capture goal

### 3.7 Inventory Management System

**Source:** Jan 14 meeting, Nikki interview

Track ~$50k in inventory (parts, consumables, used equipment).

**Rationale for Deferral:**
- Phase 2 project ($15K-$30K scope)
- Kelsey evaluating "Ply" software
- Different problem domain

### 3.8 Video Repair Library / Knowledge Monetization

**Source:** Nikki interview

Create video library of repairs for passive revenue.

**Rationale for Deferral:**
- Long-term strategy, not quick win
- Requires content production infrastructure
- Phase 3+ consideration

---

## 4. Technical Architecture

### 4.1 Current N8N Workflow

```
Quo Webhook → Parse Event → Log to Table
                              ↓
                    Clean logs >30 days
                              ↓
                    If transcript:
                              ↓
              Extract contact → Search Jobber
                              ↓
                    Client exists?
                     ↓         ↓
                   Yes         No
                     ↓         ↓
              Get client ID   Create client
                     ↓         ↓
                     └────┬────┘
                          ↓
              Search open Requests by phone
                          ↓
              [NEW] Generate AI Summary (Gemini)
                          ↓
              Request exists?
               ↓           ↓
              Yes          No
               ↓           ↓
         Add note     Create Request
```

### 4.2 Quo Configuration

| Setting | Value | Notes |
|---------|-------|-------|
| Sona AI | DISABLED | Saves credits (100 per Sona call) |
| Allow Overages | OFF | Won't charge beyond 1000 credits |
| Webhook Events | transcript, summary, message_received, message_delivered | |
| Not Using | completed, ringing, recording | Future: routing decisions |

### 4.3 Integration Points

| System | Integration | Purpose |
|--------|-------------|---------|
| Quo | Webhook (no auth) | Receive call events |
| Jobber | GraphQL API | Client/Request CRUD |
| Gemini | API | Transcript summarization |
| Slack | Webhook | Notifications |

---

## 5. Success Criteria

### 5.1 Functional Success (Must Pass)

| Test | Pass Criteria |
|------|---------------|
| New caller creates Request | Request appears in Jobber <5 min |
| Existing client call updates record | Note added to client, Request created |
| Contact name extraction | Name in Request, not "[phone number]" |
| Voicemail capture | Voicemail transcribed to Request |
| Text message capture | SMS content logged to Request |
| Request conversion | Call history preserved after → Job |

### 5.2 Operational Success (Target Metrics)

| Metric | Current State | Target |
|--------|---------------|--------|
| Communication in Jobber | Manual, delayed | 90%+ auto-captured |
| Alyssa manual entry time | 1.5+ hrs/day | <30 min/day |
| Kelsey→Alyssa handoff calls | 4-6/day | 1-2/day max |
| AI summary accuracy | N/A | 97%+ |

### 5.3 Primary Success Test

**Kelsey checks Jobber first thing and trusts it has everything.**

---

## 6. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| AI name extraction <97% accuracy | Alyssa double-checks every call | Medium | Tune prompts, fall back to phone number |
| Webhook failures undetected | Lost call data | Low | Slack error alerts, Quo event replay |
| Alyssa deletes Requests | Lost call history | Medium | SOP training, workflow education |
| Quo credits exhausted | No call capture | Low | Disabled Sona, monitoring usage |
| Number port delays | Continued Vonage dependency | Medium | Interim routing working |

---

## 7. Open Questions

| Question | Owner | Status |
|----------|-------|--------|
| Data retention policy (30-day cleanup) | Matt/Trent | Needs discussion before handoff |
| Webhook authentication priority | Trent | Low priority, deferred |
| Gemini vs OpenAI for summaries | Trent | Testing Gemini first |
| Kelsey direct line training | Matt | Pending Alyssa/Joe setup |

---

## 8. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-28 | AriseGroup.ai | Initial PRD created |
| 1.1 | 2026-01-10 | AriseGroup.ai | Added Key Use Cases, Scope Consideration |
| 1.2 | 2026-01-15 | AriseGroup.ai | **Major Update:** Restructured around Priority tiers (P1/P2/P3), added comprehensive Deferred section, incorporated Jan 14 + Jan 15 meeting insights, added current state assessment, technical architecture details, updated success criteria with specific tests |

---

## 9. Related Documents

| Document | Location | Purpose |
|----------|----------|---------|
| Alyssa Request Processing SOP | `/plotter-mechanix/deliverables/phase-1/sops/alyssa-quo-jobber-request-processing.md` | Operational workflow |
| Jan 15 Internal Meeting | `/ai-agency-development-os/.../meetings/internal/2026-01-15/summary.md` | Technical decisions |
| Jan 14 Deep Dive Meeting | `/ai-agency-development-os/.../meetings/2026-01-14-andrew-kelsey-deep-dive/summary.md` | Stakeholder alignment |
| Alyssa Interview | `/ai-agency-development-os/.../audit/stakeholder-interviews/alyssa/summary.md` | Operational pain points |
| Nikki Interview | `/ai-agency-development-os/.../audit/stakeholder-interviews/nikki/summary.md` | Strategic context |

---

**Document Owner:** AriseGroup.ai
**Last Updated:** January 15, 2026
**Next Review:** End of Phase 1 delivery

*This PRD is a living document. Requirements will be refined based on testing results and stakeholder feedback.*
