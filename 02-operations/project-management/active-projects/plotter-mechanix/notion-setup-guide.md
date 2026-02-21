# Plotter Mechanix - Notion Database Setup Guide

**Purpose:** Create a structured task management system for Phase 1 delivery that maps to PRD requirements.

**Location:** Arise AI WS → Your Private Section

---

## Step 1: Create the Main Page

1. In your private section, create a new page: **"Plotter Mechanix - Phase 1 Delivery"**
2. Add an icon (suggestion: 🖨️ or 📋)
3. Add a cover image if desired

---

## Step 2: Create the Epics Database

### Create Database
1. Inside the main page, type `/database` and select **"Database - Inline"**
2. Name it: **"Epics"**

### Configure Properties

| Property Name | Type | Options/Config |
|---------------|------|----------------|
| **Name** | Title | (default) |
| **Status** | Status | Not Started, In Progress, Done |
| **Priority** | Select | Critical, Urgent, High, Medium, Low |
| **FR Reference** | Text | For linking to PRD functional requirements |
| **Progress** | Rollup | (configure after Tasks db - counts completed sub-tasks) |
| **Description** | Text | Epic description |

### Create Views
1. **Kanban** - Group by Status
2. **Priority Table** - Sort by Priority (Critical first)

### Populate Epic Records

Create these 10 Epic records:

| Name | Priority | FR Reference | Description |
|------|----------|--------------|-------------|
| [EPIC] Communication Capture | Urgent | FR1-FR6 | Quo webhooks, call/voicemail/SMS capture |
| [EPIC] Transcription Quality | High | FR7-FR13 | Industry terminology, glossary, accuracy |
| [EPIC] AI Data Extraction | High | FR14-FR17 | Name extraction, summaries, equipment ID |
| [EPIC] Jobber Integration | High | FR18-FR25 | API calls, OAuth, Request creation |
| [EPIC] Request Routing Logic | High | FR26-FR30 | New vs existing clients, voicemail prefixes |
| [EPIC] Failover & Reliability | Critical | FR31-FR36 | Queue, retry logic, deduplication |
| [EPIC] Monitoring & Alerting | High | FR37-FR42 | Slack notifications, daily digest, error alerts |
| [EPIC] Operational Config | Medium | FR43-FR46 | Webhook endpoints, logs, manual reprocessing |
| [EPIC] Documentation & Training | High | FR47-FR50 | SOPs, videos, live training |
| [EPIC] Test Plan & Validation | High | NFR1-NFR31 | Verify FR and NFR compliance |

---

## Step 3: Create the Tasks Database

### Create Database
1. Below Epics, type `/database` and select **"Database - Inline"**
2. Name it: **"Tasks"**

### Configure Properties

| Property Name | Type | Options/Config |
|---------------|------|----------------|
| **Name** | Title | (default) |
| **Status** | Status | Not Started, In Progress, Blocked, Done, Cancelled |
| **Priority** | Select | Critical, Urgent, High, Medium, Low |
| **Epic** | Relation | → Link to Epics database |
| **Assignee** | Person | Team members |
| **Due Date** | Date | Optional |
| **FR Reference** | Text | Specific FR# this task addresses |
| **Notes** | Text | Implementation notes, blockers |
| **Source** | Select | PRD, Meeting, Ad-hoc |

### Create Views
1. **Kanban** - Group by Status
2. **By Epic** - Group by Epic relation
3. **My Tasks** - Filter by Assignee = Me
4. **Critical Path** - Filter Priority = Critical or Urgent

### Configure Rollup in Epics
After creating Tasks database:
1. Go back to Epics database
2. Edit the "Progress" property
3. Set as Rollup: Relation = Tasks, Property = Status, Calculate = Percent checked (Done)

---

## Step 4: Create the Backlog Database

### Create Database
1. Below Tasks, type `/database` and select **"Database - Inline"**
2. Name it: **"Backlog"**

### Configure Properties

| Property Name | Type | Options/Config |
|---------------|------|----------------|
| **Name** | Title | (default) |
| **Priority** | Select | High, Medium, Low |
| **Phase** | Select | Phase 2, Phase 3, Phase 4, TBD |
| **Source** | Select | PRD, Meeting, Discovery |
| **Notes** | Text | Context, dependencies |

### Create Views
1. **By Phase** - Group by Phase
2. **Priority Table** - Sort by Priority

---

## Step 5: Populate Tasks

After databases are created, populate with tasks organized by Epic.

### [EPIC] Communication Capture - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| ✅ Quo-to-Jobber webhook integration | Done | High | Trent | quo-to-jobber-request.json |
| ✅ Configure Quo call transcription | Done | High | Matthew | Working |
| 🔄 Replicate Vonage routing in Quo | In Progress | Urgent | Matthew | IVR config in progress |
| 🔄 Complete Quo IVR menu configuration | In Progress | High | Matthew | |
| ⏸️ Port Vonage number to Quo | Blocked | High | Trent | Needs IVR doc + 2FA disabled |
| ⏸️ Test all routing scenarios before porting | Blocked | Urgent | Matthew | Depends on IVR config |
| 🆕 Disable Vonage admin 2FA | Not Started | Urgent | Kelsey | Client action - blocker |
| 🆕 Document existing IVR menu | Not Started | High | Kelsey | Client action - blocker |
| 🆕 Install Quo on Alyssa's phone | Not Started | Urgent | Kelsey | Client action |
| 🆕 Configure voicemail webhook in Quo | Not Started | High | Trent | FR2 - workflow ready |
| 🆕 Configure SMS webhook in Quo | Not Started | High | Trent | FR3 - workflow ready |
| Configure time-based routing | Not Started | Medium | Matthew | |
| Configure weekend call handling | Not Started | Medium | Matthew | |

### [EPIC] AI Data Extraction - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| ✅ Quo webhook → AI processing workflow | Done | High | Trent | Gemini integration in main workflow |
| ✅ AI name extraction from transcript | Done | High | - | Working in workflow |
| ✅ AI call summary generation | Done | High | - | Working in workflow |
| ✅ AI equipment extraction | Done | High | - | Working in workflow |
| 🆕 Create Claude system prompt with glossary | Not Started | High | Matthew | Enhances accuracy |
| 🆕 Get jargon brain dump from Kelsey | Not Started | High | Matthew | Input for glossary |

### [EPIC] Jobber Integration - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| ✅ Jobber GraphQL API integration | Done | High | Trent | In main workflow |
| ✅ Create/update Jobber Requests | Done | High | - | Working |
| ✅ Client search by phone number | Done | High | - | Working |
| ✅ Auto-create client if not found | Done | High | - | Working |
| ✅ Configure Quo auto-create Request | Done | High | Trent | Working |
| 🔄 Define Jobber Request lifecycle | In Progress | High | Trent | How to mark 'done' |
| **🆕 Implement OAuth token auto-refresh** | Not Started | **CRITICAL** | Trent | FR24-25 - Tokens WILL expire |
| Test new caller → Request flow E2E | Not Started | High | Matthew | |

### [EPIC] Request Routing Logic - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| ✅ New caller → Create new Request | Done | High | - | Working |
| ✅ Existing client → Link to record | Done | High | - | Working |
| 🔄 Implement UC-2: Initial Client Calls | In Progress | High | Trent | |
| 🔄 Implement UC-3: Follow-up Client Calls | In Progress | High | Trent | |
| Test Quo contact matching | Not Started | High | Matthew | |

### [EPIC] Failover & Reliability - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| ✅ Error logging to data table | Done | High | Trent | quo_failed_webhooks table |
| ✅ Error notifications to Slack | Done | High | Trent | Error handler workflow |
| **🆕 Implement failover queue with retry** | Not Started | **CRITICAL** | Trent | FR31-36 - No retry currently |
| **🆕 Implement request deduplication** | Not Started | High | Trent | FR35 - Prevent duplicates |
| Test recovery flow E2E | Not Started | High | Matthew | |

### [EPIC] Monitoring & Alerting - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| ✅ Daily Slack digest workflow | Done | High | Trent | daily-call-summary.json |
| ✅ Error notifications to Slack | Done | High | Trent | quo-jobber-error-handler.json |
| ✅ Webhook logging to data tables | Done | Medium | Trent | |
| Configure Alyssa alert (3 pending) | Not Started | Medium | Trent | |
| Build notification routing workflow | Not Started | Medium | Trent | |

### [EPIC] Operational Config - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| Create phone number inventory doc | Not Started | Medium | Matthew | |
| 🆕 Merge n8n workflows into repo | Not Started | Medium | Trent | From Jan 14 meeting |
| 🆕 Merge plotter-mechanics-linux repo | Not Started | Medium | Trent | From Jan 14 meeting |
| Set up dedicated Quo voicemail line | Not Started | Medium | Matthew | |

### [EPIC] Documentation & Training - Tasks

| Task | Status | Priority | Assignee | Notes |
|------|--------|----------|----------|-------|
| ✅ Alyssa SOP for Request processing | Done | High | - | alyssa-quo-jobber-request-processing.md |
| ✅ Quo integration design docs | Done | Medium | - | design/integrations/quo/ |
| ✅ Jobber integration design docs | Done | Medium | - | design/integrations/jobber/ |
| 🔄 Create Phase 1 Progress Report | In Progress | Urgent | Mekaiel | |
| 🆕 Create training videos | Not Started | High | Team | FR49 - Contractual |
| 🆕 Schedule live training session | Not Started | High | Chris | FR50 - Contractual |
| 🆕 Train Alyssa on Quo | Not Started | High | Chris | From Jan 14 meeting |
| 🆕 Schedule 2nd Alyssa meeting | Not Started | High | Team | From Jan 14 meeting |
| 🆕 Schedule Joe meeting | Not Started | High | Team | From Jan 14 meeting |
| Document async handoff SOP | Not Started | Medium | Matthew | |
| Document follow-up call SOP | Not Started | Medium | Matthew | |

### [EPIC] Test Plan & Validation - Tasks

| Task | Status | Priority | FR/NFR | Notes |
|------|--------|----------|--------|-------|
| **Functional Requirements Testing** | | | | |
| Test: Call webhook → Request creation E2E | Not Started | High | FR1, FR18-21 | Happy path |
| Test: AI name extraction accuracy | Not Started | High | FR14 | ≥90% target |
| Test: AI summary quality | Not Started | High | FR15 | Manual review |
| Test: Equipment extraction accuracy | Not Started | Medium | FR16 | Manual review |
| Test: Client phone matching | Not Started | High | FR18 | Existing clients |
| Test: New client auto-creation | Not Started | High | FR19 | Unknown callers |
| Test: Voicemail → Request flow | Not Started | High | FR2 | After webhook config |
| Test: SMS → Jobber notes flow | Not Started | Medium | FR3 | After webhook config |
| Test: OAuth token refresh | Not Started | Critical | FR24-25 | After implementation |
| Test: Failover queue recovery | Not Started | Critical | FR31-36 | After implementation |
| Test: Error notification delivery | Not Started | High | FR37-38 | Slack alerts |
| Test: Daily digest accuracy | Not Started | Medium | FR39 | Stats correct |
| **Non-Functional Requirements Testing** | | | | |
| Test: Webhook processing <30s | Not Started | High | NFR1 | Performance |
| Test: Request creation <5min | Not Started | High | NFR2 | Performance |
| Test: 99% event capture rate | Not Started | High | NFR5 | Reliability |
| Test: No duplicate entries | Not Started | High | NFR8 | Reliability |
| Test: OAuth tokens encrypted | Not Started | Medium | NFR10 | Security |
| Test: API rate limits respected | Not Started | Medium | NFR16 | Integration |
| Test: AI extraction ≥90% accuracy | Not Started | High | NFR19 | Accuracy |
| Test: Client matching ≥99% accuracy | Not Started | High | NFR21 | Accuracy |
| Test: Slack alerts <2min | Not Started | Medium | NFR24 | Operational |
| **User Acceptance Testing** | | | | |
| UAT: Kelsey trusts Jobber as source | Not Started | High | Success | 30-day test |
| UAT: Alyssa processes without calling | Not Started | High | Success | Behavior change |
| UAT: Handoffs reduced to 1-2/day | Not Started | High | Success | From 4-6/day |

---

## Step 6: Populate Backlog

| Task | Priority | Phase | Source | Notes |
|------|----------|-------|--------|-------|
| [BACKLOG] Review Alternative Voice Agents | Low | TBD | PRD | Retell, Vapi, Voiceflow |
| [BACKLOG] Same-topic request routing | Medium | Phase 2 | PRD | Complex logic deferred |
| [BACKLOG] Additional phone lines (Alyssa, Joe) | Medium | Phase 2 | Meeting | After ports complete |
| [BACKLOG] Phone menu/IVR system | Medium | Phase 2 | PRD | After all lines set up |
| [BACKLOG] Demo Ply inventory software | High | Phase 2 | Jan 14 meeting | Kelsey demo Friday |
| [BACKLOG] Export contacts from Capsule | Medium | Phase 2 | Jan 14 meeting | For team review |
| [BACKLOG] Contact FBM re: Andrew suspension | Low | TBD | Jan 14 meeting | Background research |
| [BACKLOG] Set up WhatsApp group | Low | TBD | Meeting | Team communication |
| [BACKLOG] Email → Jobber automation | Low | Phase 2 | PRD | Deprioritized |
| [BACKLOG] External analytics storage | Low | Phase 2 | PRD | If needed |
| [BACKLOG] Inventory Management System | High | Phase 2 | PRD | ~$50k inventory |
| [BACKLOG] AI Training System ("Clone Kelsey") | Medium | Phase 3 | PRD | Knowledge capture |

---

## Quick Reference: Status Meanings

| Status | Color | Meaning |
|--------|-------|---------|
| Not Started | Gray | Task not yet begun |
| In Progress | Blue | Actively being worked on |
| Blocked | Red | Cannot proceed - dependency |
| Done | Green | Completed |
| Cancelled | Gray strikethrough | No longer needed |

## Quick Reference: Priority Levels

| Priority | When to Use |
|----------|-------------|
| **Critical** | Must be done for Phase 1 success, blockers |
| **Urgent** | Needed this week, time-sensitive |
| **High** | Important for delivery, do soon |
| **Medium** | Should do, but not blocking |
| **Low** | Nice to have, can defer |

---

## After Setup: Let Claude Help

Once you've created the database structure, let me know and I can help:
1. Review your setup
2. Suggest any missing tasks
3. Help prioritize the backlog
4. Track progress against PRD requirements

---

*Generated: January 14, 2026*
*Based on: Plotter Mechanix PRD v1.1 + Jan 14 Andrew/Kelsey meeting*
