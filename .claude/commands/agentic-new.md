# Agentic New Module
> Scaffold a new agentic module with proper structure.

## Variables

- name: $ARGUMENTS

## Instructions

### 1. Validate Input

If no name provided, ask the user for a module name.

The name must be:
- Lowercase
- Start with a letter
- Contain only letters, numbers, and hyphens

### 2. Run Scaffold Tool

```bash
./run tools/scaffold.py module "$name"
```

This creates:
- `modules/<name>/agentic-module.yaml` - Module manifest
- `modules/<name>/tool/<name>.py` - Python tool template
- `modules/<name>/runbook/<name>.md` - Documentation template
- `modules/<name>/commands/<name>.md` - Slash command template
- `modules/<name>/README.md` - Module readme

### 3. Run Sync

After scaffolding, run `/agentic-sync` to create the command symlink.

## Report

- Confirm module created at `modules/<name>/`
- List the files created
- Provide next steps:
  1. Edit the manifest to add description and env vars
  2. Implement the tool logic
  3. Update the runbook with usage docs
  4. Test the tool
  5. Commit the new module
