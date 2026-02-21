"""
Shared Notion API helper for agentic modules.

Provides a single notion_request() implementation used by all Notion tools.
"""

import os
from typing import Dict, Optional

try:
    import requests
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

NOTION_VERSION = "2022-06-28"


def notion_request(method: str, endpoint: str, data: Dict = None,
                   api_key: str = None, version: str = None) -> Dict:
    """
    Make a request to the Notion API.

    Args:
        method: HTTP method ("GET", "POST", "PATCH")
        endpoint: API endpoint (e.g. "pages/{id}" or "databases/{id}/query")
        data: JSON body for POST/PATCH requests
        api_key: Override NOTION_API_KEY from env
        version: Override Notion API version

    Returns:
        Parsed JSON response

    Raises:
        ValueError: If API key is not configured
        Exception: On Notion API errors
    """
    key = api_key or os.getenv("NOTION_API_KEY", "")
    ver = version or NOTION_VERSION

    if not key:
        raise ValueError("NOTION_API_KEY not configured. Set it in agentic/.env file.")

    url = f"https://api.notion.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {key}",
        "Notion-Version": ver,
        "Content-Type": "application/json"
    }

    if method.upper() == "GET":
        response = requests.get(url, headers=headers)
    elif method.upper() == "PATCH":
        response = requests.patch(url, headers=headers, json=data or {})
    else:
        response = requests.post(url, headers=headers, json=data or {})

    if response.status_code != 200:
        error = response.json().get("message", response.text)
        raise Exception(f"Notion API error ({response.status_code}): {error}")

    return response.json()
