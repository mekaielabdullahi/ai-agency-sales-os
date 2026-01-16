# Claude Code OS - Project Guide

## Quick Start

Type `/dashboard` to see all available commands and system status.

## All 26 Slash Commands

### Executive Office (Planning)
| Command | Description |
|---------|-------------|
| `/daily-plan [energy]` | Generate daily roadmap with THE ONE THING |
| `/quick-plan [one-thing]` | Rapid 60-second planning |
| `/weekly-plan [week]` | Strategic week blueprint |
| `/monthly-review [month]` | Comprehensive month analysis |
| `/one-thing [context]` | Find your focusing priority |

### Operations (Tracking)
| Command | Description |
|---------|-------------|
| `/assess` | End-of-day productivity assessment |
| `/metrics [period]` | KPI analysis and trends |
| `/project-status [name]` | Project health report |

### Content Team (Creation)
| Command | Description |
|---------|-------------|
| `/content [type]` | Full content creation workflow |
| `/hook [topic]` | Generate attention-grabbing hooks |
| `/social [platform]` | Platform-optimized social posts |
| `/email [type]` | Email campaigns and sequences |
| `/edit [content]` | Polish and refine content |

### AI Growth Engine (Sales)
| Command | Description |
|---------|-------------|
| `/client-analyze [name]` | Client intelligence report |
| `/lead-score [info]` | Score and prioritize leads |
| `/proposal [client]` | Generate client proposal |
| `/meeting-notes [type]` | Capture meeting notes and follow-ups |

### HR Department (Agent Factory)
| Command | Description |
|---------|-------------|
| `/create-agent [idea]` | Build new AI agent |
| `/qa-agent [agent]` | Run QA validation |

### Personal Development
| Command | Description |
|---------|-------------|
| `/reflect [topic]` | Personal reflection and journaling |
| `/decide [decision]` | Structured decision framework |
| `/habits [mode]` | Track habits and consistency |

### Integration Workflows
| Command | Description |
|---------|-------------|
| `/dashboard` | System overview and quick actions |
| `/morning` | Complete morning startup routine |
| `/evening` | Complete evening shutdown routine |
| `/weekly-workflow` | Day-appropriate weekly workflow |
| `/sales-pipeline [company]` | Full sales workflow |
| `/content-pipeline [topic]` | Full content workflow |

## Daily Workflow

```
MORNING (6:00 AM)
└─→ /morning or /daily-plan

WORK DAY
└─→ THE ONE THING first (8-10 AM)
└─→ Tier 1 tasks (10 AM-12 PM)
└─→ Tier 2 / meetings (afternoon)

EVENING (5:30 PM)
└─→ /evening or /assess
```

## Weekly Workflow

```
SUNDAY (6:00 PM)    → /weekly-plan
MONDAY              → Foundation day
TUESDAY             → Building day
WEDNESDAY (2:00 PM) → Mid-week checkpoint
THURSDAY            → Collaboration day
FRIDAY (4:00 PM)    → /metrics + ship
```

## Integrated Pipelines

### Sales Pipeline
```
/client-analyze → /lead-score → /email cold → /meeting-notes → /proposal
```

### Content Pipeline
```
/hook → /content → /edit → /social [platform]
```

### Agent Creation Pipeline
```
/create-agent → /qa-agent → Deploy
```

## Key Concepts

### THE ONE THING
The single most important task that makes everything else easier. Do this first during peak hours (8-10 AM).

### Brutal Prioritization
- **Tier 1**: Must complete (max 3)
- **Tier 2**: If time permits (max 3)
- **Kill List**: What NOT to do

### OBG (Overarching Business Goal)
Your 90-day strategic objective. All work aligns to this.

### Priority Levels
- **P1**: 60%+ time (OBG-critical)
- **P2**: ~25% time (strategic)
- **P3**: <15% time (maintenance)

## Project Structure

```
.claude/
├── commands/           # 26 slash commands
├── hooks/              # Automation scripts
├── settings.json       # Project config
├── AUTOMATION-GUIDE.md # Full automation docs
└── NOTION-SETUP.md     # Notion integration guide

claude-code-os-implementation/
├── 01-executive-office/   # Planning agents
├── 02-operations/         # Tracking agents
├── 03-ai-growth-engine/   # Sales agents
├── 04-content-team/       # Content agents
├── 05-hr-department/      # Agent factory
└── 07-workflows/          # Routines
```

## Tips for Best Results

1. **Start every day** with `/morning` or `/daily-plan`
2. **End every day** with `/evening` or `/assess`
3. **Protect peak hours** (8-10 AM) for THE ONE THING
4. **Use pipelines** for multi-step workflows
5. **Track patterns** with `/metrics` weekly
6. **Create automations** with `/create-agent`

## Getting Help

- `/dashboard` - See all commands
- `/help` - Claude Code help
- `.claude/AUTOMATION-GUIDE.md` - Detailed automation setup
- `.claude/NOTION-SETUP.md` - Connect to Notion
