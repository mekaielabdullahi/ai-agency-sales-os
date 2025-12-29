# Week 1 Testing Checklist - Plotter Mechanix Phase 1

**Objective:** Answer the 10 critical questions before proceeding with full implementation
**Timeline:** Dec 23-30, 2025
**Tester:** Matthew (has Quo + Jobber access)
**Status:** Ready to begin

---

## Pre-Testing Setup

- [x] Quo account created (Kelsey)
- [x] Matthew has Quo access
- [x] Matthew has Jobber access
- [ ] Identify test phone numbers (non-customer numbers for safe testing)
- [ ] Document current Jobber state (baseline for comparison)
- [ ] Set up test email addresses (if needed for email automation testing)

---

## Critical Question 1: Quo-Jobber SMS Sync Quality

**Priority:** CRITICAL (This determines if we can eliminate screenshot bombing)

### Test 1.1: Outbound SMS from Quo
- [ ] Log into Quo
- [ ] Send SMS to test number (your phone or team member)
- [ ] Message content: "Test SMS from Quo - checking Jobber sync"
- [ ] **Check Jobber:**
  - [ ] Where does it appear? (Request? Client note? Timeline? Messages tab?)
  - [ ] How long was the delay? (Record timestamp)
  - [ ] Is message content preserved accurately?
  - [ ] Is sender identified correctly?

**Result:** _____________________

---

### Test 1.2: Inbound SMS to Quo
- [ ] Text the Quo business number from test phone
- [ ] Message content: "Test inbound SMS - customer request"
- [ ] **Check Jobber:**
  - [ ] SMS captured in Jobber?
  - [ ] Where does it appear?
  - [ ] Delay time?
  - [ ] Sender phone number captured?

**Result:** _____________________

---

### Test 1.3: SMS Thread Continuity
- [ ] Send multi-message conversation (3-4 back-and-forth texts)
- [ ] **Check Jobber:**
  - [ ] Does thread appear as conversation or separate messages?
  - [ ] Is order preserved?
  - [ ] Are timestamps accurate?

**Result:** _____________________

---

### Test 1.4: SMS with Image/Photo
- [ ] Send SMS with photo attachment from Quo
- [ ] **Check Jobber:**
  - [ ] Does image sync?
  - [ ] Is image viewable in Jobber?
  - [ ] Quality preserved?

**Result:** _____________________

---

**Decision:** Can Quo SMS replace screenshot bombing? YES / NO / NEEDS_IMPROVEMENT

**Notes:**
_____________________

---

## Critical Question 2: Quo Call Summary Quality

**Priority:** CRITICAL (Determines if auto-logging provides value)

### Test 2.1: Outbound Call with Transcript
- [ ] Make test call from Quo to team member
- [ ] Have 2-3 minute conversation simulating customer call
- [ ] Include: Customer name, issue description, requested service, follow-up needed
- [ ] **Check Jobber after call:**
  - [ ] Call logged automatically?
  - [ ] Transcript available?
  - [ ] Transcript accuracy (rate 1-10): _____
  - [ ] Summary generated?
  - [ ] Summary usefulness (rate 1-10): _____
  - [ ] Action items captured? YES / NO

**Result:** _____________________

---

### Test 2.2: Inbound Call Handling
- [ ] Call Quo business number from test phone
- [ ] Answer via Quo
- [ ] Have conversation (simulate customer issue)
- [ ] **Check Jobber:**
  - [ ] Call logged?
  - [ ] Transcript quality?
  - [ ] Summary quality?
  - [ ] Where does it appear in Jobber UI?

**Result:** _____________________

---

### Test 2.3: Voicemail Transcription
- [ ] Call Quo number, leave voicemail
- [ ] Message content: "Hi, this is John from ABC Printing. My plotter is jammed. Can you come out tomorrow? Call me back at 555-1234"
- [ ] **Check Jobber:**
  - [ ] Voicemail transcribed?
  - [ ] Accuracy?
  - [ ] Action items extracted? (callback, service request)

**Result:** _____________________

---

**Decision:** Are call summaries useful for Alyssa to create Jobs/Quotes? YES / NO / NEEDS_IMPROVEMENT

**Notes:**
_____________________

---

## Critical Question 3: Quo-Jobber Request Creation

**Priority:** HIGH (Determines automation level)

### Test 3.1: Unknown Caller Behavior
- [ ] Call Quo number from phone number NOT in Jobber
- [ ] Leave voicemail or brief message
- [ ] **Check Jobber:**
  - [ ] Request auto-created? YES / NO
  - [ ] Client record created? YES / NO
  - [ ] Client details populated? (phone number, name if said)
  - [ ] Where is Request visible in Jobber UI?

**Result:** _____________________

---

### Test 3.2: Known Client Call
- [ ] Call Quo number from number that EXISTS in Jobber
- [ ] Have conversation
- [ ] **Check Jobber:**
  - [ ] Does it create new Request or just log to existing client?
  - [ ] Is call linked to correct client?
  - [ ] Summary attached to client record?

**Result:** _____________________

---

### Test 3.3: Configuration Options
- [ ] Explore Quo settings for Jobber integration
- [ ] **Document:**
  - [ ] Can we control what triggers Request creation?
  - [ ] Options: Every call? Unknown only? Manual?
  - [ ] Can we customize Request template/fields?
  - [ ] Can we set default Request status?

**Result:** _____________________

---

**Decision:** Does auto-Request creation work well or need custom N8N workflow? NATIVE_WORKS / BUILD_CUSTOM

**Notes:**
_____________________

---

## Critical Question 4: iOS Default Calling App Functionality

**Priority:** CRITICAL (This is the "single number" solution)

### Test 4.1: App Installation & Setup
- [ ] Install Quo app on iPhone (search "Quo" or "OpenPhone")
- [ ] Log in with Plotter Mechanix Quo account
- [ ] Verify business number displays in app

**Result:** App installed successfully? YES / NO

---

### Test 4.2: Default Calling App Setting
- [ ] Go to iPhone Settings → Apps → Phone
- [ ] Look for "Default calling app" option
- [ ] **Check:**
  - [ ] Is Quo available as option? YES / NO
  - [ ] Set Quo as default
  - [ ] Confirm setting saved

**Result:** _____________________

---

### Test 4.3: Outbound Call Test (Native Dialer)
- [ ] Open native iPhone Phone app (NOT Quo app)
- [ ] Dial test number using regular phone dialer
- [ ] **Ask recipient:** What number shows on caller ID?
  - [ ] Quo business number? (SUCCESS)
  - [ ] Personal cell number? (FAIL)
  - [ ] Other number? (INVESTIGATE)

**Result:** _____________________

---

### Test 4.4: Contact Tap Test
- [ ] Add test contact to iPhone contacts
- [ ] Tap contact to call (using native contacts app)
- [ ] **Verify:** Call routes through Quo
- [ ] **Ask recipient:** Caller ID shows business number?

**Result:** _____________________

---

### Test 4.5: UX Friction Assessment
- [ ] **Rate ease of use (1-10):** _____
- [ ] Any extra steps vs normal calling? YES / NO
- [ ] Delay before call connects? (seconds): _____
- [ ] Call quality issues? YES / NO
- [ ] Would Kelsey/Joe/Alyssa adopt this? LIKELY / UNLIKELY

**Result:** _____________________

---

**Decision:** Does iOS default calling solve phone number confusion? YES / NO / PARTIAL

**Notes:**
_____________________

---

## Critical Question 5: Email Parsing Accuracy

**Priority:** HIGH (Determines if email automation adds value or noise)

### Test 5.1: Email Volume Analysis
- [ ] Log into each email inbox:
  - [ ] service@plottermechanix.com
  - [ ] supplies@plottermechanix.com
  - [ ] sales@plottermechanix.com
  - [ ] accounting@plottermechanix.com
- [ ] **Count for each inbox:**
  - [ ] Total unread: _____
  - [ ] Obvious spam: _____
  - [ ] Newsletter/marketing: _____
  - [ ] Real customer requests: _____
  - [ ] Edge cases (forwards, quotes, etc): _____

**Spam-to-real ratio:** _____ % spam

---

### Test 5.2: Sample Email Review
- [ ] Review 10-20 random customer emails
- [ ] **Document patterns:**
  - [ ] Common subject line formats?
  - [ ] Typical request content?
  - [ ] Attachments common? (PDFs, images)
  - [ ] Forwarded emails common?

**Notes:**
_____________________

---

### Test 5.3: Spam Detection Test
- [ ] Identify 5 obvious spam emails
- [ ] **Note spam characteristics:**
  - [ ] Sender domains?
  - [ ] Subject line patterns?
  - [ ] Keywords in body?

**Filtering rules needed:**
_____________________

---

**Decision:** Can we reliably filter spam vs real requests? YES / NO / NEEDS_WORK

**Notes:**
_____________________

---

## Critical Question 6: A2P 10DLC Timeline

**Priority:** MEDIUM (Affects go-live timeline)

### Test 6.1: Registration Status Check
- [ ] Log into Quo admin
- [ ] Check A2P 10DLC registration status
- [ ] **Document:**
  - [ ] Already registered? YES / NO
  - [ ] If not, what info is needed?
  - [ ] Estimated approval timeline: _____
  - [ ] Can calls work before SMS approval? YES / NO

**Result:** _____________________

---

### Test 6.2: SMS Functionality Test (If Not Registered)
- [ ] Try sending SMS from Quo
- [ ] **Check:**
  - [ ] Does it work? YES / NO
  - [ ] Any warnings/errors?
  - [ ] Recipient receives message?

**Result:** _____________________

---

**Decision:** Can we go live with calls before SMS approval? YES / NO

**Timeline impact:** _____________________

---

## Critical Question 7: Number Porting vs Forwarding

**Priority:** MEDIUM (Affects permanence and risk)

### Test 7.1: Current Vonage Setup
- [ ] Document Vonage 602-606-XXXX number details
- [ ] **Check:**
  - [ ] Account owner?
  - [ ] Contract status?
  - [ ] Cancellation fees?
  - [ ] Next billing date?

**Notes:**
_____________________

---

### Test 7.2: Porting Timeline Research
- [ ] Contact Quo support: "How long does number porting take?"
- [ ] **Document:**
  - [ ] Typical timeline: _____ days
  - [ ] What info is needed from Vonage?
  - [ ] Any risk of downtime?
  - [ ] Can we test before committing?

**Result:** _____________________

---

### Test 7.3: Call Forwarding Alternative
- [ ] Check Vonage: Can we forward calls to Quo number?
- [ ] **Benefits:**
  - [ ] Reversible (safer for testing)
  - [ ] No downtime risk
  - [ ] Can revert if issues
- [ ] **Drawbacks:**
  - [ ] May have delay
  - [ ] Additional cost?
  - [ ] Not permanent solution

**Recommendation:** PORT / FORWARD_FIRST / UNCLEAR

**Notes:**
_____________________

---

## Critical Question 8: Current Vonage Cost

**Priority:** MEDIUM (Determines true ROI)

### Test 8.1: Vonage Bill Research
- [ ] Find recent Vonage invoice
- [ ] **Document:**
  - [ ] Monthly cost: $_____
  - [ ] What's included? (users, features)
  - [ ] Contract terms?
  - [ ] When can we cancel?

**Result:** _____________________

---

### Test 8.2: Net Cost Calculation
- [ ] Current monthly total:
  - Jobber: $350-400
  - Vonage: $_____
  - **Total: $_____**

- [ ] With Option 4c:
  - Jobber: $350-400 (unchanged)
  - Quo: $69-99
  - Vonage: $0
  - **Total: $420-500**

- [ ] **Net change: $_____ / month**
- [ ] **Annual impact: $_____ / year**

**Decision:** Cost increase acceptable? YES / NO

---

## Critical Question 9: Team Adoption Risk

**Priority:** HIGH (Best tech fails if not adopted)

### Test 9.1: Kelsey Adoption Assessment
- [ ] Show Kelsey Quo interface
- [ ] Demonstrate iOS default calling
- [ ] **Ask:**
  - [ ] "Would this be easier than screenshotting texts?"
  - [ ] "Can you see yourself using this daily?"
  - [ ] Concerns or hesitations?

**Response:** _____________________

---

### Test 9.2: Alyssa Adoption Assessment
- [ ] Show Alyssa where Quo data appears in Jobber
- [ ] Explain Request review workflow
- [ ] **Ask:**
  - [ ] "Would you trust auto-created Requests?"
  - [ ] "Easier than processing screenshots?"
  - [ ] Concerns?

**Response:** _____________________

---

### Test 9.3: Joe Adoption Assessment
- [ ] Explain Quo app to Joe
- [ ] Demonstrate calling from business number
- [ ] **Ask:**
  - [ ] "Comfortable using this?"
  - [ ] Any concerns?

**Response:** _____________________

---

**Decision:** Will team adopt or resist? WILL_ADOPT / LIKELY_RESIST / MIXED

**Mitigation needed:** _____________________

---

## Critical Question 10: Jobber Texting Redundancy Decision

**Priority:** LOW (Phase 2 consideration, not Phase 1 blocker)

### Test 10.1: Quo vs Jobber Texting UX Comparison
- [ ] Send test text via Quo
- [ ] Send test text via Jobber
- [ ] **Compare:**
  - [ ] Which interface is easier?
  - [ ] Which syncs better?
  - [ ] Which Kelsey prefers?

**Preference:** QUO / JOBBER / NO_PREFERENCE

---

### Test 10.2: Cost to Remove Jobber Texting
- [ ] Research Jobber plans
- [ ] **Check:**
  - [ ] Current plan: _____
  - [ ] Plan without texting: _____
  - [ ] Potential savings: $_____/month

**Note:** This is Phase 2 optimization, not Phase 1 requirement

---

**Decision:** Keep both available for now? YES / NO / DECIDE_LATER

**Notes:**
_____________________

---

## Testing Summary & Go/No-Go Decision

### Critical Questions Summary

| Question | Answer | Status | Blocker? |
|----------|--------|--------|----------|
| 1. Quo SMS syncs to Jobber? | _______ | ✅ / ❌ | YES / NO |
| 2. Call summaries useful? | _______ | ✅ / ❌ | NO |
| 3. Auto-Request creation works? | _______ | ✅ / ❌ | NO |
| 4. iOS default calling works? | _______ | ✅ / ❌ | YES |
| 5. Email spam filterable? | _______ | ✅ / ❌ | NO |
| 6. A2P timeline acceptable? | _______ | ✅ / ❌ | NO |
| 7. Porting vs forwarding? | _______ | ✅ / ❌ | NO |
| 8. Cost acceptable? | _______ | ✅ / ❌ | NO |
| 9. Team will adopt? | _______ | ✅ / ❌ | YES |
| 10. Jobber texting needed? | _______ | ✅ / ❌ | NO |

---

### GO / NO-GO Decision

**GO if:**
- [ ] Quo SMS syncs to Jobber (Q1 = YES)
- [ ] iOS default calling works (Q4 = YES)
- [ ] Team willing to adopt (Q9 = YES)
- [ ] No critical blockers discovered

**NO-GO if:**
- [ ] Quo-Jobber integration fundamentally broken
- [ ] iOS default calling doesn't work
- [ ] Team strongly resists
- [ ] Cost exceeds budget by >50%

---

### Final Recommendation

**Proceed with Option 4c?** YES / NO / MODIFY

**If MODIFY, what changes:** _____________________

**Next steps:** _____________________

---

## Post-Testing Actions

- [ ] Document all findings in testing report
- [ ] Share results with team (Trent, Mekaiel, Chris)
- [ ] Present recommendation to Kelsey
- [ ] Get approval to proceed
- [ ] Begin Week 2 implementation (if GO)

---

**Testing Completed By:** _____________________
**Date:** _____________________
**Sign-off:** _____________________
