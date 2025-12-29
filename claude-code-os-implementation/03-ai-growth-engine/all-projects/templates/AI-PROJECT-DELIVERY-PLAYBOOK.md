# AI Project Delivery Playbook

**AriseGroup.ai — Project Delivery Framework**
**Version:** 1.0
**Last Updated:** December 19, 2025

---

## Executive Summary

Most AI agencies and solo builders don't fail on the tech. They fail on planning, scoping, and managing the work.

This playbook defines how AriseGroup delivers AI projects that are **tightly scoped**, **visible**, and **actually shippable**.

---

## Core Philosophy

> **"Clients are excited, the vision is huge, and then... four months later everyone's frustrated, the scope is fuzzy, and your effective hourly rate is trash."**

We avoid this by:
1. Getting paid to scope
2. Documenting before building
3. Making progress visible
4. Working in phases
5. Protecting our margins

---

## The 8-Point Delivery Framework

### Overview

| Phase | What | Why |
|-------|------|-----|
| 1. Paid Discovery | Charge for Phase 0 scoping | Filters tire-kickers, removes risk |
| 2. PRD First | Document before building | No building without clarity |
| 3. Kanban Board | Visual project management | Progress visible to all |
| 4. Phased Delivery | MVP → Menu of upgrades | Client sees ROI before committing more |
| 5. Layer Into Workflows | Build on existing tools | Reduces resistance, faster value |
| 6. Lightweight Rituals | Daily/weekly check-ins | Surfaces scope creep early |
| 7. Buffers & Guardrails | Time + scope protection | Protects margins |
| 8. Transparent Process | Explain why we work this way | Builds trust through clarity |

---

## Phase 1: Paid Discovery (Phase 0)

### The Bad Pattern
> "Let's jump on a few calls, I'll write a proposal, we'll figure it out as we go."

### The AriseGroup Pattern
> "Phase 0 is a paid scoping engagement. We define the problem, architecture, and roadmap before we build."

### What We Sell in Phase 0

**Investment:** $1,500 - $3,000 (depending on complexity)
**Timeline:** 1-2 weeks
**Deliverables:**

| Deliverable | Description |
|-------------|-------------|
| **Discovery Sessions** | 2-4 hours of structured interviews |
| **Business Functions Map** | Current state operations mapped |
| **Opportunity Matrix** | Prioritized AI opportunities with scoring |
| **Project Requirements Document** | Full PRD with scope, timeline, investment |
| **Implementation Roadmap** | Phased approach with clear milestones |

### Why This Matters

1. **Filters tire-kickers** — People who won't pay $2K to scope won't pay $10K to build
2. **Deep enough to price properly** — No more guessing or underpricing
3. **Sets the norm** — Changing scope = changing contract
4. **Removes risk for both sides** — Client knows exactly what they're getting

### How to Position It

> "We charge for discovery because it's where we do our deepest thinking. This isn't a sales call—it's a consulting engagement. You'll walk away with a complete blueprint of your AI transformation, whether you work with us or not."

### Phase 0 Deliverable Template

```
PHASE 0 DELIVERABLES
====================

1. Discovery Report
   - Executive summary
   - Current state assessment
   - Stakeholder interview findings
   - Pain points (with direct quotes)

2. Business Functions Map
   - Core functions identified
   - Sub-functions and processes
   - Dependencies and handoffs
   - Bottlenecks highlighted

3. AI Opportunity Matrix
   - All opportunities identified
   - Scored by Impact / Feasibility / ROI
   - Prioritized recommendations
   - Quick wins vs. strategic initiatives

4. Project Requirements Document (PRD)
   - Problem statement
   - Objectives and success criteria
   - Scope (explicit IN and OUT)
   - Technical approach
   - Deliverables checklist
   - Timeline by phase
   - Investment options

5. Implementation Roadmap
   - Phase 1: MVP (2-6 weeks)
   - Phase 2: Enhancements
   - Phase 3: Scale/Transform
   - Decision points between phases
```

---

## Phase 2: Write a PRD Before Building

### The Rule
> "If you can't describe the project clearly, you have no business implementing it."

### PRD Structure

Every project must have a PRD before development begins. Use AI to help draft, then refine with the client.

#### Section 1: Problem & Objectives

```markdown
## Problem Statement

**Specific pain we're solving:**
[e.g., "Missed calls, manual data entry, quote generation delays"]

**Current cost of this problem:**
- Time: [X hours/week]
- Revenue: [$X/month in lost opportunities]
- Team impact: [Description]

## Success Criteria

**What does "success" look like in 30/60/90 days?**

| Timeframe | Success Metric | Target |
|-----------|----------------|--------|
| Day 30 | [Metric] | [Target] |
| Day 60 | [Metric] | [Target] |
| Day 90 | [Metric] | [Target] |
```

#### Section 2: Scope Definition

```markdown
## In Scope ✅

The following are INCLUDED in this engagement:

1. [Specific deliverable]
2. [Specific deliverable]
3. [Specific deliverable]
4. [Specific deliverable]

## Out of Scope ❌

The following are EXPLICITLY NOT INCLUDED:

1. [Item] — Can be addressed in Phase 2
2. [Item] — Requires separate engagement
3. [Item] — Client responsibility
4. [Item] — Future consideration

## Scope Change Process

Any requests not listed in "In Scope" require:
1. Written change request
2. Impact assessment (time + cost)
3. Client approval before work begins
4. Options: SWAP (replace uncommitted item) or ADD (new budget)
```

#### Section 3: Phases

```markdown
## Phase Structure

### Phase 1: MVP (This Engagement)
- **Timeline:** [2-6 weeks]
- **Investment:** $[X,XXX]
- **Objective:** [Single clear objective]
- **Deliverables:** [List]

### Phase 2: Enhancement (Future)
- **Timeline:** [X weeks]
- **Investment:** $[X,XXX - X,XXX]
- **Objective:** [Objective]
- **Trigger:** Successful Phase 1 completion

### Phase 3: Scale (Future)
- **Timeline:** [X weeks]
- **Investment:** $[XX,XXX+]
- **Objective:** [Objective]
- **Trigger:** Proven ROI from Phase 2
```

#### Section 4: Technical Plan

```markdown
## Technical Architecture

### Stack
- **Automation Platform:** [n8n / Make / etc.]
- **LLM Provider:** [OpenAI / Anthropic / etc.]
- **Database:** [If applicable]
- **Integrations:** [List all systems]

### Webhooks & Touch Points

| Trigger | Source | Action | Destination |
|---------|--------|--------|-------------|
| [Event] | [System] | [What happens] | [System] |
| [Event] | [System] | [What happens] | [System] |

### Data Flow
[Diagram or description of how data moves through the system]
```

#### Section 5: Deliverables Checklist

```markdown
## Deliverables

| # | Deliverable | Description | Acceptance Criteria |
|---|-------------|-------------|---------------------|
| 1 | [Name] | [Description] | [How we know it's done] |
| 2 | [Name] | [Description] | [How we know it's done] |
| 3 | [Name] | [Description] | [How we know it's done] |
| 4 | [Name] | [Description] | [How we know it's done] |
```

#### Section 6: Risks & Assumptions

```markdown
## Assumptions

This project assumes:
1. [Client will provide X access by Y date]
2. [Client SME available for Z hours/week]
3. [Current system has API access]
4. [Data is in usable format]

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | Low/Med/High | Low/Med/High | [Plan] |
| [Risk] | Low/Med/High | Low/Med/High | [Plan] |

## Dependencies

| Dependency | Owner | Due Date | Status |
|------------|-------|----------|--------|
| [Item] | [Client/Us] | [Date] | [Status] |
```

---

## Phase 3: Kanban Board Management

### Why Visual Management

> "Don't manage a multi-month AI build out of your head and a few Slack messages."

Benefits:
- **You** see where projects actually are
- **Clients** see progress even if they don't understand the code
- **Sprints** become obvious: pull important cards, don't overload

### Board Structure

**Columns:**
```
BACKLOG → THIS SPRINT → IN PROGRESS → IN REVIEW → DONE
```

**Card Format:**
```
[Card Title]
-----------
Deliverable: [Which PRD item this supports]
Owner: [Team member]
Due: [Date]
Size: S/M/L

Acceptance Criteria:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

### Card Examples

Good cards (small, demo-able units):
- "Webhook from Stripe to event handler"
- "Prompt + evals for summarizing support tickets"
- "Basic admin UI to upload training docs"
- "Configure Quo-Jobber integration"
- "Draft SOP for invoice processing"

Bad cards (too big, not demo-able):
- "Build the automation system"
- "Integrate everything"
- "Make it work"

### Tags / Lanes

Organize by workstream:
- `core-system` — Main automation
- `integrations` — API connections
- `data-migration` — Moving data
- `documentation` — SOPs, training
- `stretch-goal` — Bonus deliverables

### Sprint Planning

**Weekly Sprint Cycle:**
1. Pull highest priority cards into "This Sprint"
2. Don't overload — 3-5 cards per person per week
3. Cards in "This Sprint" = commitment
4. Cards in "Backlog" = not yet promised

---

## Phase 4: Phased Delivery Model

### Stop Selling Monoliths

> "Stop selling 5-month monoliths with fuzzy edges."

### The AriseGroup Model

#### Phase 1: Quick Win Sprint
- **Objective:** Solve ONE specific pain point
- **Investment:** Under $10K (feels safe for client)
- **Timeline:** 2-6 weeks (not 4-5 months)
- **Deliverable:** Working system + visible ROI

#### Phase 2+: Menu of Upgrades

Present as options, not assumptions:

```
PHASE 2 MENU
============

Option A: [Feature] — $X,XXX
- [What it does]
- [Why it matters]
- Timeline: X weeks

Option B: [Feature] — $X,XXX
- [What it does]
- [Why it matters]
- Timeline: X weeks

Option C: [Feature] — $X,XXX
- [What it does]
- [Why it matters]
- Timeline: X weeks

Bundle Discount: All three for $XX,XXX (save $X,XXX)
```

### Phase Transition Language

After Phase 1 delivery:

> "You're now [running X system / saving Y hours / achieving Z result]. Phase 1 is complete.
>
> But you mentioned [pain point still unaddressed]. Phase 2 tackles that.
>
> For [price], we add [feature]. Timeline: [X weeks].
>
> Want to proceed, or take some time to see Phase 1 ROI first?"

### Credit Incentive

> "$X from Phase 1 applies to Phase 2 if signed within 14 days of delivery."

Creates urgency without pressure.

---

## Phase 5: Layer Into Existing Workflows

### The Principle

> "Most clients don't want a brand new all-in-one app. They want 'this AI thing that quietly fixes my biggest bottleneck' inside the tools they already use."

### Discovery Questions

Before designing anything, ask:
- "How do you actually work today? Show me the screen."
- "What tools does your team live in?"
- "What would break if we replaced [tool]?"
- "What do you love about your current system?"

### Integration-First Design

**Do:**
- Build on their existing CRM
- Add webhooks to their current tools
- Create Chrome extensions for their workflows
- Use their preferred communication channels

**Don't:**
- Replace their whole tech stack
- Force new apps they won't adopt
- Assume your tool is better than theirs
- Underestimate switching costs

### The AriseGroup Standard

> "We build on what's working. We only replace what's broken."

Example (Plotter Mechanix):
- ✅ Keep Jobber (they love it)
- ✅ Replace Vonage (they hate it)
- ✅ Enhance with Quo (integrates with Jobber)
- ❌ Don't touch QuickBooks yet (not our scope)

---

## Phase 6: Lightweight Rituals

### Daily Check-In (5-10 minutes)

**Format:** Async Slack message or quick call

**Three Questions:**
1. What did we ship yesterday?
2. What's blocked today?
3. Any new requests that threaten scope?

**Template:**
```
DAILY UPDATE — [Date]
=====================

✅ SHIPPED:
- [Item completed]
- [Item completed]

🚧 IN PROGRESS:
- [Item] — [Status/ETA]
- [Item] — [Status/ETA]

🚨 BLOCKED:
- [Item] — Need [X] from client

⚠️ SCOPE ALERT:
- [New request mentioned] — Discuss at weekly
```

### Weekly Planning (30-60 minutes)

**Agenda:**
1. **Review Board** (10 min) — What moved to Done?
2. **Demo** (15 min) — Show something, no matter how small
3. **Reprioritize** (10 min) — Adjust next sprint's cards
4. **Scope Check** (10 min) — Are we still within current phase?
5. **Blockers** (5 min) — What do we need from client?

**Required:**
- Demo something every week — builds trust, shows progress
- Explicitly confirm scope — prevents surprise conversations later

### Why This Matters

These tiny rituals:
- Keep everyone aligned
- Surface scope creep early (when it's negotiable)
- Give constant opportunities to show progress
- Build trust through visibility

---

## Phase 7: Buffers & Guardrails

### Time Buffers

> "AI work is uncertain. New tools, brittle APIs, model weirdness. If you estimate without buffers, you eat the risk."

**Rule:** Add 20-30% on top of "best case" for anything touching:
- A new API
- A new integration
- A new model or provider
- Client-dependent tasks

**AriseGroup Standard:**
- Promise 30 days, target 2 weeks
- Quote 6-8 weeks, target 4-5 weeks
- Never promise less than 1.5x your realistic estimate

### Scope Buffers

**Explicit Out-of-Scope List:**

Every PRD must include:
```
OUT OF SCOPE (This Engagement)
==============================

The following are NOT included:

1. [Pricing changes or new pricing models]
2. [New business lines or products]
3. [Complex wholesale/fulfillment logic]
4. [Historical data migration beyond X]
5. [Training beyond X hours]
6. [Ongoing maintenance after Day 30]

These items can be addressed in future phases.
```

### When Client Asks for "One More Thing"

**Step 1:** Point back to PRD and board
> "Great idea. Let me check if that's in our current scope..."

**Step 2:** Offer options

**Option A — SWAP:**
> "We can swap this for [uncommitted item of similar size]. Same timeline, same budget."

**Option B — ADD:**
> "We can add this to the board. It's about [X hours/days]. I'll send a change order for [$X]."

**Option C — PHASE 2:**
> "This is a great Phase 2 item. Let's capture it for after we finish the current sprint."

**Never:** Quietly absorb scope creep. It kills margins and extends timelines.

---

## Phase 8: Transparent Process

### Be Honest About Why

You can be totally transparent about your process:

| What We Do | Why We Do It |
|------------|--------------|
| "We start with paid discovery" | "So we don't guess your scope and overcharge later" |
| "We use a Kanban board" | "So you can see exactly where everything stands" |
| "We work in phases" | "So you see ROI on Phase 1 before committing to more" |
| "We mark out-of-scope explicitly" | "So you're never surprised by a bill" |
| "We do weekly demos" | "So you see progress, not just promises" |
| "We have a change request process" | "So scope changes are negotiated, not assumed" |

### The Trust Statement

> "Clients respect clarity and process way more than 'we'll just figure it out.'"

### Addressing Past Burns

For clients who've been burned before:

```
WHAT [PREVIOUS VENDOR] DID    vs.    WHAT WE DO
================================================

Weekly rate, no end in sight        Fixed price, fixed timeline
Vague promises                      Specific deliverables checklist
No visibility into progress         Kanban board you can see anytime
Scope kept expanding                Explicit out-of-scope + change process
Disappeared after payment           Daily/weekly updates + demos
Made things worse                   Build on what's working first
```

---

## Quick Reference Checklists

### Pre-Engagement Checklist

```
□ Paid discovery proposal sent
□ Phase 0 payment received
□ Discovery sessions scheduled
□ Business functions map complete
□ Opportunity matrix complete
□ PRD drafted
□ PRD reviewed with client
□ Scope (in/out) explicitly agreed
□ Phase 1 proposal sent
□ Contract signed
□ Payment received
□ Kanban board created
□ Kickoff call scheduled
```

### Weekly Delivery Checklist

```
□ Daily updates sent (Mon-Fri)
□ Board updated with current status
□ Weekly call completed
□ Demo delivered (something visible)
□ Scope confirmed (still in bounds?)
□ Blockers documented and escalated
□ Next week's sprint planned
□ Client satisfaction pulse check
```

### Phase Completion Checklist

```
□ All deliverables complete
□ Acceptance criteria met
□ Client sign-off received
□ Documentation delivered
□ Training completed
□ Handoff call scheduled
□ Phase 2 menu presented
□ Feedback collected
□ Case study drafted (if permitted)
```

---

## Templates & Resources

### Location

All templates are stored in:
```
/claude-code-os-implementation/03-ai-growth-engine/sales-engine/templates/
```

### Available Templates

| Template | Purpose |
|----------|---------|
| `phase-0-proposal.md` | Paid discovery engagement |
| `prd-template.md` | Project Requirements Document |
| `change-request.md` | Scope change documentation |
| `weekly-update.md` | Client communication format |
| `phase-transition.md` | Moving from Phase N to N+1 |
| `project-closeout.md` | Final delivery and handoff |

---

## Implementation Notes

### Transition Strategy

If you have projects already in flight using the old approach:

1. **Don't change mid-project** — Finish current commitments
2. **Start new projects with new process** — Clean slate
3. **Introduce incrementally** — Phase 0 first, then Kanban, then rituals

### Team Alignment

Before first project with this framework:
1. All team members read this playbook
2. 30-minute walkthrough of process
3. Assign board management owner
4. Practice daily update format
5. Do mock weekly review

### Continuous Improvement

After each project:
1. What worked well?
2. What was painful?
3. What would we change?
4. Update this playbook

---

## Summary

**The AriseGroup Delivery Philosophy:**

1. **Get paid to scope** — Discovery is valuable work
2. **Document before building** — PRD is the contract
3. **Make progress visible** — Kanban for all
4. **Deliver in phases** — MVP first, prove value, expand
5. **Respect existing workflows** — Layer in, don't replace
6. **Ritualize communication** — Daily/weekly cadence
7. **Protect margins** — Buffers and guardrails
8. **Be radically transparent** — Process builds trust

> "We didn't fail on the tech. We succeeded because we planned, scoped, and managed the work."

---

**Document Status:** Active
**Owner:** AriseGroup.ai Delivery Team
**Review Cycle:** Quarterly
