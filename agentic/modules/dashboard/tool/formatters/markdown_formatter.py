#!/usr/bin/env python3
"""
Markdown Formatter for Dashboards

Formats dashboard data as terminal-friendly markdown.
"""

from datetime import datetime
from typing import Dict, List, Any


class MarkdownFormatter:
    """Formats dashboard data as markdown."""

    def format_executive(self, data: Dict) -> str:
        """Format executive dashboard."""
        lines = []
        lines.append("# Executive Dashboard")
        lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")

        # Tasks Summary
        tasks = data.get("tasks", {})
        if tasks and "error" not in tasks:
            lines.append("## Tasks Overview")
            lines.append(f"- **Open Tasks:** {tasks.get('total_open', 0)}")
            lines.append(f"- **Overdue:** {tasks.get('overdue', 0)}")
            lines.append(f"- **Blocked:** {tasks.get('blocked', 0)}")
            lines.append(f"- **Due Today:** {tasks.get('due_today', 0)}")
            lines.append(f"- **Due This Week:** {tasks.get('due_this_week', 0)}")
            lines.append("")

            # By Priority
            by_priority = tasks.get("by_priority", {})
            if by_priority:
                lines.append("### By Priority")
                for priority in ["Urgent", "High", "Medium", "Low"]:
                    if priority in by_priority:
                        icon = {"Urgent": "🔥", "High": "🟠", "Medium": "🟡", "Low": "🟢"}.get(priority, "")
                        lines.append(f"- {icon} {priority}: {by_priority[priority]}")
                lines.append("")

        # Pipeline Summary
        pipeline = data.get("pipeline", {})
        if pipeline and "error" not in pipeline:
            lines.append("## Pipeline Overview")
            lines.append(f"- **Total Leads:** {pipeline.get('total_leads', 0)}")
            lines.append(f"- **Total Value:** ${pipeline.get('total_value', 0):,.0f}")
            lines.append("")

            # By Stage
            stages = pipeline.get("stages", {})
            if stages:
                lines.append("### By Stage")
                lines.append("| Stage | Count | Value |")
                lines.append("|-------|-------|-------|")
                for stage, info in stages.items():
                    count = info.get("count", 0)
                    value = info.get("value", 0)
                    lines.append(f"| {stage} | {count} | ${value:,.0f} |")
                lines.append("")

            # Stale Leads
            stale = pipeline.get("stale_leads", [])
            if stale:
                lines.append(f"### Stale Leads ({len(stale)} need follow-up)")
                for lead in stale[:5]:
                    lines.append(f"- {lead['name']} ({lead['days_since']} days)")
                lines.append("")

        # Projects Summary
        projects = data.get("projects", {})
        if projects and "error" not in projects:
            lines.append("## Projects Overview")
            lines.append(f"- **Active Projects:** {projects.get('total_projects', 0)}")

            health = projects.get("health_summary", {})
            lines.append(f"- 🟢 Healthy: {health.get('green', 0)}")
            lines.append(f"- 🟡 Needs Attention: {health.get('yellow', 0)}")
            lines.append(f"- 🔴 At Risk: {health.get('red', 0)}")
            lines.append("")

        # Weekly Report Status
        reports = data.get("reports", {})
        if reports and "error" not in reports:
            latest = reports.get("latest_report", {})
            if latest:
                status = "✅ Current" if reports.get("report_current") else "⚠️ Stale"
                lines.append(f"## Weekly Report: {status}")
                lines.append(f"Latest: {latest.get('name', 'N/A')}")
                lines.append("")

        # Alerts
        alerts = self._generate_alerts(data)
        if alerts:
            lines.append("## Alerts")
            for alert in alerts:
                icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(alert["level"], "")
                lines.append(f"- {icon} {alert['message']}")
            lines.append("")

        return "\n".join(lines)

    def format_operations(self, data: Dict) -> str:
        """Format operations dashboard."""
        lines = []
        lines.append("# Operations Dashboard")
        lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")

        # Tasks Detail
        tasks = data.get("tasks", {})
        if tasks and "error" not in tasks:
            lines.append("## Task Status")
            lines.append(f"**Total Open:** {tasks.get('total_open', 0)}\n")

            # By Status breakdown
            by_status = tasks.get("by_status", {})
            if by_status:
                lines.append("### By Status")
                status_icons = {
                    "In progress": "🔵",
                    "Not started": "⬜",
                    "Blocked": "🟣",
                    "To Review": "🟡"
                }
                for status, count in by_status.items():
                    icon = status_icons.get(status, "")
                    lines.append(f"- {icon} {status}: {count}")
                lines.append("")

            # Overdue tasks
            if tasks.get("overdue", 0) > 0:
                lines.append(f"### ⚠️ Overdue Tasks: {tasks['overdue']}")
                task_list = tasks.get("tasks", [])
                overdue_tasks = [t for t in task_list if self._is_overdue(t.get("due_date"))]
                for t in overdue_tasks[:5]:
                    lines.append(f"- {t['name']} (due: {t.get('due_date', 'N/A')[:10]})")
                lines.append("")

            # Blocked tasks
            if tasks.get("blocked", 0) > 0:
                lines.append(f"### 🟣 Blocked Tasks: {tasks['blocked']}")
                task_list = tasks.get("tasks", [])
                blocked_tasks = [t for t in task_list if t.get("status") == "Blocked"]
                for t in blocked_tasks[:5]:
                    lines.append(f"- {t['name']}")
                lines.append("")

        # Project Health
        projects = data.get("projects", {})
        if projects and "error" not in projects:
            lines.append("## Project Health")
            lines.append(f"**Active Projects:** {projects.get('total_projects', 0)}\n")

            project_list = projects.get("projects", [])
            if project_list:
                lines.append("| Project | Health | Last Activity |")
                lines.append("|---------|--------|---------------|")
                for p in project_list:
                    health_icon = {"green": "🟢", "yellow": "🟡", "red": "🔴"}.get(p.get("health"), "⬜")
                    last_mod = p.get("last_modified", "N/A")
                    if last_mod and last_mod != "N/A":
                        last_mod = last_mod[:10]
                    lines.append(f"| {p['name']} | {health_icon} | {last_mod} |")
                lines.append("")

        # Action Items
        action_items = data.get("action_items", {})
        if action_items and "error" not in action_items:
            lines.append("## Action Items")
            lines.append(f"- **Open:** {action_items.get('open_items', 0)}")
            lines.append(f"- **Completed:** {action_items.get('completed_items', 0)}")

            open_items = [i for i in action_items.get("items", []) if i.get("status") == "open"]
            if open_items:
                lines.append("\n### Open Items")
                for item in open_items[:10]:
                    lines.append(f"- [ ] {item['text']}")
            lines.append("")

        # Weekly Report
        reports = data.get("reports", {})
        if reports and "error" not in reports:
            status = "✅" if reports.get("report_current") else "⚠️ Needs Update"
            lines.append(f"## Weekly Report Status: {status}")
            latest = reports.get("latest_report", {})
            if latest:
                lines.append(f"Latest: {latest.get('name', 'N/A')}")
            lines.append("")

        return "\n".join(lines)

    def _is_overdue(self, due_date: str) -> bool:
        """Check if a date is overdue."""
        if not due_date:
            return False
        try:
            due = datetime.fromisoformat(due_date.replace("Z", "+00:00"))
            return due.date() < datetime.now().date()
        except:
            return False

    def _generate_alerts(self, data: Dict) -> List[Dict]:
        """Generate alerts from dashboard data."""
        alerts = []

        # Task alerts
        tasks = data.get("tasks", {})
        if tasks.get("overdue", 0) > 0:
            alerts.append({
                "level": "high",
                "message": f"{tasks['overdue']} overdue tasks need attention"
            })
        if tasks.get("blocked", 0) > 0:
            alerts.append({
                "level": "medium",
                "message": f"{tasks['blocked']} blocked tasks"
            })

        # Project alerts
        projects = data.get("projects", {})
        health = projects.get("health_summary", {})
        if health.get("red", 0) > 0:
            alerts.append({
                "level": "high",
                "message": f"{health['red']} projects at risk (no activity >7 days)"
            })

        # Pipeline alerts
        pipeline = data.get("pipeline", {})
        stale = pipeline.get("stale_leads", [])
        if len(stale) > 0:
            alerts.append({
                "level": "medium",
                "message": f"{len(stale)} leads need follow-up (no contact >7 days)"
            })

        # Report alerts
        reports = data.get("reports", {})
        if reports and not reports.get("report_current"):
            alerts.append({
                "level": "low",
                "message": "Weekly report is stale (>7 days old)"
            })

        return alerts
