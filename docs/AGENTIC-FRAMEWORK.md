# Agentic Framework

**Source**: https://github.com/trent-40hero/agentic
**Location**: `/agentic/`
**Purpose**: Modular framework for AI-agent-powered automation

---

## Quick Start

```bash
# Run setup
/agentic-setup

# Use modules directly
./agentic/run modules/slack/tool/slack_api.py channels list
```

---

## Available Modules

| Module | Purpose | Tools |
|--------|---------|-------|
| `client-onboarding` | Client setup and welcome | Canvas, templates |
| `demo-deploy` | Demo deployment automation | Deploy scripts |
| `diagrams` | Generate diagrams | DrawIO, Mermaid |
| `infrastructure` | Cloud infrastructure | Cloudflare, Dokploy |
| `leads` | Lead generation | Scrape, verify, sheets |
| `md-export` | Markdown export | MD to DOCX |
| `n8n` | n8n automation | n8n integration |
| `notion` | Notion integration | Notion API |
| `proposal` | Proposal generation | Proposal tools |
| `slack` | Slack integration | Slack API |
| `sop` | SOP management | SOP tools |
| `ssh` | SSH management | SSH tools |

---

## Architecture

```
agentic/
├── modules/                      # All modules
│   ├── [module-name]/
│   │   ├── agentic-module.yaml   # Manifest
│   │   ├── tool/                 # Python implementation
│   │   ├── runbook/              # Documentation/SOPs
│   │   └── commands/             # Slash commands
│
├── extras/                       # Additional resources
├── tools/                        # sync.py, scaffold.py
├── run                           # Runner script
├── tests/                        # Test files
├── agentic-index.yaml            # Discovery index
├── requirements.txt              # Python dependencies
└── VERSION                       # Version file
```

---

## The 3-Layer Pattern

| Layer | Purpose | Location |
|-------|---------|----------|
| **Runbook** | SOPs defining what to do | `modules/*/runbook/` |
| **Orchestration** | AI agent decision-making | Claude Code |
| **Tool** | Python implementation | `modules/*/tool/` |

---

## Available Commands

Run these in Claude Code:

- `/agentic-setup` - Initial setup
- `/agentic-new` - Create new module
- `/agentic-new-project` - Create new project
- `/agentic-sync` - Sync modules
- `/agentic-version` - Check version

---

## Integration with AI Agency Sales OS

The agentic framework complements the existing structure:

| AI Agency Sales OS | Agentic Framework |
|--------------------|-------------------|
| `03-ai-growth-engine/` | Strategic frameworks |
| `agentic/modules/leads/` | Lead automation tools |
| `agentic/modules/client-onboarding/` | Client setup automation |
| `agentic/modules/proposal/` | Proposal generation |
| `agentic/modules/n8n/` | n8n workflow tools |

---

## Getting Started

1. Review available modules in `/agentic/modules/`
2. Check runbooks for SOPs: `/agentic/modules/[name]/runbook/`
3. Use tools via runner: `./agentic/run modules/[name]/tool/[script].py`
4. Create custom modules with `/agentic-new`

---

*Framework by trent-40hero, integrated December 27, 2024*
