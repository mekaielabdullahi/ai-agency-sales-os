# Integrations Inventory

**Last Updated:** 2026-02-12

---

## External Services

| Service | Method | Status | Used By |
|---------|--------|--------|---------|
| **Notion** | API (Bot) | ✅ Active | notion, client-feedback, content-strategy, outreach, dashboard, weekly-report |
| **Gmail** | MCP Server | ✅ Active | outreach, client-outreach |
| **LinkedIn** | Chrome MCP | ✅ Active | publish, brand-illustrator, content-strategy |
| **Slack** | API (Bot+User) | 🔴 Expired | slack, client-onboarding, dashboard |
| **n8n** | MCP Server | ✅ Active | n8n module (15 workflow exports) |
| **Google Slides** | API | ✅ Active | proposal |
| **Google Docs** | API | ✅ Active | md-export |
| **Cloudflare** | API | ✅ Active | infrastructure (DNS + tunnels) |
| **Dokploy** | API | ✅ Active | infrastructure, demo-deploy |
| **Apify** | API | ✅ Active | leads (web scraping) |
| **Google Sheets** | API | ✅ Active | leads (data storage) |
| **OpenAI** | API | ✅ Active | diagrams, sop (transcription) |
| **NotebookLM** | Unofficial CLI | ⚠️ Prototype | notebooklm |
| **Pollinations** | API | ✅ Active | brand-illustrator (image generation) |
| **GitHub** | Git + Remote | ✅ Active | Source control, matthew remote |

---

## Environment Variables

| Variable | Status | Modules |
|----------|--------|---------|
| NOTION_API_KEY | ✅ Configured | notion, client-feedback, dashboard |
| OPENAI_API_KEY | ✅ Configured | diagrams, sop |
| GOOGLE_SLIDES_TEMPLATE_ID | ✅ Configured | proposal |
| GOOGLE_FOLDER_ID | ✅ Configured | md-export |
| CLOUDFLARE_API_TOKEN | ✅ Configured | infrastructure |
| CLOUDFLARE_ACCOUNT_ID | ✅ Configured | infrastructure |
| DOKPLOY_URL | ✅ Configured | infrastructure, demo-deploy |
| DOKPLOY_API_KEY | ✅ Configured | infrastructure, demo-deploy |
| N8N_API_URL | ✅ Configured | n8n |
| N8N_API_KEY | ✅ Configured | n8n |
| APIFY_TOKEN | ✅ Configured | leads |
| SSH_KEY_PATH | ✅ Configured | ssh |
| CLIENT_FEEDBACK_DB_ID | ❌ Missing | client-feedback |
| GOOGLE_AUTH_TOKEN | ❌ Missing | notebooklm |
| SLACK_BOT_TOKEN | 🔴 Expired | slack, client-onboarding, dashboard |
| SLACK_USER_TOKEN | 🔴 Expired | slack, client-onboarding |

---

## MCP Servers

| Server | Purpose | Status |
|--------|---------|--------|
| Gmail | Email operations | ✅ Active |
| n8n | Workflow management | ✅ Active |
| Chrome (Claude in Chrome) | Browser automation for LinkedIn | ✅ Active |

---

## Git Remotes

| Remote | URL Target | Status |
|--------|-----------|--------|
| origin | GitHub (primary) | ✅ Active |
| matthew | Matthew's remote | ✅ Active |

---

## Integration Health Summary

| Status | Count | Services |
|--------|-------|----------|
| ✅ Healthy | 12 | Notion, Gmail, LinkedIn, n8n, Google Slides/Docs, Cloudflare, Dokploy, Apify, Sheets, OpenAI, Pollinations, GitHub |
| ⚠️ Degraded | 1 | NotebookLM (prototype) |
| 🔴 Broken | 1 | Slack (token expired) |
