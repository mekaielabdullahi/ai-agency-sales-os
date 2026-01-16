# Claude Code OS - Automation Guide

## Quick Start

Your slash commands are ready to use! Type any command in Claude Code:

```
/dashboard        - See all commands and system status
/daily-plan       - Generate your daily roadmap
/quick-plan       - 60-second rapid planning
/assess           - End-of-day productivity assessment
/weekly-plan      - Strategic week planning
/monthly-review   - Comprehensive month analysis
```

## All Available Commands

### Executive Office (Planning)
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/daily-plan` | Full daily roadmap with THE ONE THING | Every morning |
| `/quick-plan` | Rapid 60-second plan | When short on time |
| `/weekly-plan` | Strategic week blueprint | Sunday evenings |
| `/monthly-review` | Comprehensive month analysis | End of month |
| `/one-thing` | Find your focusing priority | When overwhelmed |

### Operations (Tracking)
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/assess` | Productivity assessment + score | Every evening |
| `/metrics` | KPI analysis and trends | Weekly review |
| `/project-status` | Project health report | As needed |

### Content Team (Creation)
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/content` | Full content creation workflow | Any content need |
| `/hook` | Generate attention-grabbing hooks | Before writing |
| `/social` | Platform-optimized social posts | Social content |
| `/email` | Email campaigns and sequences | Email marketing |
| `/edit` | Polish and refine content | Before publishing |

### AI Growth Engine (Sales)
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/client-analyze` | Client intelligence report | Before outreach |

### HR Department (Agent Factory)
| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/create-agent` | Build new AI agent | New automation need |
| `/qa-agent` | Validate agent quality | Before deployment |

## Daily Workflow Automation

### Morning Routine (6:00 AM)
```bash
# Option 1: Run the hook manually
.claude/hooks/morning-routine.sh

# Option 2: Use the command directly
/daily-plan
```

### Evening Routine (5:30 PM)
```bash
# Option 1: Run the hook manually
.claude/hooks/evening-routine.sh

# Option 2: Use the command directly
/assess
```

### Weekly Planning (Sunday 6:00 PM)
```bash
# Option 1: Run the hook manually
.claude/hooks/weekly-planning.sh

# Option 2: Use the command directly
/weekly-plan
```

## Scheduling with Cron (Optional)

If you want automated reminders, add these to your crontab:

```bash
# Edit crontab
crontab -e

# Add these lines:

# Morning reminder at 6:00 AM (Mon-Fri)
0 6 * * 1-5 notify-send "Claude Code OS" "Time for /daily-plan"

# Evening reminder at 5:30 PM (Mon-Fri)
30 17 * * 1-5 notify-send "Claude Code OS" "Time for /assess"

# Weekly planning reminder (Sunday 6:00 PM)
0 18 * * 0 notify-send "Claude Code OS" "Time for /weekly-plan"

# Monthly review reminder (Last day of month, 4:00 PM)
0 16 28-31 * * [ "$(date +%d -d tomorrow)" = "01" ] && notify-send "Claude Code OS" "Time for /monthly-review"
```

## Recommended Daily Schedule

```
TIME        ACTION              COMMAND
─────────────────────────────────────────────
6:00 AM     Morning Planning    /daily-plan
            ↓
8:00 AM     THE ONE THING       (deep work)
            ↓
10:00 AM    Tier 1 Tasks        (execution)
            ↓
12:00 PM    Lunch Break
            ↓
1:00 PM     Afternoon Work      (Tier 2)
            ↓
3:00 PM     Communications      (emails, calls)
            ↓
5:00 PM     Wrap Up
            ↓
5:30 PM     Assessment          /assess
```

## Weekly Schedule

```
DAY         THEME               FOCUS
─────────────────────────────────────────────
Monday      Foundation          Setup & deep work
Tuesday     Building            Core project work
Wednesday   Validation          Progress check
Thursday    Collaboration       Meetings & comms
Friday      Ship & Plan         Finish & next week
Saturday    Rest                Optional catch-up
Sunday      Strategy            /weekly-plan (6 PM)
```

## Tips for Maximum Automation

### 1. Start Every Session with Dashboard
```
/dashboard
```
This shows your current status and suggested actions.

### 2. Use Quick Commands When Busy
- `/quick-plan` for rapid planning
- `/one-thing` to find your focus

### 3. Build Habits Around Commands
- Morning = `/daily-plan`
- Evening = `/assess`
- Sunday = `/weekly-plan`
- End of Month = `/monthly-review`

### 4. Chain Commands for Content
```
/hook [topic]           # Get hook options
/content social         # Create full post
/edit [paste content]   # Final polish
```

### 5. Before Any Client Call
```
/client-analyze [company name]
```

### 6. When Creating New Automations
```
/create-agent [your idea]
/qa-agent [test it]
```

## Troubleshooting

### Commands Not Found?
Make sure you're in the project directory:
```bash
cd /home/user/ai-agency-sales-os
```

### Hook Not Running?
Check permissions:
```bash
chmod +x .claude/hooks/*.sh
```

### Need Help?
```
/dashboard   # See all options
/help        # Claude Code help
```

## File Locations

```
.claude/
├── commands/           # Your slash commands
│   ├── daily-plan.md
│   ├── weekly-plan.md
│   ├── monthly-review.md
│   ├── assess.md
│   ├── metrics.md
│   ├── project-status.md
│   ├── content.md
│   ├── hook.md
│   ├── social.md
│   ├── email.md
│   ├── edit.md
│   ├── client-analyze.md
│   ├── create-agent.md
│   ├── qa-agent.md
│   ├── dashboard.md
│   ├── quick-plan.md
│   └── one-thing.md
├── hooks/              # Automation scripts
│   ├── morning-routine.sh
│   ├── evening-routine.sh
│   ├── weekly-planning.sh
│   └── session-start.sh
├── settings.json       # Project settings
└── AUTOMATION-GUIDE.md # This file
```

## Next Steps

1. **Try it now**: Type `/dashboard` to see your system
2. **Plan today**: Use `/daily-plan` to create your roadmap
3. **Build the habit**: Use commands daily for 30 days
4. **Create more**: Use `/create-agent` when you need new automations

---

*Your AI-powered productivity system is ready. Use it daily and watch your output compound.*
