"""
DataOS — LinkedIn Collector (via Unipile API)

Collects LinkedIn data for engagement tracking and DM follow-ups:
- Profile views (who viewed your profile)
- Post engagement (likes, comments, shares)
- Messages and conversations
- Connection requests
- Notifications

Usage:
    python scripts/collect_linkedin.py              # Full collection
    python scripts/collect_linkedin.py --profile    # Just profile views
    python scripts/collect_linkedin.py --messages   # Just messages
    python scripts/collect_linkedin.py --chats      # List all chats
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, timezone
from pathlib import Path

# Add scripts to path for db import
sys.path.insert(0, str(Path(__file__).parent))
from db import get_connection, log_collection

# Load environment variables
from dotenv import load_dotenv
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(WORKSPACE_ROOT / ".env")

# Unipile configuration
UNIPILE_DSN = os.getenv("UNIPILE_DSN")
UNIPILE_API_KEY = os.getenv("UNIPILE_API_KEY")
UNIPILE_ACCOUNT_ID = os.getenv("UNIPILE_ACCOUNT_ID")

# Build base URL from DSN
BASE_URL = f"https://{UNIPILE_DSN}/api/v1" if UNIPILE_DSN else None


def get_headers():
    """Get API headers with authentication."""
    return {
        "X-API-KEY": UNIPILE_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


def check_config():
    """Verify Unipile configuration is present."""
    missing = []
    if not UNIPILE_DSN:
        missing.append("UNIPILE_DSN")
    if not UNIPILE_API_KEY:
        missing.append("UNIPILE_API_KEY")
    if not UNIPILE_ACCOUNT_ID:
        missing.append("UNIPILE_ACCOUNT_ID")

    if missing:
        print(f"ERROR: Missing environment variables: {', '.join(missing)}")
        print("Add these to your .env file.")
        return False
    return True


def api_request(endpoint, method="GET", params=None, data=None):
    """Make an API request to Unipile."""
    url = f"{BASE_URL}/{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, headers=get_headers(), params=params, timeout=30)
        elif method == "POST":
            response = requests.post(url, headers=get_headers(), json=data, timeout=30)
        else:
            raise ValueError(f"Unsupported method: {method}")

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text[:500]}")
        return None


def init_linkedin_tables(conn):
    """Create LinkedIn-related tables if they don't exist."""

    # Profile views - who viewed your LinkedIn profile
    conn.execute("""
        CREATE TABLE IF NOT EXISTS linkedin_profile_views (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            viewer_id TEXT,
            viewer_name TEXT,
            viewer_headline TEXT,
            viewer_profile_url TEXT,
            viewed_at TEXT,
            collected_at TEXT NOT NULL,
            raw_data TEXT,
            UNIQUE(viewer_id, viewed_at)
        )
    """)

    # Conversations/Chats
    conn.execute("""
        CREATE TABLE IF NOT EXISTS linkedin_chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id TEXT UNIQUE NOT NULL,
            participant_id TEXT,
            participant_name TEXT,
            participant_headline TEXT,
            last_message_at TEXT,
            unread_count INTEGER DEFAULT 0,
            collected_at TEXT NOT NULL,
            raw_data TEXT
        )
    """)

    # Messages
    conn.execute("""
        CREATE TABLE IF NOT EXISTS linkedin_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message_id TEXT UNIQUE NOT NULL,
            chat_id TEXT,
            sender_id TEXT,
            sender_name TEXT,
            content TEXT,
            sent_at TEXT,
            is_inbound INTEGER DEFAULT 1,
            collected_at TEXT NOT NULL,
            raw_data TEXT
        )
    """)

    # Connection requests (pending)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS linkedin_invitations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invitation_id TEXT UNIQUE NOT NULL,
            from_id TEXT,
            from_name TEXT,
            from_headline TEXT,
            from_profile_url TEXT,
            message TEXT,
            received_at TEXT,
            status TEXT DEFAULT 'pending',
            collected_at TEXT NOT NULL,
            raw_data TEXT
        )
    """)

    # Notifications
    conn.execute("""
        CREATE TABLE IF NOT EXISTS linkedin_notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            notification_id TEXT UNIQUE NOT NULL,
            notification_type TEXT,
            actor_name TEXT,
            content TEXT,
            post_id TEXT,
            created_at TEXT,
            is_read INTEGER DEFAULT 0,
            collected_at TEXT NOT NULL,
            raw_data TEXT
        )
    """)

    conn.commit()
    print("LinkedIn tables initialized.")


def collect_my_profile(conn):
    """Fetch own LinkedIn profile info from connected accounts."""
    print("\n--- Fetching your LinkedIn profile ---")

    result = api_request("accounts")
    if not result:
        print("Failed to fetch accounts.")
        return None

    items = result.get("items", [])
    linkedin_account = next(
        (acc for acc in items if acc.get("type") == "LINKEDIN" and acc.get("id") == UNIPILE_ACCOUNT_ID),
        None
    )

    if linkedin_account:
        name = linkedin_account.get("name", "Unknown")
        conn_params = linkedin_account.get("connection_params", {}).get("im", {})
        public_id = conn_params.get("publicIdentifier", "N/A")
        print(f"Profile: {name}")
        print(f"LinkedIn Handle: @{public_id}")
        print(f"Premium: {conn_params.get('premiumFeatures', [])}")
        return linkedin_account
    else:
        print("LinkedIn account not found.")
        return None


def collect_chats(conn, limit=50):
    """Collect LinkedIn conversations/chats."""
    print(f"\n--- Collecting LinkedIn chats (limit={limit}) ---")

    result = api_request("chats", params={
        "account_id": UNIPILE_ACCOUNT_ID,
        "limit": limit
    })

    if not result:
        print("Failed to fetch chats.")
        return 0

    chats = result.get("items", [])
    now = datetime.now(timezone.utc).isoformat()
    count = 0

    for chat in chats:
        try:
            chat_id = chat.get("id")
            if not chat_id:
                continue

            # Chat name is often the subject or participant name
            chat_name = chat.get("name") or chat.get("subject") or "Unknown"
            content_type = chat.get("content_type", "message")
            attendee_id = chat.get("attendee_provider_id")

            conn.execute("""
                INSERT OR REPLACE INTO linkedin_chats
                (chat_id, participant_id, participant_name, participant_headline,
                 last_message_at, unread_count, collected_at, raw_data)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                chat_id,
                attendee_id,
                chat_name,
                content_type,  # Using content_type as headline placeholder
                chat.get("timestamp"),
                chat.get("unread_count", 0),
                now,
                json.dumps(chat)
            ))
            count += 1
        except Exception as e:
            print(f"Error processing chat: {e}")
            continue

    conn.commit()
    print(f"Collected {count} chats.")

    # Show summary
    unread_total = sum(c.get("unread_count", 0) for c in chats)
    print(f"  Total unread: {unread_total}")
    return count


def collect_messages(conn, chat_id=None, limit=20):
    """Collect messages from LinkedIn chats."""
    print(f"\n--- Collecting LinkedIn messages ---")

    # If no chat_id specified, get messages from recent non-read-only chats
    if chat_id:
        chat_ids = [chat_id]
    else:
        rows = conn.execute("""
            SELECT chat_id FROM linkedin_chats
            WHERE json_extract(raw_data, '$.read_only') = 0
            ORDER BY last_message_at DESC LIMIT 10
        """).fetchall()
        chat_ids = [row[0] for row in rows]

    if not chat_ids:
        print("No chats found. Run --chats first.")
        return 0

    now = datetime.now(timezone.utc).isoformat()
    total_count = 0

    for cid in chat_ids:
        result = api_request(f"chats/{cid}/messages", params={"limit": limit})

        if not result:
            continue

        messages = result.get("items", [])

        for msg in messages:
            try:
                msg_id = msg.get("id")
                if not msg_id:
                    continue

                sender = msg.get("sender", {})
                sender_id = sender.get("attendee_provider_id") or sender.get("id")

                # Determine if inbound (not from us)
                # Check if sender matches our LinkedIn ID pattern
                is_inbound = 1
                if sender.get("account_id") == UNIPILE_ACCOUNT_ID:
                    is_inbound = 0

                conn.execute("""
                    INSERT OR IGNORE INTO linkedin_messages
                    (message_id, chat_id, sender_id, sender_name, content,
                     sent_at, is_inbound, collected_at, raw_data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    msg_id,
                    cid,
                    sender_id,
                    sender.get("name", "Unknown"),
                    msg.get("text") or msg.get("text_content") or "",
                    msg.get("timestamp") or msg.get("created_at"),
                    is_inbound,
                    now,
                    json.dumps(msg)
                ))
                total_count += 1
            except Exception as e:
                print(f"Error processing message: {e}")
                continue

    conn.commit()
    print(f"Collected {total_count} messages from {len(chat_ids)} chats.")
    return total_count


def collect_invitations(conn):
    """Collect pending connection requests."""
    print("\n--- Collecting connection requests ---")

    result = api_request("invitations/received", params={
        "account_id": UNIPILE_ACCOUNT_ID
    })

    if not result:
        print("Failed to fetch invitations (or none pending).")
        return 0

    invitations = result.get("items", result) if isinstance(result, dict) else result
    if not isinstance(invitations, list):
        invitations = [invitations] if invitations else []

    now = datetime.now(timezone.utc).isoformat()
    count = 0

    for inv in invitations:
        try:
            inv_id = inv.get("id") or inv.get("invitation_id")
            if not inv_id:
                continue

            sender = inv.get("from", {}) or inv.get("sender", {})

            conn.execute("""
                INSERT OR REPLACE INTO linkedin_invitations
                (invitation_id, from_id, from_name, from_headline, from_profile_url,
                 message, received_at, status, collected_at, raw_data)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                inv_id,
                sender.get("id"),
                sender.get("name"),
                sender.get("headline"),
                sender.get("profile_url") or sender.get("public_identifier"),
                inv.get("message"),
                inv.get("created_at") or inv.get("received_at"),
                "pending",
                now,
                json.dumps(inv)
            ))
            count += 1
        except Exception as e:
            print(f"Error processing invitation: {e}")
            continue

    conn.commit()
    print(f"Collected {count} pending invitations.")
    return count


def search_people(conn, query, limit=25):
    """Search for people on LinkedIn (requires LinkedIn API subscription)."""
    print(f"\n--- LinkedIn Search ---")
    print("Note: People search requires LinkedIn API tier with search capability.")
    print("Current Unipile plan supports messaging features (chats, messages).")
    print(f"For lead search, use: python scripts/collect_apollo.py")
    return []


def send_message(conn, chat_id, message):
    """Send a message to a LinkedIn chat."""
    print(f"\n--- Sending message to chat {chat_id} ---")

    result = api_request(f"chats/{chat_id}/messages", method="POST", data={
        "text": message
    })

    if result:
        print(f"Message sent successfully.")
        return result
    else:
        print("Failed to send message.")
        return None


def get_engagement_summary(conn):
    """Get a summary of recent LinkedIn engagement."""
    print("\n--- LinkedIn Engagement Summary ---")

    # Recent messages (inbound)
    inbound = conn.execute("""
        SELECT COUNT(*) as count FROM linkedin_messages
        WHERE is_inbound = 1
        AND datetime(sent_at) > datetime('now', '-7 days')
    """).fetchone()

    # Active chats
    active_chats = conn.execute("""
        SELECT COUNT(*) as count FROM linkedin_chats
        WHERE datetime(last_message_at) > datetime('now', '-7 days')
    """).fetchone()

    # Pending invitations
    pending = conn.execute("""
        SELECT COUNT(*) as count FROM linkedin_invitations
        WHERE status = 'pending'
    """).fetchone()

    print(f"  Inbound messages (7d): {inbound[0] if inbound else 0}")
    print(f"  Active chats (7d): {active_chats[0] if active_chats else 0}")
    print(f"  Pending invitations: {pending[0] if pending else 0}")

    # Recent messages preview
    print("\n  Recent inbound messages:")
    messages = conn.execute("""
        SELECT sender_name, content, sent_at
        FROM linkedin_messages
        WHERE is_inbound = 1
        ORDER BY sent_at DESC LIMIT 5
    """).fetchall()

    for msg in messages:
        name = msg[0] or "Unknown"
        content = (msg[1] or "")[:60]
        print(f"    - {name}: {content}...")


def main():
    parser = argparse.ArgumentParser(description="Collect LinkedIn data via Unipile")
    parser.add_argument("--profile", action="store_true", help="Fetch your profile")
    parser.add_argument("--chats", action="store_true", help="Collect conversations")
    parser.add_argument("--messages", action="store_true", help="Collect messages")
    parser.add_argument("--invitations", action="store_true", help="Collect connection requests")
    parser.add_argument("--search", type=str, help="Search for people")
    parser.add_argument("--summary", action="store_true", help="Show engagement summary")
    parser.add_argument("--all", action="store_true", help="Collect everything")
    args = parser.parse_args()

    # Check configuration
    if not check_config():
        sys.exit(1)

    print(f"Unipile LinkedIn Collector")
    print(f"Base URL: {BASE_URL}")
    print(f"Account ID: {UNIPILE_ACCOUNT_ID}")

    # Initialize database
    conn = get_connection()
    init_linkedin_tables(conn)

    total_records = 0

    try:
        # Default to --all if no specific flags
        if not any([args.profile, args.chats, args.messages, args.invitations, args.search, args.summary]):
            args.all = True

        if args.profile or args.all:
            collect_my_profile(conn)

        if args.chats or args.all:
            total_records += collect_chats(conn)

        if args.messages or args.all:
            total_records += collect_messages(conn)

        if args.invitations or args.all:
            total_records += collect_invitations(conn)

        if args.search:
            search_people(conn, args.search)

        if args.summary or args.all:
            get_engagement_summary(conn)

        # Log successful collection
        log_collection(conn, "linkedin", "success", total_records)
        print(f"\n✓ Collection complete. {total_records} records collected.")

    except Exception as e:
        log_collection(conn, "linkedin", "error", reason=str(e))
        print(f"\n✗ Collection failed: {e}")
        raise
    finally:
        conn.close()


def collect():
    """
    Orchestrator-compatible entry point.
    Returns dict with status, data, and reason.
    """
    if not check_config():
        return {"status": "error", "reason": "Missing UNIPILE_* env vars"}

    try:
        conn = get_connection()
        init_linkedin_tables(conn)

        # Collect chats and messages
        chats_count = collect_chats(conn, limit=50)
        messages_count = collect_messages(conn, limit=20)

        conn.close()

        return {
            "status": "success",
            "data": {
                "chats": chats_count,
                "messages": messages_count
            }
        }
    except Exception as e:
        return {"status": "error", "reason": str(e)}


def write(conn, result, date):
    """
    Orchestrator-compatible write function.
    Since we write during collect(), just return the count.
    """
    data = result.get("data", {})
    return data.get("chats", 0) + data.get("messages", 0)


if __name__ == "__main__":
    main()
