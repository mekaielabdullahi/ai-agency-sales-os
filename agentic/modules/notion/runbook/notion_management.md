# Notion Management

## Execution Method
**Always use Python**: `modules/notion/tool/notion_api.py`

## Purpose
Manage Notion pages, databases, and content blocks via the API. Use this for
documentation management, knowledge base operations, project tracking databases,
and workspace search.

## When to Use This Directive

**Trigger phrases:**
- "Create a Notion page for..."
- "Add content to the Notion page"
- "Query the project database"
- "Search Notion for..."
- "Archive the old documentation"
- "Update the database entry"
- "List items in the Notion database"
- "Export page content"

## Execution Tools

**Location:** `modules/notion/tool/notion_api.py`

---

## Page Operations

### Get Page
```bash
./run modules/notion/tool/notion_api.py pages get <page_id>
```

### Create Page
```bash
# Create page under another page
./run modules/notion/tool/notion_api.py pages create <parent_page_id> \
  --title "New Page Title" \
  --content "# Heading\n\nParagraph content" \
  --icon "📄"

# Create page in a database
./run modules/notion/tool/notion_api.py pages create <database_id> \
  --title "New Entry" \
  --database

# Create from markdown file
./run modules/notion/tool/notion_api.py pages create <parent_id> \
  --title "Documentation" \
  --content-file .tmp/content.md
```

### Update Page
```bash
./run modules/notion/tool/notion_api.py pages update <page_id> --title "New Title"
./run modules/notion/tool/notion_api.py pages update <page_id> --icon "✅"
```

### Archive/Restore
```bash
./run modules/notion/tool/notion_api.py pages archive <page_id>
./run modules/notion/tool/notion_api.py pages restore <page_id>
```

---

## Database Operations

### Query Database
```bash
# Get entries (default: 100)
./run modules/notion/tool/notion_api.py databases query <database_id>

# Get ALL entries (paginated)
./run modules/notion/tool/notion_api.py databases query <database_id> --all

# With filter
./run modules/notion/tool/notion_api.py databases query <database_id> \
  --filter '{"property": "Status", "select": {"equals": "Active"}}'

# With sorting
./run modules/notion/tool/notion_api.py databases query <database_id> \
  --sorts '[{"property": "Created", "direction": "descending"}]'
```

### Get Database Schema
```bash
./run modules/notion/tool/notion_api.py databases get <database_id>
```

### Create Database
```bash
./run modules/notion/tool/notion_api.py databases create <parent_page_id> \
  --title "Project Tracker" \
  --properties '{
    "Name": {"title": {}},
    "Status": {"select": {"options": [{"name": "Not Started"}, {"name": "In Progress"}, {"name": "Done"}]}},
    "Due Date": {"date": {}}
  }'
```

---

## Block Operations

### Get Page Content
```bash
# Get as JSON
./run modules/notion/tool/notion_api.py blocks children <page_id>

# Get ALL blocks (paginated)
./run modules/notion/tool/notion_api.py blocks children <page_id> --all

# Get as markdown
./run modules/notion/tool/notion_api.py blocks children <page_id> --as-markdown
```

### Append Content
```bash
# Append markdown
./run modules/notion/tool/notion_api.py blocks append <page_id> \
  --content "## New Section\n\nAdded paragraph."

# Append from file
./run modules/notion/tool/notion_api.py blocks append <page_id> \
  --content-file .tmp/additional_content.md

# Append raw JSON blocks
./run modules/notion/tool/notion_api.py blocks append <page_id> \
  --json '[{"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Hello"}}]}}]'
```

### Delete Block
```bash
./run modules/notion/tool/notion_api.py blocks delete <block_id>
```

---

## Search

```bash
# Search everything
./run modules/notion/tool/notion_api.py search "project documentation"

# Search only pages
./run modules/notion/tool/notion_api.py search "meeting notes" --filter page

# Search only databases
./run modules/notion/tool/notion_api.py search "tracker" --filter database

# Limit results
./run modules/notion/tool/notion_api.py search "notes" --limit 10
```

---

## Users

```bash
# List all users
./run modules/notion/tool/notion_api.py users list

# Get bot info
./run modules/notion/tool/notion_api.py users me

# Get specific user
./run modules/notion/tool/notion_api.py users get <user_id>
```

---

## Module Usage

```python
from modules.notion.tool.notion_api import NotionClient

client = NotionClient()

# Search
results = client.search("project", filter_type="page")

# Get page
page = client.get_page("page-id-here")

# Query database
entries = client.query_database_all("db-id", filter={
    "property": "Status",
    "select": {"equals": "Active"}
})

# Create page with content
blocks = client.markdown_to_blocks("# Title\n\nContent here")
page = client.create_page("parent-id", "My Page", children=blocks)

# Get page content as markdown
blocks = client.get_all_block_children("page-id")
markdown = client.blocks_to_markdown(blocks)
```

---

## Environment Variables

Required in `.env`:
```
NOTION_API_KEY=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Getting Your API Key

1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Name it (e.g., "Agentic Workspace")
4. Select the workspace
5. Set capabilities: Read content, Update content, Insert content
6. Copy the "Internal Integration Secret"
7. Add pages/databases to the integration:
   - Open the page in Notion
   - Click "..." menu > "Add connections"
   - Select your integration

---

## Edge Cases & Learnings

### Access Control
- The integration can only access pages explicitly shared with it
- Share parent pages to grant access to child pages
- Database entries inherit access from the database

### Rate Limits
- Notion API: ~3 requests/second average
- The client raises `NotionRateLimitError` on 429 responses
- Add retry logic for high-volume operations

### IDs
- All Notion IDs are UUIDs (with or without dashes)
- Pages, databases, and blocks all use the same ID format
- A page ID can also be used as a block ID

### Content Blocks
- Block types: paragraph, heading_1/2/3, bulleted_list_item,
  numbered_list_item, code, quote, callout, divider, toggle, to_do
- Some block types have children (toggle, column_list)
- The markdown converter handles common types
- For complex layouts, use raw JSON blocks

### Database Properties
- Common types: title, rich_text, number, select, multi_select,
  date, checkbox, url, email, phone_number, formula, relation, rollup
- The "Name" or "Title" property is required for all database entries
- Filter syntax: https://developers.notion.com/reference/post-database-query-filter

### Pagination
- List operations return max 100 items
- Use `--all` flag to auto-paginate
- Or manually use `start_cursor` and `has_more` in Python

### Markdown Conversion
The `markdown_to_blocks()` helper supports:
- Headings: `# ## ###`
- Lists: `- ` bullets, `1.` numbered
- Checkboxes: `- [ ]` and `- [x]`
- Code blocks: triple backticks with language
- Quotes: `>`
- Dividers: `---`

For unsupported markdown (tables, images), create blocks manually with JSON.

---

## Common Workflows

### Create Documentation Page
```bash
# Create page with initial content
./run modules/notion/tool/notion_api.py pages create <docs-page-id> \
  --title "API Documentation" \
  --content-file docs/api.md \
  --icon "📚"
```

### Export Page to Markdown
```bash
./run modules/notion/tool/notion_api.py blocks children <page-id> --all --as-markdown > .tmp/export.md
```

### Bulk Query Database
```bash
# Get all entries with specific status
./run modules/notion/tool/notion_api.py databases query <db-id> --all \
  --filter '{"property": "Status", "select": {"equals": "Done"}}'
```

### Add Entry to Database
```bash
# Create page in database
./run modules/notion/tool/notion_api.py pages create <database-id> \
  --title "New Task" \
  --database
```

---

## Filter Examples

### Select Property
```json
{"property": "Status", "select": {"equals": "Active"}}
```

### Checkbox Property
```json
{"property": "Done", "checkbox": {"equals": true}}
```

### Date Property
```json
{"property": "Due Date", "date": {"on_or_before": "2024-12-31"}}
```

### Text Contains
```json
{"property": "Name", "rich_text": {"contains": "project"}}
```

### Compound Filter (AND)
```json
{
  "and": [
    {"property": "Status", "select": {"equals": "Active"}},
    {"property": "Assignee", "people": {"contains": "user-id"}}
  ]
}
```

### Compound Filter (OR)
```json
{
  "or": [
    {"property": "Status", "select": {"equals": "Active"}},
    {"property": "Status", "select": {"equals": "In Progress"}}
  ]
}
```

---

## Sort Examples

```json
[{"property": "Created time", "direction": "descending"}]
```

```json
[
  {"property": "Priority", "direction": "descending"},
  {"property": "Name", "direction": "ascending"}
]
```
