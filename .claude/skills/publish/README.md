# Publish Skill

Publish approved content from brand-illustrator to LinkedIn.

## Quick Start

```bash
/publish                           # Publish most recent approved content
/publish 2026-01-19-ai-time-savings  # Publish specific project
```

## Requirements

- Approved content in brand-illustrator projects folder
- Claude in Chrome MCP for browser automation (or manual fallback)

## Workflow

1. Locates approved project content
2. Extracts image, copy, and hashtags
3. Previews post for confirmation
4. Publishes via LinkedIn (browser automation)
5. Archives project and logs publication

## See Also

- [brand-illustrator](../brand-illustrator/) - Content creation pipeline
- [content-strategy](../content-strategy/) - Content planning
