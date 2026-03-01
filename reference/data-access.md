# Data Access Reference

> Load this file when you need to query the database or understand the data pipeline.

## SQLite Data Warehouse

**Location:** `data/data.db`
**Connect:** `sqlite3.connect("data/data.db")` (Python sqlite3 module)
**Claude can run SQL directly** in sessions via Python.

## Connected Data Sources

| Source | Table(s) | Collection Script | What It Tracks |
|--------|----------|-------------------|----------------|
| Fireflies | `meetings` | `scripts/intel/collect_fireflies.py` | Meeting transcripts, summaries, action items |
| Slack | `slack_messages` | `scripts/intel/collect_slack.py` | Team messages (not yet configured) |
| Google Analytics | `ga4_daily`, `ga4_sources` | `scripts/collect_google_analytics.py` | Website sessions, users, page views, traffic sources |
| Lead Tracker | `leads` | `scripts/collect_leads.py` | Sales pipeline from Google Sheets |
| FX Rates | `fx_rates` | `scripts/collect_fx_rates.py` | Daily exchange rates from USD (ECB data) |

## Table Schemas

### fx_rates
| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Date of the rate (YYYY-MM-DD) |
| currency | TEXT | Target currency code (EUR, GBP, etc.) |
| rate | REAL | Exchange rate from USD |
| base | TEXT | Base currency (always USD) |
| collected_at | TEXT | UTC timestamp when collected |

**Primary key:** (date, currency)

### ga4_daily
| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Date of the snapshot (YYYY-MM-DD) |
| sessions | INTEGER | Total sessions |
| total_users | INTEGER | Total unique users |
| new_users | INTEGER | First-time visitors |
| page_views | INTEGER | Total page views |
| avg_session_duration | REAL | Average session length in seconds |
| bounce_rate | REAL | Bounce rate (0-1) |
| engagement_rate | REAL | Engagement rate (0-1) |
| collected_at | TEXT | UTC timestamp when collected |

**Primary key:** date

### ga4_sources
| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Date of the snapshot (YYYY-MM-DD) |
| source | TEXT | Traffic source (google, direct, etc.) |
| medium | TEXT | Traffic medium (organic, cpc, referral, etc.) |
| sessions | INTEGER | Sessions from this source |
| users | INTEGER | Users from this source |

**Primary key:** (date, source, medium)

### leads
| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Date lead was added |
| name | TEXT | Contact name |
| company | TEXT | Company name |
| source | TEXT | Where the lead came from (LinkedIn, referral, etc.) |
| status | TEXT | Pipeline stage (New, Contacted, Discovery, Proposal, Won, Lost) |
| service | TEXT | Service interested in (AI Sprint, Website Dev, AI Twin) |
| value | TEXT | Estimated deal value |
| notes | TEXT | Additional context |
| collected_at | TEXT | UTC timestamp when collected |

**Primary key:** (name, company)

### meetings (IntelOS)
| Column | Type | Description |
|--------|------|-------------|
| meeting_id | TEXT | Unique ID (e.g. fireflies_abc123) |
| source | TEXT | Recording service (fireflies, fathom, custom) |
| title | TEXT | Meeting title |
| date | TEXT | Meeting date (YYYY-MM-DD) |
| start_time | TEXT | Start time (HH:MM:SS) |
| duration_minutes | INTEGER | Length in minutes |
| participants | TEXT | JSON array of {name, email} |
| transcript_text | TEXT | Full transcript text |
| summary | TEXT | AI-generated summary |
| action_items_raw | TEXT | JSON array of action items |
| stream | TEXT | Department/stream classification |
| call_type | TEXT | team_meeting, one_on_one, external, meeting |
| classified_at | TEXT | When classification ran |
| external_url | TEXT | Link to recording in source platform |
| collected_at | TEXT | UTC timestamp when collected |

**Primary key:** meeting_id

### slack_messages (IntelOS)
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Auto-increment ID |
| workspace | TEXT | Slack workspace name |
| channel_id | TEXT | Channel ID |
| channel_name | TEXT | Channel name |
| user_id | TEXT | Sender user ID |
| user_name | TEXT | Sender display name |
| ts | TEXT | Slack timestamp (unique per message) |
| thread_ts | TEXT | Parent thread timestamp |
| message_type | TEXT | Message type (default: message) |
| text | TEXT | Message content |
| has_files | INTEGER | Whether message has file attachments |
| reactions | TEXT | JSON of reactions |
| reply_count | INTEGER | Number of thread replies |
| collected_at | TEXT | UTC timestamp when collected |

**Unique key:** (workspace, channel_id, ts)

### staff_registry (IntelOS)
| Column | Type | Description |
|--------|------|-------------|
| email | TEXT | Team member email |
| name | TEXT | Display name |
| role | TEXT | Job role |
| team | TEXT | Team name |
| department | TEXT | Department for classification |
| is_active | INTEGER | 1 = active, 0 = inactive |
| added_at | TEXT | When added to registry |

**Primary key:** email

### collection_log
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Auto-increment ID |
| collected_at | TEXT | UTC timestamp of collection run |
| source | TEXT | Collector name (e.g., "fx_rates") |
| status | TEXT | "success", "skipped", "error", "exception" |
| reason | TEXT | Error message if failed, skip reason if skipped |
| records_written | INTEGER | Number of records written |

## Common Queries

```sql
-- Search meeting transcripts
SELECT title, date, substr(transcript_text, 1, 200) FROM meetings
WHERE transcript_text LIKE '%budget%' ORDER BY date DESC;

-- Find meetings with a specific person
SELECT title, date, summary FROM meetings
WHERE participants LIKE '%jimmy%' ORDER BY date DESC LIMIT 5;

-- Recent meetings
SELECT date, title, duration_minutes, stream FROM meetings ORDER BY date DESC LIMIT 10;

-- Website traffic trend (last 7 days)
SELECT date, sessions, total_users, page_views FROM ga4_daily ORDER BY date DESC LIMIT 7;

-- Top traffic sources (latest day)
SELECT source, medium, sessions FROM ga4_sources
WHERE date = (SELECT MAX(date) FROM ga4_sources) ORDER BY CAST(sessions AS INTEGER) DESC;

-- Lead pipeline summary
SELECT status, COUNT(*) as count FROM leads GROUP BY status ORDER BY count DESC;

-- Recent leads
SELECT date, name, company, status, service FROM leads ORDER BY date DESC LIMIT 10;

-- Latest rates for all currencies
SELECT * FROM fx_rates WHERE date = (SELECT MAX(date) FROM fx_rates) ORDER BY currency;

-- Collection run history
SELECT * FROM collection_log ORDER BY collected_at DESC LIMIT 10;

-- Check data freshness across all tables
SELECT source, MAX(collected_at) as last_run, status FROM collection_log GROUP BY source;
```

## Data Collection

**Run all collectors:** `python scripts/collect.py`
**Run specific source:** `python scripts/collect.py --sources fx_rates`
**Override date:** `python scripts/collect.py --date 2026-03-01`
**Regenerate metrics only:** `python scripts/generate_metrics.py`
**Logs:** `data/collect.log` (when running via cron/scheduler)

## Adding New Collectors

1. Create `scripts/collect_NAME.py` following the pattern: `collect() -> dict`, `write(conn, result, date) -> int`
2. The orchestrator (`collect.py`) auto-discovers any `collect_*.py` file
3. Add a section function to `scripts/generate_metrics.py`
4. Update this reference doc with the new table schema

## Notes

- **Snapshot strategy:** Most APIs give current totals, not deltas. We take daily snapshots and calculate changes by comparing dates.
- **Graceful degradation:** Missing credentials = that collector is skipped. Pipeline never fully breaks.
- **Example collectors** in `scripts/examples/` for: YouTube, Stripe, GA4, Google Sheets, Bitly.
