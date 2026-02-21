# Agents Inventory

**Last Updated:** 2026-02-13
**Total Defined Agents:** ~30
**Fully Documented (Markdown):** 3
**TypeScript Agents:** 4 (undeployed)
**Role Prompts:** 6

---

## Executive Office (01-executive-office)

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| **daily-planner-agent** | Generate focused daily roadmaps using "THE ONE THING" framework | Full Markdown | Spec |
| **weekly-strategist-agent** | Create strategic weekly execution plans with day-by-day roadmaps | Full Markdown | Spec |

---

## Operations (02-operations)

### Discovery Process Agents

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| business-functions-mapping-agent | Map business operations to AI opportunities | Markdown | Spec |
| comprehensive-ai-audit-agent | Conduct paid AI audits with structured workflow | Markdown | Spec |
| post-discovery-update-agent | Generate post-discovery summaries | Markdown | Spec |
| project-manager-agent | Manage project lifecycle | Markdown | Spec |
| project-update-agent | Generate project status updates | Markdown | Spec |

### Metrics & Productivity

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| metrics-analyst-agent | Track and analyze business metrics | Markdown | Spec |
| productivity-assessor-agent | Evaluate daily work against OBG ($50k/month) | Markdown | Spec |

### Internal Projects

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| self-discovery-audit | Analyze codebase for self-improvement | Markdown | Spec |
| analyzer-agent | Analyze discovered information | Markdown | Spec |
| crawler-agent | Crawl and index codebase | Markdown | Spec |
| synthesizer-agent | Synthesize analysis results | Markdown | Spec |

### Active Project Audit Agents

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| ai-audit-framework-agent (plotter-mechanix) | Audit framework for Plotter Mechanix | Markdown | Spec |
| ai-audit-framework-agent (remus-development) | Audit framework for Remus Development | Markdown | Spec |

---

## AI Growth Engine (03-ai-growth-engine)

### Sales Agents

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| client-batch-analysis-agent | Batch analyze prospect data | Markdown | Spec |
| sales-analyst-prospect-qualification-agent | Qualify prospects using 5-Question Discovery Framework | Markdown | Spec |

### Onboarding Agents (TypeScript)

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| client-communication-agent | Handle client communications | TypeScript | ⚠️ Not Deployed (TD-002) |
| onboarding-agent | Orchestrate onboarding flow | TypeScript | ⚠️ Not Deployed (TD-002) |
| project-management-agent | Set up project infrastructure | TypeScript | ⚠️ Not Deployed (TD-002) |
| security-agent | Handle security & access | TypeScript | ⚠️ Not Deployed (TD-002) |

---

## Content Team (04-content-team)

### Full Agents

| Agent | Purpose | Format | Status |
|-------|---------|--------|--------|
| **content-strategy-alignment-agent** | Detect strategic pivots, trigger bridge posts | Full Markdown | Spec |

### Role Prompts

| Prompt | Purpose | Status |
|--------|---------|--------|
| content-director-agent | Content direction and strategy | Prompt |
| editor-agent | Copy editing and review | Prompt |
| email-copywriter-agent | Email copy creation | Prompt |
| hook-specialist-agent | LinkedIn hook writing | Prompt |
| social-media-manager-agent | Social media management | Prompt |
| video-script-writer-agent | Video script writing | Prompt |

---

## Summary by Status

| Status | Count | Notes |
|--------|-------|-------|
| Full Markdown Specs | 3 | daily-planner, weekly-strategist, content-strategy-alignment |
| Markdown Specs (Standard) | ~17 | Discovery, metrics, internal, sales |
| TypeScript (Undeployed) | 4 | Onboarding agents — TD-002 |
| Role Prompts | 6 | Content team prompts |
| **Total** | **~30** | |

---

## Notes

- No agents are deployed as autonomous services — all are specification documents
- TypeScript onboarding agents need deployment infrastructure (TD-002)
- Agent creation guide template available at `09-templates/agent-creation-guide.md`
