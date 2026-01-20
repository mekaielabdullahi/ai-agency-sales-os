# Notion Sync Skill

## Purpose

Push markdown documents from the local codebase to Notion pages. Handles automatic chunking for large documents (Notion's 100-block limit), section-based uploads, and parent page organization.

## When to Use This Skill

- "Push this document to Notion"
- "Sync the README to Notion"
- "Create a Notion page from this markdown"
- "Upload this file to Internal Projects"
- "Export documentation to Notion"

## Prerequisites

- Notion API key configured in `~/.config/cc-plugins/.env` as `NOTION_API_KEY`
- Notion MCP plugin installed at `~/.claude/plugins/cache/cc-plugins/notion/`
- Target pages/databases shared with the Notion integration

## Skill Workflow

### Phase 1: Gather Information

When invoked, ask for:

1. **Source file**: Path to the markdown file to upload
2. **Target location**: Notion page name or ID (search if name provided)
3. **Page title**: Title for the new Notion page (default: extract from `# heading`)
4. **Icon**: Emoji icon for the page (optional)

### Phase 2: Search for Target

If user provides a page name instead of ID:

```bash
cd ~/.claude/plugins/cache/cc-plugins/notion/1.5.2
python -m tool.notion_api search "page name" --filter page
```

Extract the page ID from results.

### Phase 3: Create Page

Create the page under the target parent:

```bash
cd ~/.claude/plugins/cache/cc-plugins/notion/1.5.2
PYTHONUTF8=1 python -m tool.notion_api pages create "<parent_id>" \
  --title "Page Title" \
  --content "# Page Title\n\n*Loading content...*" \
  --icon "📄"
```

Save the returned page ID for content upload.

### Phase 4: Upload Content (Chunked)

For large documents, use the chunking script:

```bash
python scripts/notion_upload.py \
  --file "/path/to/document.md" \
  --page-id "<created_page_id>"
```

The script:
1. Reads the markdown file
2. Splits by `## ` headers into sections
3. Appends each section via the Notion API
4. Reports progress and any errors

### Phase 5: Report Results

Provide:
- Notion page URL
- Number of sections uploaded
- Any errors (e.g., invalid URLs, unsupported content)

## Common Targets

| Name | Page ID | Use For |
|------|---------|---------|
| Internal Projects | `2ede7406-6c7d-815a-8988-db6b23fad418` | Internal docs, guides |

*Add more targets as discovered via search*

## Supported Markdown

| Feature | Support |
|---------|---------|
| Headings (# ## ###) | ✅ Full |
| Bullet lists | ✅ Full |
| Numbered lists | ✅ Full |
| Checkboxes | ✅ Full |
| Code blocks | ✅ Full |
| Tables | ✅ Full |
| Bold/Italic/Code | ✅ Full |
| Links | ✅ Full |
| Images | ⚠️ URLs only |
| Nested lists | ⚠️ Partial |

## Error Handling

- **100 block limit**: Automatically chunked by sections
- **Invalid URLs**: Skipped with warning
- **Encoding issues**: UTF-8 enforced via `PYTHONUTF8=1`
- **API rate limits**: Pause between section uploads

## Example Usage

**User:** "Push the brand guidelines to Internal Projects"

**Skill:**
1. Searches Notion for "Internal Projects" → gets ID
2. Reads `brand-guidelines.md`
3. Creates page with title from `# heading`
4. Chunks and uploads all sections
5. Returns: `https://notion.so/Brand-Guidelines-xxxxx`
