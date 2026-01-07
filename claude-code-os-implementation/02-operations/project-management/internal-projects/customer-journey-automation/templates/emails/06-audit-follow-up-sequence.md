# Audit Offer Follow-Up Sequence

**Stage:** 2 - Discovery
**Touchpoints:** #11, #12
**Type:** Email
**Automation:** Auto-send (triggered if no response to audit offer)

---

## Purpose

Follow up with prospects who received the audit offer but haven't responded.

---

## Follow-Up #1

**Trigger:** No response to audit offer
**Timing:** [TBD]

```
Subject: RE: AI Audit for [Company Name]

Hey [First Name],

Just checking in on the audit proposal.

Any questions I can answer? Happy to hop on a quick call if that's easier.

[Signature]
```

---

## Follow-Up #2

**Trigger:** No response to Follow-Up #1
**Timing:** [TBD]

```
Subject: RE: AI Audit for [Company Name]

[First Name],

Wanted to follow up one more time on the AI Audit.

If the timing isn't right, totally understand. Just let me know and I'll check back in a few months.

If something's holding you back that I can address, I'm all ears.

[Signature]
```

---

## Automation Rules

| Trigger | Action | Timing |
|---------|--------|--------|
| No response to audit offer | Send Follow-Up #1 | TBD |
| No response to Follow-Up #1 | Send Follow-Up #2 | TBD |
| No response to Follow-Up #2 | Move to nurture | Immediate |
| Response received | Stop sequence | Immediate |
| Invoice paid | Stop sequence, trigger Stage 3 | Immediate |

---

## Notes

- These follow-ups are warmer - they've already had a call
- Focus on removing friction, not re-selling
