"""
Shared Google OAuth credentials helper for agentic modules.

Provides get_google_credentials() used by SOP extractor, md-to-gdoc exporter,
and other tools that need user-level Google OAuth access.
"""

import os
import sys

# Google API scopes used across modules
DEFAULT_SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file"
]


def get_google_credentials(scopes: list = None, exit_on_missing: bool = False):
    """
    Get Google OAuth credentials, refreshing or initiating flow as needed.

    Args:
        scopes: OAuth scopes to request. Defaults to Docs + Drive.
        exit_on_missing: If True, sys.exit(1) when credentials.json is missing.
                         If False, return None (let caller handle gracefully).

    Returns:
        google.oauth2.credentials.Credentials or None
    """
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    scopes = scopes or DEFAULT_SCOPES
    creds = None

    if os.path.exists("token.json"):
        try:
            creds = Credentials.from_authorized_user_file("token.json", scopes)
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None

        if not creds:
            if not os.path.exists("credentials.json"):
                if exit_on_missing:
                    print("Error: credentials.json not found.", file=sys.stderr)
                    print("Please set up Google OAuth credentials first.", file=sys.stderr)
                    sys.exit(1)
                else:
                    print("Warning: credentials.json not found. Google Doc creation will be skipped.", file=sys.stderr)
                    return None

            print("Initiating Google OAuth flow...", file=sys.stderr)
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
            creds = flow.run_local_server(port=8080)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds
