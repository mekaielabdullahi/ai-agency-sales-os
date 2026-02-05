# Skills Inventory

**Last Updated:** 2026-02-05
**Total Skills:** 12

---

## Active Skills

| # | Skill | Location | Status | Dependencies |
|---|-------|----------|--------|--------------|
| 1 | brand-illustrator | .claude/skills/brand-illustrator/ | ✅ Active | OpenAI API |
| 2 | business-functions-mapping | .claude/skills/business-functions-mapping/ | ✅ Active | None |
| 3 | client-feedback | .claude/skills/client-feedback/ | ⚠️ New | Notion API, CLIENT_FEEDBACK_DB_ID |
| 4 | client-outreach | .claude/skills/client-outreach/ | ✅ Active | Gmail MCP |
| 5 | comprehensive-ai-audit | .claude/skills/comprehensive-ai-audit/ | ✅ Active | None |
| 6 | content-strategy | .claude/skills/content-strategy/ | ✅ Active | Notion API |
| 7 | dashboard | .claude/skills/dashboard/ | ✅ Active | Multiple APIs |
| 8 | notion-sync | .claude/skills/notion-sync/ | ⚠️ Partial | Notion API, Page IDs |
| 9 | outreach | .claude/skills/outreach/ | ✅ Active | Gmail MCP, Notion API |
| 10 | publish | .claude/skills/publish/ | ✅ Active | LinkedIn API |
| 11 | weekly-planning | .claude/skills/weekly-planning/ | ✅ Active | None |
| 12 | weekly-report | .claude/skills/weekly-report/ | ✅ Active | Notion API |

---

## Skill Details

### brand-illustrator
- **Purpose:** Generate branded content (illustrations + copy)
- **Style:** Warm Tech aesthetic
- **Outputs:** PNG images, post copy, hashtags

### business-functions-mapping
- **Purpose:** Map business operations to AI opportunities
- **Outputs:** Function maps, opportunity matrices

### client-feedback (NEW)
- **Purpose:** Manage client testing feedback via Notion database
- **Commands:** query, triage, respond, resolve, stats
- **Requires:** CLIENT_FEEDBACK_DB_ID in .env

### client-outreach
- **Purpose:** Systematic sales outreach and pipeline management
- **Integrations:** Gmail drafts, Notion tasks

### comprehensive-ai-audit
- **Purpose:** Full paid AI audit workflow
- **Outputs:** Audit reports, recommendations

### content-strategy
- **Purpose:** LinkedIn content planning and creation
- **Integrations:** Notion content calendar

### dashboard
- **Purpose:** Business analytics and metrics
- **Collectors:** Multiple data sources

### notion-sync
- **Purpose:** Push markdown to Notion
- **Status:** Partial - needs page IDs configured

### outreach
- **Purpose:** Universal lead outreach
- **Integrations:** Gmail, Notion
- **Features:** Graceful fallbacks

### publish
- **Purpose:** Post content to LinkedIn
- **Inputs:** brand-illustrator outputs

### weekly-planning
- **Purpose:** Strategic weekly plans
- **Outputs:** Weekly plan documents

### weekly-report
- **Purpose:** Auto-generate weekly reports
- **Integrations:** Notion, project folders

---

## Issues

1. **notion-sync** needs page IDs for full functionality
2. **client-feedback** needs CLIENT_FEEDBACK_DB_ID configured
