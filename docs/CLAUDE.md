# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **AI Agency Sales OS** - an AI-powered Business Operating System for AriseGroup.ai, an AI transformation consulting agency. The repository contains strategic frameworks, sales systems, content strategies, and operational documentation for systematic AI adoption consulting.

## Agent Team Architecture

This repo uses **Claude Code Agent Teams** for orchestration. See the root `CLAUDE.md` for the full team structure.

### Teammates

| Teammate | Agent Definition | Domain |
|----------|-----------------|--------|
| **Sales** | `.claude/agents/sales-teammate.md` | Outreach, pipeline, proposals, leads |
| **Audit** | `.claude/agents/audit-teammate.md` | AI audits, business mapping, roadmaps |
| **Content** | `.claude/agents/content-teammate.md` | LinkedIn, brand, publishing, strategy |
| **Ops** | `.claude/agents/ops-teammate.md` | Dashboard, planning, onboarding, infra |

### Enabling

Agent teams are enabled via `.claude_settings.json`:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

## Architecture

### Core Directories

- **`/arisegroup/`** - AriseGroup-specific operational docs (sales, strategy, operations, templates)
- **`/claude-code-os-implementation/`** - Full system implementation organized into 10 departments:
  - `01-executive-office/` - Strategic planning and daily roadmaps
  - `02-operations/` - Productivity tracking and project management
  - `03-ai-growth-engine/` - Sales engine, client onboarding, audits
  - `04-content-team/` - LinkedIn content creation and brand strategy
  - `05-hr-department/` - AI agent creation framework
  - `06-knowledge-base/` - Core principles and industry insights
  - `07-workflows/` - Daily/weekly/monthly automation routines
  - `08-technical-architecture/` - System design and integrations
  - `09-templates/` - Reusable prompts and agent templates
  - `10-implementation-roadmap/` - Phased rollout plans
- **`/agentic/`** - 3-layer module system (runbooks, orchestration, tools)
- **`/docs/`** - Setup guides and documentation
- **`/.claude/skills/`** - Claude Code skills for specialized workflows
- **`/.claude/agents/`** - Agent team teammate definitions
- **`/.claude/commands/`** - Slash commands

## Claude Code Skills

| Skill | Teammate | Use When |
|-------|----------|----------|
| `client-outreach` | Sales | Planning outreach campaigns, drafting messages, managing pipeline |
| `outreach` | Sales | Processing individual leads with Gmail drafts and Notion tasks |
| `comprehensive-ai-audit` | Audit | Running full paid audits using the structured audit.json workflow |
| `business-functions-mapping` | Audit | Analyzing organizations, mapping operations, AI Readiness Audits |
| `content-strategy` | Content | Planning content calendars, drafting LinkedIn posts, creating hooks |
| `brand-illustrator` | Content | Generating branded illustrations and post copy |
| `publish` | Content | Publishing approved content to LinkedIn |
| `dashboard` | Ops | Weekly reviews, strategic planning, executive overview |
| `weekly-planning` | Ops | Creating strategic weekly plans and roadmaps |
| `weekly-report` | Ops | Generating weekly progress reports |
| `client-feedback` | Ops | Managing client feedback |
| `notion-sync` | Ops | Syncing data with Notion |

## Core Principles

1. **Entropy Principle** - Accept imperfection, focus on what matters
2. **Zero Friction** - Remove barriers to create sustainable discipline
3. **Spartan Rule** - Lean operations with brutal prioritization
4. **Strategic Alignment** - Every action serves the main objective (OBG)

## Key Concepts

- **OBG (One Big Obsessional Goal)** - The singular strategic focus that all work aligns to
- **Tier 1/2/3 Tasks** - Priority-based task organization (Tier 1 = 20% of tasks, 80% of impact)
- **AI Readiness Audit** - Discovery framework for mapping client operations to AI opportunities
- **Build-in-Public** - Content strategy documenting the journey transparently

## Repository Type

This is a **documentation and framework repository** - no build commands, tests, or linting. The "code" here is markdown documentation, strategic frameworks, prompt templates, and operational guides. The `agentic/` directory contains Python tools run via `./run`.

## Working with Client Audits

Client audit files use the `audit.json` schema. When conducting comprehensive audits:
1. Initialize with `client_id` and `audit_brief`
2. Map processes in `current_state_maps`
3. Identify opportunities in `ai_opportunity_matrix`
4. Design solutions in `target_state_designs`
5. Build phased roadmap in `roadmap` (phase_1_quick_wins, phase_2_scale_up, phase_3_strategic)

## Content and Outreach

- LinkedIn posts follow the hook-body-CTA structure
- Outreach uses personalized templates with ICP targeting (20-500 employees, $2M-50M revenue)
- Discovery calls use the Q1-Q5 framework from `/arisegroup/sales/`
