# Internal Development OS

## Purpose
A complete software development lifecycle framework that combines **AutoClaude** (autonomous execution with QA loops) and **BMAD** (structured spec-driven development) with our existing agency delivery system. This is our internal OS for developing working products—ideation → brainstorming → building with testing, verification, and metrics instrumentation.

---

## The Core Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| **Execution** | AutoClaude | Autonomous coding with self-validating QA loops |
| **Planning** | BMAD Method | Spec-driven development with specialized AI agents |
| **Delivery** | Agency Framework | 4-phase client delivery with margin protection |

---

## When to Use This System

### Use Internal Dev OS When:
- Building new client deliverables
- Creating internal tools/automation
- Prototyping solutions (vibe coding phase)
- Developing reusable components

### The System Ensures:
- ✅ Testing and verification at every stage
- ✅ Metrics instrumentation from the start
- ✅ Quality gates before delivery
- ✅ Reproducible, documented processes

---

## The 5-Phase Development Lifecycle

```
PHASE 1: IDEATION & ANALYSIS (BMAD)
├── Brainstorming with AI agents
├── Research & solution exploration
├── Problem definition
└── → Decision: Build or delegate?

PHASE 2: PLANNING & SPECIFICATION (BMAD)
├── PRD creation (Product Manager agent)
├── Technical specs (Analyst agent)
├── Architecture design (Architect agent)
├── UX specification (UX Designer agent)
└── → Artifact: Complete spec package

PHASE 3: AUTONOMOUS EXECUTION (AUTOCLAUDE)
├── Task sharding into stories
├── Parallel agent execution (up to 12 terminals)
├── Self-validating QA loops (up to 50 iterations)
├── Isolated git worktrees
└── → Artifact: Working code in branch

PHASE 4: VALIDATION & TESTING
├── Automated test execution
├── Metrics instrumentation verification
├── Error handling validation
├── Cross-session memory capture
└── → Gate: All tests pass

PHASE 5: INTEGRATION & DELIVERY
├── AI-powered merge conflict resolution
├── Final QA review
├── Documentation generation
├── Monitoring setup
└── → Artifact: Production-ready deliverable
```

---

## BMAD Method Integration

### Specialized AI Agents We Use

| Agent | Role | When to Engage |
|-------|------|----------------|
| **PM Agent** | Product requirements, PRD creation | Project kickoff |
| **Analyst** | Technical specs, research | Pre-architecture |
| **Architect** | System design, tech stack decisions | Before coding |
| **Developer** | Implementation, code generation | Active development |
| **UX Designer** | User flows, interface specs | UI/UX work |
| **Test Architect** | Test strategy, QA planning | Before execution |
| **Scrum Master** | Task breakdown, sprint planning | Ongoing |
| **Tech Writer** | Documentation, handover docs | Pre-delivery |

### BMAD Workflow Tracks

| Complexity | Track | Planning Time | Use Case |
|------------|-------|---------------|----------|
| **Low** | Quick Flow | <5 min | Bug fixes, small features |
| **Medium** | BMad Method | <15 min | Products, platforms, new features |
| **High** | Enterprise | <30 min | Complex systems, compliance needs |

### BMAD Setup
```bash
# Install BMAD
npx bmad-method@alpha install

# Initialize in project
*workflow-init

# System recommends appropriate track based on project analysis
```

---

## AutoClaude Integration

### Core Features We Leverage

1. **Self-Validating QA Loop**
   - Agent completes coding task
   - QA Reviewer checks against acceptance criteria
   - QA Fixer addresses issues automatically
   - Loop runs up to 50 iterations until validation passes

2. **Parallel Execution**
   - Up to 12 concurrent agent terminals
   - Isolated git worktrees per task
   - No cross-contamination of changes

3. **AI-Powered Merge Resolution**
   - Three-tier conflict resolution
   - Handles branches 50+ commits behind
   - Automated merge verification

4. **Cross-Session Memory** (Optional)
   - Stores discovered patterns
   - Retains codebase structure knowledge
   - Improves subsequent builds

### AutoClaude Setup
```bash
# Prerequisites
npm install -g @anthropic-ai/claude-code
claude setup-token

# Run from spec
python run.py --spec 001
python run.py --spec 001 --review
python run.py --spec 001 --merge
```

---

## Combined Workflow: Start to Finish

### 1. IDEATION (10-30 min)
```markdown
**Input:** Problem statement or client request
**Tools:** BMAD Analyst agent, brainstorming workflow

Actions:
- [ ] Define the problem clearly
- [ ] Research existing solutions
- [ ] Identify technical constraints
- [ ] Draft initial approach

**Output:** Problem definition document
```

### 2. SPECIFICATION (15-45 min)
```markdown
**Input:** Problem definition
**Tools:** BMAD PM, Architect, UX Designer agents

Actions:
- [ ] Create PRD with PM agent
- [ ] Design architecture with Architect agent
- [ ] Specify UX flows if UI involved
- [ ] Define acceptance criteria
- [ ] Create test specifications

**Output:** Complete spec package (PRD, architecture, UX, tests)
```

### 3. EXECUTION (Variable)
```markdown
**Input:** Spec package
**Tools:** AutoClaude with Developer agents

Actions:
- [ ] Shard specs into implementation tasks
- [ ] Configure worktrees for isolation
- [ ] Launch parallel agent execution
- [ ] Monitor QA loop progress
- [ ] Review and approve changes

**Output:** Working code in feature branch
```

### 4. VALIDATION (15-30 min)
```markdown
**Input:** Feature branch with code
**Tools:** Test runners, metrics tools

Actions:
- [ ] Run automated test suite
- [ ] Verify error handling
- [ ] Check metrics instrumentation
- [ ] Validate logging setup
- [ ] Review monitoring dashboards

**Output:** Validated, tested code
```

### 5. DELIVERY (10-20 min)
```markdown
**Input:** Validated feature branch
**Tools:** AutoClaude merge, Tech Writer agent

Actions:
- [ ] Resolve merge conflicts (AI-assisted)
- [ ] Generate documentation
- [ ] Final QA review
- [ ] Deploy to staging
- [ ] Client handover prep

**Output:** Production-ready deliverable
```

---

## Quality Gates (Non-Negotiable)

### Gate 1: Spec Complete
- [ ] PRD approved
- [ ] Architecture reviewed
- [ ] Acceptance criteria defined
- [ ] Test specs created

### Gate 2: Code Complete
- [ ] All QA loops passed
- [ ] No failing tests
- [ ] Error handling implemented
- [ ] Metrics instrumented

### Gate 3: Merge Ready
- [ ] Conflicts resolved
- [ ] Integration tests pass
- [ ] Documentation complete
- [ ] Monitoring configured

### Gate 4: Delivery Ready
- [ ] Staging tested
- [ ] Client review complete
- [ ] Handover docs prepared
- [ ] Support plan defined

---

## Testing Requirements

### Every Build Must Include:

1. **Unit Tests**
   - Core logic coverage
   - Edge case handling
   - Error path testing

2. **Integration Tests**
   - API endpoint validation
   - Database operations
   - External service mocks

3. **E2E Tests** (when UI)
   - Critical user flows
   - Cross-browser basics
   - Mobile responsiveness

### Test Automation Setup
```bash
# Standard test commands (configure per project)
npm test           # Unit tests
npm run test:int   # Integration tests
npm run test:e2e   # End-to-end tests
npm run test:all   # Full suite
```

---

## Metrics Instrumentation

### Required Metrics Per Project

| Category | Metrics | Tool |
|----------|---------|------|
| **Performance** | Response time, load time, error rate | APM (Sentry, DataDog) |
| **Usage** | Active users, feature adoption, retention | Analytics (Posthog, Mixpanel) |
| **Business** | Conversions, revenue impact, time saved | Custom events |
| **Technical** | CPU, memory, API latency, queue depth | Infrastructure monitoring |

### Instrumentation Checklist
- [ ] Error tracking configured (Sentry or equivalent)
- [ ] Performance monitoring active
- [ ] Key business events tracked
- [ ] Alerting thresholds set
- [ ] Dashboard created for client

---

## Configuration Files

### BMAD Config (`.bmad/config.yaml`)
```yaml
workflow_track: bmad-method  # quick-flow, bmad-method, enterprise
agents:
  pm: enabled
  architect: enabled
  developer: enabled
  test_architect: enabled
  tech_writer: enabled
settings:
  auto_recommendations: true
  document_sharding: true
  update_safe: true
```

### AutoClaude Config (`apps/backend/.env`)
```env
CLAUDE_CODE_OAUTH_TOKEN=<from claude setup-token>
GRAPHITI_ENABLED=true  # Enable cross-session memory
AUTO_BUILD_MODEL=claude-3-5-sonnet  # or claude-3-opus
```

---

## Project Templates

### New Project Initialization
```bash
# 1. Create project directory
mkdir project-name && cd project-name
git init

# 2. Install development OS tools
npx bmad-method@alpha install

# 3. Initialize workflow
# Opens agent selection and project analysis
*workflow-init

# 4. Create spec using BMAD agents
# Use PM agent for PRD
# Use Architect for technical design

# 5. Configure AutoClaude (if using)
# Set up worktrees and task specs
```

---

## Best Practices

### Do:
- ✅ Start with clear problem definition
- ✅ Create complete specs before coding
- ✅ Use appropriate BMAD track for complexity
- ✅ Let AutoClaude QA loop complete fully
- ✅ Instrument metrics from day one
- ✅ Document decisions and trade-offs

### Don't:
- ❌ Skip specification phase
- ❌ Manually override QA failures
- ❌ Merge without all tests passing
- ❌ Deliver without monitoring setup
- ❌ Forget error handling
- ❌ Ignore memory layer insights

---

## Integration with Agency Workflow

This Internal Dev OS plugs into our existing 4-phase agency delivery:

| Agency Phase | Internal Dev OS Phase |
|--------------|----------------------|
| Phase 1: Discovery | → Ideation + partial Specification |
| Phase 2: Solution Design | → Complete Specification |
| Phase 3: Development | → Execution + Validation |
| Phase 4: Quality & Delivery | → Delivery |

**Key Point:** Whether YOU build (vibe coding) or DEVELOPERS build, this process applies. Developers get the spec package; you execute the QA and delivery phases.

---

## Quick Reference Commands

| Action | Command |
|--------|---------|
| Start BMAD workflow | `*workflow-init` |
| Quick bug fix track | `*quick-flow` |
| Full project track | `*bmad-method` |
| Run AutoClaude spec | `python run.py --spec NNN` |
| Review AutoClaude work | `python run.py --spec NNN --review` |
| Merge AutoClaude branch | `python run.py --spec NNN --merge` |
| Run all tests | `npm run test:all` |

---

## Resources

### AutoClaude
- GitHub: [AndyMik90/Auto-Claude](https://github.com/AndyMik90/Auto-Claude)
- Docs: See `guides/` in repository

### BMAD Method
- GitHub: [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
- Website: [bmadcodes.com](https://bmadcodes.com)
- Medium: [What is BMAD-METHOD?](https://medium.com/@visrow/what-is-bmad-method-a-simple-guide-to-the-future-of-ai-driven-development-412274f91419)

---

## The Golden Rule

**Spec before code. Test before merge. Monitor before deliver.**

Every project goes through all phases.
No shortcuts on quality gates.
The system makes the next project faster.
