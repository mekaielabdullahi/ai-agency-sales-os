# Self-Discovery Audit Command

## Command
`/self-discovery-audit [scope]`

## Scope Options
- `full` - Complete audit of both workspaces (default)
- `quick` - Priority 1 directories only
- `development` - ai-agency-development-os only
- `sales` - ai-agency-sales-os only
- `projects` - Active projects only
- `opportunities` - Focus on automation opportunities

## Execution Flow

### Phase 1: Setup (1 min)
```
1. Create timestamped audit folder: logs/audit-runs/YYYY-MM-DD/
2. Load crawl-config.yaml
3. Load classification-schema.yaml
4. Check for previous audit (for comparison)
```

### Phase 2: Crawl (5-15 min depending on scope)
```
1. Execute Crawler Agent on specified directories
2. Output raw index to outputs/index/
3. Track progress: "Crawled X of Y files..."
4. Generate crawl statistics
```

### Phase 3: Analyze (3-5 min)
```
1. Execute Analyzer Agent on crawled index
2. Run all 5 analysis modules
3. Score automation opportunities
4. Compare to previous audit (if exists)
```

### Phase 4: Synthesize (2-3 min)
```
1. Execute Synthesizer Agent
2. Generate all 4 outputs:
   - Business Process Map
   - Opportunity Matrix
   - Pattern Library
   - Executive Summary
3. Save to outputs/
```

### Phase 5: Report (immediate)
```
1. Display Executive Summary
2. Highlight top 3 opportunities
3. List critical gaps
4. Provide links to full outputs
5. Archive audit log
```

---

## Sample Execution

```
User: /self-discovery-audit quick

Claude: Starting quick self-discovery audit...

📂 Scope: Priority 1 directories (core operations)
📅 Date: 2025-12-30
📊 Previous audit: 2025-12-23

Phase 1: Setup ✓
Phase 2: Crawling...
  - ai-agency-development-os: 45 files
  - ai-agency-sales-os: 32 files
  - Total: 77 files indexed ✓

Phase 3: Analyzing...
  - Processes discovered: 12
  - Gaps identified: 8
  - Opportunities scored: 15 ✓

Phase 4: Synthesizing...
  - Business Process Map: Updated ✓
  - Opportunity Matrix: Updated ✓
  - Pattern Library: 3 new patterns ✓
  - Executive Summary: Generated ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 EXECUTIVE SUMMARY

Key Findings:
• 12 core processes documented (up from 10)
• 3 high-priority automation opportunities identified
• 2 critical gaps need attention

Top Opportunities:
1. Meeting Summary Extraction (Score: 82) - 12 hrs/month saved
2. Daily Plan Generation (Score: 78) - 8 hrs/month saved
3. Project Status Aggregation (Score: 75) - 6 hrs/month saved

Critical Gaps:
⚠️ Client offboarding process undocumented
⚠️ Developer evaluation rubric incomplete

Changes Since Last Audit:
• +2 new processes documented
• -1 gap resolved (proposal template)
• +3 new automation opportunities

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Full outputs saved to:
• outputs/business-process-map.md
• outputs/opportunity-matrix.md
• outputs/pattern-library.md
• outputs/executive-summary.md

Audit log: logs/audit-runs/2025-12-30/audit-log.md
```

---

## Output File Locations

```
self-discovery-agent/
├── outputs/
│   ├── business-process-map.md      # Updated each audit
│   ├── opportunity-matrix.md         # Updated each audit
│   ├── pattern-library.md            # Cumulative
│   └── executive-summary.md          # Latest audit only
│
├── logs/audit-runs/
│   └── YYYY-MM-DD/
│       ├── audit-log.md              # Full execution log
│       ├── raw-index.yaml            # Crawled data
│       ├── analysis-results.yaml     # Analysis outputs
│       └── comparison.md             # Diff from previous
```

---

## Scheduling Recommendations

| Frequency | Scope | Purpose |
|-----------|-------|---------|
| Weekly | quick | Track active work |
| Monthly | full | Comprehensive review |
| Quarterly | full + deep analysis | Strategic planning |
| Ad-hoc | opportunities | Before planning sprints |

---

## Integration with Other Commands

### Feed into Daily Assessment
```
/daily-assessment
→ Pulls latest opportunity matrix
→ Suggests which automation to work on today
```

### Feed into Weekly Review
```
/weekly-review
→ Includes audit findings summary
→ Tracks gaps closed this week
```

### Feed into Project Status
```
/project-status
→ Enhanced with process compliance check
→ Flags projects missing standard docs
```
