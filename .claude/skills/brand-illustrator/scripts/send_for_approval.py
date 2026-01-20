#!/usr/bin/env python3
"""
AriseGroup.ai Content Approval - Slack Integration

Sends the LinkedIn preview to a Slack channel for team approval.

Usage:
    python send_for_approval.py --project "2026-01-20-ai-audits-linkedin" --copy A --channel "#content-review"

Requires:
    SLACK_BOT_TOKEN in .env file
"""

import os
import sys
import argparse
from pathlib import Path

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False


# Configuration
SKILL_DIR = Path(__file__).parent.parent
PROJECTS_DIR = SKILL_DIR / "projects"
ENV_FILE = SKILL_DIR / ".env"


def load_slack_token():
    """Load Slack bot token from environment."""
    if DOTENV_AVAILABLE and ENV_FILE.exists():
        load_dotenv(ENV_FILE)

    return os.getenv("SLACK_BOT_TOKEN")


def parse_copy_text(copy_path: Path, copy_choice: str) -> str:
    """Extract the copy text for the message."""
    if not copy_path.exists():
        return ""

    with open(copy_path, "r", encoding="utf-8") as f:
        content = f.read()

    target = f"## COPY {copy_choice.upper()}"
    if target not in content:
        return ""

    start = content.find(target)
    next_copy = content.find("## COPY", start + 1)
    section = content[start:next_copy] if next_copy != -1 else content[start:]

    # Extract between --- markers
    lines = section.split('\n')
    copy_lines = []
    in_content = False

    for line in lines:
        if line.strip() == "---":
            in_content = not in_content
            continue
        if in_content:
            copy_lines.append(line)

    return '\n'.join(copy_lines).strip()


def send_to_slack(project_dir: Path, copy_choice: str, channel: str, token: str):
    """Send the preview to Slack for approval."""

    if not SLACK_AVAILABLE:
        print("ERROR: slack_sdk not installed. Run: pip install slack_sdk")
        sys.exit(1)

    client = WebClient(token=token)

    # Find the preview image
    preview_path = project_dir / f"linkedin-preview-{copy_choice.lower()}.png"
    if not preview_path.exists():
        print(f"ERROR: Preview not found: {preview_path}")
        print("Run create_preview.py first to generate the preview.")
        sys.exit(1)

    # Get the copy text
    copy_path = project_dir / "post-copy.md"
    copy_text = parse_copy_text(copy_path, copy_choice)

    # Build the message
    project_name = project_dir.name
    message_text = f"""
:mega: *New LinkedIn Post for Approval*

*Project:* `{project_name}`
*Copy Version:* {copy_choice.upper()}

Please review the attached preview and respond with:
:white_check_mark: Approved
:pencil2: Needs changes (with feedback)
:x: Reject

---
*Post Copy:*
```
{copy_text[:1500]}{'...' if len(copy_text) > 1500 else ''}
```
"""

    try:
        # Upload the image and post message
        response = client.files_upload_v2(
            channel=channel,
            file=str(preview_path),
            initial_comment=message_text,
            title=f"LinkedIn Preview - {project_name}",
        )

        print(f"Sent to Slack channel: {channel}")
        return True

    except SlackApiError as e:
        print(f"Slack API Error: {e.response['error']}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Send LinkedIn preview to Slack for team approval"
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Project folder name"
    )
    parser.add_argument(
        "--copy",
        required=True,
        choices=["A", "B", "C", "a", "b", "c"],
        help="Which copy variation to send"
    )
    parser.add_argument(
        "--channel",
        default="#content-review",
        help="Slack channel to post to (default: #content-review)"
    )

    args = parser.parse_args()

    # Load token
    token = load_slack_token()
    if not token:
        print("ERROR: SLACK_BOT_TOKEN not found.")
        print(f"Add it to {ENV_FILE}:")
        print("  SLACK_BOT_TOKEN=xoxb-your-token-here")
        sys.exit(1)

    # Find project
    project_dir = PROJECTS_DIR / args.project
    if not project_dir.exists():
        print(f"ERROR: Project not found: {project_dir}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print("AriseGroup.ai Content Approval")
    print(f"{'='*60}")
    print(f"Project: {args.project}")
    print(f"Copy: {args.copy.upper()}")
    print(f"Channel: {args.channel}")

    # Send to Slack
    if send_to_slack(project_dir, args.copy, args.channel, token):
        print(f"\n✓ Preview sent to {args.channel} for approval!")
        print(f"{'='*60}\n")
        return 0
    else:
        print("\nFailed to send to Slack.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
