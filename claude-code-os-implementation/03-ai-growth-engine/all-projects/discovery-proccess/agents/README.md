# Project Management Agents

## Agent Overview

The AI Agency Development OS uses two specialized agents to manage project pipeline and keep project data current:

### 1. Project Update Agent
**Purpose:** Keep individual project folders current based on meeting notes and updates

**Use when:**
- You have meeting notes or transcripts to process
- Project status has changed
- Client provided feedback or made decisions
- New action items or blockers emerged
- Deal closed, stalled, or moved stages

**What it does:**
- Creates meeting notes in proper folders
- Updates relevant project files (README, ACTION-ITEMS, PROJECT-OVERVIEW, etc.)
- Maintains consistency across all project files
- Reorganizes project structure when moving between pipeline stages
- Flags when projects should move between active/incubated/deferred

**Example prompts:**
- "Update Concrete CEO project with these meeting notes: [paste transcript]"
- "Ascension Capital deal closed, invoice sent for $5K, update project files"
- "David hasn't responded in 30 days, update Equipment Share project status"

---

### 2. Project Manager Agent
**Purpose:** Generate portfolio reports and surface pipeline health issues

**Use when:**
- You need weekly/monthly status reports
- You want to see overall pipeline health
- You need to check OBG progress ($50k/mo goal)
- You want recommendations on what to focus on
- You need to identify blockers across all projects

**What it does:**
- Reads all project folders across active/incubated/deferred stages
- Aggregates data into portfolio reports
- Flags pipeline management issues (hoarding, stale projects, etc.)
- Recommends actions to keep pipeline moving
- Tracks revenue progress toward OBG

**Example prompts:**
- "Generate weekly project portfolio status report"
- "What's our current pipeline health? Are we on track for $50k this month?"
- "Which incubated projects should I push to close this week?"
- "Show me all projects that need pipeline stage changes"

---

## When to Use Which Agent

| Scenario | Use This Agent |
|----------|----------------|
| Just had a client meeting | **Project Update Agent** |
| Need to process meeting transcript | **Project Update Agent** |
| Client made a decision or provided feedback | **Project Update Agent** |
| Deal closed or stalled | **Project Update Agent** |
| Project scope or timeline changed | **Project Update Agent** |
| Weekly pipeline review | **Project Manager Agent** |
| Need to see all active projects | **Project Manager Agent** |
| Check OBG progress | **Project Manager Agent** |
| Identify what to focus on this week | **Project Manager Agent** |
| Monthly portfolio review | **Project Manager Agent** |

---

## Agent Workflow

```
Meeting with Client
    ↓
Project Update Agent processes notes
    ↓
Project files updated and consistent
    ↓
Project Manager Agent reads updated data
    ↓
Portfolio reports show current status
    ↓
User makes decisions based on reports
```

---

## Quick Start

### Weekly Routine

**Monday:**
1. Use **Project Manager Agent** to generate weekly status report
2. Identify priorities and blockers for the week

**Throughout Week:**
1. After each client meeting, use **Project Update Agent** to process notes
2. Update project files as status changes

**Friday:**
1. Use **Project Update Agent** to process any final meeting notes
2. Use **Project Manager Agent** for weekly pipeline review
3. Review incubated projects: which to push, which to archive?
4. Plan next week's priorities

---

## File Locations

- **[project-manager-agent.md](./project-manager-agent.md)** - Portfolio reporting and pipeline health
- **[project-update-agent.md](./project-update-agent.md)** - Processing updates and maintaining project folders

---

## Key Principles

### Project Update Agent
✅ **DO:** Process meeting notes, update project files, flag stage changes, maintain consistency
❌ **DON'T:** Generate portfolio reports, track OBG progress, aggregate across projects

### Project Manager Agent
✅ **DO:** Generate reports, aggregate data, surface trends, recommend actions
❌ **DON'T:** Update project files, process meeting notes, edit action items

**Remember:** Project Update Agent maintains the data, Project Manager Agent reports on it.

---

**Last Updated:** 2024-12-15
