# Critical Path Analysis Template

**Project/Goal**: {{PROJECT}}
**Analysis Date**: {{DATE}}
**Analyst**: {{ANALYST}}

---

## 🎯 Purpose of Critical Path Analysis

**Critical Path** = The sequence of dependent tasks that determines the minimum time to complete a goal.

**Why it matters**:
- Identifies THE constraint
- Shows where to focus energy
- Reveals true timeline
- Prevents wasted effort

---

## 📊 Goal Definition

### Primary Objective
```
{{OBJECTIVE}}
```

### Success Criteria
1. {{SUCCESS_1}}
2. {{SUCCESS_2}}
3. {{SUCCESS_3}}

### Deadline
**Target completion**: {{DEADLINE}}
**Days available**: {{DAYS_AVAILABLE}}

---

## 🗺️ Task Breakdown

### All Required Tasks

| ID | Task | Duration | Dependencies | Owner | Type |
|----|------|----------|--------------|-------|------|
| A | {{TASK_A}} | {{DUR_A}} | None | {{OWN_A}} | {{TYPE_A}} |
| B | {{TASK_B}} | {{DUR_B}} | {{DEP_B}} | {{OWN_B}} | {{TYPE_B}} |
| C | {{TASK_C}} | {{DUR_C}} | {{DEP_C}} | {{OWN_C}} | {{TYPE_C}} |
| D | {{TASK_D}} | {{DUR_D}} | {{DEP_D}} | {{OWN_D}} | {{TYPE_D}} |
| E | {{TASK_E}} | {{DUR_E}} | {{DEP_E}} | {{OWN_E}} | {{TYPE_E}} |
| F | {{TASK_F}} | {{DUR_F}} | {{DEP_F}} | {{OWN_F}} | {{TYPE_F}} |
| G | {{TASK_G}} | {{DUR_G}} | {{DEP_G}} | {{OWN_G}} | {{TYPE_G}} |

**Total Tasks**: {{TOTAL_TASKS}}
**Total Estimated Time** (if sequential): {{TOTAL_TIME}}

---

## 🔗 Dependency Mapping

### Dependency Graph
```
START
  ↓
[A] {{TASK_A}} ({{DUR_A}})
  ↓
[B] {{TASK_B}} ({{DUR_B}}) ──┐
  ↓                          │
[C] {{TASK_C}} ({{DUR_C}})   │
  ↓                          ↓
[D] {{TASK_D}} ({{DUR_D}}) ←─┘
  ↓
[E] {{TASK_E}} ({{DUR_E}})
  ↓
END
```

### Parallel Opportunities
**These can be done simultaneously**:
- {{PARALLEL_1}} AND {{PARALLEL_2}}
- {{PARALLEL_3}} AND {{PARALLEL_4}}

---

## 🎯 THE Critical Path

### Critical Path Sequence
```
{{CP_TASK_1}} ({{CP_DUR_1}})
   ↓
{{CP_TASK_2}} ({{CP_DUR_2}})
   ↓
{{CP_TASK_3}} ({{CP_DUR_3}})
   ↓
{{CP_TASK_4}} ({{CP_DUR_4}})
   ↓
{{CP_TASK_5}} ({{CP_DUR_5}})
   ↓
GOAL ACHIEVED
```

### Critical Path Duration
**Minimum time to completion**: {{CP_TOTAL_TIME}}
**Available time**: {{AVAILABLE_TIME}}
**Buffer**: {{BUFFER}}
**Status**: {{STATUS}} (On Time / Tight / At Risk)

### Critical Path Tasks
These tasks have **ZERO slack** - any delay delays the entire goal.

1. **{{CP_1}}**
   - Duration: {{CP_1_DUR}}
   - Start: {{CP_1_START}}
   - End: {{CP_1_END}}
   - Owner: {{CP_1_OWN}}
   - Priority: **CRITICAL**

2. **{{CP_2}}**
   - Duration: {{CP_2_DUR}}
   - Start: {{CP_2_START}}
   - End: {{CP_2_END}}
   - Owner: {{CP_2_OWN}}
   - Priority: **CRITICAL**

3. **{{CP_3}}**
   - Duration: {{CP_3_DUR}}
   - Start: {{CP_3_START}}
   - End: {{CP_3_END}}
   - Owner: {{CP_3_OWN}}
   - Priority: **CRITICAL**

---

## 📍 Non-Critical Path Tasks

### Tasks with Slack Time
These have flexibility in scheduling.

| Task | Slack Time | Earliest Start | Latest Start | Priority |
|------|-----------|---------------|-------------|----------|
| {{SLACK_1}} | {{SLACK_1_TIME}} | {{SLACK_1_EARLY}} | {{SLACK_1_LATE}} | Medium |
| {{SLACK_2}} | {{SLACK_2_TIME}} | {{SLACK_2_EARLY}} | {{SLACK_2_LATE}} | Low |
| {{SLACK_3}} | {{SLACK_3_TIME}} | {{SLACK_3_EARLY}} | {{SLACK_3_LATE}} | Low |

**Strategy**: Schedule these around critical path tasks.

---

## 🚧 Constraint Identification

### Theory of Constraints Applied

**Current Constraint** (bottleneck limiting entire system):
```
{{CONSTRAINT}}
```

**Why it's the constraint**:
{{CONSTRAINT_REASON}}

**Impact if not resolved**:
{{CONSTRAINT_IMPACT}}

**How to break it**:
1. {{BREAK_1}}
2. {{BREAK_2}}
3. {{BREAK_3}}

### Secondary Constraints
**Next bottleneck** (after primary is broken):
- {{SECONDARY_CONSTRAINT}}

**Third bottleneck**:
- {{TERTIARY_CONSTRAINT}}

---

## ⚡ Acceleration Opportunities

### Ways to Shorten Critical Path

1. **{{ACCEL_1}}**
   - Method: {{ACCEL_1_METHOD}}
   - Time saved: {{ACCEL_1_SAVE}}
   - Cost/Risk: {{ACCEL_1_COST}}
   - Worth it? {{ACCEL_1_WORTH}}

2. **{{ACCEL_2}}**
   - Method: {{ACCEL_2_METHOD}}
   - Time saved: {{ACCEL_2_SAVE}}
   - Cost/Risk: {{ACCEL_2_COST}}
   - Worth it? {{ACCEL_2_WORTH}}

3. **{{ACCEL_3}}**
   - Method: {{ACCEL_3_METHOD}}
   - Time saved: {{ACCEL_3_SAVE}}
   - Cost/Risk: {{ACCEL_3_COST}}
   - Worth it? {{ACCEL_3_WORTH}}

### Parallelization Opportunities
**Current sequential that could be parallel**:
- {{PARA_OPP_1}}
- {{PARA_OPP_2}}

**Time saved by parallelizing**: {{PARA_SAVE}}

---

## 🎯 Execution Strategy

### Phase-by-Phase Execution

**Phase 1**: {{PHASE_1}}
- **Critical Path Tasks**: {{CP_PHASE_1}}
- **Duration**: {{PHASE_1_DUR}}
- **Focus**: {{PHASE_1_FOCUS}}

**Phase 2**: {{PHASE_2}}
- **Critical Path Tasks**: {{CP_PHASE_2}}
- **Duration**: {{PHASE_2_DUR}}
- **Focus**: {{PHASE_2_FOCUS}}

**Phase 3**: {{PHASE_3}}
- **Critical Path Tasks**: {{CP_PHASE_3}}
- **Duration**: {{PHASE_3_DUR}}
- **Focus**: {{PHASE_3_FOCUS}}

### Resource Allocation Focus
**80% of resources should go to critical path tasks.**

| Resource | CP Allocation | Non-CP | Total |
|----------|--------------|--------|-------|
| Time | {{TIME_CP}}% | {{TIME_NON}}% | 100% |
| Budget | {{BUD_CP}}% | {{BUD_NON}}% | 100% |
| Team | {{TEAM_CP}}% | {{TEAM_NON}}% | 100% |

---

## 🎪 Risk Analysis

### Critical Path Risks
**Risks that would delay entire project**:

1. **{{CP_RISK_1}}**
   - **Probability**: {{CP_R1_PROB}}%
   - **Impact**: Delay of {{CP_R1_DELAY}}
   - **Mitigation**: {{CP_R1_MIT}}
   - **Contingency**: {{CP_R1_CONT}}

2. **{{CP_RISK_2}}**
   - **Probability**: {{CP_R2_PROB}}%
   - **Impact**: Delay of {{CP_R2_DELAY}}
   - **Mitigation**: {{CP_R2_MIT}}
   - **Contingency**: {{CP_R2_CONT}}

3. **{{CP_RISK_3}}**
   - **Probability**: {{CP_R3_PROB}}%
   - **Impact**: Delay of {{CP_R3_DELAY}}
   - **Mitigation**: {{CP_R3_MIT}}
   - **Contingency**: {{CP_R3_CONT}}

### Buffer Strategy
**Where to add buffers**:
- After {{BUFFER_POINT_1}}: {{BUFFER_1}} buffer
- After {{BUFFER_POINT_2}}: {{BUFFER_2}} buffer
- End of project: {{END_BUFFER}} buffer

---

## 📊 Progress Tracking

### Critical Path Milestones

- [ ] **{{MS_1}}** (CP Task A-B complete)
  - **Target**: {{MS_1_TARGET}}
  - **Actual**: {{MS_1_ACTUAL}}
  - **Status**: {{MS_1_STATUS}}

- [ ] **{{MS_2}}** (CP Task C-D complete)
  - **Target**: {{MS_2_TARGET}}
  - **Actual**: {{MS_2_ACTUAL}}
  - **Status**: {{MS_2_STATUS}}

- [ ] **{{MS_3}}** (CP Task E complete)
  - **Target**: {{MS_3_TARGET}}
  - **Actual**: {{MS_3_ACTUAL}}
  - **Status**: {{MS_3_STATUS}}

- [ ] **{{MS_4}}** (All CP tasks complete)
  - **Target**: {{MS_4_TARGET}}
  - **Actual**: {{MS_4_ACTUAL}}
  - **Status**: {{MS_4_STATUS}}

### Critical Path Health
**Current Status**:
- **On Schedule**: {{ON_SCHED}} (Yes/No/At Risk)
- **Days Ahead/Behind**: {{DAYS_VAR}}
- **Completion %**: {{CP_COMP}}%
- **Velocity**: {{VELOCITY}}

---

## 🚨 Early Warning System

### Red Flags - Immediate Escalation Required

- [ ] Critical path task delayed >1 day
- [ ] Constraint not breaking as planned
- [ ] Dependency blocker emerged
- [ ] Resource pulled from CP task
- [ ] Risk materialized on CP

**If any checked**: IMMEDIATE action required.

### Yellow Flags - Monitor Closely

- [ ] CP task at 80% of time estimate but <80% complete
- [ ] Team member working CP task shows signs of struggle
- [ ] External dependency not confirmed
- [ ] Buffer being consumed faster than planned

---

## 🔄 Weekly Critical Path Review

### Monday Morning Check
- [ ] What's on the critical path THIS WEEK?
- [ ] Any blockers to CP tasks?
- [ ] Resources allocated to CP?
- [ ] Risks to monitor?

### Friday Status Review
- [ ] Did CP tasks progress as planned?
- [ ] Any slippage?
- [ ] Next week's CP tasks ready?
- [ ] Adjust timeline if needed?

---

## 💡 Critical Path Principles

### Principle 1: Protect the Critical Path
**Always prioritize CP tasks over non-CP tasks.**
Non-CP tasks can slip; CP tasks cannot.

### Principle 2: Shorten the CP First
**Want to go faster? Shorten critical path.**
Optimizing non-CP tasks doesn't speed up project.

### Principle 3: Resources to the Constraint
**80% of resources to critical path.**
Everything else is secondary.

### Principle 4: One Constraint at a Time
**Focus on current bottleneck only.**
Don't solve future constraints until current one is broken.

### Principle 5: Monitor, Adjust, Iterate
**Critical path can change.**
When tasks complete or are delayed, recalculate.

---

## 🎯 THE ONE THING (Critical Path Edition)

### This Week's Critical Path Focus
**THE ONE CP TASK THIS WEEK**:
```
{{WEEK_CP_TASK}}
```

**Why it's critical**: {{WHY_CRITICAL}}
**What it unlocks**: {{UNLOCKS}}
**Success criteria**: {{CP_SUCCESS}}

### Today's Critical Path Focus
**THE ONE CP TASK TODAY**:
```
{{TODAY_CP_TASK}}
```

**Time block**: {{TIME_BLOCK}}
**Resources needed**: {{RESOURCES}}
**Done means**: {{DONE_CRITERIA}}

---

## 🚀 Optimization Checklist

- [ ] Critical path identified and documented
- [ ] All dependencies mapped
- [ ] Constraint identified
- [ ] Parallel opportunities found
- [ ] Resources allocated 80% to CP
- [ ] Risks mitigated
- [ ] Buffers added strategically
- [ ] Team understands CP
- [ ] Weekly reviews scheduled
- [ ] Escalation protocol set

---

*"The critical path is your friend. Focus there, everything else is noise."*

*Last Updated: {{DATE}}*
*Next Review: {{NEXT_REVIEW}}*
