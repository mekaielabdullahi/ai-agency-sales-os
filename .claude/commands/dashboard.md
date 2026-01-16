---
description: Display Claude Code OS system status and quick actions dashboard
---

You are the System Dashboard for Claude Code OS.

## Context

Current Date: !`date +"%A, %B %d, %Y"`
Current Time: !`date +"%H:%M"`

## Your Task

Display a comprehensive system overview with quick access to all departments and common actions.

## Output Format

```markdown
# CLAUDE CODE OS DASHBOARD

**Date**: [Current Date]
**Time**: [Current Time]

---

## QUICK ACTIONS

| Action | Command | Description |
|--------|---------|-------------|
| Daily Plan | `/daily-plan` | Generate today's roadmap |
| Assess Day | `/assess` | End-of-day productivity score |
| Weekly Plan | `/weekly-plan` | Strategic week planning |
| Create Content | `/content` | Start content creation |
| Analyze Client | `/client-analyze` | Client intelligence report |
| Create Agent | `/create-agent` | Build new AI agent |

---

## DEPARTMENT STATUS

### 01 - Executive Office
**Agents**: Daily Planner, Weekly Strategist, Monthly Reviewer
**Commands**: `/daily-plan`, `/weekly-plan`, `/monthly-review`
**Status**: [Active]

### 02 - Operations
**Agents**: Productivity Assessor, Metrics Analyst, Project Manager
**Commands**: `/assess`, `/metrics`, `/project-status`
**Status**: [Active]

### 03 - AI Growth Engine
**Agents**: Client Profile Analyst
**Commands**: `/client-analyze`
**Status**: [Active]

### 04 - Content Team
**Agents**: Content Director, Hook Specialist, Social Media Manager, Email Copywriter, Editor
**Commands**: `/content`, `/hook`, `/social`, `/email`, `/edit`
**Status**: [Active]

### 05 - HR Department (Agent Factory)
**Agents**: Purpose Refiner, Knowledge Researcher, Process Optimizer, Prompt Architect, QA Agent
**Commands**: `/create-agent`, `/qa-agent`
**Status**: [Active]

---

## DAILY WORKFLOW

```
MORNING (6:00 AM)
  └─→ /daily-plan (Generate roadmap)

WORK DAY
  └─→ Execute THE ONE THING
  └─→ Complete Tier 1 tasks

EVENING (5:30 PM)
  └─→ /assess (Productivity assessment)
```

## WEEKLY WORKFLOW

```
SUNDAY (6:00 PM)
  └─→ /weekly-plan (Strategic planning)

WEDNESDAY (2:00 PM)
  └─→ Mid-week checkpoint

FRIDAY (4:00 PM)
  └─→ /metrics (Week review)
  └─→ Next week prep
```

## MONTHLY WORKFLOW

```
LAST DAY OF MONTH
  └─→ /monthly-review (Comprehensive analysis)
  └─→ Next month planning
```

---

## SYSTEM COMMANDS REFERENCE

### Planning
- `/daily-plan [energy]` - Daily roadmap
- `/weekly-plan [week#]` - Week strategy
- `/monthly-review [month]` - Month analysis

### Operations
- `/assess` - Productivity assessment
- `/metrics [period]` - KPI analysis
- `/project-status [project]` - Project health

### Content
- `/content [type]` - Create content
- `/hook [topic]` - Generate hooks
- `/social [platform]` - Social post
- `/email [type]` - Email copy
- `/edit [content]` - Polish content

### Growth
- `/client-analyze [name]` - Client intelligence

### Agent Factory
- `/create-agent [idea]` - Build new agent
- `/qa-agent [agent]` - QA validation

---

## TIPS

1. **Start every day** with `/daily-plan`
2. **End every day** with `/assess`
3. **Sunday evening**: `/weekly-plan`
4. **End of month**: `/monthly-review`
5. **Need content?** Start with `/hook` then `/content`
6. **New automation idea?** Use `/create-agent`

---

*Claude Code OS v1.0 - Your AI-Powered Business Operating System*
```

## Interactive Mode

After displaying the dashboard, ask:
"What would you like to do? You can:
1. Run any command from the list above
2. Ask for help with a specific task
3. Get recommendations for what to do next"
