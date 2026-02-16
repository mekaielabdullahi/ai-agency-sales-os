# Problem Statement Template

**Template ID:** ARISE-TPL-004
**Version:** 1.0
**Created:** February 16, 2026
**Use During:** Discovery Call (capture) + Post-Call (refine)
**Owner:** Sales (Mekaiel)

---

## Purpose

Capture the client's problem in a structured format that feeds directly into the PRD and proposal. This standardized format ensures dev gets consistent information across all clients.

**Future Vision:** Automate extraction from Fathom transcripts using AI processing.

---

## When to Use

- **During:** Discovery call (fill in real-time or immediately after)
- **After:** Refine within 24 hours of call
- **Output:** Problem statement section for proposal and PRD

---

## Problem Statement Template

```markdown
# Problem Statement: [Client Name]

**Date:** [Date]
**Discovery Call Attendees:** [Names]
**Captured By:** [Your name]

---

## Current Situation

### What
> [What do they do manually today? Describe the process in their words.]

**Process Name:** [e.g., "Invoice Processing", "Customer Intake", "Quote Generation"]

**Process Steps (Current):**
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Continue as needed]

### Who
| Role | Person/Team | Time Spent | Hourly Cost |
|------|-------------|------------|-------------|
| [e.g., Admin] | [e.g., Alyssa] | [e.g., 20 hrs/week] | [e.g., $25/hr] |
| [e.g., Owner] | [e.g., Kelsey] | [e.g., 10 hrs/week] | [e.g., $150/hr] |

### When
- **Frequency:** [Daily / Weekly / Monthly / Per transaction]
- **Volume:** [e.g., "50 invoices/month", "200 calls/week"]
- **Peak times:** [e.g., "Monday mornings", "End of month"]
- **Triggers:** [What starts this process?]

### Time
| Activity | Current Time | Notes |
|----------|--------------|-------|
| [e.g., Data entry] | [e.g., 2 hrs/day] | [e.g., Manual copy-paste] |
| [e.g., Follow-up] | [e.g., 5 hrs/week] | [e.g., Phone calls] |
| [e.g., Reporting] | [e.g., 4 hrs/month] | [e.g., Excel compilation] |
| **Total** | **[X hrs/week]** | |

### Cost (Implied)
| Cost Type | Calculation | Monthly Cost |
|-----------|-------------|--------------|
| Labor (direct) | [X hrs × $Y/hr × 4 weeks] | $[Z] |
| Labor (opportunity) | [Owner hrs × owner rate] | $[Z] |
| Errors/rework | [Estimate] | $[Z] |
| Lost business | [Estimate if applicable] | $[Z] |
| **Total Monthly Cost** | | **$[Z]** |

---

## Desired Outcome

### Goal
> [What do they want instead? In their words.]

**One-sentence summary:** [e.g., "Automate invoice processing so Alyssa can focus on customer service instead of data entry."]

### Success Looks Like
| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| [e.g., Processing time] | [e.g., 40 hrs/month] | [e.g., 4 hrs/month] | [e.g., 90% reduction] |
| [e.g., Error rate] | [e.g., 15%] | [e.g., <2%] | [e.g., 87% reduction] |
| [e.g., Response time] | [e.g., 24 hrs] | [e.g., 2 hrs] | [e.g., 92% faster] |

### Timeline
- **Urgency level:** [ ] Critical / [ ] Important / [ ] Nice to have
- **Deadline:** [e.g., "Before busy season in March"]
- **Why this timeline:** [e.g., "Hiring freeze - can't add staff"]

### Budget
- **Range discussed:** $[X] - $[Y]
- **Budget holder:** [Name and role]
- **Approval process:** [e.g., "Owner decides", "Board approval needed"]
- **Payment preference:** [e.g., "Milestone-based", "Monthly retainer"]

---

## Pain Points (Verbatim Quotes)

Capture exact client quotes that reveal pain:

| Quote | Speaker | Pain Type |
|-------|---------|-----------|
| "[Exact quote]" | [Name] | [Time / Money / Frustration / Risk] |
| "[Exact quote]" | [Name] | [Time / Money / Frustration / Risk] |
| "[Exact quote]" | [Name] | [Time / Money / Frustration / Risk] |

**Most compelling pain point:** [Which quote best captures why they need this?]

---

## Context & Constraints

### Technical Environment
- **Current tools:** [List software they use]
- **Integrations needed:** [What must connect?]
- **Tech resources:** [ ] Has IT / [ ] No IT / [ ] We handle everything
- **Data location:** [Where is their data stored?]

### Business Constraints
- **Compliance:** [HIPAA, SOC2, GDPR, etc.]
- **Stakeholders:** [Who else needs to approve/use this?]
- **Change resistance:** [Any concerns about adoption?]
- **Previous attempts:** [Have they tried to solve this before? What failed?]

---

## Red Flags Identified

| Red Flag | Observed? | Notes |
|----------|-----------|-------|
| "Make it like [huge platform]" | [ ] Yes / [ ] No | |
| "Just a simple..." | [ ] Yes / [ ] No | |
| "AI that does everything" | [ ] Yes / [ ] No | |
| "We'll figure it out as we go" | [ ] Yes / [ ] No | |
| "Unlimited revisions" | [ ] Yes / [ ] No | |
| Unclear decision maker | [ ] Yes / [ ] No | |
| No budget discussed | [ ] Yes / [ ] No | |

---

## Summary for Proposal

**The Problem (2-3 sentences):**
> [Synthesize the above into a clear problem statement for the proposal]

**The Impact (quantified):**
> [X hours/week wasted, $Y/month in costs, Z% error rate]

**The Solution Direction:**
> [High-level approach - what type of solution will address this?]

**The Value (ROI preview):**
> [If we reduce X to Y, that saves $Z/month = $W/year vs. $V investment]
```

---

## Quick Capture Version

**For use during the call when you need speed:**

```markdown
## Quick Problem Capture - [Client]

**What:** [Manual process in one line]
**Who:** [Person + hours/week]
**Cost:** [$ estimate or "TBD"]
**Want:** [Desired outcome in one line]
**Timeline:** [When needed]
**Budget:** [Range or "TBD"]
**Pain quote:** "[Best quote that shows pain]"
```

---

## Transcript-to-Problem Automation

**Future state:** Process Fathom transcripts to auto-fill this template.

**Key phrases to extract:**
- "We currently..." → Current Situation
- "I spend X hours..." → Time
- "We need..." / "We want..." → Desired Outcome
- "By [date]..." → Timeline
- "Budget is..." / "We're looking at..." → Budget
- Pain indicators: "frustrated", "waste", "manual", "hate", "wish"

---

## Example: Completed Problem Statement

```markdown
# Problem Statement: Plotter Mechanix

**Date:** January 2026
**Discovery Call Attendees:** Kelsey (Owner), Alyssa (Admin), Mekaiel, Matthew
**Captured By:** Mekaiel

---

## Current Situation

### What
> "Every call comes in, Alyssa has to manually create a ticket, look up the customer, check their history, and then figure out which tech to send. It's all in her head or on sticky notes."

**Process Name:** Service Dispatch

**Process Steps (Current):**
1. Phone rings, Alyssa answers
2. Looks up customer in spreadsheet
3. Creates ticket in paper system
4. Checks tech schedules (whiteboard)
5. Calls tech to dispatch
6. Manually updates status throughout day
7. Creates invoice from paper ticket

### Who
| Role | Person/Team | Time Spent | Hourly Cost |
|------|-------------|------------|-------------|
| Admin | Alyssa | 40 hrs/week | $25/hr |
| Owner/Tech | Kelsey | 15 hrs/week (admin) | $175/hr |

### When
- **Frequency:** 30-50 calls/day
- **Volume:** ~150 service tickets/week
- **Peak times:** Monday mornings, 8-10am
- **Triggers:** Customer phone call or email

### Time
| Activity | Current Time | Notes |
|----------|--------------|-------|
| Call handling + ticket creation | 3 hrs/day | Manual entry |
| Dispatch coordination | 2 hrs/day | Phone calls to techs |
| Status updates | 2 hrs/day | Manual tracking |
| Invoicing | 8 hrs/week | Paper to QuickBooks |
| **Total** | **40 hrs/week (Alyssa)** | |

### Cost (Implied)
| Cost Type | Calculation | Monthly Cost |
|-----------|-------------|--------------|
| Alyssa labor | 160 hrs × $25 | $4,000 |
| Kelsey admin time | 60 hrs × $175 | $10,500 |
| Missed follow-ups | ~20% leads lost | $2,000 (est) |
| **Total Monthly Cost** | | **$16,500** |

---

## Desired Outcome

### Goal
> "I want Alyssa to answer the phone and have everything she needs right there. Auto-create the ticket, auto-dispatch to the right tech, auto-update the customer. Get her 20 hours back so she can actually help customers instead of pushing paper."

**One-sentence summary:** Automate ticket creation, dispatch, and status updates so Alyssa focuses on customer service, not data entry.

### Success Looks Like
| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| Admin hours/week | 40 hrs | 20 hrs | 50% reduction |
| Quote turnaround | 24-48 hrs | <4 hrs | 90% faster |
| Missed follow-ups | 20% | <5% | 75% reduction |

### Timeline
- **Urgency level:** [x] Important
- **Deadline:** "Before spring busy season - March"
- **Why this timeline:** "Can't hire, need efficiency gains"

### Budget
- **Range discussed:** $5,000 - $15,000 Phase 1
- **Budget holder:** Kelsey (Owner)
- **Approval process:** Owner decides
- **Payment preference:** Milestone-based

---

## Pain Points (Verbatim Quotes)

| Quote | Speaker | Pain Type |
|-------|---------|-----------|
| "I'm the highest-paid secretary in Phoenix" | Kelsey | Time/Money |
| "I can't take a vacation because it's all in my head" | Alyssa | Risk |
| "We're turning away jobs because we can't keep up" | Kelsey | Money |

**Most compelling:** "I'm the highest-paid secretary in Phoenix" - Owner doing $175/hr admin work.
```

---

## Related Documents

- [DEV-REQUIREMENTS-GAPS.md](../DEV-REQUIREMENTS-GAPS.md) - Gap 4
- [metrics-discovery-template.md](./metrics-discovery-template.md) - Success metrics feed from here
- [moscow-prioritization-template.md](./moscow-prioritization-template.md) - Problem informs requirements
- Matthew's Framework: `development-framework/01-requirements-discovery/03-requirements-refinement.md`
