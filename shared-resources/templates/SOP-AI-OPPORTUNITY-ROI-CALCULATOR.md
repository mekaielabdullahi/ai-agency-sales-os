# SOP: AI Opportunity ROI Calculator

**Purpose:** Calculate and document ROI for any AI opportunity from scratch.
**Framework:** Morningside AI ROI Calculator
**Output:** Validated OPP-X-[NAME].md file with defensible ROI

---

## Quick Start (TL;DR)

| Step | Action | Output |
|------|--------|--------|
| 1 | Create opportunity file | OPP-X-[NAME].md |
| 2 | Extract Fireflies evidence | Quotes for A, B, C |
| 3 | Analyze client data | Value per unit, volumes |
| 4 | Fill in template | Calculated ROI |
| 5 | Validate and save | Committed, cited |

---

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Fireflies meeting transcript link
- [ ] Client data export (invoices, quotes, CRM export)
- [ ] Client hourly rate info (or use $22-$35 estimate)
- [ ] Project folder path: `/[project]/roi-calculator/`

---

## Step 1: Create the Opportunity File

### File Naming Convention
```
OPP-[#]-[SHORT-NAME].md
```

**Examples:**
- `OPP-1-INTAKE-AUTOMATION.md`
- `OPP-2-QUOTE-FOLLOW-UP.md`
- `OPP-3-INVOICE-PROCESSING.md`
- `OPP-4-QUOTE-GENERATION-AUTOMATION.md`

### Location
Save in: `[project-folder]/roi-calculator/OPP-X-[NAME].md`

### Action
Copy the **Blank OPP Template** from the Templates section below.

---

## Step 2: Extract Fireflies Evidence

### 2.1 Open the Fireflies Transcript
Navigate to the Fireflies meeting link and copy the full transcript.

### 2.2 Run the Extraction Prompt
Copy this prompt into Claude with the transcript:

---

**FIREFLIES EXTRACTION PROMPT** (Copy this)

```
Read this Fireflies transcript and extract evidence for ROI calculation.

## SECTION A: TIME WASTED
Find quotes about:
- Time spent on manual/repetitive tasks
- Specific hour estimates mentioned
- Feeling "behind" or overwhelmed
- Multi-step manual workflows

## SECTION B: REVENUE LOST
Find quotes about:
- Mistakes, errors, or things "slipping through cracks"
- Volume numbers (how many quotes, leads, orders affected)
- Dollar amounts for documented losses
- Missed follow-ups or lost opportunities

## SECTION C: REVENUE UPSIDE
Find quotes about:
- What they could do "if only" they had time
- Conversion rates when follow-up actually happens
- Opportunities they know exist but can't pursue
- Revenue activities blocked by current problems

## OUTPUT FORMAT

### Time Wasted Evidence (Section A)
| Quote | Speaker | Implication |
|-------|---------|-------------|
| "exact quote" | Name | X hrs/day implied |

### Lost Revenue Evidence (Section B)
| Quote | Speaker | Value Implied |
|-------|---------|---------------|
| "exact quote" | Name | $X lost |

### Revenue Upside Evidence (Section C)
| Quote | Speaker | Opportunity |
|-------|---------|-------------|
| "exact quote" | Name | $X potential |

### Estimated Time Breakdown
| Task | Daily Hours | Notes |
|------|-------------|-------|
| Task name | X hrs | Based on: quote |

### Data Limitations
List what was NOT explicitly stated:
- [ ] Exact hours per task
- [ ] Volume counts
- [ ] Dollar amounts
```

---

### 2.3 Paste Results into Template
Copy the extracted evidence into the corresponding sections of your OPP file.

---

## Step 3: Analyze Client Data

### 3.1 Request Data Exports
Ask client for these exports:

| Data Needed | Source System | Verifies |
|-------------|---------------|----------|
| Invoice export (12 months) | Jobber/QuickBooks/FreshBooks | Value per unit |
| Quote log | CRM/Quo/HubSpot | Volume of quotes |
| Time tracking | Any (if available) | Hours per task |
| AR aging report | Accounting | Collection opportunity |

### 3.2 Run the Data Analysis Prompt
Upload the export and run this prompt:

---

**DATA ANALYSIS PROMPT** (Copy this)

```
Analyze this [SYSTEM NAME] export to extract ROI inputs.

## TASK 1: Data Cleaning
1. Total records and date range
2. Filter out: drafts, $0 entries, credits, voided
3. Identify data quality issues

## TASK 2: Categorization
Categorize by type (identify the best categories for this business):
- Service calls/jobs
- Equipment sales
- Supply orders
- Contracts/retainers
- Other

## TASK 3: Statistics per Category
For each category, calculate:
| Metric | Value |
|--------|-------|
| Count | |
| Mean | |
| Median | |
| 75th percentile | |
| 90th percentile | |

## TASK 4: Distribution Analysis
Show distribution by price range:
| Range | Count | % of Total |
|-------|-------|------------|
| $0-$100 | | |
| $100-$250 | | |
| $250-$500 | | |
| $500-$1,000 | | |
| $1,000-$2,500 | | |
| $2,500+ | | |

## OUTPUT
Recommend VALUE PER UNIT for ROI calculation:
- For [category], use: $X (based on [mean/median/other])
- Rationale: [why this is appropriate]
```

---

### 3.3 Document Analysis Results
Add a "Data Analysis" subsection to Section B of your OPP file.

---

## Step 4: Fill in the Template

### Section A Calculation Worksheet

```
TIME COST CALCULATION

Inputs:
- Time wasted per person per day (hours): ___
- Number of people doing this task: ___
- Working days per year: 260 (standard)
- Loaded hourly cost ($): ___

Formula:
Annual Cost = Hours × People × 260 × Rate
Annual Cost = ___ × ___ × 260 × $___
Annual Cost = $___/year

Source citations:
- Hours: [Fireflies quote or data source]
- People: [Fireflies/discovery]
- Rate: [Client provided or estimate $22-$35]
```

### Section B Calculation Worksheet

```
LOST REVENUE CALCULATION

Inputs:
- What is being lost: [describe]
- Volume affected per month: ___
- % lost due to this problem: ___%
- Value per unit ($): $___

Formula:
Annual Lost = Volume × Loss% × Value × 12
Annual Lost = ___ × ___% × $___ × 12
Annual Lost = $___/year

Source citations:
- Volume: [Fireflies quote or CRM data]
- Loss %: [Industry benchmark 30-50% or documented]
- Value: [Client data export - specify mean/median]
```

### Section C Calculation Worksheet

```
REVENUE UPSIDE CALCULATION

For each opportunity enabled by the solution:

Opportunity: [Name]
- Activities per month: ___
- Conversion/success rate: ___%
- Value per conversion: $___

Formula:
Monthly = Activities × Conversion% × Value
Monthly = ___ × ___% × $___
Monthly = $___/month
Annual = $___/year

Repeat for each opportunity, then sum.

Source citations:
- Activities: [Fireflies evidence]
- Conversion: [Client quote or industry 40-80%]
- Value: [Client data or Fireflies estimate]
```

### Total Y Summary

```
TOTAL ANNUAL IMPACT

| Section | Annual LOW | Annual HIGH |
|---------|------------|-------------|
| A: Time Cost | $_____ | $_____ |
| B: Lost Revenue | $_____ | $_____ |
| C: Revenue Upside | $_____ | $_____ |
| **TOTAL Y** | **$_____** | **$_____** |

Conservative uses: documented data only
Full uses: documented + reasonable estimates
```

---

## Step 5: Validate and Save

### 5.1 Run Verification Checklist

Before presenting ROI to client, verify:

- [ ] **Section A:** Time estimates validated (Fireflies quotes OR time tracking data)
- [ ] **Section B:** Value per unit from real data (not just industry benchmark)
- [ ] **Section B:** Volume validated (CRM/system data or direct quotes)
- [ ] **Section C:** Conversion rates realistic (industry standard or client history)
- [ ] **All calculations verified:** A + B + C = Total Y (math checks out)
- [ ] **Data sources cited:** Every number has a source in the document
- [ ] **Data limitations disclosed:** Honest about what was estimated vs. documented

### 5.2 Add to Y-CALCULATION-WORKING-DOC.md

Copy the summary tables to the project's working document:
`[project]/roi-calculator/Y-CALCULATION-WORKING-DOC.md`

### 5.3 Commit with Source Citation

```bash
git add roi-calculator/OPP-*.md roi-calculator/Y-CALCULATION-WORKING-DOC.md
git commit -m "docs([project]): Add [Opportunity Name] ROI document

- Section A: $X (time cost)
- Section B: $X (lost revenue)
- Section C: $X-$X (revenue upside)
- Total Y: $X-$X

Source: [Fireflies meeting name] + [Data export source]"
```

---

## TEMPLATES

### Blank OPP Template

Copy everything below for a new opportunity:

```markdown
# OPPORTUNITY [#]: [Opportunity Name]

## Solution Overview
[One paragraph describing what the AI solution does]

---

## SECTION A: WHAT THIS PROBLEM COSTS IN WASTED TIME

| Field | Value | Source | Rationale |
|-------|-------|--------|-----------|
| Time wasted per person per day (hours) | **___** | | |
| Number of people doing this task | **___** | | |
| Working days per year | **260** | Standard | Default |
| Loaded hourly cost ($) | **$___** | | |
| **ANNUAL COST OF INEFFICIENCY** | **$___** | Calculated | Formula below |

**Calculation:**
```
Annual Cost = ___ hrs × ___ people × 260 days × $___ /hr
Annual Cost = $___/year
```

### Fireflies Evidence (Section A):
[Paste extracted quotes here]

### Data Limitations (Honest Disclosure):
The following data points were **NOT explicitly specified**:
- [ ] Exact hours per day
- [ ] Time per task
- [ ] Volume count

---

## SECTION B: REVENUE YOU'RE LOSING TODAY

| Field | Value | Source | Rationale |
|-------|-------|--------|-----------|
| What is being lost? | **___** | | |
| Volume affected per month | **___** | | |
| % lost due to this problem | **___%** | | |
| Value per unit ($) | **$___** | | |
| **ANNUAL LOST REVENUE** | **$___** | Calculated | Formula below |

**Calculation:**
```
Annual Lost = ___ × ___% × $___ × 12 months
Annual Lost = $___/year
```

### Fireflies Evidence (Section B):
[Paste extracted quotes here]

### Data Analysis (Value per Unit):
**Source:** [System name] export ([N] records, [date range])

| Metric | Value |
|--------|-------|
| Count | |
| Mean | |
| Median | |
| 75th percentile | |

**Value used:** $X - [rationale]

---

## SECTION C: NEW REVENUE THE SOLUTION UNLOCKS

| Field | Value | Source | Rationale |
|-------|-------|--------|-----------|
| What does saved time enable? | **___** | | |
| Additional activities per month | **___** | | |
| Conversion / success rate (%) | **___%** | | |
| Value per conversion ($) | **$___** | | |

### Revenue Opportunity Breakdown:

| Opportunity | Activities/Mo | Conversion | Value/Each | Monthly | Annual |
|-------------|---------------|------------|------------|---------|--------|
| [Name 1] | | | | | |
| [Name 2] | | | | | |
| [Name 3] | | | | | |
| **TOTAL** | | | | **$___** | **$___** |

### Fireflies Evidence (Section C):
[Paste extracted quotes here]

---

## TOTAL ANNUAL IMPACT (A + B + C)

| Section | Annual LOW | Annual HIGH | Status |
|---------|------------|-------------|--------|
| A: Time Cost | $_____ | $_____ | |
| B: Lost Revenue | $_____ | $_____ | |
| C: Revenue Upside | $_____ | $_____ | |
| **TOTAL Y** | **$_____** | **$_____** | |

---

## SOLUTION COST INPUTS (For ROI Calculation)

| Field | Value | Notes |
|-------|-------|-------|
| Solution implementation cost ($) | TBD | |
| Annual tool/license cost ($) | TBD | |
| Total first-year cost | TBD | |

### ROI Preview (If solution costs $X):
- **ROI (Conservative):** $Y_LOW ÷ $X = **Xx**
- **ROI (Full):** $Y_HIGH ÷ $X = **Xx**
- **Payback:** X months

---

## SECTION D: REFERENCE DATA & ASSUMPTIONS

| Field | Value | Source |
|-------|-------|--------|
| Business type | | |
| Service area | | |
| Team size | | |
| Average job value | | |

---

## KEY VALIDATION QUOTE

> "[Most powerful quote that validates the problem]"
> — [Speaker], [Company]

**ROI Justification:**
[One sentence explaining why this ROI is defensible]

---

## SOURCE
Fireflies Meeting: [Meeting name](URL)

---

*Generated: [Date]*
*Framework: Morningside AI ROI Calculator*
```

---

## Reference

### Example Implementation
See: `plotter-mechanix/roi-calculator/OPP-4-QUOTE-GENERATION-AUTOMATION.md`

### Industry Benchmarks (When Client Data Unavailable)

| Metric | Conservative | Moderate | Aggressive |
|--------|--------------|----------|------------|
| Lost quote conversion | 30% | 50% | 70% |
| Follow-up conversion lift | +20% | +30% | +40% |
| AR collection success | 60% | 75% | 90% |
| Hourly rate (admin) | $22 | $30 | $40 |
| Hourly rate (technical) | $35 | $50 | $75 |

### Common Value per Unit Ranges

| Business Type | Low | Typical | High |
|---------------|-----|---------|------|
| Service business | $150 | $500 | $2,000 |
| B2B services | $500 | $2,500 | $10,000 |
| Equipment sales | $2,000 | $8,000 | $25,000 |
| SaaS/subscriptions | $50/mo | $200/mo | $1,000/mo |

---

*Created: 2026-02-17*
*Version: 1.0*
*Framework: Morningside AI ROI Calculator*
