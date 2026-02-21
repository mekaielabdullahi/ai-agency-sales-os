# Comprehensive AI Audit - Quick Start Guide

## What is a Comprehensive AI Audit?

The **Comprehensive AI Audit** is AriseGroup.ai's deep-dive paid engagement that follows the free 30-minute discovery audit. It produces implementation-ready deliverables including:
- Detailed process maps and pain point analysis
- 5-10 prioritized AI/automation opportunities
- Technical architecture designs
- Phased implementation roadmap (30/90/180 days)
- ROI analysis and business case
- Executive report and presentation

**Duration**: 8-12 hours of audit work
**Cost**: Typically $3K-$10K paid engagement
**Deliverable**: audit.json + report + presentation

---

## Quick Start: 3 Ways to Conduct an Audit

### Method 1: Claude Code Skill (RECOMMENDED)

**Step 1**: Open Claude Code CLI in the ai-agency-sales-os repo

**Step 2**: Activate the skill
```bash
/skill comprehensive-ai-audit
```

**Step 3**: Follow the agent prompts
The agent will guide you through:
1. Client initialization
2. Intake questions
3. Process mapping
4. Opportunity identification
5. Solution design
6. Roadmap creation
7. Report generation

**That's it!** The agent handles the workflow, updates audit.json automatically, and produces deliverables.

---

### Method 2: Manual Workflow

**Step 1**: Create client folder
```bash
cd claude-code-os-implementation/03-ai-growth-engine/onboarding/audits
mkdir [client-name]
cd [client-name]
```

**Step 2**: Copy template
```bash
cp ../templates/audit-template.json audit.json
```

**Step 3**: Follow the 7-phase workflow
See `../agents/comprehensive-ai-audit-agent.md` for detailed phase-by-phase instructions.

**Step 4**: Populate audit.json section by section
- Phase 1: Initialize metadata
- Phase 2: Fill `audit_brief`
- Phase 3: Map processes in `current_state_maps`
- Phase 4: Identify opportunities in `ai_opportunity_matrix`
- Phase 5: Design solutions in `target_state_designs`
- Phase 6: Build `roadmap`
- Phase 7: Complete `report_outline` and `presentation_outline`

**Step 5**: Generate final deliverables
- Export report.md from report_outline
- Create presentation.md from presentation_outline

---

### Method 3: Use Business Functions Mapping Skill + Manual

**Step 1**: Map client's business functions
```bash
/skill business-functions-mapping
```

**Step 2**: Manually create audit.json
Use output from business functions mapping to populate current_state_maps

**Step 3**: Complete remaining sections manually
Follow audit-template.json structure

---

## The 7-Phase Audit Workflow

### Phase 1: Initialization (5-10 min)
**What**: Set up audit structure
**How**:
1. Create `audits/[client-name]/` folder
2. Copy audit-template.json → audit.json
3. Set client_id, created_date, audit_status: "in_progress"

**Output**: Initialized audit.json

---

### Phase 2: Intake & Context (30-45 min)
**What**: Gather company info and scope
**How**: Ask discovery questions:
- Industry, size, revenue
- Products/services, ICP
- Sales model, tech stack
- Business goals (top 3)
- Constraints (budget, timeline)
- In-scope processes

**Output**: Complete `audit_brief` section

**Pro Tip**: Review sales handoff packet and intake forms before asking questions

---

### Phase 3: Current-State Mapping (2-4 hours)
**What**: Document 3-5 critical processes
**How**: For each process:
1. Identify owner, trigger, frequency
2. Map steps (who, what, tool, duration)
3. Document pain points with metrics
4. List systems and data touchpoints
5. Calculate costs (time × hourly rate)

**Output**: 3-5 entries in `current_state_maps[]`

**Pro Tip**: Use Business Functions Mapping skill for systematic process mapping

**Example Process Map**:
```json
{
  "name": "Lead Generation Process",
  "owner_roles": ["Marketing Manager"],
  "trigger": "Website form submission",
  "frequency": "50-100 per week",
  "steps": [
    {
      "step_number": 1,
      "name": "Lead capture",
      "who": "Automated",
      "tool": "Website form",
      "duration": "Instant",
      "pain_points": ["No CRM integration", "Goes to email only"]
    },
    {
      "step_number": 2,
      "name": "Manual data entry",
      "who": "Sales admin",
      "tool": "Email → Spreadsheet",
      "duration": "10 min per lead",
      "pain_points": ["Time-consuming", "Error-prone", "Delayed response"]
    }
  ],
  "pain_points": [
    {
      "description": "Manual email-to-spreadsheet data entry",
      "frequency": "50-100 times per week",
      "time_cost": "8-16 hours per week",
      "impact": "high",
      "revenue_impact": "$3,000/month in lost leads due to slow response"
    }
  ],
  "metrics": {
    "volume": "75 leads/week average",
    "cycle_time": "10 min per lead",
    "error_rate": "15%",
    "cost_per_process": "$25 in labor"
  }
}
```

---

### Phase 4: AI Opportunity Discovery (1-2 hours)
**What**: Identify 5-10 AI/automation opportunities
**How**: For each process mapped:
1. Brainstorm AI applications:
   - Full automation
   - AI-assisted
   - AI-augmented
   - Agentic workflows
2. Score:
   - **Impact**: high/medium/low (time + revenue + quality)
   - **Effort**: high/medium/low (technical complexity + integrations)
   - **Speed to value**: Days to results
3. Calculate priority score
4. Document data requirements and risks

**Output**: 5-10 entries in `ai_opportunity_matrix[]`, ranked

**Prioritization Formula**:
Priority Score = (Impact Weight × 2) + (Feasibility Weight) + (ROI Weight) / 4

**Example Opportunity**:
```json
{
  "id": "opp_001",
  "process_name": "Lead Generation Process",
  "type": "Automation",
  "description": "Automated lead capture with CRM sync and AI-powered lead scoring",
  "impact": "high",
  "impact_details": {
    "time_saved": "10 hours/week",
    "cost_reduction": "$500/week in labor",
    "revenue_impact": "$3,000/month recovered lost leads"
  },
  "effort": "medium",
  "effort_details": {
    "technical_complexity": "medium",
    "integration_points": 2,
    "estimated_build_time": "2-3 weeks"
  },
  "speed_to_value": "30 days",
  "priority_score": 9
}
```

---

### Phase 5: Target-State Design (2-3 hours)
**What**: Design top 3-5 opportunities in detail
**How**: For each top opportunity:
1. Write solution summary (how it works)
2. List systems involved
3. Define AI components:
   - Purpose, technology, inputs/outputs
4. Map user journeys (before/after)
5. Document data flow
6. Note governance considerations
7. Set success metrics

**Output**: 3-5 entries in `target_state_designs[]`

**Example Design**:
```json
{
  "opportunity_id": "opp_001",
  "name": "Automated Lead Management System",
  "summary": "End-to-end automation: form submission → AI scoring → CRM sync → instant response",
  "ai_components": [
    {
      "component": "Lead Scoring AI",
      "purpose": "Score leads 0-100 based on conversion likelihood",
      "technology": "Claude API + custom scoring model",
      "inputs": ["Lead data", "Historical conversion data"],
      "outputs": ["Lead score", "Recommended action"]
    }
  ],
  "data_flow": "Website Form → Webhook → AI Scoring → CRM Creation → Email Automation",
  "success_metrics": [
    "Response time < 5 minutes",
    "Lead scoring accuracy > 80%",
    "Zero manual data entry"
  ]
}
```

---

### Phase 6: Roadmap Creation (1-2 hours)
**What**: Build 3-phase implementation plan
**How**:

**Phase 1 - Quick Wins (30 days)**:
- Select 1-2 high-impact, low-effort opportunities
- Define deliverables, KPIs, dependencies
- Estimate effort and monthly value

**Phase 2 - Scale Up (90 days)**:
- Medium-complexity initiatives
- Build on Phase 1 foundation

**Phase 3 - Strategic (180 days)**:
- Transformational projects
- Require Phases 1-2 complete

For each phase:
- Link to opportunity IDs
- Set timeline, owner, deliverables
- List dependencies and risks
- Define KPIs
- Estimate effort (hours) and value ($/month)

Calculate:
- Total timeline
- Total effort
- Total monthly value
- ROI break-even

**Output**: Complete `roadmap` object

---

### Phase 7: Report & Presentation (1-2 hours)
**What**: Create client-ready deliverables
**How**:

**Report Outline**:
1. Executive Summary
   - Current state (1 paragraph)
   - Key findings (3-5 bullets)
   - Recommended opportunities (top 3-5)
   - Expected impact (time, cost, revenue)
   - ROI summary

2. Detailed Sections
   - Business context
   - Current-state summary
   - Opportunity analysis
   - Target-state vision
   - Roadmap details
   - Investment & ROI
   - Next steps

**Presentation Outline** (7-10 slides):
1. Title slide
2. Agenda
3. Current state findings
4. Top opportunities (1 slide per opportunity)
5. Implementation roadmap
6. ROI & business case
7. Next steps

**Output**: `report_outline` and `presentation_outline` complete

---

## Key Questions to Ask During Discovery

### Business Context
- What industry are you in?
- How big is your company (employees, revenue)?
- What are your main products/services?
- Who's your ideal customer?
- What's your business model?

### Current State
- Walk me through your [process name]
- What happens first? Then what?
- Who does each step?
- What tools/systems do you use?
- How long does it take?
- How often does it happen?

### Pain Points
- Where do things break down?
- What's frustrating about this process?
- How much time does this waste?
- What errors occur? How often?
- What revenue are you losing?

### Goals & Constraints
- What are your top 3 business goals?
- What's your timeline?
- What's your budget range?
- What systems must we integrate with?
- What's non-negotiable?

### AI Context
- Have you tried any AI tools?
- What worked or didn't work?
- What's blocking AI adoption?
- If you could automate one thing, what would it be?

---

## Common Pitfalls & How to Avoid Them

### Pitfall 1: Vague Pain Points
❌ "Things are slow"
✅ "Lead response takes 4-6 hours, we lose 40% of interested prospects"

**Fix**: Always quantify (time, frequency, cost, impact)

---

### Pitfall 2: Generic Opportunities
❌ "Use AI to automate stuff"
✅ "Automated lead-to-CRM sync with AI-powered lead scoring based on historical conversion data"

**Fix**: Be specific about what, how, and expected results

---

### Pitfall 3: Underestimating Complexity
❌ "Just connect the systems"
✅ "Requires webhook setup, API integration, data mapping, error handling, and testing"

**Fix**: Document dependencies, integration points, and technical requirements

---

### Pitfall 4: Ignoring Change Management
❌ "We'll just deploy it"
✅ "Phase 1 includes training, gradual rollout, and feedback loops to ensure adoption"

**Fix**: Include organizational considerations in roadmap

---

### Pitfall 5: Missing ROI Justification
❌ "This will help"
✅ "Saves 10 hours/week ($500/week) + recovers $3K/month in lost leads = $5K/month value, 3-month break-even"

**Fix**: Calculate specific time savings, cost reduction, and revenue impact

---

## ROI Calculation Cheat Sheet

### Components of Value

**Time Savings**:
```
Hours saved per week × Hourly rate × 4 weeks = Monthly time value
Example: 10 hrs/week × $50/hr × 4 = $2,000/month
```

**Revenue Recovery**:
```
Lost leads per month × Close rate × Avg deal value = Monthly revenue impact
Example: 20 lost leads × 25% × $5,000 = $25,000/month
```

**Cost Reduction**:
```
Eliminated subscriptions + Reduced labor = Monthly cost savings
Example: $500 old tools + $1,000 manual work = $1,500/month
```

**Efficiency Gains**:
```
Faster cycle time → More throughput → More revenue
Example: 50% faster = 2x capacity = 2x revenue potential
```

### Total Monthly Value
```
Time + Revenue + Cost + Efficiency = Total Monthly Value
```

### ROI Calculation
```
ROI = ((Monthly Value × 12) - Total Investment) / Total Investment × 100%

Example:
Monthly Value: $5,000
Annual Value: $60,000
Investment: $15,000
ROI = ($60,000 - $15,000) / $15,000 × 100% = 300% first-year ROI
Break-even = $15,000 / $5,000 = 3 months
```

---

## Templates & Resources

### Files to Reference
- **Skill**: `.claude/skills/comprehensive-ai-audit/SKILL.md`
- **Agent**: `agents/comprehensive-ai-audit-agent.md`
- **Template**: `templates/audit-template.json`
- **Framework**: `templates/ai-audit-framework.md`
- **Audits Folder**: `audits/README.md`

### Related Skills
- `business-functions-mapping` - For process mapping
- `client-outreach` - For sales context
- `content-strategy` - For case studies from audits

---

## Success Checklist

Before delivering an audit, verify:

- [ ] Client folder created: `audits/[client-name]/`
- [ ] audit.json complete with all 8 top-level sections
- [ ] 3-5 current-state process maps with quantified pain points
- [ ] 5-10 AI opportunities identified and prioritized
- [ ] Top 3-5 opportunities with detailed designs
- [ ] 3-phase roadmap (30/90/180 days) with effort/value estimates
- [ ] ROI calculated and validated
- [ ] Executive summary written (no jargon, business language)
- [ ] Presentation outline created (7-10 slides)
- [ ] All assumptions flagged
- [ ] Technical feasibility confirmed
- [ ] Risk assessment completed
- [ ] Deliverables ready for client presentation
- [ ] Implementation team can start building immediately

---

## Next Steps After Audit Completion

1. **Mark Complete**:
   - Set `audit_status: "completed"` in audit.json
   - Add completion date

2. **Generate Final Deliverables**:
   - Create report.md from report_outline
   - Create presentation.md from presentation_outline
   - Export any diagrams or visuals

3. **Client Presentation**:
   - Schedule presentation call
   - Walk through findings, opportunities, roadmap, ROI
   - Get approval to proceed

4. **Handoff to Implementation**:
   - Share audit.json with build team
   - Roadmap becomes project plan
   - Phase 1 deliverables become sprint 1

5. **Post-Audit**:
   - Capture learnings in notes.md
   - Add client to case studies (if approved)
   - Update templates based on insights

---

**Ready to start?** Use `/skill comprehensive-ai-audit` in Claude Code or follow the manual workflow above.

For questions, see `agents/comprehensive-ai-audit-agent.md` or contact the AriseGroup.ai audit team.
