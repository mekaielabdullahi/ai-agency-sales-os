#!/usr/bin/env python3
"""
Notion Upload Script - Chunked Markdown Upload

Uploads markdown files to Notion pages, automatically handling the 100-block
limit by splitting content into sections.

Usage:
    python notion_upload.py --file "/path/to/doc.md" --page-id "xxx-xxx"
    python notion_upload.py --file "README.md" --parent-id "xxx" --title "My Doc"
"""

import os
import sys
import argparse
import subprocess
import tempfile
from pathlib import Path

# Notion plugin location
NOTION_PLUGIN_DIR = Path.home() / ".claude/plugins/cache/cc-plugins/notion/1.5.2"


def run_notion_cmd(args: list, timeout: int = 30) -> tuple[bool, str]:
    """Run a Notion API command and return success status and output."""
    cmd = ["python", "-m", "tool.notion_api"] + args
    env = {**os.environ, "PYTHONUTF8": "1"}

    try:
        result = subprocess.run(
            cmd,
            cwd=str(NOTION_PLUGIN_DIR),
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env
        )

        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)


def search_page(query: str) -> str | None:
    """Search for a Notion page by name and return its ID."""
    success, output = run_notion_cmd(["search", query, "--filter", "page"])

    if success and "id" in output:
        # Extract first page ID from results
        import json
        try:
            # Find the JSON array in output
            start = output.find("[")
            end = output.rfind("]") + 1
            if start >= 0 and end > start:
                results = json.loads(output[start:end])
                if results:
                    return results[0].get("id")
        except json.JSONDecodeError:
            pass

    return None


def create_page(parent_id: str, title: str, icon: str = "📄", initial_content: str = None) -> str | None:
    """Create a new Notion page and return its ID."""
    content = initial_content or f"# {title}\n\n*Loading content...*"

    args = [
        "pages", "create", parent_id,
        "--title", title,
        "--content", content,
        "--icon", icon
    ]

    success, output = run_notion_cmd(args)

    if success:
        import json
        try:
            # Parse the JSON response
            start = output.find("{")
            end = output.rfind("}") + 1
            if start >= 0 and end > start:
                result = json.loads(output[start:end])
                return result.get("id")
        except json.JSONDecodeError:
            pass
    else:
        print(f"Failed to create page: {output}")

    return None


def split_markdown_sections(content: str) -> list[str]:
    """Split markdown content by ## headers into sections."""
    sections = content.split("\n## ")

    result = []
    for i, section in enumerate(sections):
        if i == 0:
            # First section (before first ##) - skip if just frontmatter
            if section.strip() and not section.strip().startswith("---"):
                result.append(section)
        else:
            result.append("## " + section)

    return result


def append_section(page_id: str, content: str, section_num: int) -> bool:
    """Append a section of content to a Notion page."""
    # Truncate very long sections
    if len(content) > 15000:
        content = content[:15000] + "\n\n*[Content truncated due to length]*"

    # Write to temp file to handle special characters
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(content)
        temp_path = f.name

    try:
        success, output = run_notion_cmd(
            ["blocks", "append", page_id, "--content-file", temp_path],
            timeout=60
        )

        if not success:
            print(f"  Section {section_num} warning: {output[:100]}...")
            return False

        return True
    finally:
        os.unlink(temp_path)


def upload_markdown(file_path: str, page_id: str) -> tuple[int, int]:
    """Upload a markdown file to an existing Notion page in chunks."""
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into sections
    sections = split_markdown_sections(content)

    success_count = 0
    fail_count = 0

    print(f"Uploading {len(sections)} sections...")

    for i, section in enumerate(sections, 1):
        if append_section(page_id, section, i):
            print(f"  ✓ Section {i}/{len(sections)}")
            success_count += 1
        else:
            fail_count += 1

    return success_count, fail_count


def main():
    parser = argparse.ArgumentParser(description="Upload markdown to Notion")
    parser.add_argument("--file", required=True, help="Path to markdown file")
    parser.add_argument("--page-id", help="Existing Notion page ID to append to")
    parser.add_argument("--parent-id", help="Parent page ID to create new page under")
    parser.add_argument("--parent-name", help="Parent page name (will search)")
    parser.add_argument("--title", help="Page title (extracted from # heading if not provided)")
    parser.add_argument("--icon", default="📄", help="Page icon emoji")

    args = parser.parse_args()

    # Validate file exists
    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        sys.exit(1)

    # Read file to extract title if needed
    with open(args.file, 'r', encoding='utf-8') as f:
        content = f.read()

    title = args.title
    if not title:
        # Extract from first # heading
        for line in content.split('\n'):
            if line.startswith('# '):
                title = line[2:].strip()
                break
        if not title:
            title = Path(args.file).stem

    page_id = args.page_id

    # If no page ID, create new page
    if not page_id:
        parent_id = args.parent_id

        # Search for parent if name provided
        if not parent_id and args.parent_name:
            print(f"Searching for '{args.parent_name}'...")
            parent_id = search_page(args.parent_name)
            if not parent_id:
                print(f"Error: Could not find page '{args.parent_name}'")
                sys.exit(1)
            print(f"Found parent: {parent_id}")

        if not parent_id:
            print("Error: Must provide --page-id, --parent-id, or --parent-name")
            sys.exit(1)

        # Create the page
        print(f"Creating page '{title}'...")
        page_id = create_page(parent_id, title, args.icon)

        if not page_id:
            print("Error: Failed to create page")
            sys.exit(1)

        print(f"Created page: {page_id}")

    # Upload content
    success, failed = upload_markdown(args.file, page_id)

    print(f"\n{'='*50}")
    print(f"Upload complete!")
    print(f"  Sections uploaded: {success}")
    if failed:
        print(f"  Sections failed: {failed}")
    print(f"  Page ID: {page_id}")
    print(f"  URL: https://notion.so/{page_id.replace('-', '')}")
    print(f"{'='*50}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
