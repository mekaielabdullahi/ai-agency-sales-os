# Automation Solutions Inc (ASI) - Client Onboarding Package

## Client Overview

| Field | Value |
|-------|-------|
| **Company** | Automation Solutions Inc (ASI) |
| **Website** | automationsolinc.com |
| **Industry** | Industrial automation (robotics, controls, PLC programming) |
| **Revenue** | $7.1M |
| **Employees** | 32 |
| **President** | Brad Tompkins |
| **Email** | Brad@automationsolinc.com |
| **Phone** | 205-919-1400 |
| **Locations** | Birmingham, AL + Huntsville, AL |
| **Tagline** | "Our Passion Is Your Productivity" |
| **Lead Source** | 10X Summit (January 2026) |

## Strategic Importance

**HIGH-VALUE MANUFACTURING/AUTOMATION PROSPECT** -- $7.1M revenue, 32 employees across two locations. Industrial automation companies have deep operational complexity (project management, technician dispatch, quote generation, service call routing) that maps directly to AI transformation opportunities. This is a flagship engagement opportunity for AriseGroup.

## Current Status

| Field | Value |
|-------|-------|
| **Phase** | Pre-Close / Onboarding Prep |
| **Last Contact** | January 14, 2026 (10X Summit) |
| **Next Step** | Kickoff meeting upon close |

---

## Project Structure

```
automation-solutions-inc/
├── README.md                          # This file - master onboarding document
├── discovery/                         # Pre-engagement research and intel
├── audit/                             # AI readiness audit artifacts
│   ├── process-map.md                 # Business process documentation
│   ├── opportunity-matrix.md          # Prioritized AI opportunities
│   ├── discovery-unknowns.md          # Questions requiring follow-up
│   └── audit.json                     # Structured engagement data
├── meetings/
│   └── kickoff/                       # Kickoff meeting materials
│       ├── agenda.md                  # 60-minute kickoff agenda
│       └── transcript.md             # Meeting transcript (post-meeting)
├── planning/
│   ├── roadmap/                       # Phased implementation roadmap
│   └── proposals/                     # Scope, pricing, SOW documents
├── status/                            # Current status tracking
├── docs/                              # Client-provided documents
├── offer/                             # Engagement offer materials
├── deliverables/                      # Final deliverables for client
└── communications/                    # Communication logs and cadence docs
```

---

# 1. ONBOARDING CHECKLIST

## Internal Setup

- [ ] **Project folder created** in `active-projects/automation-solutions-inc/` (DONE)
- [ ] **Slack channels created** via `./run tools/slack_api.py client setup "asi" --display-name "Automation Solutions Inc"`
  - [ ] `#asi` -- client-facing communication channel
  - [ ] `#asi-internal` -- internal team discussion (no client access)
  - [ ] Canvas created and populated with client info
  - [ ] Welcome message posted and pinned
  - [ ] Notification posted to `#new-clients`
- [ ] **Notion workspace configured**
  - [ ] Client page created in Notion CRM
  - [ ] Feedback portal page duplicated from template
  - [ ] Filtered database view set (Company = Automation Solutions Inc)
  - [ ] Feedback form configured with pre-filled Company field
- [ ] **Google Drive folder created**
  - [ ] `AriseGroup / Clients / Automation Solutions Inc /`
  - [ ] Subfolders: Contracts, Deliverables, Meeting Notes, Client Docs
  - [ ] Share link added to Slack canvas
- [ ] **Team assignment confirmed**
  - [ ] Account Lead: TBD
  - [ ] Technical Lead: TBD
  - [ ] Audit Lead: TBD
- [ ] **Internal kickoff meeting held** (team alignment before client kickoff)

## Client-Facing Setup

- [ ] **Kickoff meeting scheduled** -- 60-minute video call with Brad Tompkins
- [ ] **Welcome email sent** with:
  - [ ] Meeting confirmation and agenda
  - [ ] Data request list (see Section 4)
  - [ ] Access request forms
  - [ ] Communication plan overview
- [ ] **Client invited to Slack channel** (`#asi` as single-channel guest)
- [ ] **Notion feedback portal shared** with Brad@automationsolinc.com
- [ ] **NDA / engagement agreement** signed and filed in Google Drive
- [ ] **Invoice / payment terms** confirmed and documented

## Technical Setup

- [ ] **Systems audit checklist prepared** (see Section 4 for full list)
- [ ] **Integration evaluation** -- assess current tech stack:
  - [ ] ERP / Accounting system (QuickBooks, SAP, etc.)
  - [ ] Project management tools (MS Project, Procore, JobBOSS, etc.)
  - [ ] CRM system (Salesforce, HubSpot, or none)
  - [ ] Dispatching / scheduling software
  - [ ] PLC programming environments (Rockwell, Siemens, etc.)
  - [ ] Document management (SharePoint, Google Drive, Dropbox)
  - [ ] Communication tools (email platform, phone system, field comms)
- [ ] **API / integration compatibility** documented
- [ ] **Data migration requirements** scoped
- [ ] **Security / compliance review** -- industrial automation may involve:
  - [ ] ITAR compliance (if defense/military contracts)
  - [ ] NIST cybersecurity framework adherence
  - [ ] OT (Operational Technology) network isolation requirements
  - [ ] Client NDA requirements for facility/process access

---

# 2. ONBOARDING TIMELINE

## Week 1: Foundation

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| Day 1 | Internal team kickoff | Account Lead | Team aligned on scope, roles, timeline |
| Day 1 | Slack channels + Notion workspace created | Ops | Infrastructure ready |
| Day 1 | Welcome email sent to Brad with agenda + data request | Account Lead | Email sent, meeting confirmed |
| Day 2 | 60-minute kickoff call with Brad Tompkins | Full team | Meeting transcript, action items |
| Day 3 | Post-kickoff internal debrief | Full team | Refined understanding, adjusted plan |
| Day 3-5 | Begin receiving client data and access credentials | Account Lead | Shared drive populated |
| Day 5 | Week 1 summary sent to Brad | Account Lead | Progress report email |

## Week 2: Discovery and Audit

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| Day 6-7 | Systems and tools inventory complete | Audit Lead | Tech stack documented |
| Day 7 | Weekly check-in call with Brad (30 min) | Account Lead | Status alignment |
| Day 8-9 | Process mapping interviews (operations, quoting, dispatch) | Audit Lead | Draft process maps |
| Day 9-10 | Shadow sessions / site observations (if on-site) | Audit Lead | Field notes, workflow observations |
| Day 10 | Week 2 summary + preliminary findings shared | Account Lead | Progress report + early insights |

## Week 3: Analysis and Opportunity Mapping

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| Day 11-12 | Complete process map documentation | Audit Lead | `audit/process-map.md` finalized |
| Day 12-13 | AI opportunity identification and scoring | Audit Lead | `audit/opportunity-matrix.md` draft |
| Day 14 | Weekly check-in call with Brad (30 min) | Account Lead | Review preliminary opportunity matrix |
| Day 14-15 | ROI modeling for top 3-5 opportunities | Technical Lead | Cost-benefit analysis per opportunity |
| Day 15 | Week 3 summary sent to Brad | Account Lead | Progress report + opportunity preview |

## Week 4: Recommendations and Roadmap

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| Day 16-17 | Finalize opportunity matrix and prioritization | Audit Lead | Final `audit/opportunity-matrix.md` |
| Day 17-18 | Build phased implementation roadmap | Technical Lead | `planning/roadmap/` populated |
| Day 18-19 | Prepare executive presentation | Account Lead | Slide deck / report for Brad |
| Day 20 | **Findings presentation to Brad Tompkins** (60 min) | Full team | Audit report delivered, next steps agreed |
| Day 20 | Proposal for Phase 1 implementation delivered | Account Lead | `planning/proposals/` SOW draft |

---

# 3. KICKOFF MEETING AGENDA

**Meeting:** ASI Kickoff -- AriseGroup x Automation Solutions Inc
**Duration:** 60 minutes
**Attendees:** Brad Tompkins (ASI President), AriseGroup team
**Format:** Video call (Zoom / Google Meet)

---

### 0:00 - 0:05 | Welcome and Introductions (5 min)

- AriseGroup team introductions (names, roles, responsibilities on this engagement)
- Confirm Brad's role and any other ASI stakeholders who should be involved
- Acknowledge the 10X Summit connection and the path to this engagement
- Set expectations: this is a working session, not a pitch

### 0:05 - 0:15 | Engagement Overview and Objectives (10 min)

- Review the engagement scope and what AriseGroup will deliver
- Clarify what success looks like for ASI:
  - "Brad, at the end of this engagement, what does a win look like for you?"
  - "What is the single biggest operational pain point you want us to address?"
- Confirm engagement timeline (4-week audit, then phased implementation)
- Discuss what is NOT in scope (set boundaries early)

### 0:15 - 0:35 | Current State Review (20 min)

- **Operations overview** -- walk through how ASI operates day-to-day:
  - How do projects flow from quote to completion?
  - How are technicians dispatched to Birmingham vs. Huntsville sites?
  - What does service call intake look like?
  - How are PLC programming projects scoped and managed?
- **Technology stack** -- what systems does ASI use today?
  - Accounting / ERP
  - Project management
  - CRM / sales pipeline
  - Communication tools (internal and client-facing)
  - Document management
  - Any proprietary or industry-specific software
- **Team structure** -- who does what?
  - Org chart or key roles across 32 employees
  - Birmingham vs. Huntsville team split
  - Who are the power users / champions for new tools?
- **Pain points deep-dive** -- Brad's top 3 frustrations:
  - Quote generation bottlenecks
  - Project coordination across two offices
  - Technician documentation and reporting
  - Service call routing and response times
  - Client communication gaps

### 0:35 - 0:45 | Access and Data Requirements (10 min)

- Walk through the data request list (Section 4 of this document)
- Identify what Brad can provide immediately vs. what needs internal coordination
- Discuss access logistics:
  - Who is the IT contact for system access?
  - Are there security policies or NDAs required for system access?
  - Remote access vs. on-site requirements
  - ITAR or other compliance considerations
- Agree on a shared document repository (Google Drive folder, link in Slack canvas)
- Set a deadline for initial data delivery (target: end of Week 1)

### 0:45 - 0:55 | Timeline, Milestones, and Communication (10 min)

- Review the 4-week timeline (Section 2 of this document)
- Confirm weekly check-in schedule:
  - Day and time for 30-minute weekly calls
  - Brad's preferred communication channel (Slack, email, phone)
  - Response time expectations (both directions)
- Review milestone gates:
  - Week 1: Foundation complete, data received
  - Week 2: Discovery and process mapping complete
  - Week 3: Opportunity matrix and ROI models drafted
  - Week 4: Final presentation and recommendations delivered
- Discuss escalation process for blockers or urgent issues
- Introduce the Slack channel and Notion feedback portal

### 0:55 - 1:00 | Next Steps and Action Items (5 min)

- Recap action items for both sides:
  - **Brad:** Send data per request list, provide IT contact, confirm weekly call time
  - **AriseGroup:** Send meeting summary, finalize access requests, begin systems inventory
- Confirm next touchpoint (weekly check-in date/time)
- Thank Brad for his time; express confidence in the engagement

---

# 4. DATA REQUEST LIST

## Specific to Industrial Automation (ASI)

### A. Organizational and Financial

| # | Item | Format | Priority | Notes |
|---|------|--------|----------|-------|
| 1 | Org chart or team roster (32 employees) | PDF / spreadsheet | HIGH | Include Birmingham vs. Huntsville split |
| 2 | Revenue breakdown by service line | Spreadsheet | HIGH | Robotics vs. controls vs. PLC vs. service |
| 3 | Top 10 clients by revenue (anonymized OK) | Spreadsheet | MEDIUM | Understand client concentration risk |
| 4 | Annual project volume (number of projects/year) | Any format | HIGH | Gauge operational throughput |
| 5 | Typical project lifecycle duration | Description | MEDIUM | Quote-to-completion average timeline |
| 6 | Current P&L or financial summary (if comfortable sharing) | PDF | LOW | Understand cost structure |

### B. Sales and Quoting

| # | Item | Format | Priority | Notes |
|---|------|--------|----------|-------|
| 7 | Sample quotes / proposals (3-5 recent) | PDF | HIGH | Understand quoting process and format |
| 8 | Quote-to-close ratio (win rate) | Any format | HIGH | Baseline for improvement measurement |
| 9 | Average quote turnaround time | Description | MEDIUM | Days from request to quote delivery |
| 10 | CRM export or pipeline snapshot | CSV / screenshot | MEDIUM | If using CRM; if not, note the gap |
| 11 | List of quoting tools or templates used | Description | MEDIUM | Spreadsheets, software, manual processes |

### C. Project Management and Operations

| # | Item | Format | Priority | Notes |
|---|------|--------|----------|-------|
| 12 | Current project tracking method | Screenshot / export | HIGH | MS Project, spreadsheets, whiteboard, etc. |
| 13 | Sample project schedule (Gantt or similar) | PDF / export | HIGH | Understand complexity of typical project |
| 14 | Technician dispatch process documentation | Description | HIGH | How are techs assigned to jobs? |
| 15 | Service call intake process | Description | HIGH | Phone? Email? Portal? Walk-in? |
| 16 | Birmingham-Huntsville coordination protocols | Description | MEDIUM | How do the two offices communicate? |
| 17 | Inventory / parts management system info | Screenshot | MEDIUM | How are parts tracked and ordered? |
| 18 | Subcontractor management process | Description | LOW | If ASI uses subs for electrical, mechanical, etc. |

### D. Technical and Engineering

| # | Item | Format | Priority | Notes |
|---|------|--------|----------|-------|
| 19 | PLC programming platforms in use | List | HIGH | Rockwell (Allen-Bradley), Siemens, Mitsubishi, etc. |
| 20 | SCADA / HMI systems deployed | List | MEDIUM | FactoryTalk, Ignition, WonderWare, etc. |
| 21 | Engineering documentation standards | Example docs | MEDIUM | How are programs, schematics, manuals stored? |
| 22 | Version control for PLC programs | Description | MEDIUM | How are code changes tracked? |
| 23 | Commissioning / startup process documentation | Description | MEDIUM | Steps from build to customer handoff |
| 24 | Safety standards compliance (NFPA 79, OSHA, etc.) | Description | LOW | Compliance requirements that affect workflows |

### E. Client Communication and Service

| # | Item | Format | Priority | Notes |
|---|------|--------|----------|-------|
| 25 | Client communication channels | Description | HIGH | Email, phone, portal, in-person? |
| 26 | Service level agreements (SLAs) with key clients | PDF | MEDIUM | Response time commitments |
| 27 | Customer satisfaction data (surveys, NPS, reviews) | Any format | LOW | Baseline for improvement |
| 28 | Warranty / support process documentation | Description | MEDIUM | Post-project support workflow |
| 29 | Recurring service contract list | Spreadsheet | MEDIUM | Ongoing maintenance agreements |

### F. Technology and Systems

| # | Item | Format | Priority | Notes |
|---|------|--------|----------|-------|
| 30 | Complete list of software tools used across the company | Spreadsheet | HIGH | Accounting, PM, CRM, email, field tools, etc. |
| 31 | IT contact name and email | Text | HIGH | For system access and integration questions |
| 32 | Network architecture overview (if available) | Diagram | LOW | IT vs. OT network separation |
| 33 | Current automation or integration between systems | Description | MEDIUM | Any existing Zapier, API connections, etc. |
| 34 | Mobile tools used by field technicians | List | MEDIUM | Phones, tablets, apps for field work |
| 35 | Document storage and sharing method | Description | MEDIUM | SharePoint, Google Drive, Dropbox, file server? |

### G. Access Requests

| # | Item | Access Type | Priority | Notes |
|---|------|-------------|----------|-------|
| 36 | Read-only access to project management system | Viewer account | HIGH | Observe current workflows |
| 37 | Read-only access to CRM (if applicable) | Viewer account | MEDIUM | Understand sales pipeline |
| 38 | Access to sample engineering documentation | Shared folder | MEDIUM | Understand documentation standards |
| 39 | Access to financial reporting dashboard (if exists) | Viewer account | LOW | Understand reporting capabilities |
| 40 | Guest access to internal communication tools | Guest account | LOW | Observe communication patterns |

---

# 5. COMMUNICATION PLAN

## Weekly Check-In Schedule

| Meeting | Frequency | Duration | Attendees | Purpose |
|---------|-----------|----------|-----------|---------|
| **Weekly Status Call** | Every week (same day/time) | 30 min | Account Lead + Brad Tompkins | Progress review, blockers, decisions |
| **Internal Sync** | Every week (day before client call) | 15 min | AriseGroup team | Prep for client call, align messaging |
| **Milestone Review** | Weeks 2 and 4 | 60 min | Full team + Brad | Deep-dive on findings and deliverables |

**Proposed Schedule (confirm with Brad at kickoff):**
- Weekly client call: Tuesdays at 10:00 AM CT (Birmingham time)
- Internal sync: Mondays at 3:00 PM (AriseGroup time)

## Reporting Format

### Weekly Status Report (delivered via email + posted in Slack)

```
SUBJECT: ASI Weekly Update -- Week [X] of [4]

STATUS: [On Track / At Risk / Blocked]

COMPLETED THIS WEEK:
- [Bullet list of completed items]

IN PROGRESS:
- [Bullet list of active work items]

BLOCKERS / NEEDS FROM ASI:
- [Any items requiring Brad's action or decision]

NEXT WEEK PLAN:
- [Bullet list of planned activities]

KEY METRICS:
- Processes mapped: [X] of [estimated total]
- Opportunities identified: [X]
- Data items received: [X] of 40

NEXT CALL: [Date, time, link]
```

### Milestone Deliverable Reports

| Milestone | Deliverable | Format | Delivery Method |
|-----------|-------------|--------|-----------------|
| Week 1 Complete | Foundation summary, data receipt confirmation | Email + Slack | Account Lead sends |
| Week 2 Complete | Process map draft, initial findings | PDF + live review | 60-min milestone call |
| Week 3 Complete | Opportunity matrix, ROI models | PDF + Slack | Shared in advance of Week 4 review |
| Week 4 Complete | Final audit report, implementation roadmap, Phase 1 proposal | Presentation + PDF | 60-min findings presentation |

## Escalation Process

### Severity Levels

| Level | Definition | Response Time | Escalation Path |
|-------|-----------|---------------|-----------------|
| **P0 -- Critical** | Engagement at risk, blocker preventing all progress | 2 hours | Account Lead calls Brad directly |
| **P1 -- High** | Significant blocker on a key workstream | 24 hours | Account Lead emails Brad, follows up with call |
| **P2 -- Medium** | Non-blocking issue requiring client input | 48 hours | Posted in Slack channel, discussed at weekly call |
| **P3 -- Low** | Nice-to-have information or minor clarification | Next weekly call | Added to weekly call agenda |

### Escalation Path

```
Step 1: Account Lead contacts Brad Tompkins (email or phone)
Step 2: If no response in 24 hours, Account Lead calls Brad's office (205-428-1550)
Step 3: If no response in 48 hours, Account Lead escalates to AriseGroup leadership
        for strategic guidance (pause engagement, adjust scope, etc.)
```

### AriseGroup Internal Escalation

```
Step 1: Teammate raises issue in #asi-internal Slack channel
Step 2: Account Lead triages within 4 hours
Step 3: If unresolved, escalate to AriseGroup leadership in daily standup
```

## Key Milestones and Review Gates

| Gate | Timing | Criteria to Pass | Decision Point |
|------|--------|-------------------|----------------|
| **Gate 0: Go/No-Go** | Pre-kickoff | Contract signed, payment terms confirmed, team assigned | Proceed with kickoff or hold |
| **Gate 1: Foundation** | End of Week 1 | Kickoff complete, data request list delivered, access granted (or timeline agreed) | Confirm audit scope is achievable with available data |
| **Gate 2: Discovery Complete** | End of Week 2 | Process maps drafted, all key interviews completed, tech stack documented | Confirm sufficient understanding to identify opportunities |
| **Gate 3: Analysis Complete** | End of Week 3 | Opportunity matrix scored, ROI models built for top opportunities | Confirm findings are defensible before final presentation |
| **Gate 4: Delivery** | End of Week 4 | Final presentation delivered, Phase 1 proposal accepted or feedback received | Decide on Phase 1 engagement (scope, timeline, pricing) |

### Gate Review Format

Each gate review follows this structure:
1. **Status check** -- Are we on track? What slipped?
2. **Findings review** -- What have we learned?
3. **Decision point** -- Do we proceed, adjust, or pause?
4. **Action items** -- What needs to happen before the next gate?

---

# 6. RISK REGISTER

## Risks Specific to Onboarding an Industrial Automation Company

| # | Risk | Likelihood | Impact | Severity | Mitigation Strategy |
|---|------|-----------|--------|----------|---------------------|
| **R1** | **OT/IT network segregation blocks system access.** Industrial automation companies typically maintain strict separation between Operational Technology (OT) networks (controlling PLCs, SCADA, robots) and IT networks. AriseGroup may be denied access to production systems or face lengthy security approval processes. | HIGH | HIGH | CRITICAL | Scope the audit to IT-side systems first (CRM, PM, quoting, email). Do not request OT network access in Week 1. If OT insight is needed, request read-only exports or have ASI staff demonstrate systems via screen share. Build trust before asking for deeper access. |
| **R2** | **ITAR or export control compliance restricts data sharing.** If ASI serves defense contractors or military facilities (common for Alabama-based industrial automation firms near Huntsville/Redstone Arsenal), they may be subject to ITAR or EAR regulations that restrict sharing technical data, schematics, or project details with outside parties. | MEDIUM | HIGH | HIGH | Ask about ITAR status at the kickoff meeting. If applicable, ensure all AriseGroup team members are U.S. persons. Scope the audit to non-controlled business operations (quoting, scheduling, dispatch) rather than controlled technical data. Have ASI legal review what can be shared. |
| **R3** | **Field technician adoption resistance.** ASI's 32 employees include hands-on technicians who program PLCs, wire panels, and commission robotic systems. These team members may resist new digital tools or workflows, viewing them as overhead that slows down real work. If Brad cannot drive adoption, any AI implementation will fail. | MEDIUM | HIGH | HIGH | Focus early recommendations on tools that reduce technician burden (less paperwork, faster dispatch, automated reporting) rather than adding new steps. Interview 2-3 technicians during discovery to understand their actual pain points. Frame AI tools as "removing the stuff you hate" not "adding new systems to learn." Identify an internal champion among the technicians. |
| **R4** | **Multi-location coordination complexity is underestimated.** Birmingham and Huntsville are 100 miles apart. Projects, technicians, parts, and management attention are split across two offices. The operational complexity of two locations may mean process mapping takes significantly longer than estimated, or that processes differ between offices. | MEDIUM | MEDIUM | MEDIUM | Interview stakeholders at both locations (not just Brad in Birmingham). Add a buffer day in Week 2 for second-location discovery. Map processes per location first, then identify commonalities and divergences. Ensure the roadmap accounts for location-specific rollout if processes differ significantly. |
| **R5** | **Brad Tompkins is a single point of failure for client engagement.** As President of a 32-person company, Brad is likely pulled in many directions -- sales calls, client site visits, operational fires. If Brad becomes unavailable or unresponsive, the entire engagement stalls because there is no designated delegate. | MEDIUM | MEDIUM | MEDIUM | At the kickoff meeting, ask Brad to designate a secondary point of contact (operations manager, office manager, or senior project manager) who can provide data, answer questions, and make decisions in Brad's absence. Get this person's contact info and add them to the Slack channel. Build the weekly check-in rhythm early so Brad protects the time on his calendar. |

### Risk Monitoring

- Review risk register at each internal sync (weekly)
- Update likelihood/impact ratings as engagement progresses
- Add new risks as they are identified during discovery
- Escalate any risk that moves to CRITICAL severity to AriseGroup leadership

---

# 7. AI OPPORTUNITY HYPOTHESES (Pre-Discovery)

Based on ASI's profile (industrial automation, $7.1M revenue, 32 employees, two locations), the following are preliminary hypotheses to investigate during the audit:

| # | Opportunity | Estimated Impact | Complexity | Investigate In |
|---|-------------|-----------------|------------|----------------|
| 1 | **Quote/proposal generation automation** -- Standardize and accelerate the quoting process for robotics and controls projects | HIGH (revenue acceleration) | MEDIUM | Week 2 |
| 2 | **Technician dispatch and scheduling optimization** -- AI-assisted assignment of techs to jobs based on skills, location, availability | HIGH (operational efficiency) | HIGH | Week 2 |
| 3 | **Service call intake and routing** -- Automated triage of incoming service requests with priority scoring | MEDIUM (client satisfaction) | LOW | Week 2 |
| 4 | **Project documentation automation** -- Auto-generate commissioning reports, as-built documentation from field data | MEDIUM (time savings) | MEDIUM | Week 3 |
| 5 | **Cross-location project visibility** -- Unified dashboard for Birmingham + Huntsville project status, resource allocation | MEDIUM (coordination) | LOW | Week 2 |
| 6 | **Client communication automation** -- Automated project status updates, milestone notifications to clients | MEDIUM (client satisfaction) | LOW | Week 3 |
| 7 | **PLC program version control and knowledge management** -- Centralized repository with search for PLC code, standards, past solutions | HIGH (institutional knowledge) | HIGH | Week 3 |

---

# 8. BRAD TOMPKINS -- CLIENT PROFILE

**Communication preferences** (to be confirmed at kickoff):

| Attribute | Assumption | Confirm At Kickoff |
|-----------|------------|--------------------|
| **Decision style** | President of a $7.1M company -- likely decisive, ROI-focused | Yes |
| **Communication preference** | Phone/email (traditional industry) | Yes |
| **Meeting tolerance** | Low -- busy running operations, prefers concise meetings | Yes |
| **Technical depth** | Deep -- understands robotics, PLC, controls | Yes |
| **AI familiarity** | Unknown -- 10X Summit attendance suggests growth mindset | Yes |

**Approach guidelines:**
- Lead with business outcomes, not technology features
- Use industrial language he knows (commissioning, PLC, panel builds, service calls)
- Show respect for what ASI has built -- $7.1M with 32 people is efficient
- Do not assume ASI is broken -- frame as optimization, not fixing
- Birmingham is CT (Central Time) -- schedule all meetings accordingly

---

# APPENDIX: QUICK REFERENCE

## Key Contacts

| Role | Name | Phone | Email |
|------|------|-------|-------|
| ASI President | Brad Tompkins | 205-919-1400 | Brad@automationsolinc.com |
| ASI Office | -- | 205-428-1550 | -- |
| ASI IT Contact | TBD (get at kickoff) | TBD | TBD |
| ASI Secondary POC | TBD (get at kickoff) | TBD | TBD |
| AriseGroup Account Lead | TBD | -- | -- |
| AriseGroup Technical Lead | TBD | -- | -- |
| AriseGroup Audit Lead | TBD | -- | -- |

## Slack Channels

| Channel | Purpose |
|---------|---------|
| `#asi` | Client-facing communication with Brad and ASI team |
| `#asi-internal` | AriseGroup internal discussion about ASI engagement |

## Key Dates

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Contract signed | TBD | Pending |
| Kickoff meeting | TBD (Week 1, Day 2) | Not scheduled |
| Week 2 milestone review | TBD | Not scheduled |
| Final presentation | TBD (Week 4, Day 20) | Not scheduled |

---

*Generated by AriseGroup Ops Teammate*
*Created: February 6, 2026*
*Status: Ready for activation upon close*
