# Output Validation Test Template

**Agent Being Tested**: [Agent Name]
**Agent ID**: [ID]
**Test Date**: [Date]
**Tester**: [QA Agent or Human]

---

## Test Objective

Validate that the agent produces quality outputs that meet its purpose and success criteria.

---

## Test Scenarios

### Primary Use Case Test

**Scenario**: [Describe the main use case from purpose statement]

**Test Input**:
```
[Provide specific input for this test]
```

**Expected Output Characteristics**:
- [Characteristic 1 from purpose]
- [Characteristic 2 from purpose]
- [Characteristic 3 from purpose]

**Actual Output**:
```
[Paste actual agent output]
```

**Quality Assessment**:

| Criterion | Target | Actual | Score (1-10) | Notes |
|-----------|--------|--------|--------------|-------|
| Accuracy | [Target] | [Result] | [Score] | [Comments] |
| Completeness | [Target] | [Result] | [Score] | [Comments] |
| Format Compliance | [Target] | [Result] | [Score] | [Comments] |
| Relevance | [Target] | [Result] | [Score] | [Comments] |
| Clarity | [Target] | [Result] | [Score] | [Comments] |

**Overall Quality Score**: [Average]/10

**Result**: ✓ PASS / ⚠ MARGINAL / ✗ FAIL

**Issues Identified**:
- [Issue 1]
- [Issue 2]

---

### Secondary Use Case Test 1

**Scenario**: [Describe a secondary use case]

**Test Input**:
```
[Input]
```

**Expected Output**: [Description]

**Actual Output**:
```
[Output]
```

**Quality Score**: [X]/10

**Result**: ✓ PASS / ⚠ MARGINAL / ✗ FAIL

**Notes**: [Comments]

---

### Secondary Use Case Test 2

**Scenario**: [Describe another secondary use case]

**Test Input**:
```
[Input]
```

**Expected Output**: [Description]

**Actual Output**:
```
[Output]
```

**Quality Score**: [X]/10

**Result**: ✓ PASS / ⚠ MARGINAL / ✗ FAIL

**Notes**: [Comments]

---

### Edge Case Test 1

**Scenario**: [Describe an unusual or boundary condition]

**Test Input**:
```
[Input that tests edge case]
```

**Expected Behavior**: [How should agent handle this?]

**Actual Output**:
```
[Output]
```

**Handling Quality**: [X]/10

**Result**: ✓ PASS / ⚠ MARGINAL / ✗ FAIL

**Notes**: [How well did it handle the edge case?]

---

### Edge Case Test 2

**Scenario**: [Describe another edge case]

**Test Input**:
```
[Input]
```

**Expected Behavior**: [Expected handling]

**Actual Output**:
```
[Output]
```

**Handling Quality**: [X]/10

**Result**: ✓ PASS / ⚠ MARGINAL / ✗ FAIL

**Notes**: [Comments]

---

## Consistency Testing

Run the same scenario multiple times to test consistency:

### Consistency Test: [Primary Use Case]

**Test Input** (same for all 3 runs):
```
[Input]
```

| Run | Output Quality (1-10) | Matches Format? | Notes |
|-----|----------------------|-----------------|-------|
| 1 | [Score] | ✓ / ✗ | [Comments] |
| 2 | [Score] | ✓ / ✗ | [Comments] |
| 3 | [Score] | ✓ / ✗ | [Comments] |

**Consistency Score**: [Variance assessment]
- Low variance (scores within 1 point): ✓ EXCELLENT
- Medium variance (scores within 2 points): ⚠ ACCEPTABLE
- High variance (scores differ by 3+ points): ✗ INCONSISTENT

**Result**: ✓ PASS / ⚠ MARGINAL / ✗ FAIL

---

## Success Metrics Validation

**From Purpose Statement**:

| Success Metric | Target | Test Result | Met? |
|----------------|--------|-------------|------|
| [Metric 1] | [Target value] | [Actual value] | ✓ / ✗ |
| [Metric 2] | [Target value] | [Actual value] | ✓ / ✗ |
| [Metric 3] | [Target value] | [Actual value] | ✓ / ✗ |

**Metrics Achievement Rate**: [X%] (Target: ≥85%)

---

## Summary

### Test Results Overview

**Total Scenarios Tested**: [Number]
**Passed**: [Number] ([X%])
**Marginal**: [Number] ([X%])
**Failed**: [Number] ([X%])

**Success Rate**: [X%] (Target: ≥85%)

**Average Output Quality**: [X]/10 (Target: ≥8/10)

**Consistency**: ✓ GOOD / ⚠ ACCEPTABLE / ✗ POOR

---

### Critical Issues

1. [Critical issue 1 - if any]
2. [Critical issue 2 - if any]

---

### Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

---

### Dimension Score: Output Validation

**Score**: [X]/25 points

**Breakdown**:
- Test success rate (15 pts max): [Score based on ≥85% = 15, 70-84% = 12, <70% = 8]
- Output quality (10 pts max): [Score based on avg ≥8/10 = 10, 6-7.9/10 = 7, <6/10 = 4]

**Status**: ✓ PASS (≥20/25) / ⚠ REVISE (15-19/25) / ✗ FAIL (<15/25)

---

**Output Validation Complete**
**Tested By**: [Name]
**Date**: [Date]
**Time Spent**: [Minutes]
