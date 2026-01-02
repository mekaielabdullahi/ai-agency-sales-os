# Agency Operations Dashboard - Internal Project

**Status:** Planning Complete - Ready for Phase 1 Execution
**Priority:** P1 (Revenue Enablement)
**Created:** December 25, 2025
**Owner:** Matt Kerns (Architect)

---

## Quick Start

### What is this?
Unified internal operations dashboard that consolidates:
- Project tracking
- Revenue management (actual vs. projected)
- Client relationships and process maps
- Pricing strategy and ROI tracking
- Development execution (Kanban)
- Deliverable validation workflow

**Problem:** Revenue and project data scattered across markdown files. Hard to answer "What's our revenue status?" quickly.

**Solution:** Single-page dashboard with visual overview of all projects, revenue, and delivery status.

---

## Project Documentation

| Document | Purpose |
|----------|---------|
| `PROJECT-OVERVIEW.md` | Complete project details, features, roadmap |
| `DATA-SCHEMA.md` | Data models and JSON structure |
| `PHASE-1-MVP-ROADMAP.md` | Detailed Phase 1 build plan (8-12 hours) |
| `UI-MOCKUP-NOTES.md` | v0.app prompts and design guidance |
| `README.md` | This file - quick reference |

---

## Phase 1 MVP Scope

**Goal:** Read-only dashboard with Tab 1 (Projects & Revenue) deployed to demo site

**Features:**
- ✅ Project grid showing all active projects
- ✅ Revenue summary (Received, Projected, Total)
- ✅ Visual status indicators (🟢 On track, 🟡 At risk, 🔴 Critical)
- ✅ Filter by Priority (P0, P1) and Status
- ✅ Tab navigation (Tab 1 active, others "Coming Soon")
- ✅ Responsive design (desktop + tablet)
- ✅ Deployed to demo site

**Timeline:** 8-12 hours (targeting Week 1, early January 2026)

---

## Build Approach

### Tools
1. **v0.app** - Generate UI components (React + Tailwind)
2. **AutoClaude** - Build logic, data integration, deployment
3. **Trent's Demo Setup** - Deploy to internal demo site

### Workflow
1. Matt generates UI in v0.app (2-3 hours)
2. Export React components from v0.app
3. AutoClaude integrates data and builds functionality (4-6 hours)
4. Matt deploys to demo site (1-2 hours)
5. Team tests and provides feedback

---

## Next Steps (Immediate)

### This Week (Dec 26-Jan 2)
1. [ ] **Review Trent's demo setup** - Understand deployment process
2. [ ] **Define Phase 1 data schema** - Finalize JSON structure (see DATA-SCHEMA.md)
3. [ ] **Generate UI in v0.app** - Use prompts from UI-MOCKUP-NOTES.md
4. [ ] **Create sample data file** - Populate with current projects

### Next Week (Jan 2-9)
1. [ ] **AutoClaude Phase 1 build** - Integrate components and data
2. [ ] **Deploy to demo site** - Get live URL
3. [ ] **Internal testing** - Use dashboard for daily stand-ups
4. [ ] **Collect feedback** - Plan Phase 2 priorities

---

## Tech Stack (Phase 1)

- **Framework:** React 18+
- **Styling:** Tailwind CSS
- **State:** React Context (simple, no external libraries)
- **Data:** Static JSON file (`src/data/projects.json`)
- **Build:** Vite
- **Deployment:** Vercel or Netlify (via Trent's demo setup)

---

## Data Sources

**Phase 1 (Manual):**
- `january-2026-revenue-kpis.md` → Revenue data
- `january-2026-project-inventory.md` → Project list
- `active-projects/*/PROJECT-OVERVIEW.md` → Project details

**Phase 2+ (Automated):**
- Parse markdown files automatically
- Sync with Git commits
- GitHub API for PR status
- Notion API (optional)

---

## Success Criteria

Phase 1 is complete when:
- [ ] Can see all projects and revenue in <5 seconds
- [ ] Visual status indicators work correctly
- [ ] Revenue totals calculate accurately
- [ ] Filters work (Priority, Status)
- [ ] Accessible via demo site URL
- [ ] Faster than opening markdown files (validated by team)

---

## Future Phases

### Phase 2: Full Feature Set (16-24 hours)
- All 7 tabs implemented
- Search and filter across tabs
- Print/export functionality

### Phase 3: Interactive Updates (12-16 hours)
- Editable fields in UI
- Save changes back to data store
- Activity log/audit trail

### Phase 4: Automation Integration (16-24 hours)
- Auto-sync with Git commits
- Slack notifications
- AutoClaude agent status integration

---

## Strategic Value

**Immediate:**
- Revenue visibility (always know current and projected revenue)
- Faster decisions (visual overview enables quick prioritization)
- Team alignment (everyone sees same project status)

**Long-term:**
- Scalability (supports 10+ projects without complexity)
- Productizable (could become service offering for other agencies)
- Case study (demo for Developer Academy)

**Time Savings:**
- Current: 30-60 min/week answering "where are we?" questions
- Target: <5 min/week with dashboard
- **Savings:** 2-4 hours/month = $100-200 value

---

## Alignment with Architect Role

**Reduces:**
- Administrative overhead (dashboard answers questions automatically)
- Context switching (all data in one place)
- Team interruptions (self-serve project status)

**Enables:**
- Strategic focus (more time for revenue activities)
- Delivery management (track development and validation)
- Margin protection (pricing tab ensures profitable scoping)

---

## Links & References

**Automation Backlog:**
- `/01-executive-office/automation/internal-automation-backlog.md` (Item #5)

**Data Sources:**
- `/02-operations/metrics-tracking/january-2026-revenue-kpis.md`
- `/01-executive-office/strategic-alignment/strategic-objectives/january-2026-project-inventory.md`
- `/02-operations/project-management/active-projects/`

**Related Projects:**
- Backlog Item #2: Slack → Notion Kanban sync (could feed this dashboard)

---

## Questions for Resolution

1. **Trent's demo setup:** What's the deployment process? Documentation available?
2. **Multi-user access:** Need authentication or internal-only (single user)?
3. **Data source priority:** Start with JSON or parse markdown in Phase 1?
4. **Mobile responsive:** Requirement for Phase 1 or defer to Phase 2?

---

**Status:** ✅ Planning Complete - Ready for Execution
**Next Action:** Generate UI in v0.app, then hand off to AutoClaude
**Target Completion:** January 3, 2026
