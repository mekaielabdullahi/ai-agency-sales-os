#!/usr/bin/env python3
"""
Google Docs Proposal Creator

Creates proposal documents in Google Docs for the /new-lead workflow.
Falls back to markdown output if not configured.

Setup:
1. Create service account at console.cloud.google.com
2. Download service account key to agentic/modules/google/service_account.json
3. Share your proposals folder with the service account email
4. Set GOOGLE_DRIVE_FOLDER_ID in agentic/.env

Usage:
    python3 docs_proposal.py --company "Company Name" --contact "John Smith" --industry "Manufacturing"
    python3 docs_proposal.py --from-file proposal_data.json
"""

import sys
import os
import json
import argparse
from datetime import datetime
from typing import Optional, Dict

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(SCRIPT_DIR, "service_account.json")

# Load env
def load_env():
    env_path = os.path.join(SCRIPT_DIR, '..', '..', '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

load_env()

DRIVE_FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID", "")

# Try to import Google libraries
GOOGLE_AVAILABLE = False
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_AVAILABLE = True
except ImportError:
    pass

SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file'
]


def get_google_services():
    """Get authenticated Docs and Drive services."""
    if not GOOGLE_AVAILABLE:
        return None, None

    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        return None, None

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    docs_service = build('docs', 'v1', credentials=credentials)
    drive_service = build('drive', 'v3', credentials=credentials)

    return docs_service, drive_service


def create_proposal(
    company: str,
    contact: str,
    industry: str = "",
    pain_points: str = "",
    proposed_solution: str = "",
    investment: str = "To be discussed based on scope",
    notes: str = ""
) -> Dict:
    """
    Create a proposal document.

    Returns:
        Dict with 'success', 'doc_id', 'doc_url', 'message', and 'fallback_markdown'
    """
    today = datetime.now().strftime("%B %d, %Y")

    # Build proposal content
    proposal_content = generate_proposal_content(
        company=company,
        contact=contact,
        industry=industry,
        pain_points=pain_points,
        proposed_solution=proposed_solution,
        investment=investment,
        notes=notes,
        date=today
    )

    # Try Google Docs API
    docs_service, drive_service = get_google_services()

    if docs_service and drive_service:
        try:
            # Create document
            doc = docs_service.documents().create(
                body={'title': f"AI Solutions Proposal - {company}"}
            ).execute()
            doc_id = doc['documentId']

            # Add content
            requests = build_docs_requests(proposal_content)
            docs_service.documents().batchUpdate(
                documentId=doc_id,
                body={'requests': requests}
            ).execute()

            # Move to folder if configured
            if DRIVE_FOLDER_ID:
                drive_service.files().update(
                    fileId=doc_id,
                    addParents=DRIVE_FOLDER_ID,
                    fields='id, parents'
                ).execute()

            doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"

            return {
                'success': True,
                'doc_id': doc_id,
                'doc_url': doc_url,
                'message': f"Proposal created in Google Docs!"
            }

        except Exception as e:
            return {
                'success': False,
                'message': f"Google Docs API error: {e}",
                'fallback_markdown': format_markdown_proposal(proposal_content)
            }
    else:
        return {
            'success': False,
            'message': "Google Docs API not configured. Markdown proposal below:",
            'fallback_markdown': format_markdown_proposal(proposal_content)
        }


def generate_proposal_content(
    company: str,
    contact: str,
    industry: str,
    pain_points: str,
    proposed_solution: str,
    investment: str,
    notes: str,
    date: str
) -> Dict:
    """Generate proposal content structure."""

    # Industry-specific value props
    industry_value = {
        "Manufacturing": "predictive maintenance, quality control automation, and process optimization",
        "System Integrator": "AI-powered tools to enhance your integration services and client delivery",
        "OEM": "intelligent product features and embedded AI capabilities",
        "Software": "AI integration, intelligent automation, and enhanced user experiences",
        "Consulting": "AI practice development and delivery capabilities for your clients"
    }.get(industry, "AI-powered automation and intelligent solutions")

    # Default pain points if not provided
    if not pain_points:
        pain_points = f"Based on our understanding of the {industry or 'your'} industry, organizations often face challenges with manual processes, data silos, and scaling operations efficiently."

    # Default solution if not provided
    if not proposed_solution:
        proposed_solution = f"""We propose a phased approach to implementing AI solutions:

**Phase 1: Discovery & Assessment**
- Deep dive into current workflows and pain points
- Identify highest-impact AI opportunities
- Create implementation roadmap

**Phase 2: Pilot Implementation**
- Deploy initial AI solution for quick wins
- Measure results and gather feedback
- Refine approach based on learnings

**Phase 3: Scale & Optimize**
- Expand successful pilots across organization
- Integrate with existing systems
- Continuous improvement and support"""

    return {
        'title': f"AI Solutions Proposal",
        'subtitle': f"Prepared for {company}",
        'date': date,
        'contact': contact,
        'executive_summary': f"AriseGroup.ai is pleased to present this proposal for {company}. We specialize in {industry_value}, helping organizations like yours leverage AI to drive efficiency, reduce costs, and accelerate growth.",
        'understanding': pain_points,
        'solution': proposed_solution,
        'investment': investment,
        'next_steps': """1. **Discovery Call** - 30-minute deep dive into your specific needs
2. **Custom Solution Design** - Tailored proposal based on discovery
3. **Pilot Project** - Low-risk proof of concept
4. **Full Implementation** - Scale successful pilots""",
        'about': """AriseGroup.ai helps businesses harness the power of artificial intelligence to transform their operations. We combine deep technical expertise with practical business understanding to deliver AI solutions that drive real results.

Our approach:
- Start with business outcomes, not technology
- Rapid prototyping and iteration
- Focus on ROI and measurable impact
- Ongoing partnership and support""",
        'notes': notes
    }


def build_docs_requests(content: Dict) -> list:
    """Build Google Docs API requests for content insertion."""
    requests = []
    index = 1

    def add_text(text: str, style: str = None):
        nonlocal index
        requests.append({
            'insertText': {
                'location': {'index': index},
                'text': text
            }
        })
        end_index = index + len(text)

        if style:
            style_request = {
                'updateParagraphStyle': {
                    'range': {'startIndex': index, 'endIndex': end_index},
                    'paragraphStyle': {},
                    'fields': 'namedStyleType'
                }
            }
            if style == 'title':
                style_request['updateParagraphStyle']['paragraphStyle']['namedStyleType'] = 'TITLE'
            elif style == 'heading1':
                style_request['updateParagraphStyle']['paragraphStyle']['namedStyleType'] = 'HEADING_1'
            elif style == 'heading2':
                style_request['updateParagraphStyle']['paragraphStyle']['namedStyleType'] = 'HEADING_2'
            requests.append(style_request)

        index = end_index

    # Build document
    add_text(f"{content['title']}\n", 'title')
    add_text(f"{content['subtitle']}\n", 'heading2')
    add_text(f"Date: {content['date']}\n\n")

    add_text("Executive Summary\n", 'heading1')
    add_text(f"{content['executive_summary']}\n\n")

    add_text("Understanding Your Needs\n", 'heading1')
    add_text(f"{content['understanding']}\n\n")

    add_text("Proposed Solution\n", 'heading1')
    add_text(f"{content['solution']}\n\n")

    add_text("Investment\n", 'heading1')
    add_text(f"{content['investment']}\n\n")

    add_text("Next Steps\n", 'heading1')
    add_text(f"{content['next_steps']}\n\n")

    add_text("About AriseGroup.ai\n", 'heading1')
    add_text(f"{content['about']}\n\n")

    if content.get('notes'):
        add_text("Additional Notes\n", 'heading1')
        add_text(f"{content['notes']}\n")

    return requests


def format_markdown_proposal(content: Dict) -> str:
    """Format proposal as markdown for copy/paste."""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 PROPOSAL (Copy to Google Docs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# {content['title']}
## {content['subtitle']}

**Date:** {content['date']}

---

## Executive Summary

{content['executive_summary']}

---

## Understanding Your Needs

{content['understanding']}

---

## Proposed Solution

{content['solution']}

---

## Investment

{content['investment']}

---

## Next Steps

{content['next_steps']}

---

## About AriseGroup.ai

{content['about']}

{f"---{chr(10)}{chr(10)}## Additional Notes{chr(10)}{chr(10)}{content['notes']}" if content.get('notes') else ""}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def main():
    parser = argparse.ArgumentParser(description="Create proposal in Google Docs")
    parser.add_argument("--company", help="Company name")
    parser.add_argument("--contact", help="Contact name")
    parser.add_argument("--industry", help="Industry", default="")
    parser.add_argument("--pain-points", help="Specific pain points", default="")
    parser.add_argument("--solution", help="Proposed solution", default="")
    parser.add_argument("--investment", help="Investment/pricing", default="To be discussed")
    parser.add_argument("--notes", help="Additional notes", default="")
    parser.add_argument("--from-file", help="Load from JSON file")
    parser.add_argument("--check", action="store_true", help="Check if API is configured")

    args = parser.parse_args()

    if args.check:
        if GOOGLE_AVAILABLE and os.path.exists(SERVICE_ACCOUNT_FILE):
            print("✅ Google Docs API configured")
            if DRIVE_FOLDER_ID:
                print(f"✅ Drive folder: {DRIVE_FOLDER_ID}")
            else:
                print("⚠️  No GOOGLE_DRIVE_FOLDER_ID set (docs created in root)")
        else:
            print("❌ Google Docs API not configured")
            print(f"   Place service_account.json in: {SCRIPT_DIR}")
            if not GOOGLE_AVAILABLE:
                print("   Install: pip install google-auth google-api-python-client")
        return

    if args.from_file:
        with open(args.from_file) as f:
            data = json.load(f)
        company = data.get('company')
        contact = data.get('contact')
        industry = data.get('industry', '')
        pain_points = data.get('pain_points', '')
        solution = data.get('solution', '')
        investment = data.get('investment', 'To be discussed')
        notes = data.get('notes', '')
    else:
        company = args.company
        contact = args.contact
        industry = args.industry
        pain_points = args.pain_points
        solution = args.solution
        investment = args.investment
        notes = args.notes

    if not company or not contact:
        print("Error: --company and --contact are required")
        sys.exit(1)

    result = create_proposal(
        company=company,
        contact=contact,
        industry=industry,
        pain_points=pain_points,
        proposed_solution=solution,
        investment=investment,
        notes=notes
    )

    if result['success']:
        print(result['message'])
        print(f"Open document: {result['doc_url']}")
    else:
        print(result['message'])
        if 'fallback_markdown' in result:
            print(result['fallback_markdown'])


if __name__ == "__main__":
    main()
