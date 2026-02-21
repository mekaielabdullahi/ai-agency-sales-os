# Plotter Mechanix CSV Import Files

## Overview
These CSV files contain all tasks organized for the Phase 1 delivery, ready to import into your Notion databases.

## Files

### 1. epics.csv (10 records)
- All Epic-level parent tasks
- Includes the new Test Plan & Validation epic
- Status reflects current implementation state

### 2. tasks.csv (86 records)
- All Phase 1 tasks organized by Epic
- Includes:
  - ✅ 27 DONE tasks (already implemented)
  - 🔄 8 In Progress tasks
  - ⏸️ 2 Blocked tasks
  - 🆕 49 Not Started tasks (including critical gaps)
- Has Epic column to link to parent Epic after import

### 3. backlog.csv (26 records)
- All Phase 2+ items marked with [BACKLOG] prefix
- Organized by Phase (2, 3, 4, or TBD)
- Includes items from PRD, meetings, and discovery

## How to Import into Notion

1. **Import Epics first:**
   - Open your Epics database
   - Click "..." menu → Import → CSV
   - Select `epics.csv`
   - Map columns to your properties

2. **Import Tasks second:**
   - Open your Tasks database
   - Import `tasks.csv`
   - The Epic column contains the Epic name - you'll need to convert these to relations after import

3. **Import Backlog last:**
   - Open your Backlog database
   - Import `backlog.csv`

## Post-Import Steps

1. **Set up Epic relations:**
   - In Tasks database, convert the Epic column from Text to Relation
   - Link it to your Epics database
   - Notion should auto-match based on Epic names

2. **Configure Progress rollup:**
   - In Epics database, create a Rollup property
   - Relation: Tasks
   - Property: Status
   - Calculate: Percent checked (where Status = Done)

3. **Review critical items:**
   - Filter for Priority = Critical
   - Focus on OAuth token refresh and failover queue

## Task Counts by Epic

| Epic | Total | Done | In Progress | Not Started | Blocked |
|------|-------|------|-------------|-------------|---------|
| Communication Capture | 13 | 2 | 2 | 7 | 2 |
| AI Data Extraction | 4 | 4 | 0 | 0 | 0 |
| Transcription Quality | 3 | 0 | 0 | 3 | 0 |
| Jobber Integration | 8 | 5 | 1 | 2 | 0 |
| Request Routing Logic | 5 | 2 | 2 | 1 | 0 |
| Failover & Reliability | 5 | 2 | 0 | 3 | 0 |
| Monitoring & Alerting | 5 | 3 | 0 | 2 | 0 |
| Operational Config | 4 | 0 | 0 | 4 | 0 |
| Documentation & Training | 12 | 3 | 1 | 8 | 0 |
| Test Plan & Validation | 27 | 0 | 0 | 27 | 0 |
| **TOTAL** | **86** | **21** | **6** | **57** | **2** |

## Critical Gaps Highlighted

**Must address immediately:**
1. OAuth token auto-refresh (Jobber Integration) - FR24-25
2. Failover queue with retry (Failover & Reliability) - FR31-36
3. Request deduplication (Failover & Reliability) - FR35

**Contractual requirements:**
1. Training videos (Documentation & Training) - FR49
2. Live training session (Documentation & Training) - FR50

---

*Generated: January 14, 2026*
*Based on: Implementation review + PRD v1.1 + Jan 14 meeting*