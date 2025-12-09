# Liam Ottley Framework vs AriseGroup.ai Audit System - Comparison Analysis

**Date**: 2025-12-09
**Purpose**: Compare Liam Ottley's $10K AI Audit framework with our existing comprehensive-ai-audit system to identify gaps and integration opportunities

---

## Executive Summary

### Key Findings
✅ **Strong Alignment**: Both frameworks follow similar audit structures with discovery → mapping → opportunities → roadmap → presentation
⚠️ **Gaps Identified**: Liam's framework includes specific interview templates, Ops Canvas visualization, and detailed ROI calculators we're missing
🎯 **Recommendation**: Integrate Liam's interview guides and ROI calculation methodology into our existing audit.json workflow

---

## Side-by-Side Framework Comparison

| Aspect | Liam Ottley Framework | AriseGroup.ai Current System | Gap? |
|--------|----------------------|------------------------------|------|
| **Structure** | 3-step framework | 7-phase workflow | ❌ Similar scope |
| **Interview Guides** | ✅ Stakeholder + End-user templates with specific questions | ⚠️ Generic "ask discovery questions" guidance | ⚠️ **GAP** |
| **Process Mapping** | ✅ Ops Canvas (3 engines: Acquisition, Delivery, Support) | ✅ current_state_maps with detailed steps | ❌ Similar |
| **Opportunity Matrix** | ✅ 2x2 matrix (Impact vs Effort) with 4 quadrants | ✅ ai_opportunity_matrix with impact/effort scoring | ❌ Similar |
| **Validation Step** | ✅ Explicit co-creation workshop with stakeholders | ⚠️ Not explicitly documented | ⚠️ **GAP** |
| **ROI Calculator** | ✅ Two-part: Direct cost savings + Revenue uplift | ⚠️ Generic ROI in roadmap section | ⚠️ **GAP** |
| **Presentation Templates** | ✅ 5 specific slide templates provided | ✅ presentation_outline with 7 slides | ❌ Similar |
| **Pricing Guidance** | ✅ "$10K for 2 weeks" explicitly stated | ✅ "$3K-$10K paid engagement" in docs | ❌ Similar |
| **Data Format** | ⚠️ Implied (slides/docs) | ✅ Structured audit.json | ✅ **ADVANTAGE** |
| **Automation** | ⚠️ Manual process | ✅ Claude Code skill with agent guidance | ✅ **ADVANTAGE** |

---

## Detailed Comparison by Phase

### Phase 1: Discovery & Interviews

#### Liam Ottley Approach
**Step 1: The Discovery Interviews**
- **Two distinct interview types**:
  1. **Stakeholder Interview** (30,000-foot view)
     - Role & team overview
     - Core processes & workflow
     - Tools & technology
     - Pain points & strategic challenges
     - Future vision
  2. **End-User Interview** (on-the-ground reality)
     - Daily role & responsibilities
     - Step-by-step process deep dive
     - Tools & frustrations
     - Pain points & wishlist

- **Specific guidance**:
  - 3-5 interviews for small businesses (10-50 employees)
  - 10-15 for larger/complex departments
  - 30-45 minutes each
  - Remote video calls
  - Record with permission (Fireflies.ai)
  - 80/20 listening rule
  - Ask "Why?" repeatedly

- **Sample questions provided** for both interview types

#### AriseGroup.ai Current System
**Phase 2: Intake & Context (30-45 min)**
- Ask discovery questions about:
  - Industry, size, revenue
  - Products/services, ICP
  - Sales model, tech stack
  - Business goals (top 3)
  - Constraints
  - In-scope processes

- **Generic guidance**:
  - Review sales handoff packet first
  - Use intake forms
  - Agent asks "minimum number of questions"

#### Gap Analysis
⚠️ **MISSING**:
- Specific stakeholder vs end-user interview templates
- Detailed question bank
- Interview best practices (recording, 80/20 rule, "why" technique)
- Interview count guidance based on company size
- Clear distinction between leadership perspective and on-the-ground reality

✅ **ADVANTAGE**:
- Integration with sales handoff and intake forms
- Automated via Claude Code skill

---

### Phase 2: Process Mapping

#### Liam Ottley Approach
**Part A: Create the Ops Canvas**
- **Visual flowchart** of core operations
- **3 fundamental engines**:
  1. Acquisition Engine: How they find and sign customers
  2. Delivery Engine: How they deliver product/service
  3. Support Engine: Customer questions and post-sale issues

- **Legend system**:
  - 🟡 Time Sinks: Manual, repetitive, time-consuming
  - 🟡 Quality Risks: Prone to errors/inconsistencies

- **Tool**: Miro or FigJam for visualization

#### AriseGroup.ai Current System
**Phase 3: Current-State Mapping (2-4 hours)**
- Document 3-5 critical processes
- **Structured JSON format**:
  - `process_id`, `name`, `function_area`
  - `owner_roles`, `trigger`, `frequency`, `duration`
  - `steps[]` with who/what/tool/duration/pain_points
  - `systems[]`, `data_touchpoints[]`
  - `pain_points[]` with frequency/impact/time_cost/error_rate
  - `metrics{}` with volume/cycle_time/error_rate/cost

- **Integration**: Business Functions Mapping skill

#### Gap Analysis
⚠️ **DIFFERENT APPROACH**:
- Liam uses **visual Ops Canvas** (3 engines framework)
- We use **structured JSON** (more detailed, machine-readable)

⚠️ **MISSING**:
- Visual flowchart/diagram output
- Simple 3-engine categorization framework
- Color-coded tagging system

✅ **ADVANTAGE**:
- More detailed structured data
- Quantified metrics built-in
- Machine-readable for automation
- Integration with business functions mapping

💡 **OPPORTUNITY**: Add visual diagram generation from audit.json data

---

### Phase 3: Opportunity Identification & Prioritization

#### Liam Ottley Approach
**Part B: Build the Opportunity Matrix**
- **2x2 Matrix**: Impact (X-axis) vs Effort (Y-axis)
- **4 Quadrants**:
  1. ⭐ **Quick Wins** (Low Effort, High Impact) - #1 priority
  2. 🚀 **Big Swings** (High Effort, High Impact) - Long-term, high-ticket
  3. 👍 **Nice-to-Haves** (Low Effort, Low Impact) - Extra value
  4. 🗑️ **Deprioritize** (High Effort, Low Impact) - Avoid

- **Explicit focus**: Start with Quick Wins to build trust

**Part C: Validate Your Solutions**
- **Co-creation workshop** with stakeholders
- Review matrix collaboratively
- Ask validation questions:
  - "Which Quick Wins resonate most?"
  - "Any hidden complexities we missed?"
  - "Which would team embrace/resist?"
  - "Align with strategic priorities?"

- **Outcome**: Agreed-upon prioritized list (not a pitch)

#### AriseGroup.ai Current System
**Phase 4: AI Opportunity Discovery (1-2 hours)**
- Identify 5-10 opportunities
- **Scoring system**:
  - Impact: high/medium/low
  - Effort: high/medium/low
  - Speed to value (days)
  - Priority score calculation

- **Structured data**:
  - `impact_details`: time_saved, cost_reduction, revenue_impact
  - `effort_details`: technical_complexity, integration_points, build_time
  - `data_requirements[]`, `risks[]`, `dependencies[]`

- **Prioritization Formula**:
  ```
  Priority Score = (Impact Weight × 2) + Feasibility + ROI / 4
  ```

#### Gap Analysis
✅ **SIMILAR APPROACH**: Both use Impact vs Effort matrix

⚠️ **MISSING**:
- Visual 2x2 matrix representation
- Explicit 4-quadrant framework (Quick Wins, Big Swings, etc.)
- **Validation workshop step** - this is a KEY missing piece
- Collaborative refinement process
- Clear "Quick Wins first" strategy communication

✅ **ADVANTAGE**:
- More detailed quantification
- Structured risk assessment
- Data requirements documented
- Priority score formula

💡 **OPPORTUNITY**:
- Add explicit validation step to workflow
- Generate visual 2x2 matrix from opportunity data
- Add "quadrant" field to opportunities (quick_win, big_swing, nice_to_have, deprioritize)

---

### Phase 4: ROI Calculation

#### Liam Ottley Approach
**The ROI Calculator: Two-Part System**

**Part 1: Calculate Direct Cost Savings**
```
Step 1: Hours Saved
- Time spent per week × Number of employees × % saved = Hours Saved Per Week

Step 2: Annual Cost Savings
- Average Annual Salary / 2080 = Hourly Rate
- Hours Saved × Hourly Rate × 52 = Annual Cost Savings

Step 3: Simple ROI
- (Annual Savings / Implementation Cost) × 100 = ROI %
```

**Part 2: Calculate Revenue Uplift** ⭐ KEY DIFFERENTIATOR
```
Step 1: Reallocated Hours
- Hours Saved Per Week × 50% = Revenue-Generating Hours Unlocked

Step 2: Additional Revenue
- Revenue-Generating Hours × Value per Hour × 52 = Potential Annual Revenue

Example: If sales rep saves 10 hours/week, 5 hours go to more selling
If 2 hours = $5,000 deal, each hour = $2,500
5 hours × $2,500 × 52 = $650,000 annual revenue potential
```

**ROI Presentation**:
- Table format showing each solution
- Implementation costs
- Direct savings
- Revenue uplift
- Total financial impact

#### AriseGroup.ai Current System
**ROI in Roadmap Section**
- For each phase:
  - `estimated_effort`: "40-60 hours"
  - `estimated_value`: "$2,000/month time savings + $3,000/month revenue recovery"

- **Aggregate calculations**:
  - `total_timeline`
  - `total_estimated_effort`
  - `total_estimated_value`
  - `roi_break_even`

- **Report section**:
  - `investment_and_roi` object with:
    - total_investment
    - monthly_recurring_value
    - break_even_point
    - 12_month_roi
    - 36_month_value

#### Gap Analysis
⚠️ **MISSING**:
- **Detailed ROI calculation methodology** - Liam provides step-by-step formulas
- **Revenue uplift calculation** - This is a KEY missing component
  - We focus on cost savings but don't explicitly calculate revenue opportunity from reallocated time
- **Per-opportunity ROI breakdown** - We have aggregate, but not individual solution ROI
- **"Money Slide" table format** - Visual ROI summary

✅ **ADVANTAGE**:
- Multi-timeframe view (12-month, 36-month)
- Break-even calculation
- Monthly recurring value concept

💡 **OPPORTUNITY**:
- Add ROI calculation template to audit.json
- Include revenue uplift methodology
- Create "Money Slide" generator from roadmap data
- Add per-opportunity ROI calculations

---

### Phase 5: Presentation & Deliverables

#### Liam Ottley Approach
**The 5 Key Slides You MUST Include**

1. **Scope & Objectives Slide**
   - Restate project goals
   - Show understanding of core needs

2. **Opportunity Matrix** (visual 2x2)
   - Master visual of all projects
   - Color-coded by quadrant

3. **Roadmap Summary**
   - Translate matrix into timeline
   - Group Quick Wins into Phase 1
   - Logical sequence (Phase 1, 2, 3)

4. **Opportunity Deep Dive** (top 1-3 Quick Wins)
   - Current vs Future State diagram
   - Key metrics on time saved

5. **ROI Summary (The "Money Slide")** ⭐
   - Table: Solution | Implementation Cost | Financial Impact
   - Most powerful slide for buy-in

#### AriseGroup.ai Current System
**Presentation Outline (7-10 slides)**
1. Title slide
2. Agenda
3. Current state findings
4. Top opportunities (1 slide per)
5. Implementation roadmap
6. ROI & business case
7. Next steps

- Structured as array of slide objects:
  - `slide_number`, `title`, `purpose`, `talking_points[]`

#### Gap Analysis
✅ **SIMILAR**: Both have 7-10 slide structure covering same topics

⚠️ **MISSING**:
- **Current vs Future State diagrams** for opportunities
- **Visual Opportunity Matrix in presentation**
- **"Money Slide" table format** explicitly
- Specific slide templates/designs

✅ **ADVANTAGE**:
- Structured data format
- Talking points documented
- Purpose for each slide

💡 **OPPORTUNITY**:
- Add slide template/designs
- Generate Current vs Future State diagrams from target_state_designs
- Create Money Slide table from roadmap data

---

## Key Philosophical Differences

### Liam Ottley's Framework
- **Visual-first**: Miro/FigJam diagrams, flowcharts, matrices
- **Simplicity**: 3 engines, 4 quadrants, 5 slides
- **Consultative**: Emphasis on co-creation, validation workshops
- **Sales-focused**: "Money Slide", revenue uplift, undeniable business case
- **Quick Wins first**: Build trust before big projects
- **Manual process**: Guided by framework but human-executed

### AriseGroup.ai System
- **Data-first**: Structured JSON, machine-readable
- **Comprehensive**: 7 phases, detailed templates
- **Automated**: Claude Code skill guides workflow
- **Implementation-ready**: Handoff to build team immediately
- **Engineering-focused**: Technical architecture, data flow
- **Agent-assisted**: AI-driven process execution

---

## Critical Gaps to Address

### 🔴 HIGH PRIORITY

1. **Interview Templates**
   - Add Liam's stakeholder vs end-user interview guides
   - Include sample questions for each type
   - Document best practices (80/20 rule, recording, "why" technique)

2. **Validation Workshop Step**
   - Add explicit validation phase between opportunity identification and roadmap
   - Document co-creation workshop process
   - Include validation questions template

3. **Revenue Uplift ROI Calculation**
   - Add methodology for calculating revenue opportunity from reallocated time
   - Include in ROI calculations alongside cost savings
   - This is the most compelling business case component

4. **"Money Slide" Generator**
   - Create visual table: Solution | Cost | Direct Savings | Revenue Uplift | Total Impact
   - Make this the centerpiece of the presentation

### 🟡 MEDIUM PRIORITY

5. **Visual Outputs**
   - Generate Ops Canvas diagram from current_state_maps
   - Generate 2x2 Opportunity Matrix from ai_opportunity_matrix
   - Generate Current vs Future State diagrams from target_state_designs

6. **Opportunity Quadrant Classification**
   - Add `quadrant` field: "quick_win" | "big_swing" | "nice_to_have" | "deprioritize"
   - Use in roadmap prioritization
   - Communicate "Quick Wins first" strategy explicitly

7. **3-Engine Framework**
   - Map processes to Acquisition, Delivery, or Support engines
   - Use as high-level categorization in presentation
   - Simplifies communication with clients

### 🟢 NICE TO HAVE

8. **Per-Opportunity ROI**
   - Calculate individual solution ROI, not just aggregate
   - Show break-even for each opportunity
   - Helps prioritization decisions

9. **Pricing Strategy Documentation**
   - Document "$10K for 2 weeks" positioning
   - Include pricing tiers based on company size
   - Add value-based pricing calculator

10. **Case Study Integration**
    - Extract case studies from completed audits
    - Use in presentations ("similar client saved X")
    - Feed into content-strategy skill

---

## Integration Recommendations

### Option A: Enhance Existing audit.json Structure (RECOMMENDED)

**Add new fields to audit.json:**

```json
{
  "discovery_interviews": {
    "stakeholder_interviews": [
      {
        "interviewee_name": "",
        "role": "",
        "date": "",
        "duration_minutes": 0,
        "key_findings": [],
        "transcript_link": ""
      }
    ],
    "end_user_interviews": [
      {
        "interviewee_name": "",
        "role": "",
        "date": "",
        "duration_minutes": 0,
        "key_findings": [],
        "transcript_link": ""
      }
    ],
    "interview_summary": ""
  },

  "ops_canvas": {
    "acquisition_engine": {
      "processes": [],
      "time_sinks": [],
      "quality_risks": []
    },
    "delivery_engine": {
      "processes": [],
      "time_sinks": [],
      "quality_risks": []
    },
    "support_engine": {
      "processes": [],
      "time_sinks": [],
      "quality_risks": []
    }
  },

  "opportunity_validation": {
    "workshop_date": "",
    "attendees": [],
    "validated_opportunities": [],
    "deprioritized_opportunities": [],
    "stakeholder_feedback": [],
    "agreed_upon_priorities": []
  },

  "ai_opportunity_matrix": [
    {
      // ... existing fields ...
      "quadrant": "quick_win|big_swing|nice_to_have|deprioritize",
      "roi_calculation": {
        "direct_cost_savings": {
          "hours_saved_per_week": 0,
          "number_of_employees": 0,
          "avg_hourly_rate": 0,
          "annual_cost_savings": 0
        },
        "revenue_uplift": {
          "reallocated_hours_per_week": 0,
          "value_per_hour": 0,
          "annual_revenue_potential": 0
        },
        "total_annual_value": 0,
        "implementation_cost": 0,
        "roi_percentage": 0,
        "break_even_months": 0
      }
    }
  ],

  "money_slide": {
    "opportunities": [
      {
        "name": "",
        "implementation_cost": 0,
        "direct_savings_annual": 0,
        "revenue_uplift_annual": 0,
        "total_impact_annual": 0,
        "roi_percentage": 0
      }
    ],
    "totals": {
      "total_investment": 0,
      "total_annual_value": 0,
      "total_roi_percentage": 0
    }
  }
}
```

**Benefits**:
- Maintains existing structure
- Backward compatible
- Adds Liam's missing components
- Keeps data-first advantage

**Implementation**:
1. Update audit-template.json with new fields
2. Update comprehensive-ai-audit-agent.md with new phases
3. Add interview question templates to documentation
4. Add ROI calculator to documentation
5. Update Claude Code skill prompts

---

### Option B: Parallel "Liam Ottley Mode" Workflow

Create a simplified alternate workflow:
- `.claude/skills/liam-ottley-audit/SKILL.md`
- Focus on visual outputs (Miro diagrams)
- Manual interview process
- Simplified 3-step structure
- Outputs to slides instead of JSON

**Benefits**:
- Preserves both approaches
- Users can choose based on preference
- Easier to implement initially

**Drawbacks**:
- Maintenance burden
- Duplicate content
- Confusion about which to use

**Recommendation**: Don't do this. Integrate into existing system.

---

### Option C: Hybrid Approach (BEST)

**Maintain audit.json as source of truth + Generate visual outputs**

1. **Enhanced data collection** (audit.json with new fields from Option A)
2. **Visual generators**:
   - `generate_ops_canvas()` → Mermaid/SVG diagram
   - `generate_opportunity_matrix()` → 2x2 visual
   - `generate_current_vs_future()` → Before/after diagrams
   - `generate_money_slide()` → ROI table
3. **Interview templates** as markdown in documentation
4. **Validation workshop checklist** as process step
5. **ROI calculator** as helper function

**Implementation**:
```
03-ai-growth-engine/onboarding/
├── templates/
│   ├── audit-template.json (enhanced)
│   ├── stakeholder-interview-questions.md (NEW)
│   ├── end-user-interview-questions.md (NEW)
│   ├── validation-workshop-guide.md (NEW)
│   └── roi-calculator.md (NEW)
├── agents/
│   └── comprehensive-ai-audit-agent.md (updated with new phases)
└── documentation/
    ├── interview-best-practices.md (NEW)
    ├── opportunity-validation-process.md (NEW)
    └── roi-calculation-methodology.md (NEW)
```

**Benefits**:
- Best of both worlds
- Data-driven + visually compelling
- Maintains automation advantage
- Adds missing components

---

## Action Items

### Phase 1: Quick Wins (This Week)
- [ ] Create stakeholder-interview-questions.md template
- [ ] Create end-user-interview-questions.md template
- [ ] Document revenue uplift ROI calculation methodology
- [ ] Add validation workshop step to workflow
- [ ] Create Money Slide generator function

### Phase 2: Core Integration (Next 2 Weeks)
- [ ] Update audit-template.json with new fields (discovery_interviews, ops_canvas, opportunity_validation, roi_calculation, money_slide)
- [ ] Update comprehensive-ai-audit-agent.md with enhanced workflow
- [ ] Add "quadrant" classification to opportunities
- [ ] Create 3-engine categorization guide
- [ ] Document interview best practices

### Phase 3: Visual Outputs (Next Month)
- [ ] Build Ops Canvas diagram generator
- [ ] Build Opportunity Matrix visualizer
- [ ] Build Current vs Future State diagram generator
- [ ] Build Money Slide table generator
- [ ] Integrate with presentation_outline

### Phase 4: Polish & Refinement (Ongoing)
- [ ] Test enhanced workflow with real client
- [ ] Refine ROI calculations based on feedback
- [ ] Create case studies from completed audits
- [ ] Update pricing strategy documentation
- [ ] Build content-strategy integration

---

## Conclusion

### Summary
Liam Ottley's framework and AriseGroup.ai's system are **strongly aligned** in structure and philosophy, but Liam provides **critical tactical components** we're missing:

**Top 3 Missing Components to Integrate:**
1. **Detailed interview templates** (stakeholder vs end-user)
2. **Validation workshop process** (co-creation with client)
3. **Revenue uplift ROI calculation** (not just cost savings)

**Our Competitive Advantages to Maintain:**
1. **Structured data format** (audit.json) for automation and handoff
2. **Claude Code skill** for guided workflow
3. **Implementation-ready outputs** for build team

### Recommendation
✅ **Integrate Liam's framework into existing system** using Hybrid Approach (Option C)

This gives us:
- More rigorous discovery process
- Better client co-creation
- More compelling business case (revenue uplift)
- Visual presentation outputs
- Maintained automation and data advantages

**Expected Impact:**
- Higher audit quality and client satisfaction
- Stronger business cases → higher close rates
- More repeatable process → faster audits
- Better handoff to implementation → smoother delivery

**Next Step:** Begin Phase 1 Quick Wins implementation this week.

---

**Document Status**: ✅ Ready for Review
**Author**: Claude (Comprehensive Analysis)
**Date**: 2025-12-09
