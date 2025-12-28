# agentic-module-leads

Scrape and verify sales leads via Apify, upload to Google Sheets.

## Features

- Scrape leads from Google Maps using Apify
- Verify lead relevance (>80% threshold)
- Upload verified leads to Google Sheets
- Supports multiple Apify actors

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-leads
```

## Setup

### Apify

1. Create an account at apify.com
2. Get your API token from Settings > Integrations
3. Add to `.env`:
   ```
   APIFY_TOKEN=apify_api_xxxxx
   ```

### Google Sheets (Optional)

1. Create OAuth credentials in Google Cloud Console
2. Download `credentials.json` to workspace root
3. Run `update_sheets.py` - it will prompt for authorization

## Slash Commands

```
/scrape-leads <industry> <location>
```

## CLI Usage

```bash
# Full workflow (test → verify → full scrape → upload)
./run tools/scrape_leads.py "Software" "San Francisco" 100

# Individual tools
./run tools/verify_leads.py .tmp/leads_test.json "Software"
./run tools/update_sheets.py .tmp/leads_full.json
```

## Workflow

1. **Test Run**: Scrapes 25 leads to validate search parameters
2. **Verification**: Checks if >80% match target industry
3. **Full Run**: If verification passes, scrapes full count
4. **Upload**: Pushes results to Google Sheets

## Supported Apify Actors

| Actor ID | Description | Plan |
|----------|-------------|------|
| `compass/crawler-google-places` | Google Maps scraper | Free tier |
| `code_crafter/leads-finder` | Lead finder | Paid only |
