# Reply Handling Playbooks
## Positive / Neutral / Negative Reply Workflows

---

## Positive Reply (Respond < 1 Hour)

### Detection
Reply contains interest signals: "interested", "tell me more", "sounds good", "let's talk", asks specific questions about the offer, shares a pain point.

### Response Template

```
[First Name],

Glad to hear it. Here's what I'm thinking:

1. Quick 20-minute call to understand your biggest operational headache
2. I identify one automation that saves you time immediately
3. I build it for free as proof of concept

Here's my calendar: [Calendly link]

Mekaiel
```

### Workflow
1. Respond within 1 hour (speed = conversion)
2. n8n triggers `pre_meeting_sequence.json`
3. If they book: Discovery Call using vertical-specific guide
4. After call: `post_call_followup.json`
5. If qualified: `proposal_assembly.json`
6. Update Google Sheet: Status = "Positive Reply" -> "Call Booked" -> "Proposal Sent" -> "Closed"

### Conviction Score Assignment
After reading the reply, assign a conviction score:

| Score | Meaning | Follow-Up Cadence |
|-------|---------|-------------------|
| 9-10 | "I KNOW we transform this business" | Every 3-4 days, up to 12 touches |
| 7-8 | "Very likely we help significantly" | Every 5-7 days, up to 8 touches |
| 5-6 | "Probably can help" | Every 7-10 days, up to 5 touches |
| 1-4 | "Not sure it's a fit" | 3 touches max, archive |

---

## Neutral Reply

### Detection
Reply is not clearly positive or negative: asks a question without expressing interest, asks "who are you?", asks for more information without enthusiasm, one-word responses like "maybe" or "what is this?".

### Response Approach
1. Acknowledge their reply warmly
2. Answer their specific question
3. Don't push -- provide value
4. Keep it short (3-4 sentences max)

### Example Response

```
Hey [First Name],

Great question -- [answer their specific question].

In short, I help [printing companies / homestead businesses] automate
their backend operations so the owner isn't the bottleneck. Happy to
share more details if helpful, or just let me know if you have other
questions.

Mekaiel
```

### Workflow
1. Respond within 2-4 hours
2. Add to `nurture_sequence.json` (60-day cycle)
3. Update Google Sheet: Status = "Neutral Reply"
4. If they respond positively to the nurture: Escalate to positive reply workflow

---

## Negative Reply

### Detection
Reply contains: "not interested", "unsubscribe", "remove me", "stop emailing", angry tone, profanity.

### Response
**Do not respond.** Or if they asked a direct question:

```
Understood, [First Name]. Removing you now. Apologies for the interruption.

Mekaiel
```

### Workflow
1. Remove from all sequences immediately
2. Update Google Sheet: Status = "Opted Out"
3. **Never contact again** -- add to suppression list
4. Do NOT take it personally -- this is normal

---

## No Reply After Email 4

### Detection
All 4 emails sent, no reply received.

### Workflow
1. Update Google Sheet: Status = "No Reply - Completed"
2. Add to `nurture_sequence.json` (90-day cycle)
3. After 90 days, nurture re-engages with new content/case studies
4. If they respond to nurture: Re-enter active outreach

---

## Out-of-Office / Auto-Reply

### Detection
Auto-reply indicating vacation, leave, etc.

### Workflow
1. Note the return date
2. Update Google Sheet: Status = "OOO - Return [date]"
3. Pause their email sequence
4. Resume sequence 2 days after their return date

---

## Reply Metrics to Track

| Metric | Where to Log |
|--------|-------------|
| Total replies | Google Sheet Dashboard |
| Positive reply % | Google Sheet Dashboard |
| Average response time (ours) | Manual tracking |
| Reply-to-call booking rate | Google Sheet Pipeline |
| Call-to-proposal rate | Google Sheet Pipeline |
| Proposal-to-close rate | Google Sheet Pipeline |

---

## Key Principles

1. **Speed wins.** Positive reply -> respond in < 1 hour. Every hour you wait, conversion drops.
2. **Don't oversell.** The reply is interest, not a commitment. Keep it simple: "Let's hop on a quick call."
3. **Respect the no.** Remove immediately. Zero follow-up. Your reputation depends on it.
4. **Log everything.** Every reply teaches you something about your ICP and copy.
5. **Conviction drives follow-up.** High conviction = more touches. Low conviction = fewer touches. Trust the scoring.
