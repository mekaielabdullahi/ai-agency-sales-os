"""
DataOS — Apollo.io Lead Scraper

Pain-signal targeting across the DMV (DC / Northern Virginia / Maryland).
Targets service businesses actively hiring for roles AI can replace —
admin, ops, scheduling, intake, dispatch, data entry.

Strategy: Industry-agnostic, geo-first, pain-signal driven.
Geography: Washington DC, Northern Virginia, Maryland (DMV metro)

Results saved to: data/data.db (apollo_leads table)
CSV export to:    outputs/leads/apollo-leads-YYYY-MM-DD.csv

Usage:
    python scripts/collect_apollo.py                    # all segments
    python scripts/collect_apollo.py --segment gov      # gov contractors only
    python scripts/collect_apollo.py --pages 3          # more leads per search

Requires:
    APOLLO_API_KEY in .env

Apollo API notes:
    - People Search: FREE (no credits consumed)
    - Email enrichment: 1 credit per lead (run separately)
    - Rate limit: 20 requests/minute → 3s delay between requests
"""

import os
import csv
import time
import argparse
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

# ── Config ────────────────────────────────────────────────────────────────────

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(WORKSPACE_ROOT / ".env")

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY", "").strip()
DB_PATH = WORKSPACE_ROOT / "data" / "data.db"
OUTPUT_DIR = WORKSPACE_ROOT / "outputs" / "leads"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

APOLLO_SEARCH_URL = "https://api.apollo.io/v1/mixed_people/search"
REQUEST_DELAY = 3  # seconds between requests (rate limit safety)

# DMV metro — DC, Northern Virginia, Maryland suburbs
DMV_LOCATIONS = [
    "Washington, District of Columbia, United States",
    "Arlington, Virginia, United States",
    "Alexandria, Virginia, United States",
    "Fairfax, Virginia, United States",
    "Centreville, Virginia, United States",
    "Tysons, Virginia, United States",
    "Reston, Virginia, United States",
    "McLean, Virginia, United States",
    "Bethesda, Maryland, United States",
    "Rockville, Maryland, United States",
    "Silver Spring, Maryland, United States",
    "Annapolis, Maryland, United States",
]

# Decision maker titles across service businesses
DECISION_MAKER_TITLES = [
    "Founder", "Co-Founder", "Owner",
    "CEO", "President", "Managing Partner",
    "COO", "Chief Operating Officer",
    "General Manager", "VP Operations", "Operations Director",
    "Managing Director", "Executive Director",
]

# ── Segments ──────────────────────────────────────────────────────────────────
#
# Each segment = a cluster of businesses with the same operational pain.
# Pain signal: they're hiring for roles AI can eliminate.
# Mekaiel's pitch: "I see you're hiring X — I can build you that without the headcount."

SEGMENTS = {

    "professional_services": {
        "name": "Professional Services — DMV",
        "description": "Consultants, agencies, advisory firms drowning in admin",
        "pain_signal": "Hiring ops coordinators, admin assistants, project managers",
        "why_now": "High-revenue firms with budget, understaffed ops teams",
        "searches": [
            {
                "label": "Consulting & Advisory Firms (5-30 employees)",
                "q_keywords": "management consulting OR strategy consulting OR business advisory OR IT consulting OR federal consulting",
                "person_titles": DECISION_MAKER_TITLES,
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
            {
                "label": "Marketing & Creative Agencies (5-30 employees)",
                "q_keywords": "marketing agency OR creative agency OR digital marketing OR PR agency OR communications agency",
                "person_titles": DECISION_MAKER_TITLES,
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
            {
                "label": "HR & Recruiting Firms",
                "q_keywords": "staffing agency OR recruiting firm OR executive search OR talent acquisition OR HR consulting",
                "person_titles": DECISION_MAKER_TITLES,
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
        ]
    },

    "gov_contractors": {
        "name": "Government Contractors — DMV",
        "description": "Small GovCon firms with compliance overhead and ops chaos",
        "pain_signal": "Hiring program coordinators, contract administrators, proposal managers",
        "why_now": "High compliance burden, manual reporting, proposal grind — perfect for AI ops",
        "note": "Mekaiel's Pentagon/NATO background = instant credibility here",
        "searches": [
            {
                "label": "Small GovCon (10-50 employees)",
                "q_keywords": "government contractor OR federal contractor OR defense contractor OR government services OR DoD contractor",
                "person_titles": DECISION_MAKER_TITLES,
                "organization_num_employees_ranges": ["10,30", "31,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
            {
                "label": "IT & Cyber GovCon",
                "q_keywords": "cybersecurity consulting OR IT government services OR federal IT OR cleared IT OR SAIC OR Booz Allen type small firm",
                "person_titles": DECISION_MAKER_TITLES,
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
        ]
    },

    "legal": {
        "name": "Law Firms & Legal Services — DMV",
        "description": "Small-mid law firms with intake, scheduling, and admin bottlenecks",
        "pain_signal": "Hiring legal assistants, paralegals, intake coordinators",
        "why_now": "Manual intake, billable hour tracking, document chaos — high ROI on automation",
        "searches": [
            {
                "label": "Small Law Firms (5-30 attorneys)",
                "q_keywords": "law firm OR legal services OR attorney OR solicitor OR legal counsel",
                "person_titles": [
                    "Managing Partner", "Partner", "Founder", "Owner",
                    "Principal", "CEO", "President", "Office Manager",
                    "Director of Operations", "COO"
                ],
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
        ]
    },

    "healthcare_services": {
        "name": "Healthcare & Allied Health — DMV",
        "description": "Private practices, therapy groups, med spas with scheduling chaos",
        "pain_signal": "Hiring medical receptionists, schedulers, patient coordinators",
        "why_now": "Phone-heavy ops, no-show problem, intake forms — automatable and high-value",
        "searches": [
            {
                "label": "Private Practices & Clinics (5-30 employees)",
                "q_keywords": "medical practice OR dental practice OR therapy practice OR chiropractic OR physical therapy OR med spa OR dermatology",
                "person_titles": [
                    "Founder", "Owner", "CEO", "President",
                    "Practice Manager", "Managing Partner",
                    "Medical Director", "Clinical Director",
                    "COO", "Operations Manager"
                ],
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
        ]
    },

    "real_estate": {
        "name": "Real Estate & Property — DMV",
        "description": "Brokerages, property management, commercial RE firms",
        "pain_signal": "Hiring transaction coordinators, admin assistants, property managers",
        "why_now": "High transaction volume, manual follow-up, lead nurturing gaps",
        "searches": [
            {
                "label": "Real Estate Brokerages & Teams (5-30 employees)",
                "q_keywords": "real estate brokerage OR property management OR commercial real estate OR real estate team",
                "person_titles": [
                    "Founder", "Owner", "Broker", "Principal Broker",
                    "CEO", "President", "Managing Broker",
                    "Director of Operations", "General Manager"
                ],
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
        ]
    },

    "associations": {
        "name": "Associations & Nonprofits — DMV",
        "description": "Trade associations, nonprofits, membership orgs with thin ops teams",
        "pain_signal": "Hiring membership coordinators, event managers, admin staff",
        "why_now": "DC is the association capital of the world. Chronically understaffed ops.",
        "searches": [
            {
                "label": "Trade Associations & Membership Orgs",
                "q_keywords": "trade association OR industry association OR professional association OR membership organization OR chamber of commerce",
                "person_titles": [
                    "Executive Director", "CEO", "President",
                    "COO", "VP Operations", "Director of Operations",
                    "Managing Director", "Chief of Staff"
                ],
                "organization_num_employees_ranges": ["5,20", "21,50"],
                "organization_locations": DMV_LOCATIONS,
                "per_page": 50,
            },
        ]
    },

}

# ── Database ───────────────────────────────────────────────────────────────────

def init_leads_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS apollo_leads (
            id TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            full_name TEXT,
            title TEXT,
            linkedin_url TEXT,
            company TEXT,
            company_website TEXT,
            company_employees TEXT,
            company_city TEXT,
            company_state TEXT,
            company_linkedin TEXT,
            segment TEXT,
            search_label TEXT,
            score INTEGER DEFAULT 0,
            stage TEXT DEFAULT 'Target',
            email TEXT,
            phone TEXT,
            notes TEXT,
            collected_at TEXT
        )
    """)
    conn.commit()


def score_lead(person: dict, segment: str) -> int:
    """Score lead 1-3 based on ICP fit signals."""
    score = 1
    title = (person.get("title") or "").lower()
    employees = person.get("_employees", 0)

    # Founder/owner/CEO = direct decision maker, highest value
    top_titles = ["founder", "owner", "ceo", "president", "co-founder", "managing partner"]
    mid_titles = ["coo", "general manager", "vp operations", "operations director",
                  "managing director", "executive director", "chief of staff"]

    if any(t in title for t in top_titles):
        score = 3
    elif any(t in title for t in mid_titles):
        score = 2

    # Sweet spot: 5-20 employees — owner still the bottleneck, budget exists
    if 5 <= employees <= 20:
        score = min(score + 1, 3)

    # Gov contractors: Pentagon background = credibility bump
    if segment == "gov_contractors":
        score = min(score + 1, 3)

    return score


def save_person(conn, person: dict, segment: str, label: str):
    org = person.get("organization") or {}
    try:
        employees = int(org.get("estimated_num_employees") or 0)
    except (ValueError, TypeError):
        employees = 0

    person["_employees"] = employees
    score = score_lead(person, segment)

    try:
        conn.execute("""
            INSERT OR IGNORE INTO apollo_leads (
                id, first_name, last_name, full_name, title,
                linkedin_url, company, company_website,
                company_employees, company_city, company_state,
                company_linkedin, segment, search_label,
                score, stage, collected_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            person.get("id", ""),
            person.get("first_name", ""),
            person.get("last_name", ""),
            person.get("name", ""),
            person.get("title", ""),
            person.get("linkedin_url", ""),
            org.get("name", ""),
            org.get("website_url", ""),
            str(employees),
            org.get("city", ""),
            org.get("state", ""),
            org.get("linkedin_url", ""),
            segment,
            label,
            score,
            "Target",
            datetime.now(timezone.utc).isoformat(),
        ))
    except sqlite3.Error as e:
        print(f"  ⚠ DB error saving {person.get('name', '?')}: {e}")


# ── Apollo API ─────────────────────────────────────────────────────────────────

def search_apollo(search_config: dict, page: int = 1) -> dict:
    payload = {
        "api_key": APOLLO_API_KEY,
        "page": page,
        "per_page": search_config.get("per_page", 50),
    }
    for key in ["q_keywords", "person_titles", "organization_num_employees_ranges",
                "organization_locations", "q_organization_keyword_tags"]:
        if key in search_config:
            payload[key] = search_config[key]

    try:
        resp = requests.post(
            APOLLO_SEARCH_URL,
            json=payload,
            headers={"Content-Type": "application/json", "Cache-Control": "no-cache"},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError:
        return {"error": f"HTTP {resp.status_code}", "people": []}
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "people": []}


def run_search(search_config: dict, segment: str, pages: int, conn) -> dict:
    label = search_config["label"]
    total_saved = 0
    total_found = 0
    errors = []

    print(f"\n  → {label}")

    for page in range(1, pages + 1):
        result = search_apollo(search_config, page)

        if "error" in result:
            errors.append(result["error"])
            print(f"    Page {page}: ERROR — {result['error']}")
            break

        people = result.get("people", [])
        pagination = result.get("pagination", {})
        total_found = pagination.get("total_entries", 0)

        if not people:
            print(f"    Page {page}: No results")
            break

        for person in people:
            save_person(conn, person, segment, label)
            total_saved += 1

        print(f"    Page {page}: {len(people)} leads (total available: {total_found:,})")

        if page < pages:
            time.sleep(REQUEST_DELAY)

    return {"label": label, "total_found": total_found, "saved": total_saved, "errors": errors}


# ── CSV Export ─────────────────────────────────────────────────────────────────

def export_csv(conn, date_str: str) -> Path:
    cursor = conn.execute("""
        SELECT
            score, stage, segment, full_name, title,
            company, company_employees, company_city, company_state,
            company_website, linkedin_url, company_linkedin,
            search_label, email, phone, collected_at
        FROM apollo_leads
        ORDER BY score DESC, segment, CAST(company_employees AS INTEGER) DESC
    """)
    rows = cursor.fetchall()
    output_path = OUTPUT_DIR / f"apollo-leads-{date_str}.csv"
    headers = [
        "Score", "Stage", "Segment", "Full Name", "Title",
        "Company", "Employees", "City", "State",
        "Website", "LinkedIn (Person)", "LinkedIn (Company)",
        "Search Label", "Email", "Phone", "Collected At"
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    return output_path


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Apollo Lead Scraper — Arise Group DMV")
    parser.add_argument(
        "--segment",
        choices=list(SEGMENTS.keys()) + ["all"],
        default="all",
        help="Which segment to scrape (default: all)"
    )
    parser.add_argument(
        "--pages", type=int, default=2,
        help="Pages per search query (default: 2 = up to 100 leads per search)"
    )
    args = parser.parse_args()

    if not APOLLO_API_KEY:
        print("❌ APOLLO_API_KEY not set in .env — add it and re-run.")
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"\n{'='*60}")
    print(f"  Arise Group — Apollo Lead Scraper")
    print(f"  Geography: Washington DC / Northern Virginia / Maryland")
    print(f"  Strategy: Pain-signal targeting (admin/ops hiring = AI opportunity)")
    print(f"  {date_str} | {args.pages} pages/search")
    print(f"{'='*60}")

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    init_leads_table(conn)

    targets = list(SEGMENTS.keys()) if args.segment == "all" else [args.segment]
    all_stats = []

    for seg_key in targets:
        seg = SEGMENTS[seg_key]
        print(f"\n{'─'*60}")
        print(f"  SEGMENT: {seg['name']}")
        print(f"  Pain signal: {seg['pain_signal']}")
        print(f"  Why now: {seg['why_now']}")
        if seg_key == "gov_contractors":
            print(f"  ⭐ Pentagon/NATO background = credibility advantage")
        print(f"{'─'*60}")

        for search_config in seg["searches"]:
            stats = run_search(search_config, seg_key, args.pages, conn)
            all_stats.append(stats)
            time.sleep(REQUEST_DELAY)

    csv_path = export_csv(conn, date_str)

    print(f"\n{'='*60}")
    print(f"  RESULTS SUMMARY")
    print(f"{'='*60}")

    total_saved = 0
    for stat in all_stats:
        status = "✓" if not stat["errors"] else "✗"
        print(f"  {status} {stat['label']}")
        print(f"    Saved: {stat['saved']} | Available in Apollo: {stat['total_found']:,}")
        if stat["errors"]:
            for err in stat["errors"]:
                print(f"    Error: {err}")
        total_saved += stat["saved"]

    # Score breakdown
    cursor = conn.execute("""
        SELECT segment, score, COUNT(*) as count
        FROM apollo_leads
        GROUP BY segment, score
        ORDER BY segment, score DESC
    """)
    print(f"\n  LEAD SCORES BY SEGMENT")
    print(f"  {'Segment':<25} {'Score':<10} {'Count'}")
    print(f"  {'-'*45}")
    for row in cursor.fetchall():
        score_label = {3: "🔥 Hot", 2: "Warm", 1: "Cold"}.get(row["score"], str(row["score"]))
        print(f"  {row['segment']:<25} {score_label:<10} {row['count']}")

    conn.close()

    print(f"\n  CSV:   {csv_path}")
    print(f"  DB:    {DB_PATH}")
    print(f"  Total new leads: {total_saved}")
    print(f"\n  Hot leads (score 3) = call first. Warm = email. Cold = sequence.")
    print(f"  Next: python scripts/enrich_apollo.py to pull emails (uses credits)")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
