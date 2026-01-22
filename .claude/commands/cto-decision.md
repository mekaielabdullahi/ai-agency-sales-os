# CTO Decision Command

Log an Architecture Decision Record (ADR) to the CTO Hub.

## Purpose

Capture important technical and architectural decisions with context, rationale, and consequences. Creates a searchable history of why things were built the way they are.

## Usage
```
/cto-decision [topic]
```

## Examples
```
/cto-decision use Notion as primary database
/cto-decision TypeScript for onboarding agents
/cto-decision 3-layer agentic architecture
```

## What This Command Does

### Step 1: Gather Context

I'll ask you:
1. **What decision are we making?** (brief statement)
2. **What's the context?** (why is this decision needed now?)
3. **What alternatives did you consider?**
4. **What are the trade-offs?**

### Step 2: Generate ADR

Create a new ADR file in `cto-hub/decisions/`:
```
ADR-XXX-[topic-slug].md
```

Following the standard ADR format:
- Status (Proposed/Accepted)
- Date
- Context
- Decision
- Consequences (Positive/Negative/Neutral)
- Alternatives Considered
- Related links

### Step 3: Update Index

Add entry to `cto-hub/decisions/INDEX.md` (created if doesn't exist)

### Step 4: Log

Note in session log that decision was recorded.

## ADR Numbering

ADRs are numbered sequentially:
- ADR-001, ADR-002, etc.
- Numbers are never reused
- Superseded ADRs keep their number but status changes

## When to Use This

Record a decision when:
- Choosing between multiple technical approaches
- Adopting a new technology or pattern
- Changing system architecture
- Establishing a standard or convention
- Making a trade-off (speed vs quality, etc.)

## Quick Capture Mode

If you just want to log quickly without the full process:

```
/cto-decision --quick "Using Pollinations API for image generation because it's free and fast"
```

Creates a minimal ADR with just the decision statement, marked for expansion later.

## Related

- `/cto-sync` - Reviews all ADRs during sync
- `/cto-debt` - For technical debt, not decisions
- `cto-hub/decisions/ADR-000-template.md` - Full template
