# Internal Development Meeting Summary - January 15, 2026

**Attendees:** Matt, Trent
**Project:** Plotter Mechanix - Phase 1
**Duration:** 7:05 PM - 8:17 PM EST

---

## Key Decisions

- Focus on Quo-to-Jobber parity first, with incremental AI enhancements where easy
- Delay phone menu system until all lines (Alyssa, Joe, Kelsey) are set up and port completes
- Disable Sona AI answering to preserve Quo credits (300/1000 used, 100 credits per Sona call)
- Kelsey's outbound calls to Capsule request → Phase 2 (out of scope)
- Data retention strategy (30-day log cleanup) needs further discussion before handoff

## Action Items

| Owner | Task | Due |
|-------|------|-----|
| Matt | Develop SOP documenting current Quo-Jobber workflow and manual processes | Tonight |
| Trent | Prepare Xigent proposal addendum with graphics (opportunity matrix, ROI calculator, blueprint) | Tomorrow AM |
| Trent | Push latest N8N workflow fixes to main branch | Done |
| Matt/Trent | Contact Denis about Xigent proposal feedback | Before Thursday |
| Matt | Swap HTTP request node with Gemini agent node for AI summary | Next session |

## Technical Details Covered

### N8N Workflow Current State
- **Webhook Setup**: Receives transcript, summary, message received/delivered events from Quo
- **Not using**: completed, ringing, recording events (potential future use for routing)
- **Daily Summary**: Posts to Slack at 6 PM EST (20 transcripts, 12 unique callers example)
- **Error Handling**: Posts to Slack on errors; fixed data type mismatch bug (phone number field expecting number, got text)
- **Debugging Tip**: In N8N executions, click "Debug in Editor" to pin data from any execution for testing

### Workflow Logic Flow
1. Webhook receives event → Parse → Log to table
2. Clean up logs older than 30 days (needs review)
3. If transcript: Extract contact → Search Jobber for client
4. If client exists: get ID; else: create client
5. Search for open requests matching contact
6. (New/Untested) Generate AI summary with Gemini
7. Create new request OR add note to existing request

### Current Gaps in Native Quo-Jobber Integration
- Does NOT capture contact names (shows phone numbers in brackets)
- Does NOT capture voicemails
- Does NOT capture text messages
- Contact suggestions in Quo don't transfer via webhook
- Alyssa must manually: add contacts, convert requests, risk losing call history/notes

### Quo Configuration Notes
- Webhook secret not being used (no authentication on incoming webhooks)
- Allow overages: DISABLED (won't charge beyond 1000 credits)
- Sona call flow is default/out-of-box - should disable to save credits
- Can retry webhook events from Quo's event log for testing
- Phone menu system exists but not useful until all lines are ported

## Plotter Mechanix Operational Context

### Current Call Volume
- ~20 calls/day (36 calls in last 2 days)
- Vonage only had 8 calls in last 3 months (barely used)
- Most calls go to Kelsey directly

### Current Workflow (Kelsey's Instructions)
- All calls go through Quo to Kelsey first
- If rings 4 times, Alyssa picks up
- This is interim until lines for Alyssa/Joe are set up
- Waiting on number port to complete

### Observed Issue
- Alyssa may be converting requests then deleting them → losing call history
- Need SOP to prevent this before they lose more data

## Phase 1 Deliverable Focus

**Core Goal**: Make Quo-to-Jobber work really well
- Reach parity with native integration, then enhance
- If contact info extraction works, also extract printer models from transcripts
- High accuracy is critical - if AI gets names wrong even 3%, Alyssa may double-check every recording anyway

**Success Criteria** (from Kelsey's feedback):
- Contact names properly assigned (not just phone numbers)
- Voicemails captured
- Messages captured
- Call history preserved on converted requests

## Xigent Proposal Follow-up

- Tim needs visuals to sell internally to stakeholders ($30K decision)
- Original proposal had many images, trimmed to just opportunity matrix
- Addendum will add: blueprint/roadmap visual, ROI calculator
- Tim at convention early next week, back Thursday/Friday for follow-up meeting
- Denis sent similar $15K proposal (40K-100K next phase) - worth getting his feedback
- Trent available Thursday/Friday afternoon Eastern for Denis call

## Out of Scope (Phase 2)

- Kelsey's request: outbound calls from Quo → Capsule (received during call)
- Phone menu system implementation
- Additional phone lines for Alyssa/Joe
- Long-term data retention strategy

## Next Steps

1. **Tonight (Matt)**: Document current manual Quo-Jobber workflow as SOP - map what Alyssa does manually, identify what can be automated, note risks
2. **Tomorrow AM (Trent)**: Create proposal addendum with additional visuals, send to Tim before he's in office
3. **This Week**: Continue N8N workflow refinement - swap HTTP node for Gemini agent node, test AI summary accuracy
4. **Before Thursday**: Reach out to Denis for proposal feedback/collaboration
