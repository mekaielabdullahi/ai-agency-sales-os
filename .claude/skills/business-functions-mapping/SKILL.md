---
name: business-functions-mapping
description: Map business functions, workflows, and operations to identify structure, dependencies, and AI opportunities. Use when analyzing organizations, creating operational assessments, identifying automation opportunities, or conducting AI Readiness Audits.
allowed-tools: Read, Write, Grep, Glob, Edit
---

# Business Functions Mapping Skill

## Purpose
Systematic framework for mapping, analyzing, and documenting business functions across any organization to identify operational structure, inefficiencies, dependencies, and AI/automation opportunities.

## When to Use This Skill
- Conducting AI Readiness Audits
- Analyzing client operations
- Identifying automation opportunities
- Understanding organizational structure
- Discovering process inefficiencies
- Mapping workflows and dependencies
- Creating operational documentation
- Prioritizing AI adoption initiatives

---

## 🎯 WHAT IS BUSINESS FUNCTIONS MAPPING?

### Definition
**Business Functions Mapping** is the systematic process of identifying, categorizing, documenting, and analyzing all operational activities within an organization to understand:
- **What** the business does (core functions)
- **How** it operates (processes and workflows)
- **Who** does what (roles and responsibilities)
- **Where** inefficiencies exist (friction points)
- **Which** functions are candidates for AI/automation

### Why It Matters

**For AI Adoption**:
- Identifies highest-impact automation opportunities
- Maps dependencies (what affects what)
- Reveals hidden inefficiencies
- Prioritizes implementation roadmap
- Quantifies potential ROI

**For Business Operations**:
- Creates clarity on who does what
- Documents tribal knowledge
- Identifies redundancies
- Reveals bottlenecks
- Enables systematic improvement

**For Strategic Planning**:
- Aligns operations with business goals
- Identifies gaps in capabilities
- Informs resource allocation
- Guides technology investments

---

## 📊 COMPREHENSIVE FRAMEWORK

### The 4-Layer Mapping Model

**Layer 1: Business Functions** (WHAT)
- High-level categories of activity
- Examples: Sales, Marketing, Operations, Finance

**Layer 2: Sub-Functions** (DETAILED WHAT)
- Specific areas within each function
- Examples: Lead Generation (under Sales), Content Creation (under Marketing)

**Layer 3: Processes** (HOW)
- Step-by-step workflows
- Examples: "How we onboard a client" or "How we process an invoice"

**Layer 4: Tasks** (GRANULAR HOW)
- Individual activities within processes
- Examples: "Send welcome email," "Create project folder," "Update CRM"

### Mapping Process

#### Step 1: Identify Core Business Functions (60 min)

**Questions to Ask**:
1. "What are the major categories of work happening in your organization?"
2. "What departments or teams exist?"
3. "What needs to happen for the business to operate?"
4. "What customer-facing activities occur?"
5. "What internal/support activities are required?"

**Standard Function Categories** (customize per business):

1. **Revenue Generation**
   - Sales
   - Marketing
   - Business Development
   - Client Success/Account Management

2. **Delivery/Operations**
   - Product Development
   - Service Delivery
   - Project Management
   - Quality Assurance
   - Customer Support

3. **Enabling Functions**
   - Finance & Accounting
   - Human Resources
   - IT/Technology
   - Legal/Compliance
   - Administration

4. **Strategic Functions**
   - Executive Leadership
   - Strategy & Planning
   - Product Management
   - Research & Development

**Output**: List of 5-12 core business functions

#### Step 2: Map Sub-Functions (45 min per function)

For each core function identified, break down into sub-functions.

**Example: Sales Function**
- Lead Generation
- Lead Qualification
- Sales Outreach
- Discovery/Needs Analysis
- Proposal Creation
- Negotiation
- Contract Execution
- Handoff to Delivery

**Example: Marketing Function**
- Content Creation
- Social Media Management
- Email Marketing
- SEO/SEM
- Brand Management
- Event Management
- Marketing Analytics

**Template**:
```
## [FUNCTION NAME]

### Purpose
[What this function accomplishes for the business]

### Sub-Functions
1. [Sub-function 1]
   - Description: [What it does]
   - Frequency: [Daily/Weekly/Monthly/Quarterly]
   - Owner: [Role/person responsible]

2. [Sub-function 2]
   ...
```

**Output**: Detailed breakdown of each core function into 3-8 sub-functions

#### Step 3: Document Key Processes (30-60 min per process)

Select 5-10 most critical processes to map in detail.

**Prioritization Criteria**:
- High frequency (happens often)
- High impact (affects revenue or customer experience)
- High pain (currently inefficient or problematic)
- High potential (clear AI/automation opportunity)

**Process Mapping Template**:
```
## Process: [Process Name]

### Overview
- **Function**: [Which function this belongs to]
- **Purpose**: [Why this process exists]
- **Frequency**: [How often it runs]
- **Owner**: [Who's responsible]
- **Stakeholders**: [Who's involved]

### Current State
**Input**: [What triggers this process]
**Output**: [What it produces]

**Steps**:
1. [Step 1]
   - Who: [Role]
   - Tool: [Technology/system used]
   - Time: [Estimated time]
   - Pain Points: [Inefficiencies, manual work, errors]

2. [Step 2]
   ...

### Metrics
- **Cycle Time**: [How long start to finish]
- **Error Rate**: [% of time it fails/needs rework]
- **Volume**: [How many times per week/month]
- **Cost**: [Estimated labor cost]

### Dependencies
- **Upstream**: [What must happen before this]
- **Downstream**: [What depends on this]
- **Systems**: [Technology/tools required]

### Pain Points
1. [Pain point 1]
   - Impact: [How it affects business]
   - Frequency: [How often it occurs]
2. [Pain point 2]
   ...

### AI/Automation Opportunities
1. [Opportunity 1]
   - Type: [Automation/AI-assistance/AI-augmentation]
   - Impact: [Time/cost/quality improvement]
   - Complexity: [Low/Medium/High]
   - Priority: [High/Medium/Low]
2. [Opportunity 2]
   ...
```

**Output**: Detailed process maps for 5-10 critical processes

#### Step 4: Identify Cross-Functional Dependencies (30 min)

**Map how functions interact**:
- What data flows between functions?
- What handoffs occur?
- Where do bottlenecks happen?
- What are the communication patterns?

**Dependency Matrix Template**:
```
| Function A → Function B | Type | Frequency | Pain Point |
|-------------------------|------|-----------|------------|
| Sales → Delivery | Client handoff | Per new client | Information loss |
| Marketing → Sales | Qualified leads | Daily | Lead quality inconsistent |
| Delivery → Finance | Completed work | Weekly | Billing delays |
```

**Output**: Clear view of inter-functional dependencies

#### Step 5: Prioritize AI Opportunities (45 min)

**Scoring Framework**:

Each opportunity rated on:
- **Impact** (1-10): How much time/cost/quality improvement
- **Feasibility** (1-10): How easy to implement (technical + organizational)
- **ROI** (1-10): Expected return on investment
- **Priority Score**: (Impact × 2 + Feasibility + ROI) / 4

**Categorization**:
- **Quick Wins** (30-90 days): High feasibility, medium-high impact
- **Strategic Initiatives** (3-6 months): High impact, medium feasibility
- **Long-Term Transformation** (6-12 months): Very high impact, lower feasibility
- **Deferred** (Future): Lower priority, needs more analysis

**Output**: Prioritized roadmap of AI/automation opportunities

---

## 🏢 STANDARD BUSINESS FUNCTION LIBRARY

### 1. SALES FUNCTION

**Core Purpose**: Generate revenue through customer acquisition

**Sub-Functions**:
1. **Lead Generation**
   - Outbound prospecting
   - Inbound lead capture
   - Networking/referrals
   - Partnership development

2. **Lead Qualification**
   - Needs assessment
   - Budget verification
   - Decision-maker identification
   - Fit evaluation

3. **Sales Process**
   - Discovery calls
   - Needs analysis
   - Solution presentation
   - Proposal creation
   - Negotiation
   - Contract execution

4. **Pipeline Management**
   - CRM maintenance
   - Forecasting
   - Deal progression tracking
   - Sales reporting

5. **Account Management**
   - Relationship maintenance
   - Upsell/cross-sell
   - Renewal management
   - Customer advocacy

**Common Pain Points**:
- Manual CRM data entry
- Inconsistent follow-up
- Lost leads due to slow response
- Proposal creation time-intensive
- Lack of pipeline visibility
- Handoff gaps to delivery team

**AI Opportunities**:
- Automated lead scoring
- CRM auto-population from emails
- AI-assisted proposal generation
- Intelligent follow-up reminders
- Sales coaching via AI analysis of calls
- Predictive deal closure probability

---

### 2. MARKETING FUNCTION

**Core Purpose**: Generate demand and build brand awareness

**Sub-Functions**:
1. **Content Creation**
   - Blog writing
   - Social media posts
   - Email campaigns
   - Video/multimedia
   - Case studies
   - Whitepapers/ebooks

2. **Content Distribution**
   - Social media management
   - Email marketing
   - SEO optimization
   - Paid advertising
   - PR/media relations

3. **Lead Nurturing**
   - Email sequences
   - Content offers
   - Webinars/events
   - Marketing automation

4. **Analytics & Reporting**
   - Campaign performance tracking
   - Attribution modeling
   - ROI measurement
   - Audience insights

5. **Brand Management**
   - Brand guidelines
   - Messaging consistency
   - Visual identity
   - Reputation management

**Common Pain Points**:
- Content creation bottleneck
- Inconsistent posting schedule
- Difficult to measure ROI
- Manual campaign setup
- Data silos across platforms
- Personalization at scale challenges

**AI Opportunities**:
- AI-assisted content creation
- Automated social media scheduling
- Personalized email campaigns
- Predictive audience segmentation
- Automated A/B testing
- Real-time campaign optimization
- Sentiment analysis and brand monitoring

---

### 3. OPERATIONS/DELIVERY FUNCTION

**Core Purpose**: Deliver products/services to customers

**Sub-Functions**:
1. **Client Onboarding**
   - Kickoff meetings
   - Requirements gathering
   - Access provisioning
   - Training delivery

2. **Project Management**
   - Scope definition
   - Resource allocation
   - Timeline management
   - Status reporting
   - Risk management

3. **Service Delivery**
   - Task execution
   - Quality control
   - Client communication
   - Issue resolution

4. **Documentation**
   - Process documentation
   - Knowledge base maintenance
   - Training materials
   - Standard operating procedures

5. **Client Offboarding**
   - Final deliverables
   - Handoff procedures
   - Feedback collection
   - Knowledge transfer

**Common Pain Points**:
- Onboarding takes too long
- Project status visibility gaps
- Resource allocation inefficiencies
- Tribal knowledge (not documented)
- Repetitive task execution
- Client communication inconsistencies

**AI Opportunities**:
- Automated onboarding workflows
- AI project status summaries
- Intelligent resource allocation
- Auto-documentation from meetings
- Task automation (repetitive work)
- Predictive project risk analysis
- Smart scheduling optimization

---

### 4. CUSTOMER SUPPORT FUNCTION

**Core Purpose**: Resolve customer issues and maintain satisfaction

**Sub-Functions**:
1. **Ticket Management**
   - Ticket creation/intake
   - Triage and routing
   - Priority assignment
   - SLA tracking

2. **Issue Resolution**
   - Troubleshooting
   - Solution implementation
   - Escalation management
   - Follow-up

3. **Knowledge Management**
   - FAQ creation/maintenance
   - Knowledge base articles
   - Internal documentation
   - Best practice sharing

4. **Customer Communication**
   - Email/chat/phone support
   - Proactive outreach
   - Status updates
   - Satisfaction surveys

**Common Pain Points**:
- High ticket volume
- Repetitive questions
- Long resolution times
- Knowledge scattered across systems
- Inconsistent responses
- Escalation delays

**AI Opportunities**:
- AI chatbots for common questions
- Automated ticket categorization
- Intelligent routing to right person
- Suggested solutions from knowledge base
- Auto-drafted responses
- Sentiment analysis for escalation
- Predictive issue identification

---

### 5. FINANCE & ACCOUNTING FUNCTION

**Core Purpose**: Manage financial operations and reporting

**Sub-Functions**:
1. **Accounts Receivable**
   - Invoicing
   - Payment processing
   - Collections
   - Revenue recognition

2. **Accounts Payable**
   - Bill processing
   - Vendor payments
   - Expense management
   - Purchase order management

3. **Financial Reporting**
   - Monthly/quarterly closes
   - Financial statements
   - Budget vs. actual analysis
   - Cash flow forecasting

4. **Payroll & Benefits**
   - Payroll processing
   - Benefits administration
   - Tax withholding
   - Compliance reporting

5. **Financial Planning & Analysis**
   - Budgeting
   - Forecasting
   - Scenario modeling
   - KPI tracking

**Common Pain Points**:
- Manual data entry from invoices/receipts
- Time-consuming reconciliation
- Late payments (AR)
- Expense approval delays
- Report generation time-intensive
- Forecasting inaccuracy

**AI Opportunities**:
- Automated invoice processing (OCR + AI)
- Smart expense categorization
- Automated reconciliation
- Predictive cash flow modeling
- Anomaly detection (fraud/errors)
- Intelligent budget variance analysis
- Automated financial report generation

---

### 6. HUMAN RESOURCES FUNCTION

**Core Purpose**: Recruit, develop, and retain talent

**Sub-Functions**:
1. **Recruiting & Hiring**
   - Job posting
   - Resume screening
   - Interview scheduling
   - Candidate evaluation
   - Offer management
   - Onboarding

2. **Employee Development**
   - Training programs
   - Performance management
   - Career development
   - Succession planning

3. **Compensation & Benefits**
   - Salary administration
   - Benefits management
   - Equity/bonus programs
   - Compliance

4. **Employee Relations**
   - Engagement initiatives
   - Conflict resolution
   - Policy enforcement
   - Offboarding

**Common Pain Points**:
- Resume screening time-intensive
- Interview scheduling coordination
- Inconsistent candidate evaluation
- Manual onboarding workflows
- Performance review admin burden
- Employee engagement data scattered

**AI Opportunities**:
- AI resume screening and ranking
- Automated interview scheduling
- Candidate assessment AI
- Personalized onboarding workflows
- Performance data analysis
- Sentiment analysis from employee feedback
- Predictive attrition modeling

---

### 7. IT/TECHNOLOGY FUNCTION

**Core Purpose**: Enable business through technology

**Sub-Functions**:
1. **Infrastructure Management**
   - Server/cloud management
   - Network administration
   - Security management
   - Backup/disaster recovery

2. **Application Management**
   - Software selection/implementation
   - System integration
   - User access management
   - Application support

3. **Help Desk**
   - User support tickets
   - Troubleshooting
   - Training
   - Documentation

4. **Development/Innovation**
   - Custom development
   - API integrations
   - Automation projects
   - Technology evaluation

**Common Pain Points**:
- Repetitive help desk tickets
- Manual provisioning/de-provisioning
- System monitoring reactive (not proactive)
- Integration complexity
- Documentation outdated
- Security vulnerability tracking manual

**AI Opportunities**:
- AI help desk chatbot
- Automated user provisioning
- Predictive system monitoring
- Intelligent incident routing
- Auto-generated documentation
- Security threat detection AI
- Code assistance for developers

---

### 8. EXECUTIVE/STRATEGY FUNCTION

**Core Purpose**: Set direction and ensure alignment

**Sub-Functions**:
1. **Strategic Planning**
   - Vision/mission definition
   - Goal setting (OBG/OKRs)
   - Market analysis
   - Competitive intelligence

2. **Decision Making**
   - Resource allocation
   - Priority setting
   - Risk assessment
   - Investment decisions

3. **Performance Management**
   - KPI definition and tracking
   - Business reviews
   - Accountability systems
   - Course correction

4. **Stakeholder Communication**
   - Board reporting
   - Investor relations
   - Company-wide communications
   - External messaging

**Common Pain Points**:
- Data collection for decisions time-intensive
- Difficult to track strategic initiatives
- KPI reporting manual
- Information overload
- Scattered data across systems
- Insight generation requires heavy analysis

**AI Opportunities**:
- Automated KPI dashboards
- AI-powered business intelligence
- Predictive scenario modeling
- Market intelligence automation
- Strategic initiative tracking AI
- Executive briefing auto-generation
- Anomaly detection in business metrics

---

## 🔍 DISCOVERY QUESTION FRAMEWORKS

### Initial Discovery Questions (Start Here)

**High-Level Mapping**:
1. "Walk me through a typical day/week. What are the main categories of work?"
2. "What are your biggest operational challenges right now?"
3. "Where does most of your time go? Your team's time?"
4. "What processes feel inefficient or frustrating?"
5. "What would you automate first if you could wave a magic wand?"

**Function Identification**:
1. "What needs to happen for you to acquire a customer?"
2. "Once you have a customer, what's the delivery process?"
3. "What internal/support functions keep the business running?"
4. "How do you measure success? What gets tracked?"

### Deep-Dive Discovery Questions (Per Function)

**For Each Function**:
1. "What are the major activities within [function]?"
2. "Who's responsible for [function]? How many people?"
3. "What tools/systems do you use for [function]?"
4. "What are the biggest pain points in [function]?"
5. "How much time does [function] consume per week?"
6. "What would 'great' look like for [function]?"

**Process-Level Questions**:
1. "Walk me through [specific process] step-by-step."
2. "What triggers this process? Where does it start?"
3. "What's the output? Where does it end?"
4. "Who's involved at each step?"
5. "Where does this process break down or slow down?"
6. "How long does this typically take?"
7. "What percentage of time does it need rework?"
8. "What data do you need? Where does it come from?"

### AI Opportunity Questions

**Identifying Automation Potential**:
1. "What tasks do you find yourself doing repeatedly?"
2. "What takes a lot of time but doesn't require deep thinking?"
3. "Where do errors happen most frequently?"
4. "What information is hard to find when you need it?"
5. "Where do handoffs between people/teams happen?"
6. "What reports or analyses take a long time to create?"
7. "Where do you wish you had more visibility?"

---

## 📋 TEMPLATES & OUTPUTS

### Template 1: Function Map Summary

```markdown
# Business Functions Map - [Company Name]

**Date**: [Date]
**Industry**: [Industry]
**Size**: [# Employees]
**Primary Business Model**: [Description]

## Executive Summary
[1-2 paragraph overview of business operations and key findings]

## Core Business Functions

### 1. [Function Name]
**Purpose**: [What it accomplishes]
**Sub-Functions**: [List]
**Team Size**: [# people]
**Key Pain Points**:
- [Pain 1]
- [Pain 2]
**AI Opportunities**: [High-level]

### 2. [Function Name]
...

## Key Findings
1. **Biggest Inefficiencies**: [Where the most pain exists]
2. **Highest-Impact Opportunities**: [Where AI can help most]
3. **Quick Wins**: [What can be done in 30-90 days]
4. **Strategic Initiatives**: [What requires 3-6 months]

## Recommended Roadmap
**Phase 1** (30 days): [Quick wins]
**Phase 2** (90 days): [Medium initiatives]
**Phase 3** (6 months): [Transformational projects]
```

### Template 2: Process Map Detail

```markdown
# Process Map: [Process Name]

## Overview
- **Function**: [Parent function]
- **Purpose**: [Why this exists]
- **Frequency**: [How often]
- **Owner**: [Responsible party]
- **Duration**: [Avg time to complete]

## Current State Workflow

### Step 1: [Step Name]
- **Who**: [Role]
- **What**: [Detailed description]
- **Tool**: [System/manual]
- **Time**: [Minutes/hours]
- **Pain Points**: [Issues]
- **Data Required**: [Inputs]
- **Output**: [What's produced]

### Step 2: [Step Name]
...

## Metrics
- **Volume**: [How many per week/month]
- **Cycle Time**: [Start to finish]
- **Error Rate**: [% requiring rework]
- **Labor Cost**: [Estimated $]

## Dependencies
- **Upstream**: [What must happen first]
- **Downstream**: [What depends on this]
- **Systems**: [Technology required]

## Pain Point Analysis

| Pain Point | Frequency | Impact | Root Cause |
|------------|-----------|--------|------------|
| [Issue 1] | [Often/Sometimes/Rarely] | [High/Med/Low] | [Why it happens] |
| [Issue 2] | ... | ... | ... |

## AI/Automation Opportunities

### Opportunity 1: [Name]
- **Type**: [Full automation / AI-assisted / AI-augmented]
- **Description**: [What would be automated]
- **Impact**: [Time/cost/quality improvement]
- **Feasibility**: [Low/Med/High]
- **Estimated Effort**: [Hours/days/weeks]
- **ROI**: [Expected return]
- **Priority**: [High/Med/Low]

### Opportunity 2: [Name]
...
```

### Template 3: AI Opportunity Prioritization Matrix

```markdown
# AI Opportunity Prioritization - [Company Name]

## Scoring Framework
- **Impact**: Time/cost/quality improvement (1-10)
- **Feasibility**: Technical + organizational ease (1-10)
- **ROI**: Expected return on investment (1-10)
- **Priority Score**: (Impact × 2 + Feasibility + ROI) / 4

## Opportunities Ranked

| Rank | Opportunity | Function | Impact | Feasibility | ROI | Priority Score | Category |
|------|------------|----------|--------|-------------|-----|----------------|----------|
| 1 | [Opp name] | [Function] | 9 | 8 | 9 | 8.75 | Quick Win |
| 2 | [Opp name] | [Function] | 10 | 6 | 8 | 8.5 | Strategic |
| 3 | ... | ... | ... | ... | ... | ... | ... |

## Implementation Roadmap

### Phase 1: Quick Wins (30-90 days)
**Target**: Low-hanging fruit with immediate impact

1. **[Opportunity Name]**
   - Function: [Function]
   - Impact: [Description]
   - Effort: [Estimated time]
   - Success Metric: [How to measure]

2. **[Opportunity Name]**
   ...

### Phase 2: Strategic Initiatives (3-6 months)
**Target**: Medium complexity, high impact

1. **[Opportunity Name]**
   ...

### Phase 3: Transformation (6-12 months)
**Target**: Complex, transformational impact

1. **[Opportunity Name]**
   ...

## Expected Cumulative Impact

**After Phase 1**:
- Time saved: [X hours/week]
- Cost reduction: [$X/month]
- Quality improvement: [Metric]

**After Phase 2**:
- Time saved: [X hours/week]
- Cost reduction: [$X/month]
- Quality improvement: [Metric]

**After Phase 3**:
- Time saved: [X hours/week]
- Cost reduction: [$X/month]
- Quality improvement: [Metric]

**Total ROI**: [Calculate]
```

---

## 🎯 INDUSTRY-SPECIFIC CONSIDERATIONS

### Professional Services (Consulting, Agency, etc.)

**Critical Functions**:
- Client acquisition (sales/BD)
- Project delivery
- Client communication
- Knowledge management
- Resource allocation

**Common Pain Points**:
- Utilization tracking manual
- Scope creep common
- Project status visibility gaps
- Time tracking inconsistent
- Knowledge silos

**High-Impact AI Opportunities**:
- Automated time tracking
- Project status AI summaries
- Knowledge base AI search
- Resource allocation optimization
- Scope monitoring and alerts

### SaaS/Technology Companies

**Critical Functions**:
- Product development
- Customer acquisition
- Customer success
- Product support
- Infrastructure management

**Common Pain Points**:
- Support ticket volume
- Feature prioritization unclear
- Onboarding drop-off
- Churn prediction needed
- Engineering productivity tracking

**High-Impact AI Opportunities**:
- AI support chatbot
- Feature usage analytics
- Predictive churn modeling
- Automated onboarding
- Code review automation

### E-commerce/Retail

**Critical Functions**:
- Inventory management
- Order fulfillment
- Customer service
- Marketing/acquisition
- Returns/logistics

**Common Pain Points**:
- Inventory forecasting inaccurate
- Customer inquiries repetitive
- Order tracking manual
- Personalization at scale hard
- Returns processing time-intensive

**High-Impact AI Opportunities**:
- Demand forecasting AI
- Customer service chatbot
- Personalized recommendations
- Automated order routing
- Returns categorization and routing

### Nonprofits

**Critical Functions**:
- Fundraising
- Donor management
- Program delivery
- Volunteer coordination
- Impact measurement

**Common Pain Points**:
- Donor data scattered
- Manual grant reporting
- Volunteer scheduling complex
- Impact tracking inconsistent
- Resource constraints (small team)

**High-Impact AI Opportunities**:
- Donor segmentation and outreach automation
- Grant report auto-generation
- Volunteer matching and scheduling
- Impact data aggregation
- Automated thank-you communications

### Manufacturing

**Critical Functions**:
- Production planning
- Quality control
- Inventory management
- Supply chain coordination
- Maintenance

**Common Pain Points**:
- Production scheduling complex
- Quality issues detected late
- Inventory imbalances
- Equipment downtime unexpected
- Supply chain visibility gaps

**High-Impact AI Opportunities**:
- Predictive maintenance
- Quality anomaly detection
- Demand forecasting
- Production optimization
- Supply chain risk monitoring

---

## 🔄 INTEGRATION WITH AI READINESS AUDITS

### How This Skill Supports Audits

**During Discovery Call** (Use this skill to):
1. Quickly map client's business functions
2. Identify pain points systematically
3. Ask targeted follow-up questions
4. Document operational structure

**After Discovery Call** (Use this skill to):
1. Create comprehensive function map
2. Analyze processes in detail
3. Identify AI opportunities
4. Prioritize recommendations
5. Build implementation roadmap

**In Audit Deliverable** (Include):
- Function map summary (1-2 pages)
- Key process maps (3-5 processes)
- AI opportunity matrix (prioritized)
- Recommended roadmap (phased)

### Audit Flow Using This Skill

```
Discovery Call
    ↓
[Use Business Functions Mapping Skill]
    ↓
Map Functions → Identify Processes → Document Pain Points
    ↓
Analyze → Prioritize AI Opportunities
    ↓
Create Roadmap
    ↓
Deliver Audit Report
```

---

## 💡 BEST PRACTICES

### 1. Start High-Level, Go Deep Selectively

**Do**:
- Begin with broad function categories
- Identify 5-10 core functions first
- Choose 3-5 highest-pain processes to map in detail

**Don't**:
- Try to document every single task
- Get lost in minutiae too early
- Map processes that don't matter

### 2. Focus on Pain and Opportunity

**Do**:
- Ask "where does this hurt?" repeatedly
- Quantify impact (time, cost, frequency)
- Identify patterns across functions

**Don't**:
- Map everything equally
- Ignore client's stated priorities
- Focus on functions that work well

### 3. Use Client Language

**Do**:
- Use their terminology for functions/roles
- Quote their pain points directly
- Adapt templates to their industry

**Don't**:
- Impose generic business terms
- Use jargon they don't use
- Force-fit standard categories

### 4. Quantify Where Possible

**Do**:
- Ask "how long does this take?"
- Ask "how often does this happen?"
- Calculate rough cost (time × hourly rate)
- Estimate error rates and rework

**Don't**:
- Accept vague answers ("it takes a while")
- Skip metrics collection
- Guess without data

### 5. Think in Systems, Not Silos

**Do**:
- Map dependencies between functions
- Identify handoff points
- Consider downstream impacts
- Look for compounding effects

**Don't**:
- Treat each function in isolation
- Miss cross-functional inefficiencies
- Ignore system-wide implications

---

## 🚀 QUICK START GUIDE

### For a 30-Minute Discovery Call

**Minutes 0-5**: High-level function identification
- "What are the main areas of work in your business?"
- List 5-8 core functions

**Minutes 5-20**: Deep dive on 2-3 highest-pain functions
- "Tell me about [function]. What's the process?"
- "Where does it break down?"
- "How much time does this consume?"
- Document pain points and process steps

**Minutes 20-28**: AI opportunity brainstorming
- "Based on what you shared, I see opportunities in..."
- Mention 3-5 specific AI applications
- Gauge interest/priority

**Minutes 28-30**: Next steps
- "I'll create a detailed function map and AI roadmap"
- Set expectations for deliverable

### For a Comprehensive Audit (2-3 hours work)

**Hour 1**: Function mapping
- Create complete function map
- Identify all sub-functions
- Document basic pain points

**Hour 2**: Process deep-dive
- Map 5-10 key processes in detail
- Analyze pain points
- Quantify impact where possible

**Hour 3**: Opportunity identification & prioritization
- List all AI opportunities
- Score and rank them
- Create phased roadmap
- Write executive summary

---

## 📊 EXAMPLE OUTPUT

### Sample: Small Business Consulting Firm

```markdown
# Business Functions Map - Acme Consulting

**Industry**: Management Consulting
**Size**: 15 employees
**Annual Revenue**: ~$2M

## Core Functions Identified

### 1. Sales & Business Development
**Purpose**: Acquire new clients
**Sub-Functions**:
- Outbound prospecting
- Proposal creation
- Contract negotiation
**Pain Points**:
- Proposals take 8-10 hours each (manual)
- Lost deals due to slow response time
- CRM data entry inconsistent

**AI Opportunities**:
- AI-assisted proposal generation (save 5-6 hours/proposal)
- Automated CRM updates from emails
- Lead scoring and prioritization

### 2. Project Delivery
**Purpose**: Execute client engagements
**Sub-Functions**:
- Client onboarding
- Research and analysis
- Report creation
- Presentation development
**Pain Points**:
- Onboarding takes 2 weeks (too long)
- Research duplicated across projects
- Report formatting time-intensive

**AI Opportunities**:
- Automated onboarding workflows
- AI research assistant (synthesize info)
- Template-based report generation
- Knowledge management AI

### 3. Operations & Administration
**Purpose**: Support business operations
**Sub-Functions**:
- Invoicing
- Time tracking
- Expense management
- Schedule coordination
**Pain Points**:
- Time tracking compliance low (~60%)
- Manual invoice creation
- Meeting scheduling coordination hell

**AI Opportunities**:
- Automated time tracking reminders
- Invoice auto-generation from time entries
- AI scheduling assistant

## Priority AI Opportunities

| Rank | Opportunity | Impact | Quick Win |
|------|------------|--------|-----------|
| 1 | AI proposal generation | 30 hours/month saved | Yes (30 days) |
| 2 | Onboarding automation | 2 weeks → 3 days | Yes (60 days) |
| 3 | Knowledge management AI | Reduce research by 40% | No (6 months) |

## Recommended Roadmap

**Phase 1 (30 days)**: Proposal automation
- Expected impact: Save 30 hours/month
- ROI: $6K/month (at $200/hr billable rate)

**Phase 2 (60 days)**: Onboarding automation + CRM integration
- Expected impact: Faster client starts + better data
- ROI: $3K/month + faster revenue recognition

**Phase 3 (6 months)**: Knowledge management system
- Expected impact: 40% faster research
- ROI: $10K/month in reclaimed billable time
```

---

## 🎯 SUCCESS METRICS

### Quality Indicators for Function Mapping

**Good Mapping Has**:
- ✅ Clear function categories (5-12)
- ✅ Specific pain points (not vague)
- ✅ Quantified impact (time, cost, frequency)
- ✅ Actionable AI opportunities (not generic)
- ✅ Prioritized roadmap (phased approach)
- ✅ Client language (their terms, not consultant-speak)

**Poor Mapping Has**:
- ❌ Too many functions (overwhelming)
- ❌ Vague pain points ("things are inefficient")
- ❌ No quantification ("it takes a while")
- ❌ Generic opportunities ("use AI for automation")
- ❌ No prioritization (everything is equal)
- ❌ Jargon the client doesn't use

---

## 🔧 TROUBLESHOOTING

### "I don't know where to start"
→ Use the Standard Function Library above
→ Start with: Sales, Delivery, Operations, Finance
→ Ask: "Do you have [function]? What does it look like?"

### "Client can't articulate their processes"
→ Ask about specific recent examples
→ "Walk me through the last time you [did X]"
→ "What happened yesterday/this week?"
→ Start with pain, work backward to process

### "Everything feels like a priority"
→ Use scoring framework (Impact × Feasibility × ROI)
→ Ask: "If you could only fix ONE thing, what would it be?"
→ Focus on frequency × impact (what hurts often and badly)

### "Client has unique business model"
→ Start with universal functions (how do you get customers, deliver value, get paid?)
→ Adapt Standard Function Library
→ Create custom categories as needed

### "Too much information, getting overwhelmed"
→ Focus on 3-5 core functions only
→ Map 3-5 highest-pain processes in detail
→ Everything else is high-level only
→ Remember: 80/20 rule applies

---

## Ready to Map a Business?

**Tell me**:
1. What organization are you mapping? (Industry, size)
2. Do you have discovery call notes? (If yes, share key points)
3. What level of detail do you need? (Quick overview vs comprehensive audit)
4. What's the primary goal? (AI opportunities, operational assessment, specific function deep-dive)

I'll use this framework to create a comprehensive business functions map with AI opportunity recommendations.
