# Plotter Mechanix Phase 2 Plan

**Created:** January 24, 2026
**Updated:** January 24, 2026
**Status:** Planning
**Investment:** $10,000 (ROI-justified)
**Depends On:** Phase 1 Quo-Jobber integration live testing (starting Jan 25-26)

---

## Executive Summary

Phase 2 builds the **infrastructure for Kelsey to scale** - enabling him to hire technicians, free his time from low-income tasks, and focus on high-value work and eventually more personal freedom.

**The Core Outcome:** Kelsey can train new technicians WITHOUT being in the room.

**Key Strategic Principles:**
- **Megan is leading Ply** - we complement, not compete. Interview to find gaps.
- **Andrew has his process** - let him cook. Interview to find where we help.
- **Training system is the anchor** - Chris filming Kelsey creates the scalability engine.
- **ROI-justified pricing** - $10k investment against $142k+ annual value.

---

## Phase 1 Status (Foundation)

### Completed
- [x] Vonage → Quo phone migration
- [x] Quo IVR/menu system configured
- [x] N8N Quo-to-Jobber integration built
- [x] AI-powered call summaries (name, equipment, issues, next steps)
- [x] Contact matching logic (Jobber → Quo → Conversation hierarchy)
- [x] Rollback procedure documented

### In Progress (This Weekend)
- [ ] Deploy N8N integration to production Jobber account
- [ ] Create Alyssa SOP for flagging AI errors
- [ ] Complete Jobber contact backup pre-deployment
- [ ] A2P registration completion (pending Quo)

### Phase 1 Success Criteria
- AI transcription accuracy validated by Alyssa over 1-2 weeks
- No data corruption in Jobber contacts
- Kelsey can trust incoming request summaries

---

## Phase 2 Deliverables

### 1. Discovery Interviews (Included)

#### 1.1 Megan Interview - Ply Assessment
**Purpose:** Understand Megan's Ply setup, identify gaps we can fill

**Questions to Answer:**
- How far along is Ply implementation?
- What's working well? What's frustrating?
- How is Ply integrated with Jobber currently?
- What's NOT covered by Ply that the business needs?
- Why aren't the SOPs she created being followed?
- Where can we add value without duplicating her work?

**Background on Ply:**
Ply is AI-powered inventory software for trades with native Jobber integration:
- Auto-syncs materials, jobs, and technicians
- Real-time webhooks (no manual sync)
- Material reservation on job booking
- Mobile POs and cycle counts
- Expense tracking in Jobber

**Ply Gaps We Can Fill:**
| Ply Does | Ply Doesn't Do | Our Opportunity |
|----------|----------------|-----------------|
| Parts inventory | Equipment serial #s | Equipment CRM |
| Job material tracking | Maintenance history | Service history database |
| Stock alerts | Used parts from parted machines | Revenue recovery system |
| Jobber sync | Quo call context | Inventory in call screen |
| Standard trades workflow | Printer-specific needs | Custom configuration |

#### 1.2 Andrew Interview - Supplies Process Map
**Purpose:** Understand Andrew's approach, find where we help without getting in his way

**Questions to Answer:**
- What's your vision for the supplies side of the business?
- Walk us through your ideal sales process
- What tools do you need that you don't have?
- How will you track leads and follow-ups?
- What's your pricing/margin strategy?
- Where would automation help vs. slow you down?
- How do you want to coordinate with Alyssa/Kelsey?

**Our Role:** Enablement, not control. Andrew owns the process.

---

### 2. Training System (MAJOR DELIVERABLE) - $4,000

**The Big Bet:** This is what enables Kelsey to scale.

**Problem:**
> "I'm so exhausted of pouring myself into people. Joe is the last dude I'm pouring myself into." - Kelsey

**Current State:**
- All knowledge in Kelsey's head
- Training requires Kelsey's physical presence
- Megan created SOPs that aren't followed
- Can't hire new techs without massive Kelsey time investment

**Solution:** Video-based training library with Chris as producer

#### 2.1 Content Capture System
**Chris's Role:** Film Kelsey during service calls, repairs, procedures

**Equipment Needed:**
- Wearable camera (GoPro or similar)
- Lapel mic for audio
- Simple editing workflow
- Cloud storage (Dropbox folder already planned)

**Initial Content Library (Phase 2 Target):**
| Video Category | Count | Examples |
|----------------|-------|----------|
| Truck loading/prep | 3-5 | Daily checklist, parts organization |
| Common repairs | 10-15 | Top service calls by frequency |
| Troubleshooting | 5-10 | Diagnostic decision trees |
| Customer interaction | 3-5 | How Kelsey handles difficult situations |
| Equipment-specific | 5-10 | Most common printer models |

#### 2.2 Knowledge Base Structure
```
Plotter Mechanics Training Hub
├── Getting Started
│   ├── Day 1 orientation
│   ├── Truck setup
│   └── Tool inventory
├── Service Procedures
│   ├── By equipment type
│   ├── By repair type
│   └── Troubleshooting guides
├── Customer Communication
│   ├── Call scripts
│   ├── Difficult situations
│   └── Upsell opportunities
├── SOPs (Megan's + New)
│   ├── Daily procedures
│   ├── Inventory management
│   └── Jobber/Ply workflows
└── Quick Reference
    ├── Part numbers
    ├── Supplier contacts
    └── Pricing guides
```

#### 2.3 SOP Enforcement Analysis
**Why Megan's SOPs Aren't Followed:**
- Interview Alyssa, Joe, Kelsey to understand
- Identify: Is it tool issue? Training issue? Culture issue?
- Design enforcement mechanisms into workflow

**Deliverable:** Recommendations for SOP adoption with implementation plan

#### 2.4 Success Metrics
| Metric | Current | Phase 2 Target |
|--------|---------|----------------|
| Training videos | 0 | 25-30 |
| SOP compliance | Low | Measured baseline |
| Joe solo call capability | ~10% | 40%+ |
| Time to train new tech | Weeks of Kelsey time | Days + video library |

---

### 3. Equipment CRM (Ply Gap Filler) - $2,000

**Problem:** Ply tracks inventory, but NOT equipment history.

> "The business lacks a system for tracking critical client data like serial numbers and maintenance history"

**What We Build:**

```
Customer → Equipment Records
├── Serial Number
├── Model / Make
├── Install Date
├── Meter Readings (track over time)
├── Maintenance History
│   ├── Date
│   ├── Work performed
│   ├── Parts used (links to Ply)
│   └── Tech who did work
├── Service Contract Status
│   ├── Eligible / Not eligible
│   ├── Eligibility score
│   └── Risk factors
└── Notes / Flags
```

**Integration Points:**
- Links to Jobber clients
- Surfaces in Quo call context (when customer calls, see their equipment)
- Informs service contract eligibility matrix
- Enables proactive maintenance outreach

**Implementation:** Likely Notion database or Airtable, connected via n8n

---

### 4. Ply Enhancement Layer - $2,500

**Purpose:** Fill gaps that Ply doesn't cover, working WITH Megan's setup

**Enhancements:**

#### 4.1 Used Parts Tracking
**Problem:** Parted machines have valuable parts with no tracking
> "$1,200 power supplies from parted-out machines lost without system"

**Solution:**
- Inventory category for "used/refurbished" parts
- Source tracking (which machine it came from)
- Condition grading
- Pricing for resale

**ROI:** $5k-15k/year in recovered value

#### 4.2 Quo ↔ Inventory Context
**Problem:** When customer calls, Alyssa doesn't know if parts are in stock

**Solution:** Surface Ply inventory status in Quo call handling
- Customer calls about Model X
- Alyssa sees: "Parts in stock: Yes/No"
- Reduces "let me check and call you back"

#### 4.3 Custom Workflow Configuration
**Problem:** Ply built for plumbing/HVAC, not printer service

**Solution:** Work with Megan to configure:
- Custom categories for printer parts vs. consumables
- Workflow adjustments for their unique service model
- Integration testing and optimization

---

### 5. Integration Work - $1,500

**Purpose:** Connect the pieces that don't talk to each other

**Integrations:**
| From | To | Purpose |
|------|-----|---------|
| Quo calls | Equipment CRM | Show customer equipment during calls |
| Ply inventory | Quo context | "Do we have X?" answered instantly |
| Training completions | Dashboard | Track Joe's progress |
| Equipment CRM | Jobber | Link equipment to jobs |

**Implementation:** n8n workflows building on Phase 1 infrastructure

---

## ROI Justification

### Investment: $10,000

### Annual Value Created

| Workstream | Conservative | Moderate | Source |
|------------|--------------|----------|--------|
| **Training System** | $50,000 | $75,000 | Kelsey time saved training |
| **Equipment CRM** | $35,000 | $55,000 | Contract eligibility, retention |
| **Ply Enhancements** | $15,000 | $25,000 | Used parts, efficiency |
| **Integrations** | $25,000 | $35,000 | "Do we have X?" elimination |
| **TOTAL** | **$125,000** | **$190,000** | |

### ROI Calculation

| Metric | Value |
|--------|-------|
| Investment | $10,000 |
| Conservative Annual Value | $125,000 |
| **ROI** | **1,150%** |
| **Payback Period** | **< 1 month** |

### The Real ROI: Scalability

The training system isn't just about saving Kelsey's time - it's about **unlocking growth**:

| Without Training System | With Training System |
|------------------------|---------------------|
| Kelsey trains every tech personally | Techs self-train with videos |
| Weeks of Kelsey time per hire | Days + video library |
| Can't hire Steve (no bandwidth) | Steve onboards independently |
| Business limited by Kelsey's hours | Business scales beyond Kelsey |
| "If I don't come to work, we make no money" | Team operates without Kelsey daily |

---

## Team Roles (Post Phase 2)

| Person | Primary Focus | Change from Today |
|--------|---------------|-------------------|
| **Kelsey** | High-value service, content creation, business development | Training new techs via video, not in-person |
| **Alyssa** | Admin, invoicing, call handling, inventory checks | Instant inventory answers via Ply + Quo |
| **Andrew** | Supplies sales, service contracts (his process) | Tools to execute his vision |
| **Megan** | Ply administration, SOP maintenance | We support her setup, fill gaps |
| **Joe** | Field support, training progression | Video-based skill building |
| **Steve** | Routine service (when hired) | Onboards via training system |
| **Chris** | Content production, filming | Creates the training library |

---

## Implementation Timeline

**Duration:** 4-6 weeks (compressed delivery)

### Week 1: Discovery & Foundation
- [ ] Megan interview - Ply assessment
- [ ] Andrew interview - supplies process map
- [ ] Audit: Why SOPs aren't followed
- [ ] Equipment CRM design + initial build
- [ ] Training system architecture
- [ ] Chris filming setup (equipment, workflow)

**Deliverables:**
- Interview summaries with recommendations
- SOP adoption analysis
- Equipment CRM schema + database shell
- Training content plan + Chris ready to film

### Week 2-3: Parallel Build (Equipment CRM + Training Videos)
- [ ] Equipment CRM populated with top 30 customers
- [ ] Used parts tracking implemented
- [ ] First 15 training videos captured
- [ ] Knowledge base structure built
- [ ] Megan collaboration on Ply config

**Deliverables:**
- Equipment database operational with top customers
- Used parts inventory category live
- 15 training videos accessible
- Knowledge base framework

### Week 4-5: Integration + Content Expansion
- [ ] Quo ↔ inventory context connected
- [ ] All system integrations connected
- [ ] 10+ additional training videos
- [ ] SOP enforcement mechanisms
- [ ] Equipment CRM completed (all customers)

**Deliverables:**
- Inventory visible in call context
- Fully integrated systems
- 25+ total training videos
- Complete equipment records

### Week 6: Training, Testing & Handoff (Optional Polish Week)
- [ ] Team training on all new systems
- [ ] Final training videos if needed
- [ ] System testing and refinement
- [ ] Steve onboarding materials ready

**Deliverables:**
- Team confident using everything
- All systems validated and documented
- **Steve onboarding ready**

**Timeline Flexibility:**
- **Aggressive:** 4 weeks (Weeks 1-5, skip Week 6 polish)
- **Standard:** 5 weeks (Weeks 1-5, light Week 6)
- **Conservative:** 6 weeks (full timeline with polish)

---

## Success Metrics

| Metric | Current | Phase 2 Target |
|--------|---------|----------------|
| Training videos | 0 | 25-30 |
| Joe solo call capability | ~10% | 40%+ |
| "Do we have X?" time | Multiple calls/day | Instant answer |
| Equipment records | 0 | Top 50 customers |
| Used parts tracked | $0 | $5k+ value catalogued |
| SOP compliance | Low | Baseline + improvement |
| Ready to hire Steve | No | **Yes** |

---

## Dependencies & Risks

### Dependencies
- [ ] Phase 1 Quo-Jobber integration stable
- [ ] Megan available for interview + collaboration
- [ ] Andrew available for interview
- [ ] Chris committed to filming role
- [ ] Kelsey willing to be filmed

### Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Megan feels stepped on | Interview first, position as support |
| Andrew doesn't need our help | Interview confirms, adjust scope |
| Kelsey uncomfortable on camera | Start small, build comfort |
| Ply doesn't integrate well | Custom workarounds via n8n |
| Videos don't get watched | Tie to onboarding, measure usage |

---

## Pricing

### Phase 2 Investment: $10,000

| Deliverable | Investment |
|-------------|------------|
| Discovery Interviews (Megan, Andrew) | Included |
| Training System Build | $4,000 |
| Equipment CRM | $2,000 |
| Ply Enhancement Layer | $2,500 |
| Integration Work | $1,500 |
| **TOTAL** | **$10,000** |

### Payment Terms
- 50% upfront ($5,000)
- 50% on completion ($5,000)

### Phase 1 Credit
If Phase 2 signed within 14 days of Phase 1 completion: **$2,500 credit applied**
Net investment: **$7,500**

---

## The Pitch

> "Kelsey, right now if you want to hire Steve, you have to train him yourself. That's weeks of your time at $300+/hour that you're not billing.
>
> Phase 2 builds a training system where Chris films you doing what you already do. New techs learn by watching you - without you being in the room.
>
> That's what gets you to Pinetop.
>
> Investment: $10,000. ROI: 10x+ in Year 1. Payback: Less than a month.
>
> More importantly: this is the difference between a job and a business."

---

## Immediate Next Steps

### This Weekend (Jan 25-26)
1. [ ] Deploy N8N integration to production Jobber
2. [ ] Create Alyssa AI error flagging SOP
3. [ ] Backup Jobber contacts pre-deployment

### Week of Jan 27
1. [ ] Monitor Phase 1 AI transcription accuracy
2. [ ] Schedule Megan interview
3. [ ] Schedule Andrew interview
4. [ ] Begin Equipment CRM design

### Week of Feb 3
1. [ ] Phase 1 success validation
2. [ ] Present Phase 2 proposal with ROI
3. [ ] Conduct Megan + Andrew interviews
4. [ ] Chris filming setup

---

## Related Documents

- [Phase 1 PRD v1.2](../planning/phase-1-prd-v1.2.md)
- [Phase 2 Roadmap (Dec 23)](../deliverables/phase-2-roadmap.md)
- [ROI Calculator Framework](../../../../agency-operations/roi-calculator/roi-calculator-framework.md)
- [MHF-CEF Framework](../../../../agency-operations/roi-calculator/mhf-build/MHF-CEF-Framework-v0.1.md)
- [Discovery Findings](../discovery/DISCOVERY-FINDINGS.md)

---

*Last Updated: January 24, 2026*
