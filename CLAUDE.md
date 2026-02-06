# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository Overview

**AI Agency Sales OS** — an AI-powered Business Operating System for AriseGroup.ai, an AI transformation consulting agency. Contains strategic frameworks, sales systems, content strategies, and operational documentation for systematic AI adoption consulting.

## Agent Team Architecture

This repo is structured for **Claude Code Agent Teams**. The team lead coordinates four specialized teammates, each owning a domain of the business.

### Team Structure

```
                         ┌─────────────┐
                         │  TEAM LEAD  │
                         │ (You)       │
                         │ Orchestrate │
                         │ & delegate  │
                         └──────┬──────┘
                                │
          ┌─────────────┬───────┴───────┬─────────────┐
          │             │               │             │
   ┌──────▼──────┐ ┌───▼────────┐ ┌────▼─────┐ ┌────▼──────┐
   │   SALES     │ │   AUDIT    │ │ CONTENT  │ │   OPS     │
   │  Teammate   │ │  Teammate  │ │ Teammate │ │ Teammate  │
   │             │ │            │ │          │ │           │
   │ Outreach    │ │ AI Audits  │ │ LinkedIn │ │ Dashboard │
   │ Pipeline    │ │ Biz Maps   │ │ Brand    │ │ Planning  │
   │ Proposals   │ │ Discovery  │ │ Publish  │ │ Reports   │
   │ Leads       │ │ Roadmaps   │ │ Strategy │ │ Onboarding│
   └─────────────┘ └────────────┘ └──────────┘ └───────────┘
```

### When to Spawn Teams

Use agent teams when the task naturally splits across domains:

| Scenario | Team Config |
|----------|-------------|
| **Full client engagement** | All 4 teammates: Sales preps proposal, Audit maps processes, Content creates case study, Ops sets up onboarding |
| **Weekly business review** | Ops (dashboard + report) + Content (performance review) + Sales (pipeline update) |
| **New client AI audit** | Audit (process mapping + opportunities) + Sales (proposal from findings) |
| **Content campaign** | Content (posts + illustrations) + Sales (outreach alignment) |
| **Client onboarding** | Ops (project setup) + Audit (discovery mapping) |

### How to Spawn

Tell the lead in natural language. Examples:

```
Create an agent team for a full client engagement with Acme Corp.
Spawn the sales, audit, content, and ops teammates.
Sales should prepare the proposal, audit should map their processes,
content should draft a case study angle, ops should prep onboarding.
```

```
Spawn the audit and sales teammates. Audit maps the client's business
functions from the discovery notes. Sales drafts a proposal based on
audit findings. Have audit share findings with sales as they go.
```

### Team Lead Responsibilities

As team lead, you:
1. **Route requests** to the right teammate(s) based on domain
2. **Coordinate handoffs** — audit findings feed into sales proposals, content pulls from audit results
3. **Synthesize results** — combine teammate outputs into cohesive deliverables
4. **Use delegate mode** (`Shift+Tab`) when teammates should do all the work

### Teammate Communication Patterns

Teammates should message each other directly for cross-domain work:

- **Audit → Sales**: Share opportunity matrix so Sales can build proposals from it
- **Audit → Content**: Share client transformation story for case study posts
- **Sales → Ops**: Hand off closed deals for onboarding setup
- **Content → Sales**: Align outreach messaging with content themes
- **Ops → All**: Share weekly metrics and dashboard data

## Directory Structure

```
/arisegroup/                    # AriseGroup-specific operations
/claude-code-os-implementation/ # 10-department system implementation
/agentic/                       # 3-layer module system (runbooks → orchestration → tools)
/docs/                          # Setup guides
/.claude/skills/                # 12 specialized skills
/.claude/agents/                # 4 teammate agent definitions
/.claude/commands/              # 9 slash commands
```

## Agentic Module System

The `agentic/` directory uses a 3-layer architecture. See `agentic/CLAUDE.md` for details.

- **Layer 1: Runbooks** — SOPs in `modules/*/runbook/`
- **Layer 2: Orchestration** — AI decision-making (you)
- **Layer 3: Tools** — Python scripts in `modules/*/tool/`

Always run tools via `./run modules/<name>/tool/<script>.py` (activates venv).

## Skills

| Skill | Domain | Teammate |
|-------|--------|----------|
| `client-outreach` | Sales pipeline, outreach campaigns | Sales |
| `comprehensive-ai-audit` | Full paid AI audits via audit.json | Audit |
| `business-functions-mapping` | Process mapping, AI opportunities | Audit |
| `content-strategy` | LinkedIn content, hooks, calendars | Content |
| `brand-illustrator` | Branded illustrations + post copy | Content |
| `publish` | Post to LinkedIn | Content |
| `dashboard` | Business analytics, metrics | Ops |
| `weekly-planning` | Strategic weekly plans | Ops |
| `weekly-report` | Weekly progress reports | Ops |
| `outreach` | Individual lead processing | Sales |
| `client-feedback` | Client feedback management | Ops |
| `notion-sync` | Notion data sync | Ops |

## Modules → Teammate Mapping

| Module | Teammate |
|--------|----------|
| `leads`, `proposal` | Sales |
| `client-onboarding`, `client-feedback` | Ops |
| `dashboard`, `sop`, `md-export` | Ops |
| `slack`, `notion`, `google` | Ops |
| `n8n`, `infrastructure`, `ssh` | Ops |
| `diagrams`, `demo-deploy` | Ops |

## Core Principles

1. **Entropy Principle** — Accept imperfection, focus on what matters
2. **Zero Friction** — Remove barriers to create sustainable discipline
3. **Spartan Rule** — Lean operations with brutal prioritization
4. **Strategic Alignment** — Every action serves the OBG

## Key Concepts

- **OBG** — One Big Obsessional Goal: the singular strategic focus
- **Tier 1/2/3 Tasks** — Priority-based organization (Tier 1 = 20% of tasks, 80% of impact)
- **AI Readiness Audit** — Discovery framework for mapping operations to AI opportunities
- **Build-in-Public** — Transparent content strategy documenting the journey
