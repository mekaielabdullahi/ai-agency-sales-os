# Phase 1: Ideation & Analysis

**Duration:** 10-30 minutes
**Tools:** BMAD Analyst agent, brainstorming workflows
**Gate:** Problem definition approved

---

## Purpose

Transform a problem statement or client request into a clear, actionable problem definition that can be specified and built.

---

## Inputs

- Problem statement or client request
- Context from discovery (if client project)
- Existing constraints or requirements

---

## Process

### Step 1: Define the Problem
- [ ] What is the actual problem being solved?
- [ ] Who experiences this problem?
- [ ] What is the impact of not solving it?
- [ ] What does success look like?

### Step 2: Research Existing Solutions
- [ ] What solutions exist in the market?
- [ ] What has been tried before?
- [ ] What worked/didn't work?
- [ ] What can we learn from existing approaches?

### Step 3: Identify Constraints
- [ ] Technical constraints (platforms, integrations, tech stack)
- [ ] Business constraints (budget, timeline, resources)
- [ ] User constraints (skill level, access, preferences)
- [ ] Regulatory/compliance constraints

### Step 4: Draft Initial Approach
- [ ] High-level solution concept
- [ ] Key components needed
- [ ] Build vs. buy decisions
- [ ] Risk assessment

---

## BMAD Agent Usage

### Analyst Agent
Use for:
- Research and solution exploration
- Technical constraint analysis
- Feasibility assessment

**Prompt Template:**
```
Analyze this problem and provide:
1. Problem breakdown
2. Existing solution landscape
3. Technical considerations
4. Recommended approach

Problem: [describe problem]
Context: [relevant context]
Constraints: [known constraints]
```

---

## Outputs

### Problem Definition Document

```markdown
# Problem Definition: [Project Name]

## Problem Statement
[Clear, concise statement of the problem]

## Target Users
[Who will use/benefit from this]

## Success Criteria
[How we'll know the problem is solved]

## Constraints
- Technical: [list]
- Business: [list]
- User: [list]

## Proposed Approach
[High-level solution concept]

## Risks
[Key risks identified]

## Decision
- [ ] Build internally
- [ ] Delegate to developer
- [ ] Use existing solution
- [ ] Needs more research
```

---

## Quality Gate: Ideation Complete

Before moving to Phase 2 (Specification):

- [ ] Problem is clearly defined
- [ ] Success criteria are measurable
- [ ] Constraints are documented
- [ ] Initial approach is viable
- [ ] Build/delegate decision made

---

## Templates

- [Problem Definition Template](./templates/problem-definition.md)
- [Research Summary Template](./templates/research-summary.md)

---

## Examples

See `/examples/` for completed ideation documents from past projects.
