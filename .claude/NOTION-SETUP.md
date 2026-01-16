# Notion MCP Integration Setup Guide

## Overview

Connect Claude Code to your Notion workspace to enable AI-powered reading and writing of your Notion pages, databases, and tasks.

## Prerequisites

1. A Notion account with a workspace
2. Access to create Notion integrations
3. Claude Code installed

## Setup Steps

### Step 1: Create Notion Integration

1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Click "+ New integration"
3. Name it "Claude Code OS" (or similar)
4. Select your workspace
5. Set capabilities:
   - [x] Read content
   - [x] Update content
   - [x] Insert content
   - [ ] Read comments (optional)
6. Click "Submit"
7. Copy the **Internal Integration Token** (starts with `secret_`)

### Step 2: Share Pages with Integration

In Notion:
1. Open the page/database you want Claude to access
2. Click "..." menu → "Connect to"
3. Search for "Claude Code OS"
4. Click to add

**Repeat for each page/database** you want accessible.

### Step 3: Install Notion MCP Server

There are several Notion MCP servers available:

**Option A: Official Notion MCP (Recommended)**
```bash
# Using npx (temporary install)
npx @anthropic/mcp-server-notion --token YOUR_NOTION_TOKEN

# Or install globally
npm install -g @anthropic/mcp-server-notion
```

**Option B: Community Notion MCP**
```bash
npm install -g notion-mcp-server
```

### Step 4: Configure Claude Code

Add the MCP server to your Claude Code configuration:

**For global config** (~/.claude.json):
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-notion"],
      "env": {
        "NOTION_API_KEY": "secret_your_token_here"
      }
    }
  }
}
```

**For project config** (.claude/settings.json):
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-notion"],
      "env": {
        "NOTION_API_KEY": "secret_your_token_here"
      }
    }
  }
}
```

### Step 5: Restart Claude Code

After configuration:
1. Exit Claude Code
2. Restart Claude Code
3. Check `/mcp` to verify the Notion server is connected

## Using Notion with Claude Code

Once connected, you can:

### Read Notion Pages
```
Read my Notion page "Weekly Planning"
```

### Search Notion
```
Search my Notion for "client meeting notes"
```

### Create/Update Pages
```
Create a new Notion page titled "January Goals" with my OBG for this month
```

### Work with Databases
```
Show me all tasks in my "Projects" database that are marked "In Progress"
```

## Useful Notion Commands to Add

Once Notion is connected, consider creating these slash commands:

### `/notion-sync` - Sync daily plan to Notion
```markdown
---
description: Sync today's plan to Notion
---

Take my current daily plan and:
1. Create/update today's page in my Daily Planning database
2. Add my THE ONE THING
3. List Tier 1 tasks as to-dos
4. Include my Kill List
```

### `/notion-review` - Pull data from Notion for review
```markdown
---
description: Pull weekly data from Notion for review
---

From my Notion workspace:
1. Get this week's daily plans
2. Calculate productivity scores
3. Identify completed vs incomplete tasks
4. Summarize for weekly review
```

## Troubleshooting

### "Notion server not connected"
- Check your API token is correct
- Ensure the integration is connected to the pages
- Restart Claude Code

### "Page not found"
- The page must be shared with your integration
- Go to Notion → Page → ... → Connect to → Claude Code OS

### "Rate limited"
- Notion has API rate limits
- Wait a moment and try again
- Batch operations when possible

## Security Notes

1. **Keep your token secret** - Never commit it to git
2. **Use environment variables** - Store token in env, not config files
3. **Limit access** - Only share necessary pages with the integration
4. **Review permissions** - Regularly audit what the integration can access

## Alternative: Environment Variable Setup

For better security, use environment variables:

**In your shell profile** (~/.bashrc or ~/.zshrc):
```bash
export NOTION_API_KEY="secret_your_token_here"
```

**In Claude config**:
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-notion"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    }
  }
}
```

## Next Steps

Once Notion is connected:
1. Create a "Claude Code OS" page in Notion
2. Set up databases for: Daily Plans, Weekly Reviews, Projects, Clients
3. Connect each database to the integration
4. Use Claude to read/write to your Notion workspace

---

*Need help? Check the MCP documentation at https://modelcontextprotocol.io/*
