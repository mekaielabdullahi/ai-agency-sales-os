# agentic-module-client-onboarding

Set up Slack channels and resources for new clients.

## Features

- Create standardized client channels (`#client` and `#client-internal`)
- Apply canvas templates with project info
- Post and pin welcome messages
- Notify team in `#new-clients` channel

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-client-onboarding
```

## Dependencies

This module requires the `slack` module:
```bash
agentic add github.com/arisegroup/agentic-module-slack
```

## Setup

### Slack App

1. Create a Slack app at api.slack.com/apps
2. Add Bot Token Scopes: `chat:write`, `channels:manage`, `channels:read`
3. Add User Token Scopes: `chat:write` (for cleaning system messages)
4. Install to workspace
5. Add tokens to `.env`:
   ```
   SLACK_BOT_TOKEN=xoxb-...
   SLACK_USER_TOKEN=xoxp-...
   ```

## Slash Commands

```
/client-setup <slug> <display_name>
```

## CLI Usage

```bash
# Basic setup
./run tools/slack_api.py client setup "acme" --display-name "Acme Corp"

# With custom templates
./run tools/slack_api.py client setup "acme" \
  --display-name "Acme Corp" \
  --canvas-template templates/custom_canvas.md \
  --notify-channel "#sales"
```

## Workflow

1. Gather client info (slug, display name)
2. Run `/client-setup` command
3. Customize the canvas with project links
4. Invite client guests to the main channel

## Templates

The module includes two templates that support variable substitution:

### `templates/client_canvas.md`
- `{display_name}` - Client display name
- `{date}` - Today's date

### `templates/client_welcome.md`
- `{display_name}` - Client display name

## What Gets Created

| Resource | Description |
|----------|-------------|
| `#slug` | Public channel for client communication |
| `#slug-internal` | Public channel for internal discussion |
| Canvas | Project reference document |
| Welcome message | Pinned intro message |
| Notification | Posted to `#new-clients` |
