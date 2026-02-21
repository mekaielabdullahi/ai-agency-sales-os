# Proposal Follow-Up Sequence

**Stage:** 4 - Implementation Proposal
**Touchpoints:** #17, #18
**Type:** Email
**Automation:** Auto-send (triggered if no response to proposal)

---

## Purpose

Follow up with prospects who received the implementation proposal but haven't responded.

---

## Follow-Up #1

**Trigger:** No response to proposal email
**Timing:** [TBD]

```
Subject: RE: Implementation Proposal for [Company Name]

Hey [First Name],

Just checking in on the proposal.

Any questions or concerns I can address? Sometimes these decisions need a conversation, so happy to hop on a quick call.

[Signature]
```

---

## Follow-Up #2

**Trigger:** No response to Follow-Up #1
**Timing:** [TBD]

```
Subject: RE: Implementation Proposal for [Company Name]

[First Name],

Wanted to follow up one more time.

I know these decisions take time. If there's something specific holding you back - budget, timing, scope - I'd rather know so we can address it.

And if now just isn't the right time, that's okay too. Just let me know.

[Signature]
```

---

## Objection Response Templates

### "Too expensive"
```
I hear you. Let me ask - what would need to be true for this investment to feel like a no-brainer?

You mentioned the current problem is costing you [$ amount] per month. This solution pays for itself in [X months] based on those numbers.

Would it help to phase the implementation differently?
```

### "Need to think about it"
```
Of course - it's a big decision.

What would help you feel more confident? More case studies? A call with an existing client? Different scope?

Happy to provide whatever you need.
```

### "Bad timing"
```
Totally understand. When would be a better time to revisit this?

I'll set a reminder to follow up then. In the meantime, the audit deliverables are yours to keep.
```

---

## Automation Rules

| Trigger | Action | Timing |
|---------|--------|--------|
| No response to proposal | Send Follow-Up #1 | TBD |
| No response to Follow-Up #1 | Send Follow-Up #2 | TBD |
| No response to Follow-Up #2 | Alert sales, move to nurture | Immediate |
| Response received | Stop sequence | Immediate |
| Contract signed | Stop sequence, trigger Stage 5 | Immediate |
