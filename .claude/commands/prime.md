# /prime — Load Context & Orient

Read all context files and orient yourself for this session.

## Instructions

1. Read the following files in order:
   - `context/personal-info.md`
   - `context/business-info.md`
   - `context/strategy.md`
   - `context/current-data.md`
   - `context/key-metrics.md` — Current business metrics (auto-generated from database)
   - `HISTORY.md` — Workspace changelog (what was built, when, by whom)
   - `docs/_index.md` — Documentation routing index (agents find relevant docs here)

2. After reading, produce a brief **Session Orientation** summary:

   **Who:** [Name, role, one-liner]
   **Business:** [Company, what it does, stage]
   **Current Focus:** [Top 2-3 priorities from strategy.md]
   **Key Numbers:** [2-3 critical metrics from current-data.md and key-metrics.md]
   **Data Status:** [Review key-metrics.md freshness. Flag anything stale (>2 days old). Note you can run live SQL queries against `data/data.db`.]
   **What to Watch:** [Any blockers, open questions, or things in motion]

3. End with: "Context loaded. What are we working on?"

## On-Demand Loading

These files are NOT read during /prime — load them when a task requires deep detail:
- `reference/data-access.md` — Full table schemas, SQL query examples, collection scripts
- `ai-docs/README.md` — **AI Landscape Reference** — Living documentation of the best AI models across 10 categories (text, code, vision, image gen, image edit, search, video gen, image-to-video, TTS, STT). Updated daily by automated scanner. When building anything that uses AI models, or when you need to know the current best model for any category — load this first, then drill into `ai-docs/{category}/state-of-the-art.md` for full rankings, pricing, integration code, and tips.

## Rules

- Keep the summary to 8-12 lines max — this is orientation, not a report
- If any context file is missing or empty, flag it clearly
- Do NOT skip any file — partial context leads to bad advice
- If context/import/ has new unprocessed files, mention it: "I see new files in import/ — want me to review them?"
- For deeper data analysis beyond key-metrics.md, load `reference/data-access.md` and query `data/data.db` directly via Python sqlite3
