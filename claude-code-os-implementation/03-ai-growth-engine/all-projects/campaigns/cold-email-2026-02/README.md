# Cold Email Attack Plan: Printing Vertical
## Launch Date: Monday, February 16, 2026

---

## Quick Navigation

| Section | File |
|---------|------|
| Otto's Strategic Synthesis | [strategy/otto-strategic-synthesis.md](strategy/otto-strategic-synthesis.md) |
| Business Sequence Framework | [strategy/business-sequence-framework.md](strategy/business-sequence-framework.md) |
| Focus Rules | [strategy/focus-rules.md](strategy/focus-rules.md) |
| **Printing Vertical** | [verticals/printing/](verticals/printing/) |
| Homestead (Archived) | [verticals/_archive/homestead/](verticals/_archive/homestead/) |
| Domain & Inbox Setup | [infrastructure/domain-inbox-setup.md](infrastructure/domain-inbox-setup.md) |
| n8n Engine Spec | [infrastructure/n8n-engine-spec.md](infrastructure/n8n-engine-spec.md) |
| Personalization Pipeline | [infrastructure/personalization-pipeline.md](infrastructure/personalization-pipeline.md) |
| **Lead Scraping Stack** | [infrastructure/lead-scraping-stack.md](infrastructure/lead-scraping-stack.md) |
| **Apollo API Queries** | [infrastructure/apollo-queries.md](infrastructure/apollo-queries.md) |
| **n8n Workflow Templates** | [infrastructure/n8n-workflow-templates.md](infrastructure/n8n-workflow-templates.md) |
| **Cold Leads (Feb 16)** | [leads/cold-leads-2026-02-16.md](leads/cold-leads-2026-02-16.md) |
| Daily Rhythm | [operations/daily-rhythm.md](operations/daily-rhythm.md) |
| Weekly Targets | [operations/weekly-targets.md](operations/weekly-targets.md) |
| Metrics Dashboard | [operations/metrics-dashboard.md](operations/metrics-dashboard.md) |
| Reply Handling | [operations/reply-handling.md](operations/reply-handling.md) |
| Team Alignment | [operations/team-alignment.md](operations/team-alignment.md) |
| Hormozi Belief System | [conviction/hormozi-belief-system.md](conviction/hormozi-belief-system.md) |
| Case Study Rotation | [conviction/case-study-rotation.md](conviction/case-study-rotation.md) |
| Warm Leads Tracker | [warm-leads/outreach-tracker-2026-02.md](warm-leads/outreach-tracker-2026-02.md) |

---

## Strategic Foundation

### The Core Insight
**Stop marketing to "anyone and everyone." Go deep on ONE vertical where you have proof: Printing.**

### The Vertical

**Large Format Printer Companies** (Kelsey/Plotter Mechanix model) - $800K revenue client, 1,378% ROI case study, Phase 1 complete, Phase 2 in progress, videos in production

> **Note:** Homestead vertical archived until $1M revenue milestone. S&S Wolf remains trackable in warm leads (warm outreach allowed under Hormozi Focus Framework).

### Phases

| Phase | Dates | Focus |
|-------|-------|-------|
| Phase 0: Infrastructure | Mon 2/16 - Wed 2/18 | Domains, inboxes, DNS, n8n engine, lead lists, Loom videos |
| Phase 1: Campaign Launch | Mon 2/24 - Fri 3/6 | First cold emails sent, reply handling, discovery calls |
| Phase 2: Optimization | Week 3-4 | A/B testing, ICP refinement, scale triggers |
| Phase 3: Belief System | Ongoing | Weekly conviction meetings, case study rotation |

### Monday 2/16 Checklist

- [ ] **8:00** Buy 3 domains (15 min)
- [ ] **8:15** Set up Google Workspace, create 15 inboxes (90 min)
- [ ] **9:45** Configure SPF/DKIM/DMARC for all 3 domains (30 min)
- [ ] **10:15** Brief Matthew: n8n cold email engine spec + personalization pipeline (15 min)
- [ ] **10:30** Matthew starts building n8n workflows
- [ ] **10:45** Coffee. Infrastructure in motion.
- [ ] **11:00** Call Scott - capture phone/email, send Phase 1 demo
- [ ] **11:30** Call Randy - walk through $4K proposal, close
- [ ] **12:00** Lunch
- [ ] **1:00** Email + call Brad Tompkins (Brad@automationsolinc.com / 205-919-1400)
- [ ] **1:30** Email Sandra (sswolfsheds@gmail.com) with visual mockup
- [ ] **2:00** Email Mike (mike.k@romandrem.com) check-in
- [ ] **2:15** Text Hank (801-815-0390) - peer check-in ONLY
- [ ] **2:30** Find Tim Moorman email on LinkedIn, send outreach
- [ ] **3:00** Email Michele (dolche900@gmail.com) partnership angle
- [ ] **3:30** Create Google Sheet "Cold Outreach Tracker" (4 tabs: Dashboard, Lead Tracker, ICP Refinement, Deliverability)
- [ ] **4:00** Research printing companies - target 40 from HP/Canon authorized service partner directories + SGIA
- [ ] **5:00** Day done.

---

## Expected Outcomes & Revenue Projection

```
PRINTING VERTICAL (Cold Email):
Week 4:   ~150 emails -> 8-15 replies -> 4-8 calls -> 2-3 proposals -> 1-2 closes ($5K Phase 1)
Month 2:  ~400 emails -> 20-40 replies -> 10-20 calls -> 5-8 proposals -> 2-4 closes
Month 3:  ~800+ emails, pipeline compounding -> 4-6 closes -> $20-80K
           + Phase 2 upsells from Month 1 closes ($15-42K each)

WARM LEADS (IMMEDIATE):
Feb Week 1: Close Scott + Randy ($4-8K) + Sandra/S&S Wolf ($500 audit + $2K) = $6.5-10.5K
Feb total: $10-25K from warm leads alone

COMBINED:
Feb:    2-4 warm closes + infrastructure setup -> $10-25K
March:  2-4 cold closes -> $10-30K
April:  4-6 cold closes + Phase 2 upsells -> $20-80K
= Path to $50K/month by Month 3-4
```

---

## Critical Files

| File | Purpose |
|------|---------|
| `ai-agency-sales-os/outreach-tracker-2026-02-05.md` | 11 existing warm leads |
| `ai-agency-sales-os/claude-code-os-implementation/06-knowledge-base/case-studies/plotter-mechanix-phase-1/` | Full case study (1,378% ROI) |
| `ai-agency-sales-os/claude-code-os-implementation/02-operations/project-management/active-projects/plotter-mechanix/offer/phase-2/2026-02-06-updated-with-alyssa/executive-summary-kelsey.md` | Kelsey Phase 2 numbers |
| `ai-agency-sales-os/claude-code-os-implementation/03-ai-growth-engine/all-projects/outreach/arise-group-ai-outreach-framework.md` | 5 Questions framework |
| `ai-agency-sales-os/agentic/modules/leads/tool/scrape_leads.py` | Apify lead scraper |
| `ai-agency-sales-os/agentic/extras/n8n-wf/nurture_sequence.json` | Post-reply nurture |
| `ai-agency-sales-os/claude-code-os-implementation/02-operations/discovery-process/templates/5-questions-discovery-call-script.md` | Discovery call script |

### Lead Scraping Tools (API-Based)

| Tool | Documentation | Free Tier |
|------|---------------|-----------|
| Apollo.io | [lead-scraping-stack.md](infrastructure/lead-scraping-stack.md) | 600 credits/mo (search FREE) |
| Apify | [lead-scraping-stack.md](infrastructure/lead-scraping-stack.md) | $5/mo credits |
| Hunter.io | [lead-scraping-stack.md](infrastructure/lead-scraping-stack.md) | 25 searches + 50 verifications |
| Clay.com | [lead-scraping-stack.md](infrastructure/lead-scraping-stack.md) | 100 credits/mo |

---

## Key Takeaway (Otto)

> You already have the solution. You already have the proof. You already have the case study. All you need to do now is **find more businesses like Kelsey's and show them what you've built.**

**Meeting Reference:** Weekly Sync - Mekaiel Abdullahi & Otto Petersen
