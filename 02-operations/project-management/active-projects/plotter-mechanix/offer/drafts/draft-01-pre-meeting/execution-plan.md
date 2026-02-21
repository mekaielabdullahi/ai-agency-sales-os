# PlotterOps Quick Win Sprint: Execution Plan

**Client:** Plotter Mechanix
**Timeline:** 2 weeks active + 30-day support buffer
**Investment:** $5,000
**New Tool Cost to Client:** ~$69/month (Quo, 3 users billed annually) or ~$99/month (billed monthly)

---

## Executive Summary

| Item | Details |
|------|---------|
| **Approach** | Jobber + Quo as unified communication hub + passive SOP capture |
| **Core Problem** | Fragmented communication costing ~$20K/year in lost time and missed opportunities |
| **Solution** | Centralized phone system (Quo) + protocols + automation + training |
| **Deliverables** | 4 SOPs + Communication Protocol + 3 Automations + Quo Setup + Blueprint |

---

## Team Assignment

| Role | Person | Responsibilities |
|------|--------|------------------|
| **Client-Facing #1** | TBD | Ride-along, SOP finalization, training delivery, passive SOP capture setup |
| **Client-Facing #2** | TBD | Communication protocol, training videos, client check-ins |
| **Developer #1** | TBD | n8n workflows (all 3 automations), Quo webhook integration |
| **Developer #2** | TBD | Jobber API integration, Quo setup, testing, deployment |

---

## Pre-Sprint Setup (Before Day 1)

**Start these IMMEDIATELY - some have long lead times.**

| Task | Owner | Notes | Status |
|------|-------|-------|--------|
| Quo account signup | Client | Business plan ($23/user/mo billed annually, or $33/mo billed monthly) | ☐ |
| **Start A2P 10DLC registration** | Client + Dev #2 | **Takes 5-30 days; start ASAP** | ☐ |
| Port existing business number (optional) | Client | Or use new Quo number | ☐ |
| Enable Jobber integration in Quo | Dev #2 | Native integration, one-click (requires Jobber Core plan or higher) | ☐ |
| Create shared Google Drive folder | Client-Facing #1 | For passive SOP recordings | ☐ |
| Get Jobber API credentials | Client | Developer access needed | ☐ |

**Critical:** A2P 10DLC registration is required for SMS and can take up to 30 days. Phone calls work immediately; SMS may be delayed until registration completes.

---

## Week 1: Discovery + Build

| Day | Activity | Owner | Deliverable | Status |
|-----|----------|-------|-------------|--------|
| 1 | Kick-off call, get Jobber API + Quo credentials | Client-facing | Access confirmed | ☐ |
| 1-2 | Ride-along / shadow session + passive SOP capture demo | Client-facing #1 | Validation notes, first recording | ☐ |
| 2-3 | Finalize 4 SOP documents | Client-facing #1 | 4 Google Docs | ☐ |
| 2-3 | Design handoff template in Jobber | Client-facing #2 | Template ready | ☐ |
| 2-3 | Configure Quo-Jobber integration | Dev #2 | Integration verified | ☐ |
| 3-5 | Build all 3 n8n workflows (with Quo webhooks) | Dev #1 | Workflows deployed | ☐ |

---

## Week 2: Deploy + Train

| Day | Activity | Owner | Deliverable | Status |
|-----|----------|-------|-------------|--------|
| 6-7 | Test automations with real data | Developers | Working system | ☐ |
| 7-8 | Record Loom training videos | Client-facing #2 | 3-4 videos | ☐ |
| 8-9 | Live training session | Both client-facing | Trained team | ☐ |
| 9-10 | Deliver Blueprint, wrap-up call | All | Complete package | ☐ |

---

## Deliverables Checklist

### SOPs (4 Core + 1 Protocol)

| Doc ID | Title | Purpose | Status |
|--------|-------|---------|--------|
| PM-FS-002 | Service Call Execution | Trains techs, ensures consistency | ☐ |
| PM-OA-002 | Invoice Queue Processing | Eliminates sticky notes, faster billing | ☐ |
| PM-OA-003 | Service Call Dispatch | Documents competitive advantage | ☐ |
| PM-FS-005 | End-of-Job Handoff | Replaces live calls with async template | ✅ Created |
| PM-CP-001 | Communication Protocol | The "5 Rules" everyone follows | ✅ Created |

### Automations (3 Core + 1 Bonus)

| Automation | Trigger | Output | Status |
|------------|---------|--------|--------|
| Daily Message Digest | 4 PM daily | Email to Alyssa | ☐ |
| New Lead Notification | Webhook (call/client create) | SMS/Email to Kelce | ☐ |
| End-of-Day Summary | 5:30 PM daily | Email to Alyssa | ☐ |
| Call Summary Auto-Sync (Bonus) | Webhook (call summary) | Note in Jobber | ☐ |

### Additional Deliverables

| Deliverable | Purpose | Status |
|-------------|---------|--------|
| Quo Setup Guide | Client setup instructions | ✅ Created |
| PlotterOps Blueprint | Roadmap for Phase 2 | ☐ |
| Training Videos (3-4) | Loom walkthroughs | ☐ |
| Google Drive folder | Passive SOP capture | ☐ |

---

## n8n Workflow Specifications

### Workflow 1: Daily Message Digest

| Field | Value |
|-------|-------|
| **Trigger** | Schedule - 4:00 PM daily |
| **Data Sources** | Quo (SMS/calls) + Jobber (in-app messages) |
| **Output** | Email to Alyssa (optionally Kelce) |

**Steps:**
1. Quo API → Get messages/calls from last 24hrs without follow-up
2. Jobber API → Get conversations without response
3. Merge → Deduplicate by client
4. Format → Build digest HTML
5. Email → Send to Alyssa

---

### Workflow 2: New Lead Notification

| Field | Value |
|-------|-------|
| **Trigger** | Quo `call.completed` webhook OR Jobber `CLIENT_CREATE` webhook |
| **Output** | SMS/Email to Kelce instantly |

**Steps:**
1. Webhook receives event → Parse contact info
2. If Quo: Check if exists in Jobber → If not, auto-create
3. Format → Build notification with source info
4. SMS/Email → Send to Kelce

**Note:** Quo's native Jobber integration handles auto-contact creation, but we add notification layer.

---

### Workflow 3: End-of-Day Summary

| Field | Value |
|-------|-------|
| **Trigger** | Schedule - 5:30 PM daily |
| **Data Sources** | Jobber API (completed jobs) + Quo API (call summaries) |
| **Output** | Email to Alyssa |

**Steps:**
1. Jobber API → Get visits completed today
2. For each visit → Pull notes, line items, photos
3. Quo API → Get any call summaries for those clients today
4. Format → Build summary with totals + call notes
5. Email → Send to Alyssa

---

### Workflow 4: Call Summary Auto-Sync (Bonus)

| Field | Value |
|-------|-------|
| **Trigger** | Quo `call.summary.completed` webhook |
| **Output** | Note added to Jobber job |

**Steps:**
1. Webhook receives AI summary
2. Match to Jobber client by phone number
3. Add summary as note to client's active job (if any)
4. Flag for follow-up if no active job exists

---

## Success Metrics (Day 30)

### Core Metrics

| Metric | Target |
|--------|--------|
| Phone calls for job handoff | Reduced by 80% |
| Messages falling through | Zero (caught by digest) |
| Alyssa using structured handoffs | 100% of jobs |
| Kelce reviewing daily digest | Daily habit formed |
| Time saved per day | 30+ minutes |
| All calls through Quo | 100% (single number) |
| AI call summaries syncing to Jobber | Verified working |
| Passive SOP recordings captured | At least 2 during sprint |

### Inventory Loss Tracking (Phase 2 Data Collection)

We're not fixing inventory in Phase 1, but we ARE measuring the cost:

| Metric | What We Track | Purpose |
|--------|---------------|---------|
| Inventory-related issues | All occurrences via handoff template | Quantify the pain |
| Rush shipping costs | $ total during sprint | Direct cost measurement |
| Wasted trips | Count of jobs where part wasn't available | Time/fuel cost |
| Jobs delayed for parts | Count + days delayed | Customer impact |
| "Do we have X?" calls | Weekly count (Alyssa logs) | Interruption cost |

**Why:** After 30 days, we'll have data like: *"You had 8 inventory issues: 3 wasted trips, 2 rush orders ($150 extra), 3 jobs delayed avg 2 days."* This justifies the Phase 2 inventory system build.

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Jobber API limitations | Research API during Day 1, have fallback polling approach |
| Kelce doesn't adopt template | Keep to 5 fields max, demo time savings |
| Automations break | Simple flows, tested thoroughly, manual fallback documented |
| Feels like "just docs" | Automations + training videos make it tangible |
| A2P 10DLC delays | Start registration before sprint; calls work immediately, SMS may be delayed |
| Quo adoption resistance | Demo AI call summaries - major wow factor; no behavior change for phone calls |
| Passive SOP capture doesn't happen | Demo during shadow session; set reminder; this is bonus, not required |

---

## Files Reference

### Created Files

| File | Purpose |
|------|---------|
| `plotter-mechanics/quick-win-proposal.md` | Client-ready proposal |
| `plotter-mechanics/sops/field-service/end-of-job-handoff.md` | End-of-Job Handoff SOP |
| `plotter-mechanics/sops/communication-protocol.md` | Communication Protocol (5 Rules) |
| `plotter-mechanics/jobber-api-notes.md` | API research + Quo integration notes |
| `plotter-mechanics/quo-setup-guide.md` | Client setup instructions |
| `plotter-mechanics/execution-plan.md` | This document |

### Files to Create During Sprint

| File | Purpose |
|------|---------|
| `n8n/plotter-mechanics/daily-message-digest.json` | n8n workflow |
| `n8n/plotter-mechanics/new-lead-notification.json` | n8n workflow |
| `n8n/plotter-mechanics/end-of-day-summary.json` | n8n workflow |
| `n8n/plotter-mechanics/call-summary-sync.json` | n8n workflow (bonus) |

---

## Phase 2 Transition

After Phase 1 delivery, use this pitch:

> "You're now running everything through Jobber with a reliable handoff system. Nothing falls through the cracks. But you're still doing it manually—and every time Alyssa needs to know if you have a part in stock, she still has to call you.
>
> Phase 2 builds the inventory system so she can answer that herself. Plus, we connect Capsule and QuickBooks so you have one place for everything."

**Credit incentive:** $5K from Phase 1 applies to Phase 2 if signed within 14 days of delivery.

---

## Key Reminders

1. **Quo is the unlock** - Native Jobber integration solves the "messages API" gap (requires Jobber Core plan or higher)
2. **A2P 10DLC is critical path** - Must start registration before sprint begins (5-30 day lead time)
3. **Passive SOP capture is low-effort, high-value** - Demo during shadow session, process recordings on our side
4. **End-of-Job Handoff is the linchpin** - This single change eliminates 4-6 phone calls per day
5. **Inventory tracking builds Phase 2 case** - We measure the pain now, fix it later with data to back it up

---

*Created: December 2025*
*PlotterOps Quick Win Sprint*
