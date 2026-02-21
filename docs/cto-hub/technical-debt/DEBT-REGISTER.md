# Technical Debt Register

Last Updated: 2026-02-13

## Overview

This register tracks known technical debt across the AI Agency Sales OS. Items are prioritized by impact and effort.

## Priority Levels
- **P0**: Blocking or causing issues now
- **P1**: Should fix soon, affecting productivity
- **P2**: Would be nice to fix, low impact
- **P3**: Cosmetic or minor, fix when convenient

## Active Debt

### P1 - High Priority

| ID | Description | Location | Impact | Effort | Added |
|----|-------------|----------|--------|--------|-------|
| TD-001 | Notion sync targets need page IDs | `.claude/skills/notion-sync/targets.json` | Can't auto-sync reports | Low | 2026-01-22 |
| TD-002 | TypeScript onboarding agents not deployed | `03-ai-growth-engine/onboarding/agents/` | Agents are specs only | High | 2026-01-22 |
| TD-006 | Missing agentic .env file | `agentic/` | Blocks all agentic module integrations | Low | 2026-02-03 |

### P2 - Medium Priority

| ID | Description | Location | Impact | Effort | Added |
|----|-------------|----------|--------|--------|-------|
| TD-003 | Duplicate templates in client-outreach & speed-to-lead | Commands/Skills | Maintenance burden | Low | 2026-01-22 |
| TD-004 | 15 n8n workflow exports untracked in git | `agentic/extras/n8n-wf/*.json` | Not version controlled | Low | 2026-01-29 |
| TD-005 | Slack bot/user tokens expired | `agentic/.env` | Blocks Slack + client-onboarding | Low | 2026-01-29 |
| TD-007 | TODOs in onboarding agent handlers | `onboarding/agents/*/handlers/*.ts` | PDF attach & Slack invite incomplete | Low | 2026-02-03 |

### P3 - Low Priority

| ID | Description | Location | Impact | Effort | Added |
|----|-------------|----------|--------|--------|-------|
| TD-008 | Deprecated code references in 3 files | Various (cto-sync, engineering-standards, classification-schema) | Code hygiene | Low | 2026-02-03 |

## Resolved Debt

| ID | Description | Resolution | Resolved |
|----|-------------|------------|----------|
| - | - | - | - |

## How to Add Debt

When you discover technical debt during a session:

1. Run `/cto-debt [brief description]`
2. Or manually add to this register with:
   - Unique ID (TD-XXX)
   - Clear description
   - Location in codebase
   - Impact assessment
   - Effort estimate (Low/Medium/High)
   - Date added

## Debt Paydown Strategy

During each sprint/week, aim to:
- Resolve at least 1 P1 item
- Review P2 items for promotion/demotion
- Archive P3 items older than 90 days if not addressed

## Notes

- Debt is normal - this register is for visibility, not shame
- Some debt is strategic (we chose speed over perfection)
- Review this register during `/cto-sync` sessions
