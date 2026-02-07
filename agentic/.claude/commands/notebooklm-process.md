# NotebookLM Process Command

Run a complete NotebookLM workflow: create notebook, upload sources, run queries, save outputs.

## Usage

```
/notebooklm-process --workflow=<workflow> --sources=<files> [--name=<notebook_name>]
```

## Workflows

| Workflow | Use Case |
|----------|----------|
| `meeting-transcript` | Process meeting recordings → action items, decisions, concerns |
| `client-discovery` | Pre-call research → bottlenecks, opportunities, tech stack |
| `proposal-research` | Mine past wins → scope, pricing, objections |
| `content-repurpose` | Long content → LinkedIn posts, hooks, contrarian takes |

## Examples

```bash
# Process today's Plotter Mechanix call
/notebooklm-process --workflow=meeting-transcript --sources=transcript.md

# Discovery research for new client
/notebooklm-process --workflow=client-discovery --sources=website.pdf,emails.md,linkedin.md --name=NewClient-Discovery

# Repurpose a blog post
/notebooklm-process --workflow=content-repurpose --sources=blog-post.md
```

## What This Command Does

1. **Create Notebook** - Named `[ClientCode]-[Date]` or custom name
2. **Upload Sources** - All specified files
3. **Run Query Template** - 4 queries per workflow
4. **Save Outputs** - Markdown file in same directory as sources
5. **Return Summary** - Key findings in chat

## Requirements

- `notebooklm-py` installed (`pip install notebooklm-py`)
- Google auth completed (`notebooklm auth`)

## Output Location

Outputs saved to: `[source_dir]/[notebook_name]-output.md`
