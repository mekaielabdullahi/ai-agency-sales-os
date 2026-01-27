#!/usr/bin/env python3
"""
Executive Dashboard Generator

Generates high-level business metrics for leadership.
"""

from datetime import datetime
from typing import Dict, Any

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collectors.notion_collector import NotionCollector
from collectors.file_collector import FileCollector


class ExecutiveDashboardGenerator:
    """Generates executive-level dashboard data."""

    def __init__(self):
        self.notion = NotionCollector()
        self.files = FileCollector()

    def generate(self) -> Dict[str, Any]:
        """Generate complete executive dashboard data."""
        data = {
            "type": "executive",
            "generated_at": datetime.now().isoformat(),
            "tasks": {},
            "pipeline": {},
            "projects": {},
            "reports": {},
            "summary": {},
            "alerts": []
        }

        # Collect from Notion
        try:
            data["tasks"] = self.notion.fetch_task_metrics()
        except Exception as e:
            data["tasks"] = {"error": str(e)}

        try:
            data["pipeline"] = self.notion.fetch_pipeline_metrics()
        except Exception as e:
            data["pipeline"] = {"error": str(e)}

        # Collect from files
        try:
            data["projects"] = self.files.fetch_project_metrics()
        except Exception as e:
            data["projects"] = {"error": str(e)}

        try:
            data["reports"] = self.files.fetch_report_metrics()
        except Exception as e:
            data["reports"] = {"error": str(e)}

        # Generate summary
        data["summary"] = self._generate_summary(data)

        # Generate alerts
        data["alerts"] = self._generate_alerts(data)

        return data

    def _generate_summary(self, data: Dict) -> Dict:
        """Generate executive summary metrics."""
        summary = {
            "health_score": 0,
            "tasks_health": "unknown",
            "pipeline_health": "unknown",
            "projects_health": "unknown"
        }

        scores = []

        # Tasks health
        tasks = data.get("tasks", {})
        if tasks and "error" not in tasks:
            overdue_pct = tasks.get("overdue", 0) / max(tasks.get("total_open", 1), 1)
            blocked_pct = tasks.get("blocked", 0) / max(tasks.get("total_open", 1), 1)

            if overdue_pct < 0.1 and blocked_pct < 0.1:
                summary["tasks_health"] = "green"
                scores.append(100)
            elif overdue_pct < 0.25 and blocked_pct < 0.2:
                summary["tasks_health"] = "yellow"
                scores.append(70)
            else:
                summary["tasks_health"] = "red"
                scores.append(40)

        # Pipeline health
        pipeline = data.get("pipeline", {})
        if pipeline and "error" not in pipeline:
            stale_count = len(pipeline.get("stale_leads", []))
            total_leads = pipeline.get("total_leads", 1) or 1
            stale_pct = stale_count / total_leads

            if stale_pct < 0.1:
                summary["pipeline_health"] = "green"
                scores.append(100)
            elif stale_pct < 0.3:
                summary["pipeline_health"] = "yellow"
                scores.append(70)
            else:
                summary["pipeline_health"] = "red"
                scores.append(40)

        # Projects health
        projects = data.get("projects", {})
        if projects and "error" not in projects:
            health = projects.get("health_summary", {})
            total = projects.get("total_projects", 1) or 1
            green_pct = health.get("green", 0) / total

            if green_pct >= 0.8:
                summary["projects_health"] = "green"
                scores.append(100)
            elif green_pct >= 0.5:
                summary["projects_health"] = "yellow"
                scores.append(70)
            else:
                summary["projects_health"] = "red"
                scores.append(40)

        # Overall health score
        if scores:
            summary["health_score"] = int(sum(scores) / len(scores))

        return summary

    def _generate_alerts(self, data: Dict) -> list:
        """Generate priority alerts for executive attention."""
        alerts = []

        # Critical alerts
        tasks = data.get("tasks", {})
        if tasks.get("overdue", 0) > 3:
            alerts.append({
                "level": "critical",
                "category": "tasks",
                "message": f"{tasks['overdue']} overdue tasks - immediate attention needed",
                "action": "Review overdue tasks and reassign or escalate"
            })

        # High priority alerts
        if tasks.get("blocked", 0) > 2:
            alerts.append({
                "level": "high",
                "category": "tasks",
                "message": f"{tasks['blocked']} blocked tasks",
                "action": "Unblock tasks to maintain velocity"
            })

        pipeline = data.get("pipeline", {})
        stale = pipeline.get("stale_leads", [])
        if len(stale) > 3:
            alerts.append({
                "level": "high",
                "category": "pipeline",
                "message": f"{len(stale)} leads need follow-up",
                "action": "Schedule outreach for stale leads"
            })

        # Medium priority alerts
        projects = data.get("projects", {})
        health = projects.get("health_summary", {})
        if health.get("red", 0) > 0:
            alerts.append({
                "level": "medium",
                "category": "projects",
                "message": f"{health['red']} projects at risk (inactive >7 days)",
                "action": "Check in on inactive projects"
            })

        reports = data.get("reports", {})
        if reports and not reports.get("report_current"):
            alerts.append({
                "level": "low",
                "category": "operations",
                "message": "Weekly report is stale",
                "action": "Generate new weekly report"
            })

        # Sort by priority
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        alerts.sort(key=lambda x: priority_order.get(x["level"], 99))

        return alerts
