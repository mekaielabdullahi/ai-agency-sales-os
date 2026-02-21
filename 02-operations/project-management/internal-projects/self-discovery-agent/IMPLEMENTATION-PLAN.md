# Self-Discovery Agent Implementation Plan

## Purpose
A systematic agent that audits both agency workspaces (`ai-agency-development-os` and `ai-agency-sales-os`) to:
1. Build comprehensive context on documentation, history, and future plans
2. Update our internal business process map
3. Identify automation opportunities (internal opportunity matrix)
4. Create reusable patterns for client engagements

---

## Scope

### Workspaces to Analyze
| Workspace | Files | Focus |
|-----------|-------|-------|
| `ai-agency-development-os` | ~540 markdown files | Operations, projects, delivery |
| `ai-agency-sales-os` | ~354 markdown files | Sales, agentic modules, playbooks |

### Output Artifacts
1. **Business Process Map** - Visual/structured map of all agency processes
2. **Internal Opportunity Matrix** - Automation candidates ranked by impact
3. **Knowledge Graph** - Connections between projects, processes, and learnings
4. **Reusable Pattern Library** - Patterns applicable to client work

---

## Architecture

### Phase 1: Systematic Crawl & Index

```
/self-discovery-agent/
├── IMPLEMENTATION-PLAN.md          # This file
├── config/
│   ├── crawl-config.yaml           # Directories to analyze, priorities
│   └── classification-schema.yaml  # How to categorize content
├── outputs/
│   ├── index/                      # Raw indexed content
│   │   ├── development-os/
│   │   └── sales-os/
│   ├── business-process-map.md     # Generated process map
│   ├── opportunity-matrix.md       # Automation opportunities
│   ├── knowledge-graph.md          # Entity relationships
│   └── pattern-library.md          # Reusable patterns
├── agents/
│   ├── crawler-agent.md            # Crawl and extract
│   ├── classifier-agent.md         # Classify content types
│   ├── analyzer-agent.md           # Find patterns and gaps
│   └── synthesizer-agent.md        # Generate outputs
└── logs/
    └── audit-runs/                 # Historical audit logs
```

### Phase 2: Classification Schema

Each file gets classified by:

| Dimension | Values |
|-----------|--------|
| **Content Type** | process, project, meeting, template, agent, config, documentation |
| **Business Function** | sales, operations, delivery, content, hr, executive |
| **Lifecycle Stage** | active, completed, deferred, incubated, archived |
| **Automation Potential** | high, medium, low, none |
| **Reusability** | client-facing, internal-only, both |

### Phase 3: Analysis Modules

#### Module 1: Process Discovery
- Extract all workflows, SOPs, and procedures
- Identify manual steps that could be automated
- Map dependencies between processes

#### Module 2: Project Intelligence
- Summarize all projects (active, completed, deferred)
- Extract lessons learned
- Identify patterns across projects

#### Module 3: Meeting & Communication Mining
- Extract action items still pending
- Identify recurring topics/pain points
- Surface commitments made to clients/partners

#### Module 4: Template & Agent Inventory
- Catalog all templates and their usage
- Inventory all agents and their purposes
- Identify gaps (missing templates, agents)

#### Module 5: Opportunity Identification
- Cross-reference manual processes with automation potential
- Score opportunities by: effort, impact, reusability
- Generate prioritized backlog

---

## Crawl Strategy

### Priority 1: Core Operations (Run First)
```
ai-agency-development-os/
├── 02-operations/project-management/active-projects/
├── 01-executive-office/strategic-alignment/
├── 02-operations/discovery-process/
└── 03-ai-growth-engine/development-framework/

ai-agency-sales-os/
├── agentic/modules/
├── claude-code-os-implementation/06-knowledge-base/
└── claude-code-os-implementation/07-workflows/
```

### Priority 2: Historical Context
```
ai-agency-development-os/
├── 02-operations/project-management/completed-projects/
├── 01-executive-office/internal-business-meetings/
└── 02-operations/reports/

ai-agency-sales-os/
├── claude-code-os-implementation/06-knowledge-base/case-studies/
└── docs/
```

### Priority 3: Templates & Patterns
```
ai-agency-development-os/
├── 02-operations/discovery-process/templates/
├── 03-ai-growth-engine/development-framework/templates/
└── 04-content-team/templates/

ai-agency-sales-os/
├── claude-code-os-implementation/09-templates/
└── agentic/modules/proposal/
```

---

## Agent Specifications

### 1. Crawler Agent
**Purpose:** Systematically read all files and extract structured data

**Inputs:**
- Directory paths to crawl
- File patterns to include/exclude
- Priority order

**Outputs:**
- Raw content index with metadata
- File relationship map
- Summary statistics

**Prompt Template:**
```
Crawl the specified directory and for each markdown file:
1. Extract title, headers, key sections
2. Identify references to other files/projects
3. Extract any action items, dates, or decisions
4. Classify content type
5. Note automation potential indicators
```

### 2. Classifier Agent
**Purpose:** Apply consistent classification schema

**Classification Rules:**
- Files in `active-projects/` → lifecycle: active
- Files containing "template" → content_type: template
- Files with "agent" in path → content_type: agent
- Files with meeting dates → content_type: meeting
- Files with "TODO", "action item" → flag for action review

### 3. Analyzer Agent
**Purpose:** Find patterns, gaps, and opportunities

**Analysis Tasks:**
1. Process bottleneck identification
2. Repeated manual work patterns
3. Cross-project pattern extraction
4. Stale/abandoned content flagging
5. Automation candidate scoring

**Scoring Criteria:**
| Factor | Weight | Description |
|--------|--------|-------------|
| Frequency | 30% | How often is this done? |
| Time Saved | 25% | Hours saved per occurrence |
| Error Reduction | 20% | Current error rate |
| Reusability | 15% | Applicable to clients? |
| Complexity | 10% | Effort to automate |

### 4. Synthesizer Agent
**Purpose:** Generate actionable outputs

**Outputs:**
1. Executive summary of findings
2. Business process map (mermaid diagrams)
3. Prioritized opportunity matrix
4. Pattern library entries
5. Recommended next actions

---

## Business Process Map Structure

```markdown
## Agency Business Processes

### Sales & Lead Generation
- Lead sourcing (Linh/Mikael)
- Qualification process
- Diagnostic call scheduling
- Proposal generation

### Project Delivery
- Discovery process
- Scoping & estimation
- Developer assignment
- Build & iteration
- Quality review
- Handoff & documentation

### Operations
- Daily planning
- Weekly reviews
- Monthly assessments
- Revenue tracking

### Content & Marketing
- Demo video production
- LinkedIn content
- Developer Academy content
```

---

## Opportunity Matrix Structure

| Opportunity | Business Function | Current State | Automation Approach | Effort | Impact | Priority |
|-------------|-------------------|---------------|---------------------|--------|--------|----------|
| Example: Meeting summary → Action items | Operations | Manual extraction | Agent + template | Medium | High | P1 |

---

## Execution Schedule

### Initial Full Audit
- Run once to establish baseline
- Expected duration: 2-3 hours of agent processing
- Output: Complete index + initial analysis

### Recurring Audits
- **Weekly:** Quick scan for new/changed files
- **Monthly:** Full re-analysis with trend comparison
- **Quarterly:** Deep pattern analysis + strategy update

---

## Implementation Steps

### Step 1: Create Directory Structure
- [x] Create `/self-discovery-agent/` folder
- [ ] Create subdirectories (config, outputs, agents, logs)

### Step 2: Build Configuration
- [ ] Define crawl-config.yaml
- [ ] Define classification-schema.yaml

### Step 3: Build Crawler Agent
- [ ] Write crawler agent prompt
- [ ] Test on sample directories
- [ ] Validate output format

### Step 4: Build Classifier Agent
- [ ] Write classification rules
- [ ] Test on diverse file types
- [ ] Refine rules based on edge cases

### Step 5: Build Analyzer Agent
- [ ] Define analysis criteria
- [ ] Build scoring algorithm
- [ ] Test pattern detection

### Step 6: Build Synthesizer Agent
- [ ] Define output templates
- [ ] Build mermaid diagram generator
- [ ] Create opportunity matrix format

### Step 7: Run Initial Audit
- [ ] Execute full crawl
- [ ] Review and validate results
- [ ] Generate initial outputs

### Step 8: Operationalize
- [ ] Create slash command for audit
- [ ] Set up recurring schedule
- [ ] Document maintenance process

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Files indexed | 100% of markdown files |
| Classification accuracy | >90% |
| Automation opportunities identified | 10+ high-priority |
| Reusable patterns extracted | 5+ for client use |
| Time to run audit | <30 minutes |

---

## Integration Points

### With Existing Systems
- `/daily-assessment` - Feed insights into daily planning
- `/project-status` - Enhance with automated project intelligence
- `/weekly-review` - Include self-discovery findings

### Future Enhancements
- Auto-update CLAUDE.md with new patterns
- Generate client discovery templates from patterns
- Build automation proposals from opportunity matrix
- Create training content for Developer Academy

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Stale data in outputs | Version outputs, timestamp all runs |
| Over-automation recommendations | Human review of top opportunities |
| Missing context | Cross-reference with meeting notes |
| Scope creep | Strict priority-based crawling |

---

## Notes

- Both workspaces have ~900 markdown files total
- Focus on actionable insights, not just inventory
- Ultimate goal: Surface automation opportunities that help both agency and clients
- This agent embodies the "eat your own dog food" principle
