# Phase 3: Autonomous Execution

**Duration:** Variable (depends on project size)
**Tools:** AutoClaude, Developer agents
**Gate:** All QA loops passed, code complete

---

## Purpose

Execute the specification using autonomous AI agents with self-validating QA loops, producing working code in isolated branches.

---

## Inputs

- Complete spec package (from Phase 2)
- Repository with main branch
- Development environment configured

---

## AutoClaude Core Concepts

### Self-Validating QA Loop
1. Agent completes coding task
2. QA Reviewer checks against acceptance criteria
3. QA Fixer addresses issues automatically
4. Loop runs up to 50 iterations until validation passes

### Parallel Execution
- Up to 12 concurrent agent terminals
- Isolated git worktrees per task
- No cross-contamination of changes

### Task Sharding
Break specs into implementable tasks:
- Each task = one feature/component
- Clear acceptance criteria per task
- Independent, parallelizable when possible

---

## Process

### Step 1: Prepare Repository
```bash
# Ensure clean main branch
git checkout main
git pull origin main

# Create worktree for AutoClaude
git worktree add ../project-autoclaude -b autoclaude/main
```

### Step 2: Create Task Specs
Convert PRD into numbered spec files:

```
/specs/
├── 001-user-authentication.md
├── 002-dashboard-ui.md
├── 003-api-endpoints.md
└── 004-database-models.md
```

**Spec File Format:**
```markdown
# Spec 001: User Authentication

## Objective
[What this task accomplishes]

## Acceptance Criteria
- [ ] Users can register with email/password
- [ ] Users can login and receive JWT
- [ ] Invalid credentials return proper errors
- [ ] Tokens expire after 24 hours

## Technical Requirements
- Use bcrypt for password hashing
- JWT with RS256 signing
- Refresh token rotation

## Files to Create/Modify
- src/auth/controller.ts
- src/auth/service.ts
- src/auth/middleware.ts

## Tests Required
- Unit tests for auth service
- Integration tests for auth endpoints
```

### Step 3: Execute with AutoClaude
```bash
# Run spec
python run.py --spec 001

# Monitor progress (QA loop iterations)
# Agent will self-correct up to 50 times

# Review completed work
python run.py --spec 001 --review

# When approved, prepare for merge
python run.py --spec 001 --merge
```

### Step 4: Monitor QA Loops
Watch for:
- Iteration count (high count = complex issue)
- Repeated failures (may need spec clarification)
- Test failures (check test setup)

---

## Parallel Execution Strategy

### When to Parallelize
- Independent features with no shared code
- Different layers (frontend/backend)
- Separate services in microservices

### When to Serialize
- Shared dependencies
- Database migrations
- Core infrastructure code

### Example Parallel Setup
```bash
# Terminal 1: Backend auth
python run.py --spec 001

# Terminal 2: Frontend auth UI
python run.py --spec 002

# Terminal 3: Database models
python run.py --spec 003
```

---

## Git Worktree Management

### Create Isolated Worktrees
```bash
# Main execution worktree
git worktree add ../project-spec-001 -b feature/spec-001

# Additional parallel worktrees
git worktree add ../project-spec-002 -b feature/spec-002
git worktree add ../project-spec-003 -b feature/spec-003
```

### Clean Up After Merge
```bash
git worktree remove ../project-spec-001
git branch -d feature/spec-001
```

---

## Handling QA Loop Failures

### If loop exceeds 20 iterations:
1. Pause execution
2. Review the failure pattern
3. Check if spec is clear enough
4. Consider breaking into smaller tasks

### If loop reaches 50 iterations:
1. Stop execution
2. Manual review required
3. Clarify spec or simplify task
4. Restart with updated spec

---

## Outputs

- Feature branches with working code
- Passing tests per spec
- Updated documentation (if applicable)
- Commit history with clear messages

---

## Quality Gate: Execution Complete

Before moving to Phase 4 (Validation):

- [ ] All spec tasks completed
- [ ] All QA loops passed
- [ ] No failing tests in any branch
- [ ] Code follows project conventions
- [ ] No linting errors
- [ ] All acceptance criteria met

---

## AutoClaude Configuration

### Environment Setup
```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code
claude setup-token

# Configure AutoClaude
export CLAUDE_CODE_OAUTH_TOKEN=<token>
export AUTO_BUILD_MODEL=claude-3-5-sonnet
```

### Optional: Cross-Session Memory
```env
GRAPHITI_ENABLED=true
```
Enables:
- Pattern storage across sessions
- Codebase structure retention
- Improved context for subsequent builds

---

## Templates

- [Spec File Template](./templates/spec-template.md)
- [Task Breakdown Template](./templates/task-breakdown.md)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| QA loop stuck | Check acceptance criteria clarity |
| Tests failing | Verify test environment setup |
| Merge conflicts | Use AI-assisted resolution |
| Slow execution | Check model selection (sonnet vs opus) |
| Memory issues | Reduce parallel agents |
