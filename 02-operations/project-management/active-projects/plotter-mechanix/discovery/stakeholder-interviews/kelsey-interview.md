# Kelsey Interview - Stakeholder Questions

**Role:** Owner / Lead Tech
**Interview Status:** Pending
**Estimated Duration:** 45 minutes

---

## Context

Kelsey is the owner and primary service technician. He handles most client relationships and all complex service calls. His personal cell phone is currently mixed with business calls, causing confusion for customers. Goal: Move to Pinetop eventually, which requires freeing up his time.

**Key Quote:**
> "They're all confused. They're like, dude, you got this number, that number, this other number"

---

## Priority 1 - Phone Number Strategy (Critical for Phase 1)

We need to establish ONE primary business number and separate personal contact.

| # | Question | Why It Matters | Answer |
|---|----------|----------------|--------|
| 1 | What phone number do most customers call? Your cell or the Vonage number? | Determines which number to port/keep | |
| 2 | Are you open to having ONE dedicated business number that isn't your personal cell? | Required for clean phone architecture | |
| 3 | If we set up Quo as the single business number, would you be comfortable giving that out instead of your cell? | Buy-in for the change | |
| 4 | What about existing customers who have your cell? How do we transition them? | Migration planning | |

---

## Priority 2 - Call Routing Design

We need to define when calls should go to whom. Help us understand the logic:

| # | Question | Why It Matters | Answer |
|---|----------|----------------|--------|
| 5 | When a new customer calls, who should answer? You? Alyssa? | Default routing for new leads | |
| 6 | When an existing customer calls about an active job, who should handle it? | Active job routing | |
| 7 | What types of calls MUST come to you vs. can go to Alyssa? | Kelsey-only routing rules | |
| 8 | Are there calls Joe could handle? When? | Joe routing potential | |
| 9 | Should Alyssa be the first line for all calls, then transfer to you if needed? | Alyssa-first model | |
| 10 | What about after-hours calls? Voicemail? Emergency line? | After-hours routing | |
| 11 | What happens today when you're on a job and can't answer? | Current fallback behavior | |

---

## Priority 3 - Vonage Access (Blocking for IVR Replication)

| # | Question | Why It Matters | Answer |
|---|----------|----------------|--------|
| 12 | Can you log into Vonage with us so we can see the current IVR menu? (Need 2FA code) | Document current state before porting | |
| 13 | Are there any features in Vonage you rely on that we need to replicate? | Ensure no feature loss | |

*Note: We'll schedule a separate session to do the Vonage walkthrough together.*

---

## Priority 4 - Time Validation

| # | Question | Why It Matters | Answer |
|---|----------|----------------|--------|
| 14 | How much time per day do you spend on handoff calls with Alyssa? (We estimated 0.5 hrs) | Validate ROI projection | |
| 15 | How many hours/week on service calls vs. admin/communication? | Understand time split | |
| 16 | How many hours/week commuting between jobs? | Total time picture | |
| 17 | How many hours would you need back per week to feel like you could step away more? | Target for success | |

---

## Priority 5 - Voice Notes Workflow

| # | Question | Why It Matters | Answer |
|---|----------|----------------|--------|
| 18 | When you're in the field and need to capture notes, what's easiest? Phone call? Voice memo? Text? | Design UC-1 (async handoff) | |
| 19 | Would you use a dedicated voicemail line to leave job updates? | Voicemail-only Quo line option | |
| 20 | You already use ChatGPT - would a custom voice-to-Jobber tool there work? | ChatGPT alternative option | |

---

## Priority 6 - Revenue & Capacity

| # | Question | Why It Matters | Answer |
|---|----------|----------------|--------|
| 21 | Annual revenue still around $600K-$750K? | Validate financial baseline | |
| 22 | What's your average service call revenue? | Per-job value | |
| 23 | How many calls do you turn away or delay each week? | Lost opportunity cost | |
| 24 | If Joe could handle more calls, how many more could the business take? | Capacity upside | |

---

## Notes Section

### Key Insights:


### Call Routing Rules Identified:


### Follow-up Actions:


---

## Post-Interview Checklist

- [ ] Document call routing logic for Quo IVR design
- [ ] Schedule Vonage walkthrough session (need 2FA)
- [ ] Update PRD with validated time estimates
- [ ] Confirm primary business number decision
- [ ] Document voice notes preference for UC-1 design

---

**Created:** January 6, 2026
**Last Updated:** January 6, 2026
