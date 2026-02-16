# Lead Scraping Stack
## Free API Tools for Cold Email Campaigns
*Created: February 16, 2026*
*Updated: February 16, 2026 - Expanded to 1-50 employees, 3x addressable market*

---

## Overview

This document outlines the free-tier API tools stack for finding decision-makers (founders, owners, ops people) at **small and mid-market companies (1-50 employees)**, plus tracking their recent activities/hiring signals.

### Company Size Targeting

| Segment | Employees | Revenue Range | Decision Maker |
|---------|-----------|---------------|----------------|
| Micro | 1-10 | $100K-$1M | Owner/Founder |
| Small | 11-20 | $500K-$3M | Owner/CEO |
| Small-Mid | 21-50 | $1M-$10M | CEO, GM, VP Ops |

**Why 1-50:** Owner/GM still accessible. Decision-maker reachable without gatekeepers. Sales cycle remains short (1-2 calls).

---

## Tier 1: Primary Tools (Use First)

### Apollo.io
| Attribute | Value |
|-----------|-------|
| **Free Tier** | 600 email credits/month |
| **Best For** | People search by job title, founder filter |
| **Key Feature** | People API Search is FREE (no credits), only enrichment costs credits |
| **Signup URL** | https://www.apollo.io/sign-up |

**API Endpoints:**
- `/people/search` - FREE, no credits required
- `/people/match` - 1 credit per enrichment
- `/organizations/enrich` - 1 credit per company

### Apify
| Attribute | Value |
|-----------|-------|
| **Free Tier** | $5/month in credits |
| **Best For** | CEO Finder, LinkedIn scraper, Leads Finder |
| **Key Feature** | 100 leads/run free, CEO Finder extracts founders from websites |
| **Signup URL** | https://apify.com/sign-up |

**Useful Actors:**
- `apify/google-search-scraper` - $0.50 per 1000 results
- `lukaskrivka/contact-info-scraper` - Finds CEO/founder from websites
- `forward_email/website-email-scraper` - Extract emails from company pages

### Hunter.io
| Attribute | Value |
|-----------|-------|
| **Free Tier** | 25 searches + 50 verifications/month |
| **Best For** | Email verification, domain search |
| **Key Feature** | Verify emails found elsewhere |
| **Signup URL** | https://hunter.io/users/sign_up |

**API Endpoints:**
- `GET /v2/domain-search` - Find emails at a domain
- `GET /v2/email-finder` - Find specific person's email
- `GET /v2/email-verifier` - Verify email deliverability

---

## Tier 2: Enrichment & Waterfall

### Clay.com
| Attribute | Value |
|-----------|-------|
| **Free Tier** | 100 credits/month |
| **Best For** | Waterfall enrichment (100+ providers) |
| **Key Feature** | If Apollo misses, tries Clearbit, Hunter, etc. automatically |
| **Signup URL** | https://www.clay.com/signup |

### GetProspect
| Attribute | Value |
|-----------|-------|
| **Free Tier** | 50 credits/month |
| **Best For** | Bulk CSV enrichment with emails/phones |
| **Signup URL** | https://getprospect.com/signup |

### Prospeo
| Attribute | Value |
|-----------|-------|
| **Free Tier** | 75 free emails |
| **Best For** | Email finder from name + domain |
| **Signup URL** | https://prospeo.io/ |

### Skrapp.io
| Attribute | Value |
|-----------|-------|
| **Free Tier** | 100 searches/month |
| **Best For** | LinkedIn email extraction |
| **Signup URL** | https://skrapp.io/register |

---

## Tier 3: Activity & Signals

### Apify LinkedIn Post Scraper
| Attribute | Value |
|-----------|-------|
| **Free Tier** | Part of $5 Apify credits |
| **Best For** | Recent posts from founders (engagement, topics) |
| **Actor** | `apify/linkedin-posts-scraper` |

### n8n + Bright Data Workflow
| Attribute | Value |
|-----------|-------|
| **Free Tier** | n8n self-hosted is free |
| **Best For** | Hiring signals from LinkedIn job posts |
| **Workflow** | See n8n-workflow-templates.md |

### ScrapIn
| Attribute | Value |
|-----------|-------|
| **Free Tier** | Limited free tier |
| **Best For** | Real-time LinkedIn activity without cookies |
| **Signup URL** | https://scrapin.io/ |

---

## Monthly Credit Budget (Updated for 1-50 Employee Range)

| Tool | Monthly Free | Your Usage | Remaining |
|------|--------------|------------|-----------|
| Apollo (search) | Unlimited | 0 | Unlimited |
| Apollo (enrich) | 600 credits | ~60 enrichments | 540 |
| Apify | $5 (~200 leads) | 60 leads | $3.50 remaining |
| Hunter | 25 searches + 50 verifications | 30 verifications | 45 |
| Clay | 100 credits | 20 enrichments | 80 |
| GetProspect | 50 credits | Backup only | 50 |
| **Total Leads Possible** | **~150/month** | **60 this week** | **90 remaining** |

**Note:** Expanded 1-50 range increases addressable market by ~3x, allowing higher weekly targets.

### Weekly Target Breakdown

| Vertical | 1-20 Employees (Priority) | 21-50 Employees (Test) | Total |
|----------|---------------------------|------------------------|-------|
| Printing | 25 leads | 10 leads | 35 |
| Homestead | 15 leads | 10 leads | 25 |
| **Weekly Total** | **40** | **20** | **60** |

---

## Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│              LEAD SCRAPING PIPELINE (1-50 EMPLOYEES)         │
└─────────────────────────────────────────────────────────────┘

Step 1: DISCOVERY (Free)
┌──────────────────┐
│ Apollo People    │ ──► Names, Titles, Companies, LinkedIn URLs
│ Search API       │     Employee count, location
│ (No credits)     │     (No email yet - FREE)
└──────────────────┘

Step 2: SEGMENT BY SIZE
┌──────────────────┐
│ 1-20 employees   │ ──► HIGH PRIORITY - Proven ICP
│ (Priority batch) │     Enrich immediately
├──────────────────┤
│ 21-50 employees  │ ──► MEDIUM PRIORITY - Test market
│ (Test batch)     │     Limit to 10/vertical
└──────────────────┘

Step 3: FOUNDER EXTRACTION (Low Cost)
┌──────────────────┐
│ Apify CEO Finder │ ──► Founder names from /about, /team pages
│ ($0.02/page)     │     Email patterns, social links
└──────────────────┘

Step 4: EMAIL ENRICHMENT (Credits)
┌──────────────────┐     ┌──────────────────┐
│ Apollo Enrich    │ OR  │ Hunter.io        │ ──► Verified Email
│ (1 credit/lead)  │     │ (1 credit/lead)  │
└──────────────────┘     └──────────────────┘

Step 5: WATERFALL (If needed)
┌──────────────────┐
│ Clay.com         │ ──► Tries 100+ providers until email found
│ (1 credit/lead)  │
└──────────────────┘

Step 6: SIGNALS (Optional)
┌──────────────────┐
│ n8n + LinkedIn   │ ──► Hiring signals, recent activity
│ (Free workflow)  │
└──────────────────┘

                         ▼
              ┌──────────────────┐
              │   ENRICHED LEAD  │
              │ ─────────────── │
              │ Name            │
              │ Title           │
              │ Company         │
              │ Employees       │
              │ Segment (1-20/  │
              │   21-50)        │
              │ Verified Email  │
              │ LinkedIn URL    │
              │ Hiring Signal   │
              │ Recent Activity │
              └──────────────────┘
```

---

## Quick Start

1. Sign up for accounts (see URLs above)
2. Get API keys from each service
3. Store keys in `.env` file (never commit!)
4. Run Apollo search queries (see `apollo-queries.md`)
5. Enrich top leads with Apollo/Hunter
6. Import to CRM or Google Sheets

---

## Related Files

- `apollo-queries.md` - Specific search queries for each vertical
- `n8n-workflow-templates.md` - Automation workflows
- `../leads/cold-leads-2026-02-16.md` - Output destination
