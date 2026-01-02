# Quo + Jobber + Sona Integration Setup

**Created:** December 28, 2025
**Status:** Testing (7-day trial period)

---

## Overview

Set up a three-tool integration stack for Plotter Mechanix to automate inbound call handling and lead capture:

1. **Quo** - Business phone system with free trial
2. **Jobber** - Field service management platform
3. **Sona** - AI call recording and transcription

---

## Setup Details

### Quo (Business Phone)
- **Purpose:** Dedicated business phone number
- **Status:** 7-day free trial active
- **Key Feature:** AI call tagging (to be tested during trial)
- **Next Step:** Initiate A2P registration for SMS capability

### Jobber
- **Purpose:** Field service management, job tracking, customer records
- **Status:** Connected to Quo
- **Integration:** Uses same email account as Quo for connection

### Sona (AI Transcription)
- **Purpose:** Call recording, transcription, and summarization
- **Status:** Active and connected
- **Output:**
  - Transcript → Jobber request notes
  - Summary → Jobber request

---

## How It Works

```
INBOUND CALL (via Quo number)
        ↓
SONA RECORDS CALL
        ↓
SONA TRANSCRIBES + SUMMARIZES
        ↓
TRANSCRIPT → JOBBER REQUEST NOTES
SUMMARY → JOBBER REQUEST FIELD
        ↓
TEAM HAS FULL CONTEXT
```

---

## Integration Requirements

- **Email Consistency:** Both Quo and Jobber must use the same email address for integration to work
- **Sona Configuration:** Point output to Jobber's request intake

---

## Trial Period Focus (7 Days)

### Must Test:
- [ ] AI call tagging feature in Quo
- [ ] Transcript accuracy for printer repair terminology
- [ ] Summary quality and relevance
- [ ] Speed of data appearing in Jobber
- [ ] Notification workflow for incoming requests

### Document:
- [ ] What works well
- [ ] What needs adjustment
- [ ] Value delivered for Plotter Mechanix workflow

---

## A2P Registration

**Status:** Should be initiated immediately
**Purpose:** Enable SMS messaging from Quo business number
**Timeline:** Waiting game once initiated - no downside to starting early
**Benefit:** Text-based customer communication and status updates

---

## Opportunities This Enables

### Immediate Value
1. Never miss call details - everything transcribed
2. Customer context available before callbacks
3. Reduced "what did they say again?" friction

### With AI Call Tagging (Testing This Week)
1. Auto-categorize call types (service request, quote, status check)
2. Priority flagging for urgent issues
3. Pattern recognition across call volume
4. Analytics on call reasons and frequency

---

## Next Steps

1. **This Week:** Test the integration with real calls
2. **Document:** What patterns emerge from AI call tagging
3. **A2P:** Initiate registration now
4. **End of Trial:** Decide on continued subscription

---

*Integration designed to support Phase 1: Communication Hub*
