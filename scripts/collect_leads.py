"""
DataOS — Lead Tracker Collector (Google Sheets)

Reads your lead tracking spreadsheet into the database.
Expects a Google Sheet with these columns (row 1 = headers):

    Date | Name | Company | Source | Status | Service | Value | Notes

Share your sheet with: dataos-reader@arise-aios.iam.gserviceaccount.com

Requires:
    GOOGLE_SERVICE_ACCOUNT_JSON  — Service account JSON path
    SHEETS_LEAD_TRACKER_ID       — Spreadsheet ID from URL

Tables created: leads
Extra pip: google-api-python-client google-auth
"""

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

try:
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
except ImportError:
    raise ImportError(
        "Missing packages — run: pip install google-api-python-client google-auth"
    )


def _get_sheets_service():
    """Create an authenticated Google Sheets API client."""
    creds_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
    if not creds_path:
        return None
    full_path = Path(creds_path)
    if not full_path.is_absolute():
        full_path = Path(__file__).resolve().parent.parent / creds_path
    if not full_path.exists():
        return None
    creds = Credentials.from_service_account_file(
        str(full_path),
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )
    return build("sheets", "v4", credentials=creds)


def collect():
    """Read leads from the Google Sheet."""
    sheet_id = os.getenv("SHEETS_LEAD_TRACKER_ID", "").strip()
    if not sheet_id:
        return {
            "source": "leads", "status": "skipped",
            "reason": "Missing SHEETS_LEAD_TRACKER_ID — create your lead "
                      "tracking sheet and add the ID to .env"
        }

    service = _get_sheets_service()
    if not service:
        return {
            "source": "leads", "status": "skipped",
            "reason": "Missing or invalid GOOGLE_SERVICE_ACCOUNT_JSON"
        }

    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range="A:H"
        ).execute()
        values = result.get("values", [])

        if not values or len(values) < 2:
            return {
                "source": "leads", "status": "skipped",
                "reason": "Sheet is empty or has only headers"
            }

        # Parse headers and rows
        raw_headers = [str(h).strip().lower().replace(" ", "_") for h in values[0]]
        rows = []
        for row in values[1:]:
            if not any(cell.strip() for cell in row if cell):
                continue
            padded = row + [""] * (len(raw_headers) - len(row))
            row_dict = {raw_headers[i]: padded[i].strip() for i in range(len(raw_headers))}
            rows.append(row_dict)

        return {
            "source": "leads",
            "status": "success",
            "data": {
                "headers": raw_headers,
                "rows": rows,
                "row_count": len(rows),
            }
        }

    except Exception as e:
        return {"source": "leads", "status": "error", "reason": str(e)}


def write(conn, result, date):
    """Write leads to the database. Returns records written."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            date TEXT,
            name TEXT,
            company TEXT,
            source TEXT,
            status TEXT,
            service TEXT,
            value TEXT,
            notes TEXT,
            collected_at TEXT,
            PRIMARY KEY (name, company)
        )
    """)

    if result.get("status") != "success":
        conn.commit()
        return 0

    collected_at = datetime.now(timezone.utc).isoformat()
    records = 0

    for row in result["data"]["rows"]:
        name = row.get("name", "").strip()
        company = row.get("company", "").strip()
        if not name and not company:
            continue

        conn.execute(
            "INSERT OR REPLACE INTO leads "
            "(date, name, company, source, status, service, value, notes, collected_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                row.get("date", ""),
                name,
                company,
                row.get("source", ""),
                row.get("status", ""),
                row.get("service", ""),
                row.get("value", ""),
                row.get("notes", ""),
                collected_at,
            )
        )
        records += 1

    conn.commit()
    return records


if __name__ == "__main__":
    result = collect()
    if result["status"] == "success":
        data = result["data"]
        print(f"Leads: {data['row_count']} rows")
        print(f"Headers: {', '.join(data['headers'])}")
        if data["rows"]:
            print(f"First lead: {data['rows'][0].get('name', '?')} @ {data['rows'][0].get('company', '?')}")
    else:
        print(f"{result['status']}: {result.get('reason', '')}")
