# CTO Hub

Your personal CTO knowledge system - a living documentation hub maintained through regular Claude Code sessions.

## Philosophy

This isn't static documentation that rots. It's a **living system** that evolves with every session. When you run `/cto-sync` or have a working session with Claude Code, relevant learnings, decisions, and system changes get captured here automatically.

## Folder Structure

```
cto-hub/
├── README.md                 # You are here
├── CURRENT-STATE.md          # Always-current system overview (regenerated each sync)
├── decisions/                # Architecture Decision Records (ADRs)
├── architecture/             # System diagrams and technical architecture
├── technical-debt/           # Known issues, tech debt tracking
├── system-inventory/         # Complete inventory of all systems, tools, integrations
├── session-logs/             # Summary of each major working session
└── learning/                 # Technical learnings, patterns, best practices
```

## How It Works

### Regular Sync Sessions
Run `/cto-sync` weekly (or after major changes) to:
1. Scan the entire codebase for changes
2. Update CURRENT-STATE.md with latest inventory
3. Capture any new decisions made
4. Log technical debt discovered
5. Update architecture docs if structure changed

### Passive Learning
During normal work sessions, when you:
- Make architectural decisions → I'll prompt to log an ADR
- Discover technical debt → I'll add to debt tracker
- Learn something new → I'll capture in learning folder
- Change system structure → I'll note for next sync

### Session Logs
After significant sessions, a brief log captures:
- What was accomplished
- Decisions made
- Questions raised
- Follow-ups needed

## Quick Commands

| Command | Purpose |
|---------|---------|
| `/cto-sync` | Full system scan and documentation refresh |
| `/cto-decision [topic]` | Log an architecture decision |
| `/cto-debt [issue]` | Log technical debt |
| `/cto-status` | Quick view of current state |

## Files

### CURRENT-STATE.md
Auto-generated overview of:
- All skills, commands, modules
- Active integrations and their status
- Key metrics and health indicators
- Last sync timestamp

### decisions/
Architecture Decision Records following ADR format:
- `ADR-001-skill-architecture.md`
- `ADR-002-notion-sync-approach.md`
- etc.

### architecture/
- System diagrams (Excalidraw/Mermaid)
- Integration maps
- Data flow documentation

### technical-debt/
- `DEBT-REGISTER.md` - Master list of known debt
- Individual issue files for larger items

### system-inventory/
- `skills-inventory.md` - All skills with status
- `modules-inventory.md` - All agentic modules
- `integrations-inventory.md` - External services
- `agents-inventory.md` - All defined agents

### session-logs/
- `YYYY-MM-DD-session-summary.md`
- Searchable history of work done

### learning/
- Technical patterns discovered
- Best practices established
- "What worked" documentation

## Getting Started

1. Run `/cto-sync` to generate initial state
2. Review CURRENT-STATE.md
3. Check technical-debt for known issues
4. Use during sessions - I'll prompt when to log things

## Maintenance

This system maintains itself through use. The more you work with Claude Code, the more accurate and valuable it becomes. No manual documentation required.

**Last synced:** [NEVER - run /cto-sync]
