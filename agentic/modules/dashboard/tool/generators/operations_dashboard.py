#!/usr/bin/env python3
"""
Operations Dashboard Generator

Generates detailed operational metrics for delivery management.
"""

from datetime import datetime, timedelta
from typing import Dict, Any, List

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collectors.notion_collector import NotionCollector
from collectors.file_collector import FileCollector


class OperationsDashboardGenerator:
    """Generates operations-focused dashboard data."""

    def __init__(self):
        self.notion = NotionCollector()
        self.files = FileCollector()

    def generate(self) -> Dict[str, Any]:
        """Generate complete operations dashboard data."""
        data = {
            "type": "operations",
            "generated_at": datetime.now().isoformat(),
            "tasks": {},
            "projects": {},
            "reports": {},
            "action_items": {},
            "velocity": {},
            "blockers": [],
            "recommendations": []
        }

        # Collect from Notion
        try:
            data["tasks"] = self.notion.fetch_task_metrics()
        except Exception as e:
            data["tasks"] = {"error": str(e)}

        # Collect from files
        try:
            data["projects"] = self.files.fetch_project_metrics()
        except Exception as e:
            data["projects"] = {"error": str(e)}

        try:
            data["reports"] = self.files.fetch_report_metrics()
        except Exception as e:
            data["reports"] = {"error": str(e)}

        try:
            data["action_items"] = self.files.fetch_action_item_metrics()
        except Exception as e:
            data["action_items"] = {"error": str(e)}

        # Calculate velocity metrics
        data["velocity"] = self._calculate_velocity(data)

        # Extract blockers
        data["blockers"] = self._extract_blockers(data)

        # Generate recommendations
        data["recommendations"] = self._generate_recommendations(data)

        return data

    def _calculate_velocity(self, data: Dict) -> Dict:
        """Calculate work velocity metrics."""
        velocity = {
            "in_progress_count": 0,
            "completion_rate": 0,
            "blocked_rate": 0,
            "overdue_rate": 0
        }

        tasks = data.get("tasks", {})
        if tasks and "error" not in tasks:
            total = tasks.get("total_open", 1) or 1
            by_status = tasks.get("by_status", {})

            velocity["in_progress_count"] = by_status.get("In progress", 0)
            velocity["blocked_rate"] = round(tasks.get("blocked", 0) / total * 100, 1)
            velocity["overdue_rate"] = round(tasks.get("overdue", 0) / total * 100, 1)

        action_items = data.get("action_items", {})
        if action_items and "error" not in action_items:
            open_items = action_items.get("open_items", 0)
            completed = action_items.get("completed_items", 0)
            total_items = open_items + completed
            if total_items > 0:
                velocity["completion_rate"] = round(completed / total_items * 100, 1)

        return velocity

    def _extract_blockers(self, data: Dict) -> List[Dict]:
        """Extract and categorize blockers."""
        blockers = []

        # Task blockers
        tasks = data.get("tasks", {})
        if tasks and "error" not in tasks:
            task_list = tasks.get("tasks", [])
            for task in task_list:
                if task.get("status") == "Blocked":
                    blockers.append({
                        "type": "task",
                        "name": task.get("name", "Unknown"),
                        "assigned": task.get("assigned", []),
                        "source": "notion"
                    })

        # Project blockers (projects with no recent activity)
        projects = data.get("projects", {})
        if projects and "error" not in projects:
            for project in projects.get("projects", []):
                if project.get("health") == "red":
                    blockers.append({
                        "type": "project_stalled",
                        "name": project.get("name", "Unknown"),
                        "last_activity": project.get("last_modified"),
                        "source": "filesystem"
                    })

        return blockers

    def _generate_recommendations(self, data: Dict) -> List[Dict]:
        """Generate actionable recommendations."""
        recommendations = []

        tasks = data.get("tasks", {})
        velocity = data.get("velocity", {})

        # High blocked rate
        if velocity.get("blocked_rate", 0) > 15:
            recommendations.append({
                "priority": "high",
                "category": "blockers",
                "recommendation": "Schedule blocker review session",
                "reason": f"Blocked rate is {velocity['blocked_rate']}% - affecting velocity"
            })

        # High overdue rate
        if velocity.get("overdue_rate", 0) > 20:
            recommendations.append({
                "priority": "high",
                "category": "deadlines",
                "recommendation": "Review and renegotiate due dates",
                "reason": f"Overdue rate is {velocity['overdue_rate']}%"
            })

        # Low completion rate
        if velocity.get("completion_rate", 100) < 50:
            recommendations.append({
                "priority": "medium",
                "category": "completion",
                "recommendation": "Focus on closing open action items",
                "reason": f"Only {velocity['completion_rate']}% of action items completed"
            })

        # Stalled projects
        projects = data.get("projects", {})
        health = projects.get("health_summary", {})
        if health.get("red", 0) > 0:
            recommendations.append({
                "priority": "medium",
                "category": "projects",
                "recommendation": f"Check in on {health['red']} stalled projects",
                "reason": "Projects with no activity in >7 days"
            })

        # Weekly report
        reports = data.get("reports", {})
        if reports and not reports.get("report_current"):
            recommendations.append({
                "priority": "low",
                "category": "reporting",
                "recommendation": "Generate weekly report",
                "reason": "Last report is >7 days old"
            })

        # Too many in progress
        if velocity.get("in_progress_count", 0) > 10:
            recommendations.append({
                "priority": "medium",
                "category": "wip",
                "recommendation": "Reduce work in progress",
                "reason": f"{velocity['in_progress_count']} tasks in progress - consider WIP limits"
            })

        # Sort by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        recommendations.sort(key=lambda x: priority_order.get(x["priority"], 99))

        return recommendations
