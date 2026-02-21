# Metrics Discovery Template

**Template ID:** ARISE-TPL-001
**Version:** 1.0
**Created:** February 16, 2026
**Use During:** Discovery Call (Section 3 - Success Metrics)
**Owner:** Sales (Mekaiel)

---

## Purpose

Capture measurable business KPIs during discovery calls. These metrics flow into the proposal, PRD, test plan, and final delivery review. They become the objective proof that we delivered value.

---

## When to Use

- **During:** Discovery call (after problem discovery, before solution exploration)
- **Time:** 10 minutes of the call
- **Output:** Completed metrics table for proposal and PRD

---

## Discovery Questions

### Business Impact Questions

Ask these to establish measurable outcomes:

1. **"What are the top 2-3 measurable outcomes you need from this project?"**
   - Listen for: time saved, cost reduced, revenue gained, errors eliminated

2. **"What does 'success' look like in numbers?"**
   - Get specific: "5 hours → 30 minutes" not "faster"

3. **"What are your current baselines?"**
   - Example: "Processing 50 invoices takes 40 hours/month"

4. **"How would you measure ROI on this investment?"**
   - Helps them justify the purchase internally

### Current Measurement Questions

5. **"How do you track this process today?"**
   - Spreadsheets, tools, manual, nothing?

6. **"What metrics do you already have access to?"**
   - Don't create new tracking if they have existing data

7. **"Who would need to see the results dashboard?"**
   - Identifies stakeholders and reporting needs

8. **"How often would you review performance data?"**
   - Daily, weekly, monthly → drives refresh requirements

---

## Metrics Capture Table

**Fill this out during or immediately after the call:**

```markdown
## Success Metrics - [Client Name]
**Captured:** [Date]
**Call Attendees:** [Names]

### Primary KPIs (Must have 2-3)

| # | KPI | Current Baseline | Target | How We Measure | Timeframe |
|---|-----|------------------|--------|----------------|-----------|
| 1 | [e.g., Invoice processing time] | [e.g., 40 hrs/month] | [e.g., 4 hrs/month] | [e.g., Time tracking in system] | [e.g., 60 days] |
| 2 | [e.g., Error rate] | [e.g., 15%] | [e.g., <2%] | [e.g., Exception log count] | [e.g., 90 days] |
| 3 | [e.g., Customer response time] | [e.g., 24 hours] | [e.g., 2 hours] | [e.g., Ticket timestamps] | [e.g., 30 days] |

### ROI Calculation

| Metric | Value |
|--------|-------|
| Monthly time saved | [X] hours |
| Hourly rate (client's cost) | $[X]/hr |
| Monthly savings | $[X] |
| Annual savings | $[X] |
| Project cost estimate | $[X] |
| **Payback period** | **[X] months** |
| **First-year ROI** | **[X]%** |

### Secondary Metrics (Nice to have)

| Metric | Current | Target | Notes |
|--------|---------|--------|-------|
| [e.g., Team satisfaction] | [e.g., Low] | [e.g., High] | [e.g., Qualitative survey] |
| [e.g., Scalability] | [e.g., Can't grow] | [e.g., 10x volume] | [e.g., Without adding staff] |

### Measurement Method Notes

- **Data source:** [Where does the baseline data come from?]
- **Access:** [Do we have access to measure this?]
- **Frequency:** [How often will we check?]
- **Owner:** [Who on client side validates?]
```

---

## Validation Checklist

Before leaving the metrics section of the call:

- [ ] At least 2 primary KPIs identified
- [ ] Current baselines captured (with numbers, not vague)
- [ ] Target values agreed (specific, not "better")
- [ ] Measurement method identified (how we prove it)
- [ ] Timeframe discussed (30/60/90 days)
- [ ] ROI estimate calculated (even rough)

---

## Red Flags

Watch for these during metrics discovery:

| Red Flag | What It Means | Response |
|----------|---------------|----------|
| "I don't know current numbers" | May not value measurement | "Let's estimate together - roughly how many per month?" |
| "Success is hard to measure" | Vague scope incoming | "What would make you say 'this was worth it' in 6 months?" |
| "We just want it to work" | No clear success criteria | "Let's define 'working' - what does that look like day-to-day?" |
| "The team will know" | No objective measure | "How would you prove value to your leadership?" |

---

## Where This Goes

After discovery call, metrics flow to:

1. **Proposal** → ROI section justifies investment
2. **PRD** → Success criteria section
3. **Test Plan** → Acceptance criteria tie to metrics
4. **Final Delivery** → Review proves we hit targets

---

## Example: Completed Metrics (Plotter Mechanix Style)

```markdown
## Success Metrics - Plotter Mechanix
**Captured:** January 2026
**Call Attendees:** Kelsey, Alyssa, Mekaiel, Matthew

### Primary KPIs

| # | KPI | Current Baseline | Target | How We Measure | Timeframe |
|---|-----|------------------|--------|----------------|-----------|
| 1 | Admin processing time | 40 hrs/week (Alyssa) | 25 hrs/week | Time tracking | 60 days |
| 2 | Quote turnaround | 24-48 hours | <4 hours | Timestamp in system | 30 days |
| 3 | Missed follow-ups | ~20% of leads | <5% | CRM tracking | 90 days |

### ROI Calculation

| Metric | Value |
|--------|-------|
| Monthly time saved | 60 hours |
| Hourly rate (Alyssa) | $25/hr |
| Monthly savings | $1,500 |
| Annual savings | $18,000 |
| Project cost estimate | $5,000 |
| **Payback period** | **3.3 months** |
| **First-year ROI** | **260%** |

### Measurement Method Notes

- **Data source:** Existing spreadsheets + new system timestamps
- **Access:** Full access via Alyssa
- **Frequency:** Weekly check-ins during implementation, monthly after
- **Owner:** Alyssa validates time savings, Kelsey validates revenue impact
```

---

## Quick Reference Card

**Print this for discovery calls:**

```
METRICS DISCOVERY (10 min)
─────────────────────────
1. "Top 2-3 measurable outcomes?"
2. "Current baseline numbers?"
3. "Target numbers?"
4. "How will we measure?"
5. "Timeframe to achieve?"

MUST CAPTURE:
□ 2+ KPIs with numbers
□ Current → Target
□ How we prove it
□ Rough ROI estimate

ROI FORMULA:
Monthly savings × 12 ÷ Project cost = ROI%
```

---

## Related Documents

- [DEV-REQUIREMENTS-GAPS.md](../DEV-REQUIREMENTS-GAPS.md) - Gap 2
- [SOP-SD-001: Sales-Dev Collaboration](../SOP-ARISE-SD-001-sales-dev-collaboration.md)
- Matthew's Framework: `development-framework/01-requirements-discovery/01-diagnostic-call.md`
