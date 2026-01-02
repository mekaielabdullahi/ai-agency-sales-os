# Phase 2: Planning & Specification

**Duration:** 15-45 minutes
**Tools:** BMAD PM, Architect, UX Designer agents
**Gate:** Complete spec package approved

---

## Purpose

Transform the problem definition into a complete, buildable specification that developers (human or AI) can execute against.

---

## Inputs

- Problem Definition Document (from Phase 1)
- Any existing documentation or context
- Stakeholder requirements

---

## Specification Package Components

### 1. Product Requirements Document (PRD)
**Owner:** PM Agent

Contents:
- User stories with acceptance criteria
- Feature breakdown
- Priority ranking (P0/P1/P2)
- Out of scope items
- Success metrics

### 2. Technical Architecture
**Owner:** Architect Agent

Contents:
- System architecture diagram
- Technology stack decisions
- Data models
- API contracts
- Integration points
- Security considerations

### 3. UX Specification (if UI)
**Owner:** UX Designer Agent

Contents:
- User flows
- Wireframes or mockups
- Component inventory
- Interaction patterns
- Accessibility requirements

### 4. Test Specification
**Owner:** Test Architect Agent

Contents:
- Test strategy
- Unit test requirements
- Integration test requirements
- E2E test scenarios
- Performance benchmarks

---

## BMAD Agent Usage

### PM Agent
```
Create a PRD for this project:

Problem: [from problem definition]
Users: [target users]
Constraints: [from problem definition]

Include:
- User stories with acceptance criteria
- Feature priority (P0/P1/P2)
- Success metrics
- Out of scope items
```

### Architect Agent
```
Design the technical architecture for:

PRD: [link or paste PRD]
Constraints: [technical constraints]

Include:
- System architecture
- Tech stack recommendations
- Data models
- API contracts
- Security approach
```

### UX Designer Agent
```
Create UX specification for:

PRD: [link or paste PRD]
User type: [target users]

Include:
- User flows
- Key screens/wireframes
- Component requirements
- Interaction patterns
```

---

## BMAD Workflow Tracks

| Complexity | Track | Time | Use When |
|------------|-------|------|----------|
| Low | Quick Flow | <5 min | Bug fixes, small features |
| Medium | BMad Method | <15 min | Products, platforms, new features |
| High | Enterprise | <30 min | Complex systems, compliance |

### Initialize BMAD
```bash
npx bmad-method@alpha install
*workflow-init
```

---

## Outputs

### Spec Package Structure
```
/specs/[project-name]/
├── PRD.md                 # Product requirements
├── ARCHITECTURE.md        # Technical design
├── UX-SPEC.md            # User experience (if UI)
├── TEST-SPEC.md          # Test strategy
├── DATA-MODELS.md        # Database schemas
├── API-CONTRACTS.md      # API definitions
└── DECISIONS.md          # Key decisions log
```

---

## Quality Gate: Specification Complete

Before moving to Phase 3 (Execution):

- [ ] PRD approved with clear acceptance criteria
- [ ] Architecture reviewed and approved
- [ ] UX flows defined (if applicable)
- [ ] Test specifications created
- [ ] All dependencies identified
- [ ] Risks documented with mitigations

---

## Templates

- [PRD Template](./templates/prd.md)
- [Architecture Template](./templates/architecture.md)
- [UX Spec Template](./templates/ux-spec.md)
- [Test Spec Template](./templates/test-spec.md)

---

## Checklist Before Execution

```markdown
## Spec Review Checklist

### PRD
- [ ] All user stories have acceptance criteria
- [ ] Priorities are clear (P0/P1/P2)
- [ ] Success metrics are measurable
- [ ] Out of scope is explicit

### Architecture
- [ ] Tech stack decisions documented with rationale
- [ ] Data models are complete
- [ ] API contracts are defined
- [ ] Security considerations addressed
- [ ] Integration points identified

### UX (if applicable)
- [ ] User flows cover all scenarios
- [ ] Wireframes/mockups reviewed
- [ ] Edge cases handled
- [ ] Error states defined

### Testing
- [ ] Test strategy is clear
- [ ] Critical paths identified for E2E
- [ ] Performance benchmarks set
- [ ] Test data requirements known
```
