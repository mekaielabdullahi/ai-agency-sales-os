#!/usr/bin/env python3
"""
Notion Data Collector for Dashboards

Collects task, contact, and pipeline data from Notion databases.

Usage:
    ./run modules/dashboard/tool/collectors/notion_collector.py tasks
    ./run modules/dashboard/tool/collectors/notion_collector.py pipeline
    ./run modules/dashboard/tool/collectors/notion_collector.py all
"""

import sys
import os
import json
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

try:
    import requests
except ImportError:
    print("Installing requests...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests


def load_env():
    """Load environment variables from .env file."""
    env_paths = [
        os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '.env'),
        os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env'),
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

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
NOTION_VERSION = "2022-06-28"

# Database IDs
TASKS_DATABASE_ID = "2d5e7406-6c7d-810e-a1be-c35b71fdf23b"
CONTACTS_DATABASE_ID = "2d5e7406-6c7d-81d3-ae7c-c375989f3bb0"
COMPANIES_DATABASE_ID = "2d7e7406-6c7d-81bd-a74b-eeb28c4aadc9"


class NotionCollector:
    """Collects dashboard data from Notion."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or NOTION_API_KEY
        if not self.api_key:
            raise ValueError("NOTION_API_KEY not configured")

    def _request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        """Make a request to Notion API."""
        url = f"https://api.notion.com/v1/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
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

    def _query_database(self, database_id: str, filter_obj: Dict = None,
                        sorts: List = None, page_size: int = 100) -> List[Dict]:
        """Query a database with pagination."""
        all_results = []
        start_cursor = None

        while True:
            data = {"page_size": page_size}
            if filter_obj:
                data["filter"] = filter_obj
            if sorts:
                data["sorts"] = sorts
            if start_cursor:
                data["start_cursor"] = start_cursor

            response = self._request("POST", f"databases/{database_id}/query", data)
            all_results.extend(response.get("results", []))

            if not response.get("has_more"):
                break
            start_cursor = response.get("next_cursor")

        return all_results

    # ==================== Task Metrics ====================

    def fetch_task_metrics(self) -> Dict[str, Any]:
        """Fetch task statistics for dashboard."""
        # Get all non-closed tasks
        filter_obj = {
            "and": [
                {"property": "Status", "status": {"does_not_equal": "Done"}},
                {"property": "Status", "status": {"does_not_equal": "Cancelled"}}
            ]
        }

        tasks = self._query_database(TASKS_DATABASE_ID, filter_obj)

        # Extract and categorize
        metrics = {
            "total_open": len(tasks),
            "by_status": {},
            "by_priority": {},
            "overdue": 0,
            "due_today": 0,
            "due_this_week": 0,
            "blocked": 0,
            "tasks": []
        }

        today = datetime.now().date()
        week_end = today + timedelta(days=7)

        for task in tasks:
            info = self._extract_task_info(task)
            metrics["tasks"].append(info)

            # Count by status
            status = info["status"] or "Unknown"
            metrics["by_status"][status] = metrics["by_status"].get(status, 0) + 1

            # Count by priority
            priority = info["priority"] or "None"
            metrics["by_priority"][priority] = metrics["by_priority"].get(priority, 0) + 1

            # Check due dates
            if info["due_date"]:
                try:
                    due = datetime.fromisoformat(info["due_date"].replace("Z", "+00:00")).date()
                    if due < today:
                        metrics["overdue"] += 1
                    elif due == today:
                        metrics["due_today"] += 1
                    elif due <= week_end:
                        metrics["due_this_week"] += 1
                except:
                    pass

            # Count blocked
            if status == "Blocked":
                metrics["blocked"] += 1

        return metrics

    def _extract_task_info(self, task: Dict) -> Dict:
        """Extract relevant info from a task object."""
        props = task.get("properties", {})

        # Task name
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

        # Assigned To
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
            "assigned": assigned
        }

    # ==================== Pipeline Metrics ====================

    def fetch_pipeline_metrics(self) -> Dict[str, Any]:
        """Fetch sales pipeline data from Contacts database."""
        try:
            contacts = self._query_database(CONTACTS_DATABASE_ID)
        except Exception as e:
            # Database might not exist or have different structure
            return {
                "error": str(e),
                "stages": {},
                "total_value": 0,
                "total_leads": 0
            }

        metrics = {
            "stages": {},
            "total_value": 0,
            "total_leads": len(contacts),
            "stale_leads": [],
            "contacts": []
        }

        today = datetime.now().date()
        stale_threshold = today - timedelta(days=7)

        for contact in contacts:
            info = self._extract_contact_info(contact)
            metrics["contacts"].append(info)

            # Count by stage/status
            stage = info.get("status", "Unknown")
            if stage not in metrics["stages"]:
                metrics["stages"][stage] = {"count": 0, "value": 0}

            metrics["stages"][stage]["count"] += 1

            # Add value if available
            value = info.get("value", 0)
            if value:
                metrics["stages"][stage]["value"] += value
                metrics["total_value"] += value

            # Check for stale leads
            last_contacted = info.get("last_contacted")
            if last_contacted:
                try:
                    last_date = datetime.fromisoformat(last_contacted.replace("Z", "+00:00")).date()
                    if last_date < stale_threshold:
                        metrics["stale_leads"].append({
                            "name": info.get("name", "Unknown"),
                            "last_contacted": last_contacted,
                            "days_since": (today - last_date).days
                        })
                except:
                    pass

        return metrics

    def _extract_contact_info(self, contact: Dict) -> Dict:
        """Extract relevant info from a contact object."""
        props = contact.get("properties", {})

        # Try common property names for contact name
        name = ""
        for prop_name in ["Name", "Client Name", "Contact Name", "title"]:
            if prop_name in props:
                prop = props[prop_name]
                if prop.get("type") == "title":
                    title_prop = prop.get("title", [])
                    name = "".join(t.get("plain_text", "") for t in title_prop)
                    break

        # Status/Stage
        status = ""
        for prop_name in ["Status", "Stage", "Pipeline Stage"]:
            if prop_name in props:
                prop = props[prop_name]
                if prop.get("type") == "select" and prop.get("select"):
                    status = prop["select"].get("name", "")
                    break
                elif prop.get("type") == "status" and prop.get("status"):
                    status = prop["status"].get("name", "")
                    break

        # Value
        value = 0
        for prop_name in ["Value", "Deal Value", "Pipeline Value", "Amount"]:
            if prop_name in props:
                prop = props[prop_name]
                if prop.get("type") == "number":
                    value = prop.get("number") or 0
                    break

        # Last Contacted
        last_contacted = ""
        for prop_name in ["Last Contacted", "Last Contact", "Last Activity"]:
            if prop_name in props:
                prop = props[prop_name]
                if prop.get("type") == "date" and prop.get("date"):
                    last_contacted = prop["date"].get("start", "")
                    break

        # Email
        email = ""
        if "Email" in props:
            prop = props["Email"]
            if prop.get("type") == "email":
                email = prop.get("email", "")

        return {
            "id": contact.get("id", ""),
            "name": name,
            "email": email,
            "status": status,
            "value": value,
            "last_contacted": last_contacted
        }

    # ==================== Combined Metrics ====================

    def fetch_all_metrics(self) -> Dict[str, Any]:
        """Fetch all metrics for executive dashboard."""
        return {
            "tasks": self.fetch_task_metrics(),
            "pipeline": self.fetch_pipeline_metrics(),
            "fetched_at": datetime.now().isoformat()
        }


def main():
    parser = argparse.ArgumentParser(description="Collect Notion data for dashboards")
    parser.add_argument("type", choices=["tasks", "pipeline", "all"],
                        default="all", nargs="?",
                        help="Type of data to collect")
    parser.add_argument("--format", choices=["json", "summary"], default="json",
                        help="Output format")

    args = parser.parse_args()

    try:
        collector = NotionCollector()

        if args.type == "tasks":
            data = collector.fetch_task_metrics()
        elif args.type == "pipeline":
            data = collector.fetch_pipeline_metrics()
        else:
            data = collector.fetch_all_metrics()

        if args.format == "json":
            print(json.dumps(data, indent=2))
        else:
            # Summary format
            if "tasks" in data:
                tasks = data["tasks"]
                print(f"Tasks: {tasks['total_open']} open, {tasks['overdue']} overdue, {tasks['blocked']} blocked")
            if "pipeline" in data:
                pipeline = data["pipeline"]
                print(f"Pipeline: {pipeline['total_leads']} leads, ${pipeline['total_value']:,.0f} value")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
