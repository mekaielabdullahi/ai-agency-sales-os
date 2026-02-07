# NotebookLM Automation Module

Automates NotebookLM workflows for AriseGroup using the unofficial `notebooklm-py` CLI.

> ⚠️ **Warning:** Uses undocumented Google APIs that can change without notice. Not for production client-facing systems.

## Quick Start

### 1. Install Dependencies

```bash
pip install notebooklm-py --break-system-packages
```

### 2. Authenticate with Google

```bash
notebooklm auth
```

This opens a browser for Google OAuth. Complete the flow once.

### 3. Test It Works

```bash
notebooklm list  # Should show your notebooks (empty at first)
```

## Usage

### Via Claude Commands

```bash
# Process a meeting transcript
/notebooklm-process --workflow=meeting-transcript --sources=transcript.md

# Create a client discovery notebook
/notebooklm-create "PM-Discovery"

# Upload sources
/notebooklm-upload PM-Discovery transcript.md scope.pdf notes.md

# Run a query
/notebooklm-query PM-Discovery "Extract action items with owners"
```

### Via Python

```python
from tool.notebooklm_client import NotebookLMClient, run_workflow

# Simple query
client = NotebookLMClient()
notebook_id = client.create_notebook("Test")
client.upload_sources(notebook_id, ["doc.pdf"])
result = client.query(notebook_id, "Summarize this document")

# Full workflow
result = run_workflow(
    workflow_name="meeting_transcript",
    notebook_name="PM-2026-02-03",
    sources=["transcript.md", "context.md"],
    output_dir="./outputs"
)
```

### Via n8n

See `extras/n8n-wf/notebooklm_automation.json` for workflow templates.

## Available Workflows

| Workflow | Purpose | Queries Run |
|----------|---------|-------------|
| `meeting_transcript` | Process meeting recordings | 4 queries |
| `client_discovery` | Pre-call research | 4 queries |
| `proposal_research` | Mine past wins | 4 queries |
| `content_repurpose` | Turn content into posts | 4 queries |

## File Triggers (Planned)

When fully configured, these auto-trigger:

| Trigger | Action |
|---------|--------|
| New `transcript.md` in any `meetings/` folder | Run meeting_transcript workflow |
| Monday 8am | Batch process week's content |

## Limitations

- No official API (uses reverse-engineered endpoints)
- Can break without notice when Google updates
- Rate limits unknown
- Audio overview may not work in all regions
- 50 source limit per notebook

## Troubleshooting

### "notebooklm not found"
```bash
pip install notebooklm-py --break-system-packages
```

### "Authentication failed"
```bash
notebooklm auth --force  # Re-authenticate
```

### "Rate limited"
Wait 5 minutes, reduce batch sizes.

## Related

- [NotebookLM Integration Workflow](../../../cto-hub/workflows/notebooklm-integration.md)
- [notebooklm-py GitHub](https://github.com/teng-lin/notebooklm-py)
