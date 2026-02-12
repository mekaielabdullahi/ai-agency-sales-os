# Agentic Modules Inventory

**Last Updated:** 2026-02-12
**Total Modules:** 15
**Total Python Tools:** 29

---

## Module Status

| # | Module | Tools | Env Status | Operational | Notes |
|---|--------|-------|------------|-------------|-------|
| 1 | client-feedback | 1 | ⚠️ Missing DB ID | ⚠️ | Notion feedback workflow |
| 2 | client-onboarding | 0 | 🔴 Slack expired | 🔴 | Blocked by slack module |
| 3 | dashboard | 7 | ✅ | ✅ | Full suite (collectors, generators, formatters) |
| 4 | demo-deploy | 1 | ✅ | ✅ | Dokploy + GitHub integration |
| 5 | diagrams | 3 | ✅ | ✅ | Excalidraw, Mermaid, ASCII |
| 6 | infrastructure | 2 | ✅ | ✅ | Cloudflare + Dokploy |
| 7 | leads | 3 | ✅ | ✅ | Apify + Google Sheets |
| 8 | md-export | 2 | ✅ | ✅ | Google Docs + Word |
| 9 | n8n | 1 | ✅ | ✅ | MCP server configured |
| 10 | notion | 1 | ✅ | ✅ | Pages, databases, blocks, search |
| 11 | notebooklm | 0 | ⚠️ Needs auth | ⚠️ | Prototype, undocumented Google APIs |
| 12 | proposal | 2 | ✅ | ✅ | Google Slides generation |
| 13 | slack | 1 | 🔴 Token expired | 🔴 | Needs token refresh |
| 14 | sop | 2 | ✅ | ✅ | Audio transcription + SOP extraction |
| 15 | ssh | 1 | ✅ | ✅ | Remote commands + SFTP |

---

## Module Details

### client-feedback
- **Location:** agentic/modules/client-feedback/
- **Tool:** feedback_api.py
- **Runbook:** feedback_management.md
- **Env Required:** NOTION_API_KEY ✅, CLIENT_FEEDBACK_DB_ID ❌
- **Dependencies:** notion module

### client-onboarding
- **Location:** agentic/modules/client-onboarding/
- **Status:** BLOCKED - Slack token expired
- **Runbook:** client_onboarding.md
- **Env Required:** SLACK_BOT_TOKEN 🔴, SLACK_USER_TOKEN 🔴

### dashboard
- **Location:** agentic/modules/dashboard/
- **Tools:** 7 (collectors, generators, formatters)
- **Env Required:** NOTION_API_KEY ✅, SLACK_BOT_TOKEN 🔴
- **Status:** Fully operational (Slack posting degraded)

### demo-deploy
- **Location:** agentic/modules/demo-deploy/
- **Tool:** deploy to Dokploy
- **Env Required:** DOKPLOY_URL ✅, DOKPLOY_API_KEY ✅
- **Dependencies:** infrastructure module

### diagrams
- **Location:** agentic/modules/diagrams/
- **Tools:** excalidraw, mermaid, ascii
- **Env Required:** OPENAI_API_KEY ✅

### infrastructure
- **Location:** agentic/modules/infrastructure/
- **Tools:** cloudflare, dokploy
- **Env Required:** CLOUDFLARE_API_TOKEN ✅, CLOUDFLARE_ACCOUNT_ID ✅, DOKPLOY_URL ✅, DOKPLOY_API_KEY ✅

### leads
- **Location:** agentic/modules/leads/
- **Tools:** apify scraper, sheets integration, data enrichment
- **Env Required:** APIFY_TOKEN ✅

### md-export
- **Location:** agentic/modules/md-export/
- **Tools:** Google Docs export, Word export
- **Env Required:** GOOGLE_FOLDER_ID ✅

### n8n
- **Location:** agentic/modules/n8n/
- **Tool:** MCP server integration
- **Env Required:** N8N_API_URL ✅, N8N_API_KEY ✅

### notion
- **Location:** agentic/modules/notion/
- **Tool:** fetch_content_context (pages, databases, blocks, search)
- **Env Required:** NOTION_API_KEY ✅

### notebooklm
- **Location:** agentic/modules/notebooklm/
- **Tool:** notebooklm_client.py (unofficial Python CLI)
- **Command:** notebooklm-process
- **Env Required:** GOOGLE_AUTH_TOKEN ⚠️ (optional, set after `notebooklm auth`)
- **n8n Workflow:** notebooklm_meeting_processor.json
- **Integration doc:** cto-hub/workflows/notebooklm-integration.md
- **Status:** Prototype - uses undocumented Google APIs

### proposal
- **Location:** agentic/modules/proposal/
- **Tools:** Google Slides generation, template rendering
- **Env Required:** GOOGLE_SLIDES_TEMPLATE_ID ✅

### slack
- **Location:** agentic/modules/slack/
- **Status:** BLOCKED - Token expired
- **Action:** Refresh at api.slack.com/apps
- **Env Required:** SLACK_BOT_TOKEN 🔴, SLACK_USER_TOKEN 🔴

### sop
- **Location:** agentic/modules/sop/
- **Tools:** audio transcription, SOP extraction
- **Env Required:** OPENAI_API_KEY ✅

### ssh
- **Location:** agentic/modules/ssh/
- **Tool:** Remote command execution + SFTP
- **Env Required:** SSH_KEY_PATH ✅ (or SSH_PASSWORD)

---

## Blocked Modules

1. **slack** — Token expired, needs refresh (TD-005)
2. **client-onboarding** — Depends on slack
3. **client-feedback** — Missing CLIENT_FEEDBACK_DB_ID
4. **notebooklm** — Prototype, needs GOOGLE_AUTH_TOKEN

---

## Agentic Commands (25)

Commands in `agentic/.claude/commands/`:

| Command | Module | Purpose |
|---------|--------|---------|
| client-setup | client-onboarding | Set up client channels |
| dashboard | dashboard | Generate dashboard |
| demo-deploy | demo-deploy | Deploy demo app |
| diagram | diagrams | Generate diagram |
| dns-list | infrastructure | List DNS records |
| drawio | diagrams | Generate Excalidraw |
| extract-sop | sop | Extract SOP from recording |
| md-to-gdoc | md-export | Export to Google Docs |
| md-to-word | md-export | Export to Word |
| mermaid | diagrams | Generate Mermaid diagram |
| migrate-ascii | diagrams | Migrate ASCII diagram |
| notion-search | notion | Search Notion |
| notebooklm-process | notebooklm | Process meeting transcript |
| proposal | proposal | Generate proposal |
| sandbox-add | infrastructure | Add sandbox |
| sandbox-remove | infrastructure | Remove sandbox |
| scrape-leads | leads | Scrape leads |
| slack | slack | Slack operations |
| transcribe | sop | Transcribe audio |
| tunnel-status | infrastructure | Check tunnel status |
| workflow-activate | n8n | Activate n8n workflow |
| workflow-deploy | n8n | Deploy n8n workflow |
| workflow-execute | n8n | Execute n8n workflow |
| workflow-history | n8n | View workflow history |
| workflow-list | n8n | List n8n workflows |

---

## n8n Workflow Exports (15)

Located in `agentic/extras/n8n-wf/`:

| Workflow | Status |
|----------|--------|
| client_onboarding.json | Exported |
| client_onboarding_email_sequence.json | Exported |
| content_repurposing.json | Exported |
| daily_content_reminder.json | Exported |
| email_classifier.json | Exported |
| email_weekly_report.json | Exported |
| generate_proposal_mcp.json | Exported |
| invoice_tracking.json | Exported |
| notebooklm_meeting_processor.json | Exported |
| nurture_sequence.json | Exported |
| post_call_followup.json | Exported |
| pre_meeting_sequence.json | Exported |
| proposal_assembly.json | Exported |
| sales_interaction_agent.json | Exported |
| tally_lead_notification.json | Exported |

**Note:** TD-004 referenced 8 exports but count has grown to 15.
