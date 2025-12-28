#!/usr/bin/env python3
"""
Agentic workspace scaffolding tool.

Creates new modules and projects with proper directory structure.

Usage:
    ./run tools/scaffold.py module <name>
    ./run tools/scaffold.py project <name>
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


def get_repo_root() -> Path:
    """Get the repository root directory."""
    return Path(__file__).parent.parent


def validate_name(name: str) -> bool:
    """Validate module/project name (lowercase, letters/numbers/hyphens, starts with letter)."""
    return bool(re.match(r"^[a-z][a-z0-9-]*$", name))


def create_module(name: str) -> None:
    """Scaffold a new agentic module."""
    repo_root = get_repo_root()
    module_dir = repo_root / "modules" / name

    if module_dir.exists():
        print(f"Error: Module '{name}' already exists at {module_dir}")
        sys.exit(1)

    # Convert hyphens to underscores for Python
    python_name = name.replace("-", "_")

    print(f"Creating new module: {name}")

    # Create feature branch
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            branch_name = f"feat/{name}"
            print(f"Creating branch: {branch_name}")
            subprocess.run(
                ["git", "checkout", "-b", branch_name],
                cwd=repo_root,
                capture_output=True,
            )
    except Exception:
        pass  # Git not available or other issue, continue anyway

    # Create directory structure
    (module_dir / "tool").mkdir(parents=True)
    (module_dir / "runbook").mkdir(parents=True)
    (module_dir / "commands").mkdir(parents=True)

    # Create agentic-module.yaml
    manifest_content = f"""name: {name}
version: "0.1.0"
description: "TODO: Describe what this module does"

env_vars: []
  # - MY_API_KEY

requires: []
  # - slack: "for notifications"
"""
    (module_dir / "agentic-module.yaml").write_text(manifest_content)

    # Create tool template
    tool_content = f'''#!/usr/bin/env python3
"""
{name} tool

Usage:
    ./run modules/{name}/tool/{python_name}.py <action> [args]

Actions:
    example     Run an example action
"""
import argparse
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="{name} tool")
    parser.add_argument("action", help="Action to perform")
    args = parser.parse_args()

    # TODO: Implement actions
    print(f"Action: {{args.action}}")


if __name__ == "__main__":
    main()
'''
    tool_path = module_dir / "tool" / f"{python_name}.py"
    tool_path.write_text(tool_content)
    tool_path.chmod(0o755)

    # Create runbook template
    runbook_content = f"""# {name} Module

## Purpose

TODO: What does this module do?

## When to Use

- TODO: Trigger phrases or scenarios

## How to Run

```bash
./run modules/{name}/tool/{python_name}.py <action>
```

## Actions

| Action | Description |
|--------|-------------|
| example | TODO: describe action |

## Edge Cases

- TODO: Document edge cases
"""
    (module_dir / "runbook" / f"{python_name}.md").write_text(runbook_content)

    # Create command template
    command_content = f"""# /{name}

Slash command for the {name} module.

## Variables

- $1: action
- $2: arg1

## Subcommands

- `/{name} example` - Run example action

## Instructions

1. Parse the subcommand from $1
2. Run the appropriate tool action:
   ```bash
   ./run modules/{name}/tool/{python_name}.py $1 $2
   ```
3. Report results to user
"""
    (module_dir / "commands" / f"{name}.md").write_text(command_content)

    # Create README
    readme_content = f"""# {name}

TODO: Describe this module.

## Setup

Add any required environment variables to `.env`:

```bash
# MY_API_KEY=your-key-here
```

## Usage

```bash
./run modules/{name}/tool/{python_name}.py example
```

Or use the slash command: `/{name} example`
"""
    (module_dir / "README.md").write_text(readme_content)

    print(f"Module '{name}' created at {module_dir}")
    print()
    print("Next steps:")
    print(f"  1. Edit {module_dir}/agentic-module.yaml - add description, env vars")
    print(f"  2. Edit {module_dir}/tool/{python_name}.py - implement the tool")
    print(f"  3. Edit {module_dir}/runbook/{python_name}.md - document usage")
    print(f"  4. Test: ./run modules/{name}/tool/{python_name}.py example")
    print(f"  5. Run /agentic-sync to create command symlink")
    print(f"  6. Commit: git add modules/{name} && git commit -m 'feat({name}): initial module'")


def create_project(name: str) -> None:
    """Create a new project in ../projects/."""
    repo_root = get_repo_root()
    projects_dir = repo_root.parent / "projects"
    project_dir = projects_dir / name

    if project_dir.exists():
        print(f"Error: Project '{name}' already exists at {project_dir}")
        sys.exit(1)

    print(f"Creating new project: {name}")

    # Create projects directory if needed
    projects_dir.mkdir(parents=True, exist_ok=True)

    # Create project structure
    (project_dir / "notes").mkdir(parents=True)
    (project_dir / "templates").mkdir(parents=True)
    (project_dir / "deliverables").mkdir(parents=True)

    # Check for template
    template_path = repo_root / "extras" / "project-claude-template.md"
    if template_path.exists():
        claude_content = template_path.read_text().replace("[PROJECT NAME]", name)
        print("Created CLAUDE.md from template")
    else:
        # Fallback minimal CLAUDE.md
        claude_content = f"""# Project: {name}

## Overview

TODO: Describe this project.

## Tools

This project uses shared tools from `../agentic/`.

Run tools with:
```bash
../agentic/run ../agentic/modules/<module>/tool/<script>.py <args>
```

## Context

TODO: Add project-specific context, constraints, and preferences.
"""
        print("Created minimal CLAUDE.md")

    (project_dir / "CLAUDE.md").write_text(claude_content)

    # Create .gitignore
    gitignore_content = """.env
.DS_Store
*.pyc
__pycache__/
.tmp/
"""
    (project_dir / ".gitignore").write_text(gitignore_content)

    # Create README
    readme_content = f"""# {name}

Project created with [agentic](../agentic/).

## Structure

```
{name}/
├── CLAUDE.md       # AI agent instructions
├── notes/          # Working notes, meeting logs
├── templates/      # Document templates
└── deliverables/   # Final outputs
```

## Getting Started

Open this folder alongside `agentic/` in VS Code:
1. File > Add Folder to Workspace > select `../agentic`
2. Save as `{name}.code-workspace`
"""
    (project_dir / "README.md").write_text(readme_content)

    # Initialize git repo
    try:
        subprocess.run(["git", "init", "-q"], cwd=project_dir, check=True)
        subprocess.run(["git", "add", "-A"], cwd=project_dir, check=True)
        subprocess.run(
            ["git", "commit", "-q", "-m", "Initial project setup"],
            cwd=project_dir,
            check=True,
        )
        print("Initialized git repository")
    except Exception as e:
        print(f"Warning: Could not initialize git: {e}")

    print(f"Project '{name}' created at {project_dir}")
    print()
    print("Next steps:")
    print(f"  1. cd {project_dir}")
    print(f"  2. Edit CLAUDE.md - add project context, tools, preferences")
    print(f"  3. Open in VS Code with agentic:")
    print(f"     code {project_dir} && code -a {repo_root}")


def main():
    parser = argparse.ArgumentParser(description="Agentic workspace scaffolding")
    parser.add_argument(
        "type",
        choices=["module", "project"],
        help="Type of scaffold to create",
    )
    parser.add_argument("name", help="Name for the module or project")

    args = parser.parse_args()

    if not validate_name(args.name):
        print(
            "Error: Name must be lowercase, start with a letter, "
            "and contain only letters, numbers, and hyphens"
        )
        sys.exit(1)

    if args.type == "module":
        create_module(args.name)
    elif args.type == "project":
        create_project(args.name)


if __name__ == "__main__":
    main()
