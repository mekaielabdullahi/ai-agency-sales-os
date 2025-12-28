# Agentic Setup
> One-time workspace setup: venv, dependencies, hooks, and symlinks.

## Instructions

Perform these setup steps in order:

### 1. Create Python Virtual Environment

```bash
python3 -m venv .venv
```

Skip if `.venv/` already exists.

### 2. Install Dependencies

```bash
.venv/bin/pip install -q -r requirements.txt
```

### 3. Create .env File

If `.env` does not exist but `.env.example` does:
```bash
cp .env.example .env
```

Warn the user to edit `.env` and add their credentials.

### 4. Enable Git Hooks

```bash
git config core.hooksPath .git-hooks
```

This enables branch protection (prevents direct commits to main).

### 5. Run Sync

Run `/agentic-sync` to create module command symlinks and generate the discovery index.

### 6. Check Environment Variables

Read each `modules/*/agentic-module.yaml` file and check for `env_vars`. For each variable listed, verify it exists in `.env` or the environment. Report any missing variables.

## Report

- Confirm each step completed
- List any missing environment variables with which module requires them
- Suggest next steps (e.g., "You can now use /slack, /diagram, etc.")
