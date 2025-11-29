# System Integration Check Template

**Agent Being Checked**: [Agent Name]
**Agent ID**: [ID]
**Check Date**: [Date]
**Reviewer**: [QA Agent or Human]

---

## Check Objective

Verify that the agent fits properly into the Claude Code OS architecture and integrates smoothly with related agents and workflows.

---

## 1. Architecture Alignment

### 1A. OS Conventions Compliance

**Naming Convention**:
- Agent ID follows pattern: `[Department]-[Number]` (e.g., HR-001)
- Agent ID: [ID] - Compliant? ✓ / ✗

**File Structure**:
- Located in correct department directory?
- Files organized per OS standards?
- All required files present (purpose, knowledge, workflow, prompt)?

| File/Directory | Expected Location | Present? | Notes |
|----------------|-------------------|----------|-------|
| Agent Prompt | `[dept]/agent-templates/prompts/` | ✓ / ✗ | [Path] |
| Knowledge Files | `[dept]/knowledge-base/` or embedded | ✓ / ✗ | [Location] |
| Workflow Docs | `[dept]/workflows/` or embedded | ✓ / ✗ | [Location] |
| Test Results | `[dept]/qa-reports/` | ✓ / ✗ | [Path] |

**File Structure Score**: ✓ COMPLIANT / ⚠ MINOR ISSUES / ✗ NON-COMPLIANT

---

### 1B. Design Patterns Compliance

**Follows OS Agent Template?**: ✓ / ✗
**Uses Standard Section Headers?**: ✓ / ✗
**Includes Required Metadata?**: ✓ / ✗
  - Agent ID
  - Version
  - Category
  - Status
  - Created date

**Metadata Complete**: [X]/5 fields present

**Design Patterns Score**: ✓ COMPLIANT / ⚠ MINOR ISSUES / ✗ NON-COMPLIANT

---

### Architecture Alignment Total

**Status**: ✓ PASS / ⚠ MINOR FIXES / ✗ FAIL

**Issues**:
- [Issue 1]
- [Issue 2]

---

## 2. Department Fit

### 2A. Categorization

**Assigned Department**: [Department Name]
**Department Number**: [Number]

**Is categorization appropriate?**
- [ ] Agent function aligns with department mission
- [ ] No better fit in another department
- [ ] Responsibilities clearly within department scope

**Categorization**: ✓ CORRECT / ⚠ QUESTIONABLE / ✗ INCORRECT

**If Questionable/Incorrect**: Recommend moving to [Department]

---

### 2B. Department Integration

**Fits Department Workflow?**: ✓ / ✗
**Complements Other Department Agents?**: ✓ / ✗
**No Redundancy with Existing Department Agents?**: ✓ / ✗

**Department Fit Score**: ✓ GOOD / ⚠ ACCEPTABLE / ✗ POOR

---

### Department Fit Total

**Status**: ✓ PASS / ⚠ REVIEW / ✗ FAIL

**Notes**:
- [Note 1]
- [Note 2]

---

## 3. Agent Relationships

### 3A. Related Agents Identification

**Agents This Agent Receives Input From**:

| Related Agent | Department | Input Type | Documented? |
|---------------|------------|------------|-------------|
| [Agent 1] | [Dept] | [Description] | ✓ / ✗ |
| [Agent 2] | [Dept] | [Description] | ✓ / ✗ |

**Total Input Relationships**: [Number]

---

**Agents This Agent Delivers Output To**:

| Related Agent | Department | Output Type | Documented? |
|---------------|------------|-------------|-------------|
| [Agent 1] | [Dept] | [Description] | ✓ / ✗ |
| [Agent 2] | [Dept] | [Description] | ✓ / ✗ |

**Total Output Relationships**: [Number]

---

**Agents This Agent Collaborates With**:

| Related Agent | Department | Collaboration Type | Documented? |
|---------------|------------|-------------------|-------------|
| [Agent 1] | [Dept] | [Description] | ✓ / ✗ |
| [Agent 2] | [Dept] | [Description] | ✓ / ✗ |

**Total Collaboration Relationships**: [Number]

---

### 3B. Relationship Documentation Quality

**All Relationships Documented?**: ✓ / ⚠ MOSTLY / ✗ NO

**Documentation Includes**:
- [ ] What information is exchanged
- [ ] In what format
- [ ] At what stage of workflow
- [ ] Why the relationship exists

**Relationship Documentation Score**: ✓ COMPLETE / ⚠ PARTIAL / ✗ MISSING

---

### 3C. Relationship Conflicts Check

**Conflicts with Existing Agents?**

| Potential Conflict | Agent(s) Affected | Type | Severity |
|-------------------|-------------------|------|----------|
| [Description] | [Agent] | [Overlap/Redundancy/Contradiction] | [High/Med/Low] |

**Conflicts Found**: [Number]

**Conflict Status**: ✓ NO CONFLICTS / ⚠ MINOR CONFLICTS / ✗ MAJOR CONFLICTS

**Resolution Needed**:
- [Resolution 1]
- [Resolution 2]

---

### Agent Relationships Total

**Status**: ✓ PASS / ⚠ DOCUMENT / ✗ RESOLVE CONFLICTS

**Actions Required**:
- [Action 1]
- [Action 2]

---

## 4. Workflow Compatibility

### 4A. OS Workflow Integration

**Workflows This Agent Participates In**:

| Workflow Name | Agent's Role | Integration Point | Works Smoothly? |
|---------------|--------------|-------------------|-----------------|
| [Workflow 1] | [Role] | [Where it fits] | ✓ / ⚠ / ✗ |
| [Workflow 2] | [Role] | [Where it fits] | ✓ / ⚠ / ✗ |

---

### 4B. Sequential Dependencies

**Agents That Must Run Before This One**:
1. [Agent 1] - Reason: [Why]
2. [Agent 2] - Reason: [Why]

**Dependencies Documented?**: ✓ / ✗

**Agents That Must Run After This One**:
1. [Agent 1] - Reason: [Why]
2. [Agent 2] - Reason: [Why]

**Dependencies Documented?**: ✓ / ✗

---

### 4C. Input/Output Format Compatibility

**Input Format**:
- Format: [Description]
- Compatible with upstream agents?: ✓ / ✗
- Documented?: ✓ / ✗

**Output Format**:
- Format: [Description]
- Compatible with downstream agents?: ✓ / ✗
- Documented?: ✓ / ✗

**Format Compatibility**: ✓ COMPATIBLE / ⚠ NEEDS ADAPTATION / ✗ INCOMPATIBLE

---

### Workflow Compatibility Total

**Status**: ✓ PASS / ⚠ DOCUMENT / ✗ INCOMPATIBLE

**Issues**:
- [Issue 1]
- [Issue 2]

---

## 5. Naming Conventions

### 5A. Agent Name

**Agent Name**: [Full Name]

**Name Check**:
- [ ] Descriptive and clear
- [ ] Follows OS naming pattern
- [ ] No conflicts with existing agents
- [ ] Appropriate length (not too long/short)

**Agent Name**: ✓ GOOD / ⚠ ACCEPTABLE / ✗ CHANGE NEEDED

---

### 5B. File Naming

**Prompt File**: [Filename]
- Follows pattern?: ✓ / ✗
- Descriptive?: ✓ / ✗

**Knowledge Files**: [Filenames]
- Follow pattern?: ✓ / ✗
- Descriptive?: ✓ / ✗

**Workflow Files**: [Filenames]
- Follow pattern?: ✓ / ✗
- Descriptive?: ✓ / ✗

**File Naming**: ✓ COMPLIANT / ⚠ MINOR ISSUES / ✗ NON-COMPLIANT

---

### 5C. Variable/Field Naming

**Internal Naming Consistency**: ✓ / ⚠ / ✗

**Naming Conventions Total**

**Status**: ✓ PASS / ⚠ MINOR FIXES / ✗ FAIL

---

## 6. File Structure

### 6A. Directory Organization

**Proper Directory Structure**:

```
[Department]/
├── agent-templates/
│   └── prompts/
│       └── [agent-prompt].md ✓ / ✗
├── knowledge-base/ (if applicable)
│   └── [knowledge-files] ✓ / ✗
├── workflows/ (if applicable)
│   └── [workflow-docs] ✓ / ✗
└── qa-reports/
    └── [qa-report].md ✓ / ✗
```

**Directory Compliance**: ✓ / ⚠ / ✗

---

### 6B. File Organization Within Agent

**Agent Documentation**:
- [ ] All components in appropriate locations
- [ ] No orphaned files
- [ ] Related files grouped logically
- [ ] Easy to find all agent components

**File Organization**: ✓ EXCELLENT / ⚠ ACCEPTABLE / ✗ POOR

---

### File Structure Total

**Status**: ✓ PASS / ⚠ REORGANIZE / ✗ FAIL

---

## Integration Check Summary

### Integration Criteria Checklist

| Criterion | Status | Weight | Points Earned |
|-----------|--------|--------|---------------|
| Architecture Alignment | ✓ / ⚠ / ✗ | 20% | [X]/5 |
| Department Fit | ✓ / ⚠ / ✗ | 15% | [X]/3.75 |
| Agent Relationships | ✓ / ⚠ / ✗ | 25% | [X]/6.25 |
| Workflow Compatibility | ✓ / ⚠ / ✗ | 25% | [X]/6.25 |
| Naming Conventions | ✓ / ⚠ / ✗ | 5% | [X]/1.25 |
| File Structure | ✓ / ⚠ / ✗ | 10% | [X]/2.5 |

**Total Integration Score**: [Sum]/25 points

---

### Scoring Guide

**✓ PASS**: Full points
**⚠ MINOR ISSUES**: 60-80% of points
**✗ FAIL**: 0-40% of points

---

### Pass/Fail Criteria

**PASS**: ≥20/25 points, no major conflicts
**REVISE**: 15-19/25 points, or has documented conflicts with resolution plan
**FAIL**: <15/25 points, or has unresolved major conflicts

---

### Dimension Score: System Integration

**Score**: [X]/25 points

**Status**: ✓ PASS / ⚠ REVISE / ✗ FAIL

---

## Critical Integration Issues (Must Fix)

1. [Critical issue 1]
2. [Critical issue 2]

---

## Integration Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

---

## Integration Conflicts & Resolutions

### Conflict 1: [Description]
**Affected Agents**: [List]
**Severity**: High / Medium / Low
**Proposed Resolution**: [Solution]
**Status**: Resolved / Pending / Escalated

### Conflict 2: [Description]
[Same structure]

---

## Integration Approval

**Integration Check**: ✓ APPROVED / ⚠ APPROVED WITH CONDITIONS / ✗ NOT APPROVED

**Conditions** (if applicable):
1. [Condition 1]
2. [Condition 2]

**Next Steps**:
- [Step 1]
- [Step 2]

---

**System Integration Check Complete**
**Checked By**: [Name]
**Date**: [Date]
**Time Spent**: [Minutes]
