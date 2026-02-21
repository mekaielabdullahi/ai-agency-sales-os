# Design Quality Review Template

**Agent Being Reviewed**: [Agent Name]
**Agent ID**: [ID]
**Review Date**: [Date]
**Reviewer**: [QA Agent or Human]

---

## Review Objective

Evaluate the quality of all agent design components: Purpose, Knowledge Base, Workflow, and System Prompt.

---

## 1. Purpose Statement Quality Review

### 1A. Purpose Statement Text

**Purpose Statement**:
```
[Copy the full purpose statement here]
```

---

### 1B. Clarity Assessment

**Formula Compliance**: Does it follow [function] → [method] → [outcome] → [user] → [quality] → [constraints]?
- [ ] Function clearly stated
- [ ] Method/approach defined
- [ ] Specific outcome identified
- [ ] Target user specified
- [ ] Quality standard included
- [ ] Constraints/boundaries noted

**Formula Score**: [X]/6 components present

**Language Clarity**:
- [ ] No ambiguous terms
- [ ] Specific, not generic
- [ ] Jargon-free or jargon explained
- [ ] Concrete, actionable language

**Clarity Score**: [X]/10 (Target: ≥9/10)

---

### 1C. Completeness Assessment

| Component | Present? | Quality | Notes |
|-----------|----------|---------|-------|
| Core Objective | ✓ / ✗ | [X/10] | [Comments] |
| Capabilities List | ✓ / ✗ | [X/10] | [At least 3 specific capabilities?] |
| Boundaries (What NOT to do) | ✓ / ✗ | [X/10] | [Clear exclusions?] |
| Success Metrics | ✓ / ✗ | [X/10] | [Measurable?] |
| Use Cases | ✓ / ✗ | [X/10] | [Practical examples?] |
| Target User | ✓ / ✗ | [X/10] | [Clearly identified?] |

**Completeness Score**: [X]/10 (Target: ≥9/10)

---

### 1D. Measurability Assessment

**Success Metrics Listed**:
1. [Metric 1] - Measurable? ✓ / ✗
2. [Metric 2] - Measurable? ✓ / ✗
3. [Metric 3] - Measurable? ✓ / ✗

**Are metrics quantifiable?** (Can you objectively determine success?)
- [ ] All metrics are quantifiable
- [ ] Most metrics are quantifiable (≥2/3)
- [ ] Few metrics are quantifiable (<2/3)

**Measurability Score**: [X]/10 (Target: ≥9/10)

---

### 1E. Alignment Assessment

**Fits OS Strategy?**: ✓ / ✗
**Supports Business Goals?**: ✓ / ✗
**No Conflict with Existing Agents?**: ✓ / ✗
**Appropriate Scope?**: ✓ / ✗

**Alignment Score**: [X]/10 (Target: ≥9/10)

---

### Purpose Statement Overall Score

**Clarity**: [X]/10 (weight: 25%)
**Completeness**: [X]/10 (weight: 25%)
**Measurability**: [X]/10 (weight: 25%)
**Alignment**: [X]/10 (weight: 25%)

**Purpose Total**: [Weighted Average]/10

**Status**: ✓ PASS (≥9/10) / ⚠ REVISE (7-8.9/10) / ✗ FAIL (<7/10)

**Issues**:
- [Issue 1]
- [Issue 2]

---

## 2. Knowledge Base Quality Review

### 2A. Knowledge Domains Coverage

**Required Domains** (from purpose statement):
1. [Domain 1] - Covered? ✓ / ✗ - Quality: [X/10]
2. [Domain 2] - Covered? ✓ / ✗ - Quality: [X/10]
3. [Domain 3] - Covered? ✓ / ✗ - Quality: [X/10]
4. [Domain 4] - Covered? ✓ / ✗ - Quality: [X/10]

**Coverage Rate**: [X]% (Target: ≥90%)

---

### 2B. Template Compliance

**Standard Sections Present**:
- [ ] Quick Reference
- [ ] Core Concepts
- [ ] Decision Trees (if applicable)
- [ ] Examples & Templates
- [ ] Best Practices
- [ ] Common Pitfalls
- [ ] Edge Cases (if applicable)
- [ ] Resources & References

**Template Compliance**: [X]/8 sections present

---

### 2C. Organization Assessment

**Ease of Navigation**:
- [ ] Clear section headers
- [ ] Logical information flow
- [ ] Quick reference at top
- [ ] Cross-references where helpful
- [ ] Information layered (quick → detailed)

**Organization Score**: [X]/10 (Target: ≥9/10)

---

### 2D. Actionability Assessment

**Practical vs. Theoretical**:
- [ ] Information is actionable, not just informative
- [ ] Examples demonstrate application
- [ ] Templates are ready-to-use
- [ ] Decision trees provide clear guidance

**Contains at least 3 practical examples?**: ✓ / ✗
**Includes usable templates?**: ✓ / ✗
**Decision frameworks included?**: ✓ / ✗

**Actionability Score**: [X]/10 (Target: ≥8/10)

---

### 2E. Accuracy Assessment

**Fact-Check Sample Points**:
1. [Claim 1] - Verified? ✓ / ✗ / N/A
2. [Claim 2] - Verified? ✓ / ✗ / N/A
3. [Claim 3] - Verified? ✓ / ✗ / N/A

**Sources Cited?**: ✓ / ✗
**Information Current?**: ✓ / ✗

**Accuracy Assessment**: ✓ GOOD / ⚠ VERIFY / ✗ CONCERNS

---

### Knowledge Base Overall Score

**Completeness**: [X]% coverage (weight: 30%)
**Organization**: [X]/10 (weight: 25%)
**Actionability**: [X]/10 (weight: 25%)
**Accuracy**: ✓ / ⚠ / ✗ (weight: 20%)

**Knowledge Base Total**: [Score]/10

**Status**: ✓ PASS (≥9/10, ≥90% coverage) / ⚠ REVISE (7-8.9/10 or 75-89% coverage) / ✗ FAIL (<7/10 or <75% coverage)

**Gaps**:
- [Gap 1]
- [Gap 2]

---

## 3. Workflow Design Quality Review

### 3A. Capability Coverage

**Capabilities from Purpose** → **Workflow Steps**:

| Capability | Workflow Step(s) | Adequately Covered? |
|------------|------------------|---------------------|
| [Capability 1] | [Step X] | ✓ / ⚠ / ✗ |
| [Capability 2] | [Step Y] | ✓ / ⚠ / ✗ |
| [Capability 3] | [Step Z] | ✓ / ⚠ / ✗ |

**Coverage**: [X]% (Target: 100%)

---

### 3B. Clarity Assessment

**Step Instructions**:
- [ ] Each step has clear action
- [ ] Decision criteria are explicit
- [ ] No ambiguous instructions
- [ ] Logic is easy to follow

**Time Estimates Provided?**: ✓ / ✗
**Decision Points Clearly Marked?**: ✓ / ✗
**Output Defined for Each Step?**: ✓ / ✗

**Clarity Score**: [X]/10 (Target: ≥9/10)

---

### 3C. Completeness Assessment

**Required Workflow Components**:
- [ ] All capabilities addressed
- [ ] Logical sequencing
- [ ] Decision point criteria defined
- [ ] Error handling included
- [ ] Output structure clearly defined
- [ ] Quality checkpoints present

**Completeness Score**: [X]/10 (Target: ≥9/10)

---

### 3D. Efficiency Assessment

**Waste Check**:
- [ ] No redundant steps
- [ ] Optimal sequencing
- [ ] No obvious inefficiencies

**Time Estimates Realistic?**: ✓ / ✗
**Common Case Optimized?**: ✓ / ✗

**Efficiency Score**: [X]/10 (Target: ≥8/10)

---

### 3E. Robustness Assessment

**Error Handling**:
- [ ] Major failure modes identified
- [ ] Recovery procedures defined
- [ ] Escalation triggers clear
- [ ] Fallback defaults exist

**Error Coverage**: ✓ COMPREHENSIVE / ⚠ BASIC / ✗ INSUFFICIENT

**Robustness Score**: [X]/10 (Target: ≥8/10)

---

### Workflow Overall Score

**Capability Coverage**: [X]% (weight: 25%)
**Clarity**: [X]/10 (weight: 25%)
**Completeness**: [X]/10 (weight: 20%)
**Efficiency**: [X]/10 (weight: 15%)
**Robustness**: [X]/10 (weight: 15%)

**Workflow Total**: [Weighted Average]/10

**Status**: ✓ PASS (≥9/10, 100% coverage) / ⚠ REVISE (7-8.9/10 or 80-99% coverage) / ✗ FAIL (<7/10 or <80% coverage)

**Issues**:
- [Issue 1]
- [Issue 2]

---

## 4. System Prompt Quality Review

### 4A. Integration Assessment

**Purpose → Prompt**:
- [ ] Mission statement reflects purpose
- [ ] Capabilities from purpose encoded
- [ ] Boundaries from purpose included
- [ ] Success metrics referenced

**Knowledge → Prompt**:
- [ ] Knowledge base referenced appropriately
- [ ] Quick reference info embedded (if needed)
- [ ] Knowledge access instructions clear

**Workflow → Prompt**:
- [ ] Workflow integrated (explicit or natural)
- [ ] Decision points encoded
- [ ] Process flow clear

**Integration Score**: [X]/10 (Target: ≥9/10)

---

### 4B. Clarity Assessment

**Instructions Quality**:
- [ ] Unambiguous directions
- [ ] Direct, clear language
- [ ] Well-organized structure
- [ ] Easy to parse

**Clarity Score**: [X]/10 (Target: ≥9/10)

---

### 4C. Actionability Assessment

**Execution Readiness**:
- [ ] Agent can execute immediately
- [ ] Workflow is clear enough to follow
- [ ] Decision criteria explicit
- [ ] Output requirements defined

**Examples Included?**: ✓ / ✗ (At least 2-3?)
**Quality Validation Built In?**: ✓ / ✗

**Actionability Score**: [X]/10 (Target: ≥9/10)

---

### 4D. Completeness Assessment

**Required Sections Present**:
- [ ] Identity & Mission
- [ ] Core Capabilities (& Boundaries)
- [ ] Workflow (explicit or natural)
- [ ] Knowledge References
- [ ] Interaction Guidelines
- [ ] Output Format
- [ ] Examples
- [ ] Success Metrics

**Completeness**: [X]/8 sections

**Completeness Score**: [X]/10 (Target: ≥9/10)

---

### 4E. Effectiveness Assessment

**Will This Prompt Drive Desired Behavior?**:
- [ ] Examples anchor expected performance
- [ ] Guardrails prevent common errors
- [ ] Flexibility allows appropriate adaptation
- [ ] Personality matches function

**Effectiveness Prediction**: ✓ HIGH / ⚠ MODERATE / ✗ LOW

**Effectiveness Score**: [X]/10 (Target: ≥8/10)

---

### System Prompt Overall Score

**Integration**: [X]/10 (weight: 30%)
**Clarity**: [X]/10 (weight: 25%)
**Actionability**: [X]/10 (weight: 25%)
**Completeness**: [X]/10 (weight: 10%)
**Effectiveness**: [X]/10 (weight: 10%)

**System Prompt Total**: [Weighted Average]/10

**Status**: ✓ PASS (≥9/10) / ⚠ REVISE (7-8.9/10) / ✗ FAIL (<7/10)

**Issues**:
- [Issue 1]
- [Issue 2]

---

## Design Quality Summary

### Component Scores

| Component | Score | Weight | Weighted Score | Status |
|-----------|-------|--------|----------------|--------|
| Purpose Statement | [X]/10 | 25% | [X]/2.5 | [Status] |
| Knowledge Base | [X]/10 | 30% | [X]/3.0 | [Status] |
| Workflow Design | [X]/10 | 25% | [X]/2.5 | [Status] |
| System Prompt | [X]/10 | 20% | [X]/2.0 | [Status] |

**Design Quality Total**: [Sum of Weighted]/10

**Dimension Score: Design Quality**

**Score**: [X]/25 points

**Calculation**: (Design Quality Total / 10) × 25 = [Score]

**Status**: ✓ PASS (≥20/25) / ⚠ REVISE (15-19/25) / ✗ FAIL (<15/25)

---

## Critical Design Issues (Must Fix)

1. [Critical issue 1]
2. [Critical issue 2]

---

## Recommended Improvements

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

---

**Design Quality Review Complete**
**Reviewed By**: [Name]
**Date**: [Date]
**Time Spent**: [Minutes]
