# Change Request Process

**Template ID:** ARISE-TPL-003
**Version:** 1.0
**Created:** February 16, 2026
**Use During:** Active projects (after contract signed)
**Owner:** Sales (Mekaiel) as client liaison, Dev (Matthew) for impact assessment

---

## Purpose

Handle scope changes professionally without derailing timelines, budgets, or relationships. Protect margins while keeping clients happy. Every change request follows the same process.

---

## The Golden Rules

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   "If it's not written down, it's not in scope."           │
│   "If it's not in Phase 1, it's in Phase 2."               │
│   "If it changes the timeline, it changes the price."      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Change Request Categories

| Category | Definition | Typical Response |
|----------|------------|------------------|
| **Clarification** | Client explaining existing requirement better | No change needed |
| **Minor Tweak** | <2 hours impact, no timeline change | Absorb if reasonable |
| **Scope Addition** | New feature not in original scope | Change request process |
| **Scope Change** | Different approach to existing requirement | Impact assessment |
| **Emergency** | Critical business need, time-sensitive | Expedited process |

---

## The 5-Step Change Request Process

### Step 1: Document the Request

**Never agree verbally.** Get it in writing.

```markdown
## Change Request - [Client Name]
**Date:** [Date]
**Requested By:** [Client contact]
**Received By:** [Team member]

### Request Description
[What exactly is the client asking for?]

### Original Scope Reference
[What did we originally agree to? Quote from SOW/proposal]

### How Client Framed It
[ ] "Can we also add..."
[ ] "I thought it included..."
[ ] "Just a quick change..."
[ ] "While you're at it..."
[ ] Other: [describe]
```

### Step 2: Assess Impact

**Before responding, evaluate:**

```markdown
### Impact Assessment

| Dimension | Impact | Notes |
|-----------|--------|-------|
| **Time** | +[X] hours | [Explanation] |
| **Timeline** | +[X] days/weeks | [New completion date] |
| **Cost** | +$[X] | [Based on hourly rate] |
| **Risk** | Low / Medium / High | [What could go wrong] |
| **Dependencies** | [List] | [What else changes] |

### Complexity Rating
[ ] Minor (<2 hrs) - Can absorb
[ ] Small (2-8 hrs) - Small change order
[ ] Medium (8-24 hrs) - Formal change order
[ ] Large (24+ hrs) - New milestone/phase
```

### Step 3: Present Options

**Always give the client choices:**

```markdown
### Options for Client

**Option A: Add to Phase 2** (Recommended)
- No impact on current timeline or budget
- Included in next phase planning
- Estimate: $[X] when we get there

**Option B: Swap with Existing Feature**
- Remove [feature] from Phase 1
- Replace with this request
- Same timeline and budget

**Option C: Extend Current Phase**
- Add [X] days to timeline
- Add $[X] to budget
- Delivers everything including this request

**Our Recommendation:** [Option A/B/C] because [reason]
```

### Step 4: Get Written Approval

**No work without sign-off:**

```markdown
### Change Order Approval

**Change Request #:** CR-[XXX]
**Client:** [Name]
**Date:** [Date]

**Description:**
[What we're adding/changing]

**Impact:**
- Timeline: [Original] → [New]
- Budget: [Original] → [New] (+$[X])

**Terms:**
- Work begins upon written approval
- Additional payment due [when]
- Original scope remains unchanged except as noted

---

**Client Approval:**
- [ ] I approve this change order
- Name: _________________
- Date: _________________
- Signature/Email confirmation: _________________
```

### Step 5: Update Documentation

After approval:
- [ ] Update PRD/requirements doc
- [ ] Update project timeline
- [ ] Update budget tracking
- [ ] Notify dev team (Matthew)
- [ ] Add to milestone tracking
- [ ] File change order in project folder

---

## Response Templates

### Template 1: "Can we also add..."

> Hi [Client],
>
> Great idea! That's definitely something we can do.
>
> Since it's outside the current scope, I've documented it for Phase 2 planning. When we wrap up Phase 1, we'll review all the enhancement ideas together and prioritize.
>
> Want me to add anything else to the Phase 2 list while we're at it?
>
> Best,
> [Your name]

### Template 2: "I thought it included..."

> Hi [Client],
>
> Thanks for raising this. Let me clarify what we agreed to:
>
> **Original scope (from our SOW):**
> [Quote the relevant section]
>
> **Your request:**
> [What they're asking for]
>
> These are different because [brief explanation].
>
> Happy to add this - here are our options:
> - **Option A:** Include in Phase 2 (no current impact)
> - **Option B:** Add to Phase 1 (+$X, +X days)
>
> Which works better for you?
>
> Best,
> [Your name]

### Template 3: "Just a quick change..."

> Hi [Client],
>
> Thanks for the request! Let me take a look at the impact.
>
> Even small changes can have ripple effects on timeline and testing. I'll get back to you within 24 hours with an assessment and options.
>
> In the meantime, we're continuing on the current scope to keep momentum.
>
> Best,
> [Your name]

### Template 4: "While you're at it..."

> Hi [Client],
>
> Noted! I'll add that to our Phase 2 planning list.
>
> For now, we're focused on delivering the Phase 1 scope on time. Once that's complete and working, we'll review all the "while you're at it" items together.
>
> Anything else you want to capture for later?
>
> Best,
> [Your name]

### Template 5: Emergency/Urgent Request

> Hi [Client],
>
> I understand this is urgent. Here's what I need to assess impact:
>
> 1. What's driving the urgency? (Helps us prioritize)
> 2. What happens if we address this in Phase 2 instead?
> 3. Are you open to adjusting timeline/budget if needed?
>
> I'll have options for you within [X hours].
>
> Best,
> [Your name]

---

## When to Push Back

| Client Behavior | Your Response |
|-----------------|---------------|
| Repeated "small" changes adding up | "We've had [X] change requests. Let's schedule a scope review." |
| Pressure to absorb costs | "Our estimates already include buffer. Additional scope requires additional investment." |
| "This should have been obvious" | "Let's look at what we documented together. I want to understand the gap." |
| Threatening relationship | "I want to find a solution. Let's discuss options on a call." |
| Refusing to sign change order | "We can't begin work without written approval. This protects both of us." |

---

## Escalation Path

```
1. Client requests change
        ↓
2. Mekaiel documents and assesses
        ↓
3. Matthew validates technical impact (if needed)
        ↓
4. Mekaiel presents options to client
        ↓
5. If client pushes back → Trent joins discussion
        ↓
6. If still unresolved → Leadership call with all parties
```

---

## Change Request Log

**Track all changes in project folder:**

```markdown
## Change Request Log - [Project Name]

| CR# | Date | Description | Category | Impact | Status | Resolution |
|-----|------|-------------|----------|--------|--------|------------|
| CR-001 | [Date] | [Brief] | Addition | +$X, +X days | Approved | Added to M2 |
| CR-002 | [Date] | [Brief] | Clarification | None | Closed | No change needed |
| CR-003 | [Date] | [Brief] | Scope change | +$X | Pending | Awaiting approval |
```

---

## Prevention: Setting Expectations Upfront

### In the Proposal/SOW

Include this language:

> **Change Management**
>
> This SOW covers the scope defined in Section [X]. Any changes to scope will follow our change request process:
>
> 1. Client submits change request in writing
> 2. We assess impact (timeline, budget, risk)
> 3. We present options
> 4. Client approves in writing before work begins
>
> Minor clarifications (<2 hours impact) may be absorbed at our discretion. Larger changes require formal change orders.

### In the Kickoff Meeting

Say this:

> "As we work together, ideas will come up. That's great! Here's how we handle them:
>
> - Write it down (email or Slack)
> - We'll assess impact
> - You'll get options
> - You decide how to proceed
>
> This keeps us on track while capturing all your good ideas for current or future phases."

---

## Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| Change requests per project | <3 | More = unclear scope |
| % approved vs declined | Track | Shows client relationship health |
| Hours added via changes | <20% of original | Scope creep indicator |
| Revenue from change orders | Track | Should be positive contribution |
| Timeline slip from changes | <10% | Delivery predictability |

---

## Related Documents

- [DEV-REQUIREMENTS-GAPS.md](../DEV-REQUIREMENTS-GAPS.md) - Gap 10
- [moscow-prioritization-template.md](./moscow-prioritization-template.md) - Original scope reference
- [SOP-ARISE-HO-001: Handoff Procedures](../SOP-ARISE-HO-001-handoff-procedures.md) - Handoff checklists
- Matthew's Framework: `development-framework/01-requirements-discovery/03-requirements-refinement.md`
