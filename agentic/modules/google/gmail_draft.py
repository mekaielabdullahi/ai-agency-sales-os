#!/usr/bin/env python3
"""
Gmail Draft Creator

Creates draft emails in Gmail for the /new-lead workflow.
Requires OAuth credentials - falls back to copyable output if not configured.

Setup:
1. Create OAuth credentials at console.cloud.google.com
2. Download credentials.json to agentic/modules/google/credentials.json
3. Run once to authorize (opens browser)
4. Token saved to agentic/modules/google/token.json

Usage:
    python3 gmail_draft.py --to "email@example.com" --subject "Subject" --body "Email body"
    python3 gmail_draft.py --from-file draft.json
"""

import sys
import os
import json
import base64
import argparse
from email.mime.text import MIMEText
from typing import Optional, Dict

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(SCRIPT_DIR, "credentials.json")
TOKEN_FILE = os.path.join(SCRIPT_DIR, "token.json")

# Try to import Google libraries
GOOGLE_AVAILABLE = False
try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    GOOGLE_AVAILABLE = True
except ImportError:
    pass

SCOPES = ['https://www.googleapis.com/auth/gmail.compose']


def get_gmail_service():
    """Get authenticated Gmail service."""
    if not GOOGLE_AVAILABLE:
        return None

    if not os.path.exists(CREDENTIALS_FILE):
        return None

    creds = None

    # Load existing token
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # Refresh or get new token
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save token
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


def create_draft(to: str, subject: str, body: str, html: bool = False) -> Dict:
    """
    Create a draft email in Gmail.

    Returns:
        Dict with 'success', 'draft_id', 'message', and 'fallback_text'
    """
    # Build email message
    if html:
        message = MIMEText(body, 'html')
    else:
        message = MIMEText(body)

    message['to'] = to
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Try Gmail API
    service = get_gmail_service()

    if service:
        try:
            draft = service.users().drafts().create(
                userId='me',
                body={'message': {'raw': raw}}
            ).execute()

            return {
                'success': True,
                'draft_id': draft['id'],
                'message': f"Draft created successfully! Draft ID: {draft['id']}",
                'gmail_link': f"https://mail.google.com/mail/u/0/#drafts"
            }
        except Exception as e:
            return {
                'success': False,
                'message': f"Gmail API error: {e}",
                'fallback_text': format_fallback(to, subject, body)
            }
    else:
        # No Gmail API available - return copyable format
        return {
            'success': False,
            'message': "Gmail API not configured. Copy the email below:",
            'fallback_text': format_fallback(to, subject, body)
        }


def format_fallback(to: str, subject: str, body: str) -> str:
    """Format email for manual copy/paste."""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📧 EMAIL DRAFT (Copy to Gmail)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

To: {to}
Subject: {subject}

{body}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def main():
    parser = argparse.ArgumentParser(description="Create Gmail draft")
    parser.add_argument("--to", help="Recipient email")
    parser.add_argument("--subject", help="Email subject")
    parser.add_argument("--body", help="Email body")
    parser.add_argument("--html", action="store_true", help="Body is HTML")
    parser.add_argument("--from-file", help="Load draft from JSON file")
    parser.add_argument("--check", action="store_true", help="Check if Gmail API is configured")

    args = parser.parse_args()

    if args.check:
        if GOOGLE_AVAILABLE and os.path.exists(CREDENTIALS_FILE):
            print("✅ Gmail API configured")
            if os.path.exists(TOKEN_FILE):
                print("✅ Already authorized")
            else:
                print("⚠️  Need to authorize (run with --to/--subject/--body)")
        else:
            print("❌ Gmail API not configured")
            print(f"   Place credentials.json in: {SCRIPT_DIR}")
            if not GOOGLE_AVAILABLE:
                print("   Install: pip install google-auth-oauthlib google-api-python-client")
        return

    if args.from_file:
        with open(args.from_file) as f:
            data = json.load(f)
        to = data.get('to')
        subject = data.get('subject')
        body = data.get('body')
        html = data.get('html', False)
    else:
        to = args.to
        subject = args.subject
        body = args.body
        html = args.html

    if not all([to, subject, body]):
        print("Error: --to, --subject, and --body are required")
        sys.exit(1)

    result = create_draft(to, subject, body, html)

    if result['success']:
        print(result['message'])
        print(f"Open drafts: {result.get('gmail_link', '')}")
    else:
        print(result['message'])
        if 'fallback_text' in result:
            print(result['fallback_text'])


if __name__ == "__main__":
    main()
