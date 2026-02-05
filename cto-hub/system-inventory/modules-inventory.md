# Agentic Modules Inventory

**Last Updated:** 2026-02-05
**Total Modules:** 14

---

## Module Status

| # | Module | Tools | Env Status | Operational | Notes |
|---|--------|-------|------------|-------------|-------|
| 1 | client-feedback | 1 | ⚠️ Missing DB ID | ⚠️ | NEW - Notion feedback workflow |
| 2 | client-onboarding | 0 | 🔴 Slack expired | 🔴 | Blocked by slack |
| 3 | dashboard | 7 | ✅ | ✅ | Full suite |
| 4 | demo-deploy | 1 | ✅ | ✅ | Dokploy |
| 5 | diagrams | 3 | ✅ | ✅ | Excalidraw, Mermaid, ASCII |
| 6 | infrastructure | 2 | ✅ | ✅ | Cloudflare + Dokploy |
| 7 | leads | 3 | ✅ | ✅ | Apify + Sheets |
| 8 | md-export | 2 | ✅ | ✅ | Google Docs + Word |
| 9 | n8n | 1 | ✅ | ✅ | MCP server |
| 10 | notion | 1 | ✅ | ✅ | Content context |
| 11 | proposal | 2 | ✅ | ✅ | Google Slides |
| 12 | slack | 1 | 🔴 Expired | 🔴 | Needs token refresh |
| 13 | sop | 2 | ✅ | ✅ | Transcription + SOP |
| 14 | ssh | 1 | ✅ | ✅ | Remote commands |

---

## Module Details

### client-feedback (NEW)
- **Location:** agentic/modules/client-feedback/
- **Tool:** feedback_api.py
- **Runbook:** feedback_management.md
- **Env Required:** NOTION_API_KEY, CLIENT_FEEDBACK_DB_ID
- **Dependencies:** notion module

### client-onboarding
- **Location:** agentic/modules/client-onboarding/
- **Status:** BLOCKED - Slack token expired
- **Runbook:** client_onboarding.md

### dashboard
- **Location:** agentic/modules/dashboard/
- **Tools:** 7 (collectors, generators, formatters)
- **Status:** Fully operational

### demo-deploy
- **Location:** agentic/modules/demo-deploy/
- **Tool:** deploy to Dokploy
- **Dependencies:** infrastructure module

### diagrams
- **Location:** agentic/modules/diagrams/
- **Tools:** excalidraw, mermaid, ascii
- **Env Required:** OPENAI_API_KEY

### infrastructure
- **Location:** agentic/modules/infrastructure/
- **Tools:** cloudflare, dokploy
- **Env Required:** CLOUDFLARE_API_TOKEN, DOKPLOY_*

### leads
- **Location:** agentic/modules/leads/
- **Tools:** apify scraper, sheets integration
- **Status:** Operational

### md-export
- **Location:** agentic/modules/md-export/
- **Tools:** gdocs, word export
- **Env Required:** GOOGLE_FOLDER_ID

### n8n
- **Location:** agentic/modules/n8n/
- **Tool:** MCP server integration
- **Env Required:** N8N_API_URL, N8N_API_KEY

### notion
- **Location:** agentic/modules/notion/
- **Tool:** fetch_content_context
- **Env Required:** NOTION_API_KEY

### proposal
- **Location:** agentic/modules/proposal/
- **Tools:** Google Slides generation
- **Env Required:** GOOGLE_SLIDES_TEMPLATE_ID

### slack
- **Location:** agentic/modules/slack/
- **Status:** BLOCKED - Token expired
- **Action:** Refresh at api.slack.com/apps

### sop
- **Location:** agentic/modules/sop/
- **Tools:** transcription, SOP extraction
- **Env Required:** OPENAI_API_KEY

### ssh
- **Location:** agentic/modules/ssh/
- **Tool:** Remote command execution
- **Status:** Operational

---

## Blocked Modules

1. **slack** — Token expired, needs refresh
2. **client-onboarding** — Depends on slack
3. **client-feedback** — Missing CLIENT_FEEDBACK_DB_ID

---

## Python Tool Count

Total: 28 tools across 14 modules
