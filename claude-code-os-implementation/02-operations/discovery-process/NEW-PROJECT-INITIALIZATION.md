# New Active-Projects Initialization Process

## Purpose
Standard process for creating new project folders in `active-projects/` to ensure consistency, completeness, and effective project management.

---

## When to Create a New Project

Create a new active-project folder when:
- A discovery call leads to a paid engagement
- A client commits to a project (verbal or written agreement)
- You begin scoping/prototyping work that may lead to revenue
- A strategic partnership requires tracking (even if not immediately billable)

**DO NOT create folders for:**
- Cold prospects with no engagement
- One-off questions or casual conversations
- Internal experiments unrelated to client work

---

## Initialization Checklist

### Step 1: Create Folder Structure
```bash
cd claude-code-os-implementation/02-operations/project-management/active-projects/
mkdir {project-name}
cd {project-name}
```

**Folder naming convention:**
- Use lowercase with hyphens
- Use client/company name (e.g., `concrete-ceo`, `ascension-capital`)
- Keep it short and recognizable

### Step 2: Create Core Files

Create these **required** files in order:

1. **README.md** - Project navigation hub
2. **PROJECT-OVERVIEW.md** - Complete project details
3. **ACTION-ITEMS.md** - Next steps tracking
4. **DISCOVERY-NOTES.md** or **MEETING-SUMMARY.md** - Initial context

Create these **conditional** files as needed:

- **TECHNICAL-ARCHITECTURE.md** - If building software
- **DELIVERY-STATUS.md** - If in active delivery phase
- **FINANCIAL-SUMMARY.md** - If complex pricing/invoicing

### Step 3: Create Subdirectories

**Standard subdirectories:**

```
{project-name}/
├── meetings/
│   ├── discovery/           # Initial discovery calls
│   ├── check-ins/           # Regular status meetings
│   └── feedback/            # Client feedback sessions
├── docs/
│   ├── requirements/        # Business requirements
│   ├── testing/             # Test plans/results
│   └── deployment/          # Deployment guides
└── deliverables/
    ├── proposals/           # Proposals and scopes
    ├── prototypes/          # Demo/prototype artifacts
    └── documentation/       # User guides, training
```

**Technical projects add:**
```
├── technical/
│   ├── codebase-reference.md
│   ├── api-documentation.md
│   ├── database-schema.md
│   └── infrastructure.md
└── audit/
    └── ERROR-LOG.md         # Bug tracking
```

**Consulting/audit projects add:**
```
├── audit/
│   ├── findings.md
│   ├── recommendations.md
│   └── deliverables/
└── research/
    ├── competitive-analysis/
    └── market-research/
```

---

## File Templates

### README.md Template

```markdown
# {Project Name} - {One-line Description}

**Client:** {Client Name}
**Project Type:** {Automation / Audit / Consulting / Development}
**Status:** {Discovery / Scoping / Delivery / On Hold}
**Priority:** {P0-P5 based on strategic-priorities.md}
**Started:** {Month Year}

---

## Folder Structure

```
{project-name}/
├── README.md                       # This file
├── PROJECT-OVERVIEW.md            # Complete project details
├── ACTION-ITEMS.md                # Next steps tracking
├── MEETING-SUMMARY.md             # Initial discovery/meeting notes
├── meetings/
│   ├── discovery/
│   ├── check-ins/
│   └── feedback/
├── docs/
│   ├── requirements/
│   └── deliverables/
└── deliverables/
    └── proposals/
```

---

## Quick Links

**📋 Current Status:**
- [PROJECT-OVERVIEW.md](./PROJECT-OVERVIEW.md) - Complete project information
- [ACTION-ITEMS.md](./ACTION-ITEMS.md) - What's next

**📊 Business Context:**
- [MEETING-SUMMARY.md](./MEETING-SUMMARY.md) - Initial context
- [Financial Summary](./PROJECT-OVERVIEW.md#financial-summary)

---

## Current Status

**Phase:** {Current phase}
**Health:** {🟢 On Track / 🟡 At Risk / 🔴 Blocked}
**Last Updated:** {Date}

**Completed:**
- [ ] Discovery call
- [ ] Requirements gathering
- [ ] Scope/proposal delivered
- [ ] Contract signed
- [ ] Development started
- [ ] Client testing
- [ ] Production delivery
- [ ] Payment collected

**Next Actions:**
1. {Immediate next step}
2. {Second priority}
3. {Third priority}

---

## Project Summary

### Business Problem
{2-3 sentences describing the client's pain point}

### Solution
{2-3 sentences describing what you're building/delivering}

---

## Key Contacts

**Primary Stakeholder:** {Name}
**Decision Maker:** {Name}
**Technical Contact:** {Name if applicable}

---

**For detailed information:** See [PROJECT-OVERVIEW.md](./PROJECT-OVERVIEW.md)
```

---

### PROJECT-OVERVIEW.md Template

```markdown
# Project: {Client Name} - {Project Title}

## Overview
**Client:** {Client Name}
**Type:** {Project Type}
**Status:** {Current Status}
**Priority:** {P0-P5}
**Health:** {🟢/🟡/🔴}

---

## Project Financials

| Item | Amount | Status |
|------|--------|--------|
| **Total Project Value** | ${X,XXX} | {Agreed/Pending} |
| Discovery & Scoping | ${XXX} | {Status} |
| Development/Delivery | ${X,XXX} | {Status} |
| **Developer Cost** | ${XXX} | {If applicable} |
| **Your Margin** | ${XXX} | {Your cut} |
| **Sales Fee** | ${XXX} | {Linh/Mikael cut} |
| **Net Profit** | ${XXX} | {Your take-home} |

**Payment Terms:** {Terms}
**Payment Status:** [ ] Invoiced [ ] Collected

---

## Business Problem

{Detailed description of what problem you're solving}

### Current State
- {Pain point 1}
- {Pain point 2}
- {Pain point 3}

### Desired State
- {Goal 1}
- {Goal 2}
- {Goal 3}

---

## Solution

{Detailed description of what you're delivering}

### Key Features
1. {Feature 1}
2. {Feature 2}
3. {Feature 3}

### Success Metrics
- **{Metric 1}:** {Target}
- **{Metric 2}:** {Target}
- **{Metric 3}:** {Target}

---

## Progress Tracker

### Discovery Phase
- [ ] Initial consultation
- [ ] Requirements gathering
- [ ] Scope definition
- [ ] Proposal delivery

### Development/Delivery Phase
- [ ] {Milestone 1}
- [ ] {Milestone 2}
- [ ] {Milestone 3}

### Completion Phase
- [ ] Client testing
- [ ] Feedback implementation
- [ ] Final delivery
- [ ] Payment collection

---

## Team

**Architect:** {Your name}
**Developer:** {Name or "Delegated to {developer}"}
**Client Stakeholder:** {Name}

---

## Timeline

| Milestone | Target Date | Actual Date | Status |
|-----------|------------|-------------|---------|
| Project Kickoff | {Date} | {Date} | {Status} |
| Discovery Complete | {Date} | {Date} | {Status} |
| Delivery | {Date} | - | {Status} |

---

## Communication Log

| Date | Type | Participants | Summary | Action Items |
|------|------|--------------|---------|--------------|
| {Date} | {Type} | {Names} | {Summary} | {Actions} |

---

## Risks & Mitigation

| Risk | Probability | Impact | Mitigation | Status |
|------|------------|--------|------------|---------|
| {Risk 1} | {H/M/L} | {H/M/L} | {Mitigation} | {Status} |

---

## Next Actions

### Immediate (This Week)
1. {Action 1}
2. {Action 2}

### Short-term (Next 2 Weeks)
1. {Action 1}
2. {Action 2}

### Project Completion
1. {Action 1}
2. {Action 2}

---

**Project Status:** {Status emoji and text}
**Next Milestone:** {Milestone}
**Escalation Contact:** {Name}
```

---

### ACTION-ITEMS.md Template

```markdown
# Action Items - {Project Name}

**Last Updated:** {Date}
**Status:** {Active/On Hold/Complete}

---

## Critical Path Items (P0)

| # | Action | Owner | Deadline | Status | Notes |
|---|--------|-------|----------|--------|-------|
| 1 | {Action} | {Name} | {Date} | 🔴 Blocked / 🟡 In Progress / 🟢 Done | {Notes} |

---

## This Week

- [ ] {Task 1}
- [ ] {Task 2}
- [ ] {Task 3}

---

## Next Week

- [ ] {Task 1}
- [ ] {Task 2}

---

## Backlog

- [ ] {Task 1}
- [ ] {Task 2}

---

## Blocked Items

| Item | Blocker | Waiting On | Expected Resolution |
|------|---------|------------|-------------------|
| {Item} | {Blocker} | {Who/What} | {Date} |

---

## Completed Items

### Week of {Date}
- [x] {Task 1} - {Date completed}
- [x] {Task 2} - {Date completed}
```

---

## Step 4: Populate with Meeting Data

If you have meeting transcripts or notes:

1. **Create MEETING-SUMMARY.md** in meetings/discovery/
2. **Extract and organize:**
   - Key themes
   - Action items
   - Decisions made
   - Open questions
3. **Update ACTION-ITEMS.md** with extracted action items
4. **Fill PROJECT-OVERVIEW.md** with business context

---

## Step 5: Classify Project Priority

Based on `strategic-priorities.md`:

| Priority | Definition | Example |
|----------|------------|---------|
| **P0** | Revenue-generating, active delivery | Ascension Capital |
| **P1** | Agency infrastructure | Templates, processes |
| **P2** | Developer pipeline | Recruitment, evaluation |
| **P3** | Developer Academy | Long-term moat |
| **P4** | Credibility assets | Demo videos |
| **P5** | Content/inbound | Deferred until OBG |

**Update the README.md and PROJECT-OVERVIEW.md with the correct priority.**

---

## Step 6: Link to OBG

Every project must align with the **One Big Goal (OBG):**

**$50k/month revenue for 3+ consecutive months**

In PROJECT-OVERVIEW.md, add:

```markdown
## OBG Alignment

**Contribution to $50k/mo OBG:**
- {How this project drives revenue}
- {Expected monthly impact: $X,XXX}
- {Timeline to revenue}

**Strategic Rationale:**
- {Why this project matters beyond revenue}
```

---

## Step 7: Quality Check

Before considering the project initialized:

- [ ] README.md created and navigable
- [ ] PROJECT-OVERVIEW.md has complete business context
- [ ] ACTION-ITEMS.md has at least 3 next steps
- [ ] Meeting notes or discovery context captured
- [ ] Priority (P0-P5) assigned
- [ ] OBG alignment documented
- [ ] Folder structure matches project type
- [ ] All required subdirectories created

---

## Common Mistakes to Avoid

1. **Creating folders too early** - Wait until there's real engagement
2. **Incomplete PROJECT-OVERVIEW.md** - Financial section must be filled out
3. **Vague action items** - Be specific and deadline-driven
4. **Missing OBG alignment** - Every project must tie to revenue goal
5. **Inconsistent naming** - Use lowercase-with-hyphens
6. **Skipping meeting notes** - Capture context from day one

---

## Quick Start Commands

```bash
# Navigate to active-projects
cd ~/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/active-projects/

# Create new project
mkdir {project-name}
cd {project-name}

# Create subdirectories
mkdir -p meetings/{discovery,check-ins,feedback}
mkdir -p docs/{requirements,testing,deployment}
mkdir -p deliverables/{proposals,prototypes,documentation}

# Optional: Technical projects
mkdir -p technical
mkdir -p audit

# Create core files (use templates above)
touch README.md PROJECT-OVERVIEW.md ACTION-ITEMS.md MEETING-SUMMARY.md
```

---

## Example Projects for Reference

**Software Development:**
- `ascension-capital/` - Full automation project
- `plotter-mechanix/` - SaaS development

**Consulting/Audit:**
- `concrete-ceo/` - Partnership and audit services

**Quick Wins:**
- `idea-framework-website/` - Simple website build

---

## After Initialization

Once the project is initialized:

1. **Add to `/project-status` command** (if not already there)
2. **Update `strategic-objectives/` if major milestone**
3. **Track in daily planning** if P0-P1
4. **Review weekly** in weekly-review sessions

---

## Maintenance

**Weekly:**
- Update ACTION-ITEMS.md
- Check project health status
- Log communication

**Monthly:**
- Review OBG contribution
- Update financial tracking
- Archive completed items

---

## Questions?

If unclear on any step, reference:
- `strategic-priorities.md` for priority classification
- `obg-definition.md` for revenue alignment
- Existing projects (ascension-capital, plotter-mechanix) for structure examples

---

**Last Updated:** 2025-12-15
