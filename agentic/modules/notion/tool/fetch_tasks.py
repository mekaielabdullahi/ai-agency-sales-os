#!/usr/bin/env python3
"""
Fetch Tasks from Notion Tasks Database

Quick script to pull all active tasks from the Tasks database for /status command.
Uses requests directly to avoid notion-client version issues.

Usage:
    python3 modules/notion/tool/fetch_tasks.py
    python3 modules/notion/tool/fetch_tasks.py --format json
"""

import sys
import os
import json
import argparse
from datetime import datetime
from typing import Dict, List, Any

from modules._shared.env import load_env
from modules._shared.notion import notion_request

load_env()

# Configuration
TASKS_DATABASE_ID = "2d5e7406-6c7d-810e-a1be-c35b71fdf23b"


def fetch_active_tasks() -> List[Dict]:
    """Fetch all active tasks (not Done or Cancelled) from Notion."""

    # Filter: Status is NOT Done AND NOT Cancelled
    filter_obj = {
        "and": [
            {
                "property": "Status",
                "status": {
                    "does_not_equal": "Done"
                }
            },
            {
                "property": "Status",
                "status": {
                    "does_not_equal": "Cancelled"
                }
            }
        ]
    }

    # Sort by Priority, then Due Date
    sorts = [
        {"property": "Priority", "direction": "ascending"},
        {"property": "Due Date", "direction": "ascending"}
    ]

    all_results = []
    start_cursor = None

    while True:
        data = {
            "filter": filter_obj,
            "sorts": sorts,
            "page_size": 100
        }
        if start_cursor:
            data["start_cursor"] = start_cursor

        response = notion_request("POST", f"databases/{TASKS_DATABASE_ID}/query", data)
        all_results.extend(response.get("results", []))

        if not response.get("has_more"):
            break
        start_cursor = response.get("next_cursor")

    return all_results


def extract_task_info(task: Dict) -> Dict:
    """Extract relevant info from a task object."""
    props = task.get("properties", {})

    # Task name (title)
    task_name = ""
    if "Task Name" in props:
        title_prop = props["Task Name"].get("title", [])
        task_name = "".join(t.get("plain_text", "") for t in title_prop)

    # Status
    status = ""
    if "Status" in props:
        status_prop = props["Status"].get("status")
        if status_prop:
            status = status_prop.get("name", "")

    # Priority
    priority = ""
    if "Priority" in props:
        priority_prop = props["Priority"].get("select")
        if priority_prop:
            priority = priority_prop.get("name", "")

    # Due Date
    due_date = ""
    if "Due Date" in props:
        date_prop = props["Due Date"].get("date")
        if date_prop:
            due_date = date_prop.get("start", "")

    # Project (relation)
    project = ""
    if "Project" in props:
        project_prop = props["Project"].get("relation", [])
        if project_prop:
            project = f"[{len(project_prop)} linked]"

    # Assigned To (people)
    assigned = []
    if "Assigned To" in props:
        people = props["Assigned To"].get("people", [])
        for person in people:
            name = person.get("name", "")
            if name:
                assigned.append(name)

    return {
        "id": task.get("id", ""),
        "url": task.get("url", ""),
        "name": task_name,
        "status": status,
        "priority": priority,
        "due_date": due_date,
        "project": project,
        "assigned": assigned
    }


def format_due_date(due_date: str) -> str:
    """Format due date for display."""
    if not due_date:
        return "-"

    try:
        date = datetime.fromisoformat(due_date.replace("Z", "+00:00"))
        today = datetime.now().date()

        if date.date() == today:
            return "Today"
        elif date.date() < today:
            days = (today - date.date()).days
            return f"{days}d overdue"
        else:
            return date.strftime("%b %d")
    except:
        return due_date[:10] if len(due_date) >= 10 else due_date


def format_markdown(tasks: List[Dict]) -> str:
    """Format tasks as markdown for /status output."""

    extracted = [extract_task_info(t) for t in tasks]

    # Group by priority and status
    urgent = [t for t in extracted if t["priority"] == "Urgent"]
    high = [t for t in extracted if t["priority"] == "High"]
    in_progress = [t for t in extracted if t["status"] == "In progress"]
    blocked = [t for t in extracted if t["status"] == "Blocked"]
    not_started = [t for t in extracted if t["status"] == "Not started"]
    to_review = [t for t in extracted if t["status"] == "To Review"]

    lines = [f"## Notion Tasks ({len(extracted)} open)\n"]

    # Urgent
    if urgent:
        lines.append(f"🔥 URGENT ({len(urgent)})")
        for t in urgent:
            assigned = f"@{t['assigned'][0]}" if t['assigned'] else ""
            due = format_due_date(t['due_date'])
            lines.append(f"• {t['name']} | Due: {due} | {assigned}")
        lines.append("")

    # High Priority
    if high:
        lines.append(f"🟠 HIGH ({len(high)})")
        for t in high:
            assigned = f"@{t['assigned'][0]}" if t['assigned'] else ""
            due = format_due_date(t['due_date'])
            lines.append(f"• {t['name']} | Due: {due} | {assigned}")
        lines.append("")

    # In Progress
    if in_progress:
        lines.append(f"🔵 IN PROGRESS ({len(in_progress)})")
        for t in in_progress:
            assigned = f"@{t['assigned'][0]}" if t['assigned'] else ""
            project = t['project'] if t['project'] else ""
            lines.append(f"• {t['name']} | {project} | {assigned}")
        lines.append("")

    # Blocked
    if blocked:
        lines.append(f"🟣 BLOCKED ({len(blocked)})")
        for t in blocked:
            lines.append(f"• {t['name']}")
        lines.append("")

    # To Review
    if to_review:
        lines.append(f"🟡 TO REVIEW ({len(to_review)})")
        for t in to_review:
            lines.append(f"• {t['name']}")
        lines.append("")

    # Not Started (exclude those already shown in urgent/high)
    not_started_other = [t for t in not_started if t not in urgent and t not in high]
    if not_started_other:
        lines.append(f"⬜ NOT STARTED ({len(not_started_other)})")
        for t in not_started_other[:5]:
            due = format_due_date(t['due_date'])
            lines.append(f"• {t['name']} | Due: {due}")
        if len(not_started_other) > 5:
            lines.append(f"  ... and {len(not_started_other) - 5} more")
        lines.append("")

    if len(extracted) == 0:
        lines.append("✅ No open tasks!")

    return "\n".join(lines)


def format_json(tasks: List[Dict]) -> str:
    """Format tasks as JSON."""
    extracted = [extract_task_info(t) for t in tasks]
    return json.dumps(extracted, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Fetch tasks from Notion")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown",
                        help="Output format (default: markdown)")
    args = parser.parse_args()

    try:
        tasks = fetch_active_tasks()

        if args.format == "json":
            print(format_json(tasks))
        else:
            print(format_markdown(tasks))

    except Exception as e:
        print(f"Error fetching tasks: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
