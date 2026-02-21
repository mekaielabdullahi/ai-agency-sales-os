"""
Shared environment loader for agentic modules.

Finds and loads the agentic/.env file by walking up from the caller's directory.
Works regardless of how deeply nested the calling script is.
"""

import os

_loaded = False


def load_env(start_dir: str = None):
    """
    Load environment variables from the agentic .env file.

    Searches upward from start_dir (or this file's location) for a .env file
    that sits alongside a 'modules/' directory (i.e., the agentic root).

    Args:
        start_dir: Directory to start searching from. Defaults to this file's dir.
    """
    global _loaded
    if _loaded:
        return

    search = os.path.abspath(start_dir or os.path.dirname(__file__))

    for _ in range(10):  # max 10 levels up
        env_path = os.path.join(search, '.env')
        modules_dir = os.path.join(search, 'modules')
        if os.path.isfile(env_path) and os.path.isdir(modules_dir):
            _parse_env_file(env_path)
            _loaded = True
            return
        parent = os.path.dirname(search)
        if parent == search:
            break
        search = parent


def _parse_env_file(path: str):
    """Parse a .env file and set environment variables (without overwriting)."""
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())
