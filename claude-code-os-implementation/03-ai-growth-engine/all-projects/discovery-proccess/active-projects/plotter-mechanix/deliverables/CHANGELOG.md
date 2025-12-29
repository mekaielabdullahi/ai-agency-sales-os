# Plotter Mechanix Deliverables - Change Log

**Purpose:** Track how deliverables evolve as we learn more through client meetings and technical discovery.

---

## December 23, 2025

**Action:** Created consolidated deliverables structure in ai-agency-development-os

**Changes:**
- Created `deliverables/` folder structure (replaced empty `delivery/` folder)
- Created comprehensive README.md with flexible framework
- Created detailed Phase 1 deliverables document
- Created Phase 2 roadmap (planning only, not scoped)

**Rationale:**
- Consolidate information from two sources (sales-os and plotter-mechanix workspace)
- Establish living documentation that can evolve daily as requirements change
- Separate committed deliverables (Phase 1) from potential future work (Phase 2)

**Key Documents Created:**
- `README.md` - Overview and navigation
- `phase-1-quick-win-sprint.md` - Detailed Phase 1 deliverables
- `phase-2-roadmap.md` - Future roadmap (not committed)
- `CHANGELOG.md` - This file

---

## Pre-December 22, 2025 (Baseline)

**Source:** `offer/drafts/draft-02-post-meeting/quick-win-proposal.md`

**Original Phase 1 Deliverables:**

1. **Quo Phone System Implementation**
   - Replace Vonage
   - Port 602 number
   - Configure call routing
   - Enable Jobber integration
   - A2P registration
   - Team training

2. **Four Core SOPs:**
   - PM-FS-002: Service Call Execution
   - PM-OA-002: Invoice Queue Processing
   - PM-OA-003: Service Call Dispatch
   - PM-FS-005: End-of-Job Handoff
   - Plus: Passive knowledge capture workflow

3. **Three Smart Automations:**
   - Unhandled Message Daily Digest (4 PM)
   - New Lead Entry Notification
   - End-of-Day Job Summary (5:30 PM)

4. **Communication Protocol Guide**
   - One-page rulebook (5 rules)

5. **PlotterOps Blueprint**
   - Visual roadmap for future phases

**Stretch Goal:**
- Internal Query Assistant (chat interface for Quo + Jobber)

**Context:**
- Created after Dec 17 discovery meeting
- Before Dec 22 onboarding meeting
- Based on initial understanding of client needs and available tools

---

## December 22, 2025 - Internal Team Meeting

**Meeting Type:** Internal team analysis (Matthew, Trent, Mekaiel, Chris Andrade)
**Purpose:** Evaluate tools, integrations, and implementation approach after initial client conversations

### Major Discoveries

**1. Quo-Jobber Native Integration is Extensive**

From Quo marketing page:
- Call summaries and transcripts automatically logged to Jobber
- Auto-create clients and requests when unknown number calls
- Click-to-call from Jobber using Quo number
- AI voice agent (Sona) for call screening

**Impact:** Majority of planned automation may be native functionality

**2. Jobber Receptionist Feature Exists**

- Built-in feature at $99/mo
- Call screening and routing capabilities
- Unknown: Full transcript capability, comparison to Quo Sona
- Need to test to determine if better than Quo voice agent

**3. CompanyCam Integration Available**

- Exists in Jobber App Marketplace
- Kelsey's workflow: "I take a picture and send it to Alyssa"
- Potential to auto-attach photos to jobs
- To evaluate: Worth the cost? Will Kelsey adopt?

**4. Key Technical Clarifications**

- **Kelsey's personal cell is the main business number** (not Vonage business line)
- Jobber shows 1,562 jobs, 1,570 clients, 136 quotes/requests
- They pay $379/mo for Jobber (Teams plan, Grow tier)
- Requests feature barely used (didn't like the form)

### Impact on Deliverables

**What Changed:**

**Smart Automations (Deliverable 3):**
- Status: UNDER REVIEW → Completely restructured
- Three generic automations → Specific solutions based on native capabilities
- Added testing protocol: Trial accounts before production
- New focus: Call screening/filtering (Kelsey's main pain)
- Added CompanyCam as potential Phase 1 addition

**Implementation Strategy:**
- New principle: "Leverage 50-60% underutilized existing tools" (Mekaiel)
- Test-first approach: Set up Jobber trials (14 days × 3 team members = 42 days coverage)
- Build custom only where significant gaps exist
- Must avoid "cluttering Jobber with more information"

**What Stayed the Same:**
- Quo implementation (core deliverable, but now evaluating vs Jobber Receptionist)
- Four SOPs (core deliverable)
- Communication protocol (core deliverable)
- PlotterOps Blueprint (core deliverable)

**What's New:**

**Testing Protocol Established:**
1. Set up Jobber trial accounts
2. Connect to Quo test environment
3. Walk through scenarios from client transcripts
4. Evaluate native vs custom solutions
5. Make data-driven recommendations

**Key Quotes from Meeting:**

> "Kelsey can't not answer calls... a bunch of them are bullshit, but a bunch of them are Requests for the business, but they're just such small things" - Matthew

> "We need to get him the things that are high priority for Kelsey to talk to them about" - Trent

> "Many small businesses only utilize 50-60% of their existing tools... our role is to help clients understand and maximize their current technology" - Mekaiel

> "We have to find a way to meet our minimum requirements of what we want to do for the quick win while providing overwhelming value beyond it, and setting us up for the next phase so that he is not even hesitant to sign for the next phase" - Trent

### Decisions Made

1. **Do not connect Quo to production Jobber yet** - Risk of auto-creating unwanted data
2. **Use trial accounts for all testing** - Protect client's production environment
3. **Test Quo-Jobber integration first** - See what's automatic before building custom
4. **Evaluate Jobber Receptionist vs Quo Sona** - Compare features before recommending
5. **Consider CompanyCam** - Evaluate during testing phase

### Action Items from Meeting

- [ ] Set up Jobber trial accounts (Matthew, Trent, Mekaiel)
- [ ] Set up Quo test account
- [ ] Connect Quo to trial Jobber and document behavior
- [ ] Extract use case scenarios from client transcripts
- [ ] Test call screening workflows
- [ ] Evaluate CompanyCam integration
- [ ] Pull Jobber data via API for analysis (N8N → database)
- [ ] Process meeting transcripts for additional insights

### Risk Mitigation

**Identified Concern:**
> "We might start testing something and something ends up in the wrong place" - Trent

**Solution:**
- All testing in isolated trial environments
- Document exactly what native integration does before production deployment
- Understand data flow: "One-way integrations" and placeholder client records

### Technical Notes

**Database Strategy:**
- Pull Jobber data via API
- Store in PostgreSQL (not AirTable - better for large data volumes)
- Enable analysis without repeatedly hitting API
- Build understanding of data structure and usage patterns

**Integration Concerns:**
- Will Quo-Jobber sync create too much clutter?
- Where do summaries appear in Jobber?
- How actionable are AI-generated summaries?
- Do they capture action items or just transcribe?

### Status

Requirements continue to evolve - expect daily updates as testing reveals actual capabilities vs marketing promises.

---

## December 17, 2025 - Discovery Meeting

**Source:** Meeting transcripts and notes

**Key Insights:**

**Client Quotes Captured:**
- "It's hard for me to relay. I get so overwhelmed sometimes." - Chris
- "If I could literally have a camera on me and go out all day..." - Chris
- "I pay him $10,000. And then I'm nowhere at the end of it." - Alyssa (re: Malik)
- "Vonage sucks" - General consensus

**Deliverables Shaped By This Meeting:**
- Passive knowledge capture workflow (Chris's camera/recording idea)
- End-of-job handoff template (eliminate 4-6 calls/day)
- Communication protocol (address scattered messages)
- Quo as Vonage replacement (they were already frustrated)

**Pricing Context:**
- $5,000 fixed price established
- 30-day timeline (team targeting 2-week delivery)
- Guarantee added (keep working free if not satisfied by day 30)

---

## Pre-December 17, 2025 (Initial Proposal)

**Source:** `offer/drafts/draft-01-pre-meeting/quick-win-proposal.md`

**Status:** Superseded by Dec 17 discovery

**Key Differences from Final:**
- Less specific on Quo (hadn't confirmed Vonage frustration)
- Automations not yet refined
- SOPs less tailored to specific pain points
- Didn't have passive knowledge capture concept yet

---

## Evolution Pattern Observed

**Pattern:** Each client conversation refines and focuses deliverables

**Pre-Meeting → Post-Meeting Changes:**
1. **Broader** → **More Specific** (general features → targeted pain points)
2. **Assumptions** → **Validation** (we think they need X → they confirmed X)
3. **Build Everything** → **Leverage Native** (custom automation → use Quo-Jobber integration)
4. **Feature-Focused** → **Outcome-Focused** (list of features → time saved, problems solved)

**Implication:**
- Living documentation approach is correct strategy
- Daily updates expected as we continue discovery
- Flexibility built into structure allows pivoting without chaos

---

## Upcoming Changes Expected

### Post-Dec 22 Meeting Processing

**Expected Updates:**
- Finalize automation scope (native vs custom)
- Refine SOP priorities based on conversation
- Update timeline based on A2P 10DLC registration requirements
- Clarify team assignments

### During Phase 1 Execution

**Expected Updates:**
- Technical constraints discovered during build
- Client feedback on early deliverables
- Scope refinements based on what's working
- Potential additions if delivering ahead of schedule

### Phase 1 Completion

**Expected Updates:**
- Phase 2 roadmap refined based on Phase 1 data
- Inventory issue tracking informs Phase 2 scope
- Cost baseline established for Phase 2 business case
- Client readiness assessment for next phase

---

## Document Maintenance Protocol

**When to Update This Changelog:**

1. After every client meeting (document what changed and why)
2. After significant technical discovery (e.g., finding native integration)
3. When deliverables scope changes (additions, removals, refinements)
4. At phase transitions (Phase 1 → Phase 2)

**What to Include in Each Entry:**

- Date
- Source/trigger (meeting, discovery, client request)
- What changed (specific deliverables affected)
- Why it changed (new information, constraints, opportunities)
- Impact (on timeline, price, scope, approach)

**Cross-Reference:**

- Link to meeting notes
- Link to affected deliverable documents
- Link to related technical documentation

---

## Version Control Integration

**Git Commits:**
- Each changelog entry should correspond to git commits
- Commit messages should reference this changelog
- Tag major milestones (Phase 1 baseline, Phase 1 delivery, Phase 2 kickoff)

**Example Commit:**
```
docs: Update Phase 1 deliverables post-Dec 22 meeting

- Move automations to UNDER REVIEW (Quo native integration discovered)
- Emphasize handoff template as linchpin change
- Update CHANGELOG.md with rationale

See: deliverables/CHANGELOG.md (Dec 22 entry)
```

---

## Related Documentation

- [Deliverables README](./README.md) - Current state overview
- [Phase 1 Deliverables](./phase-1-quick-win-sprint.md) - Detailed Phase 1 scope
- [Phase 2 Roadmap](./phase-2-roadmap.md) - Future planning
- [Meeting Notes](../meetings/) - Source conversations
- [Quick Win Proposal Draft 02](../offer/drafts/draft-02-post-meeting/quick-win-proposal.md) - Pre-Dec 22 baseline

---

*This changelog will be updated after each significant discovery or change to deliverables scope.*
