# Requirements Refinement Process

## Purpose
Transform vague client needs into specific, actionable, and priced development milestones through iterative refinement.

## The Refinement Cycle

```
VAGUE NEED → PROTOTYPE → FEEDBACK → SPECIFIC REQUIREMENT → PRICE
    ↑                                                         ↓
    └──────────────── ITERATE UNTIL CLEAR ───────────────────┘
```

---

## Stage 1: Initial Capture

### The Problem Statement Template
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

### Red Flags to Catch Early
- 🚩 "Make it like [huge platform]" → Scope creep
- 🚩 "Just a simple..." → Never simple
- 🚩 "AI that does everything" → Undefined scope
- 🚩 "We'll figure it out as we go" → No clear requirements
- 🚩 "Unlimited revisions" → Never-ending project

---

## Stage 2: Prototype-Driven Refinement

### Iteration 1: Core Function
```
Show: Basic functionality
Ask: "Is this the right direction?"
Refine: Core workflow
Document: Must-have features
```

### Iteration 2: Edge Cases
```
Show: Added complexity
Ask: "Which edges matter most?"
Refine: Critical paths only
Document: Nice-to-haves (Phase 2)
```

### Iteration 3: Integration Points
```
Show: System connections
Ask: "What else needs to connect?"
Refine: Integration priorities
Document: Technical requirements
```

---

## Requirements Documentation

### The MoSCoW Method
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
- [ ] Advanced error handling

## COULD Have (Phase 3 - Nice)
- [ ] Convenience features
- [ ] UI polish
- [ ] Advanced customization
- [ ] Performance optimization

## WON'T Have (Out of scope)
- [ ] Features for future consideration
- [ ] Explicitly excluded items
- [ ] Different problem spaces
```

---

## Functional Requirements Template

### For Each Feature
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

---

## Technical Requirements Checklist

### Data Requirements
- [ ] Data sources identified
- [ ] Data formats specified
- [ ] Volume estimates noted
- [ ] Retention policies defined

### Integration Requirements
- [ ] External systems listed
- [ ] API documentation reviewed
- [ ] Authentication methods confirmed
- [ ] Rate limits understood

### Performance Requirements
- [ ] Expected user count
- [ ] Concurrent usage
- [ ] Response time expectations
- [ ] Data processing volumes

### Security Requirements
- [ ] Authentication needs
- [ ] Authorization levels
- [ ] Data encryption requirements
- [ ] Compliance needs (HIPAA, GDPR, etc.)

---

## Scope Management

### The Change Request Process
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

### Scope Creep Prevention
| Client Says | You Respond |
|-------------|-------------|
| "Can we also add..." | "Great idea! Let's add that to Phase 2." |
| "Just a quick change..." | "Let me assess the impact and get back to you." |
| "While you're at it..." | "I'll note that for our next milestone planning." |
| "I assumed it included..." | "Let's review our documented requirements." |

---

## Requirements Sign-off

### Pre-Development Checklist
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

---

## From Requirements to Pricing

### Effort Calculation
```
Base Hours = Σ(Feature Development Hours)
Testing = Base Hours × 0.3
Documentation = Base Hours × 0.1
Project Management = Base Hours × 0.15
Buffer = Base Hours × 0.25

Total Hours = Base + Testing + Documentation + PM + Buffer
```

### Price Calculation
```
Developer Cost = Total Hours × Developer Rate
Architect Margin = Developer Cost × 0.4
Sales Fee = Developer Cost × 0.15
Infrastructure = Fixed or % based

Client Price = Developer Cost + Architect Margin + Sales Fee + Infrastructure
```

---

## Common Requirement Patterns

### Pattern 1: Automation Project
```markdown
## Core Requirements
- Trigger: [What starts the process]
- Process: [Steps to automate]
- Output: [Expected result]
- Frequency: [How often it runs]
- Exceptions: [Error handling]
```

### Pattern 2: Integration Project
```markdown
## Core Requirements
- System A: [Source system]
- System B: [Target system]
- Data Flow: [What moves between]
- Sync Frequency: [Real-time/batch]
- Conflict Resolution: [How to handle]
```

### Pattern 3: Dashboard Project
```markdown
## Core Requirements
- Data Sources: [Where data comes from]
- Metrics: [What to display]
- Refresh Rate: [How often updates]
- User Roles: [Who sees what]
- Interactivity: [Filters/drill-downs]
```

---

## Red Lines (Non-Negotiables)

Never proceed without:
1. ❌ Clear success criteria
2. ❌ Written scope agreement
3. ❌ Technical validation
4. ❌ Profitability check
5. ❌ Initial payment

---

## The Requirements Mantra

```
"If it's not written down, it's not in scope."
"If it's not in Phase 1, it's in Phase 2."
"If it changes the timeline, it changes the price."
"If you're not sure, prototype it."
```