# Option 4c: Quo + Email Automation (Recommended Approach)

**Project:** Plotter Mechanix Phase 1 Quick Win Sprint
**Date:** December 23, 2025
**Status:** Recommended - Pending Testing Validation

---

## Executive Summary

**Goal:** Make Jobber the trusted source of truth by automating communication capture from calls, texts, and emails into Jobber Requests - eliminating manual screenshot/handoff processes that cause delays and trust erosion.

**Approach:**
1. Use Quo for unified business communications (calls + SMS)
2. Auto-sync all Quo activity to Jobber
3. Automate email → Jobber Request creation
4. Keep current Jobber plan as-is

**Expected Outcome:** Kelsey can check Jobber in the morning and trust that all customer communication from the previous day is captured.

---

## Core Problem (From Client Meetings)

### Current State:

**Kelsey's Quote (Dec 22):**
> "My first instinct is not to go to Jobber and look for the information I need. It's to go into my text messages and my inbox"

**Why?**
> "I don't fully trust that everything is in there"

### Workflow Bottlenecks:

**1. Screenshot Bombing (Highest Volume)**
```
Customer texts Kelsey's personal cell
     ↓
Kelsey screenshots conversation
     ↓
Texts screenshots to Alyssa's office phone (Verizon)
     ↓
"When she comes in, she's getting bombarded with like the inbox,
 all the text messages I sent her"
     ↓
Alyssa manually creates Jobber entry
     ↓
DELAY: Hours to full day
```

**2. Phone Call Handoff (4-6x per day)**
```
Customer calls → Kelsey handles → Kelsey calls Alyssa →
Verbal handoff → Alyssa notes → Jobber entry
DELAY: Requires phone tag, memory issues
```

**3. Email Chaos (206 unread)**
```
Customer emails service@/supplies@/sales@/accounting@
     ↓
Sits in inbox ("Most of it's probably bullshit")
     ↓
Eventually checked (maybe)
     ↓
Manually create Jobber entry
     ↓
DELAY: Can be days, often missed
```

**4. Phone Number Confusion (Dec 23)**
> "All my outbound calls come from my cell phone. They just call me right back and text me on it, and they're all confused. They're like, dude, you got this number, that number, this other number."

---

## Recommended Solution: Option 4c

### Component 1: Quo for Unified Communications

**What It Does:**
- Single business phone number (port Vonage 602-606-XXXX)
- iOS default calling app (Kelsey, Joe, Alyssa all use business number from personal phones)
- Auto-transcribe all calls
- SMS capability (replaces personal cell texting)
- Auto-sync calls + SMS to Jobber

**Solves:**
- ✅ Phone number confusion (single number for all outbound)
- ✅ Screenshot bombing (texts go directly to Quo → Jobber)
- ✅ Call handoff delays (auto-logged to Jobber)
- ✅ Trust issue (calls/texts captured instantly)

**Cost:** ~$69-99/month (3 users)

---

### Component 2: Email → Jobber Automation

**What It Does:**
- N8N workflow monitors email inboxes:
  - service@plottermechanix.com
  - supplies@plottermechanix.com
  - sales@plottermechanix.com
  - accounting@plottermechanix.com
- Auto-creates Jobber Request for each customer email
- Parses: Subject → Title, Body → Notes, Sender → Client lookup/create
- Tags by inbox category

**Solves:**
- ✅ Email chaos (inbox → 0, everything in Jobber)
- ✅ Missed customer requests
- ✅ Manual email checking burden
- ✅ Trust issue (emails captured instantly)

**Cost:** $0 (using existing N8N infrastructure)

---

### Component 3: Keep Jobber As-Is

**What We're NOT Changing:**
- Current Jobber plan ($350-400/mo)
- Jobber texting feature (available if needed)
- Team's existing Jobber workflows
- Any Jobber integrations

**Why:**
- No disruption to what's working
- Kelsey likes Jobber texting UI ("I really like the way it's in Jobber")
- Let data inform future optimization decisions
- Focus on improving input, not changing existing tools

---

## Implementation Timeline

### Pre-Implementation (Completed ✅)
- [x] Quo account created (Kelsey)
- [x] Matthew has Quo access
- [x] Matthew has Jobber access

### Week 1: Testing & Validation (Dec 23-30)

**Testing Objectives:**
1. Validate Quo-Jobber integration quality
2. Determine if Quo SMS syncs to Jobber adequately
3. Test iOS default calling app functionality
4. Assess call transcript quality
5. Document any gaps

**Key Questions to Answer:**
- Does Quo SMS sync to Jobber client records?
- How do Quo summaries appear in Jobber (Request? Client note? Where?)
- Is transcript quality sufficient for Kelsey's needs?
- Does auto-create client work reliably for unknown callers?
- Can team easily access Quo from their phones?

**Testing Plan:**
- Use existing Quo account (already set up)
- Test calls in/out with sample numbers
- Test SMS in/out
- Check Jobber for synced data
- Document results

---

### Week 2: Quo Configuration & Training (Dec 30 - Jan 6)

**Tasks:**
1. Configure Quo call routing (replicate Vonage 5-option IVR):
   - Option 1: Service → Kelsey
   - Option 2: Sales → Kelsey
   - Option 3: Supplies → Alyssa
   - Option 4: Printing → Joe
   - Option 5: Accounting → Nicky (wife)

2. Set up iOS default calling app:
   - Install Quo app on Kelsey's iPhone
   - Configure default calling app setting
   - Test outbound calls show business number
   - Repeat for Joe and Alyssa

3. A2P 10DLC Registration:
   - Begin SMS compliance registration
   - 5-30 day lead time (calls work immediately, SMS requires approval)

4. Team Training:
   - How to use Quo app
   - Where to find call transcripts
   - How calls sync to Jobber

**Deliverables:**
- Configured Quo account
- 3 team members using Quo default calling
- Training documentation

---

### Week 3: Email Automation Build (Jan 6-13)

**Tasks:**
1. Build N8N workflow:
   ```
   Email Monitor (IMAP/Gmail API)
        ↓
   Filter spam (keywords/sender validation)
        ↓
   Parse email content
        ↓
   Jobber API: Create Request
        - Title: Email subject
        - Notes: Email body
        - Client: Lookup or create from sender
        - Tag: Inbox source (service/supplies/sales)
        ↓
   Log success/errors
   ```

2. Spam filtering rules:
   - Common spam keywords
   - Sender domain validation
   - Exclude newsletters/marketing
   - Manual review queue for edge cases

3. Testing:
   - Send test emails to each inbox
   - Verify Jobber Requests created correctly
   - Alyssa reviews quality
   - Refine parsing rules

**Deliverables:**
- N8N workflow operational
- Spam filtering tuned
- Alyssa trained on reviewing auto-created Requests

---

### Week 4: Go-Live & Refinement (Jan 13-20)

**Go-Live Steps:**
1. Port Vonage number to Quo (OR set up call forwarding during transition)
2. Enable email automation (monitored mode)
3. Team switches to Quo for all calls/texts
4. Monitor Request creation quality
5. Daily check-ins with Kelsey/Alyssa

**Success Metrics:**
- [ ] 90%+ calls auto-logged to Jobber within 5 minutes
- [ ] 80%+ emails auto-created as Requests within 15 minutes
- [ ] Kelsey's morning routine: Checks Jobber first
- [ ] Screenshot bombing eliminated
- [ ] Alyssa: 1-2 hours/day saved on manual entry
- [ ] Email inbox: <20 unread (down from 206)

**Refinement:**
- Tune email parsing based on real data
- Adjust Quo routing if needed
- Add missing scenarios
- Document edge cases

---

## Cost Analysis

### Current State Costs:
- Jobber: $350-400/mo (includes texting)
- Vonage: $??/mo (unknown)
- **Total Current: $350-400+ (Vonage cost unknown)**

### With Option 4c:
- Jobber: $350-400/mo (unchanged)
- Quo: $69-99/mo (3 users, annual billing)
- Vonage: $0 (eliminated)
- N8N: $0 (existing infrastructure)
- **Total With Option 4c: $420-500/mo**

### Net Cost Impact:
- **Net Increase: Depends on Vonage cost**
- If Vonage = $50/mo → Net +$20-50/mo
- If Vonage = $100/mo → Net -$30 to +$0/mo

### ROI Calculation (Conservative):
**Time Savings:**
- Alyssa: 1.5 hrs/day × 20 days = 30 hrs/mo @ $25/hr = $750/mo
- Kelsey: 0.5 hrs/day × 20 days = 10 hrs/mo @ $100/hr = $1,000/mo
- **Total Value: $1,750/mo**

**Cost of Option 4c:** ~$70-100/mo net increase
**ROI: 17-25x return on investment**

---

## Key Open Questions (Must Answer During Testing)

### Critical Path Questions:

**1. Quo-Jobber SMS Sync Quality**
- ❓ Do SMS messages sent via Quo appear in Jobber client records?
- ❓ Where do they appear? (Request? Client note? Timeline?)
- ❓ Is the sync reliable (100% capture rate)?
- ❓ What is the delay? (Real-time? Minutes? Hours?)

**Decision Impact:** If SMS doesn't sync well, may need to keep Jobber texting as primary

---

**2. Quo Call Summary Quality**
- ❓ How accurate are the AI-generated call summaries?
- ❓ Do they capture action items or just transcribe?
- ❓ Are they useful for Alyssa to convert to Jobs/Quotes?
- ❓ Can summaries be edited/improved?

**Decision Impact:** Determines if manual review/editing is needed

---

**3. Quo-Jobber Request Creation**
- ❓ Does Quo auto-create Jobber Requests for unknown callers?
- ❓ What triggers Request creation? (Unknown number? Every call? Config option?)
- ❓ Are placeholder client records created properly?
- ❓ Can we control what creates a Request vs just logs to existing client?

**Decision Impact:** May need custom N8N workflow if native behavior isn't right

---

**4. iOS Default Calling App Functionality**
- ❓ Does Quo app support iOS default calling app setting?
- ❓ Does it work reliably? (Calls always route through Quo?)
- ❓ What's the UX? (Extra steps? Friction?)
- ❓ Does it work on all 3 team members' phones (iOS versions)?

**Decision Impact:** This is critical for "single number" goal - if doesn't work, major problem

---

**5. Email Parsing Accuracy**
- ❓ What's the spam-to-real-customer ratio in those 206 emails?
- ❓ Can we reliably detect spam vs legitimate requests?
- ❓ What edge cases exist? (Quotes in PDFs, forwarded emails, etc.)
- ❓ How many emails/day per inbox?

**Decision Impact:** Determines if automation adds value or creates noise

---

**6. A2P 10DLC Timeline**
- ❓ Exact lead time for Plotter Mechanix registration?
- ❓ Can we use calls immediately while SMS approval pending?
- ❓ Any business verification requirements?
- ❓ Backup plan if rejected/delayed?

**Decision Impact:** Affects go-live timeline, may need phased rollout

---

**7. Number Porting vs Forwarding**
- ❓ Should we port Vonage 602 number to Quo permanently?
- ❓ Or set up call forwarding initially (safer, reversible)?
- ❓ What's porting timeline? (Days? Weeks?)
- ❓ Risk of downtime during port?

**Decision Impact:** Porting = permanent, forwarding = test mode

---

**8. Current Vonage Cost**
- ❓ Exact monthly Vonage bill?
- ❓ Contract? Cancellation fees?
- ❓ When does billing cycle renew?

**Decision Impact:** Determines true net cost and optimal timing

---

**9. Team Adoption Risk**
- ❓ Will Joe (shy, not great communicator) adopt Quo app?
- ❓ Will Alyssa trust auto-created Requests or keep checking email?
- ❓ Will Kelsey actually stop using personal cell for texts?

**Decision Impact:** Best tech won't work if team doesn't use it

---

**10. Jobber Texting Redundancy Decision**
- ❓ After testing Quo SMS, does Kelsey prefer Quo or Jobber texting UI?
- ❓ Is there value in keeping both options available?
- ❓ What's the cost to remove Jobber texting feature? (Downgrade option? Savings?)

**Decision Impact:** Phase 2 optimization opportunity, not Phase 1 blocker

---

## Testing Protocol (Week 1 Priority)

### Test 1: Quo SMS → Jobber Sync
**Steps:**
1. Send SMS from Quo to test number (your phone or team member)
2. Check Jobber for synced message
3. Document: Where appears? How long delay? Quality?
4. Repeat with inbound SMS

**Success Criteria:** SMS appears in Jobber client record within 5 minutes

---

### Test 2: Quo Call → Jobber Sync
**Steps:**
1. Make test call from Quo
2. Talk for 2-3 minutes (simulate customer call)
3. Check Jobber for call log + transcript/summary
4. Evaluate summary quality

**Success Criteria:** Call logged with useful summary within 5 minutes

---

### Test 3: Unknown Caller → Jobber Request
**Steps:**
1. Call Quo number from unknown number (not in Jobber)
2. Leave voicemail or brief message
3. Check if Jobber Request created automatically
4. Verify client record created

**Success Criteria:** Request auto-created, placeholder client exists

---

### Test 4: iOS Default Calling App
**Steps:**
1. Install Quo app on test iPhone
2. Set Quo as default calling app (Settings → Apps → Phone)
3. Make outbound call using native phone dialer
4. Verify recipient sees Quo business number (not personal cell)

**Success Criteria:** Business number displays on caller ID

---

### Test 5: Email Parsing
**Steps:**
1. Send test emails to service@/supplies@/sales@
2. Include: Normal request, spam, edge cases
3. Run N8N workflow (once built)
4. Check Jobber Requests created

**Success Criteria:** Real requests captured, spam filtered

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Quo SMS doesn't sync to Jobber | Medium | High | Keep Jobber texting, use Quo for calls only |
| iOS default calling doesn't work | Low | Critical | Fall back to manual Quo app usage |
| Email automation creates spam Requests | Medium | Medium | Strict filtering + Alyssa review queue |
| Team doesn't adopt new system | Medium | High | Training + make easier than old way |
| A2P 10DLC delayed >30 days | Medium | Medium | Use calls only, SMS later |
| Number porting downtime | Low | High | Test with call forwarding first |
| Quo-Jobber integration breaks | Low | Critical | Monitor daily, fallback to manual |

---

## Success Criteria (30-Day Validation)

### Quantitative:
- [ ] 90%+ communication auto-captured in Jobber
- [ ] Kelsey checks Jobber first (not texts/email) 5+ days/week
- [ ] Screenshot handoffs eliminated (0 per week)
- [ ] Phone call handoffs reduced 80% (1-2 per day max)
- [ ] Email inbox <20 unread (down from 206)
- [ ] Alyssa saves 1+ hours/day on manual entry

### Qualitative:
- [ ] Kelsey: "I trust Jobber has everything"
- [ ] Alyssa: "Morning routine is faster, less chaotic"
- [ ] Joe: "I know where to check for my jobs"
- [ ] Customers: No confusion about phone numbers

### Technical:
- [ ] Quo-Jobber sync reliability >95%
- [ ] Call transcripts useful quality
- [ ] Email automation accuracy >80% (real vs spam)
- [ ] iOS default calling works for all 3 users
- [ ] No major system downtime

---

## Decision Points

### Go/No-Go Decision (End of Week 1 Testing):

**GO if:**
- Quo SMS syncs to Jobber adequately (or Jobber texting is acceptable fallback)
- iOS default calling works
- Call transcripts are useful
- No critical blockers discovered

**NO-GO if:**
- Quo-Jobber integration fundamentally broken
- iOS default calling doesn't work (can't solve phone number problem)
- Cost exceeds expected by >50%
- Team strongly resists (Kelsey veto)

---

### Phase 2 Opportunities (Post 30-Day Success):

**If Option 4c works well, consider:**
1. Add Jobber Receptionist for call screening ($99/mo)
2. Evaluate Jobber plan optimization (if Quo SMS replaces Jobber texting)
3. ChatGPT MCP integration (Kelsey voice queries)
4. Advanced email rules (auto-assign by keywords)
5. Personal cell forwarding (eliminate duplicate numbers entirely)

**Data to collect during Phase 1:**
- Call volume by type (service vs sales vs supplies)
- Email volume by inbox (real vs spam ratio)
- Request → Job conversion rate
- Kelsey's actual usage patterns

---

## Related Documentation

- [Kelsey Onboarding Meeting (Dec 22)](../meetings/2025-12-22-kelsey-onboarding/) - Original workflow descriptions
- [Internal Team Meeting (Dec 22)](../meetings/2025-12-22-post-onboarding-team-review/) - Tool evaluation
- [Client Meeting (Dec 23)](../meetings/2025-12-23-client-meeting/) - Phone number problem, costs
- [Process Map](../audit/process-map.md) - Current state workflows
- [Kelsey's Jobber Workflow](../audit/kelsey-jobber-workflow.md) - How he uses Jobber today

---

**Next Steps:**
1. Week 1 Testing (answer the 10 critical questions)
2. Document findings
3. Make go/no-go decision
4. Proceed with implementation or pivot

**Status:** Ready to begin testing (Quo + Jobber access confirmed)
