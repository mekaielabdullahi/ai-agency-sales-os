# Phase 2: PlotterOps Transformation - Roadmap

**Status:** Validation in Progress - Joe's interview COMPLETED
**Depends On:** Phase 1 deployed; validation phase active
**Last Updated:** January 31, 2026

---

## Important Notice

⚠️ **This roadmap is now validated with Joe's stakeholder interview data.**

A formal 3-tier proposal ($15k / $28k / $47k) has been updated with validated insights.
See `offer/phase-2/final-proposal/` for the updated proposal with Joe's validated metrics.

**✅ VALIDATED Context (Jan 28, 2026 - Joe's Interview):**
- **Training burden:** 20-30 hrs/week × 3 months (not 5 hrs/week estimate)
- **Knowledge gaps:** 20% of calls need major help, 10-15% minor guidance
- **Shopify-Jobber broken:** 2-3 under-deliveries monthly due to unit mismatch
- **Morning coordination:** 1.5-2 hours daily, routes change 4/5 days
- **Mobile need:** Joe wants RAG agent for field queries
- **Learning preference:** Videos over live training

**Updated Context (Jan 27, 2026 call):**
- Revenue is ~$700-800k (NOT $600k), trending toward $1.2M-$1.7M target
- Andrew is fully operational on supplies/sales (not "ramping up")
- Steve is permanently off table; pivoting to Michael Maloney / subcontractor model
- Kelsey's dyslexia = hard UX constraint (voice-friendly / simple interfaces required)
- Subcontractor network forming (former Plotter Doctors employee, Michael Maloney)
- Tiered pricing in development to accommodate cash flow sensitivity

---

## Joe's Validation - Priority Adjustments

### NEW Priority Order (Based on Joe's Interview):
1. **Fix Shopify-Jobber Integration** (Week 1) - 2-3 under-deliveries/month
2. **Training System with Videos** - 20-30 hrs/week burden validated
3. **Knowledge Base/RAG Agent** - 30% of calls need help
4. **Equipment Management** - Missing customer equipment lists
5. **Morning Coordination Tools** - 1.5-2 hours daily chaos

### Immediate Wins Identified:
- Shopify unit conversion automation (box vs roll)
- Video tutorials for Joe's weak areas (solvents, Epson, UV)
- Mobile RAG agent for field queries
- Tech expertise mapping for better routing

## Overview

Phase 2 transforms Plotter Mechanix from reactive firefighting to proactive operations. The core focus has shifted from **inventory visibility** to **knowledge transfer and operational intelligence** based on Joe's validation.

**Built on Phase 1 Foundation:**
- Communication captured automatically (Quo-Jobber integration deployed and live)
- Jobber trusted as source of truth
- Team workflow optimized for efficiency
- IVR routing configured (5-extension menu)
- Kelsey adopted Quo as default phone; strong platform buy-in
- Data collection infrastructure in place

### Core Problem Statement

**From client conversations:**

> "If I don't know that it's taken out of inventory, then that whole process falls apart" - Alyssa

> "No fucking clue what we have" - Chris on inventory

> "I don't know what inventory I need until I'm on-site... sometimes need to stop mid-route for parts" - Chris

**Current State Costs:**
- Wasted trips (no parts available)
- Rush shipping charges
- Jobs delayed for parts
- Customer frustration
- "Do we have X?" interruptions
- Opportunity cost (can't scale without inventory control)

**Phase 1 enables Phase 2 by:**
- Capturing inventory mentions from Quo call transcripts
- Auto-logging parts issues via email automation
- Creating baseline metrics for inventory problems
- Establishing trust in system to build upon

---

## Potential Deliverables (To Be Scoped)

### 1. Inventory Management System

#### Problem to Solve

- No visibility into what parts are in stock
- Can't plan jobs because don't know what's available
- Manual tracking fails → wasted trips, rush orders
- Blocks scaling (can't hire another tech without inventory system)

#### Potential Features

**Core Inventory Tracking:**
- [ ] Part catalog (what parts exist)
- [ ] Stock levels (how many in stock)
- [ ] Location tracking (where parts are stored)
- [ ] Low stock alerts
- [ ] Usage history

**Integration Points:**
- [ ] Jobber integration (link parts to jobs)
- [ ] QuickBooks integration (purchasing, COGS)
- [ ] Quo integration (capture inventory mentions from calls)

**User Workflows:**
- [ ] Add/remove inventory (when parts arrive/used)
- [ ] Check availability (before scheduling job)
- [ ] Reserve parts (for scheduled jobs)
- [ ] Reorder triggers (auto-generate purchase orders)

**Reporting:**
- [ ] Parts usage by job type
- [ ] Inventory value
- [ ] Stock turnover
- [ ] Rush order costs (Phase 1 data baseline)

#### Questions to Answer in Phase 1

- How many unique parts do they stock?
- What's the current tracking method?
- Who adds/removes inventory (process design)?
- What's acceptable stock-out rate?
- Rush order cost baseline (track during Phase 1)

---

### 2. Planning Agent Enhancement

#### Current State (Phase 1)

Phase 1 may include basic planning agent (under review based on Quo-Jobber native capabilities).

#### Phase 2 Enhancement

**With inventory system integrated:**

```
New job created
      ↓
Analyze job type + parts needed
      ↓
Check actual inventory levels (not guessing)
      ↓
If parts available: Reserve + add to plan
If parts missing: Alert + suggest purchase
      ↓
Generate next-day route with confirmed parts
      ↓
SMS to Chris: "Tomorrow's plan - all parts confirmed ✓"
```

**Value Add:**
- Eliminate "hope I have the right parts" uncertainty
- Enable true proactive job planning
- Reduce wasted trips to zero
- Optimize inventory levels based on job pipeline

---

### 3. Unified Operations Dashboard

#### Problem to Solve

**Client Quote:**
> "If I don't see it over here, then I don't know they sent a message"

Currently managing:
- Jobber (jobs, clients, scheduling)
- QuickBooks (accounting, new system Jan 1)
- Shopify (POS for sales)
- Quo (calls, texts)
- Email (quotes, vendor communications)

Each system is a separate login, separate view.

#### Potential Features

**Single Dashboard View:**
- [ ] Today's jobs (from Jobber)
- [ ] Unhandled messages (from Quo + Jobber)
- [ ] Invoice queue status (from Jobber)
- [ ] Cash flow snapshot (from QuickBooks)
- [ ] Inventory alerts (from inventory system)
- [ ] New leads (from Quo)

**Role-Based Views:**
- Chris: Field operations + strategic metrics
- Alyssa: Admin queue + invoicing + inventory
- Joe: Assigned jobs + training checklist

**Mobile Optimization:**
- Accessible from Kelsey's phone in field
- Quick-check during morning coffee (Pine Top vision)
- Voice-friendly / simple interface (Kelsey's dyslexia constraint)

#### Questions to Answer

- What metrics matter most day-to-day?
- QuickBooks new system (Jan 1) - what data is accessible?
- Shopify integration value vs complexity?

---

### 4. Complete SOP Library

#### Phase 1 Baseline

- 4 core SOPs
- Passive knowledge capture workflow established

#### Phase 2 Expansion

**Additional SOPs to Create:**
- Equipment-specific repair procedures (top 10-20 machines)
- Customer onboarding process
- Preventive maintenance workflows
- Vendor management procedures
- Emergency response protocols

**Knowledge Capture:**
- Continue passive audio capture
- Video recordings (with Chris's permission)
- Shadow sessions with Joe (training scenarios)
- Customer interaction examples

**Organization:**
- Searchable knowledge base
- Tagged by equipment type, skill level, scenario
- Mobile-accessible for field reference

**Goal:**
> "There's maybe 5-10 people in Arizona with this knowledge" - Trent

Capture Chris's 25+ years expertise in searchable, trainable format.

---

### 5. Automated Pricing System

#### Problem to Solve

**Client conversation context:**

Vendors send quotes via email (often PDFs). Currently manual process to:
1. Read quote
2. Calculate markup
3. Update pricing in system
4. Generate customer quote

#### Potential Features

**Email Integration:**
- [ ] Connect to business email
- [ ] Detect incoming quotes (vendor emails)
- [ ] Extract pricing from PDFs
- [ ] Parse line items

**Automated Pricing:**
- [ ] Apply markup rules (by vendor, product type)
- [ ] Generate customer-facing quote
- [ ] Route for approval if needed
- [ ] Update pricing database

**Quote Management:**
- [ ] Track quote status (sent, accepted, expired)
- [ ] Historical pricing data
- [ ] Margin analysis

#### Questions to Answer

- How many vendors send quotes regularly?
- What quote formats (PDF, email body, structured)?
- What markup rules apply?
- Approval workflow requirements?

---

### 6. Additional Potential Features (Lower Priority)

#### Customer Portal

Self-service for customers:
- Job status lookup
- Invoice payment
- Request service
- View equipment history

**Depends on:** Bandwidth to support customer-facing system

#### Advanced Analytics

- Profitability by customer
- Technician efficiency metrics
- Equipment failure prediction
- Seasonal demand forecasting

**Depends on:** Data history and clean baseline

#### Voice-to-Action System

**Client Quote:**
> "If I could say, hey, I'm going to send you a quote for a T650, Jimmy, and it could take that information and say, you need to make a quote for a 650, and I could trust it"

AI extracts action items from calls:
- "Send quote to X" → Generate quote
- "Schedule follow-up" → Create reminder
- "Order part Y" → Add to purchase order

**Depends on:** Phase 1 Quo setup, confidence in AI accuracy

---

## Phasing Strategy

### Phase 2A: Foundation (First Priority)

**Core delivery:**
1. Inventory Management System (basic)
2. QuickBooks Integration (new system Jan 1)
3. Planning Agent Enhancement (inventory-aware)

**Goal:** Solve the #1 operational bottleneck (inventory chaos)

### Phase 2B: Scale Enablers (Second Priority)

**Core delivery:**
1. Unified Operations Dashboard
2. Complete SOP Library (equipment-specific)
3. Automated Pricing System

**Goal:** Enable hiring and scaling (Lucid Motors readiness)

### Phase 2C: Advanced (Third Priority)

**Core delivery:**
1. Customer Portal
2. Advanced Analytics
3. Voice-to-Action System

**Goal:** Differentiation and long-term moat

---

## Success Criteria (Phase 2)

### Quantitative Metrics

| Metric | Target |
|--------|--------|
| Wasted trips eliminated | 90%+ reduction |
| Rush order costs | 75%+ reduction |
| Jobs delayed for parts | <5% of total jobs |
| Inventory accuracy | 95%+ |
| Time saved per day | Additional 1-2 hours |
| Second tech scalability | Ready to hire |

### Qualitative Outcomes

- [ ] Kelsey confident in job planning night before
- [ ] Alyssa knows inventory status without asking
- [ ] Joe can check parts availability independently
- [ ] Foundation ready for Lucid Motors contract (200 cuts/day)
- [ ] System demonstrates productization potential

---

## Pricing Framework (Placeholder)

**NOT FINAL - Illustrative only**

Phase 2 pricing: $15,000-$47,000 (3-tier options now in internal review). Range depends on:
- Scope selected (2A, 2B, 2C components)
- Integration complexity (especially QuickBooks new system)
- Custom development vs off-the-shelf solutions
- Timeline (faster = more resources = higher cost)

**Approach:**
1. Use Phase 1 data to inform scope
2. Create fixed-price proposal for agreed deliverables
3. Potentially split into 2A, 2B, 2C milestones
4. Credit incentive: $5K from Phase 1 applies if signed within 14 days

---

## Timeline Framework (Placeholder)

**NOT FINAL - Illustrative only**

- Phase 2A: 4-6 weeks
- Phase 2B: 4-6 weeks
- Phase 2C: 6-8 weeks

Could be delivered:
- Sequentially (2A → 2B → 2C over 4-5 months)
- Parallel (compressed timeline, higher cost)
- Milestone-based (deliver 2A, pause, assess, continue)

---

## Dependencies

### Technical Dependencies

- [ ] Phase 1 Quo-Jobber integration stable
- [ ] QuickBooks new system (Jan 1) stabilized and accessible
- [ ] Jobber API capabilities confirmed for inventory linking
- [ ] Client email access granted (for quote automation)

### Business Dependencies

- [ ] Phase 1 delivered successfully
- [ ] Trust and value validated
- [ ] Client cash flow supports investment
- [ ] Team bandwidth to support implementation

### Data Dependencies

- [ ] Phase 1 inventory issue tracking completed
- [ ] Rush order cost baseline established
- [ ] Parts usage patterns documented
- [ ] Job type distribution confirmed

---

## Transition from Phase 1 to Phase 2

### Phase 1 Deliverable: Data Collection

Even during Phase 1, we'll be:

**Tracking inventory mentions:**
- Quo call transcripts analyzed for "Do we have X?"
- Handoff template includes inventory issues
- Count wasted trips, rush orders, delayed jobs

**Preparing for integrations:**
- Email connection (with permission) to identify quote patterns
- Jobber data analysis (job types, parts patterns)
- QuickBooks readiness assessment (new system Jan 1)

**Building the business case:**

> "During Phase 1, you had:
> - 8 inventory-related issues
> - 3 wasted trips = 6 hours + fuel
> - $150 in rush shipping
> - 2 jobs delayed 2+ days
> - 12 'Do we have X?' interruptions
>
> Phase 2 eliminates this entire category of problems."

---

## The Long-Term Vision: Plotter Mechanics Hub

### Client's Vision

**Lifestyle Goal:**
> "Sitting at Pine Top drinking on your coffee in the mornings on your balcony... all you have to do is just make phone calls and get paid."

**Impact Goal:**
> "My heart is, I want to do something financially... I want to start and help kids, dude."

### System Evolution

**Phase 1:** Communication control for Plotter Mechanix
**Phase 2:** Operations system for Plotter Mechanix
**Phase 3+:** Proprietary platform ("Plotter Mechanics Hub")

**Potential Future:**
- License to other printer service businesses
- Industry-specific SaaS product
- Chris becomes consultant to the industry
- System operates business while Chris focuses on growth/impact

**Matthew's Quote:**
> "You're putting the money in to build this system, this ecosystem that we are going to turn into Plotter Mechanics software down the road."

---

## Key Reminders

1. **This is a roadmap, not a commitment** - Scope/pricing TBD after Phase 1
2. **Focus on Phase 1 success first** - Phase 2 depends on proving value
3. **Use Phase 1 data to inform Phase 2** - Track inventory issues to build business case
4. **Flexibility is key** - Requirements will evolve as we learn more
5. **Client leads the pace** - We propose, they decide when ready

---

## Next Steps

### Immediate (During Phase 1)

- [ ] Track inventory-related issues
- [ ] Document parts usage patterns
- [ ] Establish cost baseline (rush orders, wasted trips)
- [ ] Monitor QuickBooks transition (Jan 1)

### End of Phase 1

- [ ] Present Phase 1 success metrics
- [ ] Share inventory tracking data
- [ ] Discuss Phase 2 interest and timing
- [ ] Assess cash flow and readiness

### Phase 2 Kickoff (If Approved)

- [ ] Create detailed Phase 2 proposal with fixed price
- [ ] Define specific deliverables from this roadmap
- [ ] Set timeline and milestones
- [ ] Begin discovery for inventory system design

---

## Related Documentation

- [Phase 1 Deliverables](./phase-1-quick-win-sprint.md)
- [Deliverables Overview](./README.md)
- [Quick Win Proposal (Draft 02)](../offer/drafts/draft-02-post-meeting/quick-win-proposal.md)
- [Client Vision Notes](../meetings/) - Various meeting transcripts

---

*This roadmap is now supplemented by a formal 3-tier Phase 2 proposal. See offer/phase-2/to-review/ for details.*

**Last Updated:** January 28, 2026
