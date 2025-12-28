#!/usr/bin/env python3
"""
Dokploy API Integration Script

Execution tool for managing Dokploy compose services via the REST API.
Complements the Dokploy MCP tools which don't expose compose creation.

Usage (CLI):
    ./run tools/dokploy_api.py compose create <environment_id> <name> --file compose.yaml
    ./run tools/dokploy_api.py compose create <environment_id> <name> --yaml "services:..."
    ./run tools/dokploy_api.py compose update <compose_id> --file compose.yaml --env "KEY=value"
    ./run tools/dokploy_api.py compose deploy <compose_id>
    ./run tools/dokploy_api.py compose list <environment_id>
    ./run tools/dokploy_api.py compose get <compose_id>
    ./run tools/dokploy_api.py compose delete <compose_id>

Usage (Module):
    from tools.dokploy_api import DokployClient
    client = DokployClient()
    compose = client.create_compose("env-id", "my-app", compose_file="services:\\n  app:...")
    client.update_compose(compose["composeId"], env="KEY=value\\nKEY2=value2")
    client.deploy_compose(compose["composeId"])
"""

import sys
import os
import json
import argparse
import requests
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to get from .env first, then fall back to .mcp.json pattern
DOKPLOY_API_URL = os.getenv("DOKPLOY_URL") or os.getenv("DOKPLOY_API_URL", "")
DOKPLOY_API_KEY = os.getenv("DOKPLOY_API_KEY", "")

# If not in .env, try to read from .mcp.json
if not DOKPLOY_API_URL or not DOKPLOY_API_KEY:
    mcp_json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".mcp.json")
    if os.path.exists(mcp_json_path):
        with open(mcp_json_path) as f:
            mcp_config = json.load(f)
            dokploy_config = mcp_config.get("mcpServers", {}).get("dokploy", {}).get("env", {})
            DOKPLOY_API_URL = DOKPLOY_API_URL or dokploy_config.get("DOKPLOY_URL", "")
            DOKPLOY_API_KEY = DOKPLOY_API_KEY or dokploy_config.get("DOKPLOY_API_KEY", "")


# --- Custom Exceptions ---

class DokployError(Exception):
    """Base exception for Dokploy API errors."""
    pass


class DokployAuthError(DokployError):
    """Authentication/token error."""
    pass


class DokployNotFoundError(DokployError):
    """Resource not found."""
    pass


class DokployClient:
    """Client for interacting with Dokploy API."""

    def __init__(self, api_url: str = None, api_key: str = None):
        self.api_url = (api_url or DOKPLOY_API_URL).rstrip("/")
        self.api_key = api_key or DOKPLOY_API_KEY

        if not self.api_url:
            raise ValueError("DOKPLOY_URL not configured. Set it in .env or .mcp.json")
        if not self.api_key:
            raise ValueError("DOKPLOY_API_KEY not configured. Set it in .env or .mcp.json")

        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """Make an API request to Dokploy."""
        url = f"{self.api_url}{endpoint}"

        if method == "GET":
            # GET uses query parameters
            response = requests.get(url, headers=self.headers, params=data)
        else:
            # POST uses JSON body
            response = requests.post(url, headers=self.headers, json=data)

        if response.status_code == 401:
            raise DokployAuthError("Authentication failed. Check your API key.")
        elif response.status_code == 404:
            raise DokployNotFoundError(f"Resource not found: {endpoint}")
        elif response.status_code == 400:
            try:
                error_data = response.json()
                raise DokployError(f"Validation error: {error_data.get('message', response.text)}")
            except json.JSONDecodeError:
                raise DokployError(f"Bad request: {response.text}")

        try:
            result = response.json()
        except json.JSONDecodeError:
            raise DokployError(f"Invalid JSON response: {response.text}")

        # Handle error responses
        if isinstance(result, dict) and "error" in result:
            error_msg = result["error"].get("message", str(result["error"]))
            raise DokployError(f"API error: {error_msg}")

        return result

    # --- Compose Operations ---

    def create_compose(
        self,
        environment_id: str,
        name: str,
        compose_file: str = None,
        description: str = None,
        server_id: str = None
    ) -> Dict[str, Any]:
        """
        Create a new compose service.

        Args:
            environment_id: ID of the environment to create in
            name: Name for the compose service
            compose_file: Optional initial compose YAML content
            description: Optional description
            server_id: Optional server ID for remote deployment

        Returns:
            Created compose service details
        """
        data = {
            "name": name,
            "environmentId": environment_id,
        }

        if server_id:
            data["serverId"] = server_id

        result = self._request("POST", "/compose.create", data)

        # If compose_file provided, update it immediately
        if compose_file and result.get("composeId"):
            self.update_compose(
                result["composeId"],
                compose_file=compose_file,
                source_type="raw"
            )
            # Re-fetch to get updated data
            result = self.get_compose(result["composeId"])

        return result

    def get_compose(self, compose_id: str) -> Dict[str, Any]:
        """Get compose service details."""
        return self._request("GET", "/compose.one", {"composeId": compose_id})

    def update_compose(
        self,
        compose_id: str,
        name: str = None,
        description: str = None,
        compose_file: str = None,
        env: str = None,
        source_type: str = None,
        compose_path: str = None
    ) -> Dict[str, Any]:
        """
        Update a compose service.

        Args:
            compose_id: ID of the compose service
            name: New name
            description: New description
            compose_file: New compose YAML content
            env: Environment variables (newline-separated KEY=value pairs)
            source_type: Source type ("raw", "github", etc.)
            compose_path: Path to compose file in repo

        Returns:
            Updated compose service details
        """
        data = {"composeId": compose_id}

        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if compose_file is not None:
            data["composeFile"] = compose_file
        if env is not None:
            data["env"] = env
        if source_type is not None:
            data["sourceType"] = source_type
        if compose_path is not None:
            data["composePath"] = compose_path

        return self._request("POST", "/compose.update", data)

    def deploy_compose(self, compose_id: str, title: str = None, description: str = None) -> Dict[str, Any]:
        """Deploy a compose service."""
        data = {"composeId": compose_id}
        if title:
            data["title"] = title
        if description:
            data["description"] = description

        return self._request("POST", "/compose.deploy", data)

    def delete_compose(self, compose_id: str) -> bool:
        """Delete a compose service."""
        self._request("POST", "/compose.delete", {"composeId": compose_id})
        return True

    def stop_compose(self, compose_id: str) -> Dict[str, Any]:
        """Stop a compose service."""
        return self._request("POST", "/compose.stop", {"composeId": compose_id})

    def start_compose(self, compose_id: str) -> Dict[str, Any]:
        """Start a compose service."""
        return self._request("POST", "/compose.start", {"composeId": compose_id})


# --- CLI Interface ---

def cmd_compose_create(args, client: DokployClient):
    """Create a compose service."""
    compose_file = None

    if args.file:
        with open(args.file) as f:
            compose_file = f.read()
    elif args.yaml:
        compose_file = args.yaml

    result = client.create_compose(
        environment_id=args.environment_id,
        name=args.name,
        compose_file=compose_file,
        description=args.description
    )

    print(f"Created compose service:")
    print(f"  ID: {result.get('composeId')}")
    print(f"  Name: {result.get('name')}")
    print(f"  App Name: {result.get('appName')}")

    if args.env:
        # Update with env vars
        client.update_compose(result["composeId"], env=args.env)
        print(f"  Environment variables set")

    return result


def cmd_compose_update(args, client: DokployClient):
    """Update a compose service."""
    compose_file = None

    if args.file:
        with open(args.file) as f:
            compose_file = f.read()
    elif args.yaml:
        compose_file = args.yaml

    result = client.update_compose(
        compose_id=args.compose_id,
        name=args.name,
        description=args.description,
        compose_file=compose_file,
        env=args.env,
        source_type="raw" if compose_file else None
    )

    print(f"Updated compose service: {args.compose_id}")
    return result


def cmd_compose_deploy(args, client: DokployClient):
    """Deploy a compose service."""
    result = client.deploy_compose(
        compose_id=args.compose_id,
        title=args.title,
        description=args.description
    )

    print(f"Deployment initiated for: {args.compose_id}")
    return result


def cmd_compose_get(args, client: DokployClient):
    """Get compose service details."""
    result = client.get_compose(args.compose_id)

    print(f"Compose Service: {result.get('name')}")
    print(f"  ID: {result.get('composeId')}")
    print(f"  App Name: {result.get('appName')}")
    print(f"  Status: {result.get('composeStatus')}")
    print(f"  Source Type: {result.get('sourceType')}")

    if args.verbose:
        print(f"\nCompose File:")
        print(result.get('composeFile', '(empty)'))
        print(f"\nEnvironment Variables:")
        print(result.get('env', '(none)'))

    return result


def cmd_compose_delete(args, client: DokployClient):
    """Delete a compose service."""
    if not args.yes:
        confirm = input(f"Are you sure you want to delete compose {args.compose_id}? [y/N] ")
        if confirm.lower() != 'y':
            print("Cancelled.")
            return

    client.delete_compose(args.compose_id)
    print(f"Deleted compose service: {args.compose_id}")


def main():
    parser = argparse.ArgumentParser(description="Dokploy API CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command group")

    # --- Compose commands ---
    compose_parser = subparsers.add_parser("compose", help="Compose service operations")
    compose_sub = compose_parser.add_subparsers(dest="subcommand")

    # compose create
    compose_create = compose_sub.add_parser("create", help="Create compose service")
    compose_create.add_argument("environment_id", help="Environment ID")
    compose_create.add_argument("name", help="Service name")
    compose_create.add_argument("--file", "-f", help="Path to compose YAML file")
    compose_create.add_argument("--yaml", help="Compose YAML content directly")
    compose_create.add_argument("--env", "-e", help="Environment variables (KEY=value, newline-separated)")
    compose_create.add_argument("--description", "-d", help="Service description")

    # compose update
    compose_update = compose_sub.add_parser("update", help="Update compose service")
    compose_update.add_argument("compose_id", help="Compose service ID")
    compose_update.add_argument("--file", "-f", help="Path to compose YAML file")
    compose_update.add_argument("--yaml", help="Compose YAML content directly")
    compose_update.add_argument("--env", "-e", help="Environment variables")
    compose_update.add_argument("--name", help="New name")
    compose_update.add_argument("--description", "-d", help="New description")

    # compose deploy
    compose_deploy = compose_sub.add_parser("deploy", help="Deploy compose service")
    compose_deploy.add_argument("compose_id", help="Compose service ID")
    compose_deploy.add_argument("--title", help="Deployment title")
    compose_deploy.add_argument("--description", "-d", help="Deployment description")

    # compose get
    compose_get = compose_sub.add_parser("get", help="Get compose service details")
    compose_get.add_argument("compose_id", help="Compose service ID")
    compose_get.add_argument("--verbose", "-v", action="store_true", help="Show full details")

    # compose delete
    compose_delete = compose_sub.add_parser("delete", help="Delete compose service")
    compose_delete.add_argument("compose_id", help="Compose service ID")
    compose_delete.add_argument("-y", "--yes", action="store_true", help="Skip confirmation")

    # compose start
    compose_start = compose_sub.add_parser("start", help="Start compose service")
    compose_start.add_argument("compose_id", help="Compose service ID")

    # compose stop
    compose_stop = compose_sub.add_parser("stop", help="Stop compose service")
    compose_stop.add_argument("compose_id", help="Compose service ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        client = DokployClient()

        if args.command == "compose":
            if args.subcommand == "create":
                cmd_compose_create(args, client)
            elif args.subcommand == "update":
                cmd_compose_update(args, client)
            elif args.subcommand == "deploy":
                cmd_compose_deploy(args, client)
            elif args.subcommand == "get":
                cmd_compose_get(args, client)
            elif args.subcommand == "delete":
                cmd_compose_delete(args, client)
            elif args.subcommand == "start":
                client.start_compose(args.compose_id)
                print(f"Started compose service: {args.compose_id}")
            elif args.subcommand == "stop":
                client.stop_compose(args.compose_id)
                print(f"Stopped compose service: {args.compose_id}")
            else:
                compose_parser.print_help()

    except DokployAuthError as e:
        print(f"Authentication error: {e}", file=sys.stderr)
        sys.exit(1)
    except DokployNotFoundError as e:
        print(f"Not found: {e}", file=sys.stderr)
        sys.exit(1)
    except DokployError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
