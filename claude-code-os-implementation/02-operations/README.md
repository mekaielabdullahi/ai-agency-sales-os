# Operations Department

## 🎯 Mission
Track productivity, manage projects, and provide objective performance metrics to ensure continuous improvement and strategic alignment.

---

## 📊 Department Overview

The Operations Department is the measurement and optimization engine of Claude Code OS. It provides objective feedback on daily performance, tracks project health, and identifies patterns that enable continuous improvement.

### Core Functions

1. **Productivity Assessment**: Daily scoring and feedback on task execution
2. **Project Management**: Portfolio tracking and status reporting
3. **Metrics & Analysis**: Trend identification and predictive insights

---

## 🗂️ Department Structure

```
02-operations/
├── productivity-assessment/
│   ├── templates/
│   │   ├── daily-assessment.md           # Daily productivity assessment template
│   │   ├── weekly-review.md              # Weekly performance review template
│   │   └── scoring-rubric.md             # Objective 1-10 scoring criteria
│   ├── logs/
│   │   ├── daily/                        # Daily assessment records
│   │   └── weekly/                       # Weekly review records
│   └── agents/
│       └── productivity-assessor-agent.md # AI agent for daily assessments
├── project-management/
│   ├── active-projects/
│   │   └── project-template.md           # Template for active project tracking
│   ├── incubated-projects/               # Projects on hold
│   ├── completed-projects/               # Archived completed projects
│   ├── PROJECT-STATUS-OVERVIEW.md        # Portfolio summary template
│   └── agents/
│       └── project-manager-agent.md      # AI agent for portfolio management
├── metrics-tracking/
│   ├── dashboards/                       # Metric visualization templates
│   ├── data/                             # Raw metrics data
│   └── agents/
│       └── metrics-analyst-agent.md      # AI agent for trend analysis
└── reports/
    ├── daily/                            # Daily status reports
    ├── weekly/                           # Weekly summaries
    └── monthly/                          # Monthly performance reviews
```

---

## 🚀 Quick Start Guide

### Step 1: Daily Productivity Assessment (5 minutes)
**When**: End of each workday
**Purpose**: Objective feedback on today's performance

1. Open `/productivity-assessment/templates/daily-assessment.md`
2. Fill in your actual completion data from today's roadmap
3. Invoke the Productivity Assessor Agent (or calculate score manually using rubric)
4. Save completed assessment to `/logs/daily/YYYY-MM-DD-assessment.md`
5. Review feedback and adjust tomorrow's plan

**Agent**: `/productivity-assessment/agents/productivity-assessor-agent.md`

---

### Step 2: Weekly Review (30 minutes)
**When**: Sunday evening or Monday morning
**Purpose**: Identify patterns and plan improvements

1. Open `/productivity-assessment/templates/weekly-review.md`
2. Aggregate data from past week's daily assessments
3. Calculate weekly averages and identify trends
4. Review blockers and success patterns
5. Plan next week's adjustments
6. Save to `/logs/weekly/week-YYYY-WW-review.md`

---

### Step 3: Project Portfolio Management (15 minutes weekly)
**When**: Monday morning or Sunday planning
**Purpose**: Ensure all projects maintain momentum

1. For each active project, update its status using `/project-management/active-projects/project-template.md`
2. Generate portfolio overview using Project Manager Agent
3. Identify blockers, dependencies, and risks
4. Define next actions for the week
5. Save portfolio snapshot to `/reports/weekly/`

**Agent**: `/project-management/agents/project-manager-agent.md`

---

### Step 4: Trend Analysis (Monthly)
**When**: Last Sunday of each month
**Purpose**: Strategic insights and system optimization

1. Collect 4 weeks of productivity data
2. Invoke Metrics Analyst Agent for trend analysis
3. Review patterns, forecasts, and recommendations
4. Implement system optimizations
5. Adjust processes based on insights
6. Save analysis to `/reports/monthly/`

**Agent**: `/metrics-tracking/agents/metrics-analyst-agent.md`

---

## 🤖 AI Agents

### 1. Productivity Assessor Agent
**Purpose**: Generate objective daily productivity assessments

**Key Features**:
- Calculates productivity score (1-10) using weighted rubric
- Identifies what worked and what held you back
- Spots patterns across multiple days
- Provides tomorrow's recovery plan
- Brutally honest feedback

**When to Use**: Daily, at end of workday

**Location**: `/productivity-assessment/agents/productivity-assessor-agent.md`

**Example Usage**:
```
[Paste agent prompt]

Here's my data for today:
- Tier 1: 3/3 completed
- Tier 2: 1/2 completed
- THE ONE THING: ✅ Completed
- P1 time: 5 hours (70%)
- Distractions: 30 minutes

Please assess my productivity.
```

---

### 2. Project Manager Agent
**Purpose**: Track project portfolio and generate status reports

**Key Features**:
- Monitors all active and incubated projects
- Calculates project health scores (1-10)
- Identifies dependencies and blockers
- Generates weekly action plans
- Flags at-risk projects early

**When to Use**: Weekly, during planning or project reviews

**Location**: `/project-management/agents/project-manager-agent.md`

**Example Usage**:
```
[Paste agent prompt]

Active Projects:
1. AI Agency Sales OS (P1, 40% complete)
2. Client Onboarding System (P2, 65% complete)

Please generate this week's portfolio status report.
```

---

### 3. Metrics Analyst Agent
**Purpose**: Analyze trends and provide predictive insights

**Key Features**:
- Identifies productivity trends over time
- Recognizes recurring patterns
- Forecasts future performance
- Provides data-driven optimization recommendations
- Performs root cause analysis

**When to Use**: Monthly, for strategic reviews

**Location**: `/metrics-tracking/agents/metrics-analyst-agent.md`

**Example Usage**:
```
[Paste agent prompt]

Past 4 weeks productivity:
Week 1: 7.2/10 avg, 5% OBG progress
Week 2: 7.6/10 avg, 8% OBG progress
Week 3: 6.2/10 avg, 4% OBG progress
Week 4: 7.8/10 avg, 10% OBG progress

Please analyze trends and provide recommendations.
```

---

## 📈 Key Metrics & KPIs

### Daily Metrics
- **Productivity Score**: 1-10 scale (Target: 7-8 average)
- **Tier 1 Completion**: % of must-do tasks (Target: 80%+)
- **THE ONE THING**: Completed Y/N (Target: 5/5 days per week)
- **Strategic Alignment**: 1-10 score (Target: 7+)

### Weekly Metrics
- **Average Daily Score**: Rolling 5-day average (Target: 7.0+)
- **Score Consistency**: Standard deviation (Target: <1.5)
- **OBG Progress**: % advancement (Target: 5-10% per week)
- **Blocker Impact**: Hours lost to recurring issues (Target: <5 hours)

### Monthly Metrics
- **Trend Direction**: Improving/stable/declining
- **Project Completion Rate**: % on schedule (Target: 80%+)
- **Time Estimation Accuracy**: Variance (Target: ±20%)
- **Strategic Time Allocation**: % on P1 (Target: 60%+)

---

## 🎯 Productivity Scoring Rubric

### Score Components (Weighted)
1. **Task Completion** (40%) - Tier 1/2 tasks + THE ONE THING
2. **Strategic Alignment** (30%) - OBG connection + priority distribution
3. **Time Efficiency** (20%) - Estimation accuracy + deep work completion
4. **Focus Quality** (10%) - Distraction management

### Score Interpretation
- **10**: Perfect execution (rare)
- **9**: Outstanding performance
- **8**: Excellent - sustainable high performance
- **7**: Good - solid productive day
- **6**: Fair - got work done, room for improvement
- **5**: Below target - struggled but made progress
- **4**: Poor - bad day, needs recovery
- **1-3**: Crisis - major intervention needed

**Target Range**: 7-8/10 average (sustainable excellence)

**Full Rubric**: `/productivity-assessment/templates/scoring-rubric.md`

---

## 🔄 Integration with Other Departments

### Inputs From:
- **Executive Office**: Daily roadmaps and strategic priorities
- **User**: Task completion data and time logs
- **Projects**: Status updates and progress reports

### Outputs To:
- **Executive Office**: Performance data for better planning
- **AI Growth Engine**: Metrics for strategic reviews
- **User**: Daily feedback and improvement recommendations
- **Knowledge Base**: Patterns and insights for system optimization

---

## 💡 Best Practices

### Daily Assessment
1. **Be Honest**: Low scores reveal truth, not failure
2. **Be Consistent**: Assess every workday for pattern recognition
3. **Be Quick**: 5 minutes max - don't overthink it
4. **Be Actionable**: Use feedback to adjust tomorrow's plan

### Project Tracking
1. **Update Weekly**: Minimum once per week per project
2. **Flag Early**: Yellow/red status as soon as issues emerge
3. **Define Next Actions**: Always have clear next steps
4. **Track Dependencies**: Don't let blocked projects surprise you

### Metrics Analysis
1. **Minimum Data**: Need 2+ weeks for basic patterns
2. **Look for Patterns**: Single data points are noise
3. **Act on Insights**: Analysis without action wastes time
4. **Iterate**: Refine your systems based on what data reveals

---

## 🚨 Common Issues & Solutions

### Issue: Consistently Low Scores (5-6 for 5+ days)
**Possible Causes**:
- Wrong priorities or unrealistic planning
- External blockers not being resolved
- Energy management issues

**Solutions**:
- Run strategic realignment check with Executive Office
- Conduct capacity reality check - are you overplanning?
- Review and eliminate recurring blockers
- Energy audit - match task energy to personal energy patterns

---

### Issue: High Score Volatility (swinging 3+ points daily)
**Possible Causes**:
- Inconsistent routines
- Poor daily planning
- Unmanaged interruptions

**Solutions**:
- Standardize morning and evening routines
- Improve daily planning with Executive Office agents
- Set and enforce boundaries around deep work time
- Track energy patterns and schedule accordingly

---

### Issue: Projects Stalling (No Progress 2+ Weeks)
**Possible Causes**:
- Unclear next actions
- Unresolved blockers
- Wrong priority level

**Solutions**:
- Define crystal-clear next action (verb + noun)
- Escalate blockers immediately
- Consider incubating if not aligned with OBG
- Reduce scope to ship something

---

## 📚 Templates & Resources

### Core Templates
- **Daily Assessment**: `/productivity-assessment/templates/daily-assessment.md`
- **Weekly Review**: `/productivity-assessment/templates/weekly-review.md`
- **Scoring Rubric**: `/productivity-assessment/templates/scoring-rubric.md`
- **Project Tracking**: `/project-management/active-projects/project-template.md`
- **Portfolio Overview**: `/project-management/PROJECT-STATUS-OVERVIEW.md`

### AI Agent Prompts
- **Productivity Assessor**: `/productivity-assessment/agents/productivity-assessor-agent.md`
- **Project Manager**: `/project-management/agents/project-manager-agent.md`
- **Metrics Analyst**: `/metrics-tracking/agents/metrics-analyst-agent.md`

---

## 🎯 Success Criteria

The Operations Department is working well when:

✅ **Consistent Assessment**: Daily productivity assessments completed 5/5 workdays
✅ **Score Stability**: Average score 7-8 with <1.5 standard deviation
✅ **Pattern Recognition**: Recurring issues identified and eliminated within 2-3 weeks
✅ **Project Momentum**: All active projects showing visible weekly progress
✅ **Strategic Alignment**: 60%+ of time spent on P1 priorities
✅ **Data-Driven Decisions**: Planning and adjustments based on metrics, not feelings
✅ **Continuous Improvement**: Week-over-week improvement in key metrics

---

## 🔄 Continuous Improvement Protocol

### Daily
- Complete productivity assessment
- Review feedback
- Adjust tomorrow's plan

### Weekly
- Aggregate daily data
- Identify patterns
- Update project statuses
- Plan week ahead optimizations

### Monthly
- Trend analysis
- System optimization
- Process refinement
- Goal recalibration

---

## 📖 Further Reading

- **Implementation Plan**: `implementation-plan.md`
- **13 Core Principles**: `/06-knowledge-base/core-principles/13-principles.md`
- **Executive Office Integration**: `/01-executive-office/README.md`

---

*"What gets measured gets managed and can be improved."*

*Operations Department - Claude Code OS*
*Version 1.0 - Built November 24, 2025*
