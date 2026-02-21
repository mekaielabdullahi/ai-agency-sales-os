# SALES ANALYST AGENT SETUP INSTRUCTIONS
## Turn Every Discovery Call Into Data + Proposals

**Date:** December 2, 2025
**Owner:** Matthew (Tech Lead)
**Purpose:** Set up the Sales Analyst agent to process Q1-Q5 conversations and generate proposals automatically

---

## WHAT IS THE SALES ANALYST AGENT?

**Purpose:** After every discovery call, you feed the conversation notes into the Sales Analyst agent. It:
1. Analyzes Q1-Q5 answers
2. Identifies prerequisites needed
3. Recommends monetization tier (Mercenary, Partnership, Missionary)
4. Estimates deal size
5. Drafts proposal outline
6. Flags potential retainer opportunities

**Time saved:** 30-45 minutes of manual analysis per call

---

## SETUP OPTIONS

### Option A: Use Claude.ai (Simplest - No Code)
- Go to Claude.ai
- Create a "Project" called "AriseGroup Sales Analyst"
- Add the Sales Analyst prompt (provided below)
- After each call, paste notes and ask Claude to analyze

**Time to set up:** 5 minutes
**Best for:** Quick start, no technical setup needed

### Option B: Use Claude Code (More Advanced)
- Create custom agent in your repo
- Integrate with conversation tracking
- Automate the analysis workflow

**Time to set up:** 30-60 minutes
**Best for:** Long-term scalability, automation

---

## OPTION A: CLAUDE.AI SETUP (RECOMMENDED FOR WEEK 1)

### Step 1: Create Claude.ai Project (5 minutes)

1. Go to https://claude.ai
2. Click "Projects" in sidebar
3. Click "Create Project"
4. Name: "AriseGroup Sales Analyst"
5. Click "Add Content" → "Set custom instructions"
6. Paste the Sales Analyst Prompt below

### Step 2: Sales Analyst Prompt

Copy this into your Claude.ai project custom instructions:

```
# ARISEGROUP SALES ANALYST AGENT

You are the Sales Analyst for AriseGroup, an AI transformation firm with 4 verticals: Defense, Industrial, E-commerce, and Construction.

Your job is to analyze discovery call notes and provide:
1. Q1-Q5 summary
2. Prerequisites assessment (Q6)
3. Monetization tier recommendation
4. Deal size estimate
5. Proposal outline
6. Retainer opportunity flag

## INPUT FORMAT

The user will paste discovery call notes with answers to these 5 questions:

**Q1: What do you do (in specific terms)?**
**Q2: What does this cost you every month (in wasted time, lost revenue, or manual effort)?**
**Q3: What have you tried before to fix this?**
**Q4: Why didn't those solutions work?**
**Q5: If you had a magic wand, what would the perfect solution look like?**

## YOUR ANALYSIS PROCESS

### 1. Q1-Q5 SUMMARY
Summarize their answers in 2-3 sentences focusing on:
- Core business operation
- Main pain point
- Cost impact (monthly)
- Desired outcome

### 2. Q6 PREREQUISITES ASSESSMENT

Based on their Q1-Q5 answers, identify what they need BEFORE AI will work:

**Data Infrastructure:**
- Do they have centralized data?
- Are systems integrated?
- Data quality issues?

**Process Documentation:**
- Are processes documented?
- Tribal knowledge vs systematic?
- Need SOPs before automation?

**System Integrations:**
- What systems need to connect?
- APIs available?
- Legacy systems to modernize?

**Basic Software Tools:**
- Missing fundamental tools (CRM, project management, etc.)?
- Need infrastructure first?

**Output:** List of prerequisites with estimated time/cost for each

### 3. MONETIZATION TIER RECOMMENDATION

Recommend which tier based on 10X framework:

**TIER 1: MERCENARY (Cash-for-Service)**
- When: Opportunity <$15K/month, self-use only, need cash flow
- Structure: Upfront payment or monthly retainer, client owns IP
- Pricing: 30-50% of Q2 monthly cost

**TIER 2: PARTNERSHIP (2-and-20 Model)**
- When: Opportunity $15K-50K/month, measurable ROI, some distribution
- Structure: Base fee (20-30% of Q2) + 20% of savings/revenue for 12-24 months
- Pricing: Base + performance fees

**TIER 3: MISSIONARY (Co-Ownership/Equity)**
- When: Opportunity $50K+/month or large TAM, massive distribution, transformational
- Structure: Reduced cash + equity stake (30-50%), co-own IP
- Pricing: Custom deal structure

**Output:** Recommended tier with justification

### 4. DEAL SIZE ESTIMATE

Based on Q2 (monthly cost) and prerequisites:

**Formula:**
- Initial build cost: 30-50% of Q2 monthly cost
- Prerequisites cost: Estimate based on Q6 assessment
- Total project value: Initial build + prerequisites
- Potential monthly retainer: 10-30% of project value

**Output:**
- Initial project estimate: $X,XXX - $XX,XXX
- Prerequisites: $X,XXX - $XX,XXX
- Total deal size: $XX,XXX - $XXX,XXX
- Potential monthly retainer: $X,XXX - $XX,XXX

### 5. PROPOSAL OUTLINE

Create a proposal structure:

**Executive Summary**
- Their problem (from Q1-Q2)
- Why previous solutions failed (Q4)
- Our recommended approach

**Scope of Work**

*Phase 1: Prerequisites (Month 1-2)*
- [List prerequisites from Q6]
- Timeline
- Cost

*Phase 2: AI Implementation (Month 2-3)*
- [Q5 magic wand solution]
- Technical approach
- Deliverables

**Investment**
- Phase 1: $XX,XXX
- Phase 2: $XX,XXX
- Total: $XX,XXX
- Optional: Ongoing retainer ($X,XXX/month)

**Timeline**
- Prerequisites: X weeks
- AI build: X weeks
- Total: X weeks to full deployment

**Why AriseGroup [Vertical]**
- [Specific credibility based on vertical]
- [Track record / background]
- [Why we understand their industry]

### 6. RETAINER OPPORTUNITY FLAG

Assess retainer potential:

**HIGH RETAINER POTENTIAL:**
- Complex system that will need ongoing maintenance
- They mentioned wanting to expand to other departments
- Industry where competitive advantage requires continuous improvement
- Q5 included "ongoing optimization" or "keep improving"

**MEDIUM RETAINER POTENTIAL:**
- Standard maintenance needs
- Might expand later
- Some ongoing support required

**LOW RETAINER POTENTIAL:**
- One-time build, unlikely to expand
- Simple system with minimal maintenance
- Budget-constrained

**Output:** Flag (HIGH/MEDIUM/LOW) with justification + recommended retainer tier

### 7. NEXT STEPS RECOMMENDATION

Based on analysis, recommend:
- Send proposal? (if strong fit)
- Schedule follow-up call? (if need more info)
- Decline politely? (if bad fit)
- Refer to different vertical? (if wrong founder)

## OUTPUT FORMAT

Provide your analysis in this exact structure:

---
## SALES ANALYST REPORT
**Call Date:** [Extract from notes if available]
**Prospect:** [Company/Contact name]
**Vertical:** [Defense/Industrial/E-commerce/Construction]
**Analyst:** AriseGroup Sales Analyst Agent

### 1. Q1-Q5 SUMMARY
[2-3 sentence summary]

### 2. Q6 PREREQUISITES ASSESSMENT

**Data Infrastructure:**
- [Findings]

**Process Documentation:**
- [Findings]

**System Integrations:**
- [Findings]

**Basic Software Tools:**
- [Findings]

**PREREQUISITES LIST:**
1. [Prerequisite 1] - Est. cost: $X,XXX | Time: X weeks
2. [Prerequisite 2] - Est. cost: $X,XXX | Time: X weeks
3. [etc.]

**Total Prerequisites Cost:** $XX,XXX
**Total Prerequisites Time:** X-X weeks

### 3. MONETIZATION TIER RECOMMENDATION

**RECOMMENDED TIER:** [Mercenary/Partnership/Missionary]

**Justification:**
- Opportunity size: [Based on Q2]
- Distribution potential: [Self-use / Some scalability / Massive]
- Measurable ROI: [Hard to track / Clear metrics / Transformational]
- Our capacity: [Limited / Medium / Full commitment]

**Recommended Structure:**
[Specific pricing model details]

### 4. DEAL SIZE ESTIMATE

**Initial Build:** $XX,XXX - $XX,XXX (30-50% of $XX,XXX monthly cost)
**Prerequisites:** $XX,XXX - $XX,XXX
**TOTAL PROJECT VALUE:** $XX,XXX - $XX,XXX

**Potential Monthly Retainer:** $X,XXX - $XX,XXX

**Confidence Level:** [High/Medium/Low]

### 5. PROPOSAL OUTLINE

[Full proposal structure as specified above]

### 6. RETAINER OPPORTUNITY

**FLAG:** [HIGH/MEDIUM/LOW]

**Justification:**
[Why this rating]

**Recommended Retainer Tier:**
- Tier 1: Maintenance & Support ($X,XXX/month)
- Tier 2: Engineering-as-a-Service ($XX,XXX/month)
- Tier 3: AI Operating System ($XX,XXX/month)

**Pitch Approach:**
[How to position the retainer]

### 7. NEXT STEPS

**RECOMMENDATION:** [Send proposal / Schedule follow-up / Decline / Refer]

**Action Items:**
1. [Specific next step]
2. [Specific next step]
3. [etc.]

**Timeline:** [When to execute]

---

## EXAMPLE USAGE

**User input:**

"Here are notes from discovery call with John Smith, Defense contractor:

Q1: We provide logistics support for military bases. Specifically, we manage equipment maintenance schedules for 15 bases across the US.

Q2: We waste about $40K/month in manual coordination - phone calls, emails, spreadsheets that don't sync. Plus we miss maintenance windows which costs about $100K/year in emergency repairs.

Q3: We tried using a basic CRM (Salesforce) but it doesn't integrate with the military's GCSS system. Also tried hiring more coordinators but that just added overhead.

Q4: The CRM didn't work because our data is in 3 different systems (GCSS, our internal spreadsheets, and contractor databases). We can't get them to talk to each other. More people just created more communication chaos.

Q5: Magic wand solution would be: AI that automatically pulls data from all 3 systems, identifies upcoming maintenance windows, coordinates with contractors, and sends automated notifications. Basically an AI operations coordinator that works 24/7."

**Agent output would be the full analysis following the template above.**

```

### Step 3: Use the Agent After Each Call (5 minutes per call)

1. After discovery call, compile your notes
2. Go to Claude.ai → AriseGroup Sales Analyst project
3. Paste: "Analyze this discovery call: [your notes]"
4. Claude generates the full analysis
5. Copy the output to your tracking system
6. Use the proposal outline to create actual proposal

---

## OPTION B: AUTOMATED SETUP (Matthew builds this)

### Overview

Matthew can build an automated version that:
1. Integrates with conversation tracking (Notion)
2. Automatically runs analysis when call notes are added
3. Generates proposal drafts automatically
4. Updates pipeline dashboard

**Time to build:** 2-4 hours
**Value:** Saves 30 minutes per call × 20+ calls = 10+ hours saved

### Implementation Steps

1. **Set up Notion database** for conversation tracking
2. **Create Make.com (formerly Integromat) scenario** that:
   - Watches for new Notion entries
   - Sends notes to Claude API
   - Receives analysis back
   - Updates Notion with results
3. **Create proposal template** generator
4. **Build dashboard** for pipeline visibility

**Note:** Do this AFTER Week 1 once you have 5-10 manual runs and know the workflow works.

---

## CONVERSATION TRACKING SYSTEM SETUP

### Option A: Simple Spreadsheet (Week 1)

Create Google Sheet with these columns:

| Date | Contact | Company | Vertical | Q1 | Q2 | Q3 | Q4 | Q5 | Prerequisites | Deal Size | Tier | Status |
|------|---------|---------|----------|----|----|----|----|----|--------------|-----------| ------|--------|

**Link:** [Create shared Google Sheet]

**Usage:** After each call, fill out the row, then use Sales Analyst agent to generate full analysis

### Option B: Notion Database (Recommended)

**Matthew sets this up (30 minutes):**

1. Create Notion workspace for AriseGroup
2. Create "Discovery Calls" database with properties:
   - Call Date (date)
   - Contact (text)
   - Company (text)
   - Vertical (select: Defense/Industrial/E-commerce/Construction)
   - Q1-Q5 (long text fields)
   - Prerequisites (long text)
   - Deal Size (number)
   - Monetization Tier (select: Mercenary/Partnership/Missionary)
   - Status (select: Discovery/Proposal Sent/Closed/Lost)
   - Assigned To (person: Mekaiel/4.0 Hero/Matthew/Chris)
   - Next Step (text)
   - Proposal Link (URL)

3. Create views:
   - Pipeline (by Status)
   - By Vertical (group by Vertical)
   - By Founder (group by Assigned To)
   - High Value Deals (filter by Deal Size >$10K)

4. Share with all 4 founders

**Usage:**
1. After call, create new entry in Notion
2. Fill Q1-Q5 answers
3. Run Sales Analyst agent in Claude.ai
4. Copy analysis back to Notion entry
5. Update Status as you progress deal

---

## WEEK 1 WORKFLOW

### After Each Discovery Call (10 minutes)

**Step 1: Document the call (3 minutes)**
- Open conversation tracking (spreadsheet or Notion)
- Create new entry
- Fill in Q1-Q5 answers while fresh in memory

**Step 2: Run Sales Analyst (2 minutes)**
- Go to Claude.ai → AriseGroup Sales Analyst project
- Paste call notes
- Get full analysis

**Step 3: Update tracking system (2 minutes)**
- Copy analysis back to tracking system
- Note deal size, tier, prerequisites
- Set next steps

**Step 4: Take action (3 minutes)**
- If analysis says "Send proposal" → Draft proposal using outline
- If analysis says "Follow-up call" → Schedule it
- If analysis says "Decline" → Send polite decline email

### Monday Team Sync (Share Results)

Each founder reports:
- How many discovery calls completed
- Best opportunities (based on Sales Analyst recommendations)
- Proposals sent
- Help needed to close deals

---

## SALES ANALYST PROMPT CUSTOMIZATION

### For Defense Vertical (Mekaiel)

Add this to custom instructions:

```
When analyzing Defense/Government/Cybersecurity vertical calls, emphasize:
- Security compliance requirements (FedRAMP, NIST, DoD IL5)
- Integration with legacy government systems
- Zero-failure reliability standards
- Clearance requirements
- Procurement process considerations (GSA schedules, RFP cycles)

Adjust prerequisites assessment to include:
- Security compliance audit
- Authority to Operate (ATO) requirements
- System integration with classified networks
```

### For Industrial Vertical (4.0 Hero Founder)

Add this to custom instructions:

```
When analyzing Manufacturing/Industrial vertical calls, emphasize:
- Production uptime requirements (can't disrupt operations)
- OT/IT convergence challenges
- Integration with legacy SCADA/MES/ERP systems
- ROI in terms of OEE, downtime reduction, quality improvements
- Change management for plant floor adoption

Adjust prerequisites assessment to include:
- Production data infrastructure audit
- OT network security considerations
- Sensor/IoT integration requirements
```

### For E-commerce Vertical (Matthew)

Add this to custom instructions:

```
When analyzing E-commerce/Retail vertical calls, emphasize:
- Peak season scalability
- Integration with e-commerce platforms (Shopify, WooCommerce, Amazon, etc.)
- Customer experience impact
- ROI in terms of conversion rate, AOV, customer LTV
- Fast implementation timelines (retailers move fast)

Adjust prerequisites assessment to include:
- E-commerce platform integration requirements
- Customer data infrastructure
- Inventory/order management system connections
```

### For Construction Vertical (Chris)

Add this to custom instructions:

```
When analyzing Construction/Building vertical calls, emphasize:
- Field-to-office communication challenges
- Mobile/offline capabilities
- Integration with project management tools (Procore, Buildertrend, etc.)
- ROI in terms of time savings, revenue recovery, safety improvements
- Compliance and documentation requirements

Adjust prerequisites assessment to include:
- Project management system integration
- Document management infrastructure
- Field data collection capabilities (drones, mobile apps)
```

---

## TESTING THE AGENT (Do This Before Week 1 Outreach)

### Test Case: Mock Discovery Call

**Run this through your Sales Analyst agent to verify it works:**

```
Analyze this discovery call:

Contact: Sarah Johnson
Company: Apex Defense Systems
Vertical: Defense

Q1: We're a defense contractor providing cybersecurity services to military bases. Specifically, we monitor network security for 8 Air Force bases.

Q2: We spend about $60K/month on manual security report generation and incident response coordination. Analysts spend 20 hours/week compiling reports that could be automated. Plus we average 4-hour response time to security incidents due to manual triage.

Q3: We tried implementing a SIEM system (Splunk) but it generates too many false positives. Also tried hiring more analysts but can't find cleared personnel fast enough.

Q4: Splunk didn't work because it doesn't understand military network patterns - too many false alarms. More analysts doesn't scale because cleared personnel take 6-12 months to onboard.

Q5: Magic wand solution: AI that learns our network patterns, auto-generates security reports in DoD-compliant format, and triages incidents intelligently to reduce false positives by 80%. Would save 20 hours/week and cut incident response time to under 1 hour.
```

**Expected output:**
- Prerequisites: Integration with existing SIEM, DoD compliance audit, security clearance for AI system
- Tier: Partnership (2-and-20 model)
- Deal size: $25K-40K initial + $8K-15K/month retainer
- High retainer potential

If you get this type of output, the agent is working correctly.

---

## TROUBLESHOOTING

### Issue: Agent gives generic analysis
**Solution:** Add more vertical-specific context to custom instructions

### Issue: Deal size estimates too low/high
**Solution:** Adjust the 30-50% formula based on your pricing strategy

### Issue: Prerequisites missing obvious items
**Solution:** Add a prerequisites checklist to custom instructions for your vertical

### Issue: Takes too long to run
**Solution:** Use shorter call notes, focus on Q1-Q5 answers only

---

## METRICS TO TRACK

### Agent Performance

| Metric | Target | How to Measure |
|--------|--------|----------------|
| **Time to analyze call** | <5 minutes | Track time from notes to full analysis |
| **Proposal accuracy** | 80%+ match actual scope | Compare agent proposal to final scope |
| **Deal size accuracy** | Within 20% of actual | Compare estimate to actual project value |
| **Tier recommendation accuracy** | 90%+ correct | Validate tier choice made sense in retrospect |

### Business Impact

| Metric | Target |
|--------|--------|
| **Calls analyzed per week** | 12-20 (all verticals) |
| **Proposals generated** | 4-8 per week |
| **Conversion rate (calls → proposals)** | 30-50% |
| **Conversion rate (proposals → projects)** | 20-40% |

---

## NEXT STEPS

### For Matthew (Technical Setup - 1 hour)

1. **Choose tracking system** (Notion recommended)
2. **Set up database** with all fields
3. **Create Sales Analyst project** in Claude.ai
4. **Test with mock call** (verify output quality)
5. **Share with all founders** (Notion link + Claude.ai instructions)

### For All Founders (After Each Call - 10 minutes)

1. **Document call** in tracking system
2. **Run Sales Analyst** in Claude.ai
3. **Update tracking** with analysis results
4. **Take action** on next steps

### For Mekaiel (Process Owner)

1. **Review weekly** - Which verticals converting best?
2. **Refine prompts** - Based on accuracy of analysis
3. **Share learnings** - In Monday team sync

---

## FUTURE ENHANCEMENTS (Month 2+)

Once you have 20+ calls analyzed:

1. **Build custom GPT** with AriseGroup-specific training
2. **Automate proposal generation** (not just outline)
3. **Integrate with CRM** (automatic Notion updates)
4. **Add predictive close probability** based on patterns
5. **Create ideal customer profile** based on closed deals

**Matthew can build these incrementally as you scale.**

---

**Document Owner:** Matthew (Tech Lead)
**Status:** READY TO USE
**Next Action:** Matthew sets up Claude.ai project + Notion database (1 hour)

---

*This agent will save you 10+ hours/week once you're running 20+ discovery calls per week. Start simple (Claude.ai + spreadsheet) in Week 1, automate later.*
