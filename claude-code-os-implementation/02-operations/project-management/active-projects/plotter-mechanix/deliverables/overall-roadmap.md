# Plotter Mechanix - Overall Roadmap

**Project:** PlotterOps Transformation
**Client:** Plotter Mechanix (Kelsey Andrade, Phoenix AZ)
**Last Updated:** January 28, 2026
**Status:** Phase 1 Deployed - Quo-Jobber integration live, IVR routing configured. Phase 2 internal review in progress.

---

## Vision: From Chaos to Clarity to Scale

### Current State (Pre-Phase 1)
**"Chaos Mode"**
- Screenshot bombing to communicate
- Phone number confusion
- Email chaos (206 unread)
- Jobber not trusted ("I don't fully trust that everything is in there")
- Manual handoffs causing delays
- Inventory blindness ("no fucking clue what we have")

### Phase 1 Goal
**"Clarity Mode"**
- Communication auto-captured
- Jobber becomes trusted source of truth
- Screenshot bombing eliminated
- Single business number for all calls
- Morning routine: Check Jobber first

### Phase 2 Goal
**"Proactive Operations"**
- Inventory visibility
- Job planning with confidence
- Unified operations dashboard
- Wasted trips eliminated
- Ready to scale (hire second tech)

### Phase 3+ Goal
**"Scale & Productize"**
- Multi-tech operations
- Lucid Motors ready (200 cuts/day)
- PlotterOps as product (industry SaaS)
- Kelsey at Pine Top on his balcony
- "All you have to do is just make phone calls and get paid"

---

## Phase 1: Communication Control & Jobber Trust
**Status:** Deployed -- Quo-Jobber integration live, IVR routing configured, Kelsey chose Quo as default phone
**Timeline:** 4 weeks (Dec 23 - Jan 20, 2026)
**Investment:** $5,000 Quick Win Sprint

### The Core Problem

**Kelsey's Quote (Dec 22):**
> "My first instinct is not to go to Jobber and look for the information I need. It's to go into my text messages and my inbox... I don't fully trust that everything is in there"

**Why Jobber Isn't Trusted:**
- Screenshot bombing creates hours of lag
- Phone handoffs get lost in phone tag
- Email requests sit unread for days
- Updates depend on manual data entry

### Solution: Option 4c (Confirmed Approach)

**Component 1: Quo for Unified Communications**
- Single business phone number (port Vonage 602-606-XXXX)
- iOS default calling app (all outbound calls show business number)
- Auto-transcribe all calls
- SMS capability (sync to Jobber)
- Auto-create Jobber Requests for new contacts
- Cost: $69-99/mo (3 users)

**Component 2: Email → Jobber Automation**
- N8N workflow monitors 4 email inboxes:
  - service@plottermechanix.com
  - supplies@plottermechanix.com
  - sales@plottermechanix.com
  - accounting@plottermechanix.com
- Auto-create Jobber Request for customer emails
- Spam filtering to prevent noise
- Parse subject, body, sender, attachments
- Cost: $0 (existing N8N infrastructure)

**Component 3: Keep Jobber As-Is**
- No changes to current Jobber plan ($350-400/mo)
- Jobber texting feature available if needed
- No disruption to existing workflows
- Let data inform future optimization

### What Gets Fixed

| Pain Point | Solution | Outcome |
|------------|----------|---------|
| Screenshot bombing | Quo SMS syncs to Jobber | Eliminated |
| Phone handoffs (4-6x/day) | Auto-logged call transcripts | 80% reduction |
| Email chaos (206 unread) | Auto-create Requests | Inbox → <20 unread |
| Phone number confusion | iOS default calling | Single business # |
| Jobber trust gap | Real-time auto-capture | "Check Jobber first" |
| Alyssa manual entry | Automation | 1-2 hrs/day saved |

### Timeline: 4-Week Phased Rollout

**Week 1: Testing & Validation (Dec 23-30)**
- Answer 10 critical questions
- Test Quo-Jobber integration quality
- Validate iOS default calling works
- Test call transcript usefulness
- Assess email spam filtering
- Document findings
- GO/NO-GO decision

**Week 2: Quo Configuration (Dec 30 - Jan 6)**
- Configure call routing (5-option IVR)
- Set up iOS default calling (Kelsey, Joe, Alyssa)
- A2P 10DLC registration (SMS compliance)
- Team training on Quo app
- Port Vonage number OR set up forwarding

**Week 3: Email Automation (Jan 6-13)**
- Build N8N email monitoring workflow
- Implement spam filtering rules
- Test Request creation quality
- Refine parsing logic
- Alyssa reviews auto-created Requests
- Tune accuracy

**Week 4: Go-Live & Refinement (Jan 13-20)**
- Enable all automations
- Team switches to Quo for calls/texts
- Monitor quality and reliability
- Daily check-ins with Kelsey/Alyssa
- Document edge cases
- Refine workflows based on real usage

### Success Metrics (30-Day Validation)

**Quantitative:**
- 90%+ communication auto-captured in Jobber within 5 min
- Screenshot handoffs eliminated (0 per week)
- Phone call handoffs reduced 80% (1-2 per day max)
- Email inbox <20 unread (from 206)
- Alyssa saves 1+ hours/day on manual entry

**Qualitative:**
- Kelsey: "I trust Jobber has everything"
- Alyssa: "Morning routine is faster, less chaotic"
- Joe: "I know where to check for my jobs"
- Kelsey checks Jobber first (not texts/email) 5+ days/week

**Technical:**
- Quo-Jobber sync reliability >95%
- Call transcripts useful quality
- Email automation accuracy >80% (real vs spam)
- iOS default calling works for all 3 users
- No major system downtime

### ROI Calculation

**Time Savings:**
- Alyssa: 1.5 hrs/day × 20 days = 30 hrs/mo @ $25/hr = $750/mo
- Kelsey: 0.5 hrs/day × 20 days = 10 hrs/mo @ $100/hr = $1,000/mo
- **Total Value: $1,750/mo**

**Cost:**
- Quo: +$69-99/mo
- Vonage: -$??/mo (to be eliminated)
- N8N: $0
- Jobber: $0 change
- **Net Cost: ~$70-100/mo** (depends on Vonage cost)

**ROI: 17-25x return on investment**

### Critical Open Questions (Week 1 Testing)

1. **Quo-Jobber SMS sync quality** (BLOCKER)
2. **Quo call summary usefulness**
3. **Auto-Request creation behavior**
4. **iOS default calling app functionality** (BLOCKER)
5. **Email parsing accuracy**
6. **A2P 10DLC timeline**
7. **Number porting vs forwarding decision**
8. **Current Vonage cost**
9. **Team adoption risk** (BLOCKER)
10. **Jobber texting redundancy decision**

### Deliverables

1. Quo Implementation (unified communications)
2. iPhone Default Calling Setup (3 users)
3. Email → Jobber Automation (N8N workflow)
4. Team Training & Documentation
5. 30-day success report with metrics

### Related Documentation

- [Phase 1 Detailed Plan](./phase-1-quick-win-sprint.md)
- [Option 4c Technical Spec](./option-4c-recommended-approach.md)
- [Week 1 Testing Checklist](./week-1-testing-checklist.md)
- [Kelsey's Jobber Workflow](../audit/kelsey-jobber-workflow.md)
- [Process Map](../audit/process-map.md)

---

## Phase 2: Inventory Visibility & Operations Dashboard
**Status:** Internal review in progress (Jan 28, 2026)
**Estimated Timeline:** 4-6 weeks
**Estimated Investment:** $15,000-$47,000 (3 tier options -- see offer/phase-2/to-review/)
**Design Constraint:** Voice-friendly / dyslexia-accessible interfaces required (Kelsey's UX needs)

> **Key Distinction: Equipment vs Inventory**
> Phase 2 addresses TWO separate tracking needs:
> - **Inventory/Consumables** (Ply) = Plotter Mechanix's own stock: printheads, inks, paper, belts, maintenance kits. Megan is implementing Ply (getply.com) for this -- parts tracking, truck stock, purchase orders, barcode scanning, Jobber integration.
> - **Customer Equipment** (Equipment Management Platform) = printers, plotters, cutters at customer locations. Tracked by serial number, model, service history, contracts. We will evaluate off-the-shelf solutions (Miracle Service, Field Force Tracker, BlueFolder) before considering a custom build.
> - **Legacy: Capsule CRM** = Kelsey still paying ~$30/mo for old customer contact database not migrated to Jobber. Data to be audited and migrated during Phase 2.

### Built on Phase 1 Foundation

Phase 1 creates the infrastructure to enable Phase 2:
- Communication captured automatically → Data for inventory analysis
- Jobber trusted as source of truth → Foundation to build operations on
- Team workflow optimized → Ready for next layer of automation
- Call transcripts → Capture "Do we have X?" mentions

### The Core Problem

**Inventory Blindness:**
> "No fucking clue what we have" - Kelsey

**Customer Equipment Blindness:**
> Service history in Kelsey's head, no database of customer equipment at their locations

**Impact:**
- Wasted trips (start job, realize no parts, reschedule)
- Rush shipping charges
- Jobs delayed for parts
- Can't plan routes effectively
- Can't hire second tech (no inventory system)
- Blocks Lucid Motors contract (200 cuts/day scale)
- Can't identify service contract eligible customers (no equipment records)
- Reactive service only (no proactive maintenance)

### Potential Deliverables (To Be Scoped)

#### 2.1 Inventory Management System
**Core Features:**
- Part catalog with stock levels
- Location tracking (where parts stored)
- Low stock alerts
- Usage history
- Jobber integration (link parts to jobs)
- QuickBooks integration (purchasing, COGS)
- Reserve parts for scheduled jobs
- Auto-generate purchase orders

**User Workflows:**
- Add/remove inventory (when parts arrive/used)
- Check availability before scheduling job
- Reserve parts for scheduled jobs
- Reorder triggers

**Reporting:**
- Parts usage by job type
- Inventory value
- Stock turnover
- Rush order cost tracking

#### 2.2 Planning Agent Enhancement
**Current State:** Phase 1 may include basic planning agent (TBD)

**Phase 2 Enhancement:**
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
SMS to Kelsey: "Tomorrow's plan - all parts confirmed ✓"
```

**Value:** Eliminate "hope I have the right parts" uncertainty

#### 2.3 Unified Operations Dashboard
**Problem:** Currently managing Jobber, QuickBooks, Shopify, Quo, Email separately

**Single Dashboard View:**
- Today's jobs (from Jobber)
- Unhandled messages (from Quo + Jobber)
- Invoice queue status
- Cash flow snapshot (from QuickBooks)
- Inventory alerts
- New leads

**Role-Based Views:**
- Kelsey: Field operations + strategic metrics
- Alyssa: Admin queue + invoicing + inventory
- Andrew: Supplies, sales, customer follow-ups
- Joe: Assigned jobs + training checklist

**Mobile Optimized:** Pine Top balcony vision

#### 2.4 Complete SOP Library
**Phase 1 Baseline:** 4 core SOPs + passive capture workflow

**Phase 2 Expansion:**
- Equipment-specific repair procedures (top 10-20 machines)
- Customer onboarding process
- Preventive maintenance workflows
- Vendor management procedures
- Emergency response protocols

**Knowledge Capture:**
- Continue passive audio capture
- Video recordings (with permission)
- Shadow sessions with Joe
- Customer interaction examples

**Organization:**
- Searchable knowledge base
- Tagged by equipment type, skill level, scenario
- Mobile-accessible for field reference

**Goal:** Capture Kelsey's 25+ years expertise in searchable format

#### 2.5 Automated Pricing System
**Problem:** Vendor quotes arrive via email (PDFs), manual process to apply markup and generate customer quotes

**Features:**
- Email integration (detect vendor quotes)
- Extract pricing from PDFs
- Apply markup rules (by vendor, product type)
- Generate customer-facing quote
- Route for approval if needed
- Historical pricing data
- Margin analysis

### Phasing Strategy

**Phase 2A: Foundation (First Priority)**
1. Inventory Management System (basic)
2. QuickBooks Integration (new system Jan 1)
3. Planning Agent Enhancement (inventory-aware)

**Goal:** Solve #1 operational bottleneck (inventory chaos)

**Phase 2B: Scale Enablers (Second Priority)**
1. Unified Operations Dashboard
2. Complete SOP Library (equipment-specific)
3. Automated Pricing System

**Goal:** Enable hiring and scaling (Lucid Motors readiness)

**Phase 2C: Advanced (Third Priority)**
1. Customer Portal (self-service)
2. Advanced Analytics (profitability, forecasting)
3. Voice-to-Action System (AI extracts action items from calls)

**Goal:** Differentiation and long-term moat

### Success Metrics (Phase 2)

| Metric | Target |
|--------|--------|
| Wasted trips eliminated | 90%+ reduction |
| Rush order costs | 75%+ reduction |
| Jobs delayed for parts | <5% of total jobs |
| Inventory accuracy | 95%+ |
| Time saved per day | Additional 1-2 hours |
| Second tech scalability | Ready to hire |

**Qualitative:**
- Kelsey confident in job planning night before
- Alyssa knows inventory status without asking
- Joe can check parts availability independently
- Foundation ready for Lucid Motors contract

### Data Collection During Phase 1

**Track for Phase 2 business case:**
- Inventory mentions in Quo transcripts ("Do we have X?")
- Count wasted trips, rush orders, delayed jobs
- Email patterns (vendor quotes, customer requests)
- Parts usage patterns (via Jobber data)
- QuickBooks new system capabilities (Jan 1)

**30-Day Report Example:**
> "During Phase 1, you had:
> - 8 inventory-related issues
> - 3 wasted trips = 6 hours + fuel
> - $150 in rush shipping
> - 2 jobs delayed 2+ days
> - 12 'Do we have X?' interruptions
>
> Phase 2 eliminates this entire category of problems."

### Related Documentation

- [Phase 2 Detailed Roadmap](./phase-2-roadmap.md)

---

## Phase 3: Multi-Tech Operations & Scale Readiness
**Status:** Conceptual
**Estimated Timeline:** 6-12 months after Phase 2
**Estimated Investment:** TBD

### The Vision

**Lucid Motors Contract:**
- 200 cuts per day
- Requires multiple techs
- Requires bulletproof operations
- Requires inventory system at scale

### Potential Focus Areas

#### 3.1 Multi-Technician Operations
**Capabilities:**
- Multiple techs using same system
- Route optimization (AI assigns jobs by location/skill/parts)
- Real-time GPS tracking
- Tech performance metrics
- Collaborative inventory management
- Quality control workflows

#### 3.2 Customer Self-Service
**Portal Features:**
- Job status lookup
- Invoice payment
- Request service
- View equipment history
- Preventive maintenance scheduling

**Value:**
- Reduce "Where's my job?" calls
- Faster payment collection
- Proactive service opportunities

#### 3.3 Advanced Analytics & Forecasting
**Insights:**
- Profitability by customer, job type, equipment
- Technician efficiency metrics
- Equipment failure prediction
- Seasonal demand forecasting
- Pricing optimization
- Customer lifetime value

#### 3.4 Industry Platform ("PlotterOps")
**Kelsey's Vision:**
> "You're putting the money in to build this system, this ecosystem that we are going to turn into Plotter Mechanics software down the road." - Matthew

**Productization Opportunity:**
- Package PlotterOps as industry SaaS
- License to other printer service businesses
- Kelsey becomes consultant/thought leader
- Recurring revenue from software licenses
- Scale impact beyond Phoenix

**Stages:**
1. Perfect for Plotter Mechanix (Phase 1-3)
2. Deploy to 1-2 pilot customers (validate generalization)
3. Build SaaS infrastructure (multi-tenant)
4. Go-to-market strategy
5. Kelsey: operator → industry platform CEO

### Success Vision

**Lifestyle Outcome:**
> "Sitting at Pine Top drinking on your coffee in the mornings on your balcony... all you have to do is just make phone calls and get paid." - Client vision

**Impact Outcome:**
> "My heart is, I want to do something financially... I want to start and help kids, dude." - Kelsey

**Business Outcome:**
- System operates Plotter Mechanix autonomously
- Kelsey focuses on strategic growth, not daily firefighting
- Multiple revenue streams (service + software licensing)
- Industry leadership position
- Foundation for social impact goals

---

## Phase 4+: Beyond Plotter Mechanix
**Status:** Long-Term Vision

### PlotterOps as Industry Platform

**Market Opportunity:**
> "There's maybe 5-10 people in Arizona with this knowledge" - Trent

**If true for Arizona, likely true nationally:**
- Niche industry with high expertise barrier
- Small businesses struggling with same problems
- No dominant software solution
- Kelsey's expertise is differentiator

**Potential:**
- SaaS platform for printer service industry
- Training/certification program (Kelsey's knowledge scaled)
- Equipment supplier partnerships
- Parts marketplace
- Industry conference/community

### Impact Goals

**Kelsey's "Why":**
- Financial freedom to focus on kids/community
- Share knowledge (training next generation)
- Scale impact beyond Phoenix
- Build something bigger than one business

**Trent's Role:**
> "I'm just trying to get you there. I want to get you there and I want to play a role in that legacy." - Trent to Kelsey

---

## Decision Points & Governance

### Phase 1 → Phase 2 Transition

**GO Decision Criteria:**
- [ ] Phase 1 delivered successfully
- [ ] Success metrics achieved (>80% targets hit)
- [ ] Jobber trusted as source of truth (Kelsey confirms)
- [ ] Client cash flow supports Phase 2 investment
- [ ] Inventory data from Phase 1 validates business case

**NO-GO Scenarios:**
- Phase 1 technical failure (integration broken)
- Team adoption failure (resistance to change)
- ROI not validated (time savings <50% of target)
- Client cash flow constraints
- Business priorities shift

### Phase 2 → Phase 3 Transition

**GO Decision Criteria:**
- [ ] Inventory system working and trusted (>90% accuracy)
- [ ] Second tech hired successfully (system scales)
- [ ] Lucid Motors contract secured or imminent
- [ ] Operations dashboard used daily
- [ ] Client ready for multi-tech complexity

### Phase 3 → Productization

**GO Decision Criteria:**
- [ ] Plotter Mechanix operating smoothly at scale
- [ ] Kelsey's role shifted from operator to strategic
- [ ] Interest from other businesses validated
- [ ] Platform architecture generalizable
- [ ] Market research supports opportunity

---

## Investment Summary

| Phase | Status | Timeline | Investment | ROI |
|-------|--------|----------|------------|-----|
| Phase 1 | Deployed | 4 weeks | $5,000 | 17-25x ($1,750/mo value) |
| Phase 2 | Internal Review | 4-6 weeks | $15K-$47K (3 tiers) | 248%+ Year 1 ROI |
| Phase 3 | Conceptual | 6-12 months | TBD | TBD |
| Phase 4+ | Vision | Multi-year | TBD | Platform/licensing revenue |

**Phase 1 Credit Incentive:**
- $5K from Phase 1 applies to Phase 2 if signed within 14 days of Phase 1 completion
- Encourages momentum and rewards commitment

---

## Current Status: Phase 1 Deployed, Phase 2 Internal Review

**Phase 1 Outcomes:**
- Quo-Jobber integration deployed and live
- IVR call routing configured (5-extension menu: Service→Kelsey, Supplies→Andrew, Sales→Andrew, Printing→Joe, Accounting→Nikki)
- Kelsey adopted Quo as default phone app
- Kelsey proactively telling customers about call recording

**Phase 2 Status (Jan 28, 2026):**
- Internal team review of 3-tier proposal in progress
- Updated with Jan 27 Kelsey call insights (revenue trajectory, dyslexia constraint, team updates)
- Validation phase planned before client presentation

**Team Updates (from Jan 27 call):**
- Andrew: Fully operational (not ramping) on supplies/sales
- Joe: More capable than assumed (Apache Rental solo, 10yr cutter experience)
- Steve: Permanently off table (personal issues). Pivoting to Michael Maloney / subcontractor model
- Market tailwind: HP competitors on credit hold, driving demand to Kelsey

---

## Key Principles

### 1. Test Before Build
- Week 1 testing validates assumptions
- Data-informed decisions, not guesses
- GO/NO-GO gates at each phase

### 2. Build Trust First
- Phase 1 must succeed before Phase 2
- Small wins create confidence for bigger investments
- Listen to team feedback and adapt

### 3. Measure Everything
- ROI must be demonstrable
- Track inputs (communication capture) and outputs (time saved)
- Use Phase 1 data to inform Phase 2 scope

### 4. Client Leads the Pace
- We propose, client decides when ready
- Respect cash flow and bandwidth
- Flexible scope based on evolving needs

### 5. Long-Term Vision, Short-Term Focus
- Keep Pine Top vision alive
- But execute Phase 1 with complete focus
- Each phase must stand on its own value

---

## Related Documentation

### Phase-Specific
- [Phase 1 Detailed Plan](./phase-1-quick-win-sprint.md)
- [Phase 2 Detailed Roadmap](./phase-2-roadmap.md)
- [Option 4c Technical Spec](./option-4c-recommended-approach.md)
- [Week 1 Testing Checklist](./week-1-testing-checklist.md)

### Client Understanding
- [Kelsey's Jobber Workflow](../audit/kelsey-jobber-workflow.md)
- [Process Map](../audit/process-map.md)
- [Dec 22 Kelsey Onboarding Meeting](../meetings/2025-12-22-kelsey-onboarding/)
- [Dec 22 Internal Team Review](../meetings/2025-12-22-post-onboarding-team-review/)
- [Dec 23 Client Follow-Up](../meetings/2025-12-23-client-meeting/)

### Project Management
- [Deliverables Overview](./README.md)
- [Deliverables Changelog](./CHANGELOG.md)

---

**Last Updated:** January 28, 2026
**Next Review:** After Phase 2 team review completion
**Document Owner:** Trent (Architect)

---

*This roadmap is a living document. Expect changes as we learn, test, and adapt to real-world data.*
