# Dev Requirements: Sales-to-Development Alignment Gaps

**Document ID:** ARISE-DEV-001
**Version:** 1.1
**Created:** February 16, 2026
**Updated:** February 16, 2026 (aligned with Mekaiel-Matthew sync meeting)
**Author:** Mekaiel (Sales) comparing to Matthew's Development Framework
**Purpose:** Identify gaps between current sales process and development requirements

---

## Meeting Context (Feb 2026)

This document incorporates decisions from the Mekaiel-Matthew collaboration sync:

| Decision | Status |
|----------|--------|
| Unified Sales-Dev Collaboration SOP | ✓ Exists (SOP-SD-001) |
| Defined Deliverables (Presentation → Proposal → SOW) | ✓ Exists (SOP-SL-001) |
| Centralized Notion Storage | ⏳ Action item |
| Clear Document Ownership (Sales leads, Dev inputs) | ✓ Exists (SOP-SD-001) |
| Consolidate Dev Inputs (remove redundancies) | 🔄 In progress |
| Automated Transcript Processing | 🔮 Future vision |

---

## Executive Summary

This document compares our current Sales SOPs against Matthew's Development Framework to identify what's missing on the sales side that dev needs before building.

**What's Already Aligned:**
- Deliverables structure (Presentation → Proposal → SOW)
- Document ownership (Sales owns docs, Dev provides inputs)
- Joint call participation
- Basic tech questionnaire

**Templates Created (P1 + P2):**
- ✅ Metrics discovery template
- ✅ MoSCoW prioritization
- ✅ Change request process
- ✅ Problem statement template
- ✅ Pricing calculator
- ✅ Milestone payment terms

**Still Needs Work (P3/P4):**
- Billable discovery (pricing decision)
- Vibe coding training
- Functional requirements template
- Quality gate checklists

**Matthew's Framework Location:** `shared-resources/matthew-repos/ai-agency-development-os/claude-code-os-implementation/03-ai-growth-engine/development-framework/`

---

## Gap Analysis

### GAP 1: Billable Discovery Calls

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| Free discovery calls to qualify | $500/hr diagnostic calls that bill for time | **MISSING** |

**Matthew's Framework Says:**
> "This is a billable diagnostic session at $500/hour where we'll diagnose your specific problem, identify potential solutions, and if appropriate, create a quick prototype."

**Why It Matters:**
- Sets value expectation from the start
- Filters out non-serious prospects
- Generates revenue during sales process
- Covers time investment in vibe coding

**Action Required:**
- [ ] Update discovery call script to position as billable diagnostic
- [ ] Create billing workflow for diagnostic sessions
- [ ] Update pricing in sales materials

---

### GAP 2: Metrics Discovery (KPIs + Baselines)

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| "Success criteria" mentioned vaguely | Structured KPI capture with current baselines and target values | **MISSING** |

**Matthew's Framework Says:**
> "Before exploring solutions, establish how we will measure success."

**Required Template:**
```markdown
## Success Metrics (Agreed During Call)
| KPI | Current Baseline | Target | How We Measure | Timeframe |
|-----|-----------------|--------|----------------|-----------|
| [Metric 1] | [Current] | [Target] | [Method] | [30/60/90 days] |
| [Metric 2] | [Current] | [Target] | [Method] | [30/60/90 days] |

ROI Estimate: $[monthly savings] x 12 = $[annual] vs $[project cost]
Payback Period: ~[X] months
```

**Why It Matters:**
- Metrics flow into PRD, test plan, and final delivery review
- Objective proof of delivered value
- Enables ROI-based selling
- Prevents "scope creep" by defining success upfront

**Action Required:**
- [ ] Add Metrics Discovery section to discovery call script
- [ ] Create Metrics Requirements Template
- [ ] Add to handoff checklist (must have before proposal)

---

### GAP 3: Vibe Coding Prototype

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| No prototyping during sales | 15-30 min vibe coding to validate approach | **MISSING** |

**Matthew's Framework Says:**
> "Live Prototype (15 minutes) - When to vibe code: Complex logic needs validation, visual interface demonstration, API integration feasibility, client needs to see it to believe it."

**Why It Matters:**
- "Seeing is believing" for clients
- Validates technical feasibility before quoting
- Feeds complexity scoring for pricing
- Creates artifact to send post-call

**Action Required:**
- [ ] Train on vibe coding process
- [ ] Add VS Code / dev environment to call setup checklist
- [ ] Create vibe code handoff process (code to Matthew for review)

---

### GAP 4: Problem Statement Template

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| Freeform discovery notes | Structured Current Situation + Desired Outcome template | **PARTIAL** |

**Matthew's Framework Template:**
```markdown
## Current Situation
- **What**: [What they do manually today]
- **Who**: [Who does it]
- **When**: [How often]
- **Time**: [How long it takes]
- **Cost**: [Implied cost of this time]

## Desired Outcome
- **Goal**: [What they want instead]
- **Success**: [How they measure success]
- **Timeline**: [When they need it]
- **Budget**: [Range if known]
```

**Why It Matters:**
- Standardized format for dev handoff
- Ensures all critical info captured
- Feeds directly into PRD

**Action Required:**
- [ ] Create Problem Statement Template
- [ ] Add to Notion discovery template
- [ ] Update discovery call script to fill this

---

### GAP 5: MoSCoW Requirements Prioritization

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| "Criteria" and "scope" defined loosely | MUST/SHOULD/COULD/WON'T prioritization | **MISSING** |

**Matthew's Framework:**
```markdown
## MUST Have (Phase 1 - Critical)
- [ ] Core functionality that solves main problem
- [ ] Basic authentication/security
- [ ] Primary integration
- [ ] Essential error handling

## SHOULD Have (Phase 2 - Important)
- [ ] Enhanced features
- [ ] Additional integrations
- [ ] Reporting/analytics

## COULD Have (Phase 3 - Nice)
- [ ] Convenience features
- [ ] UI polish

## WON'T Have (Out of scope)
- [ ] Explicitly excluded items
```

**Why It Matters:**
- Clear prioritization prevents scope creep
- Enables phased delivery
- Sets expectations with client
- Feeds directly into milestone planning

**Action Required:**
- [ ] Create MoSCoW template for proposals
- [ ] Add to proposal creation workflow
- [ ] Train team on MoSCoW methodology

---

### GAP 6: Complexity Scoring + Pricing Formula

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| "Hours estimate" from dev | Complexity tier with multipliers and pricing formula | **MISSING** |

**Matthew's Framework:**

| Complexity Tier | Production Multiplier | Timeline | Risk Factor |
|----------------|----------------------|----------|-------------|
| Simple (0-5 pts) | 40-60x vibe time | 1-2 weeks | 1.0x |
| Standard (6-15 pts) | 60-100x vibe time | 2-4 weeks | 1.2x |
| Complex (16-25 pts) | 100-160x vibe time | 4-8 weeks | 1.5x |
| Enterprise (26-40 pts) | 160-240x vibe time | 8-16 weeks | 1.8x |
| Major Build (40+ pts) | 240x+ vibe time | 16+ weeks | 2.0x |

**Pricing Formula:**
```
Base Hours = Σ(Feature Development Hours)
Testing = Base Hours × 0.3
Documentation = Base Hours × 0.1
Project Management = Base Hours × 0.15
Buffer = Base Hours × 0.25

Total Hours = Base + Testing + Documentation + PM + Buffer

Developer Cost = Total Hours × Developer Rate
Architect Margin = Developer Cost × 0.4
Sales Fee = Developer Cost × 0.15
Infrastructure = Fixed or % based

Client Price = Developer Cost + Architect Margin + Sales Fee + Infrastructure
```

**Why It Matters:**
- Consistent pricing across deals
- Protects margins (>40% target)
- Risk-adjusted estimates
- Clear formula for team alignment

**Action Required:**
- [ ] Create Pricing Calculator tool
- [ ] Add complexity scoring to vibe coding workflow
- [ ] Update proposal template with pricing breakdown

---

### GAP 7: Milestone-Based Payment Structure

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| "Contract signed" = payment | Milestone payments with work-to-payment ratio | **PARTIAL** |

**Matthew's Framework:**
```
MILESTONE 1: Foundation (25% of project)
├── Core infrastructure
├── Basic functionality
├── Proof of concept
└── Payment: 30% of total

MILESTONE 2: Full Feature (50% of project)
├── Complete functionality
├── All integrations
├── Error handling
└── Payment: 50% of total

MILESTONE 3: Polish & Deploy (25% of project)
├── UI refinement
├── Performance optimization
├── Documentation & training
└── Payment: 20% of total
```

**Payment Rules:**
- Net 15 from milestone approval
- 1.5% monthly late fee
- Work stops at 30 days late
- Code remains our property until paid

**Why It Matters:**
- Reduces cash flow risk
- Clear deliverables per payment
- Client has exit points (reduced risk for them)
- Payment gates ensure continuous commitment

**Action Required:**
- [ ] Create Milestone Planning Template
- [ ] Add payment terms to SOW template
- [ ] Update proposal template with milestone structure

---

### GAP 8: Functional Requirements Template

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| Developer Review Document (dev-focused) | User Story + Acceptance Criteria + Technical Notes | **PARTIAL** |

**Matthew's Framework (Per Feature):**
```markdown
## Feature: [Name]

### User Story
As a [user type]
I want to [action]
So that [outcome]

### Acceptance Criteria
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

### Technical Notes
- API: [Required endpoints]
- Data: [Fields needed]
- Rules: [Business logic]

### Effort Estimate
- Development: X hours
- Testing: X hours
- Total: X hours
```

**Why It Matters:**
- Clear definition of done
- Testable acceptance criteria
- Technical spec for builders
- Effort tied to feature

**Action Required:**
- [ ] Create Functional Requirements Template
- [ ] Add to proposal/PRD workflow
- [ ] Train on user story writing

---

### GAP 9: Technical Requirements Checklist

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| Tech questionnaire (basic) | Comprehensive technical requirements checklist | **PARTIAL** |

**Matthew's Framework Checklist:**

**Data Requirements:**
- [ ] Data sources identified
- [ ] Data formats specified
- [ ] Volume estimates noted
- [ ] Retention policies defined

**Integration Requirements:**
- [ ] External systems listed
- [ ] API documentation reviewed
- [ ] Authentication methods confirmed
- [ ] Rate limits understood

**Performance Requirements:**
- [ ] Expected user count
- [ ] Concurrent usage
- [ ] Response time expectations
- [ ] Data processing volumes

**Security Requirements:**
- [ ] Authentication needs
- [ ] Authorization levels
- [ ] Data encryption requirements
- [ ] Compliance needs (HIPAA, GDPR, etc.)

**Action Required:**
- [ ] Expand tech questionnaire with these items
- [ ] Create Technical Requirements Checklist
- [ ] Add to pre-proposal gate

---

### GAP 10: Change Request / Scope Creep Prevention

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| Not addressed | Formal change request process | **MISSING** |

**Matthew's Framework:**
```
1. Client requests change
2. Document the request
3. Assess impact:
   - Time impact
   - Cost impact
   - Risk impact
4. Present options:
   - Option A: Add to Phase 2 (no current impact)
   - Option B: Swap with existing feature
   - Option C: Extend timeline and budget
5. Get written approval
```

**Response Templates:**
| Client Says | You Respond |
|-------------|-------------|
| "Can we also add..." | "Great idea! Let's add that to Phase 2." |
| "Just a quick change..." | "Let me assess the impact and get back to you." |
| "While you're at it..." | "I'll note that for our next milestone planning." |
| "I assumed it included..." | "Let's review our documented requirements." |

**Why It Matters:**
- Protects scope and timeline
- Maintains profitability
- Professional boundary-setting
- Written trail for disputes

**Action Required:**
- [ ] Create Change Request SOP
- [ ] Add to client onboarding
- [ ] Train team on responses

---

### GAP 11: Quality Gates (Phase Exit Criteria)

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| Handoff procedures | Explicit phase exit checklists | **PARTIAL** |

**Matthew's Framework - Pre-Development Checklist:**
```markdown
## Requirements Confirmed
- [ ] All MUST haves documented
- [ ] Acceptance criteria defined
- [ ] Technical approach validated
- [ ] Integrations confirmed possible
- [ ] Edge cases identified
- [ ] Phase 1 scope locked

## Client Acknowledgment
- [ ] Requirements reviewed with client
- [ ] Success criteria agreed
- [ ] Timeline accepted
- [ ] Budget approved
- [ ] Change process understood
- [ ] Written confirmation received

## Internal Validation
- [ ] Technical feasibility confirmed
- [ ] Resource availability checked
- [ ] Risk assessment complete
- [ ] Profitability validated
- [ ] Quality gates defined
```

**Why It Matters:**
- No project proceeds without prerequisites
- Catches issues before they become expensive
- Clear go/no-go criteria
- Shared accountability

**Action Required:**
- [ ] Create Quality Gate Checklists for each phase
- [ ] Add to handoff procedures
- [ ] Create Notion template for gate reviews

---

### GAP 12: Red Flags to Catch Early

| Current (Sales) | Required (Dev) | Status |
|-----------------|----------------|--------|
| "Qualification" is general | Specific red flags that indicate scope risk | **MISSING** |

**Matthew's Framework:**
- 🚩 "Make it like [huge platform]" → Scope creep
- 🚩 "Just a simple..." → Never simple
- 🚩 "AI that does everything" → Undefined scope
- 🚩 "We'll figure it out as we go" → No clear requirements
- 🚩 "Unlimited revisions" → Never-ending project

**Non-Negotiables (Never proceed without):**
1. ❌ Clear success criteria
2. ❌ Written scope agreement
3. ❌ Technical validation
4. ❌ Profitability check
5. ❌ Initial payment

**Action Required:**
- [ ] Add Red Flags section to discovery call guide
- [ ] Create disqualification criteria
- [ ] Add to qualification checklist

---

## Priority Implementation Order

### Already Addressed (From Meeting Decisions)
| Gap | Meeting Decision | SOP Reference |
|-----|------------------|---------------|
| Document Ownership | Sales leads, Dev inputs | SOP-SD-001 |
| Deliverables Structure | Presentation → Proposal → SOW | SOP-SL-001 |
| Joint Calls | All hands on deck | SOP-SD-001 |
| Dev Inputs List | Time estimate, risk, complexity, criteria | SOP-SD-001 |

### P1 Templates Created (Feb 16, 2026)
| Priority | Gap | Template | Location |
|----------|-----|----------|----------|
| P1 | GAP 2: Metrics Discovery | ✅ Created | `templates/metrics-discovery-template.md` |
| P1 | GAP 5: MoSCoW Requirements | ✅ Created | `templates/moscow-prioritization-template.md` |
| P1 | GAP 10: Change Request Process | ✅ Created | `templates/change-request-process.md` |

### P2 Templates Created (Feb 16, 2026)
| Priority | Gap | Template | Location |
|----------|-----|----------|----------|
| P2 | GAP 4: Problem Statement | ✅ Created | `templates/problem-statement-template.md` |
| P2 | GAP 6: Pricing Calculator | ✅ Created | `templates/pricing-calculator.md` |
| P2 | GAP 7: Milestone Payments | ✅ Created | `templates/milestone-payment-terms.md` |

### Still Needs Implementation (P3/P4)
| Priority | Gap | Impact | Effort | Action Item Owner |
|----------|-----|--------|--------|-------------------|
| P3 | GAP 1: Billable Discovery | Medium | Medium | Trent (pricing decision) |
| P3 | GAP 3: Vibe Coding | Medium | High | Matthew (train Mekaiel) |
| P3 | GAP 8: Functional Requirements | Medium | Low | Mekaiel |
| P4 | GAP 9: Tech Requirements Checklist | Low | Low | Mekaiel (expand questionnaire) |
| P4 | GAP 11: Quality Gates | Medium | Medium | Matthew |
| P4 | GAP 12: Red Flags | Low | Low | Mekaiel |

---

## Action Items (From Meeting)

### Mekaiel Abdullahi
- [ ] Map SOP: discovery inputs → proposals → SOW *(in progress)*
- [ ] Notion process for transcripts, notes, documentation
- [ ] Process transcripts into structured tech questions
- [ ] Consolidate dev inputs criteria, remove redundancies
- [ ] **Add:** Metrics Discovery template (GAP 2)
- [ ] **Add:** MoSCoW prioritization template (GAP 5)
- [ ] **Add:** Change Request process (GAP 10)

### Matthew Kerns
- [ ] Validate time estimates format (weeks vs hours)
- [ ] **Add:** Review complexity scoring formula (GAP 6)
- [ ] **Add:** Provide vibe coding training (GAP 3)

### Both
- [ ] Follow-up review of SOP refinements
- [ ] **Add:** Align on milestone payment structure (GAP 7)

---

## Next Steps

1. ~~**Sync with Matthew** - Review this gap analysis together~~ ✓ Meeting done
2. **Pick P1 items** - Implement Metrics Discovery, MoSCoW, Change Request this week
3. **Update templates** - Create/update Notion templates for each gap
4. **Update SOPs** - Integrate new processes into existing SOPs (SOP-SD-001 consolidation)
5. **Train team** - Brief Chris and Trent on new processes

---

## Related Documents

**Our SOPs:**
- [SOP-ARISE-SL-001: Sales Lifecycle](./SOP-ARISE-SL-001-sales-lifecycle.md)
- [SOP-ARISE-SD-001: Sales-Dev Collaboration](./SOP-ARISE-SD-001-sales-dev-collaboration.md)
- [SOP-ARISE-HO-001: Handoff Procedures](./SOP-ARISE-HO-001-handoff-procedures.md)

**Matthew's Framework:**
- `shared-resources/matthew-repos/ai-agency-development-os/claude-code-os-implementation/03-ai-growth-engine/development-framework/`
- [FRAMEWORK-OVERVIEW.md](../../../shared-resources/matthew-repos/ai-agency-development-os/claude-code-os-implementation/03-ai-growth-engine/development-framework/FRAMEWORK-OVERVIEW.md)
- [01-diagnostic-call.md](../../../shared-resources/matthew-repos/ai-agency-development-os/claude-code-os-implementation/03-ai-growth-engine/development-framework/01-requirements-discovery/01-diagnostic-call.md)
- [03-requirements-refinement.md](../../../shared-resources/matthew-repos/ai-agency-development-os/claude-code-os-implementation/03-ai-growth-engine/development-framework/01-requirements-discovery/03-requirements-refinement.md)
- [03-milestone-planning.md](../../../shared-resources/matthew-repos/ai-agency-development-os/claude-code-os-implementation/03-ai-growth-engine/development-framework/02-solution-design/03-milestone-planning.md)

---

## The Dev Requirements Mantra

```
"If it's not written down, it's not in scope."
"If it's not in Phase 1, it's in Phase 2."
"If it changes the timeline, it changes the price."
"If you're not sure, prototype it."
```

*Adopted from Matthew's Development Framework*
