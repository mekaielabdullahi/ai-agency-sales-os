---
stepsCompleted: [1, 2, 3, 4, 7, 8, 9, 10, 11]
status: complete
inputDocuments:
  - 03-ai-growth-engine/onboarding/PRD-ENHANCED-ONBOARDING-SYSTEM.md
  - 03-ai-growth-engine/onboarding/ONBOARDING-PROCESS-OVERVIEW.md
  - 06-knowledge-base/external-sources/youtube/processed/2026-01-18-client-onboarding-validation.md
  - 03-ai-growth-engine/onboarding/checklists/logistics-onboarding-call-sop.md
  - 03-ai-growth-engine/onboarding/agents/onboarding-agent.md
workflowType: 'prd'
lastStep: 7
documentCounts:
  existingPRD: 1
  processOverview: 1
  validation: 1
  callSOPs: 1
  agentSpecs: 1
---

# Product Requirements Document - Enhanced Client Onboarding System

**Author:** MEKAIEL
**Date:** 2026-01-18

## Executive Summary

**The Problem:** AriseGroup's current client onboarding system covers 90% of a proven $70K/month framework (validated against Nick Severance's methodology). However, six critical gaps remain:

1. No defined Claude Code agents for automation orchestration
2. No secure credential management protocol (password vault, lifecycle)
3. No automated delivery report generation
4. Implicit 2FA handling (not explicit in call script)
5. Win conditions not systematically derived from approved PRDs
6. Communication frequency not standardized

**The Solution:** A fully automated, agent-assisted client onboarding system with four specialized Claude Code agents that orchestrate the entire client lifecycle - from payment to project close.

### What Makes This Special

**The Client Experience:** Within 5 minutes of payment, clients receive a personalized gratitude email, a clear next-steps guide, and dedicated Slack channels - eliminating buyer remorse before it starts. This exceptional first impression is why the system generates referrals.

**The Referral Engine:** Target: 5+ referrals per 10 clients through delivery clarity. The mechanism is a **closed-loop delivery guarantee**:

```
PRD (dev-approved) → Win Conditions (client-confirmed) → Delivery Report (evidence-verified)
```

What dev approves, what client expects, and what gets delivered are provably the same thing.

**Agent Orchestration:** Four agents operate independently with event-based coordination via n8n:
- **Onboarding Agent** → triggers on payment
- **Communication Agent** → triggers on Slack messages
- **Project Management Agent** → triggers on timeline milestones
- **Security Agent** → triggers on credential access events

**Target Outcomes:**
- Target: 5+ referrals per 10 clients through exceptional experience
- Eliminate buyer remorse within 5 minutes of payment
- Target: 100% access collection on first call, with same-day follow-up protocol for exceptions
- Zero out-of-scope change requests per project, validated through PRD-to-win-condition traceability
- Auto-generated delivery reports proving all conditions met

## Project Classification

| Attribute | Value |
|-----------|-------|
| **Technical Type** | Developer Tool (Agentic Module) |
| **Domain** | General (Internal Business Automation) |
| **Complexity** | Medium |
| **Project Context** | Brownfield - extending existing onboarding system |

This system builds on the existing n8n automation, Notion databases, and Slack integrations. The enhancement adds Claude Code agent orchestration, 1Password credential management, and automated report generation.

## Success Criteria

### User Success

**The "Right Choice" Moment:** Clients feel they made the right decision within 5 minutes of payment. This is triggered by:
- Personalized gratitude email (< 30 seconds)
- Clear next-steps email with calendar link (< 5 minutes)
- Dedicated Slack channels created and team notified

**Friction-Free Logistics:** The 15-minute onboarding call feels efficient, not bureaucratic:
- All platform access collected in single call (target: 100%, fallback: same-day follow-up)
- 2FA handled live, no multi-day blockers
- Win conditions confirmed and understood

**Delivery Confidence:** At project close, clients see:
- Delivery report with every win condition checked
- Evidence attached (screenshots, metrics, Loom videos)
- Clear handoff with no ambiguity about "is it done?"

### Business Success

**System Validation Milestone:** 5 clients complete the full enhanced cycle without process breakdowns:
- Payment → Logistics Call → Project Delivery → Delivery Report Signed Off

**Operational Metrics (Lagging Indicators):**

| Metric | Current State | Target | How Measured |
|--------|---------------|--------|--------------|
| Time to first email | ~1 min | < 30 sec | n8n workflow logs |
| Access collection (first call) | ~80% | 100% | Post-call checklist |
| Scope creep incidents | Unknown | 0 per project | Out-of-scope change requests |
| Delivery report generation | Manual | Automated | System trigger logs |
| Referral rate | Unknown | 5+ per 10 clients | CRM tracking |
| Client satisfaction (NPS) | Unknown | 9+ | Post-project survey |

**Leading Indicators (Early Validation):**

| Indicator | What It Predicts | Measurement | Target |
|-----------|------------------|-------------|--------|
| Client responds to gratitude email | Engagement, low remorse | Email open/reply rate | 80%+ open |
| Logistics call books within 48 hrs | Smooth onboarding | Calendar data | 100% |
| All access collected first call | No project delays | Post-call checklist | 100% |
| Win conditions confirmed in writing | Zero scope creep | Signed doc timestamp | Before kickoff |

**Scope Classification Protocol:**
When a client request comes in during a project:
1. Compare request against signed win condition document
2. If listed → in scope, proceed
3. If not listed → out-of-scope, log as change request
4. PM makes classification call, documents decision in Notion
5. Out-of-scope requests offered as Phase 2 scope

**Revenue Impact:** Referral-driven growth - each successful client experience compounds into pipeline without additional sales effort.

### Technical Success

**Agent Reliability:**
- All 4 agents trigger correctly on their designated events
- Graceful degradation with explicit fallbacks:
  - Onboarding Agent fails → Manual email + channel creation within 30 min
  - Communication Agent fails → PM monitors Slack directly
  - PM Agent fails → Manual progress tracking in Notion
  - Security Agent fails → Manual revocation checklist within 24 hours
- Error alerting: team notified within 5 minutes of any automation failure

**Credential Security:**
- Zero plaintext credentials in Slack, email, or Notion
- All credentials stored in 1Password with proper vault structure
- Credential revocation completed within 24 hours of project close

**Integration Stability:**
- n8n workflows maintain 99.9% uptime
- Webhook handlers process events within 30 seconds
- Fallback: manual execution documented for all automated steps

### Measurable Outcomes

| Outcome | Measurement | Target | Timeline |
|---------|-------------|--------|----------|
| System validated | Full cycle completed | 5 clients | First 2 months |
| Referral engine active | Referrals per 10 clients | 5+ | After 10 clients |
| Zero scope creep | Out-of-scope requests (using protocol) | 0 | Per project |
| Automation reliability | Manual interventions decreasing | Fewer each client | Ongoing |

## Product Scope

### MVP - Minimum Viable Product

**Must have for system to be useful:**

1. **Closed-Loop Delivery System** - PRD-derived win conditions, client confirmation workflow, traceable delivery checklist (this is the core value)
2. **Onboarding Agent** - Payment triggers email sequence + Slack channel creation
3. **Enhanced Logistics Call SOP** - Explicit 2FA block, win condition confirmation
4. **1Password Vault Structure** - Per-client folders, role-based access
5. **Delivery Report Template** - Manual generation from win condition checklist

**MVP Success:** One client completes the full cycle: payment → logistics call → project delivery → delivery report signed off. No process breakdowns requiring system redesign.

### Growth Features (Post-MVP)

**What makes it competitive:**

1. **Security Agent** - Automated credential lifecycle (expiry alerts, revocation)
2. **Project Management Agent** - Timeline tracking, delay alerts, automated progress updates
3. **Automated Delivery Reports** - Generated when all win conditions marked complete
4. **Communication Agent** - Slack monitoring, urgent message flagging, SLA tracking

**Growth Success:** All 4 agents operational, 5 clients processed smoothly with decreasing manual interventions per client.

### Vision (Future)

**The dream version:**

1. **Client Portal** - Self-service access to project status, win conditions, documents
2. **Predictive Alerts** - AI flags projects at risk of delays before they happen
3. **Referral Automation** - Triggered ask + tracking when NPS score is high
4. **Multi-Client Dashboard** - Single view of all active client statuses
5. **Template Library** - Win condition and delivery report templates by project type

## User Journeys

### Journey 1: Sarah Chen - The Client Who Finally Feels Taken Care Of

Sarah is the owner of a growing HVAC company who just signed a $15K automation project with AriseGroup. She's excited but nervous - she's been burned before by agencies that took her money and disappeared into a black hole of vague updates and scope creep. She clicks "Pay Invoice" on a Tuesday afternoon, half-expecting the usual silence.

Within 30 seconds, her inbox pings. A personalized email from Mekaiel thanks her for trusting AriseGroup and references the specific pain point they discussed - her techs spending hours on paperwork instead of fixing units. She smiles. Five minutes later, another email arrives with clear next steps: a calendar link to book her 15-minute Logistics Onboarding Call, and a simple PDF showing which platforms she'll need to provide access to.

The next morning, she joins the video call. Instead of the usual "we'll figure it out later" approach, Mekaiel walks her through each platform with her screen shared. When Make.com sends a 2FA code to her phone, she reads it out loud and watches Mekaiel enter it immediately. When he walked her through 2FA live instead of sending another email, Sarah realized this wasn't just efficiency - someone actually understood how agencies had failed her before. The whole call takes 18 minutes. Before they hang up, Mekaiel reads back her win conditions: "By March 15th, you'll have an automated dispatch system that assigns jobs based on tech location, sends customers real-time ETAs, and posts completed jobs to QuickBooks. When all three are working, we're done."

Sarah books her Project Kickoff feeling something she hasn't felt with an agency before: clarity.

Two weeks in, Sarah notices she hasn't heard anything in four days. The old anxiety creeps back - is this where they ghost me? Then her phone buzzes: the Tuesday progress update arrives right on schedule. Two items complete, one in progress, win conditions tracked. She exhales. The system is working exactly as promised.

Four weeks later, Sarah receives a Delivery Report with three green checkmarks, screenshots of her system in action, and a Loom video walking through how to use it. She forwards it to her business partner with the note: "This is how it should be done." When Mekaiel asks if she knows anyone else who might benefit, she immediately thinks of two friends who run service businesses.

**Journey Reveals Requirements For:**
- Automated email sequence (gratitude + next steps)
- Calendar integration for logistics call booking
- Platform-specific access collection workflow
- 2FA handling during live call
- Win condition documentation and confirmation
- Scheduled progress updates (Tuesday/Friday)
- Delivery report generation with evidence
- Referral ask timing and tracking

---

### Journey 1b: Sarah's 2FA Nightmare - Recovery Builds Trust

It's the same logistics call, but when Sarah tries to log into her Google Workspace, the 2FA code never arrives. She checks her phone - nothing. Mekaiel doesn't panic.

"No problem - sometimes there's a carrier delay. Let's try the backup method. Can you open your Google Authenticator app?" Sarah realizes she never set that up.

Mekaiel pivots smoothly: "Okay, here's what we'll do. I'm documenting Google Workspace as 'pending' in our tracker. Everything else we'll finish now. I'll send you a 2-minute Loom video showing exactly how to add me once the code arrives - you can do it whenever works for you today."

Sarah finishes the rest of the call - Make.com, Airtable, Slack - all connected. An hour later, the Google code finally arrives. She follows the Loom video and grants access in 3 minutes. Mekaiel sends a Slack message: "Got it - we're fully unblocked now."

What could have derailed the entire call became a minor footnote. Sarah's trust actually *increased* - when something went wrong, the system handled it gracefully instead of spiraling into a week of back-and-forth emails.

**Journey Reveals Requirements For:**
- Fallback 2FA methods documented per platform
- Credential status tracking (collected, pending, blocked)
- Async credential collection workflow (Loom video + instructions)
- Same-day follow-up protocol for pending access
- Documentation of what's blocking vs. what's complete
- Graceful recovery messaging

---

### Journey 2: Mekaiel - The Founder Who Stops Chasing Logistics

It's 9:47 AM and Mekaiel just got a Stripe notification: Sarah Chen paid her invoice. In the old days, this meant scrambling to send a welcome email, manually creating Slack channels, and hoping he remembered to follow up about platform access.

Today, he watches n8n do its thing. Within 30 seconds, the Onboarding Agent fires: gratitude email sent, next steps email queued for 5 minutes, Slack channels #sarahchen and #sarahchen-internal created, team notified in #new-clients. He glances at his phone - no action required.

When Sarah books her Logistics Onboarding Call, Mekaiel pulls up the enhanced SOP. He knows exactly what to cover: quick expectations (Slack channel, Tuesday/Friday updates), platform walkthrough with screen share, and the 2FA block he used to dread. "You should get a code on your phone right now - just read it to me." No more multi-day email chains begging for six-digit codes.

The critical moment comes when he reads the win conditions. He pulls them directly from the approved PRD - no making things up on the fly. "Does this match what you're expecting?" Sarah nods. He confirms in writing. Scope creep vaccine administered.

During the project, Mekaiel checks his PM dashboard. The Project Management Agent shows Sarah's project is on track - all milestones green. The Communication Agent flagged one message from Sarah yesterday as "needs response" but nothing urgent. He batches his client responses during his 12-2pm window.

At project close, he marks all win conditions complete in Notion. The system generates a Delivery Report - he reviews it, adds one screenshot, and sends it to Sarah. When she confirms "looks great!", he triggers the credential revocation. Security Agent removes her credentials from the team vault within 24 hours.

Total manual intervention this project: the 18-minute logistics call, two progress updates, and clicking "Generate Report." Everything else ran itself.

**Journey Reveals Requirements For:**
- Automated onboarding sequence triggered by payment
- Enhanced call SOP with 2FA block and win condition confirmation
- PM dashboard showing project status across clients
- Communication flagging for urgent messages
- Win condition tracking tied to PRD
- Delivery report generation and evidence attachment
- Credential revocation workflow
- Time-boxed Slack availability window

---

### Journey 3: Trent - The Developer Who Gets Access Without the Runaround

Trent is a developer on the AriseGroup team, assigned to build Sarah Chen's dispatch automation. At his last agency job, a client project stalled for a week because no one knew who had the Stripe password - credentials scattered across Slack DMs, sticky notes, and someone's personal 1Password vault. He's seen how bad it can get.

Today, Trent gets a notification: "You've been granted access to Sarah Chen - HVAC Automation project credentials." He opens 1Password, navigates to the client vault folder, and sees exactly what he needs: Make.com (API key), Airtable (workspace invite pending), QuickBooks (OAuth connected). Each credential has a note about when it was collected and by whom.

He starts building. When he needs the Airtable workspace, he sees it's marked "pending - client adding" in the vault. He pings the #sarahchen-internal channel: "Airtable access still pending." Mekaiel follows up with Sarah same-day. By 4pm, the credential appears in the vault - no plaintext passwords in Slack, no "where did that login go?" archaeology.

Mid-project, Matthew (the other developer on the team) gets pulled in to help with the QuickBooks integration. He requests access to the Sarah Chen vault - Mekaiel approves, and Matthew sees only the credentials relevant to his assigned task. Role-based access means Matthew doesn't need to see everything, just what he needs.

When Sarah's project wraps, both Trent and Matthew get notifications: "Your access to Sarah Chen credentials expires in 24 hours." Trent finishes his final testing, exports any needed reference docs, and watches his vault access disappear right on schedule. Clean handoff, no lingering access to worry about.

**Journey Reveals Requirements For:**
- Per-client vault folders in 1Password
- Role-based credential access (project assignment grants access)
- Credential collection status tracking
- Credential pending alerts
- Credential expiry monitoring
- Secure team notification when access granted/revoked
- Automatic access revocation at project close
- No plaintext credentials in communication channels
- Multi-team-member access with appropriate scoping

---

### Journey Requirements Summary

| Capability Area | Revealed By Journey | Priority |
|-----------------|---------------------|----------|
| Automated Email Sequence | Client (Sarah) | MVP |
| Slack Channel Auto-Creation | Client (Sarah), PM (Mekaiel) | MVP |
| Platform Access Collection Workflow | Client (Sarah), PM (Mekaiel) | MVP |
| 2FA Handling Workflow | Client (Sarah), Recovery (1b) | MVP |
| Win Condition Documentation | Client (Sarah), PM (Mekaiel) | MVP |
| Delivery Report Generation | Client (Sarah), PM (Mekaiel) | MVP |
| Per-Client Vault Structure | Team (Trent, Matthew) | MVP |
| Role-Based Credential Access | Team (Trent, Matthew) | MVP |
| Credential Collection Status | Team (Trent), Recovery (1b) | MVP |
| Credential Pending Alerts | Team (Trent), Recovery (1b) | Growth |
| Credential Expiry Monitoring | Team (Trent, Matthew) | Growth |
| Same-Day Follow-Up Protocol | Recovery (1b), Team (Trent) | MVP |
| Async Credential Collection | Recovery (1b) | MVP |
| Automatic Credential Revocation | PM (Mekaiel), Team (Trent, Matthew) | Growth |
| PM Dashboard / Multi-Client View | PM (Mekaiel) | Growth |
| Communication Flagging | PM (Mekaiel) | Growth |
| Scheduled Progress Updates | Client (Sarah) | MVP |
| Referral Ask Timing | Client (Sarah) | Vision |

## Developer Tool Specific Requirements

### Project-Type Overview

This is an **Agentic Module** - an internal developer tool that orchestrates client onboarding through a combination of n8n workflows, Claude Code skills, and 1Password CLI integration. Unlike a traditional SDK or library, this system is consumed by the AriseGroup team (Mekaiel, Trent, Matthew) through multiple interfaces.

### Runtime & Language Matrix

| Component | Runtime | Language | Location |
|-----------|---------|----------|----------|
| Onboarding Agent | n8n | JSON workflow | n8n instance |
| Communication Agent | Claude Code | Skill (markdown + Python) | `agentic/modules/` |
| PM Agent | Claude Code + Notion | Skill + API | `agentic/modules/` |
| Security Agent | Claude Code + 1Password | Skill + CLI | `agentic/modules/` |
| Email Templates | n8n | HTML/Markdown | n8n workflow nodes |
| Win Condition Template | Static | Markdown | `templates/` |
| Delivery Report Template | Static | Markdown | `templates/` |

### Dependency Versioning Strategy

| Dependency | Version Pinning | Update Protocol |
|------------|-----------------|-----------------|
| n8n | Export workflow JSON before any n8n updates | Test in staging, re-import if broken |
| 1Password CLI | Pin to `v2.x` in installation docs | Update only with tested release |
| Notion API | Target `2022-06-28` version | Monitor deprecation notices |
| Slack API | Use stable bot scopes only | Avoid beta features |
| Claude Code | Track `agentic/` module compatibility | Test skills after CC updates |

**Environment Validation Script:**
Before deployment, run `scripts/validate-environment.sh` to confirm:
- [ ] n8n instance reachable and authenticated
- [ ] 1Password CLI installed and logged in
- [ ] Notion API key valid (test query succeeds)
- [ ] Slack bot token valid (test post succeeds)
- [ ] Gmail API credentials configured

### Installation & Deployment Methods

| Component | Deployment Method | Owner |
|-----------|-------------------|-------|
| n8n Workflows | Import workflow JSON via n8n UI | Mekaiel |
| Claude Code Skills | `agentic-setup` or manual skill installation | Mekaiel |
| 1Password Vault Structure | Manual configuration via 1Password Teams admin | Mekaiel |
| Notion Database Schema | Template duplication or manual setup | Mekaiel |
| Slack Bot Permissions | OAuth app installation | Mekaiel |

**Single-command deployment not available** - each component has its own deployment path due to different underlying platforms. Environment validation script confirms readiness.

### Secrets Management

| Secret | Development | Production | Never |
|--------|-------------|------------|-------|
| Notion API Key | `.env.local` | n8n credential store | Git, Slack, Notion |
| Slack Bot Token | `.env.local` | n8n credential store | Git, Slack |
| Gmail API Credentials | Local `credentials.json` | n8n credential store | Git |
| 1Password Service Account | Interactive login | Service account token | Git, plaintext anywhere |
| Stripe Webhook Secret | `.env.local` | n8n credential store | Git |

**Rule:** Trent and Matthew use `.env.local` for development. Production secrets live only in n8n's encrypted credential store. Never commit secrets to git or paste in Slack.

### Developer Interaction Patterns

| Actor | Primary Interface | Secondary Interface |
|-------|-------------------|---------------------|
| Mekaiel (PM) | Claude Code CLI, n8n UI | Notion, Slack |
| Trent (Dev) | 1Password vault, Slack | Claude Code CLI |
| Matthew (Dev) | 1Password vault, Slack | Claude Code CLI |

**CLI Commands:**

| Command | Status | Current Fallback |
|---------|--------|------------------|
| `/onboard-client` | Planned | Manual: Trigger n8n workflow via UI |
| `/credential-status [client]` | Planned | Manual: Check 1Password vault directly |
| `/generate-delivery-report [client]` | Planned | Manual: Fill template from Notion data |

### Documentation Requirements

| Document | Purpose | Audience |
|----------|---------|----------|
| Agent Specifications | Triggers, inputs, outputs, error handling | All team |
| Workflow Runbooks | Step-by-step for each n8n workflow | Mekaiel |
| Troubleshooting Guide | When agents fail, how to recover | All team |
| Credential Protocol | How to collect, store, revoke credentials | All team |
| Onboarding Call SOP | Live call script with 2FA block | Mekaiel |

### Templates & Examples

| Template | Format | Purpose |
|----------|--------|---------|
| Win Condition Template | Markdown | PRD-derived client deliverables |
| Delivery Report Template | Markdown → PDF | Evidence-based project completion |
| Progress Update Template | Markdown | Tuesday/Friday client updates |
| Gratitude Email | HTML | Immediate post-payment email |
| Next Steps Email | HTML + PDF attachment | 5-minute follow-up with calendar link |
| 2FA Fallback Loom Script | Text | Script for async credential collection video |
| Platform Signup Instructions | PDF | Per-platform access grant guides |

### Testing Approach

**Test Levels:**

| Level | Scope | Tools | Owner |
|-------|-------|-------|-------|
| Unit | Individual functions (email gen, channel creation) | pytest, manual | Trent/Matthew |
| Integration | n8n workflow end-to-end with mock triggers | n8n test execution | Mekaiel |
| E2E | Full onboarding sequence with test client | Manual with test record | Mekaiel |

**Dry-Run Mode:**
Enable with `DRY_RUN=true` environment variable or `--dry-run` flag on CLI commands.
- Emails: Logged but not sent
- Slack: Messages posted to #test-notifications only
- Notion: Changes logged, not written
- 1Password: Read-only operations only

**Test Environment:**

| System | Test Instance | Reset Method |
|--------|---------------|--------------|
| Notion | Test database (filter: `Test = true`) | Delete test records after run |
| Slack | `#test-*` channels | Auto-delete after 24 hours |
| 1Password | `_test-client` vault folder | Manual cleanup weekly |
| n8n | Same instance, test workflow copies | Workflows disabled by default |
| Email | Redirect to `test@arisegroup.ai` | No cleanup needed |

**Test Data Management:**
- All test records marked with `Test = true` in Notion
- Test client name prefix: `_test-` (e.g., `_test-sarah-chen`)
- Production data never modified during testing
- Test 1Password vault folder isolated from client vaults

### Implementation Considerations

**Modular Architecture:**
Each agent is independently deployable and testable. Failure of one agent doesn't block others (graceful degradation documented in Success Criteria).

**Configuration Management:**
- Environment variables for API keys (Stripe, Notion, Slack, Gmail)
- 1Password CLI authentication via service account or interactive login
- n8n credentials stored in n8n's credential manager
- All config documented in `CONFIG.md` with example `.env.example`

**Versioning:**
- n8n workflows versioned via export/import JSON (stored in `workflows/` folder)
- Claude Code skills versioned with the `agentic/` module structure
- Templates versioned in git alongside documentation
- Dependency versions pinned per versioning strategy table

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

**MVP Approach:** Problem-Solving + Experience MVP Hybrid
- Solve the core problems: buyer remorse, scope creep, credential chaos
- Deliver the key experience: 5-minute post-payment dopamine sequence
- Build the foundation: closed-loop delivery guarantee (PRD → Win Conditions → Delivery Report)

**Resource Requirements:**
- **Team Size:** 3 (Mekaiel as PM/deployer, Trent and Matthew as developers)
- **Skills Needed:** n8n workflow building, 1Password administration, Notion API, basic Python for Claude Code skills
- **Timeline Guidance:** MVP deployable within 2-3 weeks given existing system foundation

### MVP Feature Set (Phase 1)

**Core User Journeys Supported:**
1. Sarah Chen journey - Complete flow from payment to delivery report
2. Sarah Recovery journey - Graceful 2FA failure handling
3. Mekaiel journey - Reduced manual intervention
4. Trent journey - Clean credential access (basic flow only)

**Must-Have Capabilities (validated by journey analysis):**

| Capability | Without it, product fails? | Can be manual initially? | Journey Source |
|------------|---------------------------|--------------------------|----------------|
| Automated Email Sequence | Yes - buyer remorse | No - speed is the point | Sarah |
| Slack Channel Creation | Yes - team coordination | Could be, but automated exists | Sarah, Mekaiel |
| 2FA Handling Protocol | Yes - access collection | No - must be live | Sarah, Recovery |
| Win Condition Documentation | Yes - scope creep | Partially - template OK | Sarah, Mekaiel |
| Delivery Report Template | Yes - proof of completion | Yes - manual generation OK | Sarah, Mekaiel |
| 1Password Vault Structure | Yes - credential chaos | No - security requirement | Trent |
| Same-Day Follow-Up Protocol | Yes - unblocks projects | Yes - manual tracking OK | Recovery, Trent |

**MVP Scope:**
1. **Onboarding Agent** (n8n) - Payment → email sequence → Slack channels → Notion update
2. **Enhanced Logistics Call SOP** - Explicit 2FA block, win condition confirmation, fallback protocols
3. **Closed-Loop Templates** - Win condition template, delivery report template
4. **1Password Vault Structure** - Per-client folders, role-based access grants
5. **Credential Status Tracking** - Notion database with collected/pending/blocked states
6. **Progress Update Template** - Manual Tue/Fri updates using template

**What's explicitly NOT in MVP:**
- Automated delivery report generation (manual template fill)
- Communication Agent (PM monitors Slack directly)
- PM Agent (manual timeline tracking in Notion)
- Security Agent (manual revocation checklist)
- Credential expiry alerts (manual review)

### Post-MVP Features

**Phase 2 - Growth (After 5 successful clients):**

| Feature | Why Post-MVP | Trigger for Addition |
|---------|--------------|----------------------|
| Security Agent | Manual revocation works for low volume | >3 concurrent projects |
| PM Agent | Manual tracking works initially | Missed deadline or delay |
| Automated Delivery Reports | Template fill works | >5 reports generated manually |
| Communication Agent | PM can monitor directly | Message missed, client escalation |
| Credential Expiry Monitoring | Low volume = manual review | Credential expired unnoticed |

**Phase 3 - Vision (After system proven at scale):**

| Feature | Value Proposition | Prerequisite |
|---------|-------------------|--------------|
| Client Portal | Client self-service, reduced PM load | All agents stable, 10+ clients processed |
| Predictive Alerts | Proactive vs reactive management | Historical data from PM Agent |
| Referral Automation | Maximize referral conversion | NPS tracking implemented |
| Multi-Client Dashboard | Scale visibility | 5+ concurrent projects |
| Template Library | Faster project setup by type | Patterns identified across 10+ projects |

### Risk Mitigation Strategy

**Technical Risks:**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| n8n workflow fails silently | Medium | High | Error alerting to #automation-alerts, manual fallback documented |
| 1Password CLI breaks after update | Low | High | Pin CLI version, test before updating |
| Webhook missed (Stripe payment) | Low | High | Fallback trigger via Notion status change |
| Email delivery failure | Low | Medium | Check delivery logs, Gmail backup sender |

**Operational Risks:**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Team member unavailable during onboarding call | Medium | Medium | SOPs documented for any team member to execute |
| Client doesn't book logistics call | Medium | Medium | 48-hour follow-up sequence if not booked |
| 2FA fails multiple times | Low | Medium | Async collection workflow (Loom video + instructions) |

**Scope Risks:**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| MVP scope creeps during build | Medium | High | This scoping document + PR review against scope |
| Client requests out-of-scope features | Medium | Medium | Win condition document signed before kickoff |
| Growth features needed earlier | Low | Low | Each agent independently deployable, can accelerate |

### Scope Decision Rules

**How to decide if something is MVP:**
1. Does the user journey break without it? → MVP
2. Can we do it manually for 5 clients without burnout? → Post-MVP
3. Does it directly prevent buyer remorse or scope creep? → MVP
4. Is it automation of a working manual process? → Post-MVP

**When to promote Growth feature to MVP:**
- Manual workaround fails for a real client
- Security or compliance requirement emerges
- Team cannot sustain manual effort at current volume

## Functional Requirements

### Client Onboarding Automation

- FR1: System can detect payment completion via Stripe webhook within 30 seconds
- FR2: System can send personalized gratitude email to client within 30 seconds of payment
- FR3: System can send next-steps email with calendar link and platform PDF within 5 minutes of payment
- FR4: System can create client-facing Slack channel using naming convention (#clientname)
- FR5: System can create internal Slack channel using naming convention (#clientname-internal)
- FR6: System can add default team members to newly created Slack channels
- FR7: System can update Notion database with onboarding timestamps and status
- FR8: System can post new client notification to #new-clients channel with project summary
- FR9: System can detect Notion status change to "Paid" and trigger identical onboarding sequence as webhook backup
- FR10: System can send follow-up reminder if logistics call not booked within 48 hours of payment

### Credential Management

- FR11: PM can create per-client vault folder in 1Password
- FR12: PM can grant role-based credential access to team members by project assignment
- FR13: Team member can view only credentials for their assigned projects
- FR14: PM can track credential collection status (collected, pending, blocked) in Notion
- FR15: PM can document credential collection timestamps and collector identity
- FR16: PM can revoke team member access to client credentials at project close
- FR17: System can store credentials exclusively in encrypted vault (never plaintext in Slack/email/Notion)
- FR18: PM can grant temporary, time-limited credential access to contractors

### Win Condition & Scope Management

- FR19: PM can create win condition document from approved PRD
- FR20: PM can version win condition document when scope changes are approved
- FR21: Client can confirm win conditions in writing before project kickoff
- FR22: PM can compare incoming client request against signed win condition document
- FR23: PM can classify request as in-scope or out-of-scope based on win condition comparison
- FR24: PM can log out-of-scope requests as change requests in Notion
- FR25: PM can offer out-of-scope requests as Phase 2 work
- FR26: System can log all win condition status changes with timestamp, actor, and evidence link

### Project Delivery & Reporting

- FR27: PM can generate delivery report from win condition checklist
- FR28: PM can attach evidence to each win condition (screenshots, metrics, Loom videos)
- FR29: PM can mark win conditions as complete in Notion
- FR30: Client can review delivery report with all win conditions checked
- FR31: Client can confirm project completion via email or Slack
- FR32: PM can trigger referral ask when client confirms project completion
- FR33: PM can record client satisfaction rating after project close

### Logistics Call Management

- FR34: PM can walk client through 2FA for each platform during live call
- FR35: Client can provide 2FA codes verbally during screen share
- FR36: PM can document platforms requiring 2FA with fallback methods
- FR37: PM can track credential collection progress during call
- FR38: PM can mark credentials as pending when 2FA fails
- FR39: PM can send async credential collection instructions (Loom video) for pending items
- FR40: PM can confirm all credentials collected or schedule same-day follow-up
- FR41: PM can read win conditions to client and confirm understanding

### Progress Tracking & Updates

- FR42: PM can send progress update to client on scheduled days (Tuesday/Friday)
- FR43: PM can track project timeline against milestones in Notion
- FR44: PM can view all active client project statuses in single view
- FR45: Team member can see credential pending status for their assigned projects
- FR46: PM can batch client Slack responses during availability window
- FR47: System can track project lifecycle status (Paid → Onboarding → Active → Delivered → Closed)

### Team Communication & Coordination

- FR48: Team can receive notification when new client onboards
- FR49: Team member can receive notification when granted credential access
- FR50: Team member can receive notification when credential access expires
- FR51: PM can receive alert within 5 minutes when any automation step fails
- FR52: Team can access documented manual fallback for any failed automation

### System Administration

- FR53: PM can run environment validation script to confirm all integrations working
- FR54: PM can enable dry-run mode that logs emails without sending, posts Slack to test channel only, and makes Notion read-only
- FR55: PM can mark test records in Notion to isolate from production data
- FR56: PM can export/import n8n workflows for version control
- FR57: System can maintain separate integration modules for each external service (Stripe, Notion, Slack, Gmail, 1Password) to enable independent failure handling

## Non-Functional Requirements

### Performance

| Requirement | Target | Measurement |
|-------------|--------|-------------|
| NFR-P1: Stripe webhook to first email | < 30 seconds | n8n workflow execution logs |
| NFR-P2: Next-steps email delivery | < 5 minutes from payment | n8n workflow execution logs |
| NFR-P3: Slack channel creation | < 1 minute from payment | Slack API response timestamp |
| NFR-P4: Automation failure alert | < 5 minutes from failure | Alert timestamp vs failure timestamp |
| NFR-P5: Notion database updates | < 10 seconds per operation | API response time |

**Performance Rationale:** The 5-minute post-payment experience is the core value proposition. If gratitude email arrives late, buyer remorse prevention fails.

### Security

| Requirement | Specification | Verification |
|-------------|---------------|--------------|
| NFR-S1: Credential storage | All credentials stored exclusively in 1Password encrypted vault | Audit: no credentials in Slack, email, Notion, git |
| NFR-S2: Role-based access | Team members see only credentials for assigned projects | 1Password access logs |
| NFR-S3: Credential revocation | Access removed within 24 hours of project close | Revocation timestamp audit |
| NFR-S4: API key management | Production secrets only in n8n credential store, never in code | Git scanning, code review |
| NFR-S5: Temporary access | Contractor access time-limited with explicit expiry | 1Password access policy |
| NFR-S6: Audit trail | All credential access events logged with actor and timestamp | 1Password activity log |
| NFR-S7: Development credentials | Development uses `.env.local` with test credentials only; production credentials never leave 1Password/n8n credential store | Code review, .gitignore verification |

**Security Rationale:** We handle client platform credentials. A breach would damage trust and potentially expose client systems.

### Reliability

| Requirement | Target | Fallback |
|-------------|--------|----------|
| NFR-R1: Onboarding automation uptime | 99.9% measured monthly, excluding scheduled maintenance | Manual execution within 30 minutes |
| NFR-R2: Webhook processing | 99.9% success rate | Notion status change as backup trigger |
| NFR-R3: Email delivery | 100% delivery (with retries) | Gmail backup sender |
| NFR-R4: Slack operations | 99% success rate | Manual channel creation |
| NFR-R5: Notion operations | Retry 3x with exponential backoff (1s, 5s, 30s) before fallback | Manual update after retries exhausted |
| NFR-R6: Graceful degradation | Each agent fails independently | Documented manual fallback per agent |
| NFR-R7: Agent status visibility | Each agent publishes status (operational/degraded/failed) via Notion field | Status dashboard or Notion view |

**Reliability Rationale:** Client experience depends on automation working. Every failure pathway has a documented manual fallback.

### Integration

| Requirement | Specification | Monitoring |
|-------------|---------------|------------|
| NFR-I1: Integration isolation | Each external service has separate integration module | Code architecture review |
| NFR-I2: Stripe webhook | Handle `payment_intent.succeeded` event reliably | Stripe dashboard + n8n logs |
| NFR-I3: Notion API | Use stable API version (2022-06-28), monitor deprecation | Quarterly version check |
| NFR-I4: Slack API | Use stable bot scopes only, avoid beta features | Scope audit at setup |
| NFR-I5: Gmail API | Authenticated sender with proper SPF/DKIM | Deliverability monitoring |
| NFR-I6: 1Password CLI | Pin to v2.x, test before any updates | Version lock in docs |
| NFR-I7: Integration health check | Environment validation script confirms all connections | Pre-deployment script |
| NFR-I8: Circuit breaker | If integration fails 3x consecutively, disable pathway and alert (prevent cascade) | Alert on circuit open |
| NFR-I9: Webhook idempotency | Webhook handlers must be idempotent - duplicate events produce same result without side effects | Duplicate event testing |

**Integration Rationale:** Five external services means five potential failure points. Isolation and circuit breakers ensure one service failure doesn't cascade.

### Scalability (Limited Scope)

| Requirement | Target | Notes |
|-------------|--------|-------|
| NFR-SC1: Concurrent projects | Support 10+ active client projects simultaneously | Current ceiling, revisit at 15+ |
| NFR-SC2: Team size | Support 3-5 team members with role-based access | Expand if team grows |

**Scalability Rationale:** This is an internal tool for a small team. Over-engineering for massive scale would waste effort. Revisit if usage patterns change.

### Observability

| Requirement | Specification |
|-------------|---------------|
| NFR-O1: Structured logging | All automation steps emit structured logs with correlation ID linking related events |
| NFR-O2: Performance metrics | Webhook-to-email latency and other key metrics tracked and dashboarded |
| NFR-O3: Integration health | Single view showing health status of all external service connections |

**Observability Rationale:** Without observability, we won't know if NFRs are being met until a client complains. Correlation IDs enable end-to-end debugging.

### Testability

| Requirement | Specification |
|-------------|---------------|
| NFR-T1: Dry-run mode | All automations support dry-run that logs without executing |
| NFR-T2: Test isolation | Test records marked with `Test = true`, isolated from production |
| NFR-T3: Test cleanup | Test Slack channels auto-delete after 24 hours |
| NFR-T4: Environment validation | Script confirms all integrations before deployment |
| NFR-T5: Dry-run fidelity | Dry-run mode produces identical logs to production mode, minus actual side effects |
| NFR-T6: Credential isolation | Production and test environments share no credentials or API keys |

**Testability Rationale:** We need to test the full onboarding flow without affecting real clients or sending real emails.

### Data Retention

| Requirement | Retention Period | Notes |
|-------------|------------------|-------|
| NFR-D1: Audit logs | 12 months | Credential access, win condition changes |
| NFR-D2: Project data | 24 months after project close | Client records, delivery reports |
| NFR-D3: Test data | 7 days maximum | Auto-cleanup of test records |

**Data Retention Rationale:** Balance compliance needs (audit trail) with storage efficiency (test data cleanup).
