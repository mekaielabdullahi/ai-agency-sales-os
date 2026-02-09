# Agentic Modules Inventory

**Last Updated:** 2026-02-09
**Total Modules:** 15

---

## Module Status

| # | Module | Tools | Env Status | Operational | Notes |
|---|--------|-------|------------|-------------|-------|
| 1 | client-feedback | 1 | ⚠️ Missing DB ID | ⚠️ | Notion feedback workflow |
| 2 | client-onboarding | 0 | 🔴 Slack expired | 🔴 | Blocked by slack |
| 3 | dashboard | 7 | ✅ | ✅ | Full suite |
| 4 | demo-deploy | 1 | ✅ | ✅ | Dokploy |
| 5 | diagrams | 3 | ✅ | ✅ | Excalidraw, Mermaid, ASCII |
| 6 | infrastructure | 2 | ✅ | ✅ | Cloudflare + Dokploy |
| 7 | leads | 3 | ✅ | ✅ | Apify + Sheets |
| 8 | md-export | 2 | ✅ | ✅ | Google Docs + Word |
| 9 | n8n | 1 | ✅ | ✅ | MCP server |
| 10 | notion | 1 | ✅ | ✅ | Content context |
| 11 | notebooklm | 1 | ⚠️ Needs auth | ⚠️ NEW | Meeting processor prototype |
| 12 | proposal | 2 | ✅ | ✅ | Google Slides |
| 13 | slack | 1 | 🔴 Expired | 🔴 | Needs token refresh |
| 14 | sop | 2 | ✅ | ✅ | Transcription + SOP |
| 15 | ssh | 1 | ✅ | ✅ | Remote commands |

---

## Module Details

### client-feedback
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

### notebooklm (NEW)
- **Location:** agentic/modules/notebooklm/
- **Tool:** notebooklm_client.py
- **Commands:** notebooklm-process
- **Env Required:** GOOGLE_AUTH_TOKEN (optional, set after `notebooklm auth`)
- **Status:** Prototype - uses undocumented Google APIs
- **Triggers:** File watch on transcript.md, weekly Monday 8am batch
- **n8n Workflow:** notebooklm_meeting_processor.json
- **Integration doc:** cto-hub/workflows/notebooklm-integration.md

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

1. **slack** — Token expired, needs refresh (TD-005)
2. **client-onboarding** — Depends on slack
3. **client-feedback** — Missing CLIENT_FEEDBACK_DB_ID
4. **notebooklm** — Prototype, needs GOOGLE_AUTH_TOKEN

---

## Python Tool Count

Total: 29 tools across 15 modules (↑1 from notebooklm)
