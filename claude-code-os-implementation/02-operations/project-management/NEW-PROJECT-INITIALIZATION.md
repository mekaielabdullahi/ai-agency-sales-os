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

## Standard Folder Structure

```
[project-name]/
├── README.md                    # Project overview and navigation hub
├── audit/                       # Initial assessments, tech audits
├── communications/              # Client email threads, slack exports
├── deliverables/                # Final outputs delivered to client
├── discovery/                   # Discovery session materials, research
├── docs/                        # Project documentation, specs
├── meetings/                    # Meeting notes (date-prefixed subfolders)
│   └── YYYY-MM-DD-[description]/
│       ├── notes.md
│       ├── transcript.md
│       └── action-items.md
├── offer/                       # Proposals, pricing, contracts
│   └── drafts/                  # Offer iterations
├── planning/                    # Project planning
│   ├── proposals/               # Formal proposals
│   └── roadmap/                 # Implementation roadmaps
└── status/                      # Status updates, progress reports
```

### When to Create Each Folder

| Folder | Create When |
|--------|-------------|
| `audit/` | Tech stack assessment or business audit performed |
| `communications/` | Ongoing client comms to preserve |
| `deliverables/` | Any work product delivered to client |
| `discovery/` | Discovery call scheduled or research started |
| `docs/` | Technical specs or documentation needed |
| `meetings/` | First meeting scheduled |
| `offer/` | Proposal or pricing being prepared |
| `planning/` | Active planning/roadmapping underway |
| `status/` | Regular status reporting to client |

---

## Initialization Checklist

### Step 1: Create Folder Structure

```bash
cd claude-code-os-implementation/02-operations/project-management/active-projects/
mkdir {project-name}
cd {project-name}

# Create subdirectories
mkdir -p audit communications deliverables discovery docs
mkdir -p meetings offer/drafts
mkdir -p planning/{proposals,roadmap} status
```

**Folder naming convention:**
- Use lowercase with hyphens
- Use client/company name (e.g., `concrete-ceo`, `ascension-capital`)
- Keep it short and recognizable

### Step 2: Create README.md

Use the template below as your starting point.

### Step 3: Classify Project Priority

Based on `strategic-priorities.md`:

| Priority | Definition | Example |
|----------|------------|---------|
| **P0** | Revenue-generating, active delivery | Ascension Capital |
| **P1** | Agency infrastructure | Templates, processes |
| **P2** | Developer pipeline | Recruitment, evaluation |
| **P3** | Developer Academy | Long-term moat |
| **P4** | Credibility assets | Demo videos |
| **P5** | Content/inbound | Deferred until OBG |

### Step 4: Link to OBG

Every project must align with the **One Big Goal (OBG):**

**$50k/month revenue for 3+ consecutive months**

---

## README.md Template

```markdown
# Project: [PROJECT NAME]

## Overview
**Client:** [Name]
**Type:** Client Project (P0 - Revenue)
**Status:** [Discovery/Prototyping/Scoped/Active/Delivery/Invoiced/Completed]
**Priority:** P0 - Revenue generating
**Health:** [Green/Yellow/Red]

---

## Opportunity Description
[What is the business problem and what are we potentially delivering?]
-
-
-

---

## Project Financials

| Item | Amount |
|------|--------|
| Project Value | $ |
| Developer Cost | $ |
| Your Margin | $ |
| Sales Fee (Linh/Mikael) | $ |
| Net Profit | $ |

**Target Margin:** 40%+
**Actual Margin %:**
**Payment Status:** [ ] Not invoiced [ ] Invoiced [ ] Collected

---

## Progress Tracker

### Discovery Phase
- [ ] Diagnostic call completed ($___/hr billed)
- [ ] Problem diagnosed
- [ ] Scope defined
- [ ] Estimate provided
- [ ] Client approved

### Prototyping Phase
- [ ] Prototype built (vibe coding)
- [ ] Proof of concept validated
- [ ] Client buy-in confirmed

### Build Phase
- [ ] Developer recruited/assigned
- [ ] Developer briefed
- [ ] Build in progress
- [ ] Code review completed
- [ ] Client testing completed
- [ ] Refinements implemented

### Delivery Phase
- [ ] Final delivery to client
- [ ] Client sign-off
- [ ] Invoice sent
- [ ] Payment collected

### Post-Delivery (P4 - Optional)
- [ ] Demo video created
- [ ] Results quantified
- [ ] Case study documented

---

## Team

**Architect (You):** Diagnose, prototype, scope, manage
**Sales (Linh/Mikael):** Relationship, close
**Developer:** [Name or "Needed"]

---

## Metrics

### Baseline (Before Automation)
-
-

### Results (After Automation)
-
-

### ROI for Client
- Time saved: ___ hours/week
- Value delivered: $___/month
- Annual value: $___/year

---

## Dependencies
- [ ]
- [ ]

## Blockers
-

## Risks
-

---

## Next Actions
1.
2.
3.

---

## Timeline
**Lead Source:** [Linh/Mikael/Inbound]
**Discovery Date:**
**Prototype Date:**
**Build Start:**
**Target Delivery:**
**Invoice Date:**
**Payment Due:**
**Payment Collected:**

---

## Communication Log
| Date | Type | Summary |
|------|------|---------|
| | Call/Email | |

---

## Notes
-

---

## Lessons Learned (Post-Completion)
**What went well:**
-

**What could improve:**
-

**Apply to future projects:**
-
```

---

## Quality Check

Before considering the project initialized:

- [ ] README.md created and navigable
- [ ] Folder structure matches standard layout
- [ ] Priority (P0-P5) assigned
- [ ] OBG alignment considered
- [ ] All required subdirectories created

---

## Common Mistakes to Avoid

1. **Creating folders too early** - Wait until there's real engagement
2. **Incomplete README.md** - Financial section must be filled out
3. **Vague action items** - Be specific and deadline-driven
4. **Missing OBG alignment** - Every project must tie to revenue goal
5. **Inconsistent naming** - Use lowercase-with-hyphens
6. **Skipping meeting notes** - Capture context from day one

---

## Example Projects for Reference

**Software Development:**
- `ascension-capital/` - Full automation project
- `plotter-mechanix/` - SaaS development

**Consulting/Audit:**
- `concrete-ceo/` - Partnership and audit services
- `az-events-planning/` - Opportunity assessment

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
- Update README.md with progress
- Check project health status
- Log communication

**Monthly:**
- Review OBG contribution
- Update financial tracking
- Archive completed items

---

**Last Updated:** 2025-12-31
