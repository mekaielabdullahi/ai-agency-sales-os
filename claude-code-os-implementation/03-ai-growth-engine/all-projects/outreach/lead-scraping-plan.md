# Arise Group — Lead Scraping Plan
**Last Updated: March 2026**

---

## Ideal Client Profile (ICP)

### Primary Target
| Criteria | Details |
|----------|---------|
| **Business Type** | Service business (agency, consulting, professional services) |
| **Revenue** | $1M–$10M annually |
| **Team Size** | 5–50 employees |
| **Decision Maker** | Founder / CEO / Operations Director |
| **Geography** | North America (US + Canada primary) |
| **Pain Profile** | Manual ops, repetitive admin, team bottlenecks, scaling issues |
| **AI Readiness** | Knows AI exists, hasn't systematized it yet |
| **Budget Signal** | $5K–$20K project capacity |

### Secondary Target
- Marketing agencies
- Real estate brokerages / property management
- Trades businesses scaling past $2M
- Recruitment / staffing firms
- Logistics / supply chain SMBs

### Exclusions (Don't Waste Time)
- Solo freelancers / no team
- Enterprise (>500 employees)
- Pure retail / ecommerce
- Businesses with no digital presence

---

## Pain Signals to Look For

When scraping or researching — these are buying signals:

**On LinkedIn:**
- Posts about being overwhelmed, burning out, or "wearing too many hats"
- Hiring posts for admin, ops, or coordinator roles
- Posts about failed software implementations
- Comments asking "how do you use AI in your business?"
- Sharing content about productivity, automation, or AI tools

**On their website:**
- "We're growing" or "we're hiring" sections
- No mention of systems or processes
- Generic service pages with no differentiation

**On job boards (Indeed, LinkedIn Jobs):**
- Posting for repetitive roles (data entry, admin, scheduler, coordinator)
- Job descriptions that describe manual processes
- Multiple open roles = scaling pains

---

## Lead Sources

### Tier 1 — Highest Intent

**1. Apollo.io** *(Recommended — best B2B database)*
- Filter: Industry + company size + job title
- Export CSV: Name, company, email, LinkedIn URL, phone
- Cost: Free plan (50 leads/month) → $49/mo for 1,000 credits
- ICP filters:
  - Industry: Marketing, Consulting, Professional Services, Real Estate, Staffing
  - Employees: 5–100
  - Revenue: $1M–$20M
  - Title: Founder, CEO, Owner, President, Operations Director

**2. LinkedIn Sales Navigator** *(Best for warm + personalized)*
- Filter: 2nd connections, industry, company size, geography
- Save searches, get weekly lead alerts
- Use for warm outreach (connection requests first)
- Cost: ~$99/mo

**3. LinkedIn Organic Search (Free)**
- Search: "[Industry] owner" or "[Industry] CEO" + location
- Filter by 2nd degree connections
- 25-30 targeted searches/day (free limit)

---

### Tier 2 — Supplemental

**4. Local Business Directories**
- Google Maps: Search "[industry] [city]" → scrape names/contacts
- Chamber of Commerce member directories
- BNI chapter member lists (networking groups)
- Use for door knocking + cold call targeting

**5. Clutch.co / G2**
- Find agencies + consultancies with active profiles
- Shows: Company size, revenue, contact info, reviews
- Good for targeting other agencies as clients

**6. Job Boards (Intent Signals)**
- Indeed / LinkedIn Jobs: Search for "operations coordinator" or "executive assistant" postings
- These companies are hiring for roles we can automate → hot leads
- Get: Company name → find founder on LinkedIn → scrape email via Apollo

**7. Fireflies / Meeting Data (Internal)**
- Search your 234 meeting transcripts for past warm contacts
- Run: `python scripts/intel/db.py` search for "follow up" or "interested"
- These are the hottest leads — they already know you

---

## Scraping Workflow

### Weekly Lead Pull (30-40 leads/week)

**Monday — Scrape & Qualify**
1. Pull 50 leads from Apollo (apply ICP filters)
2. Verify emails (use Apollo's built-in verification or NeverBounce)
3. Quick LinkedIn check on each — flag any pain signals
4. Drop into tracking sheet with initial score

**Tuesday-Friday — Outreach**
- Cold email: 20-30/day
- Cold calls: Pass list to caller with notes
- LinkedIn: 5-10 connection requests + DMs to warm leads

---

## Lead Scoring (Quick Filter)

Score each lead 1-3 before reaching out:

| Score | Criteria |
|-------|----------|
| **3 — Hot** | Pain signal found, right size, decision maker confirmed, warm connection |
| **2 — Warm** | Fits ICP, no clear signal, but reachable |
| **1 — Cold** | Fits ICP on paper, no other signal, lower priority |

Prioritize 3s first, then 2s. Don't waste time on 1s until you've exhausted 3s and 2s.

---

## Email Finding Stack

| Tool | Cost | Best For |
|------|------|---------|
| **Apollo.io** | Free–$49/mo | Bulk scraping with emails |
| **Hunter.io** | Free (25/mo) | Find email by name + domain |
| **Snov.io** | Free tier | Email finder + verifier |
| **RocketReach** | $39/mo | Hard-to-find executives |
| **LinkedIn + guess** | Free | [first].[last]@company.com |

**Email pattern guessing:**
- Try: firstname@company.com
- Try: firstname.lastname@company.com
- Verify with Hunter or NeverBounce before sending

---

## Weekly Lead Target

| Channel | Weekly Volume | Source |
|---------|--------------|--------|
| Cold Email | 100-150 contacts | Apollo export |
| Cold Call | 50-80 dials | Apollo + local directories |
| LinkedIn DM | 20-30 messages | LinkedIn organic + Sales Nav |
| Warm Outreach | 5-10 contacts | Fireflies + personal network |
| **Total** | **175-270 touches/week** | |

---

## Data Quality Rules

Before any lead goes into outreach:
- [ ] Email verified (not guessed)
- [ ] Decision maker confirmed (not gatekeeper)
- [ ] Company still active (website loads, LinkedIn active)
- [ ] Fits at least 3 ICP criteria
- [ ] Not a competitor or existing client

---

## Tools Summary

**Minimum setup (free/low cost):**
- Apollo.io free plan — lead scraping
- Hunter.io free plan — email finding
- Google Sheets — tracking
- Gmail — cold email (manual)

**Recommended setup ($150-200/mo):**
- Apollo.io Basic ($49) — 1,000 credits/mo
- Instantly.ai ($37) — cold email sending + warmup
- LinkedIn Sales Navigator ($99) — warm lead targeting

---

*Connect Apollo → Instantly for semi-automated cold email flow once volume justifies it.*
