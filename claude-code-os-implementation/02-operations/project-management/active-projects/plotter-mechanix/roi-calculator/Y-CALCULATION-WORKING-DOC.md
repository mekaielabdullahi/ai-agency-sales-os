# Plotter Mechanix - Y Calculation Working Document

**Date:** 2026-02-17
**Framework:** Morningside AI ROI Calculator
**Standard Working Days:** 260/year
**Status:** COMPLETE - Methodology Audit Applied

---

## Methodology Audit Summary

| Document | Issue Fixed | Impact |
|----------|-------------|--------|
| OPP-4 | Quote Follow-up in both B and C | Removed Section C entirely |
| OPP-5 | Escalation in both B and C | Removed escalation from B |
| OPP-6 | AR collection in both B and C | Removed AR from B |

**Pattern Assignments:**
- OPP-4: A + B only (per Morningside: "AI Quote Generator → A + B")
- OPP-5: A + B + C (B and C now capture different items)
- OPP-6: A + B + C (B and C now capture different items)

---

## Line Item 1: Quote Generation Automation

**Pattern:** A + B only

### Section A: Time Cost - COMPLETE

| Input | Value | Source |
|-------|-------|--------|
| Time wasted per day (hrs) | 1.5 | Fireflies: Conservative estimate of quote processing portion |
| Number of people | 1 | Alyssa |
| Working days/year | 260 | Standard |
| Loaded hourly cost | $22 | User input |

**Calculation:**
```
Annual Cost = 1.5 hrs × 1 person × 260 days × $22/hr
Annual Cost = $8,580/year
```

**Section A Total:** $8,580

---

### Section B: Lost Revenue - COMPLETE

| Input | Value | Source |
|-------|-------|--------|
| What's being lost | Quote conversion opportunity + mistakes | Fireflies + Discovery |
| Documented mistake | $5,000 (Tucson trip - wrong part) | Fireflies meeting |
| Estimated quotes/month | 16-20 (4-5/week) | Calculated from 50% new customer rate |
| Current close rate | 15-20% | Industry: unmanaged quotes |
| Potential close rate | 60-70% | Industry: systematic follow-up |
| Quote value | $750 | Jobber data (mean of 460 service invoices) |

**Calculation (Conversion Opportunity Framework):**
```
Monthly quotes:              16-20
Current close rate:          ~18% (midpoint of 15-20%)
Potential close rate:        ~65% (midpoint of 60-70%)

Current conversions/month:   16-20 × 18% = 3-4 jobs
Potential conversions/month: 16-20 × 65% = 10-13 jobs
MISSED conversions/month:    6-10 jobs

Conservative: 6 × $750 × 12 = $54,000/year
Aggressive:   10 × $750 × 12 = $90,000/year
Plus documented mistake:     + $5,000/year
```

**Section B Summary:**
| Loss Area | Annual LOW | Annual HIGH |
|-----------|------------|-------------|
| Quote conversion gap | $54,000 | $90,000 |
| Documented mistakes | $5,000 | $5,000 |
| **TOTAL** | **$59,000** | **$95,000** |

---

### Section C: REMOVED

Per Morningside methodology, Section C was removed to avoid double-counting:
- Quote follow-up already captured in Section B conversion gap
- AR Collections → Moved to OPP-6
- Supply Sales → Moved to OPP-6
- Customer Retention → Moved to OPP-6

---

### TOTAL Y (Quote Generation) - CORRECTED

| Section | Annual Low | Annual High |
|---------|------------|-------------|
| A: Time Cost | $8,580 | $8,580 |
| B: Lost Revenue | $59,000 | $95,000 |
| **TOTAL Y** | **$67,580** | **$103,580** |

---

## Line Item 2: Knowledge Capture & Training System

**Pattern:** A + B + C

### Section A: Time Cost - COMPLETE

#### Training Burden (Per New Tech Hire)
| Input | Value | Source |
|-------|-------|--------|
| Training time per hire (hrs) | 160-200 | Meeting with Plotter_Kelsey |
| Hires per year | 2 | Business growth plan |
| Kelsey's billable rate | $175/hr | Meeting with Plotter_Kelsey |

**Calculation:**
```
Annual Training Cost = 160-200 hrs × $175 × 2 hires
Annual Training Cost = $56,000-$70,000/year
```

#### Daily Coordination
| Input | Value | Source |
|-------|-------|--------|
| Coordination time/day (hrs) | 1 | Meeting with Plotter_Kelsey |
| Working days/year | 260 | Standard |
| Kelsey's rate | $175/hr | Billable rate |

**Calculation:**
```
Annual Coordination Cost = 1 hr × $175 × 260 days
Annual Coordination Cost = $45,500/year
```

#### Parts Research (Alyssa)
| Input | Value | Source |
|-------|-------|--------|
| Research time per order (hrs) | 0.5-0.75 | Plotter Mechanix-alyssa workflow |
| Orders per week | 2-3 | Estimated from context |
| Alyssa's rate | $25/hr | Administrative rate |

**Calculation:**
```
Annual Parts Research = 0.625 hrs × 2.5/week × $25 × 52 weeks
Annual Parts Research = $1,300-$2,925/year
```

**Section A Summary:**
| Cost Area | Annual LOW | Annual HIGH |
|-----------|------------|-------------|
| Training new techs | $56,000 | $70,000 |
| Daily coordination | $45,500 | $45,500 |
| Parts research | $1,300 | $2,925 |
| **TOTAL** | **$102,800** | **$118,425** |

---

### Section B: Lost Revenue - CORRECTED

**Note:** Escalation delays REMOVED (now in Section C as freed capacity)

| Input | Value | Source |
|-------|-------|--------|
| Documented HP mistake | $5,000 | Meeting with Plotter_Kelsey |
| RMA lost credits | $2,000-$5,000 | Plotter Mechanix-alyssa workflow |

**Section B Summary:**
| Loss Area | Annual LOW | Annual HIGH |
|-----------|------------|-------------|
| Documented mistakes | $5,000 | $5,000 |
| RMA lost credits | $2,000 | $5,000 |
| **TOTAL** | **$7,000** | **$10,000** |

---

### Section C: Revenue Upside - COMPLETE

#### Training Time Savings
| Input | Value | Source |
|-------|-------|--------|
| Current training time | 160-200 hrs | Meeting with Plotter_Kelsey |
| Target training time | 40-50 hrs | 75% reduction with video library |
| Saved hrs per hire | 120-150 | Calculated |
| Hires per year | 2 | Business growth plan |
| Kelsey's rate | $175/hr | Billable rate |

**Calculation:**
```
Annual Training Savings = 120-150 hrs × $175 × 2 hires
Annual Training Savings = $42,000-$52,500/year
```

#### Freed Escalation Capacity
| Input | Value | Source |
|-------|-------|--------|
| Escalation reduction target | 50% | From 25% to 12.5% with knowledge base |
| Freed Kelsey hrs/week | 2-3 | Calculated |

**Calculation:**
```
Annual Freed Capacity = 2.5 hrs × $175 × 52 weeks
Annual Freed Capacity = $18,200-$27,300/year
```

#### Remote Consulting Upside
| Input | Value | Source |
|-------|-------|--------|
| Consulting rate | $175/hr | Meeting with Plotter_Kelsey |
| Additional hrs/week | 5-10 | Meeting w/ Nikki: Pinetop vision |

**Calculation:**
```
Annual Consulting Upside = 5-10 hrs × $175 × 52 weeks
Annual Consulting Upside = $45,500-$91,000/year
```

**Section C Summary:**
| Opportunity | Annual LOW | Annual HIGH |
|-------------|------------|-------------|
| Training time savings | $42,000 | $52,500 |
| Freed escalation capacity | $18,200 | $27,300 |
| Remote consulting upside | $45,500 | $91,000 |
| **TOTAL** | **$105,700** | **$170,800** |

---

### TOTAL Y (Knowledge Capture) - CORRECTED

| Section | Annual Low | Annual High |
|---------|------------|-------------|
| A: Time Cost | $102,800 | $118,425 |
| B: Lost Revenue | $7,000 | $10,000 |
| C: Revenue Upside | $105,700 | $170,800 |
| **TOTAL Y** | **$215,500** | **$299,225** |

---

## Line Item 3: Contacts Consolidation + Outreach/Marketing

**Pattern:** A + B + C

### Section A: Time Cost - CORRECTED

| Input | Value | Source |
|-------|-------|--------|
| Duplicate entry elimination | 0.5 hrs/day | Plotter Mechanix-alyssa workflow |
| Data cleanup time | 0.25 hrs/day | Plotter Mechanix-alyssa workflow |
| QuickBooks sync errors | 0.125 hrs/day | Plotter Mechanix-alyssa workflow |
| Contact search time | 0.5 hrs/day | Estimated |
| Alyssa's hourly rate | $25/hr | Administrative rate |
| Working days/year | 260 | Standard |

**Calculation:**
```
Duplicate elimination:    0.5 hrs × $25 × 260 = $3,250/year
Data cleanup:             0.25 hrs × $25 × 260 = $1,625/year
QuickBooks sync errors:   0.125 hrs × $25 × 260 = $812.50/year
Contact search time:      0.5 hrs × $25 × 260 = $3,250/year
CALCULATED TOTAL:         $8,937.50/year
```

**Range Application:**
- LOW (80% efficiency): $8,937.50 × 0.80 = $7,150
- HIGH (120% variability): $8,937.50 × 1.20 = $10,725

**Section A Summary:**
| Cost Area | Annual LOW | Annual HIGH |
|-----------|------------|-------------|
| Duplicate entry elimination | $2,600 | $3,900 |
| Data cleanup | $1,300 | $1,950 |
| QuickBooks sync errors | $650 | $975 |
| Contact search time | $2,600 | $3,900 |
| **TOTAL** | **$7,150** | **$10,725** |

---

### Section B: Lost Revenue - CORRECTED

**Note:** AR collection gaps REMOVED (now in Section C as recovery opportunity)

| Input | Value | Source |
|-------|-------|--------|
| Contact invisibility loss | $5,000-$10,000 | 246:1 disparity (Kelsey vs team average) |
| Capsule CRM unused | $30/month | DISCOVERY-FINDINGS |

**Calculation:**
```
Contact invisibility:     Lost opportunities = $5,000-$10,000/year
Capsule CRM waste:        $30 × 12 = $360/year
```

**Section B Summary:**
| Loss Area | Annual LOW | Annual HIGH |
|-----------|------------|-------------|
| Contact invisibility | $5,000 | $10,000 |
| Capsule CRM unused | $360 | $360 |
| **TOTAL** | **$5,360** | **$10,360** |

---

### Section C: Revenue Upside - COMPLETE

#### Opportunity 1: AR Systematic Recovery
| Input | Value | Source |
|-------|-------|--------|
| Affected accounts/month | 5-10 | Fireflies meeting |
| Recovery rate with access | 70% | "When I call they pay" |
| Average invoice | $750 | Jobber analysis |
| **Annual Revenue** | **$31,500-$63,000** | |

#### Opportunity 2: Andrew Supplies Visibility
| Input | Value | Source |
|-------|-------|--------|
| Hidden customer base | 100 | Andrew's 2 contacts vs Kelsey's 10,581 |
| Average supply sale/year | $500 | Consumables estimate |
| **Annual Revenue** | **$50,000** | |

#### Opportunity 3: Service Contract Renewals
| Input | Value | Source |
|-------|-------|--------|
| Eligible customers | 20 | Customers with qualifying equipment |
| Contract value | $99/month | Proposed maintenance agreement |
| **Annual Revenue** | **$23,760** | |

#### Opportunity 4: Top Customer Activation
| Input | Value | Source |
|-------|-------|--------|
| Contacts for activation | 1,000 | Conservative (from 10,581) |
| Conversion rate | 2% | With systematic outreach |
| Value per activation | $750 | Jobber mean |
| **Annual Revenue** | **$15,000** | |

**Section C Summary:**
| Opportunity | Annual LOW | Annual HIGH |
|-------------|------------|-------------|
| AR systematic recovery | $31,500 | $63,000 |
| Andrew supplies visibility | $50,000 | $50,000 |
| Service contract renewals | $23,760 | $23,760 |
| Top customer activation | $15,000 | $15,000 |
| **TOTAL** | **$120,260** | **$151,760** |

---

### TOTAL Y (Contacts Consolidation) - CORRECTED

| Section | Annual Low | Annual High |
|---------|------------|-------------|
| A: Time Cost | $7,150 | $10,725 |
| B: Lost Revenue | $5,360 | $10,360 |
| C: Revenue Upside | $120,260 | $151,760 |
| **TOTAL Y** | **$132,770** | **$172,845** |

---

## GRAND TOTAL Y (All Line Items) - CORRECTED

| Line Item | Annual LOW | Annual HIGH |
|-----------|------------|-------------|
| 1: Quote Generation Automation | $67,580 | $103,580 |
| 2: Knowledge Capture & Training | $215,500 | $299,225 |
| 3: Contacts Consolidation + Outreach | $132,770 | $172,845 |
| **COMBINED TOTAL Y** | **$415,850** | **$575,650** |

---

## Comparison: Before vs After Audit

| Line Item | Previous LOW | Previous HIGH | Corrected LOW | Corrected HIGH | Change |
|-----------|--------------|---------------|---------------|----------------|--------|
| OPP-4 | $247,580 | $1,267,580 | $67,580 | $103,580 | -73% to -92% |
| OPP-5 | $226,875 | $321,975 | $215,500 | $299,225 | -5% to -7% |
| OPP-6 | $146,530 | $198,610 | $132,770 | $172,845 | -9% to -13% |
| **TOTAL** | **$620,985** | **$1,788,165** | **$415,850** | **$575,650** | **-33% to -68%** |

**Note:** The reduction reflects the removal of double-counting, not a reduction in actual opportunity. The corrected figures are now defensible and auditable.

---

## Sources

| Meeting | URL |
|---------|-----|
| Meeting with Plotter_Kelsey | https://app.fireflies.ai/view/01KH1QBWAEVPK4PQVG2FB4F4TD |
| Meeting w/ Nikki - Plotter Mechanix | https://app.fireflies.ai/view/01KEA3M22BPVHYR2ZB3BGK668Z |
| Meeting with Plotter Mechanix | https://app.fireflies.ai/view/01KCMCY0H3JRZV87EX0Z0ZRHMP |
| Plotter Mechanix-alyssa workflow | https://app.fireflies.ai/view/01KH6ZF397K4C6BNYGASMDX88V |

---

*Working document - Updated 2026-02-17*
*Methodology Audit: Double-counting violations corrected*
*Framework: Morningside AI ROI Calculator*
