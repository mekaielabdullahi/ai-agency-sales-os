# 03 - Development Execution

## Overview

This module contains our Internal Development OS - a complete software development lifecycle framework combining **AutoClaude** (autonomous execution with QA loops) and **BMAD** (structured spec-driven development).

---

## The 5-Phase Development Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    INTERNAL DEVELOPMENT OS                       │
└─────────────────────────────────────────────────────────────────┘

  PHASE 1          PHASE 2          PHASE 3          PHASE 4          PHASE 5
  ─────────        ─────────        ─────────        ─────────        ─────────
  IDEATION    →    SPECIFICATION →  EXECUTION   →    VALIDATION  →   DELIVERY
  (10-30 min)      (15-45 min)      (Variable)       (15-30 min)      (10-20 min)

  Problem          PRD              AutoClaude       Testing          Merge
  Definition       Architecture     QA Loops         Metrics          Deploy
  Research         UX Specs         Parallel Dev     Validation       Handover
```

---

## Directory Structure

```
03-development-execution/
├── 00-INTERNAL-DEVELOPMENT-OS.md    # Complete framework overview
├── 01-environment-management.md      # Dev environment setup
├── 02-progress-tracking.md           # Progress tracking methods
├── 03-communication-protocol.md      # Communication standards
├── phase-1-ideation/                 # Ideation & Analysis
│   └── README.md
├── phase-2-specification/            # Planning & Specification
│   └── README.md
├── phase-3-execution/                # Autonomous Execution
│   └── README.md
├── phase-4-validation/               # Validation & Testing
│   └── README.md
└── phase-5-delivery/                 # Integration & Delivery
    └── README.md
```

---

## Quick Start

### For New Projects
1. Start with [Phase 1: Ideation](./phase-1-ideation/README.md)
2. Follow each phase sequentially
3. Pass quality gates before proceeding

### For Bug Fixes / Small Features
1. Use BMAD Quick Flow track
2. Skip to Phase 3 with minimal spec
3. Still validate and deliver properly

---

## Core Tools

| Tool | Purpose | Phase |
|------|---------|-------|
| **BMAD Analyst** | Research, problem analysis | Phase 1 |
| **BMAD PM** | PRD creation | Phase 2 |
| **BMAD Architect** | Technical design | Phase 2 |
| **BMAD UX Designer** | User experience specs | Phase 2 |
| **AutoClaude** | Autonomous coding + QA | Phase 3 |
| **BMAD Tech Writer** | Documentation | Phase 5 |

---

## Quality Gates

| Gate | Phase | Requirements |
|------|-------|--------------|
| **Ideation Complete** | 1 → 2 | Problem defined, approach selected |
| **Spec Complete** | 2 → 3 | PRD, architecture, tests defined |
| **Code Complete** | 3 → 4 | All QA loops passed, tests green |
| **Validation Complete** | 4 → 5 | All tests pass, metrics working |
| **Delivery Complete** | 5 → Done | Merged, deployed, documented |

---

## The Golden Rule

**Spec before code. Test before merge. Monitor before deliver.**

Every project goes through all phases. No shortcuts on quality gates.

---

## Related Documents

- [Framework Overview](../FRAMEWORK-OVERVIEW.md)
- [Reusable Components](../reusable-components/)
- [Templates](../templates/)
