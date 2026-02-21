# Plotter Mechanix Phase 2 - ROI Validation Plan

**Created:** January 24, 2026
**Purpose:** Replace assumptions with data to justify $45k investment
**Target:** Convert 80%+ of ROI calculations from estimates to verified data

---

## Executive Summary

**Current State:** Our $153,600 Year 1 ROI calculation is based on ~70% assumptions, 30% data.

**Goal:** Collect real data from Plotter Mechanix to validate (or adjust) our pricing before presenting Phase 2.

**Timeline:** 2 weeks of data collection before Phase 2 presentation

**Outcome:** Bulletproof ROI case backed by THEIR data, not our estimates.

---

## ROI Calculation Audit: What's Real vs. Assumed?

### Training System ROI ($48,400/year claimed)

| Variable | Current Assumption | Data Source | Confidence | Action Required |
|----------|-------------------|-------------|------------|-----------------|
| Kelsey training time | 5 hrs/week | Estimate | 🔴 **LOW** | Track for 2 weeks |
| Kelsey hourly rate | $300/hr | Industry standard | 🟡 **MEDIUM** | Confirm with Kelsey |
| Reduction achievable | 50% | Optimistic guess | 🔴 **LOW** | Benchmark case studies |
| Training time per new hire | 4-6 weeks | Estimate | 🔴 **LOW** | Ask Kelsey: How long did Joe take? |
| Future hires planned | 2 in 3 years | Vague plan | 🟡 **MEDIUM** | Confirm hiring roadmap |

**Risk:** If actual training time is 2 hrs/week (not 5), ROI drops to $19,360/year (60% lower)

---

### Equipment CRM ROI ($53,600/year claimed)

| Variable | Current Assumption | Data Source | Confidence | Action Required |
|----------|-------------------|-------------|------------|-----------------|
| Bad contract avoidance | $5k-10k/year | PK Associates example | 🟢 **HIGH** | Document this case |
| Eligible customers | 20 customers | Guess | 🔴 **LOW** | Count from Jobber |
| Contract price | $99/mo | Industry rate | 🟡 **MEDIUM** | Confirm Plotter's pricing |
| Capture rate Year 1 | 25% | Conservative | 🟡 **MEDIUM** | Validate with sales velocity |
| Maintenance upsell value | $10k-20k/year | Range guess | 🔴 **LOW** | Get actual upsell data |
| Revenue baseline | $600k/year | Rough estimate | 🔴 **LOW** | **CRITICAL: Confirm actual revenue** |
| Churn rate current | Unknown | No data | 🔴 **LOW** | Calculate from Jobber |
| Retention improvement | 5% | Industry standard | 🟡 **MEDIUM** | Benchmark |

**Risk:** If revenue is $400k (not $600k), retention value drops to $20k (33% lower)

---

### Ply Enhancement ROI ($33,600/year claimed)

| Variable | Current Assumption | Data Source | Confidence | Action Required |
|----------|-------------------|-------------|------------|-----------------|
| Inventory value lost | $50k | Rough guess | 🔴 **LOW** | **CRITICAL: Audit actual inventory** |
| Recovery rate | 10-20% | Industry range | 🟡 **MEDIUM** | Get used parts inventory value |
| "Do we have X?" interruptions | 10/day | Estimate | 🔴 **LOW** | Track with Alyssa for 1 week |
| Time per interruption | 5 min | Guess | 🔴 **LOW** | Time with stopwatch |
| Reduction achievable | 80% | Optimistic | 🟡 **MEDIUM** | Validate with integration scope |
| Adoption rate | 50% | Conservative | 🟡 **MEDIUM** | Depends on Megan's buy-in |

**Risk:** If interruptions are 3/day (not 10), ROI drops to $9,360/year (72% lower)

---

### Integration Work ROI ($18,000/year claimed)

| Variable | Current Assumption | Data Source | Confidence | Action Required |
|----------|-------------------|-------------|------------|-----------------|
| Alyssa manual work time | 7.5 hrs/week | Estimate | 🔴 **LOW** | Track for 1 week |
| Alyssa hourly rate | $25/hr | Guess | 🟡 **MEDIUM** | Confirm actual wage |
| Automation reduction | 40% | Optimistic | 🟡 **MEDIUM** | Validate with workflow analysis |
| Error rate | 5% | Industry average | 🟡 **MEDIUM** | Count actual errors |
| Jobs per year | 500 | Estimate | 🔴 **LOW** | Pull from Jobber |
| Cost per error | $50 | Guess | 🟡 **MEDIUM** | Ask Kelsey/Alyssa |

**Risk:** If Alyssa's manual work is 3 hrs/week (not 7.5), ROI drops to $6,240/year (65% lower)

---

## Data Collection Action Plan

### Phase 1: Immediate Data Requests (This Week)

**Owner: Matthew (or delegate to Linh/Mikael)**

#### Request 1: Business Financials
**Ask Kelsey/Nikki:**
> "To build an accurate ROI model for Phase 2, we need a few baseline numbers. Can you share:
> 1. Annual revenue (2024 or trailing 12 months)
> 2. Number of active customers in Jobber
> 3. Number of service calls/jobs completed in 2024
> 4. Kelsey's target hourly rate for billing (for time-savings calculations)
> 5. Alyssa's hourly wage (for automation ROI)"

**Expected Output:**
- Actual revenue: $XXX,XXX
- Active customers: XX
- Jobs completed: XXX
- Kelsey rate: $XXX/hr
- Alyssa wage: $XX/hr

**Impact:** Validates 40% of our ROI calculations

---

#### Request 2: Jobber Data Export
**Ask Kelsey/Nikki:**
> "Can you export a CSV from Jobber with:
> 1. All active customers (name, last service date, total revenue)
> 2. All jobs from 2024 (date, customer, job type, revenue)
> 3. Current inventory items (if tracked in Jobber)"

**Expected Output:**
- Customer list with revenue
- Job frequency data
- Equipment/maintenance history (if exists)

**Impact:** Validates 30% of our ROI calculations

---

#### Request 3: Megan's Ply Progress
**Ask Megan (via interview):**
> "To avoid duplicating your work:
> 1. What inventory categories have you set up in Ply?
> 2. How much used parts inventory exists (dollar value)?
> 3. What's your estimate of lost/unoptimized inventory annually?
> 4. How integrated is Ply with Jobber currently? (% complete)"

**Expected Output:**
- Ply implementation status: XX% complete
- Used parts inventory: $XX,XXX
- Lost inventory estimate: $XX,XXX/year

**Impact:** Validates 25% of our ROI calculations

---

### Phase 2: Time Tracking Study (1-2 Weeks)

**Owner: Alyssa (with our support)**

#### Study 1: "Do we have X?" Interruption Tracking
**Instructions for Alyssa:**
> "For the next 5 business days, please track:
> - Each time Kelsey/Joe/customer asks 'Do we have [part] in stock?'
> - How long it takes you to answer (start to finish)
> - Whether you had to call/text/check multiple places
> - Record in simple tally sheet (we'll provide template)"

**Template:**
```
Date: ________
Interruptions: |||| |||| (tally marks)
Avg time per interruption: ___ minutes
Notes: _________________________________
```

**Expected Output:**
- Interruptions per day: X (validate our 10/day assumption)
- Avg time: X minutes (validate our 5 min assumption)

**Impact:** Validates or invalidates $25k/year ROI claim

---

#### Study 2: Alyssa Manual Work Time Tracking
**Instructions for Alyssa:**
> "For the next 5 business days, please track time spent on:
> - Data entry (customer info, job notes, etc.)
> - Calling back customers with info you had to look up
> - Updating Jobber after calls
> - Any manual inventory checks
> - Total: ___ hours per day"

**Template:**
```
Date: ________
Data entry: ___ min
Callback calls: ___ min
Jobber updates: ___ min
Inventory checks: ___ min
Other manual tasks: ___ min
TOTAL: ___ hours
```

**Expected Output:**
- Manual work time: X hrs/day (validate our 1.5 hrs/day assumption)

**Impact:** Validates $3,900/year ROI claim

---

#### Study 3: Kelsey Training Time Tracking
**Instructions for Kelsey:**
> "For the next 5 business days, please track:
> - Time spent training Joe (showing him procedures, answering questions)
> - Time spent checking Joe's work
> - Time spent fixing Joe's mistakes
> - Record in simple log (we'll provide template)"

**Template:**
```
Date: ________
Training/teaching Joe: ___ min
Reviewing Joe's work: ___ min
Fixing Joe's errors: ___ min
TOTAL: ___ hours
```

**Expected Output:**
- Training time: X hrs/week (validate our 5 hrs/week assumption)

**Impact:** Validates $48,400/year ROI claim (largest single item)

---

### Phase 3: Historical Data Analysis (1 Week)

**Owner: Matthew + Analyst Agent**

#### Analysis 1: Customer Retention & Churn
**Data Source:** Jobber export

**Questions to Answer:**
1. How many customers had service in 2023 but NOT in 2024?
2. Churn rate: X%
3. Average customer LTV
4. Value of 5% retention improvement

**Method:**
```
1. Export Jobber customers with last service date
2. Count customers with last service in 2023 (churned)
3. Calculate: Churned / Total = Churn Rate
4. Calculate: Avg revenue per customer × Churn rate × 5% = Retention value
```

**Expected Output:**
- Current churn rate: X%
- Value of 5% improvement: $XX,XXX/year
- Validates or adjusts our $30k/year retention claim

---

#### Analysis 2: Service Contract Eligibility
**Data Source:** Jobber export + Equipment specs

**Questions to Answer:**
1. How many customers have regular recurring service?
2. Which customers DON'T have contracts but should?
3. What's the opportunity value?

**Method:**
```
1. List customers with 3+ service calls in 2024
2. Filter: Which ones DON'T have active service contracts?
3. Calculate: Eligible customers × $99/mo × 12 = Opportunity
```

**Expected Output:**
- Contract-eligible customers: XX
- Opportunity value: $XX,XXX/year
- Validates our 20 customers × $99/mo assumption

---

#### Analysis 3: Training Time Per New Hire
**Data Source:** Interview with Kelsey

**Questions to Ask:**
> "Kelsey, when you hired Joe:
> 1. How many weeks before he could do a service call alone?
> 2. How many hours per week did you spend training him?
> 3. How long until he was 50% productive? 80%?
> 4. If you hired Steve next month, would it take the same time?"

**Expected Output:**
- Weeks to basic competency: X weeks
- Hours of Kelsey time invested: XX hours
- Validates our 4-6 weeks assumption

---

## Action Item Summary

### Team Responsibilities

| Person | Action | Timeline | Deliverable |
|--------|--------|----------|-------------|
| **Matthew** | Request financials from Kelsey/Nikki | This week | Revenue, customer count, job count confirmed |
| **Matthew** | Request Jobber data export | This week | Customer & job CSV files |
| **Matthew** | Schedule Megan interview | This week | Ply status, inventory data |
| **Linh** | Support Matthew on client communication | This week | Ensure data requests are fulfilled |
| **Alyssa** | Track "Do we have X?" interruptions | Week 1-2 | 5-day interruption log |
| **Alyssa** | Track manual work time | Week 1-2 | 5-day time log |
| **Kelsey** | Track Joe training time | Week 1-2 | 5-day training log |
| **Matthew** | Analyze Jobber data (churn, contracts) | Week 2 | Retention & contract opportunity report |
| **Matthew** | Interview Kelsey on training timeline | Week 2 | Joe onboarding timeline documented |

---

## Validation Checklist

Before presenting Phase 2 at $45k, we must validate:

### Critical (Must Have) ✅
- [ ] Actual annual revenue (not $600k estimate)
- [ ] Actual Kelsey training time (not 5 hrs/week estimate)
- [ ] Actual "Do we have X?" interruptions (not 10/day estimate)
- [ ] Actual used parts inventory value (not $50k estimate)
- [ ] Actual customer count eligible for contracts (not 20 estimate)

### Important (Should Have) 🔶
- [ ] Kelsey's actual billing rate (not $300/hr estimate)
- [ ] Alyssa's actual manual work time (not 7.5 hrs/week estimate)
- [ ] Actual churn rate (not 5% estimate)
- [ ] Joe's actual training timeline (not 4-6 weeks estimate)
- [ ] Actual job error rate (not 5% estimate)

### Nice to Have (Bonus) 🎁
- [ ] Maintenance upsell values from past 12 months
- [ ] Inventory shrinkage/loss data
- [ ] Time to answer customer questions (avg)
- [ ] Ply implementation % complete

---

## Adjusted ROI Calculation Framework

Once we have real data, update pricing analysis with:

### Conservative Scenario (Use Minimums)
- Use lowest data points from time tracking
- Apply 60% adoption discount
- **Result:** Minimum defensible ROI

### Realistic Scenario (Use Averages)
- Use average data points
- Apply 70-80% adoption rates
- **Result:** Most likely ROI (use for pricing)

### Optimistic Scenario (Use Maximums)
- Use highest data points
- Apply 90% adoption rates
- **Result:** Best case ROI (use for negotiation room)

**Presentation Strategy:**
> "Kelsey, we tracked YOUR actual data for 2 weeks. Here's what we found:
> - You spend X hours/week training Joe (not our estimate)
> - Alyssa gets interrupted X times/day looking for parts (we measured it)
> - You have $X in used parts inventory sitting unused (Megan confirmed)
> - Based on YOUR numbers, Phase 2 creates $X in Year 1 value.
> - Our $45k investment is X% of that value. Here's the breakdown..."

---

## Risk Mitigation: What If Data Invalidates Our Assumptions?

### Scenario 1: ROI Drops to $80k/year (instead of $153k)

**Our Options:**
- **Option A:** Reduce price to $32k (maintains 2.5:1 ratio)
- **Option B:** Keep $45k price, reduce scope to high-ROI items only
- **Option C:** Phase the project (prove value, then expand)

**Recommendation:** Option C - Start with Equipment CRM + Ply ($22k), prove ROI, add Training System ($23k)

---

### Scenario 2: Data EXCEEDS Our Assumptions (ROI = $200k+)

**Our Options:**
- **Option A:** Increase price to $55k (Premium Value-Based)
- **Option B:** Keep $45k, bank the goodwill
- **Option C:** Keep $45k, add success bonus clause

**Recommendation:** Option B - Keep $45k, use excess ROI to upsell Phase 3

---

### Scenario 3: Some ROI Items Validated, Others Not

**Strategy: Anchor on High-Confidence Items**

Example:
- ✅ Equipment CRM: $53k/year (validated with Jobber data)
- ✅ Ply Enhancements: $21k/year (validated with interruption tracking)
- ❌ Training System: $48k/year (can't validate without 6+ months)
- ❌ Integration Work: $18k/year (hard to measure)

**Adjusted Pitch:**
> "Kelsey, we can PROVE $74k/year in ROI from Equipment CRM + Ply enhancements. That's conservative. The Training System adds another $48k/year, but that requires longer-term measurement.
>
> At $45k investment, you're getting a 1.6x return in Year 1 on JUST the proven items. The training system value is bonus."

---

## Timeline & Milestones

### Week 1 (Jan 27 - Jan 31)
- [ ] Request financials from Kelsey/Nikki
- [ ] Request Jobber export
- [ ] Schedule Megan interview
- [ ] Start time tracking studies (Alyssa, Kelsey)

### Week 2 (Feb 3 - Feb 7)
- [ ] Complete time tracking studies
- [ ] Conduct Megan interview
- [ ] Analyze Jobber data (churn, contracts)
- [ ] Interview Kelsey on training timeline

### Week 3 (Feb 10 - Feb 14)
- [ ] Compile all data into ROI validation report
- [ ] Update PRICING-ANALYSIS.md with real numbers
- [ ] Adjust price if needed (maintain 2.5:1 ratio)
- [ ] Prepare Phase 2 presentation with data-backed ROI

### Week 4 (Feb 17 - Feb 21)
- [ ] Present Phase 2 with bulletproof ROI case
- [ ] Negotiate if needed (have data to support every claim)
- [ ] Close Phase 2 at $38k-45k

---

## Success Metrics

### Data Collection Success
- 80%+ of ROI variables validated with real data
- <20% margin of error on key assumptions
- Client confidence: "You actually measured OUR business"

### Pricing Justification Success
- Can defend every dollar of $45k investment
- ROI ratio stays >2.5:1 even with conservative data
- Client says: "This makes sense" not "This seems high"

### Close Rate Impact
- Higher close rate due to data-driven confidence
- Less price negotiation due to solid justification
- Faster decision cycle (data removes objections)

---

## Appendix: Data Collection Templates

### Template 1: Interruption Tracking Sheet
```markdown
# Alyssa's Interruption Log - Week of [Date]

## Instructions
Each time someone asks "Do we have [part]?" or you need to look up inventory:
1. Make a tally mark
2. Note how long it took to answer
3. Note if you had to call/text/check multiple places

## Daily Log

**Monday, [Date]**
Interruptions: |||| |||| ||| (13)
Avg time: 6 minutes
Notes: Had to call Kelsey 3 times, check shelf twice

**Tuesday, [Date]**
Interruptions: ___________
Avg time: ___ minutes
Notes: _________________________________

[Repeat for Wed, Thu, Fri]

## Weekly Summary
Total interruptions: ___
Avg per day: ___
Avg time per interruption: ___ min
Total time lost: ___ hours
```

### Template 2: Manual Work Time Tracking
```markdown
# Alyssa's Time Tracking - Week of [Date]

## Monday, [Date]

| Task | Start | End | Duration | Notes |
|------|-------|-----|----------|-------|
| Data entry (customer info) | 9:15 | 9:32 | 17 min | New customer setup |
| Looking up part availability | 10:20 | 10:28 | 8 min | Customer called |
| Updating Jobber after call | 11:45 | 11:52 | 7 min | Job notes |
| Inventory check (shelf) | 2:15 | 2:23 | 8 min | For quote |

**Daily Total:** ___ hours

[Repeat for Tue-Fri]

**Weekly Total:** ___ hours
**Daily Average:** ___ hours
```

### Template 3: Training Time Log
```markdown
# Kelsey's Joe Training Log - Week of [Date]

## Monday, [Date]

| Activity | Start | End | Duration | What I Taught |
|----------|-------|-----|----------|---------------|
| Showed Joe how to diagnose X | 10:00 | 10:45 | 45 min | Troubleshooting process |
| Reviewed Joe's repair work | 2:30 | 2:50 | 20 min | Checked his work on customer site |
| Fixed Joe's mistake | 4:00 | 4:15 | 15 min | He missed a step |

**Daily Total:** 1.3 hours

[Repeat for Tue-Fri]

**Weekly Total:** ___ hours
**Avg per day:** ___ hours
```

---

*Created: January 24, 2026*
*Owner: Matthew Kerns*
*Next Review: After 2 weeks of data collection (Feb 7, 2026)*
