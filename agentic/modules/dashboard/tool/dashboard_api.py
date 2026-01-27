#!/usr/bin/env python3
"""
Dashboard API - Core Orchestrator

Generates dashboards by coordinating collectors, generators, and formatters.

Usage:
    ./run modules/dashboard/tool/dashboard_api.py
    ./run modules/dashboard/tool/dashboard_api.py --type ops
    ./run modules/dashboard/tool/dashboard_api.py --type executive --format slack
    ./run modules/dashboard/tool/dashboard_api.py --format json
"""

import sys
import os
import json
import argparse
from datetime import datetime
from typing import Dict, Any, Optional

# Add module path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generators.executive_dashboard import ExecutiveDashboardGenerator
from generators.operations_dashboard import OperationsDashboardGenerator
from formatters.markdown_formatter import MarkdownFormatter
from formatters.slack_formatter import SlackFormatter


class DashboardEngine:
    """Central engine for dashboard generation."""

    DASHBOARD_TYPES = {
        "executive": ExecutiveDashboardGenerator,
        "exec": ExecutiveDashboardGenerator,
        "operations": OperationsDashboardGenerator,
        "ops": OperationsDashboardGenerator,
    }

    FORMAT_TYPES = ["markdown", "slack", "json"]

    def __init__(self):
        self.markdown_formatter = MarkdownFormatter()
        self.slack_formatter = SlackFormatter()

    def generate(self, dashboard_type: str = "executive",
                 output_format: str = "markdown") -> str:
        """
        Generate a dashboard.

        Args:
            dashboard_type: Type of dashboard (executive, ops, etc.)
            output_format: Output format (markdown, slack, json)

        Returns:
            Formatted dashboard string
        """
        # Normalize type
        dashboard_type = dashboard_type.lower()
        if dashboard_type not in self.DASHBOARD_TYPES:
            raise ValueError(f"Unknown dashboard type: {dashboard_type}. "
                           f"Available: {list(self.DASHBOARD_TYPES.keys())}")

        # Generate data
        generator_class = self.DASHBOARD_TYPES[dashboard_type]
        generator = generator_class()
        data = generator.generate()

        # Format output
        return self.format_output(data, output_format)

    def format_output(self, data: Dict, output_format: str) -> str:
        """Format dashboard data for output."""
        output_format = output_format.lower()

        if output_format == "json":
            return json.dumps(data, indent=2, default=str)

        elif output_format == "slack":
            dashboard_type = data.get("type", "executive")
            if dashboard_type in ["executive", "exec"]:
                blocks = self.slack_formatter.format_executive(data)
            elif dashboard_type in ["operations", "ops"]:
                blocks = self.slack_formatter.format_operations(data)
            else:
                blocks = self.slack_formatter.format_executive(data)
            return json.dumps(blocks, indent=2)

        else:  # markdown (default)
            dashboard_type = data.get("type", "executive")
            if dashboard_type in ["executive", "exec"]:
                return self.markdown_formatter.format_executive(data)
            elif dashboard_type in ["operations", "ops"]:
                return self.markdown_formatter.format_operations(data)
            else:
                return self.markdown_formatter.format_executive(data)

    def list_types(self) -> list:
        """List available dashboard types."""
        return list(set(self.DASHBOARD_TYPES.keys()))

    def list_formats(self) -> list:
        """List available output formats."""
        return self.FORMAT_TYPES


def main():
    parser = argparse.ArgumentParser(
        description="Generate agency dashboards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ./run modules/dashboard/tool/dashboard_api.py                    # Executive dashboard, markdown
  ./run modules/dashboard/tool/dashboard_api.py --type ops         # Operations dashboard
  ./run modules/dashboard/tool/dashboard_api.py --format slack     # Executive as Slack blocks
  ./run modules/dashboard/tool/dashboard_api.py --format json      # Raw JSON data
        """
    )

    parser.add_argument("--type", "-t",
                        choices=["executive", "exec", "operations", "ops"],
                        default="executive",
                        help="Dashboard type (default: executive)")

    parser.add_argument("--format", "-f",
                        choices=["markdown", "slack", "json"],
                        default="markdown",
                        help="Output format (default: markdown)")

    parser.add_argument("--list-types", action="store_true",
                        help="List available dashboard types")

    args = parser.parse_args()

    engine = DashboardEngine()

    if args.list_types:
        print("Available dashboard types:")
        for t in engine.list_types():
            print(f"  - {t}")
        return

    try:
        output = engine.generate(
            dashboard_type=args.type,
            output_format=args.format
        )
        print(output)

    except Exception as e:
        print(f"Error generating dashboard: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
