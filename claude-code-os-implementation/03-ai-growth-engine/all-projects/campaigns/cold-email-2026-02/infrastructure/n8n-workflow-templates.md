# n8n Workflow Templates
## Automation for Lead Scraping & Enrichment
*Created: February 16, 2026*

---

## Overview

n8n is a free, self-hostable workflow automation tool. These templates automate lead scraping, enrichment, and signal detection.

**n8n Setup:** https://n8n.io/ (free self-hosted) or https://n8n.cloud (free tier available)

---

## Workflow 1: Apollo to Airtable (One-Click Lead Scraping)

**Template URL:** https://n8n.io/workflows/3435-get-qualified-leads-in-one-click-from-apollo-to-airtable/

### What It Does
1. Triggers manually or on schedule
2. Runs Apollo People Search API with your filters
3. Filters results by title, company size
4. Adds qualified leads to Airtable base
5. Deduplicates existing leads

### Setup Steps
1. Import workflow from URL above
2. Add Apollo API key to HTTP Request node
3. Connect Airtable credentials
4. Customize Apollo search filters
5. Run!

### Node Configuration
```
[Manual Trigger]
    → [HTTP Request: Apollo Search]
    → [Filter: Title Match]
    → [Airtable: Create Record]
```

---

## Workflow 2: LinkedIn Lead Enrichment Pipeline

**Template URL:** https://n8n.io/workflows/8409-automated-linkedin-lead-enrichment-pipeline-using-apolloio-and-google-sheets/

### What It Does
1. Reads LinkedIn URLs from Google Sheet
2. Enriches each URL via Apollo
3. Gets email, company data, activity signals
4. Writes enriched data back to sheet
5. Flags incomplete records

### Setup Steps
1. Import workflow from URL above
2. Add Google Sheets credentials
3. Add Apollo API key
4. Create sheet with column: `linkedin_url`
5. Run!

### Node Configuration
```
[Google Sheets: Read]
    → [Loop: Each Row]
    → [HTTP Request: Apollo Enrich]
    → [Google Sheets: Update Row]
```

---

## Workflow 3: Hiring Signals from LinkedIn Jobs

**Template URL:** https://n8n.io/workflows/3580-scrape-linkedin-job-listings-for-hiring-signals-and-prospecting-with-bright-data/

### What It Does
1. Takes list of target company LinkedIn pages
2. Scrapes their job postings via Bright Data
3. Identifies hiring signals:
   - Hiring technicians = capacity constrained
   - Hiring admin = operations overwhelmed
   - Multiple openings = growth mode
4. Flags high-priority leads

### Setup Steps
1. Import workflow from URL above
2. Sign up for Bright Data (free tier available)
3. Add Bright Data credentials to workflow
4. Input company LinkedIn URLs
5. Run!

### Signal Interpretation
| Job Type | Signal | Priority |
|----------|--------|----------|
| Technician/Field Service | Capacity constrained | HIGH |
| Admin/Operations | Overwhelmed | HIGH |
| Sales/Marketing | Growth mode | MEDIUM |
| Multiple roles | Scaling fast | HIGH |

---

## Workflow 4: Apollo + Apify Combined Enrichment

**Template URL:** https://n8n.io/workflows/9057-automate-apollo-lead-scraping-and-email-enrichment-to-airtable-crm-with-apify/

### What It Does
1. Runs Apollo search for leads
2. For leads missing emails, runs Apify CEO Finder
3. Scrapes company website for contact info
4. Combines data from both sources
5. Outputs fully enriched leads

### Setup Steps
1. Import workflow from URL above
2. Add Apollo API key
3. Add Apify API key
4. Configure Airtable destination
5. Run!

### Node Configuration
```
[Apollo Search]
    → [Filter: Missing Email]
    → [Apify: CEO Finder]
    → [Merge Results]
    → [Airtable: Create/Update]
```

---

## Custom Workflow: Printing Vertical Scraper

Build this custom workflow for printing leads:

### Workflow Diagram
```
┌─────────────────┐
│ Manual Trigger  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Apollo Search   │ ── Printing vertical query
│ (HTTP Request)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Filter Results  │ ── Title: Founder/Owner/CEO
│                 │ ── Size: 5-20 employees
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Apify CEO Finder│ ── Get emails from websites
│ (HTTP Request)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Hunter Verify   │ ── Verify email deliverability
│ (HTTP Request)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Google Sheets   │ ── Output to tracking sheet
│ (Append Row)    │
└─────────────────┘
```

### Apollo Node Settings
```json
{
  "url": "https://api.apollo.io/v1/mixed_people/search",
  "method": "POST",
  "body": {
    "api_key": "={{$credentials.apolloApi.apiKey}}",
    "q_keywords": "large format printer OR wide format OR plotter",
    "person_titles": ["Founder", "Owner", "CEO"],
    "organization_num_employees_ranges": ["1,10", "11,20"],
    "organization_locations": ["United States"],
    "per_page": 25
  }
}
```

---

## Scheduling Recommendations

| Workflow | Frequency | Best Time |
|----------|-----------|-----------|
| Apollo Search | Weekly | Monday 9am |
| Email Enrichment | After search | Monday 10am |
| Hiring Signals | Weekly | Monday 11am |
| Verification | Before outreach | Tuesday 9am |

---

## Credential Storage

Store these credentials in n8n:

| Credential Name | Service | Required For |
|-----------------|---------|--------------|
| `apolloApi` | Apollo.io | Search + Enrichment |
| `apifyApi` | Apify | CEO Finder |
| `hunterApi` | Hunter.io | Email verification |
| `googleSheets` | Google | Data storage |
| `airtableApi` | Airtable | CRM integration |
| `brightData` | Bright Data | LinkedIn scraping |

---

## Error Handling

Add these error handlers to each workflow:

1. **Rate Limit Handler**
   - If 429 error, wait 60 seconds and retry
   - Max 3 retries

2. **Missing Data Handler**
   - If email not found, flag for manual lookup
   - Continue to next record

3. **API Error Handler**
   - Log error details
   - Send Slack notification
   - Continue processing

---

## Related Files

- `lead-scraping-stack.md` - Full tools documentation
- `apollo-queries.md` - Specific API queries
- `../leads/cold-leads-2026-02-16.md` - Output destination
