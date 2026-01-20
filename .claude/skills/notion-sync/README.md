# Notion Sync Skill

Push markdown documents to Notion with automatic chunking for large files.

## Quick Start

```bash
# Upload to existing page
python scripts/notion_upload.py --file "doc.md" --page-id "xxx-xxx-xxx"

# Create new page under parent
python scripts/notion_upload.py --file "README.md" --parent-id "xxx" --title "My Doc"

# Search for parent by name
python scripts/notion_upload.py --file "guide.md" --parent-name "Internal Projects" --icon "📚"
```

## Features

- **Auto-chunking**: Splits large documents by `##` headers to bypass Notion's 100-block limit
- **Search by name**: Find parent pages by title instead of ID
- **UTF-8 support**: Handles special characters and emojis
- **Progress reporting**: Shows upload status per section
- **Error resilience**: Continues uploading even if some sections fail

## Common Targets

| Name | Page ID |
|------|---------|
| Internal Projects | `2ede7406-6c7d-815a-8988-db6b23fad418` |

## Requirements

- Python 3.10+
- Notion MCP plugin installed
- `NOTION_API_KEY` in `~/.config/cc-plugins/.env`

## Invoking via Claude Code

Say any of:
- "Push this document to Notion"
- "Sync README to Internal Projects"
- "Upload the brand guidelines to Notion"
- "Create a Notion page from this markdown"
