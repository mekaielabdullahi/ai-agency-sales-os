# CTO Debt Command

Log technical debt to the CTO Hub debt register.

## Purpose

Quick capture of technical debt discovered during work sessions. Keeps the debt register current without interrupting flow.

## Usage
```
/cto-debt [description]
```

## Examples
```
/cto-debt Notion sync targets missing page IDs
/cto-debt TypeScript agents need deployment infrastructure
/cto-debt Duplicate templates in outreach skills
```

## What This Command Does

### Step 1: Parse Input

Extract from your description:
- Brief description
- Infer location if mentioned
- Infer priority if obvious

### Step 2: Quick Questions (if needed)

I may ask:
- Where in the codebase? (if not clear)
- What's the impact? (blocking, annoying, cosmetic)
- Rough effort to fix? (quick, medium, large)

### Step 3: Add to Register

Append to `cto-hub/technical-debt/DEBT-REGISTER.md`:
- Generate next TD-XXX ID
- Add row to appropriate priority table
- Include today's date

### Step 4: Confirm

```
✅ Logged: TD-004 - "Notion sync targets missing page IDs"
   Priority: P1 | Location: .claude/skills/notion-sync/targets.json

   View: cto-hub/technical-debt/DEBT-REGISTER.md
```

## Priority Levels

| Priority | Meaning | Examples |
|----------|---------|----------|
| P0 | Blocking now | Build fails, integration broken |
| P1 | Fix soon | Missing features, workarounds needed |
| P2 | Nice to have | Code cleanup, minor improvements |
| P3 | Cosmetic | Typos, formatting, minor polish |

## Quick Mode

Minimal capture with defaults:
```
/cto-debt --quick "thing that needs fixing"
```
Adds as P2 with location TBD, for triage later.

## Resolving Debt

When you fix technical debt:
```
/cto-debt --resolve TD-004
```
Moves the item to "Resolved" table with resolution notes.

## Related

- `/cto-sync` - Reviews debt register during sync
- `/cto-decision` - For architectural decisions, not debt
- `cto-hub/technical-debt/DEBT-REGISTER.md` - The register
