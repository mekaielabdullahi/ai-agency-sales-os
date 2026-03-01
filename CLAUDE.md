# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Is

This is **Mekaiel Abdullahi's AI Operating System (AIOS)** for **Arise Group** (arisegroup.ai) — an AI implementation and automation agency serving service businesses. The AIOS is a layer of AI automation wrapped around the business, powered by plug-and-play modules.

This workspace combines:
- **Claude Code OS** — Productivity system with 13 core principles, 5 departments
- **AIOS Modules** — ContextOS, DataOS, IntelOS, CommandOS, Daily Brief

**This file (CLAUDE.md) is the foundation.** It is automatically loaded at the start of every session.

---

## The Claude-User Relationship

- **User (Mekaiel)**: Founder & CEO of Arise Group. Solo operator with Pentagon/NATO cybersecurity background. Defines goals around pipeline growth, AI automation delivery, and AIOS buildout.
- **Claude**: Reads context, understands objectives, executes commands, produces outputs, and maintains workspace consistency.

Claude should always orient itself through `/prime` at session start.

---

## AIOS Mission

You are helping Mekaiel build an **AI Operating System (AIOS)** — an autonomous intelligence layer wrapped around his entire business.

### The Problem: The Operator Trap
Most business owners are stuck working IN their business — 80% of bandwidth goes to "must-dos." Nothing left for growth, strategy, or the life they actually wanted.

### The Solution: Five Layers
1. **Context** — Your AI understands the business (strategy, team, processes, history)
2. **Data** — Your AI sees the numbers in real-time (collectors pull from data sources daily)
3. **Intelligence** — Your AI watches everything (meetings, messages, signals) and synthesizes into a daily brief
4. **Automate** — Audit every task, score each one, automate them away one by one
5. **Build** — Freed bandwidth applied to growth, new initiatives, or life

### Three KPIs
- **Away-From-Desk Autonomy** — Hours per day you can step away and nothing falls apart
- **Task Automation %** — Percentage of recurring tasks automated
- **Revenue Per Employee** — Total revenue / team members

---

## Context Summary

**Business:** Arise Group — AI implementation agency for service businesses ($1M-$10M). Solo operator with contractor network.
**Role:** Founder/CEO — strategy, architecture, delivery, sales, operations all run through Mekaiel.
**Current Focus:** Rebuild pipeline from scratch (cold email + warm contacts + door knocking), LinkedIn presence, AIOS buildout.
**Key Metric:** Pipeline — starting from 0, building through 3 channels. Case study: Plotter Mechanix ($5K → $50K revenue enabled).

---

## Workspace Structure

```
.
├── CLAUDE.md                  # This file — core context, always loaded
├── .env                       # API keys and credentials (gitignored)
├── .claude/
│   └── commands/              # Slash commands Claude can execute
│       ├── prime.md           # /prime — load context and orient
│       ├── commit.md          # /commit — save work, update docs
│       ├── task-audit.md      # /task-audit — map tasks for automation
│       └── (existing commands: agentic-*, cto-*, status)
├── context/                   # Business context files
│   ├── business-info.md       # What the business does
│   ├── personal-info.md       # Who you are, your role
│   ├── strategy.md            # Current priorities and goals
│   ├── funnel.md              # Business funnel stages
│   └── key-metrics.md         # Auto-generated metrics summary
├── data/                      # SQLite database — all metrics, meetings
│   └── data.db                # Business data warehouse (gitignored)
├── scripts/                   # Automation scripts
│   ├── db.py                  # Database framework
│   ├── collect.py             # Data collection orchestrator
│   ├── collect_*.py           # Individual data collectors
│   ├── daily_brief.py         # Daily Brief generator
│   ├── metrics.py             # Funnel metrics builder
│   ├── prompt.py              # Brief prompt assembler
│   ├── dashboard.py           # Dashboard image generator
│   ├── deliver.py             # Telegram delivery
│   └── intel/                 # IntelOS — meeting collection
│       ├── collect_fireflies.py
│       └── db.py
├── gtd/                       # ProductivityOS — GTD system
│   ├── dashboard.md           # Operational hub (projects, actions, waiting-for)
│   ├── inbox.md               # Raw capture bucket
│   ├── projects.md            # Master project list by area
│   ├── next-actions.md        # Actions by context (@me, @claude, @calls, etc.)
│   ├── waiting-for.md         # Delegated items
│   ├── someday-maybe.md       # Ideas for later
│   └── areas.md               # Areas of responsibility
├── apps/
│   └── command/               # CommandOS — Telegram bot
├── outputs/
│   └── daily-brief/           # Generated daily briefs
├── claude-code-os-implementation/  # Existing: Claude Code OS
├── agentic/                   # Existing: Agentic framework
├── cto-hub/                   # Existing: CTO decision system
└── docs/                      # Documentation
```

---

## Commands

### /prime
**Purpose:** Load all context files, metrics, history, and docs index. Orient Claude for the session. Run at the start of every session.

### /commit
**Purpose:** Save work with a clean Git commit, update HISTORY.md changelog. Run at the end of every session.

### /task-audit
**Purpose:** Map every recurring task, score for automation potential. Scoreboard for Task Automation % KPI.

### /process
**Purpose:** Process GTD inbox to zero. Walk through each item with the decision tree — route to projects, actions, waiting-for, someday, or trash.

### /review
**Purpose:** Guided weekly review (Fridays recommended). Get Clear → Get Current → Get Creative → Rebuild dashboard. 30-60 minutes.

### /capture
**Purpose:** Quick capture of content ideas. Prompts for pillar, format, and hook. Stores in content database.

### /develop
**Purpose:** Develop a captured idea into a full content concept. Applies positioning angles, audience targeting, and format optimization.

### /schedule
**Purpose:** Schedule developed content for publication. Assigns to calendar slot (Mon/Wed/Fri).

### /update-ai-docs
**Purpose:** Pull live rankings from AI leaderboards, detect changes, research new leaders, and update `ai-docs/` documentation. Runs autonomously.

### /brainstorm
**Purpose:** Scan workspace and Task Audit to find the best automation opportunities. Ranks by impact x feasibility. Outputs to `plans/`.

### /explore [idea]
**Purpose:** Shape a specific idea into a buildable concept. 5 stages: Discovery → Research → Shape → Scope → Output. Feeds into `/create-plan` or `/implement`.

### Existing Commands
- `/status` — Quick status check
- `/cto-sync`, `/cto-decision`, `/cto-debt` — CTO hub commands
- `/agentic-*` — Agentic framework commands

---

## Installed AIOS Modules

- **ContextOS v1** — Context files populated, /prime command active
- **InfraOS v1** — Git version control, /commit command, HISTORY.md changelog
- **DataOS v1** — SQLite data warehouse, collection pipeline, FX rates active
- **IntelOS v1** — Meeting transcript collection from Fireflies (234 meetings)
- **CommandOS v1** — Telegram bot with Claude Code agent access
- **Daily Brief v1** — Morning intelligence report via Gemini, delivered to Telegram
- **ProductivityOS v1** — GTD system with /process and /review commands, dashboard auto-refresh
- **Content Pipeline v1** — LinkedIn content system with 7 pillars, /capture → /develop → /schedule workflow
- **Diagram Engine v1** — D2-based diagram generation, `diagrams/` folder, render script
- **AI Landscape Monitor v1** — Daily scanner tracking 10 AI categories, `/update-ai-docs` command, `ai-docs/` reference
- **Slash Command Toolkit v1** — `/brainstorm` and `/explore` commands for custom building workflow

---

## Data

All business metrics are collected into `data/data.db` (SQLite).

- **Run DataOS collection:** `python scripts/collect.py`
- **Run IntelOS collection:** `python scripts/intel/collect_all.py`
- **Generate Daily Brief:** `python scripts/daily_brief.py`
- **Search meetings:** Use `scripts/intel/db.py` helpers

**Connected sources:** Fireflies (234 meetings), FX rates. GA4 and Leads ready when configured.

---

## Session Workflow

1. **Start**: Run `/prime` to load context and orient
2. **Work**: Use commands or direct Claude with tasks
3. **Save**: Run `/commit` to save work and log to HISTORY.md
4. **Backup**: `git push` to back up to GitHub

---

## Critical Instruction: Maintain This File

**Whenever Claude makes changes to the workspace, Claude MUST consider whether CLAUDE.md needs updating.**

After any change — adding commands, scripts, workflows, or modifying structure — ask:
1. Does this change add new functionality users need to know about?
2. Does it modify the workspace structure documented above?
3. Should a new command be listed?

If yes to any, update the relevant sections.
