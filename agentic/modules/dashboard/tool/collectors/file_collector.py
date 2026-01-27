#!/usr/bin/env python3
"""
File-based Data Collector for Dashboards

Collects project and report data from the local filesystem.

Usage:
    ./run modules/dashboard/tool/collectors/file_collector.py projects
    ./run modules/dashboard/tool/collectors/file_collector.py reports
    ./run modules/dashboard/tool/collectors/file_collector.py all
"""

import sys
import os
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional


class FileCollector:
    """Collects dashboard data from local files."""

    def __init__(self, base_path: str = None):
        # Navigate from module location to workspace root
        if base_path:
            self.base_path = Path(base_path)
        else:
            # Go up from modules/dashboard/tool/collectors to agentic root, then to parent
            module_dir = Path(__file__).parent.parent.parent.parent.parent
            self.base_path = module_dir

        # Common paths
        self.paths = {
            "active_projects": self.base_path / "claude-code-os-implementation" / "02-operations" / "project-management" / "active-projects",
            "weekly_reports": self.base_path / "claude-code-os-implementation" / "02-operations" / "weekly-reports",
            "content_projects": self.base_path / "agentic" / ".claude" / "skills" / "brand-illustrator" / "projects",
            "action_items": self.base_path / "claude-code-os-implementation" / "01-executive-office" / "internal-business-meetings" / "action-items",
        }

    # ==================== Project Metrics ====================

    def fetch_project_metrics(self) -> Dict[str, Any]:
        """Scan active projects folder for project health."""
        projects_path = self.paths["active_projects"]

        metrics = {
            "total_projects": 0,
            "projects": [],
            "health_summary": {"green": 0, "yellow": 0, "red": 0, "unknown": 0}
        }

        if not projects_path.exists():
            metrics["error"] = f"Projects path not found: {projects_path}"
            return metrics

        # Each subdirectory is a project
        for project_dir in projects_path.iterdir():
            if not project_dir.is_dir():
                continue
            if project_dir.name.startswith('.'):
                continue

            project_info = self._analyze_project(project_dir)
            metrics["projects"].append(project_info)
            metrics["total_projects"] += 1

            # Count health
            health = project_info.get("health", "unknown")
            metrics["health_summary"][health] = metrics["health_summary"].get(health, 0) + 1

        return metrics

    def _analyze_project(self, project_dir: Path) -> Dict:
        """Analyze a single project directory."""
        info = {
            "name": project_dir.name,
            "path": str(project_dir),
            "health": "unknown",
            "last_modified": None,
            "has_readme": False,
            "has_meetings": False,
            "meeting_count": 0,
            "recent_activity": False
        }

        # Check for README
        readme_path = project_dir / "README.md"
        if readme_path.exists():
            info["has_readme"] = True
            info["last_modified"] = datetime.fromtimestamp(readme_path.stat().st_mtime).isoformat()

        # Check for meetings folder
        meetings_path = project_dir / "meetings"
        if meetings_path.exists() and meetings_path.is_dir():
            info["has_meetings"] = True
            meeting_files = list(meetings_path.glob("*.md"))
            info["meeting_count"] = len(meeting_files)

            # Check for recent meetings (last 7 days)
            week_ago = datetime.now() - timedelta(days=7)
            for mf in meeting_files:
                if datetime.fromtimestamp(mf.stat().st_mtime) > week_ago:
                    info["recent_activity"] = True
                    break

        # Get last modified time of any file in project
        latest_mod = None
        for f in project_dir.rglob("*"):
            if f.is_file():
                mod_time = datetime.fromtimestamp(f.stat().st_mtime)
                if latest_mod is None or mod_time > latest_mod:
                    latest_mod = mod_time

        if latest_mod:
            info["last_modified"] = latest_mod.isoformat()
            days_since = (datetime.now() - latest_mod).days

            # Determine health based on activity
            if days_since <= 3:
                info["health"] = "green"
            elif days_since <= 7:
                info["health"] = "yellow"
            else:
                info["health"] = "red"

        return info

    # ==================== Weekly Report Metrics ====================

    def fetch_report_metrics(self) -> Dict[str, Any]:
        """Check weekly report status."""
        reports_path = self.paths["weekly_reports"]

        metrics = {
            "total_reports": 0,
            "latest_report": None,
            "reports": [],
            "report_current": False
        }

        if not reports_path.exists():
            metrics["error"] = f"Reports path not found: {reports_path}"
            return metrics

        # Find all weekly report files
        report_files = list(reports_path.glob("*.md"))
        metrics["total_reports"] = len(report_files)

        # Sort by modification time
        report_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

        for rf in report_files[:5]:  # Last 5 reports
            metrics["reports"].append({
                "name": rf.name,
                "date": datetime.fromtimestamp(rf.stat().st_mtime).isoformat()
            })

        if report_files:
            latest = report_files[0]
            latest_mod = datetime.fromtimestamp(latest.stat().st_mtime)
            metrics["latest_report"] = {
                "name": latest.name,
                "date": latest_mod.isoformat()
            }

            # Check if current (within last 7 days)
            days_since = (datetime.now() - latest_mod).days
            metrics["report_current"] = days_since <= 7

        return metrics

    # ==================== Content Queue Metrics ====================

    def fetch_content_metrics(self) -> Dict[str, Any]:
        """Check content project queue."""
        content_path = self.paths["content_projects"]

        metrics = {
            "total_projects": 0,
            "recent_projects": [],
            "projects_by_date": {}
        }

        if not content_path.exists():
            # Also check alternative location
            alt_path = self.base_path / ".claude" / "skills" / "brand-illustrator" / "projects"
            if alt_path.exists():
                content_path = alt_path
            else:
                metrics["error"] = f"Content path not found"
                return metrics

        # Each subdirectory is a content project
        for project_dir in content_path.iterdir():
            if not project_dir.is_dir():
                continue
            if project_dir.name.startswith('.'):
                continue

            metrics["total_projects"] += 1

            # Extract date from folder name if possible (YYYY-MM-DD format)
            name = project_dir.name
            date_key = name[:10] if len(name) >= 10 and name[4] == '-' else "unknown"
            metrics["projects_by_date"][date_key] = metrics["projects_by_date"].get(date_key, 0) + 1

            # Get recent projects
            mod_time = datetime.fromtimestamp(project_dir.stat().st_mtime)
            if (datetime.now() - mod_time).days <= 7:
                metrics["recent_projects"].append({
                    "name": name,
                    "date": mod_time.isoformat()
                })

        return metrics

    # ==================== Action Items Metrics ====================

    def fetch_action_item_metrics(self) -> Dict[str, Any]:
        """Check action items from meeting notes."""
        action_path = self.paths["action_items"]

        metrics = {
            "total_files": 0,
            "open_items": 0,
            "completed_items": 0,
            "items": []
        }

        if not action_path.exists():
            metrics["error"] = f"Action items path not found"
            return metrics

        # Scan action item files
        for f in action_path.glob("*.md"):
            metrics["total_files"] += 1

            # Quick parse for action items (lines starting with - [ ] or - [x])
            try:
                content = f.read_text()
                for line in content.split('\n'):
                    line = line.strip()
                    if line.startswith('- [ ]'):
                        metrics["open_items"] += 1
                        metrics["items"].append({
                            "text": line[5:].strip(),
                            "status": "open",
                            "source": f.name
                        })
                    elif line.startswith('- [x]'):
                        metrics["completed_items"] += 1
            except:
                pass

        return metrics

    # ==================== Combined Metrics ====================

    def fetch_all_metrics(self) -> Dict[str, Any]:
        """Fetch all file-based metrics."""
        return {
            "projects": self.fetch_project_metrics(),
            "reports": self.fetch_report_metrics(),
            "content": self.fetch_content_metrics(),
            "action_items": self.fetch_action_item_metrics(),
            "fetched_at": datetime.now().isoformat()
        }


def main():
    parser = argparse.ArgumentParser(description="Collect file-based data for dashboards")
    parser.add_argument("type", choices=["projects", "reports", "content", "actions", "all"],
                        default="all", nargs="?",
                        help="Type of data to collect")
    parser.add_argument("--format", choices=["json", "summary"], default="json",
                        help="Output format")

    args = parser.parse_args()

    try:
        collector = FileCollector()

        if args.type == "projects":
            data = collector.fetch_project_metrics()
        elif args.type == "reports":
            data = collector.fetch_report_metrics()
        elif args.type == "content":
            data = collector.fetch_content_metrics()
        elif args.type == "actions":
            data = collector.fetch_action_item_metrics()
        else:
            data = collector.fetch_all_metrics()

        if args.format == "json":
            print(json.dumps(data, indent=2))
        else:
            # Summary format
            if "projects" in data:
                p = data["projects"]
                print(f"Projects: {p['total_projects']} total, {p['health_summary'].get('green', 0)} healthy")
            if "reports" in data:
                r = data["reports"]
                status = "current" if r.get("report_current") else "stale"
                print(f"Weekly Report: {status}")
            if "action_items" in data:
                a = data["action_items"]
                print(f"Action Items: {a['open_items']} open, {a['completed_items']} completed")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
