# agentic-module-slack

Slack channel and message management module for Agentic Workspaces.

## Features

- Channel operations: create, archive, rename, set topic/purpose
- Message retrieval with date filtering
- Pin management
- Channel canvas (rich documents)
- User group management (sidebar sections)
- Client onboarding automation

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-slack
```

## Environment Variables

Add to your `.env`:

```
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_USER_TOKEN=xoxp-your-user-token  # Optional, for deleting others' messages
```

## Slash Command

After installation, use the `/slack` command:

```
/slack create my-channel --description "Channel purpose"
/slack archive old-channel
/slack summary #general 7
/slack list-groups
```

## CLI Usage

```bash
./run tools/slack_api.py channels list
./run tools/slack_api.py channels create my-channel --description "Purpose"
./run tools/slack_api.py messages get #general --days 7
./run tools/slack_api.py canvas create #channel --markdown "# Title"
```

## Required Slack App Scopes

| Scope | Purpose |
|-------|---------|
| `channels:manage` | Create/archive public channels |
| `channels:read` | List public channels |
| `channels:history` | Read public channel messages |
| `channels:write.topic` | Set topic/purpose |
| `groups:write` | Manage private channels |
| `groups:read` | List private channels |
| `groups:history` | Read private channel messages |
| `pins:read` | View pinned content |
| `pins:write` | Add/remove pins |
| `canvases:write` | Create/edit canvases |
| `canvases:read` | Read canvas content |
| `users:read` | Resolve user IDs to names |
| `usergroups:write` | Create/manage user groups |
| `usergroups:read` | List user groups |

## Module Import

```python
from tools.slack_api import SlackClient

client = SlackClient()
channels = client.list_channels()
client.create_channel("new-project", description="Project discussions")
```
