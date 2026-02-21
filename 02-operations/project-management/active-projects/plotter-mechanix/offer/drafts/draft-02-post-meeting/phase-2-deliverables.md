# PlotterOps Phase 2: Transformation
## Deliverables Specification

**Client:** Plotter Mechanix (Chris Andrade)
**Price:** $30,000 (or $25,000 with Phase 1 credit)
**Timeline:** 16 weeks
**Prerequisite:** Successful completion of Phase 1 Quick Win Sprint

---

## Executive Summary

Phase 2 transforms Plotter Mechanix from a founder-dependent operation into a scalable, systematized business. Building on the communication foundation from Phase 1, we deliver three core outcomes:

1. **Working Inventory System** - Real-time visibility into parts and stock
2. **Unified Ops Hub** - Single dashboard connecting all systems
3. **Complete SOP & Training Library** - Chris's 25+ years of knowledge captured and transferable

---

## Context from Phase 1 Discovery

### Why Phase 2 Matters (Client's Words)

**Chris on being the bottleneck:**
> "I'm literally in the burnout phase... I can't continue on this path I'm at."

**Alyssa on inventory:**
> "If I don't know that it's taken out of inventory, then that whole process falls apart."

**Chris on growth blocked:**
> "I could be doing 200 cuts a day for Lucid Motors, but I can't because I'm stuck doing everything myself."

### Current State (Post Phase 1)

| System | Status After Phase 1 |
|--------|---------------------|
| Quo | Live, integrated with Jobber |
| Jobber | Enhanced with call logging |
| Communication | Centralized, nothing falls through |
| SOPs | 4 core workflows documented |
| Chat Agent | Basic query interface operational (stretch goal delivered) |
| Email | Connected, pricing patterns identified (stretch goal delivered) |
| Inventory | Foundation started via call transcript analysis |
| QuickBooks | Fresh start Jan 1, 2026 |
| Shopify | Still disconnected |

### Head Start from Phase 1

Because we over-delivered in Phase 1, you're not starting from zero:

1. **Email Integration Already Connected** - We've been monitoring pricing data in your inbox
2. **Inventory Mentions Tracked** - Quo transcripts flagged for parts/products discussed
3. **Chat Agent Foundation** - The query interface we built expands into the full Ops Hub
4. **Data Patterns Identified** - We know where the inventory problems actually live

This means Phase 2 moves faster. We're not discovering—we're building on what we already learned.

---

## Deliverable 1: Working Inventory System

### The Problem

From the Dec 17 transcript:
- Currently using whiteboard/manual tracking
- "We grab an ink cart off the shelf" - internal use not tracked
- Alyssa can't answer "do we have X?" without calling Chris
- RMA disputes with vendors are time-consuming
- Sister-in-law put together processes but system doesn't support them

**Chris:**
> "I couldn't even find my own products in my database."

### The Solution

A daily-use inventory system tied to actual truck stock and shop inventory.

| Component | Description |
|-----------|-------------|
| **Product Database** | All products with naming convention (C-HP-730-300K format) |
| **Stock Levels** | Real-time quantities by location (shop, truck, on-order) |
| **Usage Tracking** | Log when parts are used (jobs, internal, samples) |
| **Reorder Alerts** | Automatic notifications when stock hits threshold |
| **RMA Tracking** | Track returns, credits, vendor disputes |
| **Cost Visibility** | Know what you paid, what you're charging, margins |

### Integration Points

| System | Integration |
|--------|-------------|
| **Jobber** | Parts used on jobs auto-deduct from inventory |
| **QuickBooks** | Inventory value synced, COGS accurate |
| **Shopify** | Stock levels reflected in online store |
| **Quo** | Call transcripts flag inventory mentions for review |
| **Email** | Vendor pricing updates auto-extracted and applied |
| **Chat Agent** | "Do we have X?" queries answered instantly |

### Building on Phase 1 Foundation

The inventory tracking we started in Phase 1 (as a stretch goal) gives us:
- List of frequently mentioned parts from call transcripts
- Pricing data patterns from vendor emails
- Understanding of RMA and internal use issues

This accelerates the Phase 2 inventory build significantly.

### Success Metrics

| Metric | Target |
|--------|--------|
| Alyssa can answer "do we have X?" | Without calling Chris |
| Stockouts per month | Reduced by 80% |
| Wasted trips (wrong/missing parts) | Reduced by 90% |
| RMA processing time | Under 24 hours |
| Inventory accuracy | 95%+ |

### Naming Convention Integration

Sister-in-law's system will be core to the database:
- Format: `C-HP-730-300K` = Compatible, HP brand, 730 type, 300ml, Black
- All products categorized consistently
- Searchable by any attribute

---

## Deliverable 2: Unified Ops Hub

### The Problem

From the Dec 17 transcript:

**Current systems are disconnected:**
- Jobber (jobs, scheduling)
- QuickBooks (accounting) - fresh start Jan 1, 2026
- Shopify ("sitting out there in La La Land")
- Capsule (old CRM with contact database)
- Dropbox (files everywhere)
- Outlook (Alyssa manages, Chris ignores when overwhelmed)

**Chris:**
> "Every piece of technology I've added has added a bigger headache."

**Alyssa:**
> "If I knew everything he did" - the communication gap is the #1 issue

### The Solution

A "command center" dashboard that unifies data from all systems into a single, actionable view.

### Expanding the Chat Agent

The chat interface we built in Phase 1 becomes the foundation of the Ops Hub. Instead of a traditional dashboard you have to navigate, you can ask questions in plain English:

**Phase 1 capability:**
- "What calls came in today?"
- "Show me unhandled messages"

**Phase 2 expansion:**
- "Do we have HP 730 ink in stock?"
- "What's our revenue this month?"
- "Show me everything about ABC Printing"
- "What jobs are scheduled for tomorrow?"
- "Which invoices are overdue?"

Same familiar interface—now connected to everything.

| Component | Description |
|-----------|-------------|
| **Job Dashboard** | Today's jobs, upcoming, overdue - from Jobber |
| **Financial Snapshot** | Revenue, outstanding invoices, cash flow - from QuickBooks |
| **Inventory Status** | Low stock alerts, on-order items, cost summary |
| **Communication Log** | Recent calls, messages, action items - from Quo/Jobber |
| **Customer 360** | Full history when looking up any client |
| **Chat Interface** | Query any of the above in plain English |

### Key Features

**For Chris:**
- Morning briefing (hot tub review): What happened yesterday, what's today, what's overdue
- Voice-accessible queries: "What jobs do I have tomorrow?"
- Alerts only for things that need attention

**For Alyssa:**
- Invoice queue with all context attached
- Customer lookup with full history
- Inventory questions answered without calling Chris

**For Joe:**
- Daily schedule and delivery routes
- Job details and customer history
- Parts needed for each job

### Integration Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    UNIFIED OPS HUB                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Jobber  │  │QuickBooks│  │ Shopify │  │  Quo    │        │
│  │  API    │  │   API   │  │   API   │  │  API    │        │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │
│       │            │            │            │              │
│       └────────────┴────────────┴────────────┘              │
│                         │                                   │
│                    ┌────┴────┐                              │
│                    │  N8N    │                              │
│                    │ Backend │                              │
│                    └────┬────┘                              │
│                         │                                   │
│            ┌────────────┼────────────┐                      │
│            │            │            │                      │
│       ┌────┴────┐  ┌────┴────┐  ┌────┴────┐                │
│       │Dashboard│  │  Chat   │  │ Alerts  │                │
│       │   UI    │  │Interface│  │ System  │                │
│       └─────────┘  └─────────┘  └─────────┘                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Success Metrics

| Metric | Target |
|--------|--------|
| Time to find customer info | Under 30 seconds |
| Systems Chris needs to check daily | 1 (the hub) |
| Data entry duplication | Eliminated |
| Morning review time | Under 15 minutes |

---

## Deliverable 3: Complete SOP & Training Library

### The Problem

From the Dec 17 transcript:

**Chris is single point of failure:**
> "There's maybe 5-10 people in Arizona" with his expertise
> "I fix things with a paperclip that would cost $5,000"

**Knowledge not documented:**
> "I don't put my notes in. So it's like, I don't know where to look sometimes to find the answer."

**Training is manual:**
- Joe is new (~2 months), still learning
- Every new hire requires Chris's direct involvement
- No way to scale technician capacity

### The Solution

A complete knowledge base capturing Chris's 25+ years of expertise, structured for training and daily reference.

| Component | Description |
|-----------|-------------|
| **Core Workflow SOPs** | Every repeatable process documented |
| **Technical Knowledge Base** | Printer-specific troubleshooting guides |
| **Training Curriculum** | Structured path for new technicians |
| **Video Library** | Visual guides for complex procedures |
| **Searchable Database** | Find answers by symptom, machine, or keyword |

### SOP Categories

**Field Service:**
- Service call execution (expanded from Phase 1)
- Diagnostic procedures by machine type
- Common repairs and fixes
- Customer communication standards
- Safety protocols

**Operations/Admin:**
- Invoice processing (expanded from Phase 1)
- Dispatch and routing (expanded from Phase 1)
- Inventory management
- RMA processing
- Vendor communications

**Sales:**
- Quote generation
- Pricing guidelines
- Customer qualification
- Rental program procedures
- Ink line sales process

**Technical Reference:**
- HP printer troubleshooting
- Roland equipment guides
- Laminator setup and maintenance
- Plotter calibration procedures
- Error code reference

### Passive Knowledge Capture (Expanded)

Building on Phase 1 foundation:

**Chris's vision:**
> "If I could literally have a camera on me and go out all day... and then just let it record me while I go in there."

**Implementation:**
1. Insta360 cameras on lanyard (low friction)
2. Audio recordings during service calls
3. Automated transcription and categorization
4. AI-assisted SOP generation
5. Review and polish by team

**YouTube Integration:**
- Chris already has videos with "hundreds of thousands of views"
- Integrate existing content into knowledge base
- Create internal versions of popular tutorials

### Success Metrics

| Metric | Target |
|--------|--------|
| Core workflows documented | 100% |
| New tech training time | Reduced by 50% |
| "Ask Chris" interruptions | Reduced by 70% |
| Knowledge searchable | Any topic in under 1 minute |
| Chris required for training | Only advanced topics |

---

## Value Justification

### Lever 1: Founder Time Recovery

**Current state:** Chris is in the field 40+ hours/week, handling every service call personally.

**After Phase 2:** Chris can delegate standard work, focus on high-value activities.

| Activity | Current | After Phase 2 |
|----------|---------|---------------|
| Field service calls | 40+ hrs/week | 20 hrs/week |
| Training new techs | Direct involvement | SOPs + videos |
| Answering "do we have X?" | Multiple times/day | Zero (Alyssa checks system) |
| Strategic work (Lucid, rentals) | No time | 10+ hrs/week |

**Value:** If Chris's time is worth $175/hr (his consulting rate), recovering 20 hrs/week = **$182,000/year** in capacity.

### Lever 2: Error & Waste Reduction

**Current hidden costs:**
- Wasted trips (wrong/missing parts)
- Rush shipping for stockouts
- Rework from miscommunication
- Lost jobs from dropped balls

**Industry estimate:** 5-10% of revenue in hidden operational waste.

**After Phase 2:** Tight systems, real-time inventory, clear communication.

**Value:** Even 5% of a $500K business = **$25,000/year** recovered.

### Lever 3: Growth Unlock

**Currently blocked opportunities:**

| Opportunity | Blocked By | Phase 2 Enables |
|-------------|------------|-----------------|
| Lucid Motors (200 cuts/day) | Chris as bottleneck | Capacity through SOPs + training |
| Rental program expansion | No systematic process | Documented, repeatable program |
| Ink line scaling | Manual order processing | Automated, integrated flow |
| Remote consulting | No way to delegate field work | Trained techs handle standard calls |

**Chris's rental revenue:** $35K from ONE customer, not actively marketed.

**Value:** Unlocking even one of these = **$50,000-200,000/year** additional revenue potential.

### Lever 4: Risk Reduction

**Current risk:** Chris is single point of failure with 25+ years of knowledge.

> "I've been bit by all the people I brought into my little circle."

**After Phase 2:**
- Knowledge captured and transferable
- Systems run without Chris present
- Business has value beyond founder
- Exit or scale options available

**Value:** Business valuation multiplier improvement = **6-figure asset protection**.

---

## Timeline: 16 Weeks

### Weeks 1-4: Foundation

| Week | Focus | Deliverables |
|------|-------|--------------|
| 1 | Kickoff, system access, data audit | Project plan, access confirmed |
| 2 | Product database setup | Naming convention implemented |
| 3 | Inventory system build | Basic tracking functional |
| 4 | QuickBooks integration | Inventory synced to accounting |

### Weeks 5-8: Integration

| Week | Focus | Deliverables |
|------|-------|--------------|
| 5 | Jobber-inventory connection | Parts auto-deduct from jobs |
| 6 | Shopify integration | Online stock levels accurate |
| 7 | Unified dashboard v1 | Basic hub functional |
| 8 | Testing and refinement | Team using system daily |

### Weeks 9-12: Knowledge Capture

| Week | Focus | Deliverables |
|------|-------|--------------|
| 9 | SOP expansion (field service) | 10+ technical SOPs |
| 10 | SOP expansion (operations) | Complete admin workflows |
| 11 | Video library foundation | 5+ training videos |
| 12 | Knowledge base launch | Searchable system live |

### Weeks 13-16: Polish & Training

| Week | Focus | Deliverables |
|------|-------|--------------|
| 13 | Dashboard v2 | Full feature set |
| 14 | Training curriculum | Structured learning path |
| 15 | Team training | Chris, Alyssa, Joe certified |
| 16 | Handoff and documentation | Complete system delivered |

---

## Guarantee

> "If by week 16 we haven't delivered (1) a working inventory system in daily use, (2) a unified ops/comms hub, and (3) a complete SOP & training library for your core workflows—**and you've done your part**—we'll continue working with you at no extra fee for up to 6 months total until those are in place."

---

## Credit Mechanic

If signed within 14 days of Phase 1 completion, the **full $5,000 from Phase 1 applies as a credit** toward the $30,000 Phase 2 investment.

**Effective price:** $25,000 for the complete transformation.

---

## What's NOT Included (Phase 3/4)

These are future Expansion Sprints ($10K each):

| Item | Why Deferred |
|------|--------------|
| Lucid Motors operational readiness | Requires Phase 2 foundation |
| Customer portal | Nice-to-have, not core |
| Rental program automation | Build process first, automate later |
| Ink line e-commerce automation | Needs inventory system first |
| AI quote generation | Requires stable pricing data |
| Remote diagnostics system | Advanced capability |

---

## The Vision: Plotter Mechanics Hub

Phase 2 is the core of what becomes the "Plotter Mechanics Hub"—proprietary software that could eventually be productized.

**Chris's dream:**
> "Sitting at Pine Top drinking on your coffee in the mornings on your balcony... all you have to do is just make phone calls and get paid."

**Matthew's promise:**
> "You're putting the money in to build this system, this ecosystem that we are going to turn into Plotter Mechanics software down the road."

Phase 2 makes the Pine Top vision possible. Phase 3+ makes it a reality.

---

## Next Steps (After Phase 1 Success)

1. **Day 30 Review:** Present Phase 2 proposal
2. **Credit Window:** 14 days to lock in $5K credit
3. **Kickoff:** Begin Phase 2 immediately after Phase 1 wrap
4. **Timeline:** 16 weeks to full transformation

---

*Prepared by Arise Group AI*
*Trent Christopher | Matthew Kerns | Mekaiel Abdullahi*
