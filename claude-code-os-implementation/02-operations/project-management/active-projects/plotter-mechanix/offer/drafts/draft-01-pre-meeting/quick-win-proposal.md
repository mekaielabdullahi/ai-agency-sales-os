# PlotterOps Quick Win Sprint
## Proposal for Plotter Mechanix

**Prepared for:** Kelce (Owner)
**Date:** December 2025

---

## What You're Getting

We're implementing a **Communication Control System** that makes Jobber your single source of truth—backed by automation that ensures nothing falls through the cracks.

---

## The Problem We're Solving

Right now, your communication is scattered:

| Current State | The Cost |
|---------------|----------|
| Kelce checks texts going back days to catch missed items | 30+ min/day wasted |
| Messages get read but not handled, then forgotten | Lost jobs, frustrated customers |
| Alyssa takes notes on sticky notes during calls | Transcription errors, delays |
| Kelce calls Alyssa after every job to hand off | Interruptions, no async flexibility |
| No system catches dropped balls | Things slip through |

**Your estimate:** This costs ~$20,000/year in lost time, mistakes, and missed opportunities.

---

## The Solution: Unified Communication System

We're not replacing Jobber—we're making it work the way it should, plus adding a centralized phone system that feeds everything into Jobber automatically.

### Recommended Tool: Quo

| Feature | What It Does | Why It Matters |
|---------|--------------|----------------|
| **One Business Number** | All calls/texts go through single number | No more checking personal cell, business cell, AND Jobber |
| **AI Call Summaries** | Every call transcribed and summarized | Replaces post-call handoff to Alyssa |
| **Auto-sync to Jobber** | Calls and texts automatically appear on client records | Everything in one place without manual entry (requires Jobber Core plan or higher) |
| **Unknown Caller → New Lead** | Unrecognized numbers auto-create contacts | No leads fall through the cracks |

**Cost:** ~$23/user/month billed annually = ~$69/month total for 3 users (Kelce, Alyssa, tech) or ~$99/month billed monthly

### Three Layers Working Together

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 1: PROTOCOLS                       │
│  Clear rules for how information flows through Jobber       │
│  • Message handling discipline                              │
│  • End-of-job handoff template                              │
│  • Lead intake workflow                                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   LAYER 2: AUTOMATION                       │
│  Smart workflows that catch what humans miss                │
│  • Daily digest of unhandled messages                       │
│  • New lead notifications                                   │
│  • End-of-day job summary                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    LAYER 3: TRAINING                        │
│  SOPs + videos so everyone knows exactly what to do         │
│  • 4 core workflow documents                                │
│  • Video walkthroughs                                       │
│  • Quick reference guides                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Deliverable 1: Four Core SOPs

These are the workflows that run your business daily. We document them, optimize them, and train your team.

| SOP | What It Covers | Why It Matters |
|-----|----------------|----------------|
| **Service Call Execution** | Arrival → documentation → completion → handoff | Trains techs, ensures consistency |
| **Invoice Queue Processing** | How Alyssa processes completed jobs | Eliminates sticky notes, faster billing |
| **Service Call Dispatch** | Real-time routing based on Kelce's location | Your competitive advantage, documented |
| **End-of-Job Handoff** | Async handoff replacing live calls | Saves 30+ min/day, no more interruptions |

**Format:** Professional documents with step-by-step procedures, decision flowcharts, and embedded diagrams. Plus short video walkthroughs.

**Bonus: Passive SOP Capture**

We'll also set up a simple system where Kelce can record himself working and narrating—and we turn those recordings into additional SOPs at no extra effort from him:

```
Kelce narrates while working → Uploads to shared folder → We process into polished SOP
```

This means every job site visit is an opportunity to capture tribal knowledge.

---

## Deliverable 2: Three Smart Automations

These run in the background, watching for problems and keeping everyone informed.

### Automation 1: Unhandled Message Daily Digest

**The problem it solves:**
> "People open the messages and don't do anything about it and then don't mark it as unread and then nobody sees the message."

**How it works:**
```
Every day at 4:00 PM:
  → Scan Jobber for messages not marked complete
  → Compile into a summary
  → Send to Alyssa (and optionally Kelce)
  → Nothing slips through the cracks
```

**Example output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📬 DAILY MESSAGE CHECK - Dec 12, 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  3 messages need attention:

1. ABC Printing (Mesa)
   Received: Yesterday 2:34 PM
   "When can you come back to finish the calibration?"
   → Status: Read, not responded

2. SignWorks LLC (Tempe)
   Received: Today 9:15 AM
   "Need quote for HP DesignJet maintenance"
   → Status: Unread

3. Quick Print Shop (Scottsdale)
   Received: 2 days ago
   "Parts arrived, ready to schedule install"
   → Status: Read, not scheduled

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Automation 2: New Lead Entry Notification

**The problem it solves:**
When Alyssa adds a new contact from a business card Kelce dropped, he has no visibility until he asks.

**How it works:**
```
When Alyssa adds a new contact to Jobber:
  → Kelce gets an instant notification
  → Includes: Company, contact name, how they found us, next action
  → Kelce stays informed without asking
```

**Example output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🆕 NEW LEAD ADDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Company: Desert Graphics
Contact: Maria Santos (602-555-1234)
Source: Business card drop - Tempe
Added by: Alyssa
Next action: Intro email sent, follow-up in 3 days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Automation 3: End-of-Day Job Summary

**The problem it solves:**
Kelce calls Alyssa after every job. That's 4-6 interruptions per day. By end of day, details are fuzzy.

**How it works:**
```
Every day at 5:30 PM:
  → Pull all jobs completed today from Jobber
  → Compile: Customer, work done, notes, photos, invoice status
  → Send to Alyssa as a single organized summary
  → She processes the queue without playing phone tag
```

**Example output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 END OF DAY SUMMARY - Dec 12, 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Kelsey completed 4 jobs today:

1. ✅ ABC Printing (Mesa) - 2.5 hrs
   Work: Replaced print head, ran calibration
   Notes: "Customer wants quote for backup ink supply"
   Photos: 3 attached
   → Ready to invoice: $475 + parts

2. ✅ SignWorks LLC (Tempe) - 1 hr
   Work: Nozzle check, cleaned heads
   Notes: "Routine maintenance, all good"
   Photos: 1 attached
   → Ready to invoice: $175

3. ✅ Quick Print Shop (Scottsdale) - 3 hrs
   Work: Installed new laminator rollers
   Notes: "Need to return Tuesday for calibration"
   Photos: 4 attached
   → Ready to invoice: $850
   → SCHEDULED: Return visit Tuesday 10am

4. ✅ Valley Signs (Phoenix) - 45 min
   Work: Diagnosed feed issue - needs parts
   Notes: "Order part #HP-4520-FEED, call when arrived"
   Photos: 2 attached
   → Ready to invoice: $175 (diagnostic)
   → PARTS NEEDED: HP-4520-FEED

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Revenue Today: $1,675
Jobs Needing Follow-up: 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Deliverable 3: End-of-Job Handoff Template

This is the linchpin. Instead of calling Alyssa after every job, Kelce fills out a structured template in Jobber. Takes 2 minutes. Alyssa gets everything she needs.

**The Template:**

```
┌─────────────────────────────────────────────────────────────┐
│           END-OF-JOB HANDOFF - Complete Before Leaving      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  WORK COMPLETED:                                            │
│  ☐ Describe what you did                                    │
│  ________________________________________________          │
│                                                             │
│  INVOICE DETAILS:                                           │
│  Labor: _______ hrs @ $______                               │
│  Parts used: _________________________________              │
│  Total: $_______                                            │
│                                                             │
│  FOLLOW-UP NEEDED?                                          │
│  ☐ No - Job complete                                        │
│  ☐ Yes - Return visit needed                                │
│      When: ____________  For: ____________________          │
│  ☐ Yes - Parts needed                                       │
│      Part #: ____________  Order from: ___________          │
│                                                             │
│  CUSTOMER CONVERSATION:                                     │
│  ☐ Any quotes requested? _________________________          │
│  ☐ Any concerns mentioned? _______________________          │
│  ☐ Upsell opportunity? ___________________________          │
│                                                             │
│  PHOTOS ATTACHED: ☐ Yes  ☐ No                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Why this works:**
- Kelce fills it out while details are fresh (at the job site)
- Alyssa processes it on her own time (no interruption)
- Nothing gets forgotten (structured fields)
- Creates documentation trail (in Jobber history)

---

## Deliverable 4: Communication Protocol Guide

A one-page rulebook everyone follows:

```
┌─────────────────────────────────────────────────────────────┐
│         PLOTTER MECHANICS COMMUNICATION RULES               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  RULE 1: Everything goes in Jobber                          │
│  • Customer communication = Jobber messages                 │
│  • Job notes = Jobber notes                                 │
│  • Photos = Jobber attachments                              │
│  • If it's not in Jobber, it didn't happen                  │
│                                                             │
│  RULE 2: Messages must be actioned                          │
│  • Read it? Do something with it.                           │
│  • Can't handle now? Mark for follow-up.                    │
│  • Daily digest catches anything missed.                    │
│                                                             │
│  RULE 3: End-of-job = Handoff template                      │
│  • No more phone calls to hand off                          │
│  • Fill out template before leaving site                    │
│  • Alyssa processes from queue                              │
│                                                             │
│  RULE 4: New leads = Jobber entry + notification            │
│  • Business card → Jobber within 1 hour                     │
│  • Automation notifies Kelce                                │
│  • Intro email same day                                     │
│                                                             │
│  RULE 5: Daily check-in (until habitual)                    │
│  • 4 PM: Check for unhandled messages                       │
│  • 5:30 PM: Review end-of-day summary                       │
│  • Morning: Review schedule (Kelce in hot tub)              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Deliverable 5: PlotterOps Blueprint

A visual roadmap showing where this fits in the bigger picture:

```
┌─────────────────────────────────────────────────────────────┐
│                   PLOTTEROPS ROADMAP                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PHASE 1: QUICK WIN SPRINT (Now)                            │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━                               │
│  ✓ Communication Control System                             │
│  ✓ 4 Core SOPs                                              │
│  ✓ 3 Smart Automations                                      │
│  ✓ Training + Adoption                                      │
│  Duration: 2-4 weeks                                        │
│                                                             │
│           │                                                 │
│           ▼                                                 │
│                                                             │
│  PHASE 2: PLOTTEROPS TRANSFORMATION                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                        │
│  ○ Working Inventory System                                 │
│     → Know what you have in stock                           │
│     → Alyssa answers "do we have X?" herself                │
│     → Reorder alerts before you run out                     │
│                                                             │
│  ○ Unified Ops Hub                                          │
│     → Capsule + QuickBooks + Jobber synced                  │
│     → One place for everything                              │
│     → Real-time visibility for whole team                   │
│                                                             │
│  ○ Complete SOP Library                                     │
│     → Every workflow documented                             │
│     → New hire training without Kelce                       │
│     → Reduce single-point-of-failure risk                   │
│                                                             │
│  Duration: 16 weeks                                         │
│                                                             │
│           │                                                 │
│           ▼                                                 │
│                                                             │
│  PHASE 3: PLOTTEROPS GUARDIAN (Ongoing)                     │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                      │
│  ○ Monthly ops reviews                                      │
│  ○ System maintenance                                       │
│  ○ New hire training                                        │
│  ○ Continuous optimization                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## What Changes For You

### For Kelce:

| Before | After |
|--------|-------|
| Check texts going back days to catch things | Daily digest surfaces anything missed |
| Call Alyssa after every job | Fill out 2-min template, she processes async |
| "Did you add that contact?" | Instant notification when leads are added |
| Worry about what's falling through | System catches it for you |

### For Alyssa:

| Before | After |
|--------|-------|
| Sticky notes during Kelsey's calls | Structured handoff in Jobber queue |
| "What did he say about that job?" | Clear notes with all details |
| Wondering if messages are handled | Daily digest confirms nothing missed |
| Transcribing verbal info | Info arrives pre-formatted |

### The Numbers

| Item | Value |
|------|-------|
| **New Monthly Cost** | ~$69/month (Quo for 3 users, billed annually) or ~$99/month (billed monthly) |
| **Expected Time Savings** | 30+ min/day = 10+ hours/month |
| **ROI** | At $50/hour, that's $500+/month in recovered time vs $69-99 cost |

**Note:** Jobber must be on Core plan or higher for Quo integration.

---

## Bonus: Inventory Pain Tracking

We know inventory is a big issue, but it's not something we can fix in 2 weeks. What we CAN do is **measure the cost** so we know exactly what it's worth to solve.

During Phase 1, every handoff template includes an "Inventory Issue Today?" section:
- Missing part (didn't have it)
- Wasted trip (wrong part/no part)
- Rush order needed ($X extra cost)
- Job delayed X days waiting for part

**After 30 days, you'll have real data:**
> "Last month: 3 wasted trips, 2 rush orders ($150 extra), 3 jobs delayed avg 2 days..."

This gives us the business case for the Phase 2 inventory system—and you'll know exactly what it's costing you right now.

---

## Timeline

| Week | What Happens |
|------|--------------|
| **Week 1** | Shadow session to validate workflows. Finalize SOPs. Build automations. |
| **Week 2** | Deploy automations. Live training session. Handoff template goes live. |
| **Week 3-4** | Support adoption. Refine based on real usage. Deliver Blueprint. |

---

## Investment

**$5,000** for the complete Quick Win Sprint

### Includes:
- 4 professional SOP documents
- 3 automated workflows (built, deployed, maintained for 30 days)
- Communication protocol guide
- Training videos
- Live training session
- PlotterOps Blueprint (roadmap for future phases)
- 30-day support for questions and adjustments

### Guarantee

> "If by day 30 you don't feel you have substantially more clarity and at least one live change that makes your day easier, we keep working until you do."

---

## Why This Works

You already use Jobber. You already know the tool. We're not asking you to learn something new—we're implementing:

1. **Clear rules** for how information flows
2. **Automation** that catches what humans miss
3. **Training** so everyone does it the same way

The result: **You stop playing catch-up.** Messages don't fall through. Alyssa can process jobs without calling you. And you have a safety net that alerts you if something gets missed.

---

## Ready to Start?

Let's get your communication under control in the next 2 weeks.

**Next step:** Sign off and schedule the kick-off call.

---

*Prepared by the PlotterOps Team*
