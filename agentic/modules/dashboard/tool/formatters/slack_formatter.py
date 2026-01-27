#!/usr/bin/env python3
"""
Slack Block Kit Formatter for Dashboards

Formats dashboard data as Slack Block Kit JSON for posting.
"""

import json
from datetime import datetime
from typing import Dict, List, Any


class SlackFormatter:
    """Formats dashboard data as Slack Block Kit."""

    def format_executive(self, data: Dict) -> Dict:
        """Format executive dashboard as Slack blocks."""
        blocks = []

        # Header
        blocks.append({
            "type": "header",
            "text": {"type": "plain_text", "text": "Executive Dashboard"}
        })
        blocks.append({
            "type": "context",
            "elements": [{
                "type": "mrkdwn",
                "text": f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            }]
        })
        blocks.append({"type": "divider"})

        # Tasks Summary
        tasks = data.get("tasks", {})
        if tasks and "error" not in tasks:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*Tasks Overview*"},
                "fields": [
                    {"type": "mrkdwn", "text": f"*Open*\n{tasks.get('total_open', 0)}"},
                    {"type": "mrkdwn", "text": f"*Overdue*\n{tasks.get('overdue', 0)}"},
                    {"type": "mrkdwn", "text": f"*Blocked*\n{tasks.get('blocked', 0)}"},
                    {"type": "mrkdwn", "text": f"*Due This Week*\n{tasks.get('due_this_week', 0)}"}
                ]
            })

        # Pipeline Summary
        pipeline = data.get("pipeline", {})
        if pipeline and "error" not in pipeline:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*Pipeline Overview*"},
                "fields": [
                    {"type": "mrkdwn", "text": f"*Leads*\n{pipeline.get('total_leads', 0)}"},
                    {"type": "mrkdwn", "text": f"*Value*\n${pipeline.get('total_value', 0):,.0f}"}
                ]
            })

            # Stage breakdown
            stages = pipeline.get("stages", {})
            if stages:
                stage_text = "\n".join([
                    f"• {stage}: {info['count']} (${info['value']:,.0f})"
                    for stage, info in stages.items()
                ])
                blocks.append({
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"*By Stage*\n{stage_text}"}
                })

        blocks.append({"type": "divider"})

        # Projects Summary
        projects = data.get("projects", {})
        if projects and "error" not in projects:
            health = projects.get("health_summary", {})
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*Project Health*"},
                "fields": [
                    {"type": "mrkdwn", "text": f"*Active*\n{projects.get('total_projects', 0)}"},
                    {"type": "mrkdwn", "text": f"*Healthy*\n{health.get('green', 0)}"},
                    {"type": "mrkdwn", "text": f"*Needs Attention*\n{health.get('yellow', 0)}"},
                    {"type": "mrkdwn", "text": f"*At Risk*\n{health.get('red', 0)}"}
                ]
            })

        # Alerts
        alerts = self._generate_alerts(data)
        if alerts:
            blocks.append({"type": "divider"})
            alert_text = "\n".join([
                f"{'🔴' if a['level'] == 'high' else '🟡' if a['level'] == 'medium' else '🟢'} {a['message']}"
                for a in alerts
            ])
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Alerts*\n{alert_text}"}
            })

        return {"blocks": blocks}

    def format_operations(self, data: Dict) -> Dict:
        """Format operations dashboard as Slack blocks."""
        blocks = []

        # Header
        blocks.append({
            "type": "header",
            "text": {"type": "plain_text", "text": "Operations Dashboard"}
        })
        blocks.append({
            "type": "context",
            "elements": [{
                "type": "mrkdwn",
                "text": f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            }]
        })
        blocks.append({"type": "divider"})

        # Tasks by Status
        tasks = data.get("tasks", {})
        if tasks and "error" not in tasks:
            by_status = tasks.get("by_status", {})
            status_text = "\n".join([
                f"• {status}: {count}" for status, count in by_status.items()
            ])
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Task Status* ({tasks.get('total_open', 0)} open)\n{status_text}"}
            })

            # Overdue
            if tasks.get("overdue", 0) > 0:
                blocks.append({
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"⚠️ *{tasks['overdue']} Overdue Tasks*"}
                })

            # Blocked
            if tasks.get("blocked", 0) > 0:
                blocked_tasks = [t for t in tasks.get("tasks", []) if t.get("status") == "Blocked"]
                blocked_text = "\n".join([f"• {t['name']}" for t in blocked_tasks[:3]])
                blocks.append({
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"🟣 *Blocked Tasks*\n{blocked_text}"}
                })

        blocks.append({"type": "divider"})

        # Project Health
        projects = data.get("projects", {})
        if projects and "error" not in projects:
            project_list = projects.get("projects", [])
            project_text = "\n".join([
                f"{'🟢' if p.get('health') == 'green' else '🟡' if p.get('health') == 'yellow' else '🔴'} {p['name']}"
                for p in project_list[:5]
            ])
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Project Health*\n{project_text}"}
            })

        # Action Items Summary
        action_items = data.get("action_items", {})
        if action_items and "error" not in action_items:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*Action Items*"},
                "fields": [
                    {"type": "mrkdwn", "text": f"*Open*\n{action_items.get('open_items', 0)}"},
                    {"type": "mrkdwn", "text": f"*Completed*\n{action_items.get('completed_items', 0)}"}
                ]
            })

        return {"blocks": blocks}

    def _generate_alerts(self, data: Dict) -> List[Dict]:
        """Generate alerts from dashboard data."""
        alerts = []

        tasks = data.get("tasks", {})
        if tasks.get("overdue", 0) > 0:
            alerts.append({"level": "high", "message": f"{tasks['overdue']} overdue tasks"})
        if tasks.get("blocked", 0) > 0:
            alerts.append({"level": "medium", "message": f"{tasks['blocked']} blocked tasks"})

        projects = data.get("projects", {})
        health = projects.get("health_summary", {})
        if health.get("red", 0) > 0:
            alerts.append({"level": "high", "message": f"{health['red']} projects at risk"})

        pipeline = data.get("pipeline", {})
        stale = pipeline.get("stale_leads", [])
        if len(stale) > 0:
            alerts.append({"level": "medium", "message": f"{len(stale)} leads need follow-up"})

        return alerts

    def to_json(self, blocks: Dict) -> str:
        """Convert blocks to JSON string."""
        return json.dumps(blocks, indent=2)
