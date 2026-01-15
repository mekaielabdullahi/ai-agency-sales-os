# Internal PRD Review Meeting
**Date:** January 5, 2026
**Time:** 9:21 AM - 9:59 AM EST
**Type:** Slack Huddle
**Attendees:** Matthew Kerns, Trent, Mekaiel Abdullahi, Chris Andrade

---

## Meeting Purpose
Review and refine Phase 1 PRD for Plotter Mechanix communication control system.

---

## Key Discussion Points

### 1. Phase 1 Guiding Principle
**Critical:** Don't make anything worse than the current experience.
- Avoid "bad updates" that need to be fixed
- Even if processes change and have friction, must demonstrate how it's better
- This is the single point of failure for the project

### 2. Quo Pricing & Costs
- Sona (voice agent) costs credits per call answered
- Can do routing WITHOUT Sona (traditional IVR menu routing)
- **Recommendation:** Phase 1 uses routing only; Phase 2 adds Sona for call handling
- Need to confirm voicemail-only line costs

### 3. Number Porting Timeline
- 5-30 days once initiated
- No control over exact switch date
- **Critical:** New system must be ready BEFORE porting completes
- Will receive email updates on porting status/stages
- Vonage access requires 2FA text to Kelsey

### 4. Internal Handoff Solutions Discussed

#### Option A: Voicemail-Only Quo Line
- Single point of intake
- Auto-transcribe voicemails → Jobber Request
- Potentially free (needs validation)
- Concern: Phone friction (dial, wait, speak)

#### Option B: ChatGPT Integration
- Kelsey already uses ChatGPT
- Build custom tool that sends to Jobber
- Two taps and already listening
- Less friction than phone call
- Adds third tool but may be easier

**Consensus:** Investigate voicemail-only line first, keep ChatGPT option in back pocket.

### 5. Request Inbox Volume Concern
- Current: Phone calls + back-and-forth with Kelsey
- New: Large volume of Jobber Requests to process
- Question: How do Jobber requests get marked "done"?
- Possible solution: Provide "suggested updates" to help Alyssa process volume

### 6. Pain Quantification
- Confirmed >30 minutes/day lost (likely more)
- 4-6 interruptions/day

### 7. Kelsey's Current Call Transfer Behavior
- Sometimes Kelsey adds Alyssa to client calls (3-way)
- Sets phone aside, lets Alyssa talk to client
- This could be handled by Sona (Phase 2) or routing (Phase 1)

### 8. Contact Handling & Routing
- Quo stores contact info, one-way sync to Jobber
- If Jobber has existing contact, call info attaches to that client
- New contacts: Just phone number, needs manual enrichment
- **To Test:** Can we route based on new vs existing contact?

### 9. 80/20 Approach
- Capture 80% of communications effectively
- Edge cases addressed in later phases
- Focus on bulk first, discover edge cases through usage

---

## Decisions Made

1. **Email automation stays deprioritized** - Phone/SMS is the active channel
2. **Phase 1 = Routing only** - No Sona credit costs
3. **Phase 2 = Sona replaces Alyssa for call handling**
4. **Manual processing is OK** - Requests inbox is staging area
5. **Provide SOPs** for manual processing (ChatGPT copy-paste workflow)

---

## Action Items

| Owner | Action | Priority |
|-------|--------|----------|
| Matthew | Update PRD with meeting insights | P0 |
| Matthew | Validate voicemail-only Quo line costs | P1 |
| Team | Test Quo contact handling (new vs existing) | P1 |
| Team | Investigate ChatGPT integration as alternative | P2 |
| Team | Define how Jobber Requests get marked "done" | P1 |
| Team | Research Vonage IVR options to replicate | P1 |

---

## Open Questions (for follow-up)

1. What are the exact 5 Vonage IVR options to replicate?
2. Cost of voicemail-only Quo line?
3. Can Quo route based on contact status (new vs existing)?
4. How will Alyssa process increased Request volume efficiently?
