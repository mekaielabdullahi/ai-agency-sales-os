# Money Slide Generator
## Creating the Most Powerful Slide in Your AI Audit Presentation

**Purpose**: Generate a clear, compelling ROI summary table that makes the investment decision obvious.

**Critical Insight from Liam Ottley**: "This is the grand finale. It's a table that summarizes all recommended AI solutions, their implementation costs, and the calculated financial impact. This is the single most powerful slide for getting client buy-in."

**When to Use**: Final presentation slide, after explaining individual opportunities.

---

## Table of Contents

1. [What is the Money Slide?](#what-is-the-money-slide)
2. [Data Requirements](#data-requirements)
3. [Money Slide Format](#money-slide-format)
4. [How to Generate from audit.json](#how-to-generate-from-auditjson)
5. [Presentation Best Practices](#presentation-best-practices)
6. [Examples](#examples)
7. [Common Mistakes](#common-mistakes)

---

## What is the Money Slide?

### The Concept

The Money Slide is a **single table** that shows:
- Every AI opportunity you're recommending
- What each costs to implement
- What each delivers in value (direct savings + revenue uplift)
- Total ROI and payback period

**Why it's powerful:**
- Condenses complex audit into one clear view
- Shows total investment required
- Shows total value delivered
- Makes ROI calculation transparent and credible
- Creates "shut up and take my money" moment

---

### What It's NOT

❌ A detailed explanation of each solution
❌ A pitch deck with 20 slides
❌ A technical architecture diagram
❌ A project plan with Gantt charts

✅ A **simple, scannable table** that answers: "What do we invest and what do we get back?"

---

## Data Requirements

### From audit.json

You need the following data populated in `money_slide` object:

```json
{
  "money_slide": {
    "slide_title": "Investment & ROI Summary",
    "opportunities": [
      {
        "opportunity_id": "opp_001",
        "name": "Automated Lead Capture & CRM Sync",
        "implementation_cost": 10000,
        "direct_savings_annual": 33748,
        "revenue_uplift_annual": 702000,
        "total_impact_annual": 735748,
        "roi_percentage": 7257,
        "payback_months": 0.16
      },
      // ... more opportunities
    ],
    "totals": {
      "total_investment": 33000,
      "total_direct_savings": 80548,
      "total_revenue_uplift": 952000,
      "total_annual_value": 1032548,
      "blended_roi_percentage": 3029,
      "average_payback_months": 0.38
    }
  }
}
```

### How to Populate This Data

**Option 1: From ai_opportunity_matrix**

For each opportunity in roadmap, pull from `ai_opportunity_matrix[].roi_calculation`:

```json
{
  "opportunity_id": "opp_001",
  "name": "Automated Lead Capture & CRM Sync",
  "implementation_cost": ai_opportunity_matrix[0].roi_calculation.implementation_cost,
  "direct_savings_annual": ai_opportunity_matrix[0].roi_calculation.direct_cost_savings.annual_cost_savings,
  "revenue_uplift_annual": ai_opportunity_matrix[0].roi_calculation.revenue_uplift.annual_revenue_potential,
  "total_impact_annual": ai_opportunity_matrix[0].roi_calculation.total_annual_value,
  "roi_percentage": ai_opportunity_matrix[0].roi_calculation.roi_percentage,
  "payback_months": ai_opportunity_matrix[0].roi_calculation.break_even_months
}
```

**Option 2: From roadmap**

For each initiative in roadmap phases, extract estimated effort and value:

```json
{
  "name": roadmap.phase_1_quick_wins[0].name,
  "implementation_cost": roadmap.phase_1_quick_wins[0].estimated_effort_cost,
  "direct_savings_annual": // calculate from estimated_value,
  "revenue_uplift_annual": // calculate from estimated_value
}
```

---

## Money Slide Format

### Standard Table Format

| Solution | Investment | Direct Savings (Annual) | Revenue Uplift (Annual) | Total Value (Annual) | ROI % | Payback |
|----------|-----------|-------------------------|-------------------------|----------------------|-------|---------|
| [Opportunity 1] | $X,XXX | $X,XXX | $X,XXX | $X,XXX | X,XXX% | X days/months |
| [Opportunity 2] | $X,XXX | $X,XXX | $X,XXX | $X,XXX | X,XXX% | X days/months |
| [Opportunity 3] | $X,XXX | $X,XXX | $X,XXX | $X,XXX | X,XXX% | X days/months |
| **TOTAL** | **$XX,XXX** | **$XX,XXX** | **$XXX,XXX** | **$XXX,XXX** | **X,XXX%** | **X days** |

---

### Alternative Format: Simplified (Good for 1-3 Opportunities)

| Initiative | Investment | Annual Value | ROI | Payback |
|------------|-----------|--------------|-----|---------|
| [Name] | $XX,XXX | $XXX,XXX | X,XXX% | X months |
| **TOTAL** | **$XX,XXX** | **$XXX,XXX** | **X,XXX%** | **X months** |

---

### Alternative Format: Phased Roadmap Table

| Phase | Solutions | Investment | Monthly Value | Break-Even |
|-------|-----------|-----------|---------------|------------|
| **Phase 1: Quick Wins** (30 days) | • Lead Capture<br>• AI Scoring | $25,000 | $61,000 | 12 days |
| **Phase 2: Scale-Up** (90 days) | • Automated Follow-up<br>• CRM Enhancement | $20,000 | $25,000 | 24 days |
| **Phase 3: Strategic** (180 days) | • Forecasting Dashboard<br>• Account Intelligence | $35,000 | $15,000 | 2.3 months |
| **TOTAL** | 6 Solutions | **$80,000** | **$101,000** | **24 days** |

---

## How to Generate from audit.json

### Step 1: Extract Data

**Python/JavaScript Example:**

```python
def generate_money_slide(audit_data):
    money_slide = audit_data['money_slide']
    opportunities = money_slide['opportunities']
    totals = money_slide['totals']

    # Create table rows
    rows = []
    for opp in opportunities:
        row = {
            'Solution': opp['name'],
            'Investment': f"${opp['implementation_cost']:,}",
            'Direct Savings': f"${opp['direct_savings_annual']:,}",
            'Revenue Uplift': f"${opp['revenue_uplift_annual']:,}",
            'Total Value': f"${opp['total_impact_annual']:,}",
            'ROI %': f"{opp['roi_percentage']:,}%",
            'Payback': format_payback(opp['payback_months'])
        }
        rows.append(row)

    # Add totals row
    totals_row = {
        'Solution': '**TOTAL**',
        'Investment': f"**${totals['total_investment']:,}**",
        'Direct Savings': f"**${totals['total_direct_savings']:,}**",
        'Revenue Uplift': f"**${totals['total_revenue_uplift']:,}**",
        'Total Value': f"**${totals['total_annual_value']:,}**",
        'ROI %': f"**{totals['blended_roi_percentage']:,}%**",
        'Payback': f"**{format_payback(totals['average_payback_months'])}**"
    }
    rows.append(totals_row)

    return rows

def format_payback(months):
    if months < 1:
        days = round(months * 30)
        return f"{days} days"
    elif months < 12:
        return f"{months:.1f} months"
    else:
        years = months / 12
        return f"{years:.1f} years"
```

---

### Step 2: Format as Markdown Table

```python
def create_markdown_table(rows):
    # Headers
    headers = ['Solution', 'Investment', 'Direct Savings', 'Revenue Uplift', 'Total Value', 'ROI %', 'Payback']

    # Create header row
    header_row = '| ' + ' | '.join(headers) + ' |'
    separator = '|' + '|'.join(['---' for _ in headers]) + '|'

    # Create data rows
    data_rows = []
    for row in rows:
        data_row = '| ' + ' | '.join([str(row[h]) for h in headers]) + ' |'
        data_rows.append(data_row)

    # Combine
    table = '\n'.join([header_row, separator] + data_rows)
    return table
```

---

### Step 3: Export to Presentation Format

**For PowerPoint/Google Slides:**
- Copy markdown table
- Paste into table in slide
- Format with:
  - Header row: Bold, colored background
  - Totals row: Bold, highlighted
  - Numbers: Right-aligned
  - Currency: Proper formatting with commas

**For PDF Report:**
- Export markdown to HTML table
- Style with CSS
- Convert to PDF

---

## Presentation Best Practices

### Visual Design

**Do:**
- ✅ Use color to highlight totals row (green or blue)
- ✅ Right-align all numbers
- ✅ Bold the header row and totals row
- ✅ Use consistent currency formatting ($XX,XXX)
- ✅ Keep font size large enough to read (18pt minimum)
- ✅ Use comma separators for thousands

**Don't:**
- ❌ Overcomplicate with too many colors
- ❌ Use tiny font
- ❌ Add chart/graph overlays (keep it clean)
- ❌ Include too many columns (max 7)

---

### How to Present the Money Slide

**Setup (Before showing the slide):**

"We've walked through each opportunity individually. Now I want to show you the total picture - what it costs and what you get back."

**Reveal the slide**

**Walkthrough (Row by row):**

"Let me walk you through this table:

[Point to first row]
The first initiative, [Name], requires an investment of [Cost]. It delivers [Direct Savings] in labor cost savings, plus [Revenue Uplift] in revenue opportunity, for a total value of [Total Value] per year. That's a [ROI]% return with payback in [Payback Period].

[Point to second row]
The second initiative, [Name]...

[Continue for each row]

**Emphasize the totals row:**

[Point to totals row]
When we add all of this up: **You're investing [Total Investment], and getting [Total Value] in annual value. That's a [Total ROI]% return on investment, with an average payback of [Payback Period].**

**Pause for effect. Let it sink in.**

To put that in perspective: Every dollar you invest returns [ROI/100] dollars in year one alone."

**Address the obvious:**

"I know those numbers look aggressive. That's why we built them conservatively:
- We only counted 50% of time savings reallocated to revenue
- We used historical conversion rates, not best-case
- We didn't include efficiency gains or customer experience improvements

Even if we're off by 50%, this is still a [ROI/2]% return."

**Close with confidence:**

"This isn't a cost. It's an investment that pays for itself in [Payback] and keeps delivering value year after year."

---

### Handling Questions

**Q: "These ROI numbers seem too good to be true."**

A: "I understand the skepticism - these are big numbers. Let me show you how we calculated them. [Go to ROI methodology slide or appendix]. Every number comes from your team's interviews and your actual data. We've been conservative at every step.

But you're right to question it. What if we're 50% wrong? Even at half these numbers, it's still a [ROI/2]% return. What would make you comfortable with these projections?"

**Q: "What if the revenue uplift doesn't materialize?"**

A: "Great question. The revenue uplift assumes your team reallocates the time we save them. If that doesn't happen - if we just save time and nothing else - you still get the direct cost savings of [$X]. That's still a [X]% ROI and a [Y] month payback.

The revenue uplift is the upside if you're strategic about reallocation. The cost savings alone justify the investment."

**Q: "What about ongoing costs?"**

A: "Good catch. These numbers include ongoing costs of [$X per month] for [AI API calls, subscriptions, maintenance]. The annual value is NET of those ongoing costs.

Here's the breakdown: [Show detailed calculation if needed]"

**Q: "Can we do Phase 1 only and decide on the rest later?"**

A: "Absolutely. You don't have to commit to the full roadmap upfront. Phase 1 Quick Wins require [$X] investment and deliver [$Y] in annual value. That's a [Z]% ROI with [A] month payback.

If Phase 1 delivers as promised, we move to Phase 2. If not, you've still gotten value from Phase 1 and you stop there. No obligation."

---

## Examples

### Example 1: Sales Team Automation

| Solution | Investment | Direct Savings | Revenue Uplift | Total Value | ROI % | Payback |
|----------|-----------|----------------|----------------|-------------|-------|---------|
| Automated Lead Capture & CRM Sync | $10,000 | $33,748 | $702,000 | $735,748 | 7,257% | 5 days |
| AI-Powered Lead Scoring | $15,000 | $18,200 | $250,000 | $268,200 | 1,688% | 20 days |
| Automated Follow-up Sequences | $8,000 | $12,600 | $0 | $12,600 | 58% | 7.6 months |
| **TOTAL** | **$33,000** | **$64,548** | **$952,000** | **$1,016,548** | **2,980%** | **12 days** |

**Presentation notes:**
- Lead Capture is the star - highlight it
- Follow-up has lower ROI but still positive
- Total payback is under 2 weeks

---

### Example 2: Customer Success Automation

| Solution | Investment | Direct Savings | Revenue Uplift | Total Value | ROI % | Payback |
|----------|-----------|----------------|----------------|-------------|-------|---------|
| Automated Onboarding Workflows | $8,000 | $33,000 | $1,123,200 | $1,156,200 | 14,352% | 3 days |
| Self-Service Knowledge Base | $5,000 | $18,000 | $0 | $18,000 | 260% | 3.3 months |
| AI Chatbot for Common Questions | $12,000 | $28,000 | $156,000 | $184,000 | 1,433% | 24 days |
| **TOTAL** | **$25,000** | **$79,000** | **$1,279,200** | **$1,358,200** | **5,333%** | **7 days** |

**Presentation notes:**
- Onboarding automation is transformational
- Knowledge base is lowest ROI but still solid
- CS team unlocking revenue through better retention/upsells

---

### Example 3: Operations Efficiency

| Solution | Investment | Direct Savings | Revenue Uplift | Total Value | ROI % | Payback |
|----------|-----------|----------------|----------------|-------------|-------|---------|
| Automated Reporting Dashboard | $5,000 | $13,988 | $0 | $13,988 | 180% | 4.3 months |
| Data Integration & Sync | $10,000 | $28,600 | $0 | $28,600 | 186% | 4.2 months |
| Process Documentation AI | $3,000 | $8,500 | $0 | $8,500 | 183% | 4.2 months |
| **TOTAL** | **$18,000** | **$51,088** | **$0** | **$51,088** | **184%** | **4.2 months** |

**Presentation notes:**
- No revenue uplift (pure efficiency plays)
- Still strong ROI (nearly 200%)
- Quick payback (under 5 months)

---

## Common Mistakes

### Mistake 1: Including Too Many Opportunities

**Problem:** Table with 10+ rows is overwhelming and dilutes impact.

**Fix:** Show only top 3-5 opportunities on Money Slide. Put the rest in appendix.

---

### Mistake 2: Overly Optimistic ROI

**Problem:** 50,000% ROI makes people skeptical, not excited.

**Fix:** Use conservative assumptions. Better to under-promise and over-deliver.

---

### Mistake 3: No Revenue Uplift Breakdown

**Problem:** Client questions the revenue number because it's not explained.

**Fix:** Have a backup slide showing revenue uplift calculation methodology.

---

### Mistake 4: Inconsistent with Earlier Slides

**Problem:** Money Slide shows different numbers than individual opportunity slides.

**Fix:** Double-check all numbers match. Use single source of truth (audit.json).

---

### Mistake 5: Not Showing Payback Period

**Problem:** ROI % alone doesn't answer "when do we get our money back?"

**Fix:** Always include payback period column. Executives care about this.

---

### Mistake 6: Forgetting Ongoing Costs

**Problem:** ROI looks amazing, but then ongoing costs kill the economics.

**Fix:** Include ongoing costs in calculation. Show NET value after ongoing costs.

---

## Money Slide Generation Checklist

Before presenting Money Slide:

### Data Quality
- [ ] All investment costs validated and accurate
- [ ] Direct savings calculations reviewed
- [ ] Revenue uplift methodology sound and conservative
- [ ] Ongoing costs included in calculations
- [ ] All numbers match individual opportunity slides

### Formatting
- [ ] Currency formatted with $ and commas
- [ ] ROI % includes % symbol
- [ ] Payback shows units (days/months/years)
- [ ] Totals row is bold and highlighted
- [ ] Numbers are right-aligned
- [ ] Font size is readable (18pt+)

### Presentation
- [ ] Backup slide with calculation methodology
- [ ] Prepared to answer "these numbers are too good" objection
- [ ] Can explain each opportunity in 1 sentence
- [ ] Conservative case scenario calculated
- [ ] Confidence in every number

### Storytelling
- [ ] Opening line prepared
- [ ] Row-by-row walkthrough practiced
- [ ] Totals emphasis planned
- [ ] Closing statement ready
- [ ] Pause for effect built in

---

## Template Code

### Python Function

```python
def generate_money_slide_from_audit(audit_json_path, output_format='markdown'):
    """
    Generate Money Slide from audit.json

    Args:
        audit_json_path: Path to audit.json file
        output_format: 'markdown' | 'html' | 'csv'

    Returns:
        Formatted table string
    """
    import json

    with open(audit_json_path) as f:
        audit = json.load(f)

    money_slide = audit.get('money_slide', {})
    opportunities = money_slide.get('opportunities', [])
    totals = money_slide.get('totals', {})

    if not opportunities:
        return "Error: No opportunities in money_slide"

    # Build rows
    rows = []
    for opp in opportunities:
        row = [
            opp['name'],
            f"${opp['implementation_cost']:,}",
            f"${opp['direct_savings_annual']:,}",
            f"${opp['revenue_uplift_annual']:,}",
            f"${opp['total_impact_annual']:,}",
            f"{opp['roi_percentage']:,}%",
            format_payback(opp['payback_months'])
        ]
        rows.append(row)

    # Add totals
    totals_row = [
        '**TOTAL**',
        f"**${totals['total_investment']:,}**",
        f"**${totals['total_direct_savings']:,}**",
        f"**${totals['total_revenue_uplift']:,}**",
        f"**${totals['total_annual_value']:,}**",
        f"**{totals['blended_roi_percentage']:,}%**",
        f"**{format_payback(totals['average_payback_months'])}**"
    ]
    rows.append(totals_row)

    headers = ['Solution', 'Investment', 'Direct Savings', 'Revenue Uplift', 'Total Value', 'ROI %', 'Payback']

    if output_format == 'markdown':
        return format_as_markdown(headers, rows)
    elif output_format == 'html':
        return format_as_html(headers, rows)
    elif output_format == 'csv':
        return format_as_csv(headers, rows)

def format_payback(months):
    if months < 1:
        days = round(months * 30)
        return f"{days} days"
    elif months < 12:
        return f"{round(months, 1)} months"
    else:
        years = round(months / 12, 1)
        return f"{years} years"

# Usage
money_slide_md = generate_money_slide_from_audit('audit.json', 'markdown')
print(money_slide_md)
```

---

## Summary: Money Slide Power Framework

**Purpose:** Single table showing investment vs. value for all opportunities

**Format:**
- Row per opportunity
- Columns: Solution, Investment, Direct Savings, Revenue Uplift, Total Value, ROI %, Payback
- Bold totals row

**Data Source:** `money_slide` object in audit.json

**Presentation:**
1. Setup: "Here's the total picture"
2. Walk through: Row by row
3. Emphasize: Totals row
4. Pause: Let it sink in
5. Address: "These numbers look aggressive..."
6. Close: "Investment that pays for itself in [X]"

**Impact:** This slide closes deals. Get it right.

---

**Related Resources:**
- `roi-calculation-methodology.md` - How to calculate the numbers
- `opportunity-validation-workshop.md` - How to validate before creating this
- `audit-template.json` - Data structure reference

---

**Document Version**: 1.0
**Last Updated**: 2025-12-09
**Owner**: AriseGroup.ai Audit Team
**Based on**: Liam Ottley's "Money Slide" concept
