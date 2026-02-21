# Nate Herk: How to Deliver AI Projects

**Source Type**: YouTube / Podcast
**Source**: Nate Herk - AI Workflow Delivery Process
**Date Captured**: December 27, 2024
**Relevance**: Delivery / Operations / Client Management

---

## Overview

Complete walkthrough of the entire process of fulfilling an AI workflow or agent after a client pays - from hosting decisions through handover and ongoing maintenance.

---

## Key Insights

### Insight 1: Client Should Always Host

**The Tactic**:
Each client has their own n8n instance. You work inside it as a consultant/developer, not as a platform provider.

**Why It Works**:
- Keeps you compliant with n8n licensing
- Client owns their data and infrastructure
- Clean separation of responsibilities
- No billing complexity around hosting

**How to Apply at AriseGroup**:
- Help clients set up their own n8n Cloud or self-hosted instance
- Get invited as a team member
- Never host multiple clients on same instance

**Status**: To Test

---

### Insight 2: Clients Own Their API Keys

**The Tactic**:
Client signs up for tools themselves, enters billing info, generates API key, pastes directly into n8n. You never touch the raw keys if possible.

**Why It Works**:
- Transparent billing (they see usage)
- No markup confusion
- Clean professional relationship
- Avoids "billing babysitter" role

**How to Apply at AriseGroup**:
- Send Loom walkthrough of how to create each API key
- Walk through on Zoom call if needed
- If key transfer needed, use encrypted vault with one-time links

**Status**: To Test

---

### Insight 3: Test with Real Client Data

**The Tactic**:
Before building, ask client for sample data that looks like real usage (emails, tickets, CRM records). Agree on what success looks like and what must never happen.

**Why It Works**:
- Catches edge cases before production
- Client understands what to expect
- Clear success criteria
- Prevents "magic black box" feeling

**How to Apply at AriseGroup**:
- Add to contract/scope: "Client provides sample data within X days"
- Define success criteria before building
- Log all test results for evidence

**Status**: To Test

---

### Insight 4: Build for Failure

**The Tactic**:
Accept you don't know what you don't know. Build guardrails: timeouts, error workflows, failure logging to Google Sheets, graceful degradation.

**Why It Works**:
- Real users reveal edge cases you didn't think of
- System breaks safely and quietly
- Gives info to fix fast
- Client feels supported

**How to Apply at AriseGroup**:
- Every workflow has error handling
- Log failures to trackable location
- Test worst-case scenarios intentionally

**Status**: To Test

---

### Insight 5: Separate Test and Production Environments

**The Tactic**:
Keep one version as backup/testing, push clean one to production. Never update production blindly - test updates on dev version first.

**Why It Works**:
- Avoids outages from updates
- Safe experimentation
- Professional software practice
- Easy rollback if needed

**How to Apply at AriseGroup**:
- Duplicate workflow before going live
- Keep backups on GitHub/Google Drive
- Automate backup process with n8n itself

**Status**: To Test

---

### Insight 6: Documentation = Trust

**The Tactic**:
Clear naming in each step. Sticky notes explaining logic. Loom walkthrough. Anyone could open workflow and understand it.

**Why It Works**:
- Client feels supported
- Avoids being the bottleneck
- Enables team handoff
- Protects both sides

**How to Apply at AriseGroup**:
- Every delivery includes Loom walkthrough
- Workflow has sticky note documentation
- PDF export of workflow structure

**Status**: To Test

---

### Insight 7: Scope Protection is Critical

**The Tactic**:
When client asks for more features during build, explicitly separate v1 scope from backlog for future phases. New features = new project.

**Why It Works**:
- Prevents unpaid work
- Keeps projects focused
- Creates natural upsell opportunities
- Maintains professional boundaries

**How to Apply at AriseGroup**:
- Contract defines "done" clearly
- Feature requests get logged, not immediately added
- "That's a great v2 feature" response ready

**Status**: Validated (already doing this)

---

### Insight 8: Maintenance Retainer Structure

**The Tactic**:
Separate ongoing agreement covering: bug fixes, small tweaks, updates, monitoring, security checks. Does NOT include new features or major scope changes.

**What It Covers**:
- Bug fixes
- Small tweaks
- Dependency updates
- Monitoring
- Basic security checks

**What Requires New Project**:
- New features
- New workflows
- Major scope changes

**How to Apply at AriseGroup**:
- Offer retainer after project completion
- Define service levels (critical = hours, minor = days)
- Clear boundary between maintenance and new work

**Status**: To Test

---

### Insight 9: Clear Exit Process

**The Tactic**:
Define in contract what happens if client wants to move away. What you'll hand over: exported workflows, documentation, handover call. What's included vs billable.

**Why It Works**:
- Professional relationship
- No hostage situations
- Client feels confident
- Clean closure if needed

**How to Apply at AriseGroup**:
- Add exit clause to contracts
- List specific deliverables for offboarding
- Handover call as standard

**Status**: To Test

---

## Nate's Delivery Checklist (from video)

1. **Hosting Decision** - Client hosts (recommended)
2. **Security Setup** - Credentials encrypted, webhooks hardened
3. **API Key Ownership** - Client owns and pays
4. **Testing/QA** - Real data, defined success criteria, guardrails
5. **Handover** - Clean workflow, documentation, Loom
6. **Legal/Billing** - Scope closed, final invoice, retainer decision
7. **Ongoing** - Maintenance terms clear, exit process defined

---

## Raw Notes

### Hosting Options (n8n specific)
- **Option 1 (Recommended)**: Client hosts n8n, you're consultant
- **Option 2**: You host for your own agency (internal only)
- **Option 3**: You host as product (requires commercial license - expensive)

### Security Checklist
- Credentials encrypted at rest, decrypted in memory
- Webhooks use HTTPS
- Signature verification for Stripe/GitHub/etc
- No sensitive data in webhook URLs
- Rate limits for abuse prevention
- Prompt guardrails for AI agents

### GDPR Considerations
- Data minimization (only fields needed)
- Limit who sees workflow runs
- Know where data flows for deletion requests
- May need Data Processing Agreement
- Self-hosting = true data sovereignty

### QA for AI Workflows
- Relevance/correctness check
- Tone/safety check
- Consistency check (same inputs = same outputs?)
- A/B test prompts and models
- Log inputs, outputs, errors, tokens

### Real Example: Personal Assistant Workflow
- Client found via YouTube
- Kickoff call: walked through getting API keys, invited to n8n
- Connected CRM, calendar, email on call
- Lots of back-and-forth on system prompt (normal for conversational AI)
- Protected scope when feature requests came
- v1 complete, then scoped v2

---

## Action Items

- [ ] Create delivery playbook based on this
- [ ] Update contract template with exit clause
- [ ] Add "client provides sample data" to scope requirements
- [ ] Create Loom template for API key setup
- [ ] Add error workflow standard to all builds

---

## Playbook Created

**Location**: `/agency-playbooks/delivery/ai-project-delivery-playbook.md`
