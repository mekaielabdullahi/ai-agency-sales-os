# Content Strategy Alignment Agent

**Purpose**: Ensure content narratives align with actual strategic direction, even when priorities shift mid-week

**Created**: November 27, 2025
**Department**: Content Team
**Role**: Strategic Content Coordinator

---

## 🎯 CORE RESPONSIBILITY

**Primary Function**: Monitor weekly strategic direction and adjust content narratives to reflect reality, not just plans.

**The Problem This Solves**:
- You plan content on Monday for Tuesday/Thursday posts
- By Wednesday, strategic priorities have shifted
- Scheduled posts no longer match what you're actually doing
- Content feels disconnected from reality

**The Solution**:
- Daily alignment checks between planned work and actual work
- Automatic detection of strategic shifts
- Content adjustment recommendations
- Bridge post triggers when narrative needs course correction

---

## 📊 AGENT WORKFLOW

### **MONDAY: Weekly Strategy Capture**

**Input Required**:
1. This week's ONE THING (from Executive Office daily roadmap)
2. Planned focus areas for the week
3. Scheduled content topics (Tuesday & Thursday posts)
4. Current OBG (Overarching Business Goal)

**Agent Actions**:
- [ ] Capture week's strategic intent
- [ ] Review scheduled post topics
- [ ] Flag potential misalignments early
- [ ] Set baseline for daily tracking

**Output**: `weekly-strategy-baseline.md`

---

### **TUESDAY: Pre-Post Alignment Check**

**Input Required**:
1. Monday's actual work vs planned work
2. Tuesday morning's priorities
3. Drafted Tuesday post (if scheduled)

**Agent Actions**:
- [ ] Compare drafted post to actual strategic direction
- [ ] Flag if post doesn't match reality
- [ ] Suggest adjustments if needed
- [ ] Approve or recommend revision

**Decision Tree**:
```
Is the Tuesday post aligned with actual work?
├─ YES → Approve for posting
└─ NO → Recommend adjustment
    ├─ Minor misalignment → Quick edit
    └─ Major misalignment → Rewrite or reschedule
```

**Output**: Approval or revision recommendations

---

### **WEDNESDAY: Strategic Shift Detection**

**Input Required**:
1. Tuesday's actual work completed
2. Wednesday morning's priorities
3. Comparison to Monday's planned direction

**Agent Actions**:
- [ ] Detect if strategic shift occurred
- [ ] Assess magnitude of shift (minor, moderate, major)
- [ ] Decide if bridge post is warranted
- [ ] Draft bridge post if needed

**Bridge Post Trigger Criteria**:
A Wednesday bridge post is warranted if ANY of these are true:
1. **Major pivot**: Week's focus changed significantly (internal → client, product → sales, etc.)
2. **Narrative gap**: Tuesday post doesn't connect to Thursday post anymore
3. **Engagement opportunity**: The pivot itself is worth sharing (meta-content)
4. **Accountability play**: Publicly committing to new direction increases follow-through

**Decision Tree**:
```
Did strategic direction shift?
├─ NO → No bridge post needed, proceed to Thursday prep
└─ YES → How significant?
    ├─ Minor (tactical adjustment) → No bridge post, adjust Thursday post
    ├─ Moderate (focus shift) → Optional bridge post, document shift
    └─ Major (strategic pivot) → Bridge post recommended
        ├─ Draft bridge post
        ├─ Adjust Thursday post to reflect shift
        └─ Update weekly narrative arc
```

**Output**: Bridge post recommendation + draft (if applicable)

---

### **THURSDAY: Pre-Post Alignment Check + Series Completion**

**Input Required**:
1. Tuesday-Wednesday actual work
2. Drafted Thursday post
3. Full week's narrative arc

**Agent Actions**:
- [ ] Ensure Thursday post completes the weekly narrative
- [ ] Verify alignment with actual work completed
- [ ] Check consistency with Tuesday post (or bridge post)
- [ ] Recommend adjustments if needed
- [ ] Prepare for next week's planning

**Narrative Arc Check**:
```
Does the full week tell a coherent story?
├─ Tuesday post: What you built/did
├─ Wednesday (optional): How direction shifted
├─ Thursday post: Lessons learned
└─ Overall: Does it flow logically?
```

**Output**: Approval or revision recommendations + weekly summary

---

### **FRIDAY: Weekly Review & Learning**

**Input Required**:
1. Engagement metrics from Tuesday & Thursday posts (+ Wednesday if posted)
2. Actual strategic direction vs planned
3. Content narrative effectiveness

**Agent Actions**:
- [ ] Analyze what worked vs what didn't
- [ ] Document strategic shifts that occurred
- [ ] Identify patterns (do you always pivot mid-week?)
- [ ] Recommend adjustments for next week
- [ ] Update content strategy based on learnings

**Output**: `weekly-content-review.md` with insights for next week

---

## 🧠 DECISION FRAMEWORKS

### **Framework 1: Alignment Scoring**

Score the alignment between content and reality (1-10):

**9-10 (Perfect Alignment)**:
- Content accurately reflects actual work
- Narrative matches strategic direction
- No adjustments needed

**7-8 (Good Alignment)**:
- Minor discrepancies, easily explained
- Core message still valid
- Quick edits can improve

**5-6 (Moderate Misalignment)**:
- Content doesn't match actual priorities
- Narrative feels disconnected
- Significant revisions recommended

**1-4 (Major Misalignment)**:
- Content completely off from reality
- Would confuse or mislead audience
- Rewrite or reschedule required

**Action Thresholds**:
- 9-10: Publish as-is
- 7-8: Quick edits, then publish
- 5-6: Major revision before publishing
- 1-4: Scrap and rewrite or skip post

---

### **Framework 2: Bridge Post Decision Matrix**

| Strategic Shift Size | Narrative Gap | Engagement Value | Bridge Post? |
|---------------------|---------------|------------------|--------------|
| Minor | Small | Low | No |
| Minor | Moderate | High | Optional |
| Moderate | Small | Low | Optional |
| Moderate | Moderate | Moderate | Yes |
| Moderate | Large | High | Yes |
| Major | Any | Any | Yes |

---

### **Framework 3: Content Pivot Types**

**Type 1: Tactical Adjustment** (No bridge needed)
- Example: Planned to build 3 features, built 2 instead
- Content fix: Update numbers, proceed with narrative

**Type 2: Focus Shift** (Bridge optional)
- Example: Spent more time on operations than planned
- Content fix: Acknowledge shift, explain why, continue

**Type 3: Strategic Pivot** (Bridge recommended)
- Example: Switched from internal systems to client frameworks
- Content fix: Bridge post explaining pivot + adjusted Thursday post

**Type 4: Complete Direction Change** (Bridge required + major edits)
- Example: Abandoned planned project for new opportunity
- Content fix: Full narrative reframe, bridge post, new Thursday post

---

## 📋 TEMPLATES

### **Template 1: Weekly Strategy Baseline**

```markdown
# Weekly Strategy Baseline
**Week of**: [Date]
**Week Number**: [#] of [Year]

## Strategic Intent
**This Week's ONE THING**: [From Monday roadmap]
**Current OBG**: [Overarching Business Goal]
**Primary Focus Areas**:
1. [Area 1]
2. [Area 2]
3. [Area 3]

## Scheduled Content
**Tuesday Post**: [Topic/angle]
**Thursday Post**: [Topic/angle]
**Narrative Arc**: [How they connect]

## Alignment Baseline
On Monday, the content aligns with strategic intent: [YES/NO]
If no, what needs to change: [Adjustments]

## Success Metrics
How we'll know content is aligned:
- [ ] Tuesday post reflects actual Monday-Tuesday work
- [ ] Thursday post completes a coherent weekly narrative
- [ ] Audience engagement indicates message resonance
- [ ] Strategic goals advanced through content

---
*Captured: [Date/Time]*
*Next review: Tuesday morning*
```

---

### **Template 2: Daily Alignment Check**

```markdown
# Daily Alignment Check
**Date**: [Date]
**Day**: [Monday/Tuesday/Wednesday/Thursday/Friday]

## Today's Planned Work
**From Daily Roadmap**:
- [Priority 1]
- [Priority 2]
- [Priority 3]

## Today's Actual Work
**What Actually Got Done**:
- [Actual 1]
- [Actual 2]
- [Actual 3]

## Alignment Assessment
**Planned vs Actual Match**: [High/Moderate/Low]
**Alignment Score**: [1-10]

**Explanation**:
[Why did priorities shift? Was it intentional or reactive?]

## Content Implications
**Scheduled Post Status**: [Tuesday/Thursday/None today]

**Does scheduled post still align?**: [YES/NO]

**If NO, what needs to change**:
- [ ] Minor edit (specific line/number)
- [ ] Moderate revision (reframe one section)
- [ ] Major rewrite (new angle needed)
- [ ] Bridge post needed (document the shift)

## Action Items
- [ ] [Specific action 1]
- [ ] [Specific action 2]

---
*Checked: [Date/Time]*
*Next check: [Tomorrow]*
```

---

### **Template 3: Bridge Post Trigger Assessment**

```markdown
# Bridge Post Trigger Assessment
**Date**: Wednesday, [Date]
**Week of**: [Date]

## Strategic Shift Analysis

**Monday's Plan**:
[What you planned to focus on this week]

**Tuesday's Reality**:
[What actually happened Tuesday]

**Wednesday's Direction**:
[Where you're headed today]

**Shift Magnitude**: [Minor/Moderate/Major]

## Narrative Gap Analysis

**Tuesday Post Said**:
[Summary of Tuesday's content message]

**Thursday Post Will Say**:
[Summary of planned Thursday content]

**Gap Between Them**:
[Is there a logical connection? Or does it feel disjointed?]

**Narrative Gap Size**: [Small/Moderate/Large]

## Engagement Value

**Is the shift itself interesting/valuable?**: [YES/NO]

**Would sharing the pivot help others?**: [YES/NO]

**Does it demonstrate your product/service?**: [YES/NO]

**Engagement Value**: [Low/Moderate/High]

## Decision Matrix Result

| Factor | Rating |
|--------|--------|
| Shift Size | [Minor/Moderate/Major] |
| Narrative Gap | [Small/Moderate/Large] |
| Engagement Value | [Low/Moderate/High] |

**Bridge Post Recommendation**: [YES/NO/OPTIONAL]

## If YES: Bridge Post Draft

**Angle**:
[What's the hook? Why is this shift worth sharing?]

**Key Message**:
[What's the lesson/insight from the pivot?]

**Bridge Function**:
[How does this connect Tuesday → Thursday?]

**Draft** (Quick version):
```
[Actual post text here]
```

## If NO: Thursday Post Adjustment

**What needs to change in Thursday post**:
- [ ] [Adjustment 1]
- [ ] [Adjustment 2]

---
*Assessed: [Date/Time]*
*Decision: [Post bridge/Skip bridge/Adjust Thursday]*
```

---

### **Template 4: Weekly Content Review**

```markdown
# Weekly Content Review
**Week of**: [Date]
**Week Number**: [#] of [Year]

## Strategic Direction

**Planned Direction** (Monday):
[What you intended to focus on]

**Actual Direction** (Friday):
[What you actually focused on]

**Alignment Score**: [1-10]
**Pivot Count**: [# of strategic shifts this week]

## Content Published

**Tuesday Post**:
- Topic: [Topic]
- Engagement: [Likes, comments, shares]
- Alignment Score: [1-10]
- What worked: [Insights]
- What didn't: [Insights]

**Wednesday Bridge Post** (if applicable):
- Topic: [Topic]
- Engagement: [Likes, comments, shares]
- Was it necessary?: [YES/NO]
- What worked: [Insights]

**Thursday Post**:
- Topic: [Topic]
- Engagement: [Likes, comments, shares]
- Alignment Score: [1-10]
- Narrative completion: [Did it close the week's story?]
- What worked: [Insights]
- What didn't: [Insights]

## Narrative Arc Assessment

**Did the week tell a coherent story?**: [YES/NO]

**Story Summary**:
[In 2-3 sentences, what was this week's narrative?]

**Audience Response**:
[Did engagement indicate the story resonated?]

## Learnings

**Content Insights**:
1. [What content format/angle worked best?]
2. [What messaging resonated most?]
3. [What should we do more of?]
4. [What should we do less of?]

**Strategic Insights**:
1. [Do you consistently pivot on certain days?]
2. [Are your Monday plans realistic?]
3. [What triggers strategic shifts?]
4. [Should you plan differently?]

## Recommendations for Next Week

**Content Planning**:
- [ ] [Recommendation 1]
- [ ] [Recommendation 2]

**Strategic Planning**:
- [ ] [Recommendation 1]
- [ ] [Recommendation 2]

**Process Improvements**:
- [ ] [Improvement 1]
- [ ] [Improvement 2]

---
*Reviewed: [Date/Time]*
*Next review: [Next Friday]*
```

---

## 🚀 IMPLEMENTATION GUIDE

### **Phase 1: Setup (Week 1)**

**Day 1: Monday**
1. Read this week's daily roadmap from Executive Office
2. Fill out Weekly Strategy Baseline template
3. Review scheduled Tuesday & Thursday post topics
4. Flag any immediate misalignments

**Day 2: Tuesday Morning**
1. Complete Daily Alignment Check
2. Review Tuesday post draft
3. Approve or recommend adjustments
4. Post goes live (if approved)

**Day 3: Wednesday**
1. Complete Daily Alignment Check
2. Run Bridge Post Trigger Assessment
3. Draft bridge post if warranted
4. Begin adjusting Thursday post based on week's reality

**Day 4: Thursday Morning**
1. Complete Daily Alignment Check
2. Review Thursday post draft
3. Ensure it completes the weekly narrative
4. Approve or recommend adjustments
5. Post goes live (if approved)

**Day 5: Friday**
1. Complete Weekly Content Review
2. Analyze what worked / what didn't
3. Document learnings
4. Prepare recommendations for next week

---

### **Phase 2: Optimization (Week 2-4)**

**Refine Based on Learnings**:
- Adjust alignment scoring criteria
- Refine bridge post trigger thresholds
- Optimize templates based on what's useful
- Build pattern library of successful pivots

**Build Efficiency**:
- Create faster daily check-ins (5 min max)
- Pre-write common bridge post frameworks
- Develop quick-reference decision trees
- Automate metric tracking where possible

---

### **Phase 3: Scaling (Week 5+)**

**Expand to Full Content Calendar**:
- Apply to additional posts (not just Tue/Thu)
- Coordinate cross-platform content
- Manage longer narrative arcs (month-long campaigns)
- Integrate with sales/marketing campaigns

**Advanced Features**:
- Predictive shift detection (based on patterns)
- Auto-drafted content adjustments
- Real-time alignment dashboards
- Multi-week narrative planning

---

## 📂 FILE STRUCTURE

```
claude-code-os-implementation/
└── 04-content-team/
    ├── agents/
    │   └── content-strategy-alignment-agent.md (this file)
    ├── alignment-tracking/
    │   ├── weekly-baselines/
    │   │   ├── 2025-week-48-baseline.md
    │   │   ├── 2025-week-49-baseline.md
    │   │   └── [ongoing...]
    │   ├── daily-checks/
    │   │   ├── 2025-11-25-alignment-check.md
    │   │   ├── 2025-11-26-alignment-check.md
    │   │   ├── 2025-11-27-alignment-check.md
    │   │   └── [ongoing...]
    │   ├── bridge-assessments/
    │   │   ├── 2025-11-26-bridge-assessment.md
    │   │   └── [when needed...]
    │   └── weekly-reviews/
    │       ├── 2025-week-48-review.md
    │       └── [ongoing...]
    └── linkedin-posts/
        └── [posts go here as usual]
```

---

## 🎯 SUCCESS METRICS

**Agent Effectiveness**:
- **Alignment Score Average**: Target 8+/10 across all posts
- **Unnecessary Bridge Posts**: 0 (only post when truly warranted)
- **Missed Necessary Bridges**: 0 (catch all major shifts)
- **Content Revision Rate**: <20% (better planning = less revision)

**Business Impact**:
- **Engagement Rate**: Higher on aligned content vs misaligned
- **Audience Trust**: Consistent authenticity builds credibility
- **AriseGroup.ai Traffic**: Content that matches reality converts better
- **DM Quality**: Better fit leads when content is authentic

---

## 💡 AGENT PROMPTS

### **Monday Prompt: Capture Weekly Strategy**

```
I need to capture this week's strategic baseline for content alignment.

Please review:
1. This week's daily roadmap: [path to file]
2. Current OBG from Executive Office
3. Scheduled content topics for Tuesday & Thursday

Then fill out the Weekly Strategy Baseline template and save it to:
alignment-tracking/weekly-baselines/[year]-week-[#]-baseline.md

Flag any immediate misalignments between planned work and scheduled content.
```

---

### **Tuesday Morning Prompt: Pre-Post Check**

```
I have a LinkedIn post scheduled for today. Before I publish, I need alignment verification.

Please:
1. Review Monday's actual work from daily roadmap
2. Review Tuesday morning's priorities
3. Read the drafted Tuesday post: [path to post file]
4. Complete the Daily Alignment Check template

Does the post align with what I'm actually doing this week?
- If yes: Approve for posting
- If no: Recommend specific adjustments

Save check to: alignment-tracking/daily-checks/[date]-alignment-check.md
```

---

### **Wednesday Prompt: Shift Detection**

```
It's Wednesday - time to detect if strategic direction shifted.

Please:
1. Review Monday's planned direction from weekly baseline
2. Review Tuesday's actual work from daily roadmap
3. Review Wednesday morning's priorities
4. Run the Bridge Post Trigger Assessment

Determine:
- Did strategic direction shift? If so, how significantly?
- Is a Wednesday bridge post warranted?
- If yes, draft the bridge post
- If no, note what adjustments Thursday post needs

Save assessment to: alignment-tracking/bridge-assessments/[date]-bridge-assessment.md
```

---

### **Thursday Morning Prompt: Series Completion Check**

```
Thursday post goes live today. I need to ensure it completes the weekly narrative.

Please:
1. Review all work completed Tuesday-Wednesday
2. Review the drafted Thursday post: [path to post file]
3. Check narrative coherence with Tuesday post (and Wednesday if posted)
4. Complete the Daily Alignment Check template

Does Thursday post:
- Align with actual work done?
- Complete the weekly narrative arc?
- Connect logically with earlier posts?

Recommend adjustments if needed.

Save check to: alignment-tracking/daily-checks/[date]-alignment-check.md
```

---

### **Friday Prompt: Weekly Review**

```
Week is complete. Time to review and learn.

Please:
1. Gather engagement metrics from this week's posts
2. Compare planned vs actual strategic direction
3. Assess content effectiveness
4. Complete the Weekly Content Review template

Identify:
- What worked / what didn't
- Patterns in strategic shifts
- Recommendations for next week

Save review to: alignment-tracking/weekly-reviews/[year]-week-[#]-review.md
```

---

## 🔄 INTEGRATION WITH OTHER AGENTS

**Executive Office**:
- Input: Daily roadmaps, weekly ONE THING, OBG
- Output: Content aligned with strategic priorities

**Content Team**:
- Input: Content strategy shifts
- Output: Adjusted post recommendations

**Operations**:
- Input: Productivity assessments, actual work completed
- Output: Reality-based content, not aspirational

---

## ✅ QUICK START CHECKLIST

**To activate this agent for next week**:

- [ ] Read this full agent document
- [ ] Create the file structure (alignment-tracking folder + subfolders)
- [ ] On Monday: Run "Capture Weekly Strategy" prompt
- [ ] On Tuesday AM: Run "Pre-Post Check" prompt
- [ ] On Wednesday: Run "Shift Detection" prompt
- [ ] On Thursday AM: Run "Series Completion Check" prompt
- [ ] On Friday: Run "Weekly Review" prompt

**After 4 weeks**:
- [ ] Review all weekly reviews
- [ ] Identify patterns
- [ ] Optimize templates and thresholds
- [ ] Decide if agent is providing value or needs adjustment

---

*Agent Created: November 27, 2025*
*Version: 1.0*
*Status: Ready for implementation Week 49 (December 2-6, 2025)*
