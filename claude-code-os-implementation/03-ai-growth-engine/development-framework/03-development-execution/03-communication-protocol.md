# Communication Protocol

## Purpose
Eliminate unnecessary back-and-forth, maintain clear expectations, and ensure efficient information flow between all stakeholders throughout the development process.

## Communication Principles

```
REDUCE: Back-and-forth iterations
INCREASE: First-time understanding
DOCUMENT: Every decision
ANTICIPATE: Common questions
BATCH: Non-urgent items
ESCALATE: Blockers immediately
```

---

## Stakeholder Communication Matrix

| Stakeholder | Primary Channel | Backup | Response Time | Update Frequency |
|-------------|-----------------|--------|---------------|------------------|
| Developer | Slack/Discord | Email | <4 hours | Daily |
| Client Tech | Slack | Email | <8 hours | 2-3x/week |
| Client Business | Email | Phone | <24 hours | Weekly |
| Internal Team | Slack | Text | <1 hour | As needed |
| Sales Team | Slack | Email | <4 hours | Weekly |

---

## Channel Guidelines

### Slack/Discord Rules
```markdown
## Channel Structure
#project-[name]-general     → General discussion
#project-[name]-dev         → Development updates
#project-[name]-client      → Client communication
#project-[name]-internal    → Internal only

## Message Format
✅ GOOD: "User auth complete. PR #123 ready for review. Next: Starting payment integration."
❌ BAD: "Done with auth"

## Threading Rules
- Use threads for discussions
- Main channel for announcements
- Pin important decisions
- Archive when project ends
```

### Email Templates

#### Project Kickoff Email
```markdown
Subject: [Project Name] - Development Starting

Hi [Client],

We're starting development on your [project name] today.

**Key Information:**
- Project Dashboard: [URL]
- Slack Channel: [invite link]
- First Milestone Due: [date]
- Your Point of Contact: [name]

**Communication Schedule:**
- Daily Updates: In Slack #project-channel
- Weekly Reports: Email every Friday
- Milestone Demos: [dates]

**What We Need From You:**
1. [Specific item]
2. [Specific item]
3. [Specific item]

**Next Steps:**
1. Accept Slack invite
2. Review attached project plan
3. Confirm [specific item]

Looking forward to a successful project!

Best,
[Your name]
```

#### Status Update Email
```markdown
Subject: [Project Name] - Week [#] Update

Hi [Client],

Quick update on your project:

**Status**: 🟢 On Track
**Completion**: 45% complete
**Next Milestone**: [Date]

**This Week's Progress:**
- ✅ [Achievement]
- ✅ [Achievement]
- ✅ [Achievement]

**Next Week's Plan:**
- [ ] [Task]
- [ ] [Task]
- [ ] [Task]

**Need From You:**
- [If anything]

Details in attached report.

Best,
[Your name]
```

---

## Meeting Protocols

### Meeting Efficiency Rules
```
1. No meeting without agenda
2. No meeting without decision maker
3. Start with outcome needed
4. End with action items
5. Follow up within 24 hours
```

### Meeting Templates

#### Discovery Call Agenda (60 min)
```
1. Introductions (5 min)
2. Problem Overview (15 min)
3. Current Process (10 min)
4. Desired Outcome (10 min)
5. Technical Requirements (10 min)
6. Timeline & Budget (5 min)
7. Next Steps (5 min)
```

#### Weekly Check-in Agenda (30 min)
```
1. Progress Update (5 min)
2. Demo/Show Work (10 min)
3. Feedback & Questions (10 min)
4. Next Week Preview (3 min)
5. Action Items (2 min)
```

#### Milestone Demo Agenda (45 min)
```
1. Milestone Summary (5 min)
2. Live Demonstration (20 min)
3. Q&A (10 min)
4. Feedback Collection (5 min)
5. Next Steps & Payment (5 min)
```

### Meeting Follow-up Template
```markdown
Subject: [Meeting Type] - Action Items

Thanks for your time today. Here's what we agreed:

**Decisions Made:**
- [Decision 1]
- [Decision 2]

**Action Items:**
- [Person]: [Task] by [Date]
- [Person]: [Task] by [Date]

**Next Meeting:** [Date/Time]

Please confirm receipt and agreement.

Best,
[Your name]
```

---

## Reducing Back-and-Forth

### Anticipate Questions Method
```markdown
## When Sharing Work
Instead of: "Here's the login page"

Say: "Here's the login page:
- URL: [staging URL]
- Test credentials: user/pass
- Supports: email & Google OAuth
- Password requirements: 8+ chars, 1 number
- Forgot password: working
- Known issue: [if any]
- Next: Adding 2FA"
```

### Complete Information Framework
```
For Every Communication Include:
1. WHAT: The specific item/issue
2. WHY: The reason/context
3. WHO: Who needs to act
4. WHEN: The deadline
5. HOW: Any specific requirements
6. NEXT: What happens after
```

### Common Q&A Preemption
```markdown
## Preemptive FAQ
Before they ask, provide:

**"When will it be done?"**
→ Include timeline in every update

**"How do I test it?"**
→ Always provide test credentials

**"What's the status?"**
→ Start every message with status

**"What do you need from me?"**
→ End with clear action items

**"How much will it cost?"**
→ Reference agreed budget/scope
```

---

## Documentation Standards

### Decision Documentation
```markdown
## Decision: [Title]
**Date**: [Date]
**Participants**: [Names]
**Context**: [Why needed]

**Options Considered:**
1. Option A: [Pros/Cons]
2. Option B: [Pros/Cons]

**Decision**: [What was chosen]
**Rationale**: [Why]
**Impact**: [What changes]

**Action Items:**
- [ ] [Task]
- [ ] [Task]
```

### Change Request Documentation
```markdown
## Change Request #[Number]
**Requested By**: [Name]
**Date**: [Date]
**Current Scope**: [What was agreed]
**Requested Change**: [What they want]

**Impact Analysis:**
- Timeline: +[X] days
- Budget: +$[Amount]
- Risk: [Assessment]

**Options:**
1. Add to current milestone (+time +cost)
2. Swap with [feature] (no impact)
3. Defer to Phase 2 (no impact)

**Client Decision**: [What they chose]
**Confirmed Via**: [Email/Slack/Call]
```

---

## Crisis Communication

### Blocker Escalation
```
Level 1 (Try to solve - 1 hour):
- Check documentation
- Try alternative approach
- Ask team member

Level 2 (Escalate - immediate):
- Notify architect
- Document blocker details
- Suggest solutions

Level 3 (Client involvement - same day):
- Explain impact
- Present options
- Get decision
```

### Bad News Delivery Template
```markdown
Subject: [Project] - Important Update Required

Hi [Client],

I need to make you aware of an issue we've discovered:

**Issue**: [Clear description]
**Impact**: [What this means]
**Root Cause**: [Why it happened]

**Options:**
1. [Option with tradeoffs]
2. [Option with tradeoffs]
3. [Option with tradeoffs]

**Recommendation**: Option [X] because [reason]

**Need Decision By**: [Time]

I'm available to discuss immediately.

Best,
[Your name]
```

---

## Async Communication Best Practices

### Response Time Expectations
| Priority | Response Time | Examples |
|----------|--------------|----------|
| 🔴 Critical | <1 hour | System down, blocker |
| 🟡 High | <4 hours | Needs decision today |
| 🟢 Normal | <24 hours | Regular updates |
| ⚪ Low | <48 hours | FYI, documentation |

### Message Formatting
```markdown
## Clear Subject Lines
✅ "[Project] Milestone 2 Complete - Need Approval"
✅ "[URGENT] Blocker: API Access Needed"
✅ "[FYI] Weekly Report Attached"

❌ "Update"
❌ "Question"
❌ "Hey"

## Message Structure
1. **Status/Priority** indicator
2. **Key message** in first line
3. **Context** if needed
4. **Action needed** clearly stated
5. **Deadline** if applicable
```

---

## Client Education

### Setting Expectations Early
```markdown
## How We'll Work Together

**Daily**: We'll be heads down building
**2-3x/Week**: You'll see progress updates
**Weekly**: You'll get a detailed report
**Per Milestone**: We'll demo and get approval

**Your Time Commitment**:
- 30 min/week for check-ins
- 45 min per milestone demo
- Quick responses on blockers

**Best Practices**:
- Batch non-urgent questions
- Use agreed channels
- Reference project documents
- Trust the process
```

---

## Internal Communication

### Developer Handoff Template
```markdown
## Project Handoff: [Name]

**Repository**: [URL]
**Documentation**: [URL]
**Client Contact**: [Name/Email]

**Current Status**:
- Milestone: [X] of [Y]
- Completion: [%]
- Blockers: [List]

**Technical Context**:
- Stack: [Technologies]
- Architecture: [Overview]
- Quirks: [Any gotchas]

**Recent Changes**:
- [Change 1]
- [Change 2]

**Next Tasks**:
1. [Priority 1]
2. [Priority 2]

**Client Personality**:
- Communication style: [Notes]
- Preferences: [Notes]
- Triggers: [What to avoid]
```

---

## Communication Metrics

### Track and Improve
| Metric | Target | Measure |
|--------|--------|---------|
| Response time | <4 hours | Average response |
| Questions per task | <2 | Back-and-forth count |
| Meeting efficiency | >80% | Decisions made / Time spent |
| Client satisfaction | >90% | Regular surveys |
| Miscommunications | <1/week | Track and analyze |

---

## The Communication Mantras

```
"Overcommunicate progress, undercommunicate problems"
"No surprises - ever"
"Document decisions or they didn't happen"
"One source of truth"
"Batch the small, escalate the big"
```