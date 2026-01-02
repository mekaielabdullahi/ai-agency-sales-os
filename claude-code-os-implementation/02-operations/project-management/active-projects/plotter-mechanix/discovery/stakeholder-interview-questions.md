# Plotter Mechanix - Stakeholder Interview Questions

**Created:** December 29, 2025
**Updated:** December 29, 2025
**Purpose:** Deep discovery questions for each stakeholder to establish baseline metrics AND unblock development

---

## 🚨 PRIORITY: Development-Blocking Questions

**These 9 questions MUST be answered this week to unblock development work.**

### Questions for Kelce (5)

| # | Question | What's Blocked |
|---|----------|----------------|
| K1 | What carrier currently owns the business phone number? (VoIP, landline, wireless?) | Number porting - entire project go-live |
| K2 | Are there bundled services (internet, fax) on the phone line? | Number porting timeline estimation |
| K3 | What capture method would you actually use for voice notes? | Field notes workflow design |
| K4 | How many calls go to voicemail? Do customers complain about it? | AI voice answering decision |
| **K5** | **How open are you to using a dedicated business number where ALL calls get transcribed?** | **Personal vs business data separation** |

**Context for K5:** Currently Kelsey uses personal number for business. If we transcribe everything, personal calls get mixed in. With a dedicated business number, personal stays personal, and we avoid building software to separate the two. Think ahead: if Plotter has 10 employees, do you want personal calls accidentally creating Jobber requests?

### Questions for Alyssa (4)

| # | Question | What's Blocked |
|---|----------|----------------|
| A1 | What phone provider details do you have (account #, PIN, etc.)? | Starting porting request |
| A2 | What spam call volume do you currently experience? | Spam filtering configuration |
| A3 | How many calls currently go to voicemail? | AI answering cost-benefit analysis |
| A4 | What happens with internal team calls (Kelce↔Alyssa)? | Preventing garbage Jobber records |

### What Gets Unblocked When Answered

| Feature | Blocked By | Ready When |
|---------|------------|------------|
| Number Porting | K1, K2, A1 | All 3 answered |
| AI Voice Answering Decision | K4, A3 | Both answered |
| Field Notes Workflow | K3 | Answered |
| Spam Filtering Config | A2 | Answered |
| Internal Call Handling | A4 | Answered |
| **Data Architecture** | **K5** | **If YES → clean system; If NO → build filtering** |

---

## Why We Need These Numbers

Without knowing the actual numbers:
- Hours people spend on tasks
- Money flow (where it's going)
- Daily operating costs

We're **shooting in the dark** with what to build. These questions establish the baseline for our ROI calculator.

---

## ROI Calculator Qualification Path

### First Question (Sales Qualifier):
**"Do you know your daily operating cost?"**

| If NO | If YES |
|-------|--------|
| One path in sales script | "You're a rare breed that knows your numbers" |
| Need to help them figure it out | Can move faster to ROI calculation |
| Discovery process is longer | Discovery process is more efficient |

---

## Stakeholder: Kelce (Owner/Lead Tech)

### 🚨 BLOCKING QUESTIONS (Must Answer to Unblock Development)

| # | Question | What's Blocked |
|---|----------|----------------|
| K1 | What carrier currently owns the business phone number? (VoIP, landline, wireless?) | Number porting - entire project go-live |
| K2 | Are there bundled services (internet, fax) on the phone line? | Number porting timeline estimation |
| K3 | What capture method would you actually use for voice notes? (phone call, voice memo app, text?) | Field notes workflow design |
| K4 | How many calls go to voicemail? Do customers complain about it? | AI voice answering decision (Sona vs voicemail) |

### Time & Labor Baseline
- [ ] How many hours per week do you spend on service calls?
- [ ] How many hours per week on commuting between jobs?
- [ ] How many hours on administrative tasks (scheduling, invoicing)?
- [ ] What's your effective hourly rate? (Revenue ÷ hours worked)
- [ ] How many hours would you need back to move to Pinetop?

### Revenue & Cost Baseline
- [ ] What's your daily operating cost?
- [ ] What does a typical service call generate in revenue?
- [ ] What's the average revenue per customer per year?
- [ ] What's your cost per service call (labor + travel + parts)?
- [ ] What % of revenue goes to parts/inventory vs labor?

### Capacity & Bottleneck
- [ ] How many more calls could you take if you had help?
- [ ] What % of calls could Joe handle if properly trained?
- [ ] What's preventing Joe from handling more calls now?
- [ ] How many calls do you turn away or delay?

### Inventory Specific
- [ ] What's the current inventory value?
- [ ] How much time per week on inventory management?
- [ ] How often do you run out of critical parts?
- [ ] What's the cost when you don't have a part on the truck?
- [ ] How many trips to suppliers per week?

---

## Stakeholder: Alyssa (Office Manager)

### 🚨 BLOCKING QUESTIONS (Must Answer to Unblock Development)

| # | Question | What's Blocked |
|---|----------|----------------|
| A1 | What phone provider details do you have (account #, PIN, etc.)? | Starting porting request |
| A2 | What spam call volume do you currently experience? | Spam filtering configuration |
| A3 | How many calls currently go to voicemail? | AI answering cost-benefit analysis |
| A4 | What happens with internal team calls (Kelce↔Alyssa)? | Preventing garbage Jobber records |

### Time & Task Baseline
- [ ] How many hours per week on scheduling?
- [ ] How many hours on invoicing and billing?
- [ ] How many customer calls per day?
- [ ] Average length of customer call?
- [ ] How many status inquiry calls per week?

### Pain Point Quantification
- [ ] How often do you double-book or have scheduling conflicts?
- [ ] How many customer complaints per week?
- [ ] What's the most time-consuming part of your job?
- [ ] What tasks do you wish you didn't have to do?

### Communication Flow
- [ ] How do you communicate with Kelce during the day?
- [ ] How many systems do you check for messages? (Jobber, text, email, etc.)
- [ ] How often is information lost or miscommunicated?

---

## Stakeholder: Joe (Technician in Training)

### Training & Capability
- [ ] What % of service calls can you currently handle solo?
- [ ] What types of calls are you NOT ready for?
- [ ] What would help you get ready faster?
- [ ] How do you currently learn new repair procedures?

### Field Operations
- [ ] How do you know what parts to bring on a call?
- [ ] How often do you have to call Kelce for help during a job?
- [ ] What information do you wish you had before arriving at a job?

---

## Baseline Metrics We Need (ROI Calculator Inputs)

### Labor Metrics
| Metric | Current | Target | Value |
|--------|---------|--------|-------|
| Kelce hours/week on service calls | ___ | ___ | $___ |
| Kelce hours/week on admin | ___ | ___ | $___ |
| Alyssa hours/week on scheduling | ___ | ___ | $___ |
| Joe solo call capability | ___% | ___% | $___ |

### Financial Metrics
| Metric | Current | Notes |
|--------|---------|-------|
| Daily operating cost | $___ | |
| Average service call revenue | $___ | |
| Average service call cost | $___ | |
| Monthly lost revenue (turned away calls) | $___ | |
| Monthly inventory carrying cost | $___ | |

### Efficiency Metrics
| Metric | Current | Notes |
|--------|---------|-------|
| Status inquiry calls/week | ___ | Time sink |
| Scheduling conflicts/week | ___ | Lost revenue |
| Emergency supplier trips/week | ___ | Time + cost |
| Customer complaints/week | ___ | Churn risk |

---

## Discovery Session Structure

### Session 1: Kelce Deep Dive (60-90 min)
- Financial baseline
- Time allocation
- Strategic vision
- Bottleneck identification

### Session 2: Alyssa Operations Review (45-60 min)
- Daily workflow walkthrough
- Pain point ranking
- Communication flow mapping
- Time tracking for key tasks

### Session 3: Joe Field Assessment (30-45 min)
- Capability assessment
- Training gap analysis
- Tool and information needs
- Shadowing opportunity?

---

## Post-Discovery: ROI Calculator

Once we have these numbers, we can build a simple spreadsheet that shows:

1. **Current State Cost** = Labor + Waste + Lost Revenue + Inefficiency
2. **Target State Cost** = Optimized Labor + Reduced Waste + Captured Revenue
3. **Investment Required** = Our solution cost
4. **ROI** = (Savings - Investment) / Investment × 100
5. **Payback Period** = Investment / Monthly Savings

**Key Insight:** If they don't know their numbers, we help them figure it out. That process alone is valuable and builds trust.

---

## Pre-Interview Preparation

### Required Watching
- [ ] **Liam's Baseline Metrics Video** - Critical for understanding what metrics to collect during stakeholder interviews

### This Week's Interviews (Chris Leading)
- [ ] Kelsey
- [ ] Nikki
- [ ] Alyssa
- [ ] Joe

**Goal:** Collect as many baseline metrics as possible from these conversations for the ROI calculator.

---

## Nikki-Specific Questions (Office/Admin)

Based on Dec 29 session discussion:

### Daily Operating Cost Collection
- [ ] What's the monthly rent for the shop?
- [ ] What are the average monthly utilities (electric, gas, water, internet)?
- [ ] How many employees and what's the total monthly payroll?
- [ ] What's the monthly liability/building insurance cost?
- [ ] How many trucks and what's the monthly cost per truck (payment, fuel, maintenance)?
- [ ] What software subscriptions does the company have? (Check for duplicates!)

**Goal:** Get Nikki to fill out the Daily Operating Cost spreadsheet so we can calculate their baseline.

### Time Tracking
- [ ] How many hours per week do you spend on each major task?
- [ ] What's the most repetitive part of your day?
- [ ] How often do you have to look up the same information multiple times?

---

## ROI Calculator Spreadsheet

**Action Item:** Share draft ROI calculator spreadsheet with Nikki & Alyssa during their interviews.

The spreadsheet should include:
- Rent/Facilities line items
- Utilities breakdown
- Payroll summary
- Insurance costs
- Vehicle costs
- Software subscriptions
- Inventory/materials estimate

**Chris's insight from Dec 29:** "For us to do our jobs, we need at least this. We're not asking for personal financial information. I just need you to answer these simple, basic operational costs for us to gauge what your daily operating cost is."

---

**Next Step:** Schedule discovery sessions with each stakeholder
- Chris to lead interviews this week
- Incorporate Liam's baseline metrics approach
- Collect data for ROI calculator spreadsheet
