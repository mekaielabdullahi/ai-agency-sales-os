# Notion Module

Notion page, database, and block management module for Agentic Workspaces.

## Features

- **Pages**: Create, read, update, archive, restore
- **Databases**: Query with filters/sorts, create with custom schemas
- **Blocks**: Read content, append, update, delete
- **Search**: Full-text search across workspace
- **Helpers**: Markdown-to-blocks conversion for easy content creation

## Installation

The module is bundled with agentic. Ensure dependencies are installed:

```bash
pip install notion-client python-dotenv
```

## Environment Variables

Add to your `.env`:

```
NOTION_API_KEY=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Getting Your API Key

1. Go to https://www.notion.so/my-integrations
2. Click **"+ New integration"**
3. Fill in:
   - **Name**: "Agentic Workspace"
   - **Associated workspace**: Select your workspace
   - **Capabilities**: Read, Update, Insert content
4. Click **Submit** and copy the **Internal Integration Secret**
5. Share pages with the integration:
   - Open a page in Notion
   - Click **"..."** > **"Add connections"**
   - Select your integration

## Slash Commands

```
/notion-search project docs    # Search workspace
```

## CLI Usage

```bash
# Search
./run modules/notion/tool/notion_api.py search "project"
./run modules/notion/tool/notion_api.py search "notes" --filter page

# Pages
./run modules/notion/tool/notion_api.py pages get <page_id>
./run modules/notion/tool/notion_api.py pages create <parent_id> --title "New Page"
./run modules/notion/tool/notion_api.py pages create <parent_id> --title "Doc" --content "# Hello"
./run modules/notion/tool/notion_api.py pages archive <page_id>

# Databases
./run modules/notion/tool/notion_api.py databases get <db_id>
./run modules/notion/tool/notion_api.py databases query <db_id> --all
./run modules/notion/tool/notion_api.py databases query <db_id> --filter '{"property": "Status", "select": {"equals": "Done"}}'

# Blocks (page content)
./run modules/notion/tool/notion_api.py blocks children <page_id> --as-markdown
./run modules/notion/tool/notion_api.py blocks append <page_id> --content "## New Section"

# Users
./run modules/notion/tool/notion_api.py users list
./run modules/notion/tool/notion_api.py users me
```

## Module Import

```python
from modules.notion.tool.notion_api import NotionClient

client = NotionClient()

# Search
results = client.search("project", filter_type="page")

# Create page with markdown content
blocks = client.markdown_to_blocks("# Title\n\n- Item 1\n- Item 2")
page = client.create_page("parent-id", "My Page", children=blocks)

# Query database
entries = client.query_database_all("db-id", filter={
    "property": "Status",
    "select": {"equals": "Active"}
})

# Export page as markdown
blocks = client.get_all_block_children("page-id")
markdown = client.blocks_to_markdown(blocks)
```

## API Coverage

| Resource | Operations |
|----------|------------|
| Pages | get, create, update, archive, restore |
| Databases | get, query, query_all, create, update |
| Blocks | get, children, append, update, delete |
| Search | full-text with type filtering |
| Users | list, get, me (bot) |

## Limitations

- Integration can only access pages explicitly shared with it
- Rate limited to ~3 requests/second
- Some block types not supported by markdown converter (use JSON for those)
- Cannot manage workspace settings or permissions

## Related

- [Notion API Documentation](https://developers.notion.com/)
- [notion-client Python SDK](https://github.com/ramnes/notion-sdk-py)
