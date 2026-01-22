#!/usr/bin/env python3
"""
Fetch Lead Information from Notion

Pulls contact and company details for a lead to power the /new-lead workflow.

Usage:
    python3 modules/notion/tool/fetch_lead.py "Contact Name"
    python3 modules/notion/tool/fetch_lead.py --list-leads
    python3 modules/notion/tool/fetch_lead.py --format json "Contact Name"
"""

import sys
import os
import json
import argparse
from typing import Dict, List, Any, Optional

try:
    import requests
except ImportError:
    print("Installing requests...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

# Load from .env file if exists
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

load_env()

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
CONTACTS_DATABASE_ID = "2d5e7406-6c7d-81d3-ae7c-c375989f3bb0"
COMPANIES_DATABASE_ID = "2d7e7406-6c7d-81bd-a74b-eeb28c4aadc9"
NOTION_VERSION = "2022-06-28"


def notion_request(method: str, endpoint: str, data: Dict = None) -> Dict:
    """Make a request to Notion API."""
    if not NOTION_API_KEY:
        raise ValueError("NOTION_API_KEY not configured. Set it in agentic/.env file.")

    url = f"https://api.notion.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }

    if method == "GET":
        response = requests.get(url, headers=headers)
    else:
        response = requests.post(url, headers=headers, json=data or {})

    if response.status_code != 200:
        error = response.json().get("message", response.text)
        raise Exception(f"Notion API error ({response.status_code}): {error}")

    return response.json()


def get_page(page_id: str) -> Dict:
    """Get a single page by ID."""
    return notion_request("GET", f"pages/{page_id}")


def search_contacts(name: str = None, lead_only: bool = False) -> List[Dict]:
    """Search contacts by name or list all leads."""

    filter_conditions = []

    if lead_only:
        filter_conditions.append({
            "property": "Type",
            "select": {"equals": "Lead"}
        })

    if name:
        filter_conditions.append({
            "property": "Client Name",
            "title": {"contains": name}
        })

    filter_obj = None
    if len(filter_conditions) == 1:
        filter_obj = filter_conditions[0]
    elif len(filter_conditions) > 1:
        filter_obj = {"and": filter_conditions}

    data = {"page_size": 100}
    if filter_obj:
        data["filter"] = filter_obj

    response = notion_request("POST", f"databases/{CONTACTS_DATABASE_ID}/query", data)
    return response.get("results", [])


def extract_contact_info(contact: Dict) -> Dict:
    """Extract relevant info from a contact."""
    props = contact.get("properties", {})

    # Client Name (title)
    name = ""
    if "Client Name" in props:
        title_prop = props["Client Name"].get("title", [])
        name = "".join(t.get("plain_text", "") for t in title_prop)

    # Email
    email = ""
    if "Email" in props:
        email = props["Email"].get("email", "") or ""

    # Phone
    phone = ""
    if "Phone" in props:
        phone = props["Phone"].get("phone_number", "") or ""

    # Role
    role = ""
    if "Role" in props:
        role_prop = props["Role"].get("rich_text", [])
        role = "".join(t.get("plain_text", "") for t in role_prop)

    # Notes
    notes = ""
    if "Notes" in props:
        notes_prop = props["Notes"].get("rich_text", [])
        notes = "".join(t.get("plain_text", "") for t in notes_prop)

    # Type
    contact_type = ""
    if "Type" in props:
        type_prop = props["Type"].get("select")
        if type_prop:
            contact_type = type_prop.get("name", "")

    # Industry
    industries = []
    if "Industry" in props:
        industry_prop = props["Industry"].get("multi_select", [])
        industries = [i.get("name", "") for i in industry_prop]

    # Last Contacted
    last_contacted = ""
    if "Last Contacted" in props:
        date_prop = props["Last Contacted"].get("date")
        if date_prop:
            last_contacted = date_prop.get("start", "")

    # Company relation (we'll resolve this separately)
    company_ids = []
    if "Company" in props:
        company_prop = props["Company"].get("relation", [])
        company_ids = [c.get("id") for c in company_prop if c.get("id")]

    return {
        "id": contact.get("id", ""),
        "url": contact.get("url", ""),
        "name": name,
        "email": email,
        "phone": phone,
        "role": role,
        "notes": notes,
        "type": contact_type,
        "industries": industries,
        "last_contacted": last_contacted,
        "company_ids": company_ids
    }


def extract_company_info(company: Dict) -> Dict:
    """Extract relevant info from a company."""
    props = company.get("properties", {})

    # Company Name (title)
    name = ""
    if "Company Name" in props:
        title_prop = props["Company Name"].get("title", [])
        name = "".join(t.get("plain_text", "") for t in title_prop)

    # Website
    website = ""
    if "Website" in props:
        website = props["Website"].get("url", "") or ""

    # Industry
    industry = ""
    if "Industry" in props:
        industry_prop = props["Industry"].get("select")
        if industry_prop:
            industry = industry_prop.get("name", "")

    # Type
    company_type = ""
    if "Type" in props:
        type_prop = props["Type"].get("select")
        if type_prop:
            company_type = type_prop.get("name", "")

    # Notes
    notes = ""
    if "Notes" in props:
        notes_prop = props["Notes"].get("rich_text", [])
        notes = "".join(t.get("plain_text", "") for t in notes_prop)

    return {
        "id": company.get("id", ""),
        "url": company.get("url", ""),
        "name": name,
        "website": website,
        "industry": industry,
        "type": company_type,
        "notes": notes
    }


def get_full_lead_info(contact_name: str) -> Optional[Dict]:
    """Get full lead information including company details."""

    contacts = search_contacts(name=contact_name)

    if not contacts:
        return None

    # Take the first match
    contact = contacts[0]
    contact_info = extract_contact_info(contact)

    # Resolve company info
    company_info = None
    if contact_info["company_ids"]:
        try:
            company_page = get_page(contact_info["company_ids"][0])
            company_info = extract_company_info(company_page)
        except Exception as e:
            print(f"Warning: Could not fetch company info: {e}", file=sys.stderr)

    return {
        "contact": contact_info,
        "company": company_info
    }


def format_markdown(lead_data: Dict) -> str:
    """Format lead info as markdown."""
    contact = lead_data.get("contact", {})
    company = lead_data.get("company")

    lines = []
    lines.append(f"# Lead: {contact.get('name', 'Unknown')}\n")

    # Contact Details
    lines.append("## Contact Information")
    lines.append(f"- **Name:** {contact.get('name', '-')}")
    lines.append(f"- **Email:** {contact.get('email', '-')}")
    lines.append(f"- **Phone:** {contact.get('phone', '-')}")
    lines.append(f"- **Role:** {contact.get('role', '-')}")
    lines.append(f"- **Type:** {contact.get('type', '-')}")
    if contact.get('industries'):
        lines.append(f"- **Industries:** {', '.join(contact['industries'])}")
    if contact.get('last_contacted'):
        lines.append(f"- **Last Contacted:** {contact['last_contacted']}")
    lines.append(f"- **Notion:** {contact.get('url', '-')}")
    lines.append("")

    # Company Details
    if company:
        lines.append("## Company Information")
        lines.append(f"- **Company:** {company.get('name', '-')}")
        lines.append(f"- **Website:** {company.get('website', '-')}")
        lines.append(f"- **Industry:** {company.get('industry', '-')}")
        lines.append(f"- **Type:** {company.get('type', '-')}")
        lines.append(f"- **Notion:** {company.get('url', '-')}")
        if company.get('notes'):
            lines.append(f"\n**Company Notes:**\n{company['notes']}")
        lines.append("")

    # Contact Notes
    if contact.get('notes'):
        lines.append("## Notes")
        lines.append(contact['notes'])
        lines.append("")

    return "\n".join(lines)


def list_leads() -> str:
    """List all contacts marked as Lead."""
    contacts = search_contacts(lead_only=True)

    if not contacts:
        return "No leads found in Notion."

    lines = [f"## Active Leads ({len(contacts)})\n"]
    lines.append("| Name | Email | Company | Last Contacted |")
    lines.append("|------|-------|---------|----------------|")

    for contact in contacts:
        info = extract_contact_info(contact)
        name = info.get('name', '-')
        email = info.get('email', '-')
        last = info.get('last_contacted', '-')

        # We'd need to resolve company names - for now just show count
        company = f"{len(info.get('company_ids', []))} linked" if info.get('company_ids') else "-"

        lines.append(f"| {name} | {email} | {company} | {last} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch lead info from Notion")
    parser.add_argument("name", nargs="?", help="Contact name to search for")
    parser.add_argument("--list-leads", action="store_true", help="List all leads")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown",
                        help="Output format (default: markdown)")
    args = parser.parse_args()

    try:
        if args.list_leads:
            print(list_leads())
        elif args.name:
            lead_data = get_full_lead_info(args.name)
            if lead_data:
                if args.format == "json":
                    print(json.dumps(lead_data, indent=2))
                else:
                    print(format_markdown(lead_data))
            else:
                print(f"No contact found matching '{args.name}'")
                sys.exit(1)
        else:
            parser.print_help()
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
