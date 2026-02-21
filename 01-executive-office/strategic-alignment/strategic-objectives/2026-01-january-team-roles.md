# January 2026 - Team Roles & Responsibilities

**Created:** December 28, 2025
**Context:** 4-5 active clients requiring real business solution delivery
**Source:** [12/28 BMAD + AutoClaude Sync](../../internal-business-meetings/meetings/2025-12-28-bmad-autocloud-sync/summary.md)

---

## Core Philosophy

Everyone plays to their strengths. The agency operates as a delivery machine with clear handoffs between roles. No one does work outside their zone of genius unless absolutely necessary.

**Key Insight:** "Time is the ultimate resource. We are the product - our time. The more safeguards we put in place, the less stressful and more profitable delivery becomes."

---

## The Four Roles

### Chris Andrade - Lead Generator & Relationship Builder

**Zone of Genius:** Opening doors, building trust, bringing in high-quality leads

**Responsibilities:**
- Source and qualify new leads
- Initial relationship building with potential clients
- Warm handoffs to Mekaiel/Trent for deeper engagement
- Maintain relationships with referral sources
- Attend networking events and build pipeline

**Does NOT Do:**
- Discovery calls (hands off to Trent/Mekaiel)
- Requirements gathering
- Technical scoping
- Project delivery

**Success Metrics:**
- Number of qualified leads brought in
- Lead-to-close conversion rate
- Referral source relationships maintained

**Track Record:** Brought in essentially all leads to date, all of which have been high-quality paying clients.

---

### Trent Christopher - Technical Lead & Production Developer

**Zone of Genius:** Agentic workflows, Notion systems, client rapport, technical demonstrations, production development

**Responsibilities:**
- Technical discovery calls with potential clients
- Client onboarding sessions (builds trust and rapport)
- Agentic workflow design and architecture
- Notion workspace setup and systems design
- Technical demonstrations and prototyping
- **Production code development** (tag-teams with Matthew)
- **Final delivery testing and sign-off** (shared with Matthew)
- Support Mekaiel with technical validation during requirements

**Tools & Expertise:**
- Claude / AI coding agents
- Notion (advanced)
- N8N workflow automation
- Cloud infrastructure
- Systems architecture
- Production software development

**Does NOT Do:**
- Cold outreach or lead sourcing
- Requirements documentation (hands off to Mekaiel)

**Success Metrics:**
- Client satisfaction on onboarding calls
- Technical designs approved and ready for build
- Production code quality and delivery
- Notion workspaces set up and operational

---

### Matthew Kerns - Production Engineer & Strategic Architect

**Zone of Genius:** Production-grade software, asking "why," ensuring builds match business needs, working through issues that don't work even with AI tools

**Responsibilities:**
- **Production code development** (tag-teams with Trent)
- Code review and production readiness
- Challenge assumptions - ensure what we're building is what the business actually needs
- Quality assurance before client delivery (shared with Trent)
- Technical decisions on architecture and tooling
- Review PRDs and mark "build-safe" items
- Keep builds constrained to approved scope
- Work through integration issues and edge cases AI can't solve

**Tools & Expertise:**
- Production software development
- Claude Code / AI coding agents
- AutoClaude for automated planning/execution
- BMAD Method for structured development
- Code review and testing
- System architecture

**Does NOT Do:**
- Lead sourcing
- Client relationship management (Mekaiel shields from client chaos)
- Requirements gathering (reviews, not gathers)
- Scope changes without PRD update

**Success Metrics:**
- Code quality and production stability
- Deliverables match SOW exactly
- No rework due to misalignment
- On-time delivery to spec

**Key Quote from Meeting:** "If I have clear things that I need to build, there's so many tools that I can build stuff quickly. But I also need to work through all the issues - there's gonna be so many issues that come up in development, even with all the AI tools in the world. There's things where it just doesn't work. And that's why I have a job."

**Dev Team Dynamic:** Matthew and Trent tag-team production development with AI coding agents. Both contribute to builds, both sign off on delivery. Division of work based on project needs and availability.

---

### Mekaiel Abdullahi - Product Manager & Requirements Bridge

**Zone of Genius:** Bridging sales and development, protecting developers from chaos, change management, coordinating multiple projects simultaneously

**Background:** 2.5 years managing 5-6 concurrent technical security integrations at embassies with various team sizes. Experienced in the chaos of multi-project coordination and client management.

**Responsibilities:**
- Own the PRD (Product Requirements Document) - single source of truth
- Gather and document requirements from sales/discovery
- Translate client needs into actionable development specs
- **Protect development team from client chaos and scope creep**
- Manage client communications (defined windows and channels)
- Run change management process for requirement changes
- Ensure quick-win sprint outputs map precisely to SOW
- Be the bridge between offer/sale and development

**The PRD Process:**
1. Sales/Discovery feeds into PRD
2. Mekaiel gathers additional requirements from client as needed
3. Mekaiel uses BMAD agents (PM, Analyst) to create comprehensive PRD
4. PRD reviewed and **signed off** by dev team (Matthew + Trent) for technical feasibility
5. Only dev-approved PRD items get built
6. Changes flow through Mekaiel → PRD update → dev sign-off → build

**Critical:** Development team must sign off on PRD before building begins. Mekaiel works to bring the PRD to a really good state by working with the client, then devs validate it's buildable.

**Key Insight from Mekaiel:** "Before you change the PRD, it has to come from a business funnel. If you're putting outputs in, they should be coming from inputs from a business funnel - not from whatever the customer wants. We have to frame the request through a business funnel."

**Does NOT Do:**
- Lead sourcing
- Production code development
- Technical architecture decisions
- Direct client problem-solving without PRD update

**Success Metrics:**
- PRD accuracy and completeness
- Developer protection (measured by interruption reduction)
- Scope contained to SOW
- Change requests properly documented and approved

**January Focus:** Create first PRD for Plotter Mechanix using BMAD (Analyst/PM agents), establish PRD creation process that can be replicated for future clients.

---

## The Delivery Flow

```
                    SALES SIDE                         DEV SIDE

Chris brings lead
       ↓
Trent runs discovery/onboarding call
       ↓
Mekaiel documents requirements → PRD v0
       ↓
Matthew reviews PRD → marks "build-safe" items
       ↓
Trent designs technical architecture/workflows
       ↓
Matthew + Trent build production code (tag-team with AI agents)
       ↓
Matthew + Trent sign off on delivery quality
       ↓
Mekaiel coordinates client sign-off
       ↓
                  DELIVERED & PAID
```

---

## Why Developer Protection Matters

**From the Meeting:**
> "Bro, you have to protect your time. Because people will be people. And it's like, cool, but you have to set up a system that protects you from the chaos of the client."

> "Keep [Matthew] as far away from the client as possible, because what you should be working out of is the structure. The client is chaos. You should only be working on it through the business frame."

> "I had my work email and Teams on my personal phone, and it was just bad. It was nonstop. So we gotta set up a system that protects you from the chaos of the client."

**The Solution:** Mekaiel acts as the shield. All client requests flow through him, get evaluated against SOW, and only approved items reach development.

---

## Client Communication Protocol

**Owner:** Mekaiel

**Rules:**
1. **Availability Windows:** Defined business hours when team responds to clients (not 24/7)
2. **Channels:** Slack for async during business hours, scheduled weekly check-ins for sync
3. **Emergency Line:** One defined path for true production emergencies only
4. **Weekly Check-ins:** Scheduled, predictable, not ad-hoc
5. **Change Requests:** All changes go through Mekaiel → PRD update process

**From Meeting:** "As long as you set expectations, they'll be fine. Give them a channel they can reach you during business hours, only during specific times. Otherwise, trust me, they'll be sitting in their office going 'Oh, can we do this? Can we do that?' and you don't have time for that."

**Goal:** Developers focus 100% on building, not client management.

---

## Change Management Protocol

**Owner:** Mekaiel

**Process:**
1. Client requests change
2. Mekaiel evaluates against SOW
3. If within scope → PRD update → Matthew reviews → build
4. If out of scope → Change request documented → pricing/timeline impact assessed → client approval → SOW addendum → PRD update → build
5. **Cutoff Point:** At defined milestone, no more changes accepted for current phase

**Key Principle:** "Once it reaches a certain stage, we can't go back and change what the plan was. Otherwise, we've lost development time. And that's our profit."

**From Meeting:** "At a certain stage, it's like, okay, we're figuring things out, a little chaotic, changes are fine. But once it reaches a certain stage, whatever that stage is, when we start building - we can't go back. We deliver what was promised. New requests go to next phase."

---

## PRD as Single Source of Truth

**Why PRD-First Development:**
- "The sooner we get the PRD, the better"
- "You shouldn't be building until we have that level of certainty"
- "Development should only work from the PRD"
- "The more safeguards we put in place, the better it will be and less stressful"

**What Feeds the PRD:**
1. Discovery call notes and transcripts
2. Client pain points and requirements
3. Technical feasibility assessment
4. SOW deliverables alignment
5. Internal deliverables mapping (like Miro boards)

**PRD vs SOW:**
- **SOW:** Intentionally high-level to protect the agency, defines what we commit to deliver
- **PRD:** Detailed internal document that specifies exactly how we'll deliver on the SOW
- Both must align, but PRD has the implementation details

---

## Documentation Requirements

**Every Meeting:**
- Recorded via Google Meet + Fathom/Fireflies (NOT Slack huddles - no video recording)
- Summary created and stored in appropriate project folder
- Action items extracted and assigned

**Why Not Slack Huddles:** "I'm a little bit like, I don't know about doing Slack huddles ever again. You don't record the video, and there's so much in there."

**Every Project:**
- PRD (Mekaiel owns)
- Technical design (Trent creates, Matthew reviews)
- SOW (maps to PRD deliverables)
- Meeting notes and decisions
- Internal deliverables mapping (Miro or similar)

---

## Task Management

**Primary Tool:** Notion (for task tracking, project status, client workspaces)
**Fallback:** Trello (if Notion setup is blocking progress)

**Requirements:**
- All tasks visible to whole team
- Clear ownership and deadlines
- Status updates at least daily during active sprints
- Connected to PRD items
- Kanban-style task assignment

---

## Toolchain for January

See [Development Framework Overview](../../../03-ai-growth-engine/development-framework/FRAMEWORK-OVERVIEW.md) and [Internal Development OS](../../../03-ai-growth-engine/development-framework/03-development-execution/00-INTERNAL-DEVELOPMENT-OS.md) for complete details.

### Planning & Context
- **Claude Code OS:** Centralized planning, context, documentation
- **BMAD Method:** Structured analysis, PRD creation, epics/stories (ALL team members use this)
- **AutoClaude:** Code planning, execution, automated review via worktrees

### BMAD Agents Used by Role

| Role | BMAD Agents | Purpose |
|------|-------------|---------|
| **Mekaiel** | PM Agent, Analyst Agent | PRD creation, requirements gathering |
| **Matthew + Trent** | Architect, Developer, Test Architect | Technical design, implementation, QA |
| **All** | Tech Writer | Documentation generation |

### Development
- **AutoClaude:** Runs in background building while team does other work
- **Claude Code:** Interactive development and issue resolution
- **N8N:** Workflow automation execution
- **Git Worktrees:** Isolated feature development for review

### The 5-Phase Development Lifecycle

```
PHASE 1: IDEATION & ANALYSIS (BMAD)
├── Brainstorming with AI agents
├── Research & solution exploration
└── → Decision: Build or delegate?

PHASE 2: PLANNING & SPECIFICATION (BMAD)
├── PRD creation (PM agent - Mekaiel)
├── Technical specs (Analyst agent)
├── Architecture design (Architect agent - Matthew/Trent)
└── → Dev team signs off on PRD

PHASE 3: AUTONOMOUS EXECUTION (AUTOCLAUDE)
├── Task sharding into stories
├── Parallel agent execution
├── Self-validating QA loops
└── → Working code in branch

PHASE 4: VALIDATION & TESTING
├── Automated test execution
├── Error handling validation
└── → All tests pass

PHASE 5: INTEGRATION & DELIVERY
├── AI-powered merge conflict resolution
├── Final QA review
└── → Production-ready deliverable
```

### Communication & Documentation
- **Google Meet:** All meetings (video recording)
- **Fathom/Fireflies:** Transcription and AI summaries
- **Slack:** Async communication (NOT for meetings)
- **Notion/Trello:** Task tracking

### Optimizing Human Time

**Goal:** Minimize human review time, work time, and meeting time through strategic planning.

| Activity | Optimization Strategy |
|----------|----------------------|
| **Human Review** | AI does first pass, humans review AI output |
| **Work Time** | AutoClaude runs in background while humans do other tasks |
| **Meeting Time** | Async-first communication, scheduled syncs only |
| **Planning** | BMAD agents do heavy lifting, humans validate |

---

## Handoff Checklist

### Lead → Discovery (Chris → Trent)
- [ ] Lead qualified and interested
- [ ] Basic context shared (business type, pain point, budget range)
- [ ] Meeting scheduled

### Discovery → PRD (Trent → Mekaiel)
- [ ] Discovery call recorded and transcribed
- [ ] Key requirements documented
- [ ] Technical feasibility confirmed
- [ ] Ready for PRD creation

### PRD → Build (Mekaiel → Matthew + Trent)
- [ ] PRD v0 complete (created with BMAD PM/Analyst agents)
- [ ] **Dev team (Matthew + Trent) signs off on PRD** - confirms it's buildable
- [ ] SOW aligned with PRD deliverables
- [ ] Scope locked for phase
- [ ] Work assigned between Matthew and Trent
- [ ] High-certainty items identified for immediate build
- [ ] AutoClaude tasks created from approved PRD items

### Build → Delivery (Matthew + Trent → Mekaiel)
- [ ] Code complete and tested
- [ ] Both devs sign off on quality
- [ ] Matches PRD exactly
- [ ] Ready for client demo/handoff
- [ ] Documentation updated

---

## Scaling Readiness

**Current State:** 4-5 active clients (Plotter Mechanix priority)
**Target:** Handle February event pipeline surge

**From Meeting:** "We're going to be so busy. It's going to be crazy. So we got to have our processes dialed in."

**Key Enablers:**
1. Clear role separation = no stepping on toes
2. PRD-first = no wasted build time
3. Change management = scope contained
4. Documentation = anyone can pick up context
5. BMAD/AutoClaude + AI coding agents = multiply output without multiplying hours
6. Two production developers = parallel workstreams
7. Developer protection = focus on building, not client management

**The AI Advantage:** "This is how we can optimize - we pay like $100-200/month for Claude subscription. AutoClaude can be running, as long as we keep it running on stuff, it'll just keep building. It'll work for us."

---

## Role Boundaries Summary

| Activity | Chris | Trent | Matthew | Mekaiel |
|----------|-------|-------|---------|---------|
| Lead sourcing | **OWN** | - | - | - |
| Relationship building | **OWN** | Support | - | Support |
| Discovery calls | - | **OWN** | - | Support |
| Client onboarding | - | **OWN** | - | Support |
| Technical design | - | **OWN** | Review | - |
| PRD creation | - | Input | Review | **OWN** |
| Production build | - | **SHARED** | **SHARED** | - |
| Code review | - | **SHARED** | **SHARED** | - |
| Delivery sign-off | - | **SHARED** | **SHARED** | - |
| Client comms | - | Support | - | **OWN** |
| Change management | - | - | - | **OWN** |

---

## January Priorities by Role

### Chris
- Continue lead sourcing and relationship building
- Prep for February event promotion
- Warm contacts outreach starting mid-January

### Trent
- Set up Notion workspace for task management
- Technical design for Plotter Mechanix
- Support onboarding calls as needed
- Tag-team builds with Matthew

### Matthew
- Review Mekaiel's PRD drafts, mark build-safe items
- Keep AutoClaude from running ahead of PRD
- Build production code from approved PRD items
- Work through integration issues

### Mekaiel
- **Priority #1:** Create PRD v0 for Plotter Mechanix using BMAD
- Draft client comms policy with specific windows/channels
- Document PRD creation process for future clients
- Get socials/brand on-point before mid-January event promo
- Document the brand setup process to share with team

---

## SOW Learnings for Future Contracts

**From reviewing Plotter Mechanix SOW:**
- SOW was intentionally vague to protect us while we figure things out
- Internal Miro deliverables were more specific than SOW
- Need to better align SOW with specific internal deliverables for future contracts
- Example: SOW says "Supporting SOPs" but Miro specifies "4 main how-to guides"

**Action:** Sync with Trent to reconcile SOW vs internal deliverables (Miro) and tighten future SOW templates.

---

## Next Steps

1. **Mekaiel (Today):** Draft PRD v0 for Plotter Mechanix using BMAD, share for Matthew's review
2. **Mekaiel:** Post Miro deliverables link in Plotter channel, map to SOW items
3. **Matthew:** Review PRD v0 when ready, mark build-safe items, propose initial epics/stories
4. **Both:** Meet with Trent to align SOW vs internal deliverables
5. **Matthew:** Keep AutoClaude from running ahead of PRD (pause/redirect tasks as needed)
6. **Mekaiel:** Draft client comms policy for team approval
7. **Mekaiel:** Document socials/brand rollout process, share guide with team
8. **Both:** Regroup later today to assign tasks Kanban-style

---

**Review Cadence:** Weekly during January, adjust as needed
**Owner:** Matthew Kerns (Strategic Alignment)
**Contributors:** All team members
