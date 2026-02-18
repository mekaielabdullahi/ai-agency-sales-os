# Apollo API Search Queries
## Ready-to-Use Queries for Lead Scraping
*Created: February 16, 2026*
*Updated: February 16, 2026 - Expanded to 1-50 employees*

---

## Overview

These queries use Apollo's **People Search API** which is **FREE** (no credits required). Only enrichment (getting emails) costs credits.

**Base URL:** `https://api.apollo.io/v1/mixed_people/search`

---

## Company Size Targeting

| Segment | Employees | Revenue Range | Decision Maker | Priority |
|---------|-----------|---------------|----------------|----------|
| Micro | 1-10 | $100K-$1M | Owner/Founder | HIGH |
| Small | 11-20 | $500K-$3M | Owner/CEO | HIGH |
| Small-Mid | 21-50 | $1M-$10M | CEO, GM, VP Ops | MEDIUM (test) |

**Why 1-50:** Owner/GM still accessible. Decision-maker reachable without gatekeepers. Sales cycle remains short (1-2 calls).

---

## Printing Vertical Query

### Basic Search (1-20 Employees - Proven ICP)
```json
{
  "api_key": "YOUR_API_KEY",
  "q_keywords": "large format printer OR wide format OR plotter service OR designjet",
  "person_titles": [
    "Founder",
    "Owner",
    "CEO",
    "President",
    "General Manager",
    "Operations Manager"
  ],
  "organization_num_employees_ranges": ["1,10", "11,20"],
  "organization_locations": ["United States"],
  "page": 1,
  "per_page": 25
}
```

### Expanded Search (1-50 Employees - Full Range)
```json
{
  "api_key": "YOUR_API_KEY",
  "q_keywords": "printer repair OR plotter maintenance OR canon imageprograf OR hp designjet OR epson surecolor OR wide format graphics",
  "person_titles": [
    "Founder",
    "Owner",
    "CEO",
    "President",
    "COO",
    "Co-Founder",
    "Managing Partner",
    "General Manager",
    "VP Operations",
    "Operations Director",
    "Service Manager"
  ],
  "organization_num_employees_ranges": ["1,10", "11,20", "21,50"],
  "organization_locations": ["United States"],
  "q_organization_keyword_tags": ["printing", "graphics", "signage", "wide format", "plotter", "designjet"],
  "page": 1,
  "per_page": 50
}
```

### 21-50 Employee Segment (Test Market)
```json
{
  "api_key": "YOUR_API_KEY",
  "q_keywords": "large format printer OR wide format OR plotter service",
  "person_titles": [
    "CEO",
    "President",
    "COO",
    "VP Operations",
    "General Manager",
    "Operations Director"
  ],
  "organization_num_employees_ranges": ["21,50"],
  "organization_locations": ["United States"],
  "q_organization_keyword_tags": ["printing", "graphics", "signage"],
  "page": 1,
  "per_page": 25
}
```

**Expanded Titles for 21-50 Segment:**
- VP Operations, COO - Common in growing service businesses
- General Manager - Often the decision-maker when owner is hands-off
- Operations Director - Handles vendor/tool decisions

### By Industry (NAICS Codes)
```json
{
  "api_key": "YOUR_API_KEY",
  "organization_industry_tag_ids": ["commercial printing", "printing services"],
  "person_titles": ["Founder", "Owner", "CEO"],
  "organization_num_employees_ranges": ["1,10", "11,20"],
  "organization_locations": ["United States"],
  "page": 1,
  "per_page": 25
}
```

---

---

## cURL Examples

### Printing Vertical - Full Range (1-50 Employees)
```bash
curl --request POST \
  --url 'https://api.apollo.io/v1/mixed_people/search' \
  --header 'Content-Type: application/json' \
  --header 'Cache-Control: no-cache' \
  --data '{
    "api_key": "YOUR_API_KEY",
    "q_keywords": "large format printer OR wide format OR plotter service",
    "person_titles": ["Founder", "Owner", "CEO", "President", "COO", "VP Operations", "General Manager"],
    "organization_num_employees_ranges": ["1,10", "11,20", "21,50"],
    "organization_locations": ["United States"],
    "per_page": 50
  }'
```

### Printing Vertical - Priority Segment (1-20 Employees)
```bash
curl --request POST \
  --url 'https://api.apollo.io/v1/mixed_people/search' \
  --header 'Content-Type: application/json' \
  --header 'Cache-Control: no-cache' \
  --data '{
    "api_key": "YOUR_API_KEY",
    "q_keywords": "large format printer OR wide format OR plotter service",
    "person_titles": ["Founder", "Owner", "CEO", "President"],
    "organization_num_employees_ranges": ["1,10", "11,20"],
    "organization_locations": ["United States"],
    "per_page": 25
  }'
```

---

## Email Enrichment Query (1 Credit Each)

Once you have LinkedIn URLs from the search, enrich to get emails:

```bash
curl --request POST \
  --url 'https://api.apollo.io/v1/people/match' \
  --header 'Content-Type: application/json' \
  --header 'Cache-Control: no-cache' \
  --data '{
    "api_key": "YOUR_API_KEY",
    "linkedin_url": "https://www.linkedin.com/in/example-person",
    "reveal_personal_emails": false
  }'
```

---

## Expected Response Format

```json
{
  "people": [
    {
      "id": "abc123",
      "first_name": "John",
      "last_name": "Smith",
      "name": "John Smith",
      "linkedin_url": "https://www.linkedin.com/in/johnsmith",
      "title": "Founder & CEO",
      "organization": {
        "name": "Print Solutions Inc",
        "website_url": "printsolutions.com",
        "linkedin_url": "https://linkedin.com/company/print-solutions",
        "estimated_num_employees": 12,
        "city": "Phoenix",
        "state": "Arizona"
      }
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 25,
    "total_entries": 150,
    "total_pages": 6
  }
}
```

---

## Processing the Results

### Step 1: Export to CSV
From Apollo response, extract:
- `first_name`
- `last_name`
- `title`
- `organization.name`
- `organization.website_url`
- `organization.estimated_num_employees`
- `linkedin_url`
- `organization.city`, `organization.state`

### Step 2: Segment by Company Size
| Segment | Employees | Priority | Action |
|---------|-----------|----------|--------|
| Micro | 1-10 | HIGH | Enrich immediately |
| Small | 11-20 | HIGH | Enrich immediately |
| Small-Mid | 21-50 | MEDIUM | Test batch (10 max) |

### Step 3: Prioritize for Enrichment
Score leads by:
- Segment (1-20 = high priority, 21-50 = test)
- Title match (Founder/Owner = high priority)
- Company size (5-15 employees = sweet spot within segment)
- Has website (needed for personalization)

### Step 4: Enrich by Segment
**Priority Batch (1-20 employees):**
- Printing: Enrich 40 leads

**Test Batch (21-50 employees):**
- Printing: Enrich up to 20 leads

Use remaining Apollo credits or Hunter.io for email enrichment on highest-scored leads.

---

## Rate Limits

| Endpoint | Rate Limit |
|----------|------------|
| People Search | 20 requests/minute |
| People Enrich | 50 requests/minute |
| Organization Enrich | 50 requests/minute |

**Recommendation:** Add 3-second delay between requests to stay safe.

---

## Related Files

- `lead-scraping-stack.md` - Full tools documentation
- `n8n-workflow-templates.md` - Automation workflows
- `../leads/cold-leads-2026-02-16.md` - Output destination
