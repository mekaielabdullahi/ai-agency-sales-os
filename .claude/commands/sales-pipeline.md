---
description: Full sales pipeline workflow from prospect to proposal
argument-hint: [company-name]
---

You are the Sales Pipeline Orchestrator for Claude Code OS.

## Context

Date: !`date +"%A, %B %d, %Y"`
Prospect: $ARGUMENTS

## Your Task

Execute the full sales pipeline workflow, guiding you through each step from prospect research to proposal generation.

## Sales Pipeline Stages

```
STAGE 1: RESEARCH & ANALYZE
    └─→ /client-analyze [company]
    ↓
STAGE 2: SCORE & PRIORITIZE
    └─→ /lead-score [company]
    ↓
STAGE 3: OUTREACH
    └─→ /email cold [company]
    ↓
STAGE 4: DISCOVERY CALL
    └─→ /meeting-notes discovery
    ↓
STAGE 5: PROPOSAL
    └─→ /proposal [company]
    ↓
STAGE 6: FOLLOW-UP
    └─→ Track and nurture
```

## Integrated Workflow

### STAGE 1: Research & Analyze

First, let's analyze this prospect:

**Run**: `/client-analyze [company name]`

This will generate:
- Top 3 problems with evidence
- Industry context
- Value hypothesis
- Recommended 5 Questions opening
- Personalization hooks

---

### STAGE 2: Score & Prioritize

With analysis complete, score the lead:

**Run**: `/lead-score [company name]`

This will determine:
- Fit score (40 pts)
- Engagement score (30 pts)
- Timing score (30 pts)
- Priority level (HOT/WARM/NURTURE/DISQUALIFY)

---

### STAGE 3: Outreach

If priority is HOT or WARM, create outreach:

**Run**: `/email cold`

Provide the analysis insights for personalized outreach.

---

### STAGE 4: Discovery Call

After booking a call:

**Before call**: Review client analysis
**During call**: Use 5 Questions Method
**After call**: `/meeting-notes discovery`

This captures:
- Pain points confirmed
- Budget/timeline signals
- Decision makers
- Action items

---

### STAGE 5: Proposal

If qualified, generate proposal:

**Run**: `/proposal [company name]`

Provide discovery insights for customized proposal.

---

### STAGE 6: Follow-Up

Track the opportunity:
- Log in CRM
- Set follow-up reminders
- Nurture with relevant content

## Output Format

```markdown
# SALES PIPELINE: [COMPANY NAME]

**Current Stage**: [Stage X]
**Priority**: [HOT/WARM/NURTURE]
**Next Action**: [What to do]

---

## PIPELINE PROGRESS

| Stage | Status | Date | Notes |
|-------|--------|------|-------|
| 1. Research | [Done/Pending] | [Date] | [Notes] |
| 2. Score | [Done/Pending] | [Date] | [Notes] |
| 3. Outreach | [Done/Pending] | [Date] | [Notes] |
| 4. Discovery | [Done/Pending] | [Date] | [Notes] |
| 5. Proposal | [Done/Pending] | [Date] | [Notes] |
| 6. Follow-up | [Done/Pending] | [Date] | [Notes] |

---

## QUICK STATS

- **Lead Score**: [X]/100
- **Key Pain Point**: [Main problem]
- **Value Hypothesis**: [Our solution]
- **Estimated Deal Size**: $[Amount]
- **Close Probability**: [X]%

---

## NEXT STEPS

1. [Immediate action]
2. [This week action]
3. [Follow-up scheduled]

---

## COMMANDS TO RUN

Based on current stage, run:
- [ ] [Next command]
```

## Pipeline Visualization

Auto-generate a visual of where this prospect is in the pipeline:

```mermaid
flowchart LR
    subgraph Pipeline
        R[1. Research] --> S[2. Score]
        S --> O[3. Outreach]
        O --> D[4. Discovery]
        D --> P[5. Proposal]
        P --> F[6. Follow-up]
    end

    style [CURRENT_STAGE] fill:#22c55e,color:#fff
```

**Saved to**: ./diagrams/YYYY-MM-DD-[company]-pipeline.mmd

---

## Quick Pipeline Check

To check where a prospect is in the pipeline:

"What stage is [company] at?"

I'll review and recommend the next action.
