# agentic-module-n8n

Manage n8n workflows - list, deploy, activate, execute, and monitor.

## Features

- List all workflows and their status
- Deploy workflows from local JSON files
- Activate/deactivate workflows
- Execute workflows via webhook triggers
- View execution history
- Export workflows to local files

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-n8n
```

## Setup

1. Get your n8n API key from Settings > API
2. Add to `.env`:
   ```
   N8N_API_URL=https://your-n8n-instance.com
   N8N_API_KEY=your_api_key_here
   ```

## Slash Commands

```
/workflow-list                    # List all workflows
/workflow-deploy <json_path>      # Deploy from file
/workflow-activate <workflow_id>  # Activate workflow
/workflow-execute <workflow_id>   # Execute via webhook
/workflow-history <workflow_id>   # View execution history
```

## CLI Usage

```bash
# List workflows
./run modules/n8n/tool/n8n_api.py list

# Get workflow details
./run modules/n8n/tool/n8n_api.py get <workflow_id>

# Get workflow info (triggers, webhook URLs)
./run modules/n8n/tool/n8n_api.py info <workflow_id>

# Create new workflow
./run modules/n8n/tool/n8n_api.py create workflows/my_workflow.json

# Update existing workflow
./run modules/n8n/tool/n8n_api.py update <workflow_id> workflows/my_workflow.json

# Activate/deactivate
./run modules/n8n/tool/n8n_api.py activate <workflow_id>
./run modules/n8n/tool/n8n_api.py deactivate <workflow_id>

# Execute via webhook (requires webhook trigger + active workflow)
./run modules/n8n/tool/n8n_api.py execute <workflow_id> [input_json]

# View executions
./run modules/n8n/tool/n8n_api.py executions <workflow_id>

# Export to file
./run modules/n8n/tool/n8n_api.py export <workflow_id> workflows/exported.json

# Delete (with confirmation)
./run modules/n8n/tool/n8n_api.py delete <workflow_id>
```

## Workflow Development

1. **Design in n8n UI** - Build and test visually
2. **Export** - `./run modules/n8n/tool/n8n_api.py export <id> workflows/<name>.json`
3. **Version control** - Commit JSON to repository
4. **Deploy updates** - `./run modules/n8n/tool/n8n_api.py update <id> workflows/<name>.json`

## Important: API Execution Limitation

The n8n public API does not support direct workflow execution. The `execute` command works by calling the workflow's **webhook trigger**.

To execute a workflow via API:
1. Add a **Webhook node** as the trigger
2. **Activate** the workflow
3. Use `execute` to call the webhook

Use `info <workflow_id>` to see a workflow's triggers and webhook URLs.

## When to Use n8n vs Python Scripts

| n8n | Python |
|-----|--------|
| Scheduled tasks (cron) | Complex data transforms |
| Webhook-driven flows | Heavy computation |
| Visual debugging needed | Custom logic |
| SaaS integrations | One-off executions |
| Non-technical users | Local file processing |
