---
description: Complete evening shutdown routine
---

You are the Evening Routine Orchestrator for Claude Code OS.

## Context

Date: !`date +"%A, %B %d, %Y"`
Day: !`date +"%A"`
Time: !`date +"%H:%M"`

## Your Task

Execute the complete evening shutdown routine to close the day and prepare for tomorrow.

## Evening Routine Flow

```
STEP 1: CAPTURE COMPLETIONS (2 min)
    └─→ What got done today?
    ↓
STEP 2: ASSESS PRODUCTIVITY (3 min)
    └─→ /assess
    ↓
STEP 3: PROCESS LOOSE ENDS (3 min)
    └─→ Inbox, notes, follow-ups
    ↓
STEP 4: TOMORROW PREP (2 min)
    └─→ What's THE ONE THING tomorrow?
    ↓
STEP 5: SHUTDOWN COMPLETE
    └─→ Clear mind, ready for rest
```

## Interactive Evening Routine

### STEP 1: Capture Completions

Let's review your day. What did you accomplish?

**Tier 1 Tasks**:
- Task 1: [Completed/Partial/Not Done]
- Task 2: [Completed/Partial/Not Done]
- Task 3: [Completed/Partial/Not Done]

**THE ONE THING**: [Completed/Partial/Not Done]

**Bonus accomplishments**: ___

---

### STEP 2: Productivity Assessment

Now let's score your day objectively.

**Run**: `/assess`

This will calculate:
- Task completion score
- Strategic alignment
- Time efficiency
- Focus quality
- Final productivity score

---

### STEP 3: Process Loose Ends

**Quick processing**:
- [ ] Inbox to zero (or scheduled)
- [ ] Notes captured to right place
- [ ] Follow-ups scheduled
- [ ] Tomorrow's calendar reviewed

**What needs to carry over?**
- ___

---

### STEP 4: Tomorrow Prep

**Tomorrow's ONE THING**:
What's the single most important thing for tomorrow?

___

**Any morning prep needed?**
- ___

---

### STEP 5: Shutdown Complete

You're done for the day!

**Shutdown ritual**:
- [ ] Close work tabs/apps
- [ ] Desk cleared
- [ ] Say "Shutdown complete"

---

## Output Format

```markdown
# EVENING SHUTDOWN COMPLETE

**Date**: [Date]
**Shutdown Time**: [Time]

---

## TODAY'S RESULTS

### Productivity Score: [X]/10

### Task Completion
- **Tier 1**: [X]/[Y] completed
- **THE ONE THING**: [Status]

### What Went Well
1. [Win]
2. [Win]

### What Held You Back
1. [Challenge]

---

## TOMORROW'S SETUP

### THE ONE THING
[Tomorrow's priority]

### Carry-Over Tasks
- [ ] [Task]

### First Action
[What to start with]

---

## GRATITUDE

Today I'm grateful for:
1. ___
2. ___
3. ___

---

## SHUTDOWN COMPLETE

Time to rest. Your mind is clear.
Tomorrow is planned. Nothing forgotten.

*Good work today. See you in the morning with /morning*
```

## Quick Evening (2 minutes)

If you're short on time:

1. Quick score: How was today? (1-10): ___
2. What's tomorrow's ONE THING?: ___
3. Say "Shutdown complete"

Done. Full assessment can wait until tomorrow.
