# AntSavvy Discovery Meeting Analysis - November 28, 2025

**Analyzed By:** Software Engineering Manager Perspective
**Meeting Date:** November 28, 2025
**Analysis Date:** November 30, 2025

---

## Meeting Summary

**Client:** AntSavvy
**Industry:** Filipino marketing and fabrication company specializing in large-scale event production (concerts, brand activations, experiential marketing)
**Meeting Date:** November 28, 2025
**Duration:** 99 minutes
**Attendees:**
- Christian Marangone (Sales/Client Relations, AntSavvy family member)
- Joshua McCrystal (Turtle) - Software Engineer, Cache Converters
- Matthew Kerns - AI Agency Development (Architect)
- Guest: Christian's partner (AntSavvy family member, finance owner's daughter)

---

## What We Know (Explicitly Stated)

### Current Pain Points:

**Project Budgeting and Scoping Issues:**
- Current process takes approximately **80 hours (2 weeks)** from initial client contact to signed contract
- Projects range from $5K USD (small) to $2M+ USD (large blue-chip clients like Amazon Prime, Coca-Cola)
- Medium projects: $125K-$400K USD
- Large projects: $500K-$2M+ USD
- Human errors cause cost overruns averaging **$50K per project** (example: 10 × $5K forgotten items)
- Projects frequently go over budget due to forgotten client requirements
- Company is "taking losses on projects" due to missing costs in budgets

**Communication Breakdowns:**
- Information loss occurs between three departments: Accounts, Procurement, Implementation
- **16 work hours** spent on initial client-accounts team conversations to determine budget
- **24 hours** of conversation between Accounts, Procurement, and Implementation teams
- **30 hours** of conversation between Procurement and suppliers/contractors
- Total **70+ hours** before reaching Finance for final approval
- Finance manages 11 sub-businesses in addition to AntSavvy, creating bottlenecks
- Email is primary communication method between departments after initial face-to-face meetings
- No centralized tracking system for project requirements

**Trust and Security Issues:**
- "A lot of trust has been lost" within the business
- A department head allowed company resources to work for direct competitors, "stabbed the entire family and business in the back"
- Implementation department was eliminated (reduced from full department to 1-2 people)
- At least **3 departments have been eliminated** due to restructuring
- Lack of visibility into who is working on what and where resources are allocated

**Technology and Process Maturity:**
- Company director (Trissie) has used ChatGPT only **twice in her life**
- "Very, very new to the AI space"
- Currently using **Google Sheets** for project checklists
- Transitioned from Google to Outlook for email (lost access to historical emails)
- Use "Blue Project Management app" as CRM to track projects
- Most meetings are **face-to-face** (not digital), making capture difficult
- Some team members use Zoom with Otter AI or Zoom's built-in AI transcription

**Business Condition:**
- "The business is sinking right now"
- "Their reputation is sinking"
- "Their funds are sinking"
- Company has been operating for **20 years**
- Currently employs approximately **60 people**

### Current Systems/Tools:

**Documented:**
- Google Sheets (project checklists, budgeting templates)
- Blue Project Management app (CRM for project tracking)
- Zoom (online meetings, some with AI transcription enabled)
- Otter AI (note-taking, used by some team members)
- Outlook (recently migrated from Google email)
- Historical project data from past events (example: Coca-Cola 2024 event)

**Technology Infrastructure:**
- Company has Zoom Pro (includes AI transcription features)
- Some transcripts already being generated but not systematically used
- No AI automation currently in use
- No documented API integrations

### Current Processes:

**Project Intake and Budgeting Flow (As-Is):**

1. **Client → Accounts Team** (~16 hours)
   - Initial conversations to understand project scope
   - Budget determination
   - Meetings are primarily face-to-face, then move to email

2. **Accounts → Procurement + Implementation** (~24 hours)
   - Resource allocation discussions
   - Permit requirements identification
   - Material and logistics planning

3. **Procurement → Suppliers/Contractors** (~30 hours)
   - Pricing negotiations
   - Transit and logistics coordination
   - Material specifications

4. **All Teams → Finance** (via email)
   - Budget compilation sent to Finance department
   - Finance has final approval authority
   - Finance manages 11+ businesses, creating delays

5. **Finance → Client** (post-approval)
   - All client communication transfers to Finance team
   - Accounts, Procurement, Implementation teams removed from client contact

**Pain Points in Process:**
- All work is manual, no automation
- Heavy reliance on email communication
- Information forgotten between departments
- No systematic note-taking from client meetings
- Employees sometimes **cut costs from budget** to make projects "fit" without proper authorization
- Missing requirements discovered late in project lifecycle
- No paper trail for forgotten items or overlooked requirements

**Location-Specific Requirements:**
- Different permits required by region (example: Siargao island vs. Manila)
- Regulatory requirements vary significantly by location
- No automated system to cross-reference permit requirements

### Stated Goals:

**Primary Objectives:**
- **Reduce project sign-up time** from 80 hours (2 weeks) to 20 hours (3 days)
- **"Quadruple revenue on paper"** through time efficiency gains
- **Eliminate human error** in project scoping and budgeting
- **Centralize information** across departments and projects
- Implement tracking to know "who goes where, what happened"
- Prevent resource leakage to competitors
- Stick within client budgets (stop taking losses)

**Solution Vision (Christian's Proposal):**
- Implement AI note-taker (Fireflies, Fathom, or Zoom AI) in client meetings
- Build RAG (Retrieval Augmented Generation) chatbot trained on:
  - Company handbook
  - Historical project checklists
  - Past event data (Coca-Cola example provided)
  - Permit requirements by region
- RAG system outputs **3 datasets:**
  - Dataset 1: Accounts team information
  - Dataset 2: Procurement team information
  - Dataset 3: Implementation team information
- Automated email distribution to relevant departments
- Consolidate all data into single email to Finance

**Desired Quick Wins:**
- Get system operational before Christmas 2025
- Reduce forgotten costs from $50K/project to $5K-$10K/project (80-90% reduction)
- Demonstrate value quickly to build trust for larger custom solution
- Start with accounts team (5-6 people) as pilot

### Technical Constraints:

**Data Access Limitations:**
- Cannot access historical emails (Google → Outlook migration)
- Privacy concerns around email access ("a lot of it's really private")
- Face-to-face meetings are primary client interaction method
- No current API integrations in place

**Budget Constraints:**
- "Funds are sinking" - limited budget available
- Christian emphasized need for "cheapest possible overhead"
- Focus on quick wins with minimal upfront investment
- Suggested starting with $100/month Fathom licenses (5-6 accounts team members)
- Proposed $250/month retainer (down from typical $500/month)

**Organizational Constraints:**
- Low AI literacy across organization
- Change management will be challenging (20-year-old company, traditional processes)
- Trust issues due to recent internal betrayals
- Multiple stakeholders (Finance owns 11+ businesses)
- Restructuring in progress (3+ departments eliminated)

**Timeline Constraints:**
- **Goal: Onboard before Christmas 2025** (approximately 3-4 weeks from meeting date)
- Christian traveling to Philippines office on Monday (December 2, 2025)
- Minimal time for discovery and development
- Pressure to deliver quick wins to prove concept

**Security/Privacy:**
- Not government-level PII, but business-sensitive data
- Client project details are confidential
- No need for "six-foot concrete buried underground" security
- Standard business data protection required

---

## Questions Asked But Not Fully Answered

### From the meeting transcript, these questions were raised but need follow-up:

1. **Matthew asked: "Do we can we have access to basically the paper, the reports that like would run between departments?"**
   - **Who asked:** Matthew Kerns
   - **Context:** Trying to understand current email/document flow between Accounts → Procurement → Implementation → Finance
   - **Response:** Christian's partner (finance owner's daughter) said she would look, but no definitive answer provided. Christian mentioned they don't currently have access to the email system.
   - **Status:** UNRESOLVED - Need to get sample reports/emails during office visit Dec 2

2. **Matthew asked: "Are the procedures mapped out already and the process is mapped out already? Like if there's maybe internal documentation or guidance around the steps?"**
   - **Who asked:** Matthew Kerns
   - **Context:** Determining if formal process documentation exists
   - **Response:** Christian said "pretty sure they would have a handbook regarding that" but was not certain
   - **Status:** PARTIALLY ANSWERED - Handbook likely exists but not confirmed, need to verify during office visit

3. **Matthew asked: "Where have things gone wrong in the past?"**
   - **Who asked:** Matthew Kerns
   - **Context:** Understanding historical failure patterns to avoid repeating them
   - **Response:** Christian gave general examples (food truck forgotten, $5K items × 10 = $50K loss) but no specific documented incidents
   - **Status:** UNRESOLVED - Need specific post-mortems or incident reports

4. **Matthew asked: "Can we hook into their emails? Like, can we get access to the emails?"**
   - **Who asked:** Matthew Kerns
   - **Context:** Exploring possibility of automated email processing
   - **Response:** Christian said "that might be tricky" due to privacy concerns, suggested sample emails instead
   - **Status:** PARTIALLY ANSWERED - Full email access unlikely, sample emails possible

5. **Matthew asked: "Are those [transcripts] being used in any way already?"**
   - **Who asked:** Matthew Kerns
   - **Context:** Understanding current use of Zoom AI transcripts
   - **Response:** Christian confirmed transcripts are being generated but didn't clarify if/how they're used systematically
   - **Status:** UNRESOLVED - Need to understand current transcript workflow and adoption

6. **Matthew asked: "How do they do these client meetings?"**
   - **Who asked:** Matthew Kerns
   - **Context:** Understanding meeting format to determine AI note-taker implementation
   - **Response:** Christian's partner clarified they're "usually face-to-face" with email thread starting afterward
   - **Status:** PARTIALLY ANSWERED - Face-to-face primary method, but unclear if hybrid meetings occur or if recording face-to-face is feasible

7. **Joshua asked: "What sort of things do they focus on when they're trying to build a budget? Do they go, all right, safety is number one or we need X, Y, Z better?"**
   - **Who asked:** Joshua McCrystal
   - **Context:** Understanding budget prioritization and decision-making criteria
   - **Response:** Not directly answered - Christian showed checklist spreadsheet but didn't explain prioritization logic
   - **Status:** UNRESOLVED - Need to understand budget construction methodology and decision criteria

8. **Matthew asked: "Why is the company sinking? What is the biggest lever that we can attack with software?"**
   - **Who asked:** Matthew Kerns
   - **Context:** Root cause analysis to prioritize solution development
   - **Response:** Christian identified oversights, communication gaps, forgotten costs, lack of structure, and trust issues, but didn't quantify which is most impactful
   - **Status:** PARTIALLY ANSWERED - Multiple pain points identified, but need quantification and prioritization

---

## Additional Clarifying Questions (Organized by Category)

### Category 1: Current State Assessment

#### Understanding Existing Systems:

- What specific features of the "Blue Project Management app" are currently being used, and what data does it contain (project status, budgets, timelines, resource allocation)?
- How is project data currently structured in Google Sheets - are there standardized templates, or does each project manager create their own format?
- What is the current Zoom account setup - how many licenses, who has admin access, and is AI transcription enabled by default for all users or opt-in?
- Describe the Outlook email structure - are there shared mailboxes for departments, or individual accounts only?
- What other software tools are being used that weren't mentioned (accounting software, scheduling tools, file storage systems like Google Drive or Dropbox)?
- How do teams currently share files and documents - email attachments, shared drives, cloud storage, or other methods?

#### Process Documentation:

- Can you provide the employee handbook that was referenced - specifically sections covering project intake, budgeting, and cross-department communication?
- Are there standard operating procedures (SOPs) documented for each department, or are processes learned through shadowing and tribal knowledge?
- When a new accounts team member joins, what training materials or documentation do they receive to learn the project scoping process?
- Are there templates for emails that go between departments, or is each communication written from scratch?
- Has anyone attempted to map out the current workflow visually (flowcharts, process diagrams), or is this the first time it's being documented?
- Who owns process improvement initiatives currently - is there an operations manager or process improvement role?

#### Data Flow & Information Architecture:

- Walk me through a specific recent project from initial client contact to finance approval - what was communicated, when, through which channels, and by whom?
- Where do meeting notes currently go after client meetings - are they stored in Blue app, email, Google Docs, or personal notes?
- How does the Procurement team currently receive project requirements from Accounts - forwarded email, meeting, shared document, or verbal handoff?
- When Finance reviews a project budget, what format is it in - Excel spreadsheet, PDF, email body, or something else?
- How do suppliers and contractors currently submit quotes - email, phone, portal, or face-to-face?
- What happens to project data after a project is completed - is it archived, deleted, or used as reference for future similar projects?

---

### Category 2: Problem Root Cause Analysis

#### Operational Bottlenecks:

- In the 80-hour project scoping process, which specific steps take the longest - is it waiting for responses, gathering information, negotiating with suppliers, or internal approvals?
- When you say "16 hours" for accounts-client conversations, is that calendar time spread over multiple days/weeks, or actual conversation time?
- What causes delays in Finance approval - missing information, too many projects in queue, unclear budget presentations, or other factors?
- At what point in the process do most forgotten requirements surface - during implementation, at finance review, or after contract signing?
- Which department creates the most friction or delays in the current process from accounts team perspective, and why?
- Are there seasonal bottlenecks (busy event season) where this 80-hour timeline gets even longer?

#### Communication Gaps:

- When information gets "lost" between departments, what form does that information loss take - unclear emails, verbal instructions not written down, or assumptions made without confirmation?
- How often do departments need to circle back to clients for clarification because information wasn't captured in initial conversations?
- When Accounts sends a project to Procurement, what information is frequently missing that Procurement needs to ask about?
- How does Finance communicate rejections or revision requests - do they provide specific feedback on what needs to change, or generic "revise and resubmit"?
- Are there regular sync meetings between Accounts, Procurement, and Implementation, or is all coordination done asynchronously via email?
- When a project requirement changes mid-process, how is that change communicated to all stakeholders?

#### Human Error Patterns:

- Can you provide 3-5 specific examples of "forgotten costs" from recent projects - what was forgotten, why, and what was the financial impact?
- What types of client requirements are most commonly overlooked - physical items (food trucks), services (permits), location-specific needs (regional regulations), or something else?
- When employees "cut costs to fit the budget," is this a conscious decision documented somewhere, or does it happen silently without approval?
- Are the same team members responsible for most errors, or is it distributed across the accounts team?
- What quality control or review process exists before budgets are sent to Finance - does anyone double-check the accounts team's work?
- Have you attempted to address these error patterns before through training, checklists, or process changes? What was tried and why didn't it work?

---

### Category 3: Solution Feasibility Assessment

#### Technical Infrastructure:

- Do you have IT staff or a technical point of contact who can help with API integrations, system access, and troubleshooting?
- What is the current hosting/cloud infrastructure situation - do you use AWS, Google Cloud, Azure, on-premises servers, or no cloud infrastructure?
- For the Blue Project Management app, does it have an API we can integrate with, or is it a closed system with no programmatic access?
- What is the internet connectivity situation for team members - reliable high-speed internet, or occasional connectivity issues?
- Are team members using company-issued devices (laptops, tablets) or personal devices for work?
- What authentication systems are in place - single sign-on (SSO), individual passwords, two-factor authentication (2FA)?

#### Organizational Readiness:

- How would the accounts team (5-6 people) react to being required to use AI note-takers in every client meeting - enthusiastic, neutral, or resistant?
- Who has authority to mandate new tools and processes across departments - is it Finance, Operations, or individual department heads?
- What is the typical timeline for rolling out new tools at AntSavvy - immediate adoption, phased rollout over weeks/months, or slow adoption over quarters?
- Have previous technology initiatives succeeded or failed, and what were the key factors in those outcomes?
- How comfortable are team members with learning new software - do they adapt quickly, need extensive training, or resist change?
- Is there executive sponsorship for this AI automation initiative from Finance/President level, or is it being driven bottom-up?

#### Resource Constraints:

- What is the actual budget available for this initial phase - is there a hard cap at a specific dollar amount?
- Beyond the $250/month retainer mentioned, is there budget for one-time development costs, and if so, how much?
- Who will be the internal point of contact for providing documentation, answering questions, and testing solutions during development?
- How much time can the accounts team dedicate to testing and providing feedback on new systems during the busy period leading up to Christmas?
- If we need access to specific data or systems, what approval process is required and how long does it typically take?
- Are there any upcoming initiatives or changes that might conflict with this implementation (new CRM rollout, office relocation, etc.)?

---

### Category 4: Solution Type Determination

#### Software vs. Process Questions:

- Walk me through the accounts team's client intake meeting step-by-step as it happens today - who does what, when, and using which tools?
- After a client meeting, what does the accounts team member do first - write notes, send emails, update Blue app, create spreadsheet, or something else?
- If the accounts team had a perfect checklist that covered every possible client requirement, would following that checklist eliminate the forgotten costs problem, or is the issue that requirements are unique per project?
- When creating a budget, do accounts team members reference past similar projects, or does each project start from scratch?
- What happens when a client requests something unusual that's not on the standard checklist - is there a process to escalate and research, or does the accounts team wing it?
- If every client meeting was recorded and transcribed, would accounts team members actually review those transcripts, or would they still rely on their memory/notes?

#### AI Automation Viability:

- For the RAG chatbot vision, what specific questions would you expect it to answer - "What permits are needed in Manila?" or "Estimate budget for 500-person concert in Siargao" or something else?
- When you review the historical event data (Coca-Cola 2024 example), how consistent is the data format across projects - standardized fields, or every project documented differently?
- When the accounts team determines a project budget, what percentage is formulaic/rules-based (venue square footage × price per sqft) vs. judgment calls and negotiation?
- For regional permit requirements, does this information change frequently, or is it relatively stable over months/years?
- When suppliers provide quotes, are they structured consistently (line items, totals, terms) or do different suppliers use completely different formats?
- If the AI system suggested a budget but was 20% off from what accounts team expected, how would that be handled - trust the AI, override it, investigate the discrepancy?

#### Integration Requirements:

- Which systems absolutely need to communicate with each other for this solution to work - must Blue app talk to email, must Zoom integrate with N8N, or can they remain separate?
- Where are you currently manually copying data from one system to another - Blue app to Excel, email to Excel, Zoom transcripts to notes documents?
- Which tools are "must-keep" because they're mission-critical or contractually required, and which are you open to replacing if a better alternative exists?
- If we build an N8N workflow that processes Zoom transcripts and generates emails, does it need to integrate with Blue app immediately, or can that be phase 2?
- What is the priority order for integrations - AI note-taker → email distribution → Blue app updates → supplier communication → something else?
- Are there any tools or systems that are definitely going away in the next 6 months that we shouldn't invest time integrating with?

---

### Category 5: Implementation Strategy

#### Phased Approach Questions:

- If you could only fix ONE thing right now that would have the biggest impact on reducing losses, what would it be - better meeting notes, automated email reminders, budget templates, or something else?
- What's the smallest change we could make that would prove the AI concept works and build trust with skeptical team members?
- Which specific accounts team member would be the best "pilot" user for testing a solution - someone tech-savvy, someone with the most problematic projects, or the team leader?
- What does "quick win" mean to you in terms of timeline and impact - 50% reduction in one metric within 2 weeks, or something different?
- If we had to prioritize between (1) reducing forgotten costs or (2) reducing time to sign clients, which delivers more value to the business right now?
- Can we start with just new projects going forward, or do you need the solution to help with in-flight projects that are already in progress?

#### Risk & Change Management:

- What's the worst thing that could happen if we get this wrong - client data leaked, project goes over budget, team refuses to use new tools, or something else?
- Who needs to approve changes to the accounts team's workflow - Finance, department head, president, or team consensus?
- How do you typically roll out new tools or processes to your team - mandated top-down, voluntary adoption, pilot with early adopters, or other approach?
- What's failed in the past when you've tried to improve processes, and what can we learn from those failures?
- If the AI system makes a mistake (forgets a cost that human caught), how will that impact trust and adoption - will team lose faith immediately, or is there tolerance for learning curve?
- How will we measure success for this initiative - cost reduction, time savings, user satisfaction, error reduction, or multiple metrics?

---

## Information Gaps & Next Steps

### Critical Missing Information:

**Documentation Needed:**
- [ ] Company handbook (especially project intake, budgeting, communication protocols)
- [ ] Standard operating procedures (SOPs) for Accounts, Procurement, Implementation teams
- [ ] Sample project budgets (redacted for privacy) showing final format sent to Finance
- [ ] Email examples of department-to-department handoffs
- [ ] Historical project checklists (beyond the single Google Sheets example shown)
- [ ] Post-mortem or incident reports from projects that went over budget

**Data Access Requirements:**
- [ ] Access to historical Zoom transcripts (if available and not privacy-restricted)
- [ ] Sample client meeting notes from accounts team
- [ ] Blue Project Management app demo/walkthrough showing actual project data
- [ ] Supplier quote examples showing typical format and structure
- [ ] Regional permit requirement documentation (Manila, Siargao examples)

**Process Clarity Needed:**
- [ ] Detailed workflow map: Client → Accounts → Procurement → Implementation → Finance
- [ ] Decision criteria for budget approval/rejection from Finance perspective
- [ ] Escalation process when unusual client requests occur
- [ ] Quality control checkpoints in current process (if any exist)
- [ ] Change management process for updating budgets mid-project

**Quantified Impact Data:**
- [ ] Actual frequency of forgotten costs (per project, per month, per quarter)
- [ ] Distribution of project sizes (how many small vs. medium vs. large per month)
- [ ] Finance approval rate (what % of budgets get approved vs. sent back for revision)
- [ ] Time breakdown of 80-hour process (how much is waiting vs. active work)
- [ ] Account team capacity (how many projects can they handle simultaneously)

**Organizational Context:**
- [ ] Current restructuring plan and timeline
- [ ] Reporting structure (who reports to whom, decision-making authority)
- [ ] IT support availability and technical skill level
- [ ] Training budget and time availability for onboarding new tools

### Recommended Discovery Activities:

**Before Next Meeting (During Dec 2 Office Visit):**

1. **Conduct stakeholder interviews:**
   - Finance director (Trissie) - understand approval criteria and pain points
   - Accounts team lead - understand day-to-day workflow and error patterns
   - Procurement team - understand supplier communication and data needs
   - IT/Operations (if exists) - understand technical infrastructure and constraints

2. **Gather process artifacts:**
   - Request handbook and all available SOPs
   - Collect 3-5 sample project files (full paper trail from intake to finance approval)
   - Export recent Zoom transcripts if available
   - Screenshot Blue app workflow showing project stages
   - Photograph or export Google Sheets templates being used

3. **Shadow accounts team:**
   - Observe (or listen to recording of) actual client intake meeting
   - Watch accounts team member create budget from meeting notes
   - Observe handoff email being written to Procurement
   - Document actual time spent on each step vs. estimated 16 hours

4. **Map current state:**
   - Create visual workflow diagram with stakeholders to validate understanding
   - Identify all decision points and approval gates
   - Document all systems and tools touching the process
   - Mark pain points and error-prone steps on the map

5. **Validate technology readiness:**
   - Confirm Zoom AI transcription is enabled and test quality
   - Verify if Fathom or Otter AI is feasible for face-to-face meetings
   - Check if Blue app has API or export capabilities
   - Test email access and confirm sample emails can be provided

---

## Solution Type Recommendation (Preliminary)

Based on information gathered, the problem appears to require:

- [ ] **Process Modification Only** - Better documentation, checklists, training
- [ ] **Software Solution** - Custom application development
- [X] **AI Agent Automation** - Chatbots, RAG systems, workflow automation
- [X] **Hybrid Approach** - Process improvements + automation
- [ ] **Insufficient Information** - Need more discovery before recommendation

**Recommendation: Hybrid Approach (Process + Automation)**

### Reasoning:

**Why NOT Process Modification Only:**
- Company has operated for 20 years with current processes - pure documentation won't change behavior
- Human error patterns are systemic and repeated despite institutional knowledge
- Face-to-face meetings make manual note-taking unreliable
- No evidence of existing SOP adherence even if handbook exists
- Trust issues indicate cultural/structural problems that checklists alone won't solve

**Why NOT Pure Software Solution:**
- Timeline too aggressive (before Christmas) for custom development
- Budget too constrained ("funds are sinking") for ground-up application
- Team has low AI literacy - complex custom software will have adoption challenges
- Existing tools (Blue app, Zoom, email) are sufficient if connected properly
- Company is restructuring - custom software risks becoming obsolete if org changes

**Why Hybrid Approach (Process + Automation) Makes Sense:**

**1. Clear Process Gaps That Need Resolution First:**
- No systematic meeting note-taking process
- No standardized handoff format between departments
- No quality control checkpoints before Finance review
- Verbal/face-to-face communication not being captured
- Missing paper trail for decision-making

**Process improvements needed:**
- Mandate AI note-taker usage in all client meetings (Zoom AI or Otter AI)
- Create standardized email templates for Accounts → Procurement → Implementation handoffs
- Establish review checkpoint before Finance submission
- Document decision criteria for budget construction
- Create centralized repository for meeting transcripts and project documentation

**2. Automation Can Amplify Good Process:**
- Once meetings are recorded, AI can extract action items and requirements automatically
- Once email templates exist, N8N workflow can auto-populate and route them
- Once data is centralized, RAG chatbot can surface relevant historical projects and permit requirements
- Automation reduces cognitive load on accounts team (no manual copying between systems)

**3. Phased Implementation Aligns with Constraints:**

**Phase 1 (Quick Win - Target: Before Christmas):**
- Enable Zoom AI transcription for all accounts team meetings (5-6 licenses)
- Create simple N8N workflow: Zoom transcript → extract key requirements → generate reminder email to accounts team
- Build basic checklist template based on historical Google Sheets data
- Result: Reduce forgotten costs by capturing better meeting notes (aim for 50% error reduction)

**Phase 2 (Trust Builder - Target: January 2025):**
- Implement automated email distribution based on project phase
- Build department-specific email templates in N8N
- Add quality control checkpoint: automated email to accounts team after client meeting saying "Did you capture these 10 items?"
- Result: Reduce time from 80 hours to ~50 hours by automating communication handoffs

**Phase 3 (Core Solution - Target: February-March 2025):**
- Build RAG chatbot trained on handbook, historical projects, permit requirements
- Integrate chatbot into accounts team workflow for budget estimation assistance
- Create dashboard showing project status across all departments
- Result: Reduce time to ~20-30 hours, reduce errors by 80-90% vs. baseline

**Phase 4 (Scale & Optimize - Target: Post-OBG Achievement):**
- Custom AntSavvy solution with Blue app integration
- Supplier/contractor quote automation
- Predictive budget modeling based on project parameters
- Result: Full centralization, real-time visibility, sub-20-hour project scoping

**4. Risk Mitigation Through Incremental Delivery:**
- If Phase 1 fails, minimal investment lost (only time spent on N8N workflow + Zoom setup)
- Each phase builds trust before requesting more budget
- Can pivot based on which interventions show highest ROI
- Team can learn AI tools gradually (Zoom AI → N8N → RAG chatbot) rather than all at once

**5. Addresses Root Cause Hierarchy:**

**Immediate Root Cause (80% of problem):**
- Information not captured in client meetings → AI note-taker solves this
- Information not communicated between departments → Email automation solves this

**Secondary Root Cause (15% of problem):**
- No standardized process for budget construction → Templates + RAG chatbot assistance
- No quality control before Finance review → Automated checklist verification

**Tertiary Root Cause (5% of problem):**
- Low AI literacy and resistance to change → Phased approach allows gradual adoption
- Trust issues from internal betrayal → Centralized tracking provides visibility

**Technology Stack Recommendation:**

**Phase 1 (Minimal Viable Automation):**
- **Note-taking:** Zoom AI (already paid for) + Otter AI backup for face-to-face
- **Workflow:** N8N (cloud hosted) - free tier or $20/month Pro
- **Storage:** Google Sheets (already familiar) or Airtable (better structure)
- **Communication:** Existing email (Outlook)
- **Total Monthly Cost:** $20-40 + ~20 hours development time

**Phase 2-3 (Core Solution):**
- **RAG Chatbot:** OpenAI API (GPT-4) + Assistants API with file search
- **Vector Database:** Pinecone free tier or OpenAI native file search
- **Backend:** N8N workflows for orchestration
- **Frontend:** Simple web interface (e.g., Streamlit) or directly in N8N chat widget
- **Total Monthly Cost:** $50-150 (depending on usage) + ~40-60 hours development time

**Why NOT AWS Bedrock/Aurora (as Richard suggested):**
- Timeline too short to learn AWS infrastructure if team not already expert
- OpenAI Assistants API provides faster time-to-value with built-in RAG capabilities
- Budget constraints don't justify AWS infrastructure costs for quick win
- Can migrate to AWS later if scale demands it (Phase 4)

**Why NOT Pure Custom Code:**
- N8N provides visual workflow builder that client can understand and modify
- Faster iteration and testing vs. writing Python/Node.js from scratch
- Christian mentioned "we can do custom-built" but emphasized "cheapest overhead"
- Custom code appropriate for Phase 4 when budget increases

---

## Proposed Next Steps

### Before Building Anything:

**1. Discovery & Documentation (Dec 2-6, 2025 - During Philippines Office Visit):**

**Priority 1 (Must Have):**
- [ ] Obtain company handbook and any existing SOPs
- [ ] Collect 3-5 complete project files showing full paper trail (client meeting → finance approval)
- [ ] Interview Finance director (Trissie) - 30 min to understand approval criteria
- [ ] Interview Accounts team lead - 30 min to understand workflow and pain points
- [ ] Confirm Zoom AI transcription is enabled; collect sample transcripts if available
- [ ] Export historical project checklist templates from Google Sheets

**Priority 2 (Should Have):**
- [ ] Shadow or review recording of actual client intake meeting
- [ ] Collect sample emails showing Accounts → Procurement handoff
- [ ] Document Blue app workflow with screenshots
- [ ] Gather regional permit requirement documentation (Manila/Siargao examples)
- [ ] Map stakeholder decision-making authority (who approves what)

**Priority 3 (Nice to Have):**
- [ ] Interview Procurement team member - understand supplier communication
- [ ] Collect supplier quote examples showing format variations
- [ ] Document any previous process improvement attempts and why they failed
- [ ] Identify IT/technical point of contact for implementation support

**2. Analysis & Design (Dec 7-10, 2025 - Remote Collaboration):**

- [ ] Matthew: Analyze handbook and process documentation for gaps
- [ ] Matthew: Review sample project files to identify error patterns
- [ ] Christian: Create Figma workflow diagram showing proposed solution
- [ ] Team: Conduct gap analysis - compare current state vs. desired state
- [ ] Team: Prioritize interventions by ROI (quick wins vs. long-term value)
- [ ] Joshua: Research N8N + Zoom AI integration options and feasibility

**3. Architecture & Scoping (Dec 11-13, 2025 - Technical Planning):**

- [ ] Define Phase 1 scope in detail (features, timeline, cost)
- [ ] Create technical architecture diagram for Phase 1
- [ ] Identify any blockers or dependencies (API access, permissions, approvals)
- [ ] Estimate development time and cost (both build and ongoing operations)
- [ ] Draft proposal with Christian for Finance team review

**4. Approval & Contracting (Dec 14-18, 2025 - Business Alignment):**

- [ ] Christian presents Figma workflow + proposal to AntSavvy Finance/President
- [ ] Negotiate scope, budget, timeline for Phase 1
- [ ] Define success metrics (how will we measure 50% error reduction?)
- [ ] Establish communication cadence (weekly check-ins, async updates)
- [ ] Sign contract with clear deliverables and payment terms

---

### Quick Win Opportunities:

**Option A: Zoom AI Transcript → Email Reminder (Lowest Effort, Moderate Impact)**

**Description:**
- Enable Zoom AI transcription for all accounts team client meetings
- Create N8N workflow that triggers when new Zoom transcript available
- Extract key requirements using OpenAI API (GPT-4 prompt engineering)
- Generate email to accounts team member listing: "From your meeting with [Client], did you remember to include: [list of 10 items extracted from transcript]?"
- Email sent within 1 hour of meeting ending

**Timeline:** 3-5 days to build and test
**Resources Required:**
- Zoom Pro access (already have)
- N8N Pro account ($20/month)
- OpenAI API key ($20-50/month estimated usage)
- 10-15 hours development time (Matthew + Joshua)

**Expected Impact:**
- 30-50% reduction in forgotten costs (catches items mentioned in meeting but not written down)
- Accounts team builds habit of reviewing transcripts
- Demonstrates AI value with minimal disruption to workflow

**Success Metrics:**
- Accounts team reports fewer "oh, we forgot that" moments in first month
- Finance rejects fewer budgets for missing information
- Team actually uses the reminder emails (open rate >80%)

---

**Option B: Standardized Email Templates + Auto-Population (Moderate Effort, High Impact)**

**Description:**
- Create email templates for each handoff: Accounts → Procurement, Accounts → Implementation, All → Finance
- Templates include structured fields: Project Name, Client, Budget Range, Key Requirements, Special Considerations, Location/Permits
- N8N workflow auto-populates templates from Zoom transcript or manual Google Sheets entry
- Pre-filled draft email generated for accounts team to review and send

**Timeline:** 5-7 days to build and test
**Resources Required:**
- Template design collaboration with Accounts team (2-3 hours)
- N8N workflow development (15-20 hours)
- Google Sheets as interim database
- Training session for accounts team (1 hour)

**Expected Impact:**
- 40-60% reduction in communication time (no writing emails from scratch)
- Standardized format reduces information loss between departments
- Creates paper trail for forgotten items (if it's not in template, it wasn't communicated)

**Success Metrics:**
- Time from client meeting to Finance submission reduced from 80 hours to 50-60 hours
- Finance team reports higher quality budget submissions
- Accounts team adoption rate >90% after first month

---

**Option C: Simple RAG Chatbot for Permit/Historical Reference (High Effort, High Impact)**

**Description:**
- Build basic RAG chatbot using OpenAI Assistants API + file search
- Train on: Company handbook, historical project checklists (Coca-Cola example), regional permit requirements
- Accounts team can ask: "What permits are needed for outdoor concert in Manila?" or "Show me similar projects to [client request]"
- Embedded in simple web interface or N8N chat widget

**Timeline:** 10-14 days to build and test
**Resources Required:**
- Document collection and formatting (5-10 hours)
- OpenAI Assistants API setup ($50-100/month)
- Web interface development (20-30 hours) or N8N chat widget (10-15 hours)
- Training session and user guide creation (3-5 hours)

**Expected Impact:**
- Accounts team can reference past projects instantly (vs. searching Google Sheets)
- Reduce time spent researching permit requirements
- New accounts team members ramp up faster with AI assistant

**Success Metrics:**
- Accounts team uses chatbot at least once per project on average
- Time spent on research reduced by 25-50%
- Budgets include accurate permit costs (fewer missing permits)

---

**Recommendation: Start with Option A + Option B in Parallel**

**Rationale:**
- **Option A** is quick proof-of-concept showing AI value (build trust)
- **Option B** addresses communication gaps which seem to be bigger pain point than knowledge gaps
- Combined, these two deliver 60-70% of desired impact for ~20% of Option C effort
- Can build Option C (RAG chatbot) in Phase 2 once trust established and budget secured

**Combined Timeline:** 7-10 days development + 3-5 days testing = **~2 weeks total**
**Combined Cost:** ~$40/month ongoing + 25-35 hours development time
**Combined Impact:** 50-60% reduction in forgotten costs + 30-40% reduction in time to Finance submission

---

### Phased Implementation Plan

#### Phase 1 (Quick Win): Meeting Capture & Communication Automation
**Timeline:** December 2025 (Weeks 1-3)
**Budget:** $500-1000 one-time + $50-100/month ongoing

**Deliverables:**
1. Zoom AI transcription enabled for 5-6 accounts team members
2. N8N workflow: Zoom transcript → requirement extraction → reminder email
3. Standardized email templates for department handoffs
4. N8N workflow: Auto-populate templates from meeting notes
5. Training session for accounts team (1 hour)
6. User guide with screenshots and FAQs

**Success Criteria:**
- 80%+ accounts team adoption within 2 weeks
- At least 1 forgotten cost caught per project using reminder emails
- Time from client meeting to Finance submission reduced by 20-30%
- Finance team reports improved budget submission quality

**Risks & Mitigations:**
- **Risk:** Accounts team resists using new tools → **Mitigation:** Executive mandate from Finance, show quick wins in first week
- **Risk:** Zoom transcripts poor quality for face-to-face meetings → **Mitigation:** Otter AI backup plan, test recording from phone
- **Risk:** N8N workflow breaks and no one knows how to fix → **Mitigation:** Comprehensive documentation, Christian learns N8N basics for triage
- **Risk:** Privacy concerns about recording client meetings → **Mitigation:** Client disclosure scripts, store transcripts securely, retention policy

---

#### Phase 2 (Core Solution): RAG Chatbot & Process Centralization
**Timeline:** January-February 2026 (Weeks 4-10)
**Budget:** $2000-4000 one-time + $150-250/month ongoing

**Deliverables:**
1. RAG chatbot trained on handbook, historical projects, permit requirements
2. Web interface or N8N chat widget for accounts team access
3. Integration with Blue Project Management app (if API available)
4. Automated budget draft generation from meeting transcript + chatbot data
5. Quality control checkpoint: Automated email flagging missing checklist items
6. Centralized dashboard showing project status across departments

**Success Criteria:**
- Chatbot answers 80%+ of accounts team questions accurately
- Time from client meeting to Finance submission reduced to 30-40 hours
- Forgotten costs reduced by 70-80% vs. baseline
- Finance approval rate increases (fewer revisions needed)

**Risks & Mitigations:**
- **Risk:** RAG chatbot gives incorrect permit requirements → **Mitigation:** Human review required, chatbot labeled as "assistant" not "authority"
- **Risk:** Historical project data too inconsistent to train effectively → **Mitigation:** Manual data cleaning sprint, start with subset of clean data
- **Risk:** Team doesn't trust AI recommendations → **Mitigation:** Show confidence scores, cite sources, allow easy override
- **Risk:** Budget blows out due to API usage → **Mitigation:** Set OpenAI spending limits, optimize prompts, cache common queries

---

#### Phase 3 (Optimization): Full Workflow Automation & Insights
**Timeline:** March-May 2026 (Weeks 11-20)
**Budget:** $5000-10000 one-time + $250-500/month ongoing

**Deliverables:**
1. End-to-end automation: Client meeting → Budget draft → Department routing → Finance approval tracking
2. Supplier/contractor quote ingestion and comparison
3. Predictive budget modeling using historical project data
4. Real-time project tracking dashboard replacing/enhancing Blue app
5. Resource allocation visibility (who's working on what)
6. Automated reporting for Finance across 11+ businesses

**Success Criteria:**
- Time from client meeting to Finance submission reduced to 20-30 hours
- Forgotten costs reduced by 90%+ vs. baseline
- Revenue increased due to faster client sign-up (4x more projects per quarter)
- Finance team spends 50% less time on AntSavvy project reviews

**Risks & Mitigations:**
- **Risk:** Custom development introduces bugs that disrupt operations → **Mitigation:** Rigorous testing, staged rollout, fallback to Phase 2 system
- **Risk:** Solution becomes too complex for team to maintain → **Mitigation:** Comprehensive documentation, video walkthroughs, $250/month retainer for support
- **Risk:** Business needs change due to ongoing restructuring → **Mitigation:** Modular architecture allowing components to be swapped without full rebuild

---

## Key Assumptions & Validation Needed

**Assumptions Made in This Analysis:**

1. **The 80-hour timeline is primarily wasted time, not necessary work** → Validate by shadowing actual project and timing each step
2. **Forgotten costs ($50K/project) are primarily due to poor meeting notes** → Validate by reviewing post-mortems to see if root cause is really note-taking
3. **Accounts team will adopt AI tools if mandated by Finance** → Validate through stakeholder interviews about change management history
4. **Face-to-face meetings can be captured via phone + Otter AI** → Validate through technical testing before committing to solution
5. **Finance approval delays are due to missing information, not high volume** → Validate by interviewing Finance team about rejection reasons
6. **Blue app integration is not critical for Phase 1** → Validate by understanding current Blue app usage and data dependencies
7. **Historical project data is sufficiently structured to train RAG chatbot** → Validate by reviewing multiple project files for consistency
8. **$250/month retainer is acceptable to AntSavvy given budget constraints** → Validate during proposal presentation and negotiation
9. **Procurement and Implementation teams will accept automated handoffs** → Validate through stakeholder interviews about their current pain points
10. **Regional permit requirements can be documented and kept current** → Validate by understanding how often regulations change and who tracks updates

---

## Final Recommendations

### For Christian (Sales/Project Manager):

**Before Next Team Meeting:**
1. Gather all Priority 1 discovery materials during Dec 2 Philippines office visit
2. Confirm executive sponsorship from Finance/President level
3. Validate budget availability for Phase 1 ($500-1000 + $50-100/month)
4. Set expectations with AntSavvy that this is phased approach, not instant fix

**For Proposal/Figma Presentation:**
1. Focus on quick wins, not ambitious end state
2. Emphasize **tangible metrics**: 50% fewer forgotten costs, 30% faster approvals
3. Position as "pilot with accounts team" expandable to other departments if successful
4. Include clear success criteria and decision point: "After 1 month, we measure X - if met, continue to Phase 2"
5. Avoid overpromising on complex features (RAG chatbot, predictive modeling) until Phase 2/3

### For Matthew (Technical Architect):

**Before Building Anything:**
1. Review handbook and process documentation to validate workflow understanding
2. Analyze sample project files to identify actual vs. perceived error patterns
3. Test Zoom AI transcript quality with sample meetings
4. Research N8N + Zoom API integration (confirm feasibility before committing)
5. Prototype simple requirement extraction prompt with OpenAI (validate accuracy)

**Technical Architecture Decisions:**
1. **Start with N8N, not custom code** - faster iteration, visual workflows client can understand
2. **Use OpenAI Assistants API for RAG, not AWS Bedrock** - faster time-to-value given timeline
3. **Store data in Google Sheets or Airtable initially** - familiar to client, avoid DB setup overhead
4. **Build modular workflows** - each N8N workflow solves one problem, can be deployed/tested independently
5. **Instrument with logging** - capture every API call, error, and user action for debugging and optimization

### For Joshua (Developer):

**Phase 1 Focus Areas:**
1. N8N workflow development - you have practical experience, lead on this
2. Testing transcript quality and requirement extraction accuracy
3. Email template design and auto-population logic
4. User acceptance testing with accounts team (get feedback early and often)

**Learning Opportunities:**
1. OpenAI API prompt engineering for information extraction
2. N8N best practices for error handling and retry logic
3. Change management and user training (technical skills + people skills)

---

## Appendix: Reference Materials Needed

**To Be Collected During Dec 2 Philippines Office Visit:**

### Documents:
- [ ] Company handbook (full or relevant sections)
- [ ] Standard operating procedures (SOPs) for each department
- [ ] 3-5 complete project files with full paper trail
- [ ] Sample emails showing department handoffs
- [ ] Historical project checklists (multiple examples beyond Coca-Cola)
- [ ] Regional permit requirement documentation

### System Access:
- [ ] Blue Project Management app demo/screenshots
- [ ] Zoom account admin access to verify AI settings
- [ ] Sample Zoom transcripts (if available)
- [ ] Google Sheets templates currently in use

### Stakeholder Input:
- [ ] Finance director interview notes (approval criteria, pain points)
- [ ] Accounts team lead interview notes (workflow, error patterns)
- [ ] Procurement team interview notes (supplier communication)
- [ ] IT/technical contact information

### Process Maps:
- [ ] Visual workflow diagram (created collaboratively during visit)
- [ ] Pain point and error location mapping
- [ ] Decision authority matrix (who approves what)

---

**Analysis Complete - Ready for Discovery Phase**

**Next Action:** Christian to gather Priority 1 materials during Dec 2-6 Philippines office visit, then schedule follow-up technical planning meeting with Matthew and Joshua for Dec 7-10.
