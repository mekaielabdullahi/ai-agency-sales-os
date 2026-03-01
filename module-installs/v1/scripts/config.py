"""
Configuration loader for AI Landscape Monitor.
Reads optional API keys from .env file.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Scripts directory (where this file lives)
SCRIPTS_DIR = Path(__file__).resolve().parent


def _find_workspace_root() -> Path:
    """Find the workspace root by walking up from the scripts directory.

    Looks for markers: CLAUDE.md, .claude/, or data/ directory.
    Falls back to one level above scripts/ (assumes scripts/ is directly in workspace root).
    """
    current = SCRIPTS_DIR
    for _ in range(6):  # Don't walk up more than 6 levels
        if (current / "CLAUDE.md").exists() or (current / ".claude").exists():
            return current
        current = current.parent
    # Fallback: assume scripts/ is directly inside workspace root
    return SCRIPTS_DIR.parent


WORKSPACE_ROOT = _find_workspace_root()

# Load .env from workspace root first, then scripts dir as fallback
load_dotenv(WORKSPACE_ROOT / ".env")
load_dotenv(SCRIPTS_DIR / ".env")


def get_env(key: str) -> str | None:
    """Get an environment variable. Returns None if not set."""
    value = os.getenv(key, "").strip()
    return value if value else None


def get_db_path() -> Path:
    """Get the path to the SQLite database.

    Uses DB_PATH env var if set, otherwise looks for any .db file in data/,
    falling back to data/workspace.db.
    """
    env_path = get_env("DB_PATH")
    if env_path:
        return Path(env_path) if Path(env_path).is_absolute() else WORKSPACE_ROOT / env_path

    data_dir = WORKSPACE_ROOT / "data"
    if data_dir.exists():
        db_files = list(data_dir.glob("*.db"))
        if db_files:
            return db_files[0]  # Use existing DB

    return data_dir / "workspace.db"


def get_ai_docs_dir() -> Path:
    """Get the path to the ai-docs folder."""
    return WORKSPACE_ROOT / "ai-docs"


def get_scan_output_path() -> Path:
    """Get the path for the scan results JSON."""
    return WORKSPACE_ROOT / "data" / "ai-scan-latest.json"


def get_report_dir() -> Path:
    """Get the path for daily landscape reports."""
    return WORKSPACE_ROOT / "outputs" / "daily-intel" / "ai-landscape"


if __name__ == "__main__":
    print(f"Workspace root: {WORKSPACE_ROOT}")
    print(f"DB path: {get_db_path()}")
    print(f"AI docs dir: {get_ai_docs_dir()}")
    print(f"OpenRouter key: {'set' if get_env('OPENROUTER_API_KEY') else 'not set'}")
