#!/usr/bin/env python3
"""
Create Follow-up Tasks in Notion

Creates follow-up tasks in the Notion Tasks database after outreach.
Used by /new-lead workflow to ensure leads don't go cold.

Default follow-up sequence:
1. Follow up in 3 days if no response
2. Second follow up in 7 days
3. Final follow up / nurture decision in 14 days

Usage:
    python3 create_follow_up.py --contact "Brian Powell" --email "brian@test.com"
    python3 create_follow_up.py --contact "Brian Powell" --contact-id "xxx" --custom-days 3,7,14
    python3 create_follow_up.py --contact "Brian Powell" --single --days 5 --task "Schedule discovery call"
"""

import os
import sys
import argparse
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load env
def load_env():
    env_paths = [
        os.path.join(SCRIPT_DIR, '..', '..', '..', '.env'),
        os.path.join(SCRIPT_DIR, '..', '..', '.env'),
    ]
    for env_path in env_paths:
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ.setdefault(key.strip(), value.strip())
            break

load_env()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_VERSION = "2022-06-28"

# Database IDs
TASKS_DATABASE_ID = "2d5e7406-6c7d-810e-a1be-c35b71fdf23b"
CONTACTS_DATABASE_ID = "2d5e7406-6c7d-81d3-ae7c-c375989f3bb0"

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

# Default follow-up sequence
DEFAULT_FOLLOW_UPS = [
    {"days": 3, "task": "Follow up with {name} if no response", "priority": "High"},
    {"days": 7, "task": "Second follow up with {name}", "priority": "Medium"},
    {"days": 14, "task": "Final follow up / nurture decision for {name}", "priority": "Low"},
]


def create_task(
    task_name: str,
    due_date: str,
    priority: str = "Medium",
    contact_id: Optional[str] = None,
    notes: Optional[str] = None
) -> Dict:
    """
    Create a task in Notion Tasks database.

    Args:
        task_name: Name of the task
        due_date: Due date in YYYY-MM-DD format
        priority: "Urgent", "High", "Medium", "Low"
        contact_id: Notion page ID of related contact (optional)
        notes: Additional notes for the task

    Returns:
        Dict with success status and task details
    """
    if not NOTION_API_KEY:
        return {"success": False, "error": "NOTION_API_KEY not configured"}

    # Build properties
    properties = {
        "Task Name": {
            "title": [{"text": {"content": task_name}}]
        },
        "Due Date": {
            "date": {"start": due_date}
        },
        "Priority": {
            "select": {"name": priority}
        },
        "Status": {
            "status": {"name": "Not started"}
        }
    }

    # Add description/notes if provided
    if notes:
        properties["Description"] = {
            "rich_text": [{"text": {"content": notes}}]
        }

    # Note: Tasks DB doesn't have a Contacts relation field
    # Contact reference is included in task name instead

    # Create the task
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=HEADERS,
        json={
            "parent": {"database_id": TASKS_DATABASE_ID},
            "properties": properties
        }
    )

    if response.status_code == 200:
        task = response.json()
        return {
            "success": True,
            "task_id": task.get("id"),
            "task_name": task_name,
            "due_date": due_date,
            "priority": priority,
            "url": task.get("url"),
            "message": f"Task created: {task_name} (due {due_date})"
        }
    else:
        error = response.json().get("message", response.text)
        return {
            "success": False,
            "error": f"Notion API error: {error}",
            "status_code": response.status_code
        }


def create_follow_up_sequence(
    contact_name: str,
    contact_id: Optional[str] = None,
    contact_email: Optional[str] = None,
    custom_days: Optional[List[int]] = None,
    outreach_type: str = "cold"
) -> Dict:
    """
    Create standard follow-up task sequence for a contact.

    Args:
        contact_name: Name of the contact
        contact_id: Notion page ID of the contact (for relation)
        contact_email: Email for reference in task notes
        custom_days: Override default [3, 7, 14] day sequence
        outreach_type: "cold" or "follow-up" for task context

    Returns:
        Dict with created tasks and summary
    """
    today = datetime.now().date()
    tasks_created = []
    errors = []

    # Use custom days or default sequence
    if custom_days:
        follow_ups = [
            {"days": d, "task": f"Follow up with {{name}}", "priority": "Medium"}
            for d in custom_days
        ]
    else:
        follow_ups = DEFAULT_FOLLOW_UPS

    for follow_up in follow_ups:
        due_date = (today + timedelta(days=follow_up["days"])).strftime("%Y-%m-%d")
        task_name = follow_up["task"].format(name=contact_name)

        # Add context about outreach type
        if outreach_type == "cold" and follow_up == follow_ups[0]:
            task_name = f"Follow up with {contact_name} (cold outreach - no response)"

        # Build notes with contact info
        notes = None
        if contact_email:
            notes = f"Contact: {contact_name}\nEmail: {contact_email}"
            if contact_id:
                notes += f"\nNotion: https://notion.so/{contact_id.replace('-', '')}"

        result = create_task(
            task_name=task_name,
            due_date=due_date,
            priority=follow_up["priority"],
            notes=notes
        )

        if result["success"]:
            tasks_created.append({
                "task": task_name,
                "due": due_date,
                "priority": follow_up["priority"],
                "url": result.get("url")
            })
        else:
            errors.append(result["error"])

    return {
        "success": len(errors) == 0,
        "tasks_created": tasks_created,
        "total": len(tasks_created),
        "errors": errors if errors else None,
        "contact_name": contact_name,
        "contact_email": contact_email
    }


def create_single_follow_up(
    contact_name: str,
    task_description: str,
    days: int,
    priority: str = "Medium",
    contact_id: Optional[str] = None
) -> Dict:
    """
    Create a single follow-up task.

    Args:
        contact_name: Name of the contact
        task_description: Custom task description
        days: Days from today for due date
        priority: Task priority
        contact_id: Notion contact ID for relation
    """
    due_date = (datetime.now().date() + timedelta(days=days)).strftime("%Y-%m-%d")

    # Format task name with contact if not included
    if contact_name.lower() not in task_description.lower():
        task_name = f"{task_description} - {contact_name}"
    else:
        task_name = task_description

    return create_task(
        task_name=task_name,
        due_date=due_date,
        priority=priority,
        contact_id=contact_id
    )


def format_output(result: Dict) -> str:
    """Format the result for display."""
    lines = []

    if result.get("tasks_created"):
        lines.append(f"## Follow-up Tasks Created for {result['contact_name']}")
        lines.append("")
        for task in result["tasks_created"]:
            priority_icon = {"Urgent": "🔴", "High": "🟠", "Medium": "🟡", "Low": "🟢"}.get(task["priority"], "⚪")
            lines.append(f"{priority_icon} **{task['task']}**")
            lines.append(f"   Due: {task['due']} | Priority: {task['priority']}")
            if task.get("url"):
                lines.append(f"   Notion: {task['url']}")
            lines.append("")

        lines.append(f"Total: {result['total']} tasks created")
    elif result.get("task_name"):
        # Single task result
        lines.append(f"✅ Task created: {result['task_name']}")
        lines.append(f"   Due: {result['due_date']} | Priority: {result['priority']}")

    if result.get("errors"):
        lines.append("")
        lines.append("⚠️ Errors:")
        for error in result["errors"]:
            lines.append(f"   - {error}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Create follow-up tasks in Notion")
    parser.add_argument("--contact", required=True, help="Contact name")
    parser.add_argument("--contact-id", help="Notion contact page ID (for relation)")
    parser.add_argument("--email", help="Contact email (for reference)")
    parser.add_argument("--custom-days", help="Custom follow-up days (comma-separated, e.g., '3,7,14')")
    parser.add_argument("--outreach-type", choices=["cold", "follow-up"], default="cold",
                        help="Type of outreach (affects task wording)")

    # Single task mode
    parser.add_argument("--single", action="store_true", help="Create single task instead of sequence")
    parser.add_argument("--task", help="Task description (for single task mode)")
    parser.add_argument("--days", type=int, help="Days until due (for single task mode)")
    parser.add_argument("--priority", choices=["Urgent", "High", "Medium", "Low"], default="Medium",
                        help="Task priority (for single task mode)")

    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.single:
        if not args.task or not args.days:
            print("Error: --single mode requires --task and --days")
            sys.exit(1)

        result = create_single_follow_up(
            contact_name=args.contact,
            task_description=args.task,
            days=args.days,
            priority=args.priority,
            contact_id=args.contact_id
        )
    else:
        custom_days = None
        if args.custom_days:
            custom_days = [int(d.strip()) for d in args.custom_days.split(",")]

        result = create_follow_up_sequence(
            contact_name=args.contact,
            contact_id=args.contact_id,
            contact_email=args.email,
            custom_days=custom_days,
            outreach_type=args.outreach_type
        )

    if args.json:
        import json
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))

    if not result["success"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
