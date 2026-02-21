# Milestone Payment Terms

**Template ID:** ARISE-TPL-006
**Version:** 1.0
**Created:** February 16, 2026
**Use During:** Proposal creation + SOW drafting
**Owner:** Sales (Mekaiel) + Dev (Matthew for milestone definition)

---

## Purpose

Structure every project into milestone-based payments that reduce risk, maintain cash flow, and ensure continuous value delivery. No more "one big payment at the end."

---

## The Milestone Philosophy

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   NEVER: One big delivery at the end                        │
│   ALWAYS: Multiple small wins along the way                 │
│                                                             │
│   Each milestone must:                                      │
│   ✓ Deliver working value                                   │
│   ✓ Be independently useful                                 │
│   ✓ Trigger a payment                                       │
│   ✓ Build on the previous                                   │
│   ✓ Reduce remaining risk                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Standard Milestone Patterns

### Pattern A: 3-Milestone (Most Common)

**Best for:** $5,000 - $25,000 projects, 2-6 weeks

```
MILESTONE 1: Foundation (25% of work)
├── Core infrastructure setup
├── Basic functionality working
├── Proof of concept validated
└── Payment: 30% of total

MILESTONE 2: Full Feature (50% of work)
├── Complete functionality
├── All integrations connected
├── Error handling implemented
└── Payment: 50% of total

MILESTONE 3: Polish & Deploy (25% of work)
├── UI refinement
├── Performance optimization
├── Documentation & training
├── Production deployment
└── Payment: 20% of total
```

### Pattern B: 5-Milestone (Complex Projects)

**Best for:** $25,000+ projects, 6+ weeks

```
M1: Discovery & Design (10% of work)
├── Technical architecture
├── Detailed requirements
├── Environment setup
└── Payment: 15% of total

M2: Core Development (25% of work)
├── Primary features
├── Core workflow
└── Payment: 25% of total

M3: Integration Layer (25% of work)
├── External connections
├── Data sync
└── Payment: 25% of total

M4: Testing & Refinement (25% of work)
├── QA testing
├── Bug fixes
├── Performance tuning
└── Payment: 25% of total

M5: Deployment & Handover (15% of work)
├── Production deployment
├── Documentation
├── Training
└── Payment: 10% of total
```

### Pattern C: Sprint-Based (Agile)

**Best for:** Ongoing relationships, unclear scope

```
2-Week Sprints × N

Each sprint:
├── Clear deliverables defined
├── Demo at end of sprint
├── Payment on approval
├── Next sprint planned together

Payment: Fixed per sprint or time & materials
```

---

## Payment Structure Rules

### Work-to-Payment Ratio

| Milestone | Work % | Payment % | Why |
|-----------|--------|-----------|-----|
| M1 | 25% | 30% | Front-load for cash flow |
| M2 | 50% | 50% | Aligned with value |
| M3 | 25% | 20% | Incentive to complete |

### Payment Timing Options

**Option 1: On Delivery (Standard)**
```
Work complete → Demo → Client approval → Invoice → Payment (Net 15)
```

**Option 2: Advance Payment (Higher Risk Projects)**
```
Invoice → Payment received → Work begins → Delivery
```

**Option 3: Hybrid (Recommended)**
```
M1: 50% advance → Work → Delivery → 50% balance
M2+: On delivery (Net 15)
```

---

## Milestone Definition Template

```markdown
## Milestone [#]: [Name]

**Duration:** [X days/weeks]
**Work %:** [X]%
**Payment:** $[Amount] ([X]% of total)
**Payment Terms:** [Advance / On delivery / Net 15]

---

### Deliverables

- [ ] [Specific, measurable deliverable]
- [ ] [Specific, measurable deliverable]
- [ ] [Specific, measurable deliverable]

### Success Criteria

| Criteria | How We Prove It |
|----------|-----------------|
| [Criterion 1] | [Demo / Test / Metric] |
| [Criterion 2] | [Demo / Test / Metric] |
| [Criterion 3] | [Demo / Test / Metric] |

### Dependencies

- **Requires from client:** [What we need before starting]
- **Requires from previous milestone:** [What must be done first]
- **Enables for next milestone:** [What this unlocks]

### Demo Script

At milestone completion, we will demonstrate:
1. [What we show first]
2. [What we show second]
3. [How we prove success criteria met]

### Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | Low/Med/High | Low/Med/High | [Plan] |
| [Risk 2] | Low/Med/High | Low/Med/High | [Plan] |
```

---

## SOW Payment Terms Language

**Include this in every Statement of Work:**

```markdown
## Payment Terms

### Milestone Payment Schedule

| Milestone | Description | Amount | Due |
|-----------|-------------|--------|-----|
| M1 | [Foundation] | $[X] | [Upon signing / Net 15 from approval] |
| M2 | [Full Feature] | $[X] | Net 15 from milestone approval |
| M3 | [Polish & Deploy] | $[X] | Net 15 from milestone approval |
| **Total** | | **$[X]** | |

### Payment Terms

1. **Due Date:** Payment is due within 15 days of milestone approval.

2. **Late Payment:** A late fee of 1.5% per month (18% annually) will be applied to overdue balances.

3. **Work Stoppage:** If payment is more than 30 days overdue:
   - All work will pause until payment is received
   - Timeline will be extended by duration of delay
   - Additional fees may apply for project restart

4. **Intellectual Property:** All deliverables remain the property of [Agency Name] until full payment is received. Upon final payment, IP transfers to Client as specified in the IP section.

5. **Milestone Approval:** Client has 5 business days to review and approve each milestone. No response within 5 days constitutes approval.

### Refund Policy

- **Before work begins:** Full refund minus administrative fee ($500)
- **After M1 started:** No refund for completed milestones
- **Partial milestone:** Pro-rated based on work completed

### Additional Work

Any work outside the defined scope will be quoted separately and requires written approval before beginning. See Change Request process.
```

---

## Milestone Planning Session Guide

### Before the Session
- [ ] MoSCoW prioritization complete
- [ ] Pricing calculator complete
- [ ] Matthew available for technical input

### Session Agenda (30 min)

**1. Review Scope (5 min)**
- Confirm MUST have features for this phase
- Confirm total hours and price

**2. Define Milestones (15 min)**
- How many milestones? (Usually 3)
- What's in each milestone?
- What order makes sense technically?

**3. Set Deliverables (5 min)**
- Specific outputs for each milestone
- Success criteria (how do we know it's done?)

**4. Validate Timeline (5 min)**
- Duration per milestone
- Dependencies and blockers
- Client availability for reviews

### Output
- Completed milestone definitions
- Payment schedule for SOW
- Demo dates on calendar

---

## Client Communication Templates

### Milestone Kickoff Email

```markdown
Subject: Starting Milestone [#]: [Name]

Hi [Client],

We're beginning Milestone [#] of your [project] today.

**This Milestone Includes:**
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

**Timeline:** [X] days (completing [date])
**Your Investment:** $[amount] due on approval

**What We Need From You:**
- [Any client dependencies]
- [Access / credentials / info needed]

**Next Steps:**
1. We'll provide updates in [Slack/email]
2. Demo scheduled for [date]
3. Your review and approval by [date]

Questions? Let's discuss.

Best,
[Your name]
```

### Milestone Completion Email

```markdown
Subject: Milestone [#] Complete - Ready for Review

Hi [Client],

Milestone [#] is complete and ready for your review.

**Delivered:**
✓ [Deliverable 1]
✓ [Deliverable 2]
✓ [Deliverable 3]

**Demo Recording:** [Link]
**Documentation:** [Link]

**Success Criteria Met:**
- [Criterion 1]: ✓ Achieved
- [Criterion 2]: ✓ Achieved
- [Criterion 3]: ✓ Achieved

**Next Steps:**
1. Review and test the deliverables
2. Reply with approval by [date] (5 business days)
3. Invoice for $[amount] will be sent upon approval
4. Milestone [#+1] begins [date]

**Progress:** [X]% complete with full project

Let me know if you have questions or want to discuss anything.

Best,
[Your name]
```

### Payment Reminder (Friendly)

```markdown
Subject: Invoice #[XXX] - Friendly Reminder

Hi [Client],

Just a friendly reminder that invoice #[XXX] for $[amount] (Milestone [#]) is due [date].

If you've already sent payment, thank you! Please disregard this note.

**Payment Options:**
- [Bank transfer details]
- [Credit card link if applicable]

Let me know if you have any questions.

Best,
[Your name]
```

### Payment Overdue (Firm)

```markdown
Subject: Invoice #[XXX] - Payment Overdue

Hi [Client],

Invoice #[XXX] for $[amount] is now [X] days overdue.

Per our agreement, a late fee of 1.5% ($[X]) has been applied, bringing the total to $[new total].

**Important:** If payment is not received within [X] days, we will need to pause work on Milestone [#+1] until the balance is resolved.

Please let me know if there are any issues with payment, and we can discuss options.

**Payment Options:**
- [Bank transfer details]
- [Credit card link if applicable]

Best,
[Your name]
```

---

## Milestone Tracking Dashboard

```markdown
## Project: [Client Name]

### Overall Progress
[████████░░░░░░░░] 53% Complete

### Milestone Status

| # | Name | Status | Due | Payment | Collected |
|---|------|--------|-----|---------|-----------|
| 1 | Foundation | ✅ Complete | Feb 1 | $3,000 | ✅ Paid |
| 2 | Core Features | 🔄 In Progress (Day 5/10) | Feb 15 | $5,000 | ⏳ On approval |
| 3 | Deployment | ⏳ Planned | Feb 25 | $2,000 | ⏳ Future |

### Cash Flow

| Metric | Amount |
|--------|--------|
| Total Contract | $10,000 |
| Collected | $3,000 (30%) |
| Outstanding | $0 |
| Future | $7,000 |

### Upcoming

- [ ] Complete M2 development (Feb 12)
- [ ] M2 demo with client (Feb 14)
- [ ] Collect M2 payment (Feb 15)
- [ ] Start M3 development (Feb 16)
```

---

## Red Flags & Responses

| Red Flag | Risk | Response |
|----------|------|----------|
| Client wants single payment at end | Cash flow risk | "Milestone payments protect both of us. Let's discuss concerns." |
| Client delays approval | Timeline slip | "Per our agreement, no response in 5 days = approval. Can I help with the review?" |
| Client disputes deliverables | Scope confusion | "Let's review the success criteria we agreed to. What specifically isn't meeting expectations?" |
| Payment consistently late | Cash flow issues | "I'd like to discuss moving to advance payment for future milestones." |
| Client wants to skip milestone | Rushing | "Each milestone builds on the previous. Skipping M2 would risk quality in M3." |

---

## Related Documents

- [DEV-REQUIREMENTS-GAPS.md](../DEV-REQUIREMENTS-GAPS.md) - Gap 7
- [pricing-calculator.md](./pricing-calculator.md) - Total price feeds into milestones
- [moscow-prioritization-template.md](./moscow-prioritization-template.md) - Scope defines milestones
- [change-request-process.md](./change-request-process.md) - Changes during milestones
- Matthew's Framework: `development-framework/02-solution-design/03-milestone-planning.md`
