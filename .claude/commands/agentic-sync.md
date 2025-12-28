# Agentic Sync
> Regenerate command symlinks and rebuild the workspace index.

## Instructions

Run the sync tool:

```bash
./run tools/sync.py
```

## What Sync Does

1. Scans `modules/*/commands/*.md` for module commands
2. Creates symlinks in `.claude/commands/` for each
3. Preserves core commands (`agentic-*.md` files)
4. Removes stale symlinks (pointing to deleted commands)
5. Rebuilds `agentic-index.yaml` with all module metadata

## When to Use

- After creating a new module with `/agentic-new`
- After manually adding/removing commands from a module
- After pulling changes that modify modules
- If command symlinks appear broken

## Report

- Number of modules synced
- Number of commands updated
- Confirm `agentic-index.yaml` was generated
- Any warnings (stale symlinks removed, etc.)
