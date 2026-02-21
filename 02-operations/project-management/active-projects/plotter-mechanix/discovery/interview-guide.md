# Plotter Mechanix - ROI Interview Guide

**Created:** January 5, 2026
**Purpose:** Quick reference for stakeholder interviews to gather ROI data
**Related:** [Stakeholder Questions ROI](./stakeholder-questions-roi.md) | [Phase 1 PRD](../planning/phase-1-prd.md)

---

## Interview Schedule

| Stakeholder | Role | Duration | Priority Focus |
|-------------|------|----------|----------------|
| Kelsey | Owner/Lead Tech | 45 min | Phone system, financial baseline |
| Alyssa | Office Manager | 30 min | Phone details, time validation |
| Nikki | Co-Owner/Bookkeeping | 30 min | Operating costs, Malik review |
| Joe | Tech in Training | 20 min | Capability, field needs |

---

## Kelsey (Owner/Lead Tech) - 45 min

### Opening
> "We need to nail down some specifics to finalize the Quo phone setup and validate our ROI projections. These questions will take about 45 minutes."

### Priority 1 - Phone System (BLOCKS GO-LIVE)

| # | Question | Notes |
|---|----------|-------|
| 1 | What carrier owns your business phone number? (VoIP, landline, or wireless?) | |
| 2 | Are there bundled services on the phone line? (internet, fax?) | |
| 3 | What are the current Vonage IVR menu options we need to replicate? | |
| 4 | How open are you to using a dedicated business number where ALL calls get transcribed? | Context: If no, we need to build filtering for personal calls |
| 5 | What capture method would you actually use for voice notes? (phone call, voice memo app, text?) | |
| 6 | How many calls go to voicemail? Do customers complain about it? | |

### Priority 2 - Time Validation

| # | Question | Notes |
|---|----------|-------|
| 7 | We estimated ~0.5 hrs/day on handoff calls with Alyssa. Does that sound right? | PRD estimate |
| 8 | How many hours/week on admin tasks? (scheduling, invoicing) | |

### Priority 3 - Financial Baseline

| # | Question | Notes |
|---|----------|-------|
| 9 | What is your daily operating cost? | |
| 10 | What is the average service call revenue? | |
| 11 | What is your effective hourly rate? (Revenue divided by hours worked) | |

### Capacity Questions

| # | Question | Notes |
|---|----------|-------|
| 12 | How many calls do you turn away or delay per week? | Lost revenue |
| 13 | What % of calls could Joe handle if properly trained? | Scale potential |
| 14 | What is preventing Joe from handling more calls now? | Training gaps |

### Strategic (if time permits)

| # | Question | Notes |
|---|----------|-------|
| 15 | How many hours would you need back to make the move to Pinetop realistic? | His goal |

---

## Alyssa (Office Manager) - 30 min

### Opening
> "We need phone system details to start the number porting process, and to validate our time savings estimates."

### Priority 1 - Phone System (BLOCKS GO-LIVE)

| # | Question | Notes |
|---|----------|-------|
| 1 | Do you have the phone provider details? (account number, PIN) | Needed to start porting |
| 2 | What is the current Vonage monthly cost? | Calculate actual savings |
| 3 | What spam call volume do you currently experience? | Spam filtering config |
| 4 | How many calls go to voicemail? | AI answering decision |
| 5 | What happens with internal team calls between you and Kelsey? | Prevent garbage Jobber records |
| 6 | Do you need your own Quo line, or just access to view calls/transcripts? | Phone architecture |

### Priority 2 - Time Validation

| # | Question | Notes |
|---|----------|-------|
| 7 | We estimated ~1.5 hrs/day on manual entry. Does that sound right? | PRD estimate |
| 8 | How many hours/week on scheduling? | |
| 9 | How many status inquiry calls per week? | Call deflection value |
| 10 | How many customer calls per day? Average length? | |

### Pain Point Validation

| # | Question | Notes |
|---|----------|-------|
| 11 | How often do you double-book or have scheduling conflicts? | |
| 12 | What is the most time-consuming part of your job? | |
| 13 | What tasks do you wish you did not have to do? | |

---

## Nikki (Co-Owner / Bookkeeping) - 30 min

### Opening
> "We want to understand what happened with the previous project and get the operating cost numbers for our ROI calculator."

### Priority 1 - Past Project Review

| # | Question | Notes |
|---|----------|-------|
| 1 | Do you have Malik project folder? Can we review what was built? | Avoid duplicate work |
| 2 | What went wrong with Malik from your perspective? | Set expectations |
| 3 | Do you take any client calls or need a business phone line? | Phone architecture |

### Priority 2 - Daily Operating Costs

| # | Question | Monthly Amount |
|---|----------|----------------|
| 4 | What is the monthly rent for the shop? | $ |
| 5 | What are the average monthly utilities? (electric, gas, water, internet) | $ |
| 6 | How many employees and what is the total monthly payroll? | $ |
| 7 | What is the monthly liability/building insurance cost? | $ |
| 8 | How many trucks and what is the monthly cost per truck? | $ |
| 9 | What software subscriptions does the company have? | $ |

**Goal:** Calculate daily operating cost = Total monthly / 30

### QuickBooks Questions

| # | Question | Notes |
|---|----------|-------|
| 10 | What is the current state of QuickBooks after the $700K reconciliation error? | |
| 11 | How does information flow from Jobber to QuickBooks today? | |
| 12 | How many hours/week do you spend on bookkeeping? | |

### Business Perspective

| # | Question | Notes |
|---|----------|-------|
| 13 | What was your initial concern about this project? | She started skeptical |
| 14 | What changed your mind? | Understanding conversion |
| 15 | What would success look like to you specifically? | |

### Referral Potential

| # | Question | Notes |
|---|----------|-------|
| 16 | Who are the 5+ referral contacts you mentioned? | Names |
| 17 | What industries are they in? | |
| 18 | What would we need to deliver for you to feel confident making introductions? | |

---

## Joe (Tech in Training) - 20 min

### Opening
> "We want to understand your current capabilities and what would help you handle more calls independently."

### Capability Assessment

| # | Question | Notes |
|---|----------|-------|
| 1 | What % of service calls can you currently handle solo? | |
| 2 | What types of calls are you NOT ready for? | |
| 3 | What would help you get ready faster? | |
| 4 | How do you currently learn new repair procedures? | |

### Field Operations

| # | Question | Notes |
|---|----------|-------|
| 5 | How do you know what parts to bring on a call? | |
| 6 | How often do you have to call Kelsey for help during a job? | |
| 7 | What information do you wish you had before arriving at a job? | Field notes value |

---

## Quick Reference - What We Already Know

| Metric | Value | Confidence |
|--------|-------|------------|
| Annual revenue | $600K-$750K | Medium |
| Jobber subscription | $379/month | High |
| Phone tag calls/day | 4-6 | High |
| Screenshot handoffs/week | 20+ | Medium |
| Alyssa manual entry | 1.5 hrs/day | Estimate |
| Kelsey handoff time | 0.5 hrs/day | Estimate |
| Projected ROI | 17-25x | Pending validation |

---

## After Interview Checklist

- [ ] Update stakeholder-questions-roi.md with answers
- [ ] Mark questions as Gathered or Still Need
- [ ] Calculate validated daily operating cost
- [ ] Update ROI projections with real numbers
- [ ] Identify any new blockers discovered

---

**Tips:**
- Focus on getting actual numbers, not estimates
- If they say "I dont know," ask "Who would know?"
- Record answers in real-time
- Note any new pain points that emerge
