# Agentic Workspaces

A modular framework for AI-agent-powered automation. Clone once, use everything, contribute via git.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/trent-40hero/agentic
cd agentic

# Open in Claude Code and run:
/agentic-setup

# Done! Use modules directly
./run modules/slack/tool/slack_api.py channels list
```

## Architecture

Each module is a self-contained package:

```
agentic/
├── modules/                      # All modules (source of truth)
│   ├── slack/
│   │   ├── agentic-module.yaml   # Manifest
│   │   ├── tool/                 # Python implementation
│   │   │   └── slack_api.py
│   │   ├── runbook/              # Documentation/SOPs
│   │   │   └── slack_management.md
│   │   └── commands/             # Slash commands
│   │       └── slack.md
│   └── leads/
│       └── ...
│
├── .claude/commands/             # Core + module commands
├── .git-hooks/                   # Branch protection
├── agentic-index.yaml            # Discovery index for AI agents
├── requirements.txt              # Combined Python deps
├── tools/                        # sync.py, scaffold.py
└── VERSION                       # Workspace version
```

### The 3-Layer Pattern

| Layer | Purpose | Location |
|-------|---------|----------|
| **Runbook** | SOPs defining what to do | `modules/*/runbook/` |
| **Orchestration** | AI agent decision-making | Claude, Gemini, etc. |
| **Tools** | Deterministic scripts | `modules/*/tool/` |

**Why this works:** LLMs are probabilistic; business logic needs consistency. Push complexity into deterministic code, let the AI focus on routing and decisions.

---

## Commands

All commands are slash commands in Claude Code:

```
/agentic-setup          # One-time: venv, deps, hooks, symlinks
/agentic-sync           # Regenerate symlinks + index after module changes
/agentic-new <name>     # Scaffold a new module
/agentic-new-project    # Create a new project in ../projects/
/agentic-version        # Show version
```

That's it. Everything else is just git.

---

## Workflow

### Using Modules

```bash
# Run tools directly
./run modules/slack/tool/slack_api.py channels list

# Or use Claude Code with slash commands
/slack create my-channel
```

### Creating a New Module

```
/agentic-new my-feature
# Creates modules/my-feature/ + switches to feat/my-feature branch
```

Then edit:
- `agentic-module.yaml` — metadata, env vars
- `tool/*.py` — implementation
- `runbook/*.md` — documentation
- `commands/*.md` — slash commands

### Contributing

```bash
# Create a branch (or use agentic new)
git checkout -b feat/my-change

# Make changes
vim modules/slack/tool/slack_api.py

# Commit and push
git add modules/slack
git commit -m 'fix(slack): handle rate limits'
git push origin feat/my-change

# Open PR on GitHub
```

Git hooks prevent direct commits to main — you must use a feature branch.

---

## Agent Discovery

The `agentic-index.yaml` file gives AI agents everything they need:

```yaml
modules:
  slack:
    description: "Slack channel and message management"
    paths:
      root: modules/slack/
      tools:
        - modules/slack/tool/slack_api.py
      runbooks:
        - modules/slack/runbook/slack_management.md
    python_import: "modules.slack.tool"
    env_vars: [SLACK_BOT_TOKEN, SLACK_USER_TOKEN]
```

Agents can:
1. Read `agentic-index.yaml` to discover capabilities
2. Read the relevant runbook for instructions
3. Run tools with `./run modules/<name>/tool/<script>.py`
4. Edit tools/runbooks and commit with module-scoped changes

---

## Available Modules

See [modules/](./modules/) for the full catalog.

### Core
| Module | Description |
|--------|-------------|
| `slack` | Slack channel/message management |
| `md-export` | Markdown to Google Docs/Word |
| `sop` | Audio transcription and SOP extraction |
| `diagrams` | Mermaid/DrawIO diagram generation |

### Sales
| Module | Description |
|--------|-------------|
| `proposal` | Generate sales proposals and Google Slides |
| `leads` | Scrape and verify leads via Apify |
| `client-onboarding` | Set up Slack channels for new clients |

### Infrastructure
| Module | Description |
|--------|-------------|
| `infrastructure` | Cloudflare DNS/tunnels + Dokploy containers |
| `n8n` | n8n workflow management |

---

## Key Files

| File | Purpose |
|------|---------|
| `agentic-index.yaml` | Discovery index for AI agents |
| `CLAUDE.md` | Instructions for Claude Code |
| `.claude/commands/` | Symlinks to module commands |
| `.git-hooks/` | Branch protection hooks |
| `run` | Wrapper that activates venv |
| `tools/` | Python tools for sync and scaffolding |
| `VERSION` | Workspace version |

---

## Environment Variables

After running `/agentic-setup`, edit `.env` with your credentials:

```bash
# Required by slack module
SLACK_BOT_TOKEN=xoxb-...
SLACK_USER_TOKEN=xoxp-...

# Required by leads module
APIFY_API_TOKEN=...
```

The setup command will warn you about any missing variables.
