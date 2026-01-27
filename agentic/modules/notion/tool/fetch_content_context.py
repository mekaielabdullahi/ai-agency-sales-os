#!/usr/bin/env python3
"""
Fetch Content Context from Notion

Aggregates relevant context for content creation:
- Active client projects
- Recent meeting transcripts
- Current tasks/priorities
- Notes and documents

Usage:
    ./run modules/notion/tool/fetch_content_context.py
    ./run modules/notion/tool/fetch_content_context.py --days 7
    ./run modules/notion/tool/fetch_content_context.py --pillar education
"""

import sys
import os
import json
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

# Add parent path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from dotenv import load_dotenv
load_dotenv()

from modules.notion.tool.notion_api import NotionClient, NotionError


class ContentContextFetcher:
    """Fetches and aggregates content context from Notion."""

    PILLARS = {
        "education": ["training", "workshop", "learning", "guide", "tutorial", "how-to"],
        "consulting": ["audit", "strategy", "assessment", "roadmap", "advisory"],
        "development": ["build", "implement", "deploy", "integration", "automation", "agent"]
    }

    def __init__(self):
        self.client = NotionClient()

    def fetch_all_context(self, days: int = 14, pillar: Optional[str] = None) -> Dict[str, Any]:
        """
        Fetch all relevant content context from Notion.

        Args:
            days: Number of days to look back
            pillar: Optional filter by business pillar (education/consulting/development)

        Returns:
            Dict with projects, transcripts, tasks, and notes
        """
        context = {
            "fetched_at": datetime.now().isoformat(),
            "lookback_days": days,
            "pillar_filter": pillar,
            "projects": [],
            "transcripts": [],
            "tasks": [],
            "notes": [],
            "content_opportunities": []
        }

        # Fetch each category
        print("Fetching active projects...", file=sys.stderr)
        context["projects"] = self._fetch_projects(days)

        print("Fetching recent transcripts...", file=sys.stderr)
        context["transcripts"] = self._fetch_transcripts(days)

        print("Fetching current tasks...", file=sys.stderr)
        context["tasks"] = self._fetch_tasks()

        print("Fetching relevant notes...", file=sys.stderr)
        context["notes"] = self._fetch_notes(days)

        # Generate content opportunities
        print("Identifying content opportunities...", file=sys.stderr)
        context["content_opportunities"] = self._identify_opportunities(context, pillar)

        return context

    def _fetch_projects(self, days: int) -> List[Dict]:
        """Fetch active client projects."""
        projects = []

        # Search for project-related pages
        search_terms = ["project", "client", "engagement", "phase"]

        for term in search_terms:
            try:
                results = self.client.search(term, filter_type="page", page_size=20)
                for page in results:
                    # Check if recently edited
                    last_edited = page.get("last_edited_time", "")
                    if self._is_within_days(last_edited, days):
                        title = self.client.get_page_title(page)
                        if title and title != "Untitled":
                            projects.append({
                                "id": page.get("id"),
                                "title": title,
                                "last_edited": last_edited,
                                "url": page.get("url", ""),
                                "properties": self._extract_key_properties(page)
                            })
            except NotionError as e:
                print(f"Warning: Error searching '{term}': {e}", file=sys.stderr)

        # Deduplicate by ID
        seen = set()
        unique_projects = []
        for p in projects:
            if p["id"] not in seen:
                seen.add(p["id"])
                unique_projects.append(p)

        return unique_projects

    def _fetch_transcripts(self, days: int) -> List[Dict]:
        """Fetch recent meeting transcripts."""
        transcripts = []

        # Search for transcripts/meetings
        search_terms = ["meeting", "call", "transcript", "sync", "discovery"]

        for term in search_terms:
            try:
                results = self.client.search(term, filter_type="page", page_size=15)
                for page in results:
                    last_edited = page.get("last_edited_time", "")
                    if self._is_within_days(last_edited, days):
                        title = self.client.get_page_title(page)
                        props = page.get("properties", {})

                        # Extract summary if available
                        summary = ""
                        for prop_name in ["Summary", "New Summary", "Notes", "Description"]:
                            if prop_name in props:
                                prop = props[prop_name]
                                if prop.get("type") == "rich_text":
                                    summary = self.client._extract_rich_text(prop.get("rich_text", []))
                                    break

                        if title:
                            transcripts.append({
                                "id": page.get("id"),
                                "title": title,
                                "date": last_edited,
                                "summary": summary[:500] if summary else "",
                                "participants": self._extract_participants(props)
                            })
            except NotionError as e:
                print(f"Warning: Error fetching transcripts for '{term}': {e}", file=sys.stderr)

        # Deduplicate and sort by date
        seen = set()
        unique = []
        for t in transcripts:
            if t["id"] not in seen:
                seen.add(t["id"])
                unique.append(t)

        unique.sort(key=lambda x: x["date"], reverse=True)
        return unique[:15]  # Return most recent 15

    def _fetch_tasks(self) -> List[Dict]:
        """Fetch current tasks and priorities."""
        tasks = []

        # Search for tasks
        search_terms = ["task", "todo", "action", "priority"]

        for term in search_terms:
            try:
                results = self.client.search(term, filter_type="page", page_size=20)
                for page in results:
                    props = page.get("properties", {})
                    title = self.client.get_page_title(page)

                    # Extract status
                    status = "Unknown"
                    for prop_name in ["Status", "State", "Progress"]:
                        if prop_name in props:
                            prop = props[prop_name]
                            if prop.get("type") == "select" and prop.get("select"):
                                status = prop["select"].get("name", "Unknown")
                                break
                            elif prop.get("type") == "status" and prop.get("status"):
                                status = prop["status"].get("name", "Unknown")
                                break

                    # Skip completed tasks
                    if status.lower() in ["done", "completed", "closed"]:
                        continue

                    if title and title != "Untitled":
                        tasks.append({
                            "id": page.get("id"),
                            "title": title,
                            "status": status,
                            "properties": self._extract_key_properties(page)
                        })
            except NotionError as e:
                print(f"Warning: Error fetching tasks for '{term}': {e}", file=sys.stderr)

        # Deduplicate
        seen = set()
        unique = []
        for t in tasks:
            if t["id"] not in seen:
                seen.add(t["id"])
                unique.append(t)

        return unique[:20]

    def _fetch_notes(self, days: int) -> List[Dict]:
        """Fetch relevant notes and documents."""
        notes = []

        # Search for strategic docs
        search_terms = ["strategy", "planning", "roadmap", "doc", "notes"]

        for term in search_terms:
            try:
                results = self.client.search(term, filter_type="page", page_size=10)
                for page in results:
                    last_edited = page.get("last_edited_time", "")
                    if self._is_within_days(last_edited, days):
                        title = self.client.get_page_title(page)
                        if title and title != "Untitled":
                            notes.append({
                                "id": page.get("id"),
                                "title": title,
                                "last_edited": last_edited,
                                "type": self._categorize_note(title)
                            })
            except NotionError as e:
                print(f"Warning: Error fetching notes for '{term}': {e}", file=sys.stderr)

        # Deduplicate
        seen = set()
        unique = []
        for n in notes:
            if n["id"] not in seen:
                seen.add(n["id"])
                unique.append(n)

        return unique

    def _identify_opportunities(self, context: Dict, pillar: Optional[str]) -> List[Dict]:
        """Identify content opportunities from the fetched context."""
        opportunities = []

        # From projects - case studies and build-in-public
        for project in context["projects"]:
            title = project["title"].lower()
            opp = {
                "source": "project",
                "title": project["title"],
                "content_type": "case_study" if "phase" in title or "client" in title else "build_update",
                "pillar": self._determine_pillar(title),
                "hook_angle": f"Working on {project['title']} - here's what we're learning",
                "key_points": []
            }

            if pillar and opp["pillar"] != pillar:
                continue

            opportunities.append(opp)

        # From transcripts - insights and learnings
        for transcript in context["transcripts"][:5]:  # Top 5 recent
            if transcript["summary"]:
                opp = {
                    "source": "transcript",
                    "title": transcript["title"],
                    "content_type": "insight",
                    "pillar": self._determine_pillar(transcript["title"].lower()),
                    "hook_angle": "Had a conversation that revealed...",
                    "key_points": [transcript["summary"][:200]]
                }

                if pillar and opp["pillar"] != pillar:
                    continue

                opportunities.append(opp)

        # From tasks - what we're actively working on
        active_work = [t for t in context["tasks"] if t["status"].lower() in ["in progress", "active", "doing"]]
        if active_work:
            opp = {
                "source": "tasks",
                "title": "Current Focus Areas",
                "content_type": "build_update",
                "pillar": "development",
                "hook_angle": "Here's what we're actively building this week",
                "key_points": [t["title"] for t in active_work[:5]]
            }
            opportunities.append(opp)

        return opportunities

    def _determine_pillar(self, text: str) -> str:
        """Determine which business pillar content belongs to."""
        text = text.lower()

        for pillar, keywords in self.PILLARS.items():
            for keyword in keywords:
                if keyword in text:
                    return pillar

        return "consulting"  # Default

    def _is_within_days(self, iso_date: str, days: int) -> bool:
        """Check if a date is within the specified number of days."""
        if not iso_date:
            return False
        try:
            dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
            cutoff = datetime.now(dt.tzinfo) - timedelta(days=days)
            return dt >= cutoff
        except:
            return False

    def _extract_key_properties(self, page: Dict) -> Dict:
        """Extract key properties from a page."""
        props = page.get("properties", {})
        extracted = {}

        for name, prop in props.items():
            prop_type = prop.get("type")

            if prop_type == "select" and prop.get("select"):
                extracted[name] = prop["select"].get("name")
            elif prop_type == "multi_select":
                extracted[name] = [s.get("name") for s in prop.get("multi_select", [])]
            elif prop_type == "rich_text":
                text = self.client._extract_rich_text(prop.get("rich_text", []))
                if text:
                    extracted[name] = text[:200]
            elif prop_type == "date" and prop.get("date"):
                extracted[name] = prop["date"].get("start")

        return extracted

    def _extract_participants(self, props: Dict) -> List[str]:
        """Extract participants from properties."""
        participants = []

        for prop_name in ["Participants", "Attendees", "People"]:
            if prop_name in props:
                prop = props[prop_name]
                if prop.get("type") == "multi_select":
                    participants = [s.get("name") for s in prop.get("multi_select", [])]
                elif prop.get("type") == "people":
                    participants = [p.get("name", "") for p in prop.get("people", [])]
                break

        return participants

    def _categorize_note(self, title: str) -> str:
        """Categorize a note by its title."""
        title_lower = title.lower()

        if any(w in title_lower for w in ["strategy", "roadmap", "plan"]):
            return "strategy"
        elif any(w in title_lower for w in ["meeting", "sync", "call"]):
            return "meeting"
        elif any(w in title_lower for w in ["doc", "guide", "how"]):
            return "documentation"
        else:
            return "general"

    def format_for_content(self, context: Dict) -> str:
        """Format context as markdown for content creation."""
        lines = []

        lines.append("# Notion Content Context")
        lines.append(f"\n*Fetched: {context['fetched_at'][:10]}*")
        lines.append(f"*Lookback: {context['lookback_days']} days*\n")

        # Active Projects
        if context["projects"]:
            lines.append("## Active Projects")
            for p in context["projects"][:5]:
                lines.append(f"- **{p['title']}** (last edited: {p['last_edited'][:10]})")
            lines.append("")

        # Recent Transcripts
        if context["transcripts"]:
            lines.append("## Recent Conversations")
            for t in context["transcripts"][:5]:
                lines.append(f"- **{t['title']}** ({t['date'][:10]})")
                if t["summary"]:
                    lines.append(f"  - {t['summary'][:150]}...")
            lines.append("")

        # Current Tasks
        active_tasks = [t for t in context["tasks"] if t["status"].lower() not in ["done", "completed"]]
        if active_tasks:
            lines.append("## Active Work")
            for t in active_tasks[:7]:
                lines.append(f"- {t['title']} [{t['status']}]")
            lines.append("")

        # Content Opportunities
        if context["content_opportunities"]:
            lines.append("## Content Opportunities")
            for opp in context["content_opportunities"][:5]:
                lines.append(f"### {opp['content_type'].replace('_', ' ').title()}: {opp['title']}")
                lines.append(f"- **Pillar**: {opp['pillar'].title()}")
                lines.append(f"- **Hook angle**: {opp['hook_angle']}")
                if opp["key_points"]:
                    lines.append("- **Key points**:")
                    for point in opp["key_points"]:
                        lines.append(f"  - {point}")
                lines.append("")

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch content context from Notion")
    parser.add_argument("--days", type=int, default=14, help="Days to look back (default: 14)")
    parser.add_argument("--pillar", choices=["education", "consulting", "development"],
                       help="Filter by business pillar")
    parser.add_argument("--json", action="store_true", help="Output as JSON instead of markdown")

    args = parser.parse_args()

    try:
        fetcher = ContentContextFetcher()
        context = fetcher.fetch_all_context(days=args.days, pillar=args.pillar)

        if args.json:
            print(json.dumps(context, indent=2))
        else:
            print(fetcher.format_for_content(context))

        # Summary stats
        print(f"\n---", file=sys.stderr)
        print(f"Found: {len(context['projects'])} projects, "
              f"{len(context['transcripts'])} transcripts, "
              f"{len(context['tasks'])} tasks, "
              f"{len(context['notes'])} notes", file=sys.stderr)
        print(f"Identified {len(context['content_opportunities'])} content opportunities", file=sys.stderr)

    except NotionError as e:
        print(f"Notion error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
