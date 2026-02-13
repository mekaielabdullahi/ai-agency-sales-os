# Skills Inventory

**Last Updated:** 2026-02-13
**Total Skills:** 13

---

## Active Skills

| # | Skill | Location | Status | Dependencies |
|---|-------|----------|--------|--------------|
| 1 | brand-illustrator | .claude/skills/brand-illustrator/ | ✅ Active | Pollinations, Excalidraw |
| 2 | business-functions-mapping | .claude/skills/business-functions-mapping/ | ✅ Active | None |
| 3 | client-feedback | .claude/skills/client-feedback/ | ⚠️ Needs DB ID | Notion API, CLIENT_FEEDBACK_DB_ID |
| 4 | client-outreach | .claude/skills/client-outreach/ | ✅ Active | Gmail MCP, Notion API |
| 5 | comprehensive-ai-audit | .claude/skills/comprehensive-ai-audit/ | ✅ Active | None |
| 6 | content-strategy | .claude/skills/content-strategy/ | ✅ Active | Notion API |
| 7 | dashboard | .claude/skills/dashboard/ | ✅ Active | Multiple APIs |
| 8 | notion-sync | .claude/skills/notion-sync/ | ⚠️ Partial | Notion API, Page IDs (TD-001) |
| 9 | outreach | .claude/skills/outreach/ | ✅ Active | Gmail MCP, Notion API |
| 10 | publish | .claude/skills/publish/ | ✅ Active | LinkedIn, Chrome MCP |
| 11 | weekly-planning | .claude/skills/weekly-planning/ | ✅ Active | None |
| 12 | tasks | .claude/skills/tasks/ | ✅ Active | Notion API |
| 13 | weekly-report | .claude/skills/weekly-report/ | ✅ Active | Notion API |

---

## Skill Details

### brand-illustrator
- **Purpose:** Generate branded content packages (illustrations + copy + hashtags + CTAs) in "Warm Tech" style
- **Outputs:** PNG images, post copy, hashtags
- **Integrations:** Pollinations (image gen), Excalidraw, LinkedIn
- **Recent:** Discovery Process post (Feb 6), One Technician Problem post (Feb 5)

### business-functions-mapping
- **Purpose:** Map business operations to AI opportunities
- **Outputs:** Function maps, opportunity matrices, AI readiness assessments

### client-feedback
- **Purpose:** Manage client testing feedback via Notion database
- **Commands:** query, triage, respond, resolve, stats
- **Requires:** CLIENT_FEEDBACK_DB_ID in .env
- **Status:** Schema ready, awaiting database ID configuration

### client-outreach
- **Purpose:** Systematic sales outreach, discovery calls, pipeline management
- **Integrations:** Gmail drafts, Notion tasks, LinkedIn messaging

### comprehensive-ai-audit
- **Purpose:** Full paid AI audit workflow using structured audit.json
- **Outputs:** Audit reports, executive summaries, implementation roadmaps

### content-strategy
- **Purpose:** LinkedIn content planning and creation (build-in-public strategy)
- **Integrations:** Notion content calendar, fetch_content_context

### dashboard
- **Purpose:** Business analytics dashboards (Executive, Sales, Marketing, Financial, Operations, Support)
- **Integrations:** Multiple data sources, Slack summary posting

### notion-sync
- **Purpose:** Push markdown documents to Notion pages
- **Status:** Partial - needs page IDs configured (TD-001)

### outreach
- **Purpose:** Universal lead outreach (direct input + Notion pull)
- **Integrations:** Gmail drafts, Notion lead/task management, WebFetch (company research)
- **Features:** Graceful fallbacks when services unavailable

### publish
- **Purpose:** Post brand-illustrator output to LinkedIn
- **Integrations:** LinkedIn, Chrome MCP (browser automation), Slack notifications

### weekly-planning
- **Purpose:** Strategic weekly plans with daily breakdowns and energy management
- **Integrations:** Executive Office systems

### tasks
- **Purpose:** Pull Notion tasks, leads, projects, and meetings into a prioritized dashboard
- **Commands:** `/tasks`, `/tasks today`, `/tasks overdue`, `/tasks [project]`, `/tasks update`
- **Integrations:** Notion API (Tasks DB, Leads DB, Projects DB, Meetings DB)

### weekly-report
- **Purpose:** Auto-generate weekly progress reports from project folders
- **Integrations:** Project file system, Slack, Notion (optional sync)

---

## Integration Matrix

| Integration | Skills Using It |
|-------------|-----------------|
| **Notion** | client-feedback, client-outreach, content-strategy, dashboard, notion-sync, outreach, publish, tasks, weekly-report |
| **LinkedIn** | brand-illustrator, client-outreach, content-strategy, outreach, publish |
| **Gmail** | client-outreach, outreach |
| **Slack** | dashboard, publish, weekly-report |
| **Chrome MCP** | publish |

---

## Issues

1. **notion-sync** needs page IDs for full functionality (TD-001)
2. **client-feedback** needs CLIENT_FEEDBACK_DB_ID configured
