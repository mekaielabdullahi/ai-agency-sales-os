# Visual Glossary: What Each System Looks Like

Simple guide to understand the technology in this case study.

---

## How to Use This Document

Each system has:
- **What it is** (simple explanation)
- **What it looks like** (visual description)
- **Screenshot status** (do we have images?)

---

## The Main Systems

### 1. Jobber

| Question | Answer |
|----------|--------|
| What is it? | Software to manage repair jobs |
| Who uses it? | Kelsey, Alyssa, Joe |
| Why is it important? | This is where ALL work should be tracked |

**What it looks like:**
- Calendar with scheduled jobs
- List of customers
- List of requests (inbox)
- Invoices and payments

**Key screens to show:**
| Screen | Description |
|--------|-------------|
| Request Queue | Inbox of new customer requests |
| Job Schedule | Calendar showing who goes where |
| Customer Profile | Information about one customer |

**Colors:** Blue and white interface

**Screenshot status:** NEED TO CAPTURE
- Need demo with fake data (not real customer names)

---

### 2. Quo

| Question | Answer |
|----------|--------|
| What is it? | Phone system that records and transcribes calls |
| Who uses it? | Kelsey (mainly) |
| Why is it important? | This captures ALL phone calls automatically |

**What it looks like:**
- Phone app (looks like normal phone)
- Shows call history
- Shows transcript (written words from call)
- Shows AI summary

**Key screens to show:**
| Screen | Description |
|--------|-------------|
| Call History | List of recent calls |
| Transcript View | Full text of what was said |
| Summary View | Short version of key points |

**Colors:** Modern, clean interface (usually white/gray)

**Screenshot status:** NEED TO CAPTURE
- Need example showing transcript

---

### 3. N8N (workflow automation)

| Question | Answer |
|----------|--------|
| What is it? | Tool that connects different apps together |
| Who uses it? | AriseGroup team (backend) |
| Why is it important? | This is what makes everything automatic |

**What it looks like:**
- Flowchart with boxes and arrows
- Each box is one step
- Arrows show how data moves

**Example diagram:**
```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│   QUO    │ →  │    AI    │ →  │  JOBBER  │ →  │  SLACK   │
│  (call)  │    │(summary) │    │ (request)│    │ (alert)  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

**Colors:** Orange brand color, boxes are colorful

**Screenshot status:** NEED TO CAPTURE
- Need workflow diagram view
- BLUR any API keys or sensitive data

---

### 4. Slack

| Question | Answer |
|----------|--------|
| What is it? | Team chat application |
| Who uses it? | AriseGroup team, Kelsey's team |
| Why is it important? | Shows alerts when things happen |

**What it looks like:**
- Chat bubbles
- Channels (like group chats)
- Notifications

**Key screens to show:**
| Screen | Description |
|--------|-------------|
| Alert notification | Message showing new call came in |
| Daily digest | Summary of day's activity |

**Colors:** Purple brand color, chat bubbles

**Screenshot status:** NEED TO CAPTURE
- Need example of automation alert

---

## Visual Diagrams to Create

### The Full Flow (Main Diagram)

This shows how everything connects:

```
┌─────────────────────────────────────────────────────────────┐
│                      THE FLOW                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  CUSTOMER        QUO          AI           JOBBER    TEAM   │
│     │            │            │              │         │    │
│     │  CALLS     │            │              │         │    │
│     ├──────────► │            │              │         │    │
│     │            │  RECORDS   │              │         │    │
│     │            ├──────────► │              │         │    │
│     │            │            │  SUMMARIZES  │         │    │
│     │            │            ├────────────► │         │    │
│     │            │            │              │  ALERTS │    │
│     │            │            │              ├───────► │    │
│     │            │            │              │         │    │
│                                                              │
│  ◄──────────── SECONDS ──────────────────────────────────►  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Time emphasis:** The whole thing happens in SECONDS

---

### Before vs After

**BEFORE (chaos):**
```
    ┌─────┐
    │PHONE│
    └──┬──┘
       │
    ┌──▼──┐     ┌─────────┐
    │KELSEY├────► TEXT    │
    └──┬──┘     └────┬────┘
       │             │
       ▼             ▼
    ┌─────┐     ┌────────┐
    │CALL │     │ LOST   │
    │ALYSSA│    │ INFO   │
    └─────┘     └────────┘

    PROBLEM: Things get lost!
```

**AFTER (organized):**
```
    ┌─────┐
    │PHONE│
    └──┬──┘
       │
    ┌──▼──┐
    │ QUO │ (records everything)
    └──┬──┘
       │ (automatic)
    ┌──▼─────┐
    │ JOBBER │ (has everything)
    └──┬─────┘
       │ (notification)
    ┌──▼────┐
    │ALYSSA │ (sees immediately)
    └───────┘

    RESULT: Nothing gets lost!
```

---

## System Icons

When showing these in the video, use these visual ideas:

| System | Icon Idea | Color |
|--------|-----------|-------|
| Jobber | Calendar or clipboard | Blue |
| Quo | Phone with soundwaves | Gray/White |
| N8N | Flowchart/connected dots | Orange |
| Slack | Chat bubble | Purple |
| AI | Brain or lightbulb | Teal |

---

## Animation Ideas

### For the main flow:
1. Show phone ringing (customer calls)
2. Arrow moves to Quo (recording)
3. Arrow moves to AI (processing)
4. Arrow moves to Jobber (task created)
5. Arrow moves to team (notification)
6. Show "3 seconds" timer

### For before/after:
1. Start with chaos diagram (things flying around)
2. Transition to organized diagram (clean flow)
3. Show checkmark (success)

---

## Screenshot Checklist

| System | Screen Needed | Status |
|--------|---------------|--------|
| Jobber | Request queue | [ ] NEED |
| Jobber | Job schedule | [ ] NEED |
| Quo | Call transcript | [ ] NEED |
| Quo | AI summary | [ ] NEED |
| N8N | Workflow diagram | [ ] NEED |
| Slack | Alert example | [ ] NEED |

**Important rules for screenshots:**
- Use DEMO data (not real customer names)
- BLUR any API keys or passwords
- BLUR any phone numbers or emails

---

## Terminology Translation

| Technical Word | Simple Meaning |
|----------------|----------------|
| Workflow | Steps that happen automatically |
| Integration | Two apps talking to each other |
| Transcription | Writing down what someone said |
| API | How computer programs talk to each other |
| Webhook | Instant notification between systems |
| Request | A new task or customer question |
| Queue | A list of things waiting to be done |

---

## Questions?

If you need screenshots or do not understand what something looks like, please ask.
