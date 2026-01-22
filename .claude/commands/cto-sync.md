# CTO Sync Command

Comprehensive system scan and documentation refresh for the CTO Hub.

## Purpose

Keep the CTO knowledge system current by scanning the entire codebase and updating documentation. Run weekly or after major changes.

## Usage
```
/cto-sync              # Full sync
/cto-sync --quick      # Quick status only
/cto-sync --inventory  # Update inventories only
```

## What This Command Does

### Phase 1: System Scan

**Scan all skills:**
```
.claude/skills/*/SKILL.md
```
Extract: name, description, last modified, integration points

**Scan all commands:**
```
.claude/commands/*.md
```
Extract: name, purpose

**Scan all agentic modules:**
```
agentic/modules/*/agentic-module.yaml
```
Extract: module name, tools, env requirements

**Scan all agents:**
```
claude-code-os-implementation/*/agents/*.md
```
Extract: agent name, purpose, location

### Phase 2: Detect Changes

Compare current scan to last CURRENT-STATE.md:
- New skills/modules/agents added
- Removed or deprecated items
- Changed configurations
- New integrations

### Phase 3: Update Inventories

Update files in `cto-hub/system-inventory/`:
- `skills-inventory.md`
- `modules-inventory.md`
- `agents-inventory.md`
- `integrations-inventory.md`

### Phase 4: Generate CURRENT-STATE.md

Create fresh `cto-hub/CURRENT-STATE.md` with:

```markdown
# Current System State

**Last Synced:** [TIMESTAMP]
**Synced By:** Claude Code

## Quick Stats
- Skills: [X]
- Commands: [X]
- Agentic Modules: [X]
- Agents: [X]
- Active Projects: [X]

## Recent Changes (Since Last Sync)
- [List of detected changes]

## System Health
| Component | Status | Notes |
|-----------|--------|-------|
| [Component] | ✅/⚠️/🔴 | [Notes] |

## Skills Overview
| Skill | Status | Last Used | Notes |
|-------|--------|-----------|-------|
| [name] | Active | [date] | [notes] |

## Modules Overview
| Module | Tools | Env Configured | Notes |
|--------|-------|----------------|-------|
| [name] | [count] | ✅/❌ | [notes] |

## Known Technical Debt
[Summary from DEBT-REGISTER.md]

## Pending Decisions
[Any open ADRs or decision points]

## Recommendations
[Auto-generated based on scan findings]
```

### Phase 5: Check for Issues

Automatically detect and flag:
- Missing environment variables
- Orphaned files (referenced but don't exist)
- Stale documentation (not updated in 30+ days)
- Broken integration points
- Unused skills/modules

### Phase 6: Log Session

Create entry in `cto-hub/session-logs/`:
```
YYYY-MM-DD-cto-sync.md
```

With:
- Timestamp
- Changes detected
- Issues found
- Recommendations

## Output

After sync, display summary:

```
🔄 CTO Sync Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 System Inventory
   Skills: 9 (↑2 new)
   Commands: 7 (↑1 new)
   Modules: 12 (no change)
   Agents: 15 (↑4 new)

📝 Changes Detected
   + Added: /publish skill
   + Added: /status command
   + Added: /dashboard skill
   ~ Modified: weekly-report (notion sync)
   ~ Modified: client-outreach (speed-to-lead link)

⚠️ Issues Found
   - 3 Notion sync targets need page IDs
   - TypeScript onboarding agents not deployed

📋 Recommendations
   1. Configure Notion page IDs for auto-sync
   2. Review onboarding agents for deployment
   3. Run /weekly-report (5 days overdue)

✅ Updated: cto-hub/CURRENT-STATE.md
✅ Updated: cto-hub/system-inventory/*
✅ Created: cto-hub/session-logs/2026-01-22-cto-sync.md

Next sync recommended: 2026-01-29
```

## Integration Points

- **cto-hub/** - All outputs stored here
- **technical-debt/DEBT-REGISTER.md** - Auto-populated with found issues
- **notion-sync** - Can optionally push CURRENT-STATE to Notion

## Automation

Consider scheduling weekly:
- Every Friday at 5pm
- Or Monday morning as week start

## Related Commands

- `/cto-decision [topic]` - Log an architecture decision
- `/cto-debt [issue]` - Log technical debt
- `/cto-status` - Quick status (no full scan)
- `/status` - System health check
