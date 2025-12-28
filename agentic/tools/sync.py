#!/usr/bin/env python3
"""
Agentic workspace sync tool.

Regenerates command symlinks and rebuilds the workspace discovery index.

Usage:
    ./run tools/sync.py
"""
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


PROTECTED_PREFIX = "agentic-"
INDEX_FILE = "agentic-index.yaml"


def get_repo_root() -> Path:
    """Get the repository root directory."""
    return Path(__file__).parent.parent


def is_protected(filename: str) -> bool:
    """Check if a file is a protected core command."""
    return filename.startswith(PROTECTED_PREFIX)


def yaml_get(file_path: Path, key: str) -> str:
    """Read a simple key from a YAML file."""
    with open(file_path) as f:
        data = yaml.safe_load(f)
    return data.get(key, "") if data else ""


def yaml_get_array(file_path: Path, key: str) -> list:
    """Read an array value from a YAML file."""
    with open(file_path) as f:
        data = yaml.safe_load(f)
    return data.get(key, []) if data else []


def remove_stale_symlinks(commands_dir: Path) -> int:
    """Remove symlinks that point to non-existent targets."""
    removed = 0
    for link in commands_dir.glob("*.md"):
        if link.is_symlink() and not link.exists():
            link.unlink()
            removed += 1
    return removed


def sync_module_commands(modules_dir: Path, commands_dir: Path) -> tuple[int, int]:
    """
    Sync command symlinks from modules to .claude/commands/.

    Returns (modules_synced, commands_updated).
    """
    commands_dir.mkdir(parents=True, exist_ok=True)

    synced_modules = 0
    synced_commands = 0

    for module_dir in sorted(modules_dir.iterdir()):
        if not module_dir.is_dir():
            continue

        manifest = module_dir / "agentic-module.yaml"
        if not manifest.exists():
            continue

        synced_modules += 1
        module_commands_dir = module_dir / "commands"

        if not module_commands_dir.exists():
            continue

        for cmd_file in module_commands_dir.glob("*.md"):
            basename = cmd_file.name

            # Never overwrite protected core commands
            if is_protected(basename):
                continue

            symlink_path = commands_dir / basename
            # Relative path from .claude/commands/ to modules/<name>/commands/
            target = Path("../..") / module_dir.relative_to(module_dir.parent.parent) / "commands" / basename

            # Check if symlink exists and points to correct target
            if symlink_path.is_symlink():
                try:
                    current_target = os.readlink(symlink_path)
                    if current_target == str(target):
                        continue  # Already correct
                except OSError:
                    pass

            # Create or fix symlink
            if symlink_path.exists() or symlink_path.is_symlink():
                symlink_path.unlink()

            try:
                symlink_path.symlink_to(target)
                synced_commands += 1
            except OSError:
                # Fallback: copy file if symlinks not supported
                import shutil
                shutil.copy2(cmd_file, symlink_path)
                print(f"  Copied (symlinks not supported): {symlink_path.name}")
                synced_commands += 1

    return synced_modules, synced_commands


def rebuild_index(repo_root: Path, modules_dir: Path) -> None:
    """Regenerate the agentic-index.yaml discovery index."""
    workspace_name = repo_root.name
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    index = {
        "workspace": {"name": workspace_name},
        "modules": {},
        "tool_index": {},
        "runbook_index": {},
    }

    # Header comment will be added manually

    for module_dir in sorted(modules_dir.iterdir()):
        if not module_dir.is_dir():
            continue

        manifest = module_dir / "agentic-module.yaml"
        if not manifest.exists():
            continue

        with open(manifest) as f:
            manifest_data = yaml.safe_load(f) or {}

        module_name = manifest_data.get("name", module_dir.name)
        python_name = module_name.replace("-", "_")

        module_entry = {
            "description": manifest_data.get("description", ""),
            "version": manifest_data.get("version", ""),
            "paths": {
                "root": f"{module_dir}/",
            },
            "python_import": f"modules.{python_name}.tool",
        }

        # List tools
        tool_dir = module_dir / "tool"
        if tool_dir.exists():
            tools = []
            for tool_file in sorted(tool_dir.glob("*.py")):
                if tool_file.name != "__init__.py":
                    tools.append(str(tool_file))
                    index["tool_index"][tool_file.name] = module_name
            if tools:
                module_entry["paths"]["tools"] = tools

        # List runbooks
        runbook_dir = module_dir / "runbook"
        if runbook_dir.exists():
            runbooks = []
            for runbook_file in sorted(runbook_dir.glob("*.md")):
                runbooks.append(str(runbook_file))
                index["runbook_index"][runbook_file.name] = module_name
            if runbooks:
                module_entry["paths"]["runbooks"] = runbooks

        # List commands
        commands_dir = module_dir / "commands"
        if commands_dir.exists():
            commands = []
            for cmd_file in sorted(commands_dir.glob("*.md")):
                commands.append(str(cmd_file))
            if commands:
                module_entry["paths"]["commands"] = commands

        # Env vars
        env_vars = manifest_data.get("env_vars", [])
        if env_vars:
            module_entry["env_vars"] = env_vars

        index["modules"][module_name] = module_entry

    # Write index file with header comment
    index_path = repo_root / INDEX_FILE
    with open(index_path, "w") as f:
        f.write(f"# Agentic Workspace Discovery Index\n")
        f.write(f"# Generated by: /agentic-sync\n")
        f.write(f"# Generated at: {timestamp}\n")
        f.write(f"# DO NOT EDIT MANUALLY - regenerate with '/agentic-sync'\n\n")

        # Write workspace section
        f.write("workspace:\n")
        f.write(f"  name: {workspace_name}\n\n")

        # Write modules section
        f.write("modules:\n")
        if index["modules"]:
            for mod_name, mod_data in index["modules"].items():
                f.write(f"  {mod_name}:\n")
                f.write(f"    description: \"{mod_data.get('description', '')}\"\n")
                f.write(f"    version: \"{mod_data.get('version', '')}\"\n")
                f.write(f"    paths:\n")
                f.write(f"      root: {mod_data['paths']['root']}\n")

                if "tools" in mod_data["paths"]:
                    f.write(f"      tools:\n")
                    for tool in mod_data["paths"]["tools"]:
                        f.write(f"        - {tool}\n")

                if "runbooks" in mod_data["paths"]:
                    f.write(f"      runbooks:\n")
                    for rb in mod_data["paths"]["runbooks"]:
                        f.write(f"        - {rb}\n")

                if "commands" in mod_data["paths"]:
                    f.write(f"      commands:\n")
                    for cmd in mod_data["paths"]["commands"]:
                        f.write(f"        - {cmd}\n")

                f.write(f"    python_import: \"{mod_data['python_import']}\"\n")

                if "env_vars" in mod_data:
                    f.write(f"    env_vars:\n")
                    for var in mod_data["env_vars"]:
                        f.write(f"      - {var}\n")

                f.write("\n")
        else:
            f.write("  # No modules found\n\n")

        # Write tool index
        f.write("# Quick lookup: tool filename -> module name\n")
        f.write("tool_index:\n")
        if index["tool_index"]:
            for tool_name, mod_name in sorted(index["tool_index"].items()):
                f.write(f"  {tool_name}: {mod_name}\n")
        else:
            f.write("  # No tools\n")
        f.write("\n")

        # Write runbook index
        f.write("# Quick lookup: runbook filename -> module name\n")
        f.write("runbook_index:\n")
        if index["runbook_index"]:
            for rb_name, mod_name in sorted(index["runbook_index"].items()):
                f.write(f"  {rb_name}: {mod_name}\n")
        else:
            f.write("  # No runbooks\n")


def main():
    """Main entry point."""
    repo_root = get_repo_root()
    modules_dir = repo_root / "modules"
    commands_dir = repo_root / ".claude" / "commands"

    print("Syncing workspace...")

    # Ensure directories exist
    commands_dir.mkdir(parents=True, exist_ok=True)

    # Remove stale symlinks (but not protected files)
    stale_removed = 0
    for link in commands_dir.glob("*.md"):
        if is_protected(link.name):
            continue
        if link.is_symlink() and not link.exists():
            link.unlink()
            stale_removed += 1

    if stale_removed:
        print(f"  Removed {stale_removed} stale symlink(s)")

    # Sync module commands
    modules_synced, commands_updated = sync_module_commands(modules_dir, commands_dir)

    # Rebuild index
    rebuild_index(repo_root, modules_dir)

    print(f"Synced {modules_synced} modules, {commands_updated} commands updated")
    print(f"Generated {INDEX_FILE}")


if __name__ == "__main__":
    main()
