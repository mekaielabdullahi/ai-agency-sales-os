# SOP: ROI Verification for AI Opportunities

**Purpose:** Verify each AI opportunity ROI with real client data before presenting.

---

## Overview

Each ROI calculation has 3 sections that need verification:
- **Section A:** Time Cost (hours wasted × people × rate)
- **Section B:** Lost Revenue (volume × loss rate × value per unit)
- **Section C:** Revenue Upside (opportunities enabled by automation)

---

## Step 1: Extract Evidence from Fireflies

Open the Fireflies meeting transcript and prompt Claude:

```
Read this Fireflies transcript and extract:

1. TIME WASTED (Section A):
   - Direct quotes about time spent on manual tasks
   - Specific hour estimates mentioned
   - Task descriptions that indicate inefficiency

2. LOST REVENUE (Section B):
   - Quotes about mistakes, errors, or things "slipping through cracks"
   - Volume numbers (how many quotes, leads, orders affected)
   - Any dollar amounts mentioned for losses

3. REVENUE UPSIDE (Section C):
   - Quotes about what they could do "if only" they had time
   - Opportunities they're missing
   - Conversion rates when follow-up happens

Format as a table:
| Quote | Speaker | Section | Data Point |
```

---

## Step 2: Request Client Data Exports

Ask the client for actual data to verify assumptions:

| Data Needed | Source System | Verifies |
|-------------|---------------|----------|
| Invoice export (12 months) | Jobber/QuickBooks | Value per unit |
| Quote log | CRM/Quo | Volume of quotes |
| Time tracking | Any | Hours per task |
| AR aging report | Accounting | Collection opportunity |

---

## Step 3: Analyze Data with Claude

Upload the export and prompt:

```
Analyze this [Jobber/QuickBooks] export:

1. Total records and date range
2. Filter out: drafts, $0 invoices, credits
3. Categorize by type (service calls, equipment, supplies, contracts)
4. For each category, calculate:
   - Count
   - Mean
   - Median
   - 75th percentile
   - 90th percentile
5. Provide distribution breakdown by price range

I need the MEAN for [service calls/quotes] to use as Value per Unit.
```

---

## Step 4: Update ROI Documents

Update both files in `/roi-calculator/`:

### OPP-X-[NAME].md
1. Update Section B table with real data
2. Replace "Industry benchmark" source with actual data source
3. Add data analysis section showing methodology
4. Recalculate Annual Lost Revenue
5. Update Total Y

### Y-CALCULATION-WORKING-DOC.md
1. Update Section B inputs
2. Update calculation block
3. Update Section B Summary
4. Update Total Y table

---

## Step 5: Commit Changes

```bash
git add roi-calculator/OPP-*.md roi-calculator/Y-CALCULATION-WORKING-DOC.md
git commit -m "docs(project): Update [Section] with [data source]

- Value per unit: $X → $Y (source)
- Annual impact: $X → $Y
- Total Y: $X → $Y

Source: [Client system] export ([N] records, [date])"
```

---

## Verification Checklist

Before presenting ROI to client:

- [ ] Section A: Time estimates validated (Fireflies quotes OR time tracking data)
- [ ] Section B: Value per unit from real data (not industry benchmark)
- [ ] Section B: Volume validated (CRM/system data)
- [ ] Section C: Conversion rates realistic (industry standard or client history)
- [ ] All calculations verified (A + B + C = Total Y)
- [ ] Data sources cited in document

---

## Example: Plotter Mechanix Opp 4

| Section | Original Source | Verified Source | Change |
|---------|-----------------|-----------------|--------|
| A: Time | Fireflies estimate | Fireflies (1.5 hrs/day) | Kept |
| B: Value/Unit | Industry benchmark ($1,500) | Jobber export ($750 mean) | -50% |
| B: Volume | Kelsey quote (15 quotes) | Fireflies | Kept |
| C: Upside | Industry estimates | Fireflies quotes | Kept |

**Result:** Total Y HIGH dropped from $1,312,580 to $1,245,080 (more defensible)

---

*Created: 2026-02-17*
