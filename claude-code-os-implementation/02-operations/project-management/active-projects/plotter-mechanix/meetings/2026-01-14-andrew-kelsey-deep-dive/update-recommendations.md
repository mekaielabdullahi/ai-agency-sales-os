# Jan 14, 2026 Meeting - Update Recommendations

This report summarizes what should be updated in the roadmap/project docs and Notion tasks based on the Andrew & Kelsey deep dive meeting.

---

## PART 1: ROADMAP & PROJECT DOC UPDATES

### Documents to Update

#### 1. `deliverables/overall-roadmap.md`
**Current State:** Last updated Dec 23, 2025 - references "Week 1 Testing" as current status

**Recommended Updates:**
- [ ] Update status to reflect current phase (we're past Week 1 testing)
- [ ] Add new context from Kelsey:
  - **Inventory scope clarified:** ~$50k in untracked inventory (parts, consumables, used equipment)
  - **Used parts revenue:** $1,200 power supplies from parted-out machines being lost
  - **AR problem:** $100k in AR due to poor payment follow-up
  - **Communication gaps:** Kelsey's service focus leaves no time for sales/quoting, Alyssa lacks industry knowledge
- [ ] Add "Ply" as inventory management system being evaluated (Kelsey demoing Friday)
- [ ] Add Andrew JV context as potential future opportunity

#### 2. `deliverables/phase-2-roadmap.md`
**Current State:** Last updated Dec 23, 2025 - planning/not yet scoped

**Recommended Updates:**
- [ ] Update "Questions to Answer in Phase 1" section - some questions now answered:
  - How many unique parts? → ~$50k worth, includes consumables and used equipment
  - Current tracking method? → None (lost without a system)
  - Revenue from used parts? → Yes, example: $1,200 power supplies from parted machines
- [ ] Add "Ply" to inventory management research
- [ ] Add Supplies JV as potential Phase 2/3 opportunity:
  - Andrew (e-commerce expert, ex-Amazon) as potential partner
  - Direct fulfillment model vs Amazon FBA
  - Free ink trial strategy
- [ ] Add revenue protection items:
  - $75 non-refundable travel fee
  - CC on file requirement
- [ ] Add AR collection automation as potential scope

#### 3. `status/P0-ACTIVE-NOW.md`
**Current State:** Last updated Dec 29, 2025 - still shows "Discovery Phase"

**Recommended Updates:**
- [ ] Update to reflect current Phase 1 delivery status
- [ ] Update immediate next steps:
  - Quo migration confirmed (Vonage → Quo)
  - 3 users: Kelsey, Alyssa, Joe
  - Kelsey cell phone forwarding tested and working
- [ ] Add new action items from Jan 14 meeting:
  - Number porting (Vonage + Kelsey cell)
  - IVR replication
  - Alyssa training on Quo
- [ ] Add Jobber automation breakthrough: GraphQL API access for Request status logic

#### 4. `planning/phase-1-prd.md` or `planning/phase-1-prd-v1.1.md`
**Recommended Updates:**
- [ ] Add Jobber GraphQL API discovery as technical enabler
- [ ] Clarify Request status challenge and proposed solution
- [ ] Add Vonage IVR documentation requirement before porting

---

## PART 2: NOTION TASK UPDATES

### Current Notion Task Summary (Plotter Mechanix)

| Status | Count |
|--------|-------|
| Blocked | 2 |
| In Progress | 12 |
| Not Started | 24 |
| Done | 11 |
| Cancelled | 1 |

### Tasks to UPDATE (Change Status/Details)

#### Move to DONE or update status:
| Current Task | Current Status | Recommended Change | Reason |
|--------------|----------------|-------------------|--------|
| "Coordinate Vonage 2FA access with Kelsey" | Done | ✅ Keep as Done | Confirmed in meeting |
| "Document Vonage IVR menu options..." | Done | ✅ Keep as Done | Referenced as complete |

#### BLOCKED Tasks - New context:
| Task | Current Status | Update Needed |
|------|----------------|---------------|
| "Port Vonage number to Quo" | Blocked | Add note: Waiting on Vonage 2FA disable + IVR documentation. Kelsey to disable 2FA. |
| "Test all routing scenarios before number porting" | Blocked | Add note: Pending IVR documentation |

#### IN PROGRESS Tasks - Context updates:
| Task | Update Needed |
|------|---------------|
| "Replicate Vonage routing functionality in Quo" | On track - need IVR menu documentation from Kelsey first |
| "Complete Quo IVR menu configuration" | Dependency: Need Vonage menu structure |
| "Call transcript to jobber requests" | Breakthrough: Can use Claude Code + Jobber GraphQL API for Request status logic |

### NEW Tasks to CREATE

From Jan 14 meeting action items:

#### Kelsey Tasks (Client):
| Task | Priority | Assignee | Notes |
|------|----------|----------|-------|
| Forward personal cell to Quo for live test | High | Kelsey | ✅ Already done per meeting |
| Install Quo on Alyssa's phone | Urgent | Kelsey | Temporary call handling |
| Create shared Dropbox folder for social media content | Medium | Kelsey | Share w/ Chris, Matthew, Trent |
| Export contacts from Capsule | High | Kelsey | Email to Matthew |
| Demo "Ply" inventory software (Friday) | High | Kelsey | Report back to team |
| Disable Vonage admin 2FA | Urgent | Kelsey | Blocker for porting |
| Document existing IVR menu | High | Kelsey | Required before porting |

#### Team Tasks:
| Task | Priority | Assignee | Notes |
|------|----------|----------|-------|
| Begin number porting process (Vonage + Kelsey cell) | High | Trent & Matthew | After IVR documented |
| Configure Quo to replicate Vonage menu system | High | Matthew | After IVR documented |
| Refine N8N → Jobber workflow for Request statuses | High | Trent | Use GraphQL API |
| Merge plotter-mechanics-linux repo into main | Medium | Trent/Matthew | Repo consolidation |
| Merge n8n workflows into Plotter Mechanics repo | Medium | Trent | Push to GitHub |
| Contact FBM network re: Andrew's Amazon suspension | Low | Matthew | Background research |
| Schedule 2nd Alyssa meeting | High | Team | Training follow-up |
| Schedule Joe meeting | High | Team | Stakeholder interview |
| Implement $75 non-refundable travel fee in Jobber | Medium | Team | Revenue protection |
| Train Alyssa to answer Quo after 4 rings | High | Chris | Part of Quo rollout |

---

## PART 3: PHASE 2 PROPOSAL CONSIDERATIONS

New information to incorporate into Phase 2 proposal prep:

### Inventory Management (Confirmed Priority)
- ~$50k in untracked inventory
- Used parts from parted-out machines = lost revenue (e.g., $1,200 power supplies)
- Kelsey evaluating "Ply" - demo Friday
- Need to design data model and integrate with Jobber

### AR/Collections Problem
- $100k AR due to poor payment follow-up
- Revenue protection: $75 travel fee, CC on file
- Could be Phase 2 automation target

### Supplies JV Opportunity
- Andrew (e-commerce, ex-Amazon) interested in JV
- Direct fulfillment model, avoid FBA
- Free ink trial strategy for customer acquisition
- Could be Phase 3+ if partnership forms

### Communication/Team Gaps Confirmed
- Kelsey = service focus, no time for sales/quoting
- Alyssa lacks industry knowledge for effective follow-up
- Google Meet transition for better multi-party collaboration
- Andrew to join future calls for logistics discussions

---

## RECOMMENDED IMMEDIATE ACTIONS

### High Priority (Do Today/Tomorrow)
1. Create new Notion tasks for Kelsey's client actions (Vonage 2FA, IVR doc, Dropbox, Capsule export)
2. Update blocked tasks with context from meeting
3. Create task for "Alyssa Quo training"

### Medium Priority (This Week)
1. Update `status/P0-ACTIVE-NOW.md` with current state
2. Update `overall-roadmap.md` status section
3. Add Phase 2 context to `phase-2-roadmap.md`

### Low Priority (Before Phase 2 Proposal)
1. Document Andrew JV context for future reference
2. Capture AR/collections problem scope
3. Add Ply evaluation results (after Friday demo)

---

*Generated from 2026-01-14 Andrew & Kelsey Deep Dive meeting*
