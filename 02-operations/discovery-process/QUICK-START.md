# Discovery Processing - Quick Start

## After a Discovery Call, Say:

> "Process the discovery call for [CLIENT]. Generate:
> 1. Process map of current workflows
> 2. Key questions / unknowns we need answered
> 3. Opportunity matrix based on what we know"

---

## What Gets Produced

| Output | Location | Purpose |
|--------|----------|---------|
| **Process Map** | `audit/process-map.md` | Visual workflow of current state |
| **Opportunity Matrix** | `audit/opportunity-matrix.md` | Prioritized AI/automation opportunities |
| **Discovery Unknowns** | `discovery/discovery-unknowns.md` | Questions for follow-up |
| **Audit JSON** | `audit/audit.json` | Structured data for proposals |

---

## Quick Reference Paths

### Input Sources
- Meeting transcript: `meetings/[date]-discovery/transcript.md`
- Meeting summary: `meetings/[date]-discovery/summary.md`
- Fathom recording link

### Output Destinations
```
active-projects/[client]/
├── audit/
│   ├── process-map.md           # Current workflows
│   ├── opportunity-matrix.md    # Prioritized opportunities
│   └── audit.json               # Structured audit data
├── discovery/
│   ├── discovery-unknowns.md    # Questions to answer
│   └── discovery-findings.md    # What we learned
```

---

## Processing Steps (Automated)

1. **Extract Facts** - Pull only explicitly stated information from transcript
2. **Map Processes** - Document current workflows as described
3. **Identify Gaps** - Note what's missing / unclear
4. **Find Opportunities** - Categorize by impact/effort
5. **Generate Questions** - Create follow-up question list

---

## Key Agents & Tools

| Resource | Location | When to Use |
|----------|----------|-------------|
| Discovery Analysis Prompt | `project-management/discovery-meeting-analysis-prompt.md` | Initial transcript analysis |
| Business Functions Mapping | `discovery-process/agents/business-functions-mapping-agent.md` | Deep process mapping |
| Comprehensive Audit Agent | `discovery-process/agents/comprehensive-ai-audit-agent.md` | Full paid audit |
| Discovery SOP | `discovery-process/README.md` | Complete process reference |

---

## Anti-Hallucination Rules

**NEVER fabricate:**
- Dollar amounts (unless client stated)
- Time estimates (unless client stated)
- ROI projections (without baseline data)
- Percentages or counts

**ALWAYS:**
- Use `null` or "UNKNOWN" when data missing
- Add unknowns to discovery-unknowns.md
- Describe opportunities qualitatively when metrics unavailable
- Cite source for any specific claim

---

## Example Prompt

```
Process the Remus Development discovery call from 2025-12-23.

Input: meetings/2025-12-23-discovery/transcript.md

Generate:
1. Process map showing bid-to-contract workflow
2. Opportunity matrix with impact/effort scoring
3. List of unknowns we need to resolve
4. Recommended next steps

Follow anti-hallucination rules - only use facts from transcript.
```

---

*Last Updated: December 23, 2025*
