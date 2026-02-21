# AI Project Delivery Playbook

## Purpose
Complete end-to-end process for delivering AI workflows and agents to clients after they pay. Covers hosting, security, testing, handover, and ongoing maintenance.

## When to Use
After contract is signed and payment received. This playbook runs from kickoff through go-live and maintenance setup.

## Prerequisites
- Signed contract with clear scope and "definition of done"
- Payment received (or deposit for milestone-based)
- Client committed to providing sample data
- Access to client's communication channel (Slack, email, etc.)

---

## The Playbook

### Phase 1: Hosting Decision
**Goal**: Determine where the automation will live
**Time**: Decided during sales, confirmed at kickoff

#### Decision Framework

| Option | When to Use | Compliance |
|--------|-------------|------------|
| **Client Hosts (Recommended)** | Almost always | Safe - each client owns their instance |
| You Host (Internal Only) | Your own agency automation | Safe - not exposing to clients |
| You Host as Product | SaaS model | Requires commercial license |

#### Steps:
1. Default to client hosting (n8n Cloud or self-hosted)
2. Help them set up account if needed
3. Get invited as team member/developer
4. Confirm you have access before kickoff call

**Output**: Client has their own automation instance, you have access

---

### Phase 2: Kickoff Call
**Goal**: Set up environment, collect credentials, align on success criteria
**Time**: 30-60 minutes

#### Agenda:
1. **Confirm Scope** (5 min)
   - Walk through what's being built
   - Confirm "definition of done"
   - Note any questions for clarification

2. **Environment Setup** (15 min)
   - Confirm you're in their n8n instance
   - Connect core integrations (CRM, calendar, email, etc.)
   - Walk them through creating API keys (or share Loom)

3. **Sample Data Collection** (10 min)
   - Get sample inputs for testing
   - Real examples, anonymized if needed
   - At least 10-20 samples (more for AI workflows)

4. **Success Criteria** (10 min)
   - What does "good output" look like?
   - What must NEVER happen?
   - How will they evaluate quality?

5. **Timeline & Communication** (5 min)
   - Expected delivery timeline
   - How you'll communicate progress
   - When they'll review/provide feedback

#### Kickoff Deliverables:
- [ ] Access to client environment confirmed
- [ ] Core integrations connected
- [ ] API keys created (client owns/pays)
- [ ] Sample data received
- [ ] Success criteria documented
- [ ] Timeline agreed

**Output**: Ready to build

---

### Phase 3: Security & Data Setup
**Goal**: Ensure data protection before building
**Time**: During initial build phase

#### Security Checklist:
- [ ] Credentials stored in n8n credential vault (encrypted at rest)
- [ ] No API keys hardcoded in workflow nodes
- [ ] Webhooks use HTTPS only
- [ ] Webhook signature verification enabled (Stripe, GitHub, etc.)
- [ ] No sensitive data in webhook URLs
- [ ] Rate limits considered for public endpoints

#### Data Protection Checklist:
- [ ] Only necessary fields collected (data minimization)
- [ ] Workflow access limited to appropriate users
- [ ] Execution logs pruned appropriately
- [ ] Data flow documented (for deletion requests)
- [ ] Data Processing Agreement in place (if required)

#### For AI Components:
- [ ] Prompt guardrails against jailbreaking
- [ ] No system prompts leaking in outputs
- [ ] Appropriate content filters
- [ ] Logging of AI inputs/outputs for review

**Output**: Secure foundation for build

---

### Phase 4: Build & Internal QA
**Goal**: Build workflow and test thoroughly before client sees it
**Time**: Varies by project complexity

#### Build Standards:
- [ ] Clear naming for every node
- [ ] Sticky notes explaining logic
- [ ] Error handling on all critical paths
- [ ] Timeout handling for external calls
- [ ] Error workflow that alerts on failures
- [ ] Failure logging (Google Sheet or similar)

#### Internal Testing Process:

1. **Unit Testing**
   - Test each component individually
   - Verify credential connections work
   - Check error handling triggers correctly

2. **Edge Case Testing**
   - What happens with bad data?
   - What happens with no data?
   - What happens with duplicate data?
   - What happens with unexpected formats?

3. **Volume Testing**
   - Run 50-100+ sample inputs
   - Log every input/output/error
   - Check for consistency

4. **AI Quality Testing** (if applicable)
   - Relevance: Does output match input?
   - Correctness: Is information accurate?
   - Tone: Matches brand, not toxic?
   - Consistency: Same inputs = similar outputs?
   - No prompt leakage

#### Build Deliverables:
- [ ] Working workflow in test environment
- [ ] Test log with 50+ runs documented
- [ ] Edge cases identified and handled
- [ ] Error scenarios documented
- [ ] Internal QA passed (no blockers)

**Output**: Workflow ready for client testing

---

### Phase 5: Client QA
**Goal**: Client validates workflow meets success criteria
**Time**: 3-7 days typically

#### Setup for Client Testing:
1. Create simple testing interface (chat UI, form, or clear instructions)
2. Don't require them to use n8n directly
3. Explain what to test and how to give feedback
4. Set expectations on response time

#### Client Testing Checklist:
- [ ] Client has clear way to test system
- [ ] Feedback channel established
- [ ] Success criteria from kickoff reviewed
- [ ] Timeline for feedback agreed

#### Handling Feedback:

| Feedback Type | Response |
|---------------|----------|
| Bug / Error | Fix immediately |
| Tweak / Refinement | Implement if in scope |
| New Feature | "Great for v2" - log to backlog |
| Out of Scope | Explain boundary, offer as new project |

#### Scope Protection Script:
> "That's a great idea. It falls outside our v1 scope, so I'm adding it to the backlog for phase 2. Once we complete and close out v1, we can scope a follow-up project around these enhancements."

**Output**: Client signs off that workflow meets success criteria

---

### Phase 6: Production Deployment
**Goal**: Move from test to live environment
**Time**: 1-2 hours

#### Deployment Checklist:
1. [ ] Duplicate workflow (keep test version as backup)
2. [ ] Export JSON backup to secure storage
3. [ ] Swap test credentials for production credentials
4. [ ] Activate workflow in production
5. [ ] Run 3-5 live tests to confirm working
6. [ ] Disable test version
7. [ ] Document production workflow location

#### Backup Strategy:
- Export JSON to GitHub/Google Drive
- Keep version history
- Consider automated backup workflow

**Output**: Live workflow in production

---

### Phase 7: Handover
**Goal**: Transfer knowledge and ownership to client
**Time**: 30-60 minutes

#### Handover Package:

1. **Loom Walkthrough** (5-10 min video)
   - How the workflow runs end-to-end
   - Where to find logs/outputs
   - How to pause/restart if needed
   - What to do if something breaks

2. **Written Documentation**
   - Workflow overview (what it does)
   - Trigger conditions
   - Expected inputs/outputs
   - Error handling behavior
   - API keys and where they're used

3. **Workflow Hygiene**
   - All nodes clearly labeled
   - Sticky notes explaining logic
   - No sensitive data exposed
   - Clean, readable structure

4. **Backup Access**
   - Client has exported JSON
   - Knows where backups are stored
   - Can restore if needed

#### Handover Meeting:
- Walk through Loom video together
- Answer questions
- Confirm they can access everything
- Get sign-off on completion

**Output**: Client fully onboarded, project complete

---

### Phase 8: Project Close & Billing
**Goal**: Close project cleanly and set up ongoing relationship
**Time**: Same day as handover

#### Project Closure:
1. [ ] Walk through original scope - confirm all items delivered
2. [ ] Get written confirmation project is complete
3. [ ] Send final invoice
4. [ ] Thank client for partnership

#### Maintenance Retainer Offer:

**What Retainer Covers**:
- Bug fixes
- Small tweaks
- Platform/dependency updates
- Basic monitoring
- Security checks

**What Retainer Does NOT Cover**:
- New features
- New workflows
- Major scope changes
- Additional integrations

**Service Levels** (example):
- Critical outage: Response within 4 hours
- Bug: Response within 24 hours
- Minor request: Response within 48-72 hours

#### Retainer Pitch:
> "Now that we're live, I recommend a monthly maintenance retainer to keep everything running smoothly. This covers bug fixes, updates, and monitoring. New features would be scoped separately. Would you like me to send over the details?"

**Output**: Final payment received, maintenance terms agreed (if applicable)

---

## Quality Checklist

Before closing any project:

- [ ] All scope items delivered and confirmed
- [ ] Security checklist completed
- [ ] Error handling in place
- [ ] Documentation provided
- [ ] Loom walkthrough recorded
- [ ] Backup exported
- [ ] Client sign-off received
- [ ] Final invoice sent and paid
- [ ] Maintenance terms discussed

---

## Common Mistakes

| Mistake | How to Avoid |
|---------|--------------|
| Building before getting sample data | Require sample data at kickoff |
| Testing with fake data only | Always use real client data |
| No error handling | Add error workflow to every build |
| Scope creep | Log new features to backlog, don't add mid-project |
| Client doesn't understand system | Always do walkthrough video |
| You own the API keys | Client creates and owns all keys |
| No backup | Export JSON before going live |
| Vague "done" definition | Define in contract, confirm at kickoff |

---

## Templates Needed

- [ ] Kickoff call agenda template
- [ ] Sample data request template
- [ ] Client testing instructions template
- [ ] Handover document template
- [ ] Maintenance retainer agreement template
- [ ] API key setup Loom script

---

## Version History

- **v1.0** (2024-12-27): Initial version based on Nate Herk methodology

---

## Source

Based on: Nate Herk - "How to Deliver AI Projects" (YouTube)
Location: `/external-sources/podcasts/nate-herk/how-to-deliver-ai-projects-source.md`
