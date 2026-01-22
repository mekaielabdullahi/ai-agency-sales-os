#!/usr/bin/env python3
"""
Update Contact Status in Notion

Updates a contact's status after outreach is generated.
Used by /new-lead workflow to close the loop.

Actions:
- Update contact Type/Status to "Outreach Sent"
- Set Last Contacted to today
- Add activity note about outreach

Usage:
    python3 update_contact.py --contact-id "xxx" --status "Outreach Sent"
    python3 update_contact.py --contact-id "xxx" --note "Sent intro email about AI consulting"
    python3 update_contact.py --contact-id "xxx" --status "Outreach Sent" --note "Cold outreach" --last-contacted
"""

import os
import sys
import argparse
import requests
from datetime import datetime
from typing import Dict, Optional

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

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

# Valid status values for Type field (based on your Notion setup)
VALID_STATUSES = [
    "Lead",
    "Outreach Sent",
    "Responded",
    "Discovery Scheduled",
    "Discovery Complete",
    "Proposal Sent",
    "Negotiating",
    "Client",
    "Lost",
    "Nurture"
]


def update_contact(
    contact_id: str,
    status: Optional[str] = None,
    last_contacted: bool = False,
    note: Optional[str] = None
) -> Dict:
    """
    Update a contact in Notion.

    Args:
        contact_id: Notion page ID of the contact
        status: New status value (Type field)
        last_contacted: If True, set Last Contacted to today
        note: Text to append to Notes field

    Returns:
        Dict with success status and details
    """
    if not NOTION_API_KEY:
        return {"success": False, "error": "NOTION_API_KEY not configured"}

    # Build properties to update
    properties = {}

    # Update Type/Status
    if status:
        if status not in VALID_STATUSES:
            return {
                "success": False,
                "error": f"Invalid status '{status}'. Valid: {VALID_STATUSES}"
            }
        properties["Type"] = {
            "select": {"name": status}
        }

    # Update Last Contacted
    if last_contacted:
        today = datetime.now().strftime("%Y-%m-%d")
        properties["Last Contacted"] = {
            "date": {"start": today}
        }

    # If we need to append a note, first fetch existing notes
    if note:
        # Get current notes
        current_notes = get_current_notes(contact_id)

        # Append new note with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_note = f"\n\n[{timestamp}] {note}"
        updated_notes = (current_notes or "") + new_note

        properties["Notes"] = {
            "rich_text": [{"text": {"content": updated_notes[-2000:]}}]  # Notion limit
        }

    if not properties:
        return {"success": False, "error": "No updates specified"}

    # Make the update request
    response = requests.patch(
        f"https://api.notion.com/v1/pages/{contact_id}",
        headers=HEADERS,
        json={"properties": properties}
    )

    if response.status_code == 200:
        updates = []
        if status:
            updates.append(f"Status → {status}")
        if last_contacted:
            updates.append("Last Contacted → Today")
        if note:
            updates.append("Note added")

        return {
            "success": True,
            "contact_id": contact_id,
            "updates": updates,
            "message": f"Contact updated: {', '.join(updates)}"
        }
    else:
        error = response.json().get("message", response.text)
        return {
            "success": False,
            "error": f"Notion API error: {error}",
            "status_code": response.status_code
        }


def get_current_notes(contact_id: str) -> Optional[str]:
    """Fetch current Notes field value from contact."""
    response = requests.get(
        f"https://api.notion.com/v1/pages/{contact_id}",
        headers=HEADERS
    )

    if response.status_code != 200:
        return None

    props = response.json().get("properties", {})
    notes_prop = props.get("Notes", {}).get("rich_text", [])

    if notes_prop:
        return "".join(t.get("plain_text", "") for t in notes_prop)
    return None


def mark_outreach_sent(contact_id: str, email_subject: str, outreach_type: str = "cold") -> Dict:
    """
    Convenience function for /new-lead workflow.
    Updates contact after outreach email is generated.

    Args:
        contact_id: Notion contact page ID
        email_subject: Subject line of the email sent
        outreach_type: "cold" or "follow-up"
    """
    note = f"Outreach email drafted: '{email_subject}' ({outreach_type})"

    return update_contact(
        contact_id=contact_id,
        status="Outreach Sent",
        last_contacted=True,
        note=note
    )


def main():
    parser = argparse.ArgumentParser(description="Update contact in Notion")
    parser.add_argument("--contact-id", required=True, help="Notion page ID of contact")
    parser.add_argument("--status", help=f"New status. Valid: {VALID_STATUSES}")
    parser.add_argument("--last-contacted", action="store_true", help="Set Last Contacted to today")
    parser.add_argument("--note", help="Note to append to contact Notes field")
    parser.add_argument("--outreach", help="Mark outreach sent with this email subject")

    args = parser.parse_args()

    if args.outreach:
        # Shortcut for outreach workflow
        result = mark_outreach_sent(args.contact_id, args.outreach)
    else:
        result = update_contact(
            contact_id=args.contact_id,
            status=args.status,
            last_contacted=args.last_contacted,
            note=args.note
        )

    if result["success"]:
        print(f"✅ {result['message']}")
    else:
        print(f"❌ Error: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
