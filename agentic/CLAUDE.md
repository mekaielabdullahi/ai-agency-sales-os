# Agentic Workspace

This workspace is part of the **AriseGroup.ai Agent Team** architecture. See the root `CLAUDE.md` for team structure, teammate definitions (`.claude/agents/`), and cross-team communication patterns.

When operating as a teammate, your modules and tools are scoped to your domain. Consult `agentic-index.yaml` to find the right module, then follow the 3-layer architecture below.

---

You operate within a 3-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

## The 3-Layer Architecture

**Layer 1: Runbooks (What to do)**
- SOPs written in Markdown, live in `modules/*/runbook/`
- Define goals, inputs, tools to use, outputs, and edge cases
- Natural language instructions, like you'd give a mid-level employee

**Layer 2: Orchestration (Decision making)**
- This is you. Your job: intelligent routing.
- Read runbooks, call tools in the right order, handle errors, ask for clarification
- You're the glue between intent and execution

**Layer 3: Tools (Doing the work)**
- Python scripts in `modules/*/tool/`
- Handle API calls, data processing, file operations
- Reliable, testable, fast. Use scripts instead of manual work.

**Why this works:** if you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. Push complexity into deterministic code. Focus on decision-making.

## Module Discovery

| What you need | Where to look |
|---------------|---------------|
| Installed modules | `agentic-index.yaml` |
| Module overview | `modules/<name>/README.md` |
| Tool implementation | `modules/<name>/tool/*.py` |
| How to use a tool | `modules/<name>/runbook/*.md` |
| Slash commands | `.claude/commands/` |

**IMPORTANT: Before working with any module, ALWAYS read:**
1. `modules/<name>/README.md` - Overview, setup, limitations
2. `modules/<name>/runbook/*.md` - Detailed procedures and edge cases

This prevents wasted effort from not understanding API limitations, authentication requirements, or known issues that are already documented.

## Running Tools

Always use the `./run` wrapper (activates venv automatically):
```bash
./run modules/<name>/tool/<script>.py <action> [args]
```

Do NOT run `python3` directly—it will fail due to missing dependencies.

## Operating Principles

**0. Identify available tools first**
Before starting ANY task, scan `agentic-index.yaml` to identify modules that may be relevant. This prevents reinventing tools that already exist.

1. Read `agentic-index.yaml` - scan module names and descriptions
2. For relevant modules, read their README.md and runbooks
3. Only then begin planning the task

This is non-negotiable. Skipping this step leads to manual work when automation exists.

**1. Read module documentation first**
Before working with ANY module, read its documentation in this order:
1. `modules/<name>/README.md` - Setup, limitations, gotchas
2. `modules/<name>/runbook/*.md` - Procedures and edge cases

This prevents wasted effort debugging issues that are already documented (e.g., API limitations, auth requirements, known bugs).

**2. Check for tools first**
Before writing a script, check if a tool already exists in the relevant module. Only create new implementations if none exist.

**3. Self-anneal when things break**
- Read error message and stack trace
- Fix the script and test it again (unless it uses paid tokens/credits—check with user first)
- Update the runbook with what you learned (API limits, timing, edge cases)
- Example: hit API rate limit → investigate API → find batch endpoint → rewrite script → test → update runbook

**4. Update runbooks as you learn**
Runbooks are living documents. When you discover API constraints, better approaches, common errors, or timing expectations—update the runbook. But don't create or overwrite runbooks without asking. Runbooks are your instruction set.

**5. Ask for format when ambiguous**
If the user's request doesn't specify the implementation approach, ASK which format they want. Do not assume.

**6. Cross-reference existing implementations**
When building something new, check if similar tools exist. Use them as reference for logic, API calls, and edge cases.

**7. Ask before creating or modifying modules**
Do not automatically create new modules or significantly revise existing ones. Always ask the user first:
- "Should I create a new module for this?"
- "Would you like me to improve/revise this existing module?"

You can iterate and improve modules, but get explicit permission before planning module creation or major changes.

## Self-Annealing Loop

Errors are learning opportunities. When something breaks:
1. Fix the tool (script)
2. Test it, make sure it works
3. Update runbook to include new flow
4. System is now stronger

## File Organization

**Deliverables vs Intermediates:**
- **Deliverables**: Google Sheets, Google Slides, or other cloud-based outputs that the user can access
- **Intermediates**: Temporary files needed during processing

**Directory structure:**
- `.tmp/` - All intermediate files (dossiers, scraped data, temp exports). Never commit, always regenerated.
- `modules/*/runbook/` - SOPs in Markdown
- `modules/*/tool/` - Python scripts
- `.env` - Environment variables and API keys
- `credentials.json`, `token.json` - Google OAuth credentials (in `.gitignore`)

**Key principle:** Local files are only for processing. Deliverables live in cloud services where the user can access them. Everything in `.tmp/` can be deleted and regenerated.

## Adding Capabilities

Check if a module exists for your task by reading `agentic-index.yaml` or browsing `modules/`.

To create a new module:
```
/agentic-new <module-name>
```

After adding or modifying modules, regenerate symlinks:
```
/agentic-sync
```

## Making Changes

When you fix bugs or improve tools:
1. Edit the source: `modules/<name>/tool/<file>.py`
2. Update the runbook: `modules/<name>/runbook/<file>.md`
3. Commit scoped to module: `git add modules/<name> && git commit -m 'fix(<name>): description'`

After adding new files to a module, run `/agentic-sync` to update symlinks and the discovery index.

## Git Workflow

**NEVER commit directly to main.** Always use feature branches:

```bash
git checkout -b feat/description    # Create feature branch
# ... make changes ...
git add <files> && git commit -m "feat(scope): description"
git checkout main && git merge feat/description --no-edit
git branch -d feat/description      # Clean up
```

Branch naming conventions:
- `feat/` - New features or modules
- `fix/` - Bug fixes
- `refactor/` - Code improvements without behavior change

## Summary

You sit between human intent (runbooks) and deterministic execution (Python scripts). Read instructions, make decisions, call tools, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.
