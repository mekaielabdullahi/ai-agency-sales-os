# Arise Group CRM Templates
## 5 Questions Framework Data Tracking

**Last Updated**: November 26, 2025
**Version**: 1.0

---

## TABLE OF CONTENTS

1. [Simple Lead Tracking Template](#simple-lead-tracking-template)
2. [Detailed Conversation Tracker](#detailed-conversation-tracker)
3. [Pipeline Management Template](#pipeline-management-template)
4. [Analytics Dashboard Template](#analytics-dashboard-template)
5. [Email Sequence Tracker](#email-sequence-tracker)
6. [CRM Field Definitions](#crm-field-definitions)
7. [Import Instructions](#import-instructions)

---

## SIMPLE LEAD TRACKING TEMPLATE

**Use this for**: Quick daily tracking of Q1-Q5 conversations

### CSV Template Structure:

```csv
Lead_ID,Date,Name,Company,Industry,Source,Q1_Problem,Q2_Monthly_Cost,Q3_Timeline,Q4_Consequence,Q5_Magic_Wand,Status,Next_Action,Owner
L001,2025-11-26,John Smith,Acme Corp,SaaS,LinkedIn,Low lead quality,$45000,8 months,Miss growth targets,AI pre-qualification system,Proposal Sent,Follow up on proposal,Sarah
L002,2025-11-26,Jane Doe,Tech Inc,E-commerce,Referral,High cart abandonment,$12000,6 months,Lost revenue compounds,Automated recovery emails,In Conversation,Send Q4-Q5 email,Mike
L003,2025-11-26,Bob Johnson,Service Co,Professional Services,Cold Email,Manual workflows,$8000,2 years,Can't scale team,Workflow automation platform,Qualified,Schedule discovery call,Sarah
```

### Field Descriptions:

| Field | Description | Example |
|-------|-------------|---------|
| **Lead_ID** | Unique identifier | L001 |
| **Date** | First contact date | 2025-11-26 |
| **Name** | Contact name | John Smith |
| **Company** | Company name | Acme Corp |
| **Industry** | Business industry | SaaS, E-commerce, etc. |
| **Source** | Lead source | LinkedIn, Referral, Cold Email |
| **Q1_Problem** | Biggest problem (verbatim) | "Low lead quality" |
| **Q2_Monthly_Cost** | Cost per month (number) | 45000 |
| **Q3_Timeline** | How long they've had problem | "8 months" |
| **Q4_Consequence** | What happens if nothing changes | "Miss growth targets" |
| **Q5_Magic_Wand** | Perfect solution description | "AI pre-qualification system" |
| **Status** | Current stage | New, Qualified, Proposal Sent, Closed Won, Closed Lost |
| **Next_Action** | What happens next | "Follow up on proposal" |
| **Owner** | Sales rep name | Sarah |

---

## DETAILED CONVERSATION TRACKER

**Use this for**: Deep analysis of each conversation and proposal building

### Template Structure:

```
═══════════════════════════════════════════════════════════════
                    LEAD CONVERSATION TRACKER
═══════════════════════════════════════════════════════════════

LEAD INFORMATION
──────────────────────────────────────────────────────────────
Lead ID:              L001
Date Created:         2025-11-26
Lead Owner:           Sarah Johnson
Lead Source:          LinkedIn DM
Contact Name:         John Smith
Job Title:            Marketing Director
Company:              Acme Corp
Industry:             B2B SaaS
Company Size:         50-100 employees
Website:              www.acmecorp.com
Email:                john@acmecorp.com
Phone:                (555) 123-4567
LinkedIn:             linkedin.com/in/johnsmith

═══════════════════════════════════════════════════════════════
                    5 QUESTIONS FRAMEWORK
═══════════════════════════════════════════════════════════════

Q1: PROBLEM DISCOVERY
──────────────────────────────────────────────────────────────
Question Asked:       "What's the biggest problem in your business
                      right now?"

Their Answer:         "Our sales team is drowning in unqualified
                      leads. We're generating volume but conversion
                      rates are terrible. Reps spend 60% of their
                      time on prospects that never close."

Key Phrases:          - "drowning in unqualified leads"
                      - "volume but conversion terrible"
                      - "60% of time wasted"

Problem Category:     Lead Quality / Sales Efficiency

Severity (1-10):      8/10

Notes:                They scaled ad spend 2 months ago which made
                      this worse. Sales team morale is low.

──────────────────────────────────────────────────────────────

Q2: COST QUANTIFICATION
──────────────────────────────────────────────────────────────
Question Asked:       "How much is this costing you per month?"

Their Answer:         "We're spending about $30K/month on lead gen,
                      and our sales team wastes probably 60% of
                      their time on bad fits. That's like 3
                      full-time salaries... so maybe $45K total
                      wasted per month?"

Monthly Cost:         $45,000

Cost Breakdown:       - Lead gen spend: $30,000
                      - Wasted sales time: ~$15,000
                      - Total: $45,000

Annual Cost:          $540,000

Confidence Level:     High (they did the math themselves)

Notes:                They volunteered the calculation without
                      prompting. Good sign they understand the cost.

Pricing Range:        $13,500 - $22,500/month (30-50% of Q2)
                      Recommended: $15,000/month

──────────────────────────────────────────────────────────────

Q3: TIMELINE ASSESSMENT
──────────────────────────────────────────────────────────────
Question Asked:       "How long have you had this problem?"

Their Answer:         "About 8 months. It got worse when we scaled
                      our ad spend."

Timeline:             8 months

Total Cost to Date:   $360,000 (8 months × $45K)

Previous Solutions:   Tried manual lead scoring (didn't scale)

Why Not Solved Yet:   No good automated solution found

Urgency Score:        High (8 months = chronic pain)

Notes:                Problem is getting worse, not better.
                      Ad spend increasing = problem compounds.

──────────────────────────────────────────────────────────────

Q4: CONSEQUENCE AMPLIFICATION
──────────────────────────────────────────────────────────────
Question Asked:       "If you do nothing, what does the next 6 to
                      12 months look like?"

Their Answer:         "Honestly? We'll probably have to hire more
                      SDRs to sift through the garbage, which means
                      more overhead. Or we cut ad spend and miss
                      our growth targets. Lose-lose."

Consequences:         1. Hire more SDRs = higher overhead
                      2. Cut ad spend = miss growth targets
                      3. Either way = lose-lose scenario

Emotional Tone:       Frustrated, resigned ("lose-lose")

Stakes:               - Growth targets at risk
                      - Pressure from leadership
                      - Team morale suffering

Future Cost:          If they hire 2 more SDRs: +$10K/month
                      Total problem cost: $55K/month

Urgency Created:      Yes - clear lose-lose painted

Notes:                Use "lose-lose" language in proposal.
                      They're feeling stuck.

──────────────────────────────────────────────────────────────

Q5: MAGIC WAND SOLUTION
──────────────────────────────────────────────────────────────
Question Asked:       "If I had a magic wand and could build the
                      perfect solution to fix this, what would
                      that look like?"

Their Answer:         "I wish we had an AI system that could
                      pre-qualify leads before they ever hit the
                      sales team. Like, answer their basic
                      questions, figure out if they're a fit,
                      book qualified meetings only. That would
                      be a game-changer."

Key Phrases:          - "AI system"
                      - "pre-qualify leads before sales sees them"
                      - "answer basic questions"
                      - "figure out if they're a fit"
                      - "book qualified meetings only"
                      - "game-changer"

Must-Have Features:   1. Pre-qualification (before sales touch)
                      2. Answer basic questions (FAQ handling)
                      3. Fit assessment (qualification criteria)
                      4. Meeting booking (only qualified)

Nice-to-Have:         Automated (implied by "AI system")

Success Criteria:     Sales team only talks to qualified prospects

Notes:                Use exact phrase "pre-qualify leads before
                      they hit sales" in proposal. They said
                      "game-changer" = high emotional buy-in.

Our Solution Fit:     Excellent - we have exactly this

──────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════
                    PROPOSAL BLUEPRINT
═══════════════════════════════════════════════════════════════

Problem Statement:
"Your sales team is spending 60% of their time on unqualified
leads, costing you $45K/month and putting your growth targets
at risk."

Current Situation:
- 8 months of wasted time and money ($360K lost so far)
- Problem getting worse as ad spend scales
- Team morale suffering
- Facing lose-lose: hire more people or cut growth

Desired Outcome (Q5):
"An AI system that pre-qualifies leads before they hit your sales
team, answers basic questions, figures out fit, and only books
qualified meetings."

Our Solution:
[Build proposal using their exact Q5 language]
- AI-powered lead qualification system
- Pre-qualifies before sales touch
- Answers FAQs automatically
- Assesses fit based on your criteria
- Books meetings only with qualified prospects

Investment:
$15,000/month

ROI:
- Current cost: $45,000/month
- Our solution: $15,000/month
- Net savings: $30,000/month ($360K annually)
- Payback period: Immediate
- 12-month value: $360,000 in savings

Timeline:
Live in 2 weeks

Next Steps:
15-minute call to walk through implementation

──────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════
                    CONVERSATION HISTORY
═══════════════════════════════════════════════════════════════

Date            Channel         Activity                Status
────────────────────────────────────────────────────────────────
2025-11-26      LinkedIn DM     Initial outreach (Q1)   Sent
2025-11-26      LinkedIn DM     Response received       Replied
2025-11-27      LinkedIn DM     Q2 & Q3 email          Sent
2025-11-27      LinkedIn DM     Response received       Replied
2025-11-28      LinkedIn DM     Q4 & Q5 email          Sent
2025-11-28      LinkedIn DM     Response received       Replied
2025-11-28      Email           Proposal sent           Sent
2025-11-29      Phone           Follow-up call          Scheduled

──────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════
                    DEAL STATUS
═══════════════════════════════════════════════════════════════

Current Stage:        Proposal Sent

Next Action:          Follow-up call scheduled 2025-11-29 at 2pm

Probability:          70% (all 5 questions answered, strong fit)

Expected Close Date:  2025-12-05

Deal Value:           $15,000/month ($180,000 annually)

Competitors:          None mentioned

Decision Maker:       John Smith (confirmed)

Decision Timeline:    By end of Q4

Blockers:             None identified

Notes:                Strong fit. Quick responses. Did the ROI
                      math themselves. High confidence close.

──────────────────────────────────────────────────────────────

═══════════════════════════════════════════════════════════════
```

---

## PIPELINE MANAGEMENT TEMPLATE

**Use this for**: Weekly pipeline review and forecasting

### Template Structure:

```csv
Week_Of,Lead_ID,Name,Company,Q2_Cost,Our_Price,Net_Savings,Stage,Probability,Expected_Close_Date,Status,Days_in_Pipeline,Owner
2025-11-25,L001,John Smith,Acme Corp,$45000,$15000,$30000,Proposal Sent,70%,2025-12-05,On Track,3,Sarah
2025-11-25,L002,Jane Doe,Tech Inc,$12000,$4000,$8000,Q4-Q5 Stage,50%,2025-12-12,On Track,2,Mike
2025-11-25,L003,Bob Johnson,Service Co,$8000,$3000,$5000,Q1-Q2 Stage,30%,2025-12-20,On Track,1,Sarah
```

### Pipeline Summary Dashboard:

```
═══════════════════════════════════════════════════════════════
                    WEEKLY PIPELINE SUMMARY
═══════════════════════════════════════════════════════════════

Week Of: November 25, 2025

PIPELINE BY STAGE
──────────────────────────────────────────────────────────────
Stage                    Count    Total Value    Avg Deal Size
────────────────────────────────────────────────────────────────
New Leads                   15      $0             $0
Q1-Q2 (Discovery)           8       $96,000        $12,000
Q3-Q4 (Qualification)       5       $75,000        $15,000
Q5 (Solution Design)        3       $54,000        $18,000
Proposal Sent               4       $120,000       $30,000
Negotiation                 2       $80,000        $40,000
Closed Won                  3       $135,000       $45,000
Closed Lost                 2       $0             $0
────────────────────────────────────────────────────────────────
TOTAL PIPELINE             42       $560,000       $15,909

FORECAST
──────────────────────────────────────────────────────────────
Weighted Pipeline:          $280,000 (probability-adjusted)
Expected Closes (30 days):  $180,000
Expected Closes (60 days):  $320,000
Expected Closes (90 days):  $450,000

TEAM PERFORMANCE
──────────────────────────────────────────────────────────────
Rep            Leads    Q1-Q5 Complete    Proposals    Close %
────────────────────────────────────────────────────────────────
Sarah              18            12             6         35%
Mike               14            10             4         28%
Alex               10             6             3         30%
────────────────────────────────────────────────────────────────
TEAM TOTAL         42            28            13         31%

CONVERSION FUNNEL
──────────────────────────────────────────────────────────────
New Leads                   100%    (42 leads)
    ↓
Q1 Response                  40%    (17 leads)
    ↓
Q1 → Q2 Progression          70%    (12 leads)
    ↓
Q2 → Q5 Completion           60%    (7 leads)
    ↓
Q5 → Proposal Sent           90%    (6 leads)
    ↓
Proposal → Close             30%    (2 leads)

OVERALL CLOSE RATE: 4.8% (of all leads)
Q1-Q5 COMPLETE CLOSE RATE: 28.6% (of qualified leads)

═══════════════════════════════════════════════════════════════
```

---

## ANALYTICS DASHBOARD TEMPLATE

**Use this for**: Monthly performance analysis and pattern recognition

### Problem Analysis:

```csv
Problem_Category,Frequency,Avg_Q2_Cost,Avg_Deal_Size,Close_Rate,Industries
Lead Quality,15,$42000,$14000,35%,"SaaS, E-commerce"
Manual Workflows,12,$18000,$6000,40%,"Professional Services, Healthcare"
Customer Support Overload,8,$25000,$8500,25%,"E-commerce, SaaS"
High Cart Abandonment,6,$15000,$5000,30%,"E-commerce"
Inefficient Follow-up,5,$10000,$3500,45%,"Real Estate, Services"
```

### Industry Analysis:

```csv
Industry,Total_Leads,Q1_Response_Rate,Avg_Q2_Cost,Avg_Close_Rate,Top_Problem
SaaS,28,45%,$38000,32%,Lead Quality
E-commerce,18,38%,$22000,28%,Cart Abandonment
Professional Services,12,50%,$15000,40%,Manual Workflows
Healthcare,8,35%,$30000,25%,Patient Follow-up
Real Estate,6,42%,$12000,45%,Lead Follow-up
```

### Magic Wand Solutions Database:

```csv
Solution_Type,Frequency,Avg_Deal_Size,Build_Complexity,Industries,Sample_Q5_Answer
AI Lead Qualification,22,$15000,Medium,"SaaS, E-commerce","Pre-qualify leads before sales touch"
Workflow Automation,15,$8000,Low,"Professional Services","Automate manual processes end-to-end"
AI Phone Agent,12,$12000,Low,"Multiple","24/7 AI assistant to handle calls"
Email Automation,10,$5000,Low,"E-commerce, Services","Automated follow-up sequences"
Custom Dashboard,8,$18000,High,"SaaS","Real-time analytics and reporting"
```

---

## EMAIL SEQUENCE TRACKER

**Use this for**: Tracking email campaign performance

### Template Structure:

```csv
Lead_ID,Email_1_Sent,Email_1_Opened,Email_1_Replied,Email_2_Sent,Email_2_Opened,Email_2_Replied,Email_3_Sent,Email_3_Opened,Email_3_Replied,Email_4_Sent,Email_4_Opened,Email_4_Replied,Sequence_Status
L001,2025-11-26,2025-11-26,2025-11-26,2025-11-27,2025-11-27,2025-11-27,2025-11-28,2025-11-28,2025-11-28,2025-11-28,2025-11-29,,Active
L002,2025-11-26,2025-11-26,2025-11-26,2025-11-27,2025-11-27,,,,,,,Stalled at Email 2
L003,2025-11-26,2025-11-26,2025-11-27,2025-11-28,,,,,,,,Active
```

### Email Performance Summary:

```
═══════════════════════════════════════════════════════════════
                EMAIL SEQUENCE PERFORMANCE
═══════════════════════════════════════════════════════════════

Campaign Period: November 1-30, 2025

EMAIL 1: Q1 PROBLEM DISCOVERY
──────────────────────────────────────────────────────────────
Sent:               150
Opened:             82 (54.7%)
Replied:            45 (30.0%)
Qualified:          32 (21.3%)

Best Subject Line:  "Quick question about [their business]"
Best Send Time:     Tuesday 10am

──────────────────────────────────────────────────────────────

EMAIL 2: Q2 & Q3 COST + TIMELINE
──────────────────────────────────────────────────────────────
Sent:               45
Opened:             35 (77.8%)
Replied:            28 (62.2%)
Qualified:          22 (48.9%)

Drop-off Reason:    Unwilling to quantify cost

──────────────────────────────────────────────────────────────

EMAIL 3: Q4 & Q5 CONSEQUENCE + SOLUTION
──────────────────────────────────────────────────────────────
Sent:               28
Opened:             24 (85.7%)
Replied:            18 (64.3%)
Qualified:          15 (53.6%)

Drop-off Reason:    No clear consequence (Q4 weak)

──────────────────────────────────────────────────────────────

EMAIL 4: PROPOSAL
──────────────────────────────────────────────────────────────
Sent:               15
Opened:             14 (93.3%)
Replied:            12 (80.0%)
Meetings Booked:    8 (53.3%)
Closed:             5 (33.3%)

Average Deal:       $18,500

──────────────────────────────────────────────────────────────

OVERALL SEQUENCE PERFORMANCE
──────────────────────────────────────────────────────────────
Email 1 → Email 2:  30.0% progression
Email 2 → Email 3:  62.2% progression
Email 3 → Email 4:  53.6% progression
Email 4 → Close:    33.3% conversion

Total Sequence Close Rate: 3.3% (of all Email 1 sends)
Qualified Lead Close Rate: 33.3% (of Email 4 proposals)

═══════════════════════════════════════════════════════════════
```

---

## CRM FIELD DEFINITIONS

### Standard Fields (Required):

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| `lead_id` | Text | Unique identifier | L001 |
| `created_date` | Date | First contact date | 2025-11-26 |
| `owner` | Text | Sales rep name | Sarah Johnson |
| `contact_name` | Text | Lead's full name | John Smith |
| `company` | Text | Company name | Acme Corp |
| `email` | Email | Contact email | john@acme.com |
| `phone` | Phone | Contact phone | (555) 123-4567 |
| `industry` | Dropdown | Business industry | SaaS, E-commerce, Services |
| `company_size` | Dropdown | Employee count | 1-10, 11-50, 51-100, 101-500, 500+ |
| `source` | Dropdown | Lead source | LinkedIn, Referral, Cold Email, Website |

### 5 Questions Fields (Required):

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| `q1_problem` | Long Text | Biggest problem (verbatim) | "Sales team drowning in unqualified leads" |
| `q1_category` | Dropdown | Problem type | Lead Quality, Workflow, Support, etc. |
| `q1_severity` | Number (1-10) | How severe | 8 |
| `q2_monthly_cost` | Currency | Cost per month | $45,000 |
| `q2_confidence` | Dropdown | How confident in number | High, Medium, Low, Estimated |
| `q2_annual_cost` | Formula | Q2 × 12 | $540,000 |
| `q3_timeline` | Text | How long problem exists | "8 months" |
| `q3_timeline_months` | Number | Timeline in months | 8 |
| `q3_total_cost` | Formula | Q2 × Q3 months | $360,000 |
| `q4_consequence` | Long Text | What happens if nothing changes | "Miss growth targets or hire more people" |
| `q4_urgency_score` | Number (1-10) | How urgent | 9 |
| `q5_magic_wand` | Long Text | Perfect solution (verbatim) | "AI system that pre-qualifies leads" |
| `q5_must_haves` | Long Text | Required features | "Pre-qualification, FAQ handling, meeting booking" |

### Deal Fields (Required):

| Field Name | Type | Description | Example |
|------------|------|-------------|---------|
| `stage` | Dropdown | Pipeline stage | New, Q1-Q2, Q3-Q4, Q5, Proposal, Closed Won/Lost |
| `our_price` | Currency | Proposed monthly price | $15,000 |
| `pricing_percentage` | Formula | Our price ÷ Q2 | 33% |
| `net_savings` | Formula | Q2 - Our price | $30,000 |
| `annual_value` | Formula | Our price × 12 | $180,000 |
| `probability` | Percentage | Likelihood to close | 70% |
| `expected_close_date` | Date | Forecast close date | 2025-12-05 |
| `actual_close_date` | Date | Actual close date | 2025-12-03 |
| `close_status` | Dropdown | Won or Lost | Closed Won, Closed Lost |
| `lost_reason` | Text | Why lost (if applicable) | "Went with competitor" |
| `days_in_pipeline` | Formula | Today - Created Date | 12 days |

### Activity Tracking (Optional but Recommended):

| Field Name | Type | Description |
|------------|------|-------------|
| `last_contact_date` | Date | Last touchpoint |
| `last_contact_type` | Dropdown | Email, Call, Meeting, DM |
| `total_touchpoints` | Number | Count of all interactions |
| `next_action` | Text | What happens next |
| `next_action_date` | Date | When next action due |

---

## IMPORT INSTRUCTIONS

### For Salesforce:

1. Download CSV template
2. Navigate to: Setup → Data → Data Import Wizard
3. Select "Leads" or "Opportunities"
4. Map fields:
   - `lead_id` → External ID
   - `q1_problem` → Custom Field: Q1 Problem
   - `q2_monthly_cost` → Custom Field: Q2 Monthly Cost
   - (etc.)
5. Import and validate

### For HubSpot:

1. Navigate to: Contacts → Import
2. Select "Start an import"
3. Upload CSV
4. Map columns to HubSpot properties
5. Create custom properties for Q1-Q5 fields if needed

### For Pipedrive:

1. Navigate to: Settings → Import Data
2. Select "Deals" or "Organizations"
3. Upload CSV
4. Map fields to Pipedrive fields
5. Create custom fields for 5 Questions data

### For Google Sheets (Simple Setup):

1. Copy any CSV template above
2. Create new Google Sheet
3. Paste data
4. Format as table
5. Use built-in filters and pivot tables for analysis

---

## BEST PRACTICES

### Data Hygiene:

✅ Enter Q1-Q5 answers **verbatim** (use their exact words)
✅ Update deal stage **immediately** after each conversation
✅ Set **next action date** every time
✅ Track **all** conversations (even brief ones)
✅ Review pipeline **weekly** minimum

### Analysis Cadence:

- **Daily**: Update individual lead statuses
- **Weekly**: Review pipeline and next actions
- **Monthly**: Analyze patterns (problems, industries, Q2 costs)
- **Quarterly**: Optimize framework based on data

### Team Collaboration:

- Share winning Q5 answers in team meetings
- Highlight best Q4 consequences for learning
- Track which industries have highest close rates
- Document objections and how they were overcome

---

*CRM Templates Version 1.0*
*Last Updated: November 26, 2025*
*Questions? Contact: [Team Lead]*
