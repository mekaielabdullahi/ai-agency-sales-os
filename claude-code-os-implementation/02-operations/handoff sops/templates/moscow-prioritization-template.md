# MoSCoW Prioritization Template

**Template ID:** ARISE-TPL-002
**Version:** 1.0
**Created:** February 16, 2026
**Use During:** Proposal Creation (after discovery, before pricing)
**Owner:** Sales (Mekaiel) + Dev (Matthew)

---

## Purpose

Categorize all requirements into MUST/SHOULD/COULD/WON'T to control scope, enable phased delivery, and prevent scope creep. This becomes the source of truth for what's in Phase 1 vs. future phases.

---

## When to Use

- **After:** Discovery call complete, opportunity matrix built
- **Before:** Proposal drafted, pricing calculated
- **Collaborators:** Mekaiel (sales) + Matthew (dev input)
- **Output:** Prioritized requirements for proposal and PRD

---

## The MoSCoW Categories

| Category | Meaning | Phase | Payment |
|----------|---------|-------|---------|
| **MUST** | Critical - project fails without it | Phase 1 | Included |
| **SHOULD** | Important - significant value, not critical | Phase 2 | Future |
| **COULD** | Nice - enhances but not necessary | Phase 3 | Future |
| **WON'T** | Out of scope - explicitly excluded | Never | N/A |

---

## Prioritization Criteria

### MUST Have (Phase 1)
Include if ALL of these are true:
- [ ] Core functionality that solves the main problem
- [ ] Client explicitly stated as critical
- [ ] Project cannot deliver value without it
- [ ] We can build it within Phase 1 timeline/budget

**Examples:**
- Basic automation of primary workflow
- Core integration to main system
- Essential data capture
- Minimum viable reporting

### SHOULD Have (Phase 2)
Include if:
- [ ] Adds significant value but project works without it
- [ ] Client mentioned but not as critical
- [ ] Requires Phase 1 foundation to build on
- [ ] Would extend timeline significantly if included

**Examples:**
- Enhanced features beyond minimum
- Additional integrations
- Advanced reporting/analytics
- Secondary workflow automation

### COULD Have (Phase 3)
Include if:
- [ ] Convenience/polish feature
- [ ] "Nice to have" mentioned by client
- [ ] Low impact on core value
- [ ] Can be added independently later

**Examples:**
- UI polish and customization
- Advanced filtering/search
- Notifications beyond essential
- Performance optimization
- Mobile app (when web works)

### WON'T Have (Out of Scope)
Include if ANY of these are true:
- [ ] Different problem space entirely
- [ ] Requires capabilities we don't have
- [ ] Client floated but not serious about
- [ ] Would fundamentally change project scope
- [ ] "Someday/maybe" ideas

**Examples:**
- Features for a different user group
- Platforms we don't support
- AI capabilities beyond current tech
- Integrations with systems they don't use yet

---

## MoSCoW Template

**Fill this out during proposal creation:**

```markdown
## Requirements Prioritization - [Client Name]
**Created:** [Date]
**Sales:** [Name]
**Dev Input:** [Name]
**Client Confirmed:** [ ] Yes / [ ] Pending

---

## MUST Have (Phase 1 - Critical)

| # | Requirement | User Story | Acceptance Criteria | Dev Estimate |
|---|-------------|------------|---------------------|--------------|
| M1 | [Feature] | As a [user], I want [action] so that [outcome] | - Given X, when Y, then Z | [X hrs] |
| M2 | [Feature] | As a [user], I want [action] so that [outcome] | - Given X, when Y, then Z | [X hrs] |
| M3 | [Feature] | As a [user], I want [action] so that [outcome] | - Given X, when Y, then Z | [X hrs] |

**Phase 1 Total Estimate:** [X hrs]
**Phase 1 Timeline:** [X weeks]

---

## SHOULD Have (Phase 2 - Important)

| # | Requirement | Why Important | Depends On | Est. Effort |
|---|-------------|---------------|------------|-------------|
| S1 | [Feature] | [Value add] | M1, M2 | [X hrs] |
| S2 | [Feature] | [Value add] | M3 | [X hrs] |

**Phase 2 Estimate:** [X hrs]
**Recommend After:** Phase 1 success validated

---

## COULD Have (Phase 3 - Nice)

| # | Requirement | Why Nice | Priority Within Category |
|---|-------------|----------|--------------------------|
| C1 | [Feature] | [Convenience] | High |
| C2 | [Feature] | [Polish] | Medium |
| C3 | [Feature] | [Enhancement] | Low |

**Phase 3 Estimate:** [X hrs]
**Recommend After:** Phase 2 complete

---

## WON'T Have (Out of Scope)

| # | Requirement | Why Excluded | Future Consideration? |
|---|-------------|--------------|----------------------|
| W1 | [Feature] | [Reason] | Yes / No |
| W2 | [Feature] | [Reason] | Yes / No |

**Important:** These are explicitly NOT included in any phase. If client asks, refer to this list.

---

## Phase Summary

| Phase | Scope | Est. Hours | Est. Cost | Timeline |
|-------|-------|------------|-----------|----------|
| Phase 1 (MUST) | Core automation | [X] hrs | $[X] | [X] weeks |
| Phase 2 (SHOULD) | Enhancements | [X] hrs | $[X] | [X] weeks |
| Phase 3 (COULD) | Polish | [X] hrs | $[X] | [X] weeks |
| **Total Vision** | Full transformation | [X] hrs | $[X] | [X] weeks |

**Current Proposal:** Phase 1 only
**Presentation:** Shows full vision (all phases)
```

---

## Prioritization Session Guide

### Step 1: List Everything (5 min)
Write down every feature/requirement mentioned in discovery. Don't filter yet.

### Step 2: Identify MUSTs (10 min)
Ask for each item:
- "Does the project fail without this?"
- "Did client say this is critical?"

If yes to both → MUST

### Step 3: Sort Remaining (10 min)
For non-MUSTs, ask:
- "Significant value add?" → SHOULD
- "Nice to have?" → COULD
- "Different problem?" → WON'T

### Step 4: Validate with Dev (15 min)
Review with Matthew:
- Are MUSTs actually achievable in Phase 1?
- Any technical dependencies missing?
- Effort estimates reasonable?

### Step 5: Confirm with Client (Call or Email)
Before finalizing proposal:
- "Here's what we'll deliver in Phase 1..."
- "Here's what we recommend for Phase 2..."
- "These items are out of scope..."

---

## Scope Lock Rules

Once proposal is sent:

| Situation | Response |
|-----------|----------|
| Client wants to add MUST | "That changes Phase 1 scope. Let me re-estimate." |
| Client wants to add SHOULD | "Great for Phase 2! Let's note it." |
| Client wants to move SHOULD → MUST | "We can swap it with [existing MUST] or extend Phase 1." |
| Client questions WON'T | "That's a different project. Happy to scope separately." |

---

## Red Flags During Prioritization

| Red Flag | Risk | Response |
|----------|------|----------|
| Everything is MUST | Scope creep | "If we can only do 3 things, which 3?" |
| No clear MUSTs | Undefined problem | "What's the ONE thing that must work?" |
| WON'T list empty | Hidden expectations | "What are you NOT expecting us to build?" |
| Phase 1 > 4 weeks | Too big | "Let's split this into Phase 1a and 1b" |

---

## Example: Completed MoSCoW

```markdown
## Requirements Prioritization - Print Shop Automation
**Created:** February 2026
**Sales:** Mekaiel
**Dev Input:** Matthew
**Client Confirmed:** [x] Yes

---

## MUST Have (Phase 1)

| # | Requirement | User Story | Acceptance Criteria | Est. |
|---|-------------|------------|---------------------|------|
| M1 | Auto-ticket creation | As admin, I want calls to auto-create tickets so I don't manually enter | - Call → ticket in <30 sec | 8 hrs |
| M2 | Quote calculator | As owner, I want quick quotes so turnaround is <4 hrs | - Input → quote PDF in 2 min | 12 hrs |
| M3 | Service dashboard | As owner, I want to see open jobs so nothing falls through | - All active jobs visible | 6 hrs |

**Phase 1 Total:** 26 hrs (~$5,200)
**Timeline:** 2 weeks

---

## SHOULD Have (Phase 2)

| # | Requirement | Why Important | Depends On | Est. |
|---|-------------|---------------|------------|------|
| S1 | Automated follow-ups | Reduces missed opportunities | M1 | 8 hrs |
| S2 | Inventory alerts | Prevents stockouts | M3 | 6 hrs |

**Phase 2 Total:** 14 hrs (~$2,800)

---

## WON'T Have

| # | Requirement | Why Excluded |
|---|-------------|--------------|
| W1 | Mobile app | Web responsive is sufficient for now |
| W2 | Customer portal | Different project, different users |
| W3 | Accounting integration | Client not ready, no QuickBooks API access |
```

---

## Related Documents

- [DEV-REQUIREMENTS-GAPS.md](../DEV-REQUIREMENTS-GAPS.md) - Gap 5
- [metrics-discovery-template.md](./metrics-discovery-template.md) - KPIs feed into acceptance criteria
- Matthew's Framework: `development-framework/01-requirements-discovery/03-requirements-refinement.md`
