#!/usr/bin/env python3
"""
Client Feedback API Integration Script

Execution tool for managing client feedback entries in Notion.
Supports: create, query, update, triage, and task linking.

Usage (CLI):
    ./run modules/client-feedback/tool/feedback_api.py create \
        --title "Bug description" \
        --type "Bug" \
        --severity "High" \
        --client "Client Name" \
        --description "Detailed description"

    ./run modules/client-feedback/tool/feedback_api.py query \
        --client "Client Name" \
        --status "Submitted"

    ./run modules/client-feedback/tool/feedback_api.py get <feedback_id>

    ./run modules/client-feedback/tool/feedback_api.py update <feedback_id> \
        --status "In Progress" \
        --priority "High" \
        --assigned-to "user@email.com"

    ./run modules/client-feedback/tool/feedback_api.py triage <feedback_id> \
        --priority "High" \
        --assigned-to "user@email.com" \
        --internal-notes "Investigating root cause"

    ./run modules/client-feedback/tool/feedback_api.py respond <feedback_id> \
        --response "We've identified the issue and are working on a fix."

    ./run modules/client-feedback/tool/feedback_api.py link <feedback_id> <task_id>

    ./run modules/client-feedback/tool/feedback_api.py stats [--client "Client Name"]

Usage (Module):
    from modules.client_feedback.tool.feedback_api import FeedbackClient
    client = FeedbackClient()
    feedback = client.create_feedback(title="Bug", type="Bug", severity="High")
"""

import sys
import os
import json
import argparse
from datetime import datetime
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
CLIENT_FEEDBACK_DB_ID = os.getenv("CLIENT_FEEDBACK_DB_ID", "")

# Valid options for select fields
VALID_STATUSES = ["Submitted", "Triaging", "Needs Info", "In Progress", "Responded", "Resolved", "Closed"]
VALID_TYPES = ["Urgent Issue", "Bug", "Change Request", "Enhancement", "Question"]
VALID_SEVERITIES = ["Critical", "High", "Medium", "Low"]
VALID_PRIORITIES = ["Urgent", "High", "Medium", "Low"]


# --- Custom Exceptions ---

class FeedbackError(Exception):
    """Base exception for Feedback API errors."""
    pass


class FeedbackConfigError(FeedbackError):
    """Configuration error (missing API key, database ID)."""
    pass


class FeedbackNotFoundError(FeedbackError):
    """Feedback entry not found."""
    pass


class FeedbackValidationError(FeedbackError):
    """Invalid input parameters."""
    pass


class FeedbackClient:
    """Client for managing client feedback in Notion."""

    def __init__(self, api_key: str = None, database_id: str = None):
        self.api_key = api_key or NOTION_API_KEY
        self.database_id = database_id or CLIENT_FEEDBACK_DB_ID

        if not self.api_key:
            raise FeedbackConfigError("NOTION_API_KEY not configured. Set it in .env file.")

        if not self.database_id:
            raise FeedbackConfigError("CLIENT_FEEDBACK_DB_ID not configured. Set it in .env file.")

        try:
            from notion_client import Client
            from notion_client.errors import APIResponseError
            self._APIResponseError = APIResponseError
        except ImportError:
            raise ImportError("notion-client not installed. Run: pip install notion-client")

        self.client = Client(auth=self.api_key)

    def _handle_error(self, error) -> None:
        """Convert notion-client errors to custom exceptions."""
        code = getattr(error, 'code', None)
        status = getattr(error, 'status', None)

        if code == 'object_not_found' or status == 404:
            raise FeedbackNotFoundError(str(error))
        elif code == 'validation_error' or status == 400:
            raise FeedbackValidationError(str(error))
        else:
            raise FeedbackError(str(error))

    def _request(self, method, *args, **kwargs) -> Any:
        """Make an API request with error handling."""
        try:
            return method(*args, **kwargs)
        except self._APIResponseError as e:
            self._handle_error(e)

    def _build_rich_text(self, text: str) -> List[Dict]:
        """Build rich text array from plain text."""
        if not text:
            return []
        return [{"type": "text", "text": {"content": text}}]

    def _extract_rich_text(self, rich_text: List[Dict]) -> str:
        """Extract plain text from rich text array."""
        return "".join(item.get("plain_text", "") for item in rich_text)

    def _extract_title(self, page: Dict) -> str:
        """Extract title from a page object."""
        props = page.get("properties", {})
        for prop_name in ["Title", "title", "Name", "name"]:
            if prop_name in props:
                title_prop = props[prop_name]
                if title_prop.get("type") == "title":
                    return self._extract_rich_text(title_prop.get("title", []))
        return "Untitled"

    def _extract_select(self, prop: Dict) -> Optional[str]:
        """Extract value from select property."""
        if prop and prop.get("type") == "select":
            select = prop.get("select")
            if select:
                return select.get("name")
        return None

    def _extract_formula(self, prop: Dict) -> Optional[str]:
        """Extract value from formula property."""
        if prop and prop.get("type") == "formula":
            formula = prop.get("formula", {})
            return formula.get("string") or formula.get("number")
        return None

    def _build_properties(
        self,
        title: str = None,
        request_type: str = None,
        severity: str = None,
        priority: str = None,
        status: str = None,
        description: str = None,
        steps_to_reproduce: str = None,
        response: str = None,
        internal_notes: str = None,
        resolution_summary: str = None
    ) -> Dict:
        """Build Notion properties object from arguments."""
        properties = {}

        if title is not None:
            properties["Title"] = {"title": self._build_rich_text(title)}

        if request_type is not None:
            if request_type not in VALID_TYPES:
                raise FeedbackValidationError(f"Invalid type '{request_type}'. Valid: {VALID_TYPES}")
            properties["Request Type"] = {"select": {"name": request_type}}

        if severity is not None:
            if severity not in VALID_SEVERITIES:
                raise FeedbackValidationError(f"Invalid severity '{severity}'. Valid: {VALID_SEVERITIES}")
            properties["Severity"] = {"select": {"name": severity}}

        if priority is not None:
            if priority not in VALID_PRIORITIES:
                raise FeedbackValidationError(f"Invalid priority '{priority}'. Valid: {VALID_PRIORITIES}")
            properties["Priority"] = {"select": {"name": priority}}

        if status is not None:
            if status not in VALID_STATUSES:
                raise FeedbackValidationError(f"Invalid status '{status}'. Valid: {VALID_STATUSES}")
            properties["Status"] = {"select": {"name": status}}

        if description is not None:
            properties["Description"] = {"rich_text": self._build_rich_text(description)}

        if steps_to_reproduce is not None:
            properties["Steps to Reproduce"] = {"rich_text": self._build_rich_text(steps_to_reproduce)}

        if response is not None:
            properties["Response"] = {"rich_text": self._build_rich_text(response)}

        if internal_notes is not None:
            properties["Internal Notes"] = {"rich_text": self._build_rich_text(internal_notes)}

        if resolution_summary is not None:
            properties["Resolution Summary"] = {"rich_text": self._build_rich_text(resolution_summary)}

        return properties

    # ==================== Create Operations ====================

    def create_feedback(
        self,
        title: str,
        request_type: str,
        severity: str,
        description: str = "",
        steps_to_reproduce: str = "",
        priority: str = None
    ) -> Dict:
        """
        Create a new feedback entry.

        Args:
            title: Brief description of the feedback
            request_type: Type of request (Bug, Enhancement, etc.)
            severity: Severity level (Critical, High, Medium, Low)
            description: Detailed description
            steps_to_reproduce: Steps to reproduce (for bugs)
            priority: Initial priority (usually set during triage)

        Returns:
            Created page object
        """
        properties = self._build_properties(
            title=title,
            request_type=request_type,
            severity=severity,
            status="Submitted",
            description=description,
            steps_to_reproduce=steps_to_reproduce,
            priority=priority
        )

        return self._request(
            self.client.pages.create,
            parent={"database_id": self.database_id},
            properties=properties
        )

    # ==================== Query Operations ====================

    def query_feedback(
        self,
        status: str = None,
        request_type: str = None,
        severity: str = None,
        priority: str = None,
        limit: int = 100
    ) -> List[Dict]:
        """
        Query feedback entries with optional filters.

        Args:
            status: Filter by status
            request_type: Filter by request type
            severity: Filter by severity
            priority: Filter by priority
            limit: Maximum results

        Returns:
            List of matching feedback entries
        """
        filters = []

        if status:
            if status not in VALID_STATUSES:
                raise FeedbackValidationError(f"Invalid status '{status}'. Valid: {VALID_STATUSES}")
            filters.append({
                "property": "Status",
                "select": {"equals": status}
            })

        if request_type:
            if request_type not in VALID_TYPES:
                raise FeedbackValidationError(f"Invalid type '{request_type}'. Valid: {VALID_TYPES}")
            filters.append({
                "property": "Request Type",
                "select": {"equals": request_type}
            })

        if severity:
            if severity not in VALID_SEVERITIES:
                raise FeedbackValidationError(f"Invalid severity '{severity}'. Valid: {VALID_SEVERITIES}")
            filters.append({
                "property": "Severity",
                "select": {"equals": severity}
            })

        if priority:
            if priority not in VALID_PRIORITIES:
                raise FeedbackValidationError(f"Invalid priority '{priority}'. Valid: {VALID_PRIORITIES}")
            filters.append({
                "property": "Priority",
                "select": {"equals": priority}
            })

        query_params = {
            "database_id": self.database_id,
            "page_size": min(limit, 100),
            "sorts": [{"property": "Created", "direction": "descending"}]
        }

        if filters:
            if len(filters) == 1:
                query_params["filter"] = filters[0]
            else:
                query_params["filter"] = {"and": filters}

        response = self._request(self.client.databases.query, **query_params)
        return response.get("results", [])

    def get_feedback(self, page_id: str) -> Dict:
        """Get a single feedback entry by ID."""
        return self._request(self.client.pages.retrieve, page_id=page_id)

    def get_open_feedback(self) -> List[Dict]:
        """Get all open (non-resolved/closed) feedback."""
        return self.query_feedback_advanced({
            "and": [
                {"property": "Status", "select": {"does_not_equal": "Resolved"}},
                {"property": "Status", "select": {"does_not_equal": "Closed"}}
            ]
        })

    def query_feedback_advanced(self, filter: Dict, limit: int = 100) -> List[Dict]:
        """Query with custom Notion filter object."""
        response = self._request(
            self.client.databases.query,
            database_id=self.database_id,
            filter=filter,
            page_size=min(limit, 100),
            sorts=[{"property": "Created", "direction": "descending"}]
        )
        return response.get("results", [])

    # ==================== Update Operations ====================

    def update_feedback(
        self,
        page_id: str,
        title: str = None,
        status: str = None,
        request_type: str = None,
        severity: str = None,
        priority: str = None,
        description: str = None,
        steps_to_reproduce: str = None,
        response: str = None,
        internal_notes: str = None,
        resolution_summary: str = None
    ) -> Dict:
        """
        Update a feedback entry.

        Args:
            page_id: ID of the feedback page to update
            (other args): Fields to update (None = no change)

        Returns:
            Updated page object
        """
        properties = self._build_properties(
            title=title,
            status=status,
            request_type=request_type,
            severity=severity,
            priority=priority,
            description=description,
            steps_to_reproduce=steps_to_reproduce,
            response=response,
            internal_notes=internal_notes,
            resolution_summary=resolution_summary
        )

        if not properties:
            raise FeedbackValidationError("No fields to update")

        return self._request(
            self.client.pages.update,
            page_id=page_id,
            properties=properties
        )

    def triage_feedback(
        self,
        page_id: str,
        priority: str,
        internal_notes: str = None
    ) -> Dict:
        """
        Triage a feedback entry - set priority and move to Triaging status.

        Args:
            page_id: ID of the feedback to triage
            priority: Assigned priority (Urgent, High, Medium, Low)
            internal_notes: Internal notes about triage decision

        Returns:
            Updated page object
        """
        return self.update_feedback(
            page_id=page_id,
            status="Triaging",
            priority=priority,
            internal_notes=internal_notes
        )

    def respond_to_feedback(
        self,
        page_id: str,
        response_text: str,
        new_status: str = "Responded"
    ) -> Dict:
        """
        Add response to feedback and update status.

        Args:
            page_id: ID of the feedback
            response_text: Official response to client
            new_status: Status to set (default: Responded)

        Returns:
            Updated page object
        """
        return self.update_feedback(
            page_id=page_id,
            status=new_status,
            response=response_text
        )

    def resolve_feedback(
        self,
        page_id: str,
        resolution_summary: str
    ) -> Dict:
        """
        Mark feedback as resolved with summary.

        Args:
            page_id: ID of the feedback
            resolution_summary: How the issue was resolved

        Returns:
            Updated page object
        """
        return self.update_feedback(
            page_id=page_id,
            status="Resolved",
            resolution_summary=resolution_summary
        )

    # ==================== Relation Operations ====================

    def link_to_task(self, feedback_id: str, task_id: str) -> Dict:
        """
        Link feedback to a task (bidirectional relation).

        Args:
            feedback_id: ID of the feedback page
            task_id: ID of the task page

        Returns:
            Updated feedback page
        """
        # Get current related tasks
        feedback = self.get_feedback(feedback_id)
        props = feedback.get("properties", {})
        related_tasks_prop = props.get("Related Tasks", {})

        current_relations = []
        if related_tasks_prop.get("type") == "relation":
            current_relations = [r["id"] for r in related_tasks_prop.get("relation", [])]

        # Add new task if not already linked
        if task_id not in current_relations:
            current_relations.append(task_id)

        return self._request(
            self.client.pages.update,
            page_id=feedback_id,
            properties={
                "Related Tasks": {
                    "relation": [{"id": tid} for tid in current_relations]
                }
            }
        )

    # ==================== Statistics Operations ====================

    def get_stats(self) -> Dict:
        """
        Get feedback statistics.

        Returns:
            Dict with counts by status, type, severity, priority
        """
        # Get all feedback (paginate if needed)
        all_feedback = []
        cursor = None

        while True:
            params = {
                "database_id": self.database_id,
                "page_size": 100
            }
            if cursor:
                params["start_cursor"] = cursor

            response = self._request(self.client.databases.query, **params)
            all_feedback.extend(response.get("results", []))

            if not response.get("has_more"):
                break
            cursor = response.get("next_cursor")

        # Calculate stats
        stats = {
            "total": len(all_feedback),
            "by_status": {},
            "by_type": {},
            "by_severity": {},
            "by_priority": {},
            "open": 0,
            "closed": 0
        }

        for fb in all_feedback:
            props = fb.get("properties", {})

            status = self._extract_select(props.get("Status"))
            if status:
                stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
                if status in ["Resolved", "Closed"]:
                    stats["closed"] += 1
                else:
                    stats["open"] += 1

            fb_type = self._extract_select(props.get("Request Type"))
            if fb_type:
                stats["by_type"][fb_type] = stats["by_type"].get(fb_type, 0) + 1

            severity = self._extract_select(props.get("Severity"))
            if severity:
                stats["by_severity"][severity] = stats["by_severity"].get(severity, 0) + 1

            priority = self._extract_select(props.get("Priority"))
            if priority:
                stats["by_priority"][priority] = stats["by_priority"].get(priority, 0) + 1

        return stats

    # ==================== Formatting Helpers ====================

    def format_feedback_summary(self, feedback: Dict) -> Dict:
        """Format a feedback page into a summary dict."""
        props = feedback.get("properties", {})

        return {
            "id": feedback.get("id"),
            "url": feedback.get("url"),
            "title": self._extract_title(feedback),
            "feedback_id": self._extract_formula(props.get("Feedback ID")),
            "status": self._extract_select(props.get("Status")),
            "type": self._extract_select(props.get("Request Type")),
            "severity": self._extract_select(props.get("Severity")),
            "priority": self._extract_select(props.get("Priority")),
            "description": self._extract_rich_text(props.get("Description", {}).get("rich_text", [])),
            "response": self._extract_rich_text(props.get("Response", {}).get("rich_text", [])),
            "created": feedback.get("created_time"),
            "last_edited": feedback.get("last_edited_time")
        }


# --- CLI Interface ---

def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        description="Client Feedback CLI - Manage client feedback in Notion",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="action", help="Action to perform")

    # === Create ===
    create_parser = subparsers.add_parser("create", help="Create new feedback entry")
    create_parser.add_argument("--title", required=True, help="Brief description")
    create_parser.add_argument("--type", required=True, choices=VALID_TYPES, help="Request type")
    create_parser.add_argument("--severity", required=True, choices=VALID_SEVERITIES, help="Severity level")
    create_parser.add_argument("--description", default="", help="Detailed description")
    create_parser.add_argument("--steps", default="", help="Steps to reproduce (for bugs)")
    create_parser.add_argument("--priority", choices=VALID_PRIORITIES, help="Initial priority")

    # === Get ===
    get_parser = subparsers.add_parser("get", help="Get feedback by ID")
    get_parser.add_argument("page_id", help="Feedback page ID")
    get_parser.add_argument("--raw", action="store_true", help="Output raw JSON")

    # === Query ===
    query_parser = subparsers.add_parser("query", help="Query feedback entries")
    query_parser.add_argument("--status", choices=VALID_STATUSES, help="Filter by status")
    query_parser.add_argument("--type", choices=VALID_TYPES, help="Filter by type")
    query_parser.add_argument("--severity", choices=VALID_SEVERITIES, help="Filter by severity")
    query_parser.add_argument("--priority", choices=VALID_PRIORITIES, help="Filter by priority")
    query_parser.add_argument("--limit", type=int, default=20, help="Max results")
    query_parser.add_argument("--open", action="store_true", help="Show only open feedback")
    query_parser.add_argument("--raw", action="store_true", help="Output raw JSON")

    # === Update ===
    update_parser = subparsers.add_parser("update", help="Update feedback entry")
    update_parser.add_argument("page_id", help="Feedback page ID")
    update_parser.add_argument("--title", help="New title")
    update_parser.add_argument("--status", choices=VALID_STATUSES, help="New status")
    update_parser.add_argument("--type", choices=VALID_TYPES, help="New type")
    update_parser.add_argument("--severity", choices=VALID_SEVERITIES, help="New severity")
    update_parser.add_argument("--priority", choices=VALID_PRIORITIES, help="New priority")
    update_parser.add_argument("--description", help="New description")
    update_parser.add_argument("--internal-notes", help="Internal notes")

    # === Triage ===
    triage_parser = subparsers.add_parser("triage", help="Triage feedback (set priority)")
    triage_parser.add_argument("page_id", help="Feedback page ID")
    triage_parser.add_argument("--priority", required=True, choices=VALID_PRIORITIES, help="Priority")
    triage_parser.add_argument("--notes", help="Internal triage notes")

    # === Respond ===
    respond_parser = subparsers.add_parser("respond", help="Respond to feedback")
    respond_parser.add_argument("page_id", help="Feedback page ID")
    respond_parser.add_argument("--response", required=True, help="Response text")
    respond_parser.add_argument("--status", choices=VALID_STATUSES, default="Responded", help="New status")

    # === Resolve ===
    resolve_parser = subparsers.add_parser("resolve", help="Resolve feedback")
    resolve_parser.add_argument("page_id", help="Feedback page ID")
    resolve_parser.add_argument("--summary", required=True, help="Resolution summary")

    # === Link ===
    link_parser = subparsers.add_parser("link", help="Link feedback to task")
    link_parser.add_argument("feedback_id", help="Feedback page ID")
    link_parser.add_argument("task_id", help="Task page ID")

    # === Stats ===
    subparsers.add_parser("stats", help="Get feedback statistics")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        sys.exit(1)

    try:
        client = FeedbackClient()
    except (FeedbackConfigError, ImportError) as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        # === Create ===
        if args.action == "create":
            feedback = client.create_feedback(
                title=args.title,
                request_type=args.type,
                severity=args.severity,
                description=args.description,
                steps_to_reproduce=args.steps,
                priority=args.priority
            )
            print(f"Created feedback: {feedback.get('id')}", file=sys.stderr)
            print(f"URL: {feedback.get('url')}", file=sys.stderr)
            print(json.dumps(client.format_feedback_summary(feedback), indent=2))

        # === Get ===
        elif args.action == "get":
            feedback = client.get_feedback(args.page_id)
            if args.raw:
                print(json.dumps(feedback, indent=2))
            else:
                summary = client.format_feedback_summary(feedback)
                print(f"Title: {summary['title']}", file=sys.stderr)
                print(f"Status: {summary['status']} | Type: {summary['type']} | Severity: {summary['severity']}", file=sys.stderr)
                print(json.dumps(summary, indent=2))

        # === Query ===
        elif args.action == "query":
            if args.open:
                results = client.get_open_feedback()
            else:
                results = client.query_feedback(
                    status=args.status,
                    request_type=args.type,
                    severity=args.severity,
                    priority=args.priority,
                    limit=args.limit
                )

            print(f"Found {len(results)} feedback entries", file=sys.stderr)

            if args.raw:
                print(json.dumps(results, indent=2))
            else:
                summaries = [client.format_feedback_summary(fb) for fb in results]
                for s in summaries:
                    print(f"  [{s['status']}] {s['title']} ({s['id'][:8]}...)", file=sys.stderr)
                print(json.dumps(summaries, indent=2))

        # === Update ===
        elif args.action == "update":
            feedback = client.update_feedback(
                page_id=args.page_id,
                title=args.title,
                status=args.status,
                request_type=args.type,
                severity=args.severity,
                priority=args.priority,
                description=args.description,
                internal_notes=args.internal_notes
            )
            print(f"Updated feedback: {args.page_id}", file=sys.stderr)
            print(json.dumps(client.format_feedback_summary(feedback), indent=2))

        # === Triage ===
        elif args.action == "triage":
            feedback = client.triage_feedback(
                page_id=args.page_id,
                priority=args.priority,
                internal_notes=args.notes
            )
            print(f"Triaged feedback: {args.page_id} -> Priority: {args.priority}", file=sys.stderr)
            print(json.dumps(client.format_feedback_summary(feedback), indent=2))

        # === Respond ===
        elif args.action == "respond":
            feedback = client.respond_to_feedback(
                page_id=args.page_id,
                response_text=args.response,
                new_status=args.status
            )
            print(f"Responded to feedback: {args.page_id}", file=sys.stderr)
            print(json.dumps(client.format_feedback_summary(feedback), indent=2))

        # === Resolve ===
        elif args.action == "resolve":
            feedback = client.resolve_feedback(
                page_id=args.page_id,
                resolution_summary=args.summary
            )
            print(f"Resolved feedback: {args.page_id}", file=sys.stderr)
            print(json.dumps(client.format_feedback_summary(feedback), indent=2))

        # === Link ===
        elif args.action == "link":
            feedback = client.link_to_task(args.feedback_id, args.task_id)
            print(f"Linked feedback {args.feedback_id} to task {args.task_id}", file=sys.stderr)

        # === Stats ===
        elif args.action == "stats":
            stats = client.get_stats()
            print(f"Total: {stats['total']} | Open: {stats['open']} | Closed: {stats['closed']}", file=sys.stderr)
            print(json.dumps(stats, indent=2))

        else:
            parser.print_help()
            sys.exit(1)

    except FeedbackError as e:
        print(f"Feedback API error: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
