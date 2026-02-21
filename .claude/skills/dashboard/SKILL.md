---
name: dashboard
description: Generate comprehensive analytics dashboard showing business metrics, pipeline status, content performance, and system health. Use for weekly reviews, strategic planning, or executive overview.
---

# Dashboard Skill

## Purpose

Generate a comprehensive analytics view of the AI Agency Sales OS - pulling data from projects, pipeline, content, and system components to provide actionable business intelligence.

## When to Use This Skill

- Weekly business review
- Strategic planning sessions
- Investor/stakeholder updates
- Monthly performance analysis
- When asking "how is the business doing?"
- Before quarterly planning

## Data Sources

### 1. Pipeline & Revenue
- Active projects folder (`02-operations/project-management/active-projects/`)
- Discovery pipeline tracking
- Proposal status
- Revenue actuals vs targets

### 2. Content Performance
- Brand-illustrator projects (`.claude/skills/brand-illustrator/projects/`)
- Published content log
- Engagement metrics (if tracked in Notion)

### 3. Operations Health
- Weekly report history (`02-operations/weekly-reports/`)
- Action item completion rates
- Meeting frequency by client

### 4. System Metrics
- Skills usage (if logged)
- Integration health
- Documentation freshness

---

## Dashboard Sections

### Section 1: Executive Summary

```markdown
## 📊 Executive Dashboard - [DATE]

**Period:** [WEEK/MONTH of YEAR]
**Generated:** [TIMESTAMP]

### Key Metrics at a Glance

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Active Clients | [X] | [Y] | ✅/⚠️/🔴 |
| Pipeline Value | $[X] | $[Y] | ✅/⚠️/🔴 |
| Monthly Revenue | $[X] | $[Y] | ✅/⚠️/🔴 |
| Content Published | [X] | [Y] | ✅/⚠️/🔴 |
| Discovery Calls | [X] | [Y] | ✅/⚠️/🔴 |
```

### Section 2: Revenue & Pipeline

```markdown
### 💰 Revenue & Pipeline

**This Month:**
- Closed Revenue: $[X]
- Pipeline Value: $[X]
- Avg Deal Size: $[X]

**Pipeline Breakdown:**
| Stage | Count | Value |
|-------|-------|-------|
| Discovery | [X] | $[X] |
| Proposal | [X] | $[X] |
| Negotiation | [X] | $[X] |
| Verbal Yes | [X] | $[X] |

**Conversion Funnel:**
Lead → Discovery: [X]%
Discovery → Proposal: [X]%
Proposal → Close: [X]%

**Client Health:**
| Client | Status | MRR | Risk |
|--------|--------|-----|------|
| [Name] | Active | $[X] | 🟢/🟡/🔴 |
```

### Section 3: Project Delivery

```markdown
### 🚀 Project Delivery

**Active Projects:** [X]

| Project | Phase | Progress | Health | Next Milestone |
|---------|-------|----------|--------|----------------|
| [Name] | Build | [X]% | 🟢 | [Milestone] |
| [Name] | Discovery | [X]% | 🟡 | [Milestone] |

**This Week's Completions:**
- ✅ [Deliverable 1]
- ✅ [Deliverable 2]

**Blockers:**
- ⚠️ [Blocker 1] | Impact: [Project]
```

### Section 4: Content & Marketing

```markdown
### 📝 Content & Marketing

**Content Published (This Month):** [X] / [Target]

| Date | Title | Platform | Engagement |
|------|-------|----------|------------|
| [Date] | [Title] | LinkedIn | [Likes/Comments] |

**Content Queue:** [X] drafts pending

**Top Performing (Last 30 Days):**
1. [Title] - [X] impressions, [Y] engagements
2. [Title] - [X] impressions, [Y] engagements

**Content Pillar Balance:**
- Build-in-Public: [X]% (target: 40%)
- AI Insights: [X]% (target: 30%)
- Productivity: [X]% (target: 20%)
- Client Value: [X]% (target: 10%)
```

### Section 5: Operations Health

```markdown
### ⚙️ Operations Health

**Action Items:**
- Open: [X]
- Completed this week: [X]
- Overdue: [X]

**Meeting Cadence:**
- Internal meetings: [X] this week
- Client meetings: [X] this week
- Discovery calls: [X] this week

**System Health:**
| Component | Status | Last Check |
|-----------|--------|------------|
| Notion Sync | ✅ | [Time] |
| Slack | ✅ | [Time] |
| Weekly Report | ✅ | [Date] |
| Git | ✅ Clean | [Now] |
```

### Section 6: Strategic Alignment

```markdown
### 🎯 Strategic Alignment

**OBG Progress:** [Brief status on One Big Goal]

**This Week's Focus:**
1. [Priority 1] - [Status]
2. [Priority 2] - [Status]
3. [Priority 3] - [Status]

**Key Decisions Needed:**
- [ ] [Decision 1]
- [ ] [Decision 2]

**Risks & Mitigations:**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Action] |
```

### Section 7: Recommendations

```markdown
### 💡 Recommendations

Based on current data, priority actions:

1. **[Action]** - [Rationale based on metrics]
2. **[Action]** - [Rationale based on metrics]
3. **[Action]** - [Rationale based on metrics]

**Opportunities Identified:**
- [Opportunity based on data pattern]

**Warnings:**
- ⚠️ [Warning based on negative trend]
```

---

## Data Collection Workflow

### Step 1: Scan Projects
```
02-operations/project-management/active-projects/
```
For each project:
- Read README for client/status
- Count recent meetings
- Check deliverables status
- Extract revenue/investment data

### Step 2: Scan Pipeline
```
02-operations/discovery-process/
```
- Count leads at each stage
- Calculate conversion rates
- Sum pipeline value

### Step 3: Scan Content
```
.claude/skills/brand-illustrator/projects/
.claude/skills/brand-illustrator/published-log.md (if exists)
```
- Count published content
- Count pending drafts
- Calculate pillar distribution

### Step 4: Scan Operations
```
02-operations/weekly-reports/
01-executive-office/internal-business-meetings/action-items/
```
- Count open/closed items
- Calculate completion rate
- Find overdue items

### Step 5: Check System Health
- Git status
- Check for required env vars
- Verify last report dates

### Step 6: Calculate & Compare
- Compare actuals vs targets
- Calculate trends (week-over-week, month-over-month)
- Flag anomalies

---

## Output Formats

### Quick View (Default)
Single markdown document with all sections, emoji-coded status indicators.

### Slack Summary
Condensed version for posting to Slack:
```
📊 *Weekly Dashboard - [DATE]*

💰 Revenue: $[X] / $[Target] [emoji]
🚀 Projects: [X] active, [Y] on track
📝 Content: [X] published this month
⚙️ Health: [X] open items, [Y] overdue

Top Priority: [Most important action]

Full dashboard: [link to markdown file]
```

### Notion Sync
Push dashboard to Notion page for team visibility using notion-sync skill.

---

## Targets & Benchmarks

Configure targets in a `dashboard-config.json`:

```json
{
  "targets": {
    "monthly_revenue": 25000,
    "active_clients": 3,
    "pipeline_value": 75000,
    "content_per_month": 8,
    "discovery_calls_per_week": 2
  },
  "thresholds": {
    "green": 0.9,
    "yellow": 0.7,
    "red": 0.5
  }
}
```

Status indicators:
- 🟢 ≥ 90% of target
- 🟡 70-89% of target
- 🔴 < 70% of target

---

## Automation

### Scheduled Generation
- **Weekly:** Every Friday at 4pm (end of week review)
- **Monthly:** First Monday of month (monthly review)

### Triggers
- `/dashboard` - Generate on demand
- `/dashboard weekly` - Weekly summary format
- `/dashboard monthly` - Full monthly analysis
- `/dashboard slack` - Generate and post to Slack

---

## Integration Points

- **weekly-report** - Feeds operations data
- **notion-sync** - Push dashboard to Notion
- **slack module** - Post summaries to channel
- **status command** - Quick health check (subset of dashboard)

---

## Example Output

```
📊 EXECUTIVE DASHBOARD - Week 4, January 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Metrics

| Metric | Actual | Target | Status |
|--------|--------|--------|--------|
| Monthly Revenue | $18,500 | $25,000 | 🟡 74% |
| Active Clients | 3 | 3 | 🟢 100% |
| Pipeline Value | $92,000 | $75,000 | 🟢 123% |
| Content Published | 6 | 8 | 🟡 75% |
| Discovery Calls | 3 | 2 | 🟢 150% |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pipeline Health

Discovery: 4 leads ($45K)
Proposal: 2 prospects ($32K)
Negotiation: 1 prospect ($15K)

Conversion: Lead→Discovery 20% | Discovery→Proposal 50% | Proposal→Close 33%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Active Projects

🟢 PlotterMechanix | Phase 1 Build | 65% | On Track
🟢 Wolf Sheds | Discovery | 40% | On Track
🟡 Internal Systems | Ongoing | - | Needs Attention

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Recommendations

1. 🔥 Close the negotiation-stage deal (add $15K to this month)
2. 📝 Publish 2 more content pieces to hit monthly target
3. 📞 Follow up on 2 discovery calls scheduled for next week

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated by /dashboard | Synced to Notion
```
