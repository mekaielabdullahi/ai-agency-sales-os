# Pricing Calculator & Complexity Scoring

**Template ID:** ARISE-TPL-005
**Version:** 1.0
**Created:** February 16, 2026
**Use During:** Post-Discovery (before proposal)
**Owner:** Sales (Mekaiel) + Dev (Matthew for validation)

---

## Purpose

Calculate consistent, margin-protected pricing using complexity scoring and standardized formulas. Eliminates guesswork and ensures profitability on every deal.

**Target Margin:** >40% on all projects

---

## When to Use

- **After:** Discovery call + vibe coding (if applicable)
- **Before:** Proposal creation
- **Collaborators:** Mekaiel (runs calculator), Matthew (validates complexity)
- **Output:** Pricing for proposal

---

## Step 1: Complexity Scoring

### Score Each Dimension (0-10 points each)

| Dimension | Score | Criteria |
|-----------|-------|----------|
| **Integration Complexity** | /10 | How many systems? How well-documented are APIs? |
| **Data Complexity** | /10 | Volume, formats, transformations needed? |
| **Business Logic** | /10 | How many rules, edge cases, exceptions? |
| **User Interface** | /10 | Custom UI needed? How polished? |
| **Security/Compliance** | /10 | HIPAA, SOC2, encryption requirements? |

### Scoring Guide

**Integration Complexity (0-10)**
| Score | Description |
|-------|-------------|
| 0-2 | No integrations or single well-documented API |
| 3-4 | 2-3 integrations with good documentation |
| 5-6 | Multiple integrations, some undocumented |
| 7-8 | Complex integrations, custom APIs needed |
| 9-10 | Enterprise systems, legacy integrations |

**Data Complexity (0-10)**
| Score | Description |
|-------|-------------|
| 0-2 | Simple structured data, low volume |
| 3-4 | Multiple data sources, standard formats |
| 5-6 | Data transformation required, medium volume |
| 7-8 | Complex data models, high volume, real-time |
| 9-10 | Unstructured data, ML processing, massive scale |

**Business Logic (0-10)**
| Score | Description |
|-------|-------------|
| 0-2 | Simple rules, linear workflow |
| 3-4 | Some conditional logic, few exceptions |
| 5-6 | Complex rules, multiple branches |
| 7-8 | Many edge cases, approval workflows |
| 9-10 | Dynamic rules, AI decision-making |

**User Interface (0-10)**
| Score | Description |
|-------|-------------|
| 0-2 | No UI or simple admin panel |
| 3-4 | Basic UI with standard components |
| 5-6 | Custom UI, moderate polish |
| 7-8 | Polished UI, responsive, good UX |
| 9-10 | Complex UI, real-time updates, mobile |

**Security/Compliance (0-10)**
| Score | Description |
|-------|-------------|
| 0-2 | Basic auth, no compliance needs |
| 3-4 | Standard security, role-based access |
| 5-6 | Encryption, audit logs |
| 7-8 | HIPAA, GDPR, or similar compliance |
| 9-10 | SOC2, financial regulations, multi-tenant |

---

## Step 2: Determine Complexity Tier

| Total Score | Tier | Description |
|-------------|------|-------------|
| 0-10 | Simple | Basic automation, single integration |
| 11-20 | Standard | Typical client project |
| 21-30 | Complex | Multiple systems, custom logic |
| 31-40 | Enterprise | Large-scale, compliance-heavy |
| 41-50 | Major Build | Full platform development |

---

## Step 3: Calculate Base Hours

### From Vibe Coding (Preferred Method)

If you did a vibe coding session:

| Tier | Vibe Code Time | Multiplier | Production Hours |
|------|----------------|------------|------------------|
| Simple | 30 min | 40-60x | 20-30 hrs |
| Standard | 30 min | 60-100x | 30-50 hrs |
| Complex | 30 min | 100-160x | 50-80 hrs |
| Enterprise | 30 min | 160-240x | 80-120 hrs |
| Major Build | 30 min | 240x+ | 120+ hrs |

**Formula:** `Production Hours = Vibe Code Minutes × Multiplier / 60`

### From Feature List (Alternative)

If no vibe coding, estimate per feature:

| Feature Type | Typical Hours |
|--------------|---------------|
| Simple automation | 4-8 hrs |
| API integration | 8-16 hrs |
| Dashboard/reporting | 12-24 hrs |
| Custom UI component | 8-16 hrs |
| Complex workflow | 16-32 hrs |
| AI/ML component | 24-48 hrs |

---

## Step 4: Add Overhead

```
Base Development Hours:     [X] hrs
+ Testing (30%):            [X × 0.30] hrs
+ Documentation (10%):      [X × 0.10] hrs
+ Project Management (15%): [X × 0.15] hrs
+ Buffer (25%):             [X × 0.25] hrs
─────────────────────────────────────────
= Total Hours:              [X × 1.80] hrs
```

**Quick formula:** `Total Hours = Base Hours × 1.8`

---

## Step 5: Calculate Price

### Developer Cost

```
Total Hours:           [X] hrs
× Developer Rate:      $[Y]/hr
─────────────────────────────────
= Developer Cost:      $[Z]
```

**Standard Developer Rates:**
| Level | Rate |
|-------|------|
| Junior | $50-75/hr |
| Mid-level | $75-125/hr |
| Senior | $125-200/hr |
| Specialist | $200-300/hr |

### Add Margins

```
Developer Cost:        $[Z]
+ Architect Margin:    $[Z × 0.40] (40%)
+ Sales Fee:           $[Z × 0.15] (15%)
+ Infrastructure:      $[Fixed or %]
─────────────────────────────────────────
= Client Price:        $[Total]
```

### Margin Targets

| Role | Percentage | Goes To |
|------|------------|---------|
| Developer | Base cost | Dev payment |
| Architect Margin | 30-50% | Matthew (oversight, quality) |
| Sales Fee | 10-20% | Mekaiel/Chris (sales effort) |
| Infrastructure | Fixed | Tools, hosting, etc. |

**Minimum total margin:** 40% above developer cost

---

## Pricing Calculator Template

```markdown
# Pricing Calculator: [Client Name]

**Date:** [Date]
**Project:** [Brief description]
**Calculated By:** [Name]
**Validated By:** [Matthew - required]

---

## Complexity Scoring

| Dimension | Score (0-10) | Notes |
|-----------|--------------|-------|
| Integration Complexity | [X] | [e.g., "2 APIs, well-documented"] |
| Data Complexity | [X] | [e.g., "Medium volume, standard formats"] |
| Business Logic | [X] | [e.g., "Some conditional rules"] |
| User Interface | [X] | [e.g., "Basic admin dashboard"] |
| Security/Compliance | [X] | [e.g., "Standard auth, no special compliance"] |
| **Total Score** | **[X]/50** | |

**Complexity Tier:** [ ] Simple / [ ] Standard / [ ] Complex / [ ] Enterprise / [ ] Major

---

## Hours Calculation

### Method: [ ] Vibe Coding / [ ] Feature Estimate

**If Vibe Coding:**
- Vibe code time: [X] minutes
- Multiplier: [X]x
- Base hours: [X] hrs

**If Feature Estimate:**
| Feature | Hours |
|---------|-------|
| [Feature 1] | [X] hrs |
| [Feature 2] | [X] hrs |
| [Feature 3] | [X] hrs |
| **Base Total** | **[X] hrs** |

---

## Overhead Calculation

| Category | % | Hours |
|----------|---|-------|
| Base Development | 100% | [X] hrs |
| Testing | 30% | [X] hrs |
| Documentation | 10% | [X] hrs |
| Project Management | 15% | [X] hrs |
| Buffer | 25% | [X] hrs |
| **Total Hours** | **180%** | **[X] hrs** |

---

## Pricing Calculation

| Item | Calculation | Amount |
|------|-------------|--------|
| Total Hours | | [X] hrs |
| Developer Rate | | $[Y]/hr |
| **Developer Cost** | [X] × $[Y] | **$[Z]** |
| Architect Margin (40%) | $[Z] × 0.40 | $[A] |
| Sales Fee (15%) | $[Z] × 0.15 | $[B] |
| Infrastructure | Fixed | $[C] |
| **Client Price** | | **$[Total]** |

---

## Margin Validation

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Margin | [X]% | >40% | [ ] Pass / [ ] Fail |
| Hourly Rate (effective) | $[X]/hr | >$150/hr | [ ] Pass / [ ] Fail |
| ROI for Client | [X]% | >100% | [ ] Pass / [ ] Fail |

---

## Pricing Summary

| Phase | Hours | Price | Timeline |
|-------|-------|-------|----------|
| Phase 1 (MUST) | [X] hrs | $[Y] | [Z] weeks |
| Phase 2 (SHOULD) | [X] hrs | $[Y] | [Z] weeks |
| Phase 3 (COULD) | [X] hrs | $[Y] | [Z] weeks |
| **Total Vision** | **[X] hrs** | **$[Y]** | **[Z] weeks** |

**Proposal Price (Phase 1):** $[X]
```

---

## Quick Pricing Reference

### By Project Type

| Project Type | Typical Range | Typical Timeline |
|--------------|---------------|------------------|
| Simple Automation | $3,000 - $8,000 | 1-2 weeks |
| Standard Integration | $8,000 - $20,000 | 2-4 weeks |
| Custom Dashboard | $10,000 - $25,000 | 3-5 weeks |
| Complex Workflow | $20,000 - $50,000 | 4-8 weeks |
| Full Platform | $50,000+ | 8+ weeks |

### By Discovery Pricing

| Discovery Type | Price | Includes |
|----------------|-------|----------|
| Diagnostic Call (1 hr) | $500 | Problem diagnosis, rough estimate |
| Discovery Sprint (half-day) | $2,000 | Deep dive, vibe code, detailed scope |
| Full Discovery (1-2 days) | $3,000-5,000 | Workshops, technical review, PRD draft |

---

## Red Flags in Pricing

| Red Flag | Risk | Action |
|----------|------|--------|
| Total margin <40% | Unprofitable | Increase price or reduce scope |
| Hours > 200 (Phase 1) | Scope too big | Split into more phases |
| Client budget < calculated price | Misalignment | Reduce scope to match budget |
| Effective rate < $150/hr | Underpriced | Review complexity scoring |
| ROI for client < 100% | Hard sell | Re-examine value proposition |

---

## Example: Completed Calculator

```markdown
# Pricing Calculator: Print Shop Automation

**Date:** February 2026
**Project:** Ticket automation + dispatch system
**Calculated By:** Mekaiel
**Validated By:** Matthew ✓

---

## Complexity Scoring

| Dimension | Score | Notes |
|-----------|-------|-------|
| Integration | 4 | Phone system + QuickBooks |
| Data | 3 | Customer records, tickets |
| Business Logic | 5 | Dispatch rules, scheduling |
| User Interface | 4 | Admin dashboard |
| Security | 2 | Basic auth |
| **Total** | **18/50** | |

**Complexity Tier:** [x] Standard

---

## Hours Calculation

**Vibe Coding:** 30 minutes → 80x multiplier → 40 base hours

## Overhead

| Category | % | Hours |
|----------|---|-------|
| Base | 100% | 40 hrs |
| Testing | 30% | 12 hrs |
| Documentation | 10% | 4 hrs |
| PM | 15% | 6 hrs |
| Buffer | 25% | 10 hrs |
| **Total** | **180%** | **72 hrs** |

---

## Pricing

| Item | Calculation | Amount |
|------|-------------|--------|
| Total Hours | | 72 hrs |
| Developer Rate | | $100/hr |
| **Developer Cost** | | **$7,200** |
| Architect (40%) | | $2,880 |
| Sales (15%) | | $1,080 |
| Infrastructure | | $200 |
| **Client Price** | | **$11,360** |

**Rounded Proposal Price:** $12,000

---

## Margin Check

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Margin | 47% | >40% | [x] Pass |
| Effective Rate | $167/hr | >$150/hr | [x] Pass |
| Client ROI | 320% | >100% | [x] Pass |
```

---

## Related Documents

- [DEV-REQUIREMENTS-GAPS.md](../DEV-REQUIREMENTS-GAPS.md) - Gap 6
- [moscow-prioritization-template.md](./moscow-prioritization-template.md) - Scope feeds hours
- [milestone-payment-terms.md](./milestone-payment-terms.md) - Payment structure
- Matthew's Framework: `development-framework/01-requirements-discovery/03-requirements-refinement.md`
