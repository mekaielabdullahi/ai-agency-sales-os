# agentic-module-diagrams

Generate diagrams in multiple formats from structured input or natural language descriptions.

## Features

- **Draw.io (.drawio)**: Full-featured diagrams with swimlanes, flowcharts, architecture
- **Mermaid**: Code-based diagrams for Markdown embedding
- **ASCII Migration**: Convert legacy ASCII diagrams to Mermaid
- **Dual Input**: JSON structured input OR natural language descriptions

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-diagrams
```

## Environment Variables

```
OPENAI_API_KEY=sk-your-api-key  # Required for ASCII migration & NL processing
```

## Slash Commands

```
/diagram "Create a flowchart showing user login process"
/drawio input.json --output login_flow.drawio
/mermaid input.json --output diagram.md
/migrate-ascii path/to/docs/ --apply
```

## Input Formats

### Structured JSON

```json
{
  "type": "flowchart",
  "title": "Login Flow",
  "direction": "TD",
  "nodes": [
    {"id": "start", "label": "User visits site", "shape": "ellipse"},
    {"id": "check", "label": "Check credentials", "shape": "diamond"}
  ],
  "connections": [
    {"from": "start", "to": "check", "label": "Submit"}
  ]
}
```

### Natural Language

Simply describe what you want:
> "Create a swimlane diagram showing the sales process with 4 phases: Lead Generation, Qualification, Proposal, and Close"

## Templates

Pre-built templates are available in `templates/`:
- `flowchart_simple.json` - Basic flowchart input template
- `swimlane_process.json` - Multi-phase swimlane input template

## Tools

| Tool | Purpose |
|------|---------|
| `generate_drawio.py` | Generate Draw.io XML from JSON |
| `generate_mermaid.py` | Generate Mermaid syntax from JSON |
| `migrate_ascii_to_mermaid.py` | Convert ASCII flowcharts to Mermaid |
