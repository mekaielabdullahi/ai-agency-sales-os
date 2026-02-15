# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **AI Agency Sales OS** - an AI-powered Business Operating System for AriseGroup.ai, an AI transformation consulting agency. The repository contains strategic frameworks, sales systems, content strategies, and operational documentation for systematic AI adoption consulting.

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
- **`/docs/`** - Setup guides and documentation
- **`/.claude/skills/`** - Claude Code skills for specialized workflows

## Claude Code Skills

The repository has 5 custom skills configured in `.claude/skills/`. Use these for specialized tasks:

| Skill | Use When |
|-------|----------|
| `business-functions-mapping` | Analyzing organizations, mapping operations, conducting AI Readiness Audits |
| `client-outreach` | Planning outreach campaigns, drafting LinkedIn/email messages, managing sales pipeline |
| `comprehensive-ai-audit` | Running full paid audits using the structured audit.json workflow |
| `content-strategy` | Planning content calendars, drafting LinkedIn posts, creating hooks |
| `weekly-planning` | Creating strategic weekly plans and roadmaps |

Invoke skills by name when the user's request matches the skill's purpose.

## Core Principles

The system operates on 4 foundational principles:

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

This is a **documentation and framework repository** - no build commands, tests, or linting. The "code" here is markdown documentation, strategic frameworks, prompt templates, and operational guides.

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

## Monthly Maintenance Tasks

- [ ] **WhatsApp Export** (1st of each month)
  - Export "AAA Agency" WhatsApp chat
  - Select "Without Media" for text-only export
  - Unzip and store `_chat.txt` in `shared-resources/team-context/whatsapp-exports/YYYY-MM/`
  - Full media exports stored locally if needed for reference
