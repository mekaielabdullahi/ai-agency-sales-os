# Agency Operations Dashboard - Project Overview

**Project Name:** Agency Operations Dashboard (Internal)
**Priority:** P1 (Revenue Enablement)
**Status:** Planning Phase
**Created:** December 25, 2025
**Owner:** Matt Kerns (Architect)

---

## Executive Summary

**What:** Unified internal operations dashboard consolidating project tracking, revenue management, client relationships, pricing strategy, and delivery execution.

**Why:** Revenue and project data is scattered across markdown files. No visual overview. Hard to quickly answer "What's our revenue status?" or "Where are we with Client X?"

**How:** Single-page application (SPA) built with v0.app + AutoClaude, deployed to internal demo site.

**When:** Phase 1 MVP in 8-12 hours, full feature set over 4-6 weeks (phased approach).

---

## Problem Statement

### Current State (Pain Points)
1. **Revenue visibility:** Manual calculation from multiple markdown files
2. **Project status:** Requires reading multiple project folders
3. **Client relationships:** Process maps exist but not easily accessible
4. **Pricing decisions:** Manual calculations, no historical reference
5. **Development tracking:** Status scattered across files and boards
6. **Deliverable validation:** Manual tracking, no structured workflow
7. **Team questions:** "Where are we?" takes 30-60 min to answer accurately

### Impact
- Architect time spent on administrative overhead vs. revenue activities
- Delayed decision-making due to lack of visibility
- Difficult to identify at-risk projects or revenue gaps
- Team misalignment on project status
- Client questions require file searching

---

## Solution Overview

### Desired End State
**Single dashboard that provides:**
- Real-time revenue visibility (actual vs. projected)
- Visual project pipeline with status indicators
- Client relationship tracking and process maps
- Pricing strategy with ROI calculations
- Development execution tracking (Kanban)
- Deliverable validation workflow

### User Experience
- Load dashboard → See all projects and revenue in <5 seconds
- Click project → See full details (status, revenue, deliverables, Kanban)
- Tab navigation → Switch between views (revenue, clients, pricing, etc.)
- Search/filter → Find specific project or deliverable quickly
- Export → Generate reports for stakeholders

---

## Core Features (7 Dashboard Tabs)

### Tab 1: Project & Revenue Tracker (Primary View) 🎯
**Purpose:** Main dashboard view showing all projects and revenue at a glance

**Features:**
- Project cards with: Name, Client, Status, Phase, Revenue (actual + projected)
- Visual status indicators: 🟢 On track, 🟡 At risk, 🔴 Blocked, ✅ Complete
- Revenue summary: Total YTD, Current month, Projected month/quarter
- Filter by: Client, Phase, Status, Revenue range
- Sort by: Revenue, Deadline, Status

**Data Displayed:**
- Project name
- Client name
- Current phase (Pre-discovery, Audit, Discovery, Quick Win, Phase 2/3/4)
- Revenue received (actual $)
- Revenue projected (expected $)
- Status indicator
- Next deadline

### Tab 2: Client Process Map 🗺️
**Purpose:** Visual process map per client showing project journey

**Features:**
- Client selector dropdown
- Visual process flow: Discovery → Quick Win → Phase 2 → Phase 3+
- Stage status: ✅ Complete, 🔄 Current, ⏳ Upcoming
- Integration points and dependencies
- Client contacts (name, role, email)
- Communication log (last contact, next meeting)
- Notes section

**Data Displayed:**
- Process stages per client
- Completion status per stage
- Client contact information
- Meeting history and upcoming meetings

### Tab 3: Opportunity Matrix 📊
**Purpose:** Sales pipeline visualization and opportunity tracking

**Features:**
- Pipeline stages: Lead → Discovery → Proposal → Negotiation → Closed
- Opportunity cards with: Company, Contact, Expected revenue, Probability, Close date
- Weighted revenue calculation (revenue × probability)
- Filter by: Stage, Expected revenue, Owner
- Drag-and-drop to move between stages (Phase 3+)

**Data Displayed:**
- Opportunity name/company
- Contact person
- Pipeline stage
- Expected revenue
- Probability % (e.g., 25% Lead, 50% Discovery, 75% Proposal)
- Expected close date
- Owner/responsible person

### Tab 4: Pricing Strategy 💰
**Purpose:** Pricing reference, ROI calculations, margin tracking

**Features:**
- **Consulting Phase Pricing:** Discovery calls, audits, diagnostic sessions (hourly rates)
- **Deliverable Pricing Table:**
  - Deliverable name/description
  - Client price (what they pay)
  - Our cost (dev time × rate or outsourced)
  - Margin ($ and %)
  - Client ROI (value justification)
- Pricing templates (Quick Win, Phase 2, custom)
- Historical pricing data for reference
- Margin calculator tool

**Data Displayed:**
- Deliverable pricing breakdown
- Margin analysis
- ROI justifications
- Historical pricing trends

### Tab 5: Implementation Objectives & Deadlines 📅
**Purpose:** All active deliverables across all projects with deadlines

**Features:**
- Deliverable list with: Project, Objective, Deadline (internal + client), Status, Owner
- Status: 🔴 Not started, 🟡 In progress, 🔵 Review, ✅ Complete
- Priority indicators: P0 (Ultra-critical), P1 (High), P2 (Medium)
- Deadline proximity warning (overdue, due today, due this week)
- Dependency tracking (blocks/blocked by)
- Filter by: Project, Status, Owner, Priority, Deadline range

**Data Displayed:**
- Objective/deliverable description
- Associated project
- Deadline (internal vs. client-facing)
- Current status
- Assigned owner/developer
- Priority level
- Dependencies

### Tab 6: Development Kanban 🛠️
**Purpose:** Live development status per objective (Kanban board)

**Features:**
- Kanban columns: 📋 Backlog, 🔄 In Progress, 👁️ Review, ✅ Complete
- Cards with: Objective name, Project, Owner, Time (invested vs. estimated), Status
- AutoClaude agent status (if applicable): Running, Complete, Blocked
- Blockers/issues highlighted
- GitHub PR links and status
- Drag-and-drop to update status (Phase 3+)

**Data Displayed:**
- Objective/task name
- Associated project
- Current Kanban column
- Owner/developer
- Time invested vs. estimated
- Blockers or issues
- GitHub PR status (Open, In Review, Merged)
- AutoClaude agent status (if running)

### Tab 7: Final Validation & Sign-Off ✅
**Purpose:** Deliverable acceptance workflow and audit trail

**Features:**
- Deliverable list with validation checklist per item:
  - [ ] Internal QA complete
  - [ ] Client demo scheduled
  - [ ] Client feedback received
  - [ ] Revisions completed
  - [ ] Final sign-off obtained
  - [ ] Payment triggered
- Audit trail: Who approved, when, notes
- Documentation links (demo URLs, sign-off emails, etc.)
- Filter by: Project, Status, Sign-off date

**Data Displayed:**
- Deliverable name
- Associated project and client
- Validation checklist status
- Approval history (who, when, notes)
- Documentation links

---

## Technical Approach

### Build Tools
1. **v0.app** - Rapid UI prototyping and component generation
2. **AutoClaude** - Autonomous development agent for implementation
3. **Trent's Demo Setup** - Internal demo hosting infrastructure

### Tech Stack (Proposed)
- **Frontend:** React + Tailwind CSS (v0.app default)
- **State Management:** React Context or Zustand (simple, fast)
- **Data Source (Phase 1):** JSON files in repo (parsed from markdown)
- **Data Source (Phase 2+):** Lightweight backend (Supabase or Firebase)
- **Deployment:** Vercel or Netlify (via Trent's demo setup)
- **Version Control:** Git (same repo as Claude Code OS)

### Data Strategy
- **Phase 1 (MVP):** Static JSON data manually extracted from markdown files
- **Phase 2 (Interactive):** Editable JSON data store with UI updates
- **Phase 3 (Automated):** Sync with project markdown files, auto-update from commits

### Development Workflow
1. **UI Design:** Use v0.app to generate dashboard layout and components
2. **Export Code:** Export React components from v0.app
3. **Integration:** AutoClaude builds data integration, logic, routing
4. **Deployment:** Push to demo site using Trent's infrastructure
5. **Iteration:** Collect feedback, improve based on usage

---

## Phased Roadmap

### Phase 1: MVP - Read-Only Dashboard (8-12 hours)
**Goal:** Visual overview better than markdown files

**Deliverables:**
- Tab 1 (Projects & Revenue Tracker) fully functional
- Basic project cards with status, revenue, phase
- Simple tab navigation skeleton
- Responsive design (desktop + tablet)
- Deployed to demo site

**Success Criteria:**
- [ ] Can see all projects and revenue in <5 seconds
- [ ] Visual status indicators work
- [ ] Revenue totals calculate correctly
- [ ] Accessible via demo site URL

**Timeline:** Week 1 (targeting early January)

### Phase 2: Full Feature Set (16-24 hours)
**Goal:** Replace manual spreadsheets and scattered docs

**Deliverables:**
- All 7 tabs implemented and functional
- Data pulled from JSON files (manual data entry for now)
- Search and filter capabilities across all tabs
- Print/export functionality
- Improved UI polish and responsiveness

**Success Criteria:**
- [ ] All tabs load and display correct data
- [ ] Search/filter works across tabs
- [ ] Can export data for reports
- [ ] Team prefers dashboard over markdown files

**Timeline:** Week 2-3 (mid-January)

### Phase 3: Interactive Updates (12-16 hours)
**Goal:** Single source of truth for operations

**Deliverables:**
- Editable fields in UI (click to edit)
- Save changes back to JSON data store
- User authentication (if multi-user access needed)
- Activity log/audit trail for changes
- Data validation and error handling

**Success Criteria:**
- [ ] Can update project status from UI
- [ ] Changes persist across sessions
- [ ] Audit trail shows who changed what and when
- [ ] No need to manually edit markdown files

**Timeline:** Week 4-5 (late January)

### Phase 4: Automation Integration (16-24 hours)
**Goal:** Self-updating dashboard

**Deliverables:**
- Sync with Git commits (auto-update project status from markdown files)
- Integration with Notion (if applicable)
- Slack notifications for status changes
- AutoClaude agent status integration (show live agent progress)
- Webhook support for external integrations

**Success Criteria:**
- [ ] Dashboard auto-updates when markdown files change
- [ ] Slack notifications sent for critical status changes
- [ ] AutoClaude agent status visible in Development Kanban
- [ ] Minimal manual data entry required

**Timeline:** Week 6+ (February+)

---

## Success Metrics

### Time Savings
- **Current:** 30-60 min/week answering "where are we?" questions
- **Target:** <5 min/week with dashboard (50-95% reduction)
- **Monthly savings:** 2-4 hours = $100-200 (at $50/hr)

### Visibility Improvements
- **Current:** Revenue status requires manual calculation from files
- **Target:** Real-time revenue visibility in <5 seconds

### Decision Speed
- **Current:** Project prioritization decisions require 30+ min of file reading
- **Target:** Prioritization decisions in <5 min with visual overview

### Team Alignment
- **Current:** Team members ask Architect for project status
- **Target:** Team self-serves project status from dashboard

---

## Strategic Value

### Immediate Benefits
1. **Revenue visibility:** Always know current and projected revenue
2. **Faster decisions:** Visual overview enables quick prioritization
3. **Team alignment:** Everyone sees same project status
4. **Client confidence:** Professional dashboard for check-ins

### Long-Term Benefits
1. **Scalability:** Supports 10+ concurrent projects without complexity increase
2. **Productizable:** Could become a service offering for other agencies
3. **Case study:** Demo for Developer Academy ("How we built our ops dashboard")
4. **Competitive advantage:** Professional operations vs. scattered spreadsheets

### Alignment with Architect Role
- **Reduce administrative overhead:** Dashboard answers questions automatically
- **Enable strategic focus:** Spend time on revenue activities, not status updates
- **Support delivery management:** Track development and validation workflows
- **Protect margins:** Pricing tab ensures profitable project scoping

---

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Data quality issues** | Low - Dashboard shows incorrect data | Start with manual data entry, validate before automating |
| **Scope creep** | Medium - Phase 1 delays | Strict phase boundaries, MVP first |
| **AutoClaude integration complexity** | Medium - Build takes longer than estimated | Use v0.app to reduce UI development time |
| **Team adoption** | High - Dashboard not used | Involve team in design, make it better than current process |
| **Maintenance burden** | Medium - Becomes another system to maintain | Design for low maintenance (static JSON initially) |

---

## Next Steps (Immediate)

### Week of Dec 26-Jan 2
1. [ ] **Review Trent's demo setup documentation** - Understand deployment process
2. [ ] **Define Phase 1 data schema** - Structure for projects, revenue, status
3. [ ] **Create sample data file** - Populate with current projects for testing
4. [ ] **Generate UI in v0.app** - Tab 1 (Projects & Revenue) layout

### Week of Jan 2-9
1. [ ] **Export v0.app code** - Get React components
2. [ ] **AutoClaude Phase 1 build** - Integrate data, deploy to demo site
3. [ ] **Internal testing** - Use dashboard for daily stand-ups
4. [ ] **Collect feedback** - What's working, what needs improvement

---

## Related Documentation

- **Automation Backlog Entry:** `/01-executive-office/automation/internal-automation-backlog.md` (Item #5)
- **Revenue KPIs (Data Source):** `/02-operations/metrics-tracking/january-2026-revenue-kpis.md`
- **Project Inventory (Data Source):** `/01-executive-office/strategic-alignment/strategic-objectives/january-2026-project-inventory.md`
- **Active Projects (Data Source):** `/02-operations/project-management/active-projects/`

---

## Questions for Resolution

1. **Trent's demo setup:** What's the process for deploying to internal demo site? Documentation available?
2. **Multi-user access:** Do we need authentication or is it internal-only (single user)?
3. **Data source priority:** Start with JSON or attempt to parse markdown files directly in Phase 1?
4. **Slack integration:** Do we want Slack notifications in Phase 1 or defer to Phase 4?
5. **Mobile responsive:** Is mobile access a requirement or desktop-only acceptable initially?

---

**Status:** Planning Complete - Ready for Phase 1 Execution
**Next Owner Action:** Review Trent's demo setup, define data schema, generate UI in v0.app
**AutoClaude Ready:** Yes - Can hand off Phase 1 build once UI components and data schema are defined
