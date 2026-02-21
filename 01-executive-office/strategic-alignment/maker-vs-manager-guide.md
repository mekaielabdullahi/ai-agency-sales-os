# Maker vs Manager Time: The Productivity Protection Guide

**Created:** January 11, 2026
**Purpose:** Protect developer productivity while maintaining team alignment
**Inspired by:** Paul Graham's "Maker's Schedule, Manager's Schedule" + Alex Hormozi's time block concepts

---

## The Core Problem

Makers and Managers have fundamentally different productivity profiles:

| | Managers | Makers |
|--|---------|--------|
| **Work unit** | 15-30 minute blocks | 4-hour blocks |
| **Blocks per week** | ~80 blocks (15 min each) | ~10 blocks (4 hrs each) |
| **Meeting cost** | 1 block (15-30 min) | 1 full block (4 hrs) |
| **Context switch cost** | Low (designed for it) | Catastrophic |
| **Productivity mode** | Coordination | Deep work |

**The math that kills agencies:**
- A 30-minute meeting costs a manager 1/80th of their week (1.25%)
- A 30-minute meeting costs a maker 1/10th of their week (10%)
- But worse: that meeting fragments a 4-hour block into two 1.5-hour pieces
- Neither fragment is long enough for deep work
- Net maker productivity loss: 25-40% from a single "quick sync"

---

## Our Team Structure

### Managers (Coordination Mode)
- **Chris Andrade** - Lead flow, relationships, networking
- **Mekaiel Abdullahi** - Client comms, PRD, change management

### Makers (Deep Work Mode)
- **Matthew Kerns** - Production development, code review, architecture
- **Trent Christopher** - Technical design, production development, Notion systems

---

## The Weekly Math

### Manager Week (Chris + Mekaiel)
```
80 × 15-minute blocks = 20 hours coordination capacity

Spend on:
- Client check-ins (10-15 blocks)
- Internal syncs (5-10 blocks)
- Lead calls (10-20 blocks)
- Admin/planning (10-15 blocks)
- Buffer for chaos (20-30 blocks)

Meetings ARE the work.
```

### Maker Week (Matthew + Trent)
```
10 × 4-hour blocks = 40 hours deep work capacity

Spend on:
- Development (7-8 blocks = 28-32 hrs)
- Code review (1 block = 4 hrs)
- Technical design (1 block = 4 hrs)
- Sync time (0.5 blocks = 2 hrs MAX)

Meetings DESTROY the work.
```

---

## The Daily Structure

### For Makers (Matthew + Trent)

```
DAY STRUCTURE - MAKERS
======================

07:00-07:30  |  Morning standup (async or 15-min sync)
             |  Check priorities, blockers, daily goal
             |
07:30-11:30  |  ████████ DEEP WORK BLOCK 1 ████████
             |  NO meetings, NO Slack, NO interruptions
             |  Phone on DND, notifications off
             |
11:30-12:00  |  Mid-day sync window (if needed)
             |  Quick questions, unblock issues
             |
12:00-13:00  |  Lunch + break
             |
13:00-17:00  |  ████████ DEEP WORK BLOCK 2 ████████
             |  NO meetings, NO Slack, NO interruptions
             |
17:00-17:30  |  End-of-day sync window
             |  Status update, tomorrow's priorities
             |
17:30+       |  Personal time / overflow if needed
```

**Non-negotiable rules for makers:**
1. Maximum 2 sync windows per day (30 min each)
2. Minimum 2 uninterrupted 4-hour blocks per day
3. All meetings scheduled AT LEAST 24 hours in advance
4. Emergency interruptions only for production fires

---

### For Managers (Chris + Mekaiel)

```
DAY STRUCTURE - MANAGERS
========================

07:00-07:30  |  Morning standup with makers
             |  Set daily priorities, identify blockers
             |
07:30-12:00  |  Meeting blocks (as needed)
             |  Client calls, lead calls, internal syncs
             |  CAN interrupt, CAN context switch
             |
12:00-13:00  |  Lunch + break
             |
13:00-17:00  |  Meeting blocks (as needed)
             |  Admin, documentation, planning
             |
17:00-17:30  |  End-of-day sync with makers
             |  Status check, tomorrow prep
             |
17:30+       |  Async follow-ups, planning
```

**Manager responsibilities toward makers:**
1. Shield makers from client chaos
2. Batch questions - don't ping throughout the day
3. Schedule meetings in maker sync windows ONLY
4. Treat maker time as sacred and expensive

---

## The Communication Protocol

### Async-First (Default Mode)

```
ASYNC COMMUNICATION RULES
=========================

Default channel: Slack / Notion comments
Expected response time: 4-8 hours (within next sync window)

Good async message:
"@Matthew - When you get to your next sync window, can you clarify
how the inventory API should handle duplicate SKUs? No rush,
tomorrow is fine. Context: [link to PRD section]"

Bad async message:
"@Matthew - Quick question, you there?"
"@Matthew - ?"
"@Matthew - Need this ASAP"
```

### Sync Windows (Scheduled)

```
SYNC WINDOW SCHEDULE
====================

Morning sync:    07:00-07:30 (all team, daily)
Mid-day window:  11:30-12:00 (makers available, managers can use)
End-of-day:      17:00-17:30 (all team, daily)

Meetings with makers: ONLY during sync windows
Meetings between managers: Anytime (within each other's availability)
```

### Emergency Protocol (Rare)

```
EMERGENCY INTERRUPTION CRITERIA
===============================

Qualifies as emergency:
- Production system down affecting client operations
- Client threatening to cancel contract TODAY
- Legal/compliance issue requiring immediate response

Does NOT qualify:
- Client asked a question
- Feature request came in
- "Quick question" about anything
- Scope clarification needed
- Status update requested

Emergency channel: Phone call / SMS
If it's not worth a phone call, it's not an emergency.
```

---

## Meeting Guidelines

### Meetings Makers Should Attend

| Meeting Type | Frequency | Duration | Purpose |
|--------------|-----------|----------|---------|
| Daily standup | Daily | 15 min | Alignment, blockers |
| Weekly planning | Weekly | 60 min | Sprint planning |
| Technical review | As needed | 60 min | Architecture decisions |
| Client demos | Per milestone | 30-60 min | Delivery handoff |

**Total maker meeting time: 3-5 hours/week MAX**

### Meetings Makers Should NOT Attend

| Meeting Type | Who Attends Instead |
|--------------|---------------------|
| Client check-ins | Mekaiel |
| Lead qualification calls | Chris/Trent |
| Audit presentations | Mekaiel + Trent |
| Scope discussions | Mekaiel |
| Status update calls | Mekaiel |

---

## The Shield Protocol (Mekaiel's Role)

Mekaiel acts as the shield between clients and developers:

```
CLIENT REQUEST FLOW
===================

Client has question/request
        ↓
Goes to Mekaiel (NOT to devs)
        ↓
Mekaiel evaluates:
├── Within SOW? → Document, add to backlog
├── Out of scope? → Change request process
├── Needs dev input? → Queue for next sync window
└── True emergency? → Interrupt (rare)
        ↓
Devs receive batched, prioritized items
(not random pings throughout the day)
```

**What Mekaiel says to clients:**
- "I'll get an answer from the dev team and get back to you by [specific time]"
- "Let me document this and make sure it's in our backlog"
- "This sounds like a scope change - let me walk you through our process"

**What Mekaiel does NOT say:**
- "Let me ping Matthew real quick"
- "I'll add the devs to this call"
- "Can you send that question directly to Trent?"

---

## Time Blocking Templates

### Matthew's Ideal Week

| Day | Block 1 (AM) | Block 2 (PM) | Meetings |
|-----|--------------|--------------|----------|
| Mon | S&S Wolf dev | S&S Wolf dev | Standup, EOD sync |
| Tue | S&S Wolf dev | Code review | Standup, EOD sync |
| Wed | S&S Wolf dev | S&S Wolf dev | Standup, Weekly planning |
| Thu | S&S Wolf dev | S&S Wolf dev | Standup, EOD sync |
| Fri | S&S Wolf dev | Buffer/overflow | Standup, EOD sync |
| Sat | Client delivery push | Buffer | Minimal |
| Sun | Rest/planning | Rest | None |

**Weekly: 8-9 deep work blocks (32-36 hours development)**

### Trent's Ideal Week

| Day | Block 1 (AM) | Block 2 (PM) | Meetings |
|-----|--------------|--------------|----------|
| Mon | Plotter dev | Plotter dev | Standup, EOD sync |
| Tue | Plotter dev | Technical design | Standup, EOD sync |
| Wed | Plotter dev | Plotter dev | Standup, Weekly planning |
| Thu | Plotter dev | Plotter dev | Standup, EOD sync |
| Fri | Plotter dev | Client demo prep | Standup, EOD sync |
| Sat | Client delivery push | Buffer | Minimal |
| Sun | Rest/planning | Rest | None |

**Weekly: 8-9 deep work blocks (32-36 hours development)**

---

## Productivity Metrics to Track

### For Makers
- Deep work blocks completed per week (target: 8+)
- Uninterrupted blocks (no mid-block interruptions)
- Features/deliverables shipped
- Code commits per week

### For Managers
- Maker interruptions caused (target: minimal)
- Client questions resolved without dev involvement
- Meetings scheduled within sync windows
- Blockers removed for makers

---

## The Contract

### Makers Commit To:
1. Being available during sync windows (daily)
2. Providing clear status updates
3. Flagging blockers immediately
4. Honoring committed deliverables

### Managers Commit To:
1. Protecting maker deep work blocks
2. Batching questions to sync windows
3. Shielding makers from client chaos
4. Scheduling meetings with 24hr+ notice

### Everyone Commits To:
1. Respecting the schedule
2. Communicating async-first
3. Using emergency protocol only for true emergencies
4. Celebrating shipped work, not busy work

---

## Red Flags to Watch

**Maker red flags:**
- Attending >5 hours of meetings per week
- Context switching >3 times per deep work block
- Reporting feeling "behind" despite long hours
- Zero shipped features despite "being busy"

**Manager red flags:**
- Pinging makers during deep work blocks
- Scheduling "quick calls" without notice
- Adding makers to client calls unnecessarily
- Creating urgency for non-urgent items

**Team red flags:**
- All-hands meetings exceeding 2 per week
- "Alignment" meetings with no clear outcome
- More time planning than doing
- Audit/systems work exceeding delivery work

---

## Implementation Checklist

### Immediate (Today)
- [ ] All team members read this guide
- [ ] Calendar blocking for deep work blocks
- [ ] Sync windows added to shared calendar
- [ ] Emergency contact protocol documented

### This Week
- [ ] First week of new schedule
- [ ] Track interruptions (makers log them)
- [ ] Managers practice batching questions
- [ ] Review at end of week

### Ongoing
- [ ] Weekly review of maker productivity
- [ ] Adjust sync windows as needed
- [ ] Celebrate shipped deliverables
- [ ] Hold boundaries firmly

---

## The Bottom Line

**Makers make. Managers manage. The boundaries protect everyone.**

A maker who attends too many meetings becomes an expensive, frustrated coordinator.
A manager who doesn't shield makers becomes an interruption generator.

The agency wins when:
- Makers ship 30+ hours of development per week
- Managers handle 100% of client chaos
- Everyone syncs briefly, consistently, and purposefully

---

*"The best thing a manager can do for makers is leave them alone—except when they need to be unblocked."*

*Next: See `prioritization-plan-jan-2026.md` for how to implement this starting today.*
