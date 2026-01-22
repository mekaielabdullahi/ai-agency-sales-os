#!/usr/bin/env python3
"""
Fetch Transcripts from Notion (Multiple Sources)

Retrieves meeting transcripts from multiple Notion databases:
1. Transcripts database (Fireflies sync - personal)
2. Meetings database (shared team meetings with transcript relations)

Can search by participant email, name, or contact relation.

Usage:
    python3 fetch_transcripts.py "Brian Powell"           # Search by name across all sources
    python3 fetch_transcripts.py --email "brian@test.com" # Search by email
    python3 fetch_transcripts.py --contact-id "xxx"       # Search by Notion contact ID
    python3 fetch_transcripts.py --list                   # List recent from all sources
    python3 fetch_transcripts.py --source transcripts     # Only personal Fireflies
    python3 fetch_transcripts.py --source meetings        # Only shared team meetings
"""

import os
import sys
import argparse
import requests
from datetime import datetime

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

# Database IDs
TRANSCRIPTS_DB_ID = "2dae7406-6c7d-8146-b22f-e5700666ca6c"  # Personal Fireflies
MEETINGS_DB_ID = "2d5e7406-6c7d-81c6-b336-ca6acaf0c48a"     # Shared team meetings

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}


def get_transcripts_by_participant(search_term: str, limit: int = 5, source: str = "all") -> list:
    """Search transcripts by participant name or email across sources."""

    all_results = []

    # Search Transcripts database (Fireflies)
    if source in ["all", "transcripts"]:
        response = requests.post(
            f"https://api.notion.com/v1/databases/{TRANSCRIPTS_DB_ID}/query",
            headers=HEADERS,
            json={
                "filter": {
                    "or": [
                        {"property": "Participants", "rich_text": {"contains": search_term}},
                        {"property": "Name", "title": {"contains": search_term}}
                    ]
                },
                "sorts": [{"property": "Date", "direction": "descending"}],
                "page_size": limit
            }
        )
        if response.status_code == 200:
            results = response.json().get("results", [])
            all_results.extend([parse_transcript(t, source="Fireflies") for t in results])

    # Search Meetings database (shared team)
    if source in ["all", "meetings"]:
        response = requests.post(
            f"https://api.notion.com/v1/databases/{MEETINGS_DB_ID}/query",
            headers=HEADERS,
            json={
                "filter": {
                    "property": "Name",
                    "title": {"contains": search_term}
                },
                "sorts": [{"property": "Date", "direction": "descending"}],
                "page_size": limit
            }
        )
        if response.status_code == 200:
            results = response.json().get("results", [])
            all_results.extend([parse_meeting(m) for m in results])

    # Sort by date and limit
    all_results.sort(key=lambda x: x.get("date", ""), reverse=True)
    return all_results[:limit]


def get_transcripts_by_contact_id(contact_id: str, limit: int = 5, source: str = "all") -> list:
    """Get transcripts linked to a specific contact across sources."""

    all_results = []

    # Search Transcripts database
    if source in ["all", "transcripts"]:
        response = requests.post(
            f"https://api.notion.com/v1/databases/{TRANSCRIPTS_DB_ID}/query",
            headers=HEADERS,
            json={
                "filter": {"property": "Contacts", "relation": {"contains": contact_id}},
                "sorts": [{"property": "Date", "direction": "descending"}],
                "page_size": limit
            }
        )
        if response.status_code == 200:
            results = response.json().get("results", [])
            all_results.extend([parse_transcript(t, source="Fireflies") for t in results])

    # Search Meetings database
    if source in ["all", "meetings"]:
        response = requests.post(
            f"https://api.notion.com/v1/databases/{MEETINGS_DB_ID}/query",
            headers=HEADERS,
            json={
                "filter": {"property": "Contacts", "relation": {"contains": contact_id}},
                "sorts": [{"property": "Date", "direction": "descending"}],
                "page_size": limit
            }
        )
        if response.status_code == 200:
            results = response.json().get("results", [])
            all_results.extend([parse_meeting(m) for m in results])

    all_results.sort(key=lambda x: x.get("date", ""), reverse=True)
    return all_results[:limit]


def get_recent_transcripts(limit: int = 10, source: str = "all") -> list:
    """Get most recent transcripts from all sources."""

    all_results = []

    # Get from Transcripts database
    if source in ["all", "transcripts"]:
        response = requests.post(
            f"https://api.notion.com/v1/databases/{TRANSCRIPTS_DB_ID}/query",
            headers=HEADERS,
            json={
                "sorts": [{"property": "Date", "direction": "descending"}],
                "page_size": limit
            }
        )
        if response.status_code == 200:
            results = response.json().get("results", [])
            all_results.extend([parse_transcript(t, source="Fireflies") for t in results])

    # Get from Meetings database
    if source in ["all", "meetings"]:
        response = requests.post(
            f"https://api.notion.com/v1/databases/{MEETINGS_DB_ID}/query",
            headers=HEADERS,
            json={
                "sorts": [{"property": "Date", "direction": "descending"}],
                "page_size": limit
            }
        )
        if response.status_code == 200:
            results = response.json().get("results", [])
            all_results.extend([parse_meeting(m) for m in results])

    all_results.sort(key=lambda x: x.get("date", ""), reverse=True)
    return all_results[:limit]


def get_transcript_content(page_id: str) -> str:
    """Get the full content of a transcript page."""

    response = requests.get(
        f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100",
        headers=HEADERS
    )

    if response.status_code != 200:
        return ""

    blocks = response.json().get("results", [])
    content = []

    for block in blocks:
        block_type = block.get("type")
        if block_type in ["paragraph", "heading_1", "heading_2", "heading_3",
                          "bulleted_list_item", "numbered_list_item", "quote"]:
            text_content = block.get(block_type, {}).get("rich_text", [])
            if text_content:
                text = " ".join([t.get("plain_text", "") for t in text_content])
                content.append(text)

    return "\n".join(content)


def parse_meeting(item: dict) -> dict:
    """Parse a meeting from the Meetings database."""
    props = item.get("properties", {})

    # Title
    title_prop = props.get("Name", {}).get("title", [])
    title = title_prop[0].get("plain_text", "Untitled") if title_prop else "Untitled"

    # Date
    date_prop = props.get("Date", {}).get("date")
    date = date_prop.get("start", "") if date_prop else ""
    if date:
        try:
            dt = datetime.fromisoformat(date.replace("Z", "+00:00"))
            date = dt.strftime("%Y-%m-%d %H:%M")
        except:
            pass

    # Summary
    summary_prop = props.get("Summary", {}).get("rich_text", [])
    summary = summary_prop[0].get("plain_text", "") if summary_prop else ""

    # Action Items
    action_items_prop = props.get("Action Items", {}).get("rich_text", [])
    action_items = action_items_prop[0].get("plain_text", "") if action_items_prop else ""

    # External URL
    external_url = props.get("External URL", {}).get("url", "")

    # Contact relations
    contacts = props.get("Contacts", {}).get("relation", [])
    contact_ids = [c.get("id") for c in contacts]

    # Transcript relations
    transcripts = props.get("Transcripts", {}).get("relation", [])
    transcript_ids = [t.get("id") for t in transcripts]

    # Team Attendees
    attendees = props.get("Team Attendees", {}).get("people", [])
    team_attendees = [a.get("name", "") for a in attendees if a.get("name")]

    # Type
    type_prop = props.get("Type", {}).get("select")
    meeting_type = type_prop.get("name", "") if type_prop else ""

    return {
        "id": item.get("id"),
        "title": title,
        "date": date,
        "participants": ", ".join(team_attendees),
        "summary": summary,
        "action_items": action_items,
        "external_url": external_url,
        "contact_ids": contact_ids,
        "transcript_ids": transcript_ids,
        "source": "Team Meetings",
        "meeting_type": meeting_type,
        "notion_url": item.get("url", "")
    }


def parse_transcript(item: dict, source: str = "Fireflies") -> dict:
    """Parse a transcript from Notion API response."""
    props = item.get("properties", {})

    # Title
    title_prop = props.get("Name", {}).get("title", [])
    title = title_prop[0].get("plain_text", "Untitled") if title_prop else "Untitled"

    # Date
    date_prop = props.get("Date", {}).get("date")
    date = date_prop.get("start", "") if date_prop else ""
    if date:
        try:
            dt = datetime.fromisoformat(date.replace("Z", "+00:00"))
            date = dt.strftime("%Y-%m-%d %H:%M")
        except:
            pass

    # Participants
    participants_prop = props.get("Participants", {}).get("rich_text", [])
    participants = participants_prop[0].get("plain_text", "") if participants_prop else ""

    # Summary
    summary_prop = props.get("Summary", {}).get("rich_text", [])
    summary = summary_prop[0].get("plain_text", "") if summary_prop else ""

    # External URL (Fireflies link)
    external_url = props.get("External URL", {}).get("url", "")

    # Contact relations
    contacts = props.get("Contacts", {}).get("relation", [])
    contact_ids = [c.get("id") for c in contacts]

    # Source
    source_prop = props.get("Source", {}).get("select")
    source = source_prop.get("name", "") if source_prop else ""

    return {
        "id": item.get("id"),
        "title": title,
        "date": date,
        "participants": participants,
        "summary": summary,
        "action_items": "",  # Transcripts don't have this
        "external_url": external_url,
        "contact_ids": contact_ids,
        "transcript_ids": [],
        "source": source,
        "notion_url": item.get("url", "")
    }


def format_transcript_for_context(transcript: dict, include_full_content: bool = False) -> str:
    """Format a transcript for use as context in email drafting."""

    output = []
    source_icon = "🎙️" if transcript.get('source') == "Fireflies" else "📋"
    output.append(f"{source_icon} **{transcript['title']}**")
    output.append(f"   Source: {transcript.get('source', 'Unknown')} | Date: {transcript['date']}")

    if transcript['participants']:
        output.append(f"   Participants: {transcript['participants']}")

    if transcript.get('summary'):
        output.append(f"\n   **Summary:** {transcript['summary']}")

    if transcript.get('action_items'):
        output.append(f"\n   **Action Items:** {transcript['action_items']}")

    if include_full_content and transcript['id']:
        content = get_transcript_content(transcript['id'])
        if content:
            output.append(f"\n   **Full Transcript:**\n{content[:5000]}")

    if transcript.get('external_url'):
        output.append(f"\n   Link: {transcript['external_url']}")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Fetch transcripts from Notion")
    parser.add_argument("search", nargs="?", help="Name or email to search for")
    parser.add_argument("--email", help="Search by email address")
    parser.add_argument("--contact-id", help="Search by Notion contact ID")
    parser.add_argument("--list", action="store_true", help="List recent transcripts")
    parser.add_argument("--limit", type=int, default=5, help="Number of results")
    parser.add_argument("--source", choices=["all", "transcripts", "meetings"], default="all",
                        help="Source: all, transcripts (Fireflies), meetings (team)")
    parser.add_argument("--full", action="store_true", help="Include full transcript content")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if not NOTION_API_KEY:
        print("Error: NOTION_API_KEY not found in environment")
        sys.exit(1)

    transcripts = []

    source = args.source

    if args.list:
        transcripts = get_recent_transcripts(args.limit, source)
        print(f"## Recent Transcripts ({len(transcripts)}) - Source: {source}\n")
    elif args.contact_id:
        transcripts = get_transcripts_by_contact_id(args.contact_id, args.limit, source)
        print(f"## Transcripts for Contact - Source: {source}\n")
    elif args.email:
        transcripts = get_transcripts_by_participant(args.email, args.limit, source)
        print(f"## Transcripts matching: {args.email} - Source: {source}\n")
    elif args.search:
        transcripts = get_transcripts_by_participant(args.search, args.limit, source)
        print(f"## Transcripts matching: {args.search} - Source: {source}\n")
    else:
        parser.print_help()
        return

    if args.json:
        import json
        print(json.dumps(transcripts, indent=2))
        return

    if not transcripts:
        print("No transcripts found.")
        return

    for t in transcripts:
        print(format_transcript_for_context(t, include_full_content=args.full))
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
