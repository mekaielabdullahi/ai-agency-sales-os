# Plotter Mechanix - Internal Team Meeting
**Date:** December 22, 2025
**Time:** 1:16:59 PM - 3:30:52 PM EST
**Type:** Internal Team Analysis
**Attendees:** Matthew Kerns, Trent Christopher, Mekaiel Abdullahi, Chris Andrade

---

## Meeting Overview

**Purpose:** Evaluate Quo, Jobber, and integration strategy for Plotter Mechanix Phase 1 implementation following initial client discovery calls.

**Context:** Team analyzed client transcripts and researched available tools to determine optimal approach for Quick Win Sprint deliverables.

---

## Major Discoveries

### 1. Quo-Jobber Native Integration

**Finding:** Quo and Jobber have extensive native integration that may handle most planned automation.

**Capabilities (from Quo marketing):**
- Call summaries and transcripts automatically logged to Jobber
- Auto-create clients and requests when unknown number calls
- Click-to-call from Jobber using Quo number
- AI voice agent (Sona) for call screening

**Impact:** Reduces need for custom automation builds

---

### 2. Jobber Receptionist Feature

**Finding:** Jobber has built-in receptionist feature at $99/mo

**Comparison needed:**
- Quo Sona (voice agent) vs Jobber Receptionist
- Transcript capabilities
- Call screening effectiveness
- Integration quality

**Decision:** Must test both before recommending

---

### 3. CompanyCam Integration

**Finding:** CompanyCam exists in Jobber App Marketplace

**Client workflow context:**
> "I take a picture and then I send it to Alyssa" - Kelsey

**Potential value:**
- Auto-attach field photos to jobs
- Eliminate texting photos to Alyssa
- Structured photo documentation

**Decision:** Evaluate during testing phase, potential Phase 1 addition

---

### 4. Technical Clarifications

**Key facts established:**
- Kelsey's personal cell is main business number (not Vonage line)
- Jobber account: 1,562 jobs, 1,570 clients, 136 quotes/requests
- Current Jobber cost: $379/mo (Teams plan, Grow tier)
- Requests feature barely used (didn't like the form)

---

## Key Discussion Points

### Communication Filtering Problem

**Matthew:**
> "Kelsey can't not answer calls... a bunch of them are bullshit, but a bunch of them are Requests for the business, but they're just such small things"

**Trent:**
> "We need to get him the things that are high priority for Kelsey to talk to them about"

**Solution direction:**
- Screen calls before reaching Kelsey
- Auto-handle low-value calls (FAQs, paper orders)
- Route high-income calls directly to Kelsey
- Log everything to Jobber

---

### Leverage Existing Tools Philosophy

**Mekaiel:**
> "Many small businesses only utilize 50-60% of their existing tools... our role is to help clients understand and maximize their current technology"

**Team agreement:**
- Test native integrations first
- Build custom only where significant gaps exist
- Avoid adding complexity

---

### Jobber as Source of Truth

**Matthew:**
> "Every day multiple things come in. Kelsey communicates to Alyssa... she takes notes on that call, then she'll go update Jobber. But some of the stuff will get missed and then they'll be back and forth"

**Goal:**
- All communication automatically captured in Jobber
- Kelsey can trust Jobber for daily planning
- Eliminate manual note-taking and phone tag

---

### Risk: Cluttering Jobber

**Trent:**
> "Is it gonna clutter and cause more overwhelm in Jobber? That's what we want to avoid. More information at this point could go the opposite direction on us"

**Concern:**
- Native integration may dump too much data
- Raw transcripts not actionable
- Need structured, useful information

**Solution:**
- Test extensively before production
- Evaluate what native integration actually does
- Add custom parsing only if needed

---

## Decisions Made

1. **Do NOT connect Quo to production Jobber yet**
   - Risk of auto-creating unwanted data
   - Test in isolated environment first

2. **Use Jobber trial accounts for testing**
   - 14-day trials with full Grow plan access
   - Stack trials across team members (Matthew, Trent, Mekaiel = 42 days)
   - Protect client's production environment

3. **Test Quo-Jobber integration thoroughly**
   - Document exactly what happens automatically
   - Identify gaps between marketing promises and reality
   - Make data-driven recommendations

4. **Evaluate Jobber Receptionist vs Quo Sona**
   - Compare features side-by-side
   - Test with real scenarios
   - Determine which better serves Kelsey's needs

5. **Consider CompanyCam as Phase 1 addition**
   - Evaluate cost vs value
   - Test integration behavior
   - Assess Kelsey adoption likelihood

---

## Action Items

### Immediate (This Week)

- [ ] Set up Jobber trial account #1 (Matthew)
- [ ] Set up Quo test account
- [ ] Connect Quo to trial Jobber and document behavior
- [ ] Extract use case scenarios from client transcripts
- [ ] Contact Jobber support for developer/testing assistance

### Testing Phase

- [ ] Test call screening workflows (low-value vs high-value)
- [ ] Evaluate CompanyCam integration
- [ ] Document where Quo summaries appear in Jobber
- [ ] Test auto-create client behavior
- [ ] Evaluate transcript quality and actionability

### Technical Setup

- [ ] Pull Jobber data via API into PostgreSQL database
- [ ] Set up N8N workflows for data sync
- [ ] Build analysis capability for client data patterns
- [ ] Process meeting transcripts for additional insights

---

## Testing Protocol Established

**Approach:**

1. **Set up isolated test environment**
   - Jobber trial accounts (not production)
   - Quo test account (already have for Kelsey)
   - No risk to client data

2. **Walk through real scenarios**
   - Incoming call from unknown number (new lead)
   - Call from existing client requesting quote
   - Low-value call (paper order, FAQ)
   - Kelsey field communication to Alyssa

3. **Document native integration behavior**
   - What happens automatically?
   - Where does data go in Jobber?
   - How actionable are AI summaries?
   - What triggers auto-create client/request?

4. **Identify gaps**
   - What doesn't work as promised?
   - What workflow needs custom build?
   - Where is additional value needed?

5. **Make recommendations**
   - Native features to use
   - Custom builds to add
   - Tools to adopt or skip

---

## Strategic Insights

### Quick Win + Phase 2 Setup

**Trent:**
> "We have to find a way to meet our minimum requirements of what we want to do for the quick win while providing overwhelming value beyond it, and setting us up for the next phase so that he is not even hesitant to sign for the next phase"

**Approach:**
- Over-deliver on Phase 1
- Build trust through tangible results
- Lay foundation for Phase 2 (inventory, unified dashboard)
- Make Phase 2 signup effortless

---

### Data Analysis Foundation

**Decision:** Pull Jobber data into PostgreSQL for analysis

**Why:**
- Understand usage patterns
- Identify workflow bottlenecks
- Build business case for Phase 2
- Faster analysis (not hitting API repeatedly)

**Tools:**
- N8N for data sync
- PostgreSQL for storage (not AirTable - better for large volumes)
- API access for real client data

---

## Technical Concerns to Address

**Integration Data Flow:**
- How do one-way integrations behave?
- Risk of placeholder client records?
- Data accuracy and deduplication?

**Jobber Clutter:**
- Will summaries overwhelm users?
- Are transcripts stored usefully?
- Can data be filtered/organized?

**Call Routing:**
- How to identify high-value vs low-value calls?
- Can routing bypass receptionist for known contacts?
- What triggers immediate Kelsey connection?

---

## Next Steps

### Before Next Client Meeting

1. Complete trial account testing
2. Document Quo-Jobber integration behavior
3. Make Jobber Receptionist vs Quo Sona recommendation
4. Prepare demo scenarios showing actual capabilities
5. Refine Phase 1 deliverables based on findings

### Communication Strategy

- Show Kelsey what native tools can do (not just promises)
- Demo actual tested workflows
- Present recommendations based on data, not guesses
- Set realistic expectations on timelines and capabilities

---

## Meeting Outcome

**Strategic Direction Established:**
- Test-first, build-second approach
- Leverage native tools maximally
- Custom builds only for significant value gaps
- Protect client production environment
- Over-deliver on Quick Win to set up Phase 2

**Key Mindset Shift:**
From "What should we build?" → "What already works that we can leverage?"

---

**Notes:**
- Full transcript available (34K+ tokens)
- Some "Chris" audio may be Kelsey speaking (microphone pickup)
- Holiday timing noted - Jobber support may be slower
- Team motivated to prove value quickly and differentiate from failed previous vendor (Malik)