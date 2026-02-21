# Cold Leads - February 16, 2026
## Lead Scraping Execution Plan
*Updated: February 16, 2026 - Expanded to 1-50 employees*

---

## Company Size Targeting

| Segment | Employees | Priority | Target Leads |
|---------|-----------|----------|--------------|
| 1-20 employees | Micro + Small | HIGH | 40/week |
| 21-50 employees | Small-Mid | MEDIUM (test) | 20/week |

---

## Execution Checklist

### Phase 1: Account Setup (15 min)
- [ ] Sign up Apollo.io free account → https://www.apollo.io/sign-up
- [ ] Sign up Apify free account ($5 credits) → https://apify.com/sign-up
- [ ] Sign up Hunter.io free account (25 credits) → https://hunter.io/users/sign_up
- [ ] Get API keys from each service
- [ ] Test Apollo People Search API (FREE - no credits)

### Phase 2: Printing Leads (35 total)
- [ ] Run Apollo People API Search with **expanded 1-50 employee filters**
- [ ] Export 35 decision-makers (founders, owners, GMs, VPs)
- [ ] Segment results: 1-20 (priority) vs 21-50 (test)
- [ ] Run Apify CEO Finder on company domains
- [ ] Enrich top 15 with Apollo (15 credits) or Hunter
- [ ] Add to table below with segment tag

### Phase 3: Homestead Leads (25 total)
- [ ] Run Apollo People API Search with **expanded 1-50 employee filters**
- [ ] Cross-reference with Homesteaders of America vendor list (already scraped)
- [ ] Segment results: 1-20 (priority) vs 21-50 (test)
- [ ] Run Apify CEO Finder on company domains
- [ ] Enrich top 15 with Apollo or Hunter
- [ ] Add to table below with segment tag

### Phase 4: Activity Signals (Optional)
- [ ] Import n8n hiring signals workflow
- [ ] Run against target company LinkedIn pages
- [ ] Flag companies with active job posts = high-priority leads

---

## Quick Reference: Apollo Queries

### Printing Vertical (1-50 Employees)
```bash
curl --request POST \
  --url 'https://api.apollo.io/v1/mixed_people/search' \
  --header 'Content-Type: application/json' \
  --data '{
    "api_key": "YOUR_KEY",
    "q_keywords": "large format printer OR wide format OR plotter service",
    "person_titles": ["Founder", "Owner", "CEO", "President", "COO", "VP Operations", "General Manager", "Operations Director", "Service Manager"],
    "organization_num_employees_ranges": ["1,10", "11,20", "21,50"],
    "organization_locations": ["United States"],
    "per_page": 50
  }'
```

### Homestead Vertical (1-50 Employees)
```bash
curl --request POST \
  --url 'https://api.apollo.io/v1/mixed_people/search' \
  --header 'Content-Type: application/json' \
  --data '{
    "api_key": "YOUR_KEY",
    "q_keywords": "homestead OR homesteading OR small farm OR organic",
    "person_titles": ["Founder", "Owner", "CEO", "General Manager", "Operations Manager", "Managing Partner", "Director"],
    "organization_num_employees_ranges": ["1,10", "11,20", "21,50"],
    "organization_locations": ["United States"],
    "per_page": 50
  }'
```

---

## Credit Budget Tracker

| Tool | Monthly Free | Used | Remaining |
|------|--------------|------|-----------|
| Apollo (search) | Unlimited | 0 | Unlimited |
| Apollo (enrich) | 600 credits | 0 | 600 |
| Apify | $5 (~200 leads) | $0 | $5 |
| Hunter | 25 searches + 50 verifications | 0 | 75 |
| **Total Leads Target** | **60 this week** | **24** | **36 to go** |

### Weekly Breakdown by Segment

| Vertical | 1-20 Employees (Priority) | 21-50 Employees (Test) | Total Target |
|----------|---------------------------|------------------------|--------------|
| Printing | 25 leads | 10 leads | 35 |
| Homestead | 15 leads | 10 leads | 25 |
| **Weekly Total** | **40** | **20** | **60** |

---

## Printing Vertical (15 Found / 35 Target)

| # | Company | Owner | Email | Website | Location | Brands | Employees | Segment | Source | Pain Signal | Status |
|---|---------|-------|-------|---------|----------|--------|-----------|---------|--------|-------------|--------|
| 1 | Steven Enterprises | Family-owned (3 gen) | sales@plotters.com | plotters.com | Irvine, CA | HP, Canon | ~20 | 1-20 | Web Search | 30K+ businesses served | new |
| 2 | Techni-Serve Inc | TBD | TBD | techniservekc.com | Kansas City, MO | Canon, HP | ~10-15 | 1-20 | Web Search | 39 years, 2500 systems | new |
| 3 | Signa Digital Solutions | Family-owned | TBD | gosigna.com | San Diego, CA | Canon, HP, Samsung | ~10 | 1-20 | Web Search | Since 1995, 80yr mgmt exp | new |
| 4 | Print Scan Solutions | TBD | TBD | printscansolutions.com | Phoenix, AZ | HP, wide format | ~5-10 | 1-20 | Web Search | $125-150/hr rates | new |
| 5 | COSATL | TBD | TBD | cosatl.com | Atlanta, GA | HP (authorized) | ~10-15 | 1-20 | Web Search | HP authorized center | new |
| 6 | Plotter Pro | TBD | TBD | plotterpro.com | Austin/Houston/Dallas | HP, Canon | ~10-20 | 1-20 | Web Search | Multi-city coverage | new |
| 7 | Sign-It-Right | TBD | TBD | signitright.com | Houston/Dallas, TX | Mutoh | ~5-10 | 1-20 | Web Search | Mutoh authorized | new |
| 8 | netEffx | TBD | TBD | neteffx.com | Hudson Valley, NY | HP, Canon | ~10 | 1-20 | Web Search | 30+ years experience | new |
| 9 | Printer Coach | TBD | TBD | printercoach.com | Dallas/Fort Worth, TX | HP DesignJet | ~5-10 | 1-20 | Web Search | Since 2001 | new |
| 10 | TAVCO | TBD | TBD | tavcotech.com | Austin, TX | Canon imagePROGRAF | ~15-20 | 1-20 | Web Search | 200-mile on-site radius | new |
| 11 | The Right Equipment Co | TBD | TBD | rightequipment.net | Largo, FL | Canon (authorized) | ~10 | 1-20 | Web Search | Greater Tampa Bay | new |
| 12 | Superior Office Solutions | TBD | TBD | sosny.com | NY Metro/NJ/CT | Canon, Kyocera | ~15-20 | 1-20 | Web Search | Multi-state coverage | new |
| 13 | Great Lakes Computer | TBD | TBD | greatlakescomputer.com | Ohio | Epson (only OH partner) | ~15-20 | 1-20 | Web Search | 30+ years, Epson exclusive | new |
| 14 | Usherwood | TBD | TBD | usherwood.com | Binghamton, NY | Canon Elite Dealer | ~15-20 | 1-20 | Web Search | Master Tech certified | new |
| 15 | Chicago Printer Repair | TBD | TBD | chicagoprinterrepairinc.com | Chicago, IL | Wide format | ~5-10 | 1-20 | Web Search | Local service | new |

**Printing Progress:** 15/35 - Need 20 more (10 from 1-20 segment, 10 from 21-50 segment)

### Enrichment Priority (Printing)
1. Techni-Serve Inc - 39 years, large customer base
2. Signa Digital Solutions - Family-owned, long history
3. Print Scan Solutions - Phoenix market, clear pricing
4. Plotter Pro - Multi-city operation
5. TAVCO - 200-mile radius, established

---

## Homestead Vertical (9 Found / 25 Target)

| # | Business | Owner | Email | Website/Shop | Social | Location | Employees | Segment | Type | Revenue Indicator | Source | Pain Signal | Status |
|---|----------|-------|-------|--------------|--------|----------|-----------|---------|------|-------------------|--------|-------------|--------|
| 1 | Green Willow Homestead | Kelsey | hello@greenwillowhomestead.com | greenwillowhomestead.com | TBD | TBD | ~1-5 | 1-20 | Courses | Cultivating Capital course | Web Search | Coaching farm businesses | new |
| 2 | Living Traditions Homestead | Kevin & Sarah | PO Box 323, Ava MO | livingtraditionshomestead.com | 842K YouTube | Ava, MO | ~5-10 | 1-20 | Content + Products | 842K subs | Web Search | High volume requests | new |
| 3 | Abundance Plus | Justin Rhodes | TBD (DM for members) | abundanceplus.com | 1M+ YouTube | Asheville, NC | ~10-20 | 1-20 | Courses + Membership | #1 selling book | Web Search | Large audience | new |
| 4 | The Homestead Education | Kody Hanner | TBD | thehomesteadeducation.com | TBD | TBD | ~1-5 | 1-20 | Courses + Coaching | 20yr experience | Web Search | Pork operation + courses | new |
| 5 | HarmonyFarmsShop | TBD | TBD | etsy.com/shop/HarmonyFarmsShop | TBD | TBD | ~1-5 | 1-20 | Seeds, Nursery | Licensed seed dealer | Etsy | Heirloom + heritage focus | new |
| 6 | MountainlilyFarm | TBD | TBD | etsy.com/shop/MountainlilyFarm | TBD | Winslow, AR | ~1-5 | 1-20 | Heirloom seeds | 30+ yr horticulturist | Etsy | Licensed nursery | new |
| 7 | FarmFromHome | TBD | TBD | etsy.com/shop/FarmFromHome | TBD | TBD | ~1-5 | 1-20 | Herbs, Medicines | Wildcrafted herbs | Etsy | Urban homestead focus | new |
| 8 | Silver Homestead | TBD | TBD | silverhomestead.com | TBD | TBD | ~1-5 | 1-20 | Farm stand products | Best-seller guides | Web Search | Content + products | new |
| 9 | HomesteadHow-To | TBD | TBD | homesteadhow-to.com | TBD | TBD | ~1-5 | 1-20 | Beeswax products | Multi-year Etsy shop | Web Search | Growing customer base | new |

**Homestead Progress:** 9/25 - Need 16 more (6 from 1-20 segment, 10 from 21-50 segment)

### Enrichment Priority (Homestead)
1. Living Traditions Homestead - 842K YouTube, high volume
2. Abundance Plus - 1M+ YouTube, book author
3. Green Willow Homestead - Has email, coaches businesses
4. The Homestead Education - 20yr experience
5. Silver Homestead - Best-seller guides

---

## Lead Sources for API Scraping

### Printing (Use Apollo Query)
- HP Partner Locator: https://locator.hp.com/us/en/
- PRINTING United Directory: https://directory.printing.org/
- LinkedIn: "large format printer owner" + company size filter

### Homestead (Use Apollo Query)
- Homesteaders of America: https://homesteadersofamerica.com/conference-vendor-list/
- Mother Earth News Fair: https://www.motherearthnewsfair.com/exhibitors-sponsors/
- Etsy: "homestead" shops with 1000+ sales

---

## Verification Criteria

### Target Outcomes
- [ ] 35 printing leads with decision-maker names + emails
  - At least 25 from 1-20 employee segment (proven ICP)
  - Up to 10 from 21-50 employee segment (test)
- [ ] 25 homestead leads with decision-maker names + emails
  - At least 15 from 1-20 employee segment (proven ICP)
  - Up to 10 from 21-50 employee segment (test)
- [ ] At least 50% email verification rate from Hunter
- [ ] Document any hiring signals found

### Segment Prioritization
| Segment | Priority | Reason |
|---------|----------|--------|
| 1-20 employees | HIGH | Proven ICP (Plotter Mechanix profile) |
| 21-50 employees | MEDIUM | New territory, test messaging |

### Data Quality Standards
Each enriched lead MUST have:
- Company name
- Owner/Founder/GM name (not TBD)
- Email (verified preferred)
- Employee count (for segmentation)
- Segment tag (1-20 or 21-50)
- LinkedIn URL
- Hiring signal (Y/N)
- Pain signal or personalization hook

---

## Status Key
| Status | Meaning |
|--------|---------|
| `new` | Just added |
| `researched` | Verified email, found pain signal |
| `queued` | Ready for outreach |
| `emailed` | First email sent |
| `replied` | Got response |
| `call` | Discovery call scheduled |
| `proposal` | Proposal sent |
| `closed` | Deal won |
| `lost` | Not interested |

---

## Related Documentation
- `../infrastructure/lead-scraping-stack.md` - Full tools documentation
- `../infrastructure/apollo-queries.md` - Detailed API queries
- `../infrastructure/n8n-workflow-templates.md` - Automation workflows
