# modules

Official module collection for [agentic](https://github.com/trent-40hero/agentic) workspaces.

## Quick Start

```bash
# Install the agentic CLI
curl -fsSL https://raw.githubusercontent.com/trent-40hero/agentic/main/install.sh | bash

# Create a workspace
agentic init my-workspace
cd my-workspace

# Add modules
agentic add github.com/trent-40hero/modules/slack
agentic add github.com/trent-40hero/modules/n8n
```

## Available Modules

### Core

| Module | Description | Install |
|--------|-------------|---------|
| [slack](./slack/) | Slack channel/message management | `agentic add .../slack` |
| [md-export](./md-export/) | Markdown to Google Docs/Word | `agentic add .../md-export` |
| [sop](./sop/) | Audio transcription & SOP extraction | `agentic add .../sop` |

### Sales

| Module | Description | Install |
|--------|-------------|---------|
| [proposal](./proposal/) | Sales proposals & Google Slides | `agentic add .../proposal` |
| [leads](./leads/) | Lead scraping via Apify | `agentic add .../leads` |
| [client-onboarding](./client-onboarding/) | Slack channel setup for clients | `agentic add .../client-onboarding` |

### Infrastructure

| Module | Description | Install |
|--------|-------------|---------|
| [infrastructure](./infrastructure/) | Cloudflare DNS/tunnels + Dokploy | `agentic add .../infrastructure` |
| [n8n](./n8n/) | n8n workflow management | `agentic add .../n8n` |

*Replace `...` with `github.com/trent-40hero/modules`*

## Module Structure

Each module is self-contained in its own directory:

```
module-name/
├── agentic-module.yaml    # Manifest (name, version, deps)
├── requirements.txt       # Python dependencies
├── tool/                  # Python scripts (run via ./run)
├── runbook/               # SOPs for the AI agent
└── commands/              # Slash commands (symlinked to .claude/commands/)
```

When installed, modules stay in `modules/<name>/` - they're not flattened.

## Creating Your Own Module

```bash
# In a workspace
agentic new my-module    # Creates modules/my-module/ + feat/my-module branch
```

This scaffolds the structure with templates. Then edit:

- `modules/my-module/agentic-module.yaml` - metadata and env vars
- `modules/my-module/tool/*.py` - implementation
- `modules/my-module/runbook/*.md` - documentation

**Manifest format:**

```yaml
name: my-module
version: "1.0.0"
description: What this module does

env_vars:
  - MY_API_KEY

requires:
  - slack: "for notifications"

mcp_servers:
  my-server:
    package: "@org/my-mcp-server"
    command: npx
    args: ["-y", "@org/my-mcp-server"]
    env_from_module: true  # pass module's env_vars to the server
```

**MCP Server Options:**

| Field | Description |
|-------|-------------|
| `package` | npm package name (for display/install checks) |
| `command` | Executable to run |
| `args` | Command arguments |
| `env_from_module` | If `true`, passes all module `env_vars` to the server |
| `env` | Explicit env var mapping with `${VAR}` interpolation |

When a module is added, the CLI prompts to configure any required MCP servers in the user's MCP config.

## Contributing

Modules stay in their directories, so changes are easy to track:

```bash
# See local changes
agentic pr slack

# Commit and push
git add modules/slack
git commit -m 'fix(slack): description'
git push origin $(git branch --show-current)
```

Then open a PR on GitHub.

## License

MIT
