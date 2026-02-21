# Content Opportunity Engine - Epics & User Stories

**Project:** Content Opportunity Engine
**PRD Reference:** `content-opportunity-engine-prd.md`
**Created:** January 18, 2026
**Status:** Ready for Development

---

## Epic Overview

| Epic | Name | Priority | Stories | Est. Points |
|------|------|----------|---------|-------------|
| E1 | Trend Scraper Module | P0 | 5 | 13 |
| E2 | Context Extractor Module | P0 | 4 | 8 |
| E3 | Opportunity Matcher Module | P0 | 5 | 13 |
| E4 | Suggestion Generator Module | P0 | 4 | 8 |
| E5 | Storage & Delivery Integration | P1 | 6 | 13 |
| **Total** | | | **24** | **55** |

---

# Epic 1: Trend Scraper Module

**Goal:** Scrape trending AI/automation content from external sources daily

**Success Criteria:**
- Scrapes 50+ relevant items daily from 4 sources
- >90% scraping success rate
- Raw data stored in structured JSON format
- Configurable keywords and sources

---

## E1-S1: LinkedIn Trend Scraping

**As a** content creator
**I want** trending LinkedIn posts about AI/automation scraped automatically
**So that** I can see what thought leaders are posting without manual browsing

**Priority:** P0 | **Points:** 3

### Acceptance Criteria
- [ ] Uses Apify `apify/linkedin-scraper` actor
- [ ] Scrapes posts matching configurable keywords:
  - "AI agency", "AI transformation", "business automation"
  - "AI implementation", "AI consulting", "building in public AI"
- [ ] Captures for each post: text, author, URL, likes, comments, timestamp
- [ ] Stores results in `.tmp/trends_linkedin_{date}.json`
- [ ] Handles rate limiting gracefully (min 2s delay between requests)
- [ ] Returns 25-50 posts per run

### Technical Notes
- Reference: `agentic/modules/leads/tool/scrape_leads.py` for Apify patterns
- Requires: `APIFY_TOKEN` environment variable

---

## E1-S2: Reddit Trend Scraping

**As a** content creator
**I want** trending Reddit posts from AI-related subreddits scraped
**So that** I can discover discussions and pain points in my target audience

**Priority:** P0 | **Points:** 3

### Acceptance Criteria
- [ ] Uses Apify `trudax/reddit-scraper` actor
- [ ] Scrapes from target subreddits:
  - r/ChatGPT, r/LocalLLaMA, r/artificial
  - r/smallbusiness, r/Entrepreneur, r/SaaS
- [ ] Filters posts containing AI/automation keywords
- [ ] Captures: title, body, author, URL, upvotes, comments, timestamp
- [ ] Stores results in `.tmp/trends_reddit_{date}.json`
- [ ] Returns 50-100 relevant posts per run

### Technical Notes
- Filter by keywords: "ai", "automation", "chatgpt", "claude", "llm", "gpt"

---

## E1-S3: Twitter/X Trend Scraping

**As a** content creator
**I want** tweets from AI influencers and trending hashtags scraped
**So that** I can see real-time conversations in the AI space

**Priority:** P1 | **Points:** 3

### Acceptance Criteria
- [ ] Uses Apify `apidojo/tweet-scraper` actor
- [ ] Scrapes from configurable account list (AI influencers)
- [ ] Scrapes posts with hashtags: #AIAgency, #Automation, #BuildInPublic
- [ ] Captures: text, author, URL, likes, retweets, timestamp
- [ ] Stores results in `.tmp/trends_twitter_{date}.json`
- [ ] Returns 25-50 tweets per run

### Technical Notes
- May require Twitter API credentials depending on Apify actor

---

## E1-S4: Hacker News Trend Scraping

**As a** content creator
**I want** AI-related Hacker News discussions scraped
**So that** I can capture technical community perspectives

**Priority:** P1 | **Points:** 2

### Acceptance Criteria
- [ ] Uses Apify `drobnikj/hackernews-scraper` actor
- [ ] Filters for AI/automation/LLM related posts
- [ ] Captures: title, URL, points, comments count, timestamp
- [ ] Stores results in `.tmp/trends_hn_{date}.json`
- [ ] Returns 20-30 relevant posts per run

---

## E1-S5: Unified Scraper CLI

**As a** developer
**I want** a single CLI command to run all scrapers
**So that** I can trigger scraping manually or via n8n

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] `scrape_trends.py` accepts source argument: `linkedin`, `reddit`, `twitter`, `hn`, `all`
- [ ] `--days N` flag to set lookback period (default: 2)
- [ ] Outputs summary: "Scraped X items from Y sources"
- [ ] Returns exit code 0 on success, 1 on failure
- [ ] Handles partial failures gracefully (continue with other sources)

### Example Usage
```bash
python scrape_trends.py all --days 2
python scrape_trends.py linkedin
python scrape_trends.py reddit --days 7
```

---

# Epic 2: Context Extractor Module

**Goal:** Extract current work context from the operating system files

**Success Criteria:**
- Reads all P0 status files from active projects
- Parses weekly reports for recent wins
- Outputs structured JSON with work context
- Runs in <5 seconds

---

## E2-S1: P0 Status File Extraction

**As a** content system
**I want** current client work extracted from P0-ACTIVE-NOW files
**So that** content suggestions can reference real projects

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Reads all `active-projects/*/status/P0-ACTIVE-NOW.md` files
- [ ] Extracts for each project:
  - Project name (from directory name)
  - Current focus/deliverables (from file content)
  - Client name (parsed from content)
- [ ] Returns structured list of active projects
- [ ] Handles missing files gracefully

### Technical Notes
- Path: `claude-code-os-implementation/02-operations/project-management/active-projects/`

---

## E2-S2: Weekly Report Extraction

**As a** content system
**I want** recent wins and progress extracted from weekly reports
**So that** suggestions can highlight achievements

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Reads most recent `weekly-report-*.md` file
- [ ] Extracts:
  - Deliverables completed
  - Client milestones
  - Technologies mentioned
- [ ] Returns structured summary of recent progress
- [ ] Falls back gracefully if no reports exist

### Technical Notes
- Path: `claude-code-os-implementation/02-operations/weekly-reports/`

---

## E2-S3: Project README Extraction

**As a** content system
**I want** client context extracted from project READMEs
**So that** suggestions understand industry and use case

**Priority:** P1 | **Points:** 2

### Acceptance Criteria
- [ ] Reads `active-projects/*/README.md` files
- [ ] Extracts:
  - Client industry
  - Problem being solved
  - Technologies/integrations used
- [ ] Returns structured context per project
- [ ] Handles varied README formats

---

## E2-S4: Context Aggregator CLI

**As a** developer
**I want** a single command to extract all work context
**So that** I can pipe it to the matcher

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] `extract_context.py` outputs JSON to stdout
- [ ] Includes: active_clients, current_deliverables, recent_wins, technologies, industries
- [ ] Runs in <5 seconds
- [ ] Returns exit code 0 on success

### Output Schema
```json
{
  "extracted_at": "2026-01-18T10:00:00",
  "active_clients": ["Plotter Mechanix", "Wolf Sheds"],
  "current_deliverables": ["Quo migration", "Website rebuild"],
  "recent_wins": ["Voice-to-ticket demo complete"],
  "technologies": ["Quo", "Jobber", "n8n", "Claude"],
  "industries": ["printer service", "shed dealership"],
  "content_themes": ["Build-in-Public", "AI Adoption"]
}
```

---

# Epic 3: Opportunity Matcher Module

**Goal:** Score and match scraped trends against work context

**Success Criteria:**
- Calculates relevance score (0-100) for each item
- Finds specific work connections using Claude API
- Filters out low-relevance items (<50)
- Identifies best content angle for each match

---

## E3-S1: Keyword Matching (Fast Path)

**As a** content system
**I want** quick keyword-based relevance scoring
**So that** obvious matches are identified without API calls

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Scores topic alignment (40% weight) based on keyword presence
- [ ] Keyword categories:
  - Primary: "AI agency", "AI transformation", "automation"
  - Pain points: "AI overwhelm", "AI ROI", "AI failed"
  - Audience: "small business", "founder", "operations"
- [ ] Returns partial score (0-40) for topic alignment
- [ ] Runs without API calls (pure Python)

### Scoring Logic
```python
def score_topic_alignment(text: str) -> int:
    # Returns 0-40 based on keyword matches
    primary_match = sum(1 for kw in PRIMARY_KEYWORDS if kw in text.lower())
    pain_match = sum(1 for kw in PAIN_KEYWORDS if kw in text.lower())
    # Weighted scoring...
```

---

## E3-S2: Claude Connection Finder

**As a** content system
**I want** Claude to find non-obvious connections between trends and work
**So that** suggestions surface unique angles

**Priority:** P0 | **Points:** 5

### Acceptance Criteria
- [ ] Calls Claude API with trend + work context
- [ ] Prompt asks for:
  - Connection point (how this relates to our work)
  - Suggested angle (unique perspective we can offer)
  - Confidence score (how strong is the connection)
- [ ] Returns structured connection data
- [ ] Handles API errors gracefully
- [ ] Caches similar queries to reduce costs

### Prompt Template
```
Given this trending topic: "{scraped_text}"

And our current work context:
- Active projects: {projects}
- Recent wins: {wins}
- Technologies: {tech}
- Industries: {industries}

Find 1-2 angles where this topic connects to our real work.
For each angle, provide:
1. Connection point (specific project/technology/win)
2. Unique perspective we can offer
3. Confidence (high/medium/low)

Return as JSON.
```

---

## E3-S3: Relevance Score Calculator

**As a** content system
**I want** a combined relevance score for each opportunity
**So that** I can rank and filter suggestions

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Combines scores with weights:
  - Topic Alignment: 40%
  - Work Connection: 30%
  - Audience Fit: 20%
  - Timeliness: 10%
- [ ] Returns final score 0-100
- [ ] Includes score breakdown for transparency
- [ ] Threshold filtering: only pass items ≥50

### Score Structure
```json
{
  "total_score": 78,
  "breakdown": {
    "topic_alignment": 35,
    "work_connection": 25,
    "audience_fit": 12,
    "timeliness": 6
  }
}
```

---

## E3-S4: Audience Fit Scoring

**As a** content system
**I want** audience relevance assessed for each trend
**So that** we prioritize content for founders/small business owners

**Priority:** P1 | **Points:** 2

### Acceptance Criteria
- [ ] Checks if content relevant to target audience:
  - Founders / business owners
  - Small business (20-500 employees)
  - Service businesses
  - Non-technical decision makers
- [ ] Returns score 0-20 based on audience fit
- [ ] Flags enterprise-only or developer-only content as lower priority

---

## E3-S5: Matcher CLI

**As a** developer
**I want** a CLI to run matching on scraped trends
**So that** I can test and debug the matching logic

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] `match_opportunities.py` accepts trends JSON + context JSON
- [ ] Outputs matched opportunities with scores
- [ ] `--threshold N` flag to set minimum score (default: 50)
- [ ] `--limit N` flag to cap output count (default: 20)
- [ ] Outputs JSON to stdout

### Example Usage
```bash
python match_opportunities.py \
  --trends .tmp/trends_all_2026-01-18.json \
  --context .tmp/context_2026-01-18.json \
  --threshold 60 \
  --limit 10
```

---

# Epic 4: Suggestion Generator Module

**Goal:** Transform matched opportunities into actionable content suggestions

**Success Criteria:**
- Maps each opportunity to best LinkedIn framework
- Generates 3 hook options using 10 formulas
- Assigns appropriate content pillar
- Outputs structured markdown per suggestion

---

## E4-S1: Framework Selector

**As a** content creator
**I want** each suggestion mapped to the best LinkedIn framework
**So that** I know what post structure to use

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Analyzes opportunity type and maps to framework:
  - Educational/how-to → Problem-Solution-Value (PSV)
  - Tips/lists → Listicle
  - Personal experience → Story Arc
  - Challenging norms → Contrarian
  - Quick actionable → Quick Win
  - Discussion starter → Question Hook
  - Data-driven → Data/Statistics Hook
- [ ] Returns recommended framework with reasoning
- [ ] Falls back to PSV if uncertain

### Framework Reference
- Path: `04-content-team/content-templates/social/linkedin-post-frameworks.md`

---

## E4-S2: Hook Generator

**As a** content creator
**I want** 3 hook options generated for each suggestion
**So that** I can choose the best opening line

**Priority:** P0 | **Points:** 3

### Acceptance Criteria
- [ ] Uses 10 hook formulas from Hook Specialist:
  - Curiosity Gap, Big Promise, Pattern Interrupt
  - Authority Statement, Problem Agitation, Contrarian View
  - Transformation Story, Question Hook, Specific Data, Direct Benefit
- [ ] Generates 3 diverse hooks (different formulas)
- [ ] Hooks reference specific work when possible
- [ ] Each hook is <150 characters for LinkedIn impact

### Hook Reference
- Path: `04-content-team/agents/prompts/hook-specialist-agent.md`

---

## E4-S3: Content Pillar Assigner

**As a** content creator
**I want** each suggestion tagged with a content pillar
**So that** I can balance my content mix

**Priority:** P0 | **Points:** 1

### Acceptance Criteria
- [ ] Assigns one of 4 pillars:
  - Build-in-Public (40%): Our journey, systems, real results
  - AI Insights (30%): Frameworks, ROI, common mistakes
  - Productivity (20%): Operational frameworks
  - Case Studies (10%): Client transformations
- [ ] Tags based on opportunity type and work connection
- [ ] Tracks pillar distribution for balance reporting

---

## E4-S4: Suggestion Formatter

**As a** developer
**I want** suggestions output in structured markdown
**So that** they can be stored in Notion and displayed consistently

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Outputs per suggestion:
  - Title
  - Relevance score
  - Source + URL
  - Work connection
  - Recommended framework
  - Content pillar
  - 3 hook options
  - Body direction (2-3 sentences)
- [ ] Markdown format for Notion compatibility
- [ ] JSON format for programmatic use

### Output Template
```markdown
## Content Opportunity: {title}

**Relevance:** {score}/100 | **Source:** {source}
**Work Connection:** {connection}

### Suggested Approach
**Framework:** {framework}
**Pillar:** {pillar}

**Hook Options:**
1. {hook_1}
2. {hook_2}
3. {hook_3}

**Direction:** {body_direction}

---
**Source URL:** {url}
**Generated:** {timestamp}
```

---

# Epic 5: Storage & Delivery Integration

**Goal:** Store suggestions in Notion and deliver via Slack/skill

**Success Criteria:**
- Notion database created with full schema
- Daily n8n workflow running at 6 AM
- Slack notifications for high-scoring ideas
- `/content-ideate` skill for on-demand generation

---

## E5-S1: Notion Database Setup

**As a** content creator
**I want** a Content Ideas database in Notion
**So that** I can track ideas through their lifecycle

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Database created with properties:
  - Title (title)
  - Status (select: Pending, In Progress, Published, Rejected)
  - Relevance Score (number)
  - Source (select: LinkedIn, Reddit, Twitter, HN, Manual)
  - Source URL (url)
  - Content Pillar (select: Build-in-Public, AI Insights, Productivity, Case Studies)
  - Framework (select: PSV, Listicle, Story Arc, Contrarian, Quick Win, Question, Data)
  - Work Connection (multi-select: project names)
  - Draft Hooks (rich_text)
  - Body Direction (rich_text)
  - Generated Date (date)
  - Published Date (date)
  - Published URL (url)
- [ ] Database linked from Sales Hub or Content workspace

---

## E5-S2: Notion Storage Integration

**As a** content system
**I want** suggestions automatically written to Notion
**So that** they're ready for weekly planning

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Uses existing `modules/notion/tool/notion_api.py`
- [ ] Creates page in Content Ideas database per suggestion
- [ ] Maps all fields correctly
- [ ] Handles duplicates (skip if URL already exists)
- [ ] Returns Notion page URL for reference

---

## E5-S3: n8n Scheduled Workflow

**As a** content creator
**I want** the engine to run automatically every morning
**So that** fresh ideas are waiting when I start my day

**Priority:** P0 | **Points:** 3

### Acceptance Criteria
- [ ] n8n workflow triggers at 6 AM daily
- [ ] Executes full pipeline:
  1. Scrape trends (all sources)
  2. Extract context
  3. Match opportunities
  4. Generate suggestions
  5. Store in Notion
  6. Send Slack notification
- [ ] Workflow exported to `agentic/extras/n8n-wf/content_trend_scraper.json`
- [ ] Error handling with Slack alert on failure

---

## E5-S4: Slack Notification

**As a** content creator
**I want** top ideas posted to Slack daily
**So that** I see high-value opportunities immediately

**Priority:** P1 | **Points:** 2

### Acceptance Criteria
- [ ] Posts to #content channel (or configurable channel)
- [ ] Shows top 3 ideas (score ≥80)
- [ ] Message includes: title, score, work connection, Notion link
- [ ] Uses existing Slack module
- [ ] Falls back gracefully if <3 high-scoring ideas

### Message Format
```
🎯 *Content Opportunities* (Jan 18)

1. *AI agencies are charging $10K for ChatGPT wrappers* (Score: 92)
   → Connects to: Plotter Mechanix voice-to-ticket
   [View in Notion](url)

2. *"We replaced 3 tools with one n8n workflow"* (Score: 85)
   → Connects to: Internal automation stack
   [View in Notion](url)

3. *Small business owners are overwhelmed by AI options* (Score: 81)
   → Connects to: Build-in-public positioning
   [View in Notion](url)
```

---

## E5-S5: /content-ideate Skill

**As a** content creator
**I want** an on-demand skill to generate ideas
**So that** I can run the engine anytime, not just on schedule

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] Skill file at `.claude/skills/content-ideation/SKILL.md`
- [ ] Triggered by `/content-ideate` command
- [ ] Accepts optional arguments:
  - `--sources linkedin,reddit` (filter sources)
  - `--threshold 70` (minimum score)
  - `--limit 5` (max suggestions)
- [ ] Returns formatted suggestions in conversation
- [ ] Optionally stores to Notion with `--save` flag

### Skill Definition
```markdown
---
name: content-ideate
description: Generate content ideas from trending topics matched to current work
---

# Content Ideation Skill

Run the Content Opportunity Engine on-demand...
```

---

## E5-S6: Module Registration

**As a** developer
**I want** the module properly registered in the agentic system
**So that** it follows established patterns

**Priority:** P0 | **Points:** 2

### Acceptance Criteria
- [ ] `agentic-module.yaml` created with:
  - name: content-ideation
  - version: 1.0.0
  - type: bundled
  - files: tools, runbooks, commands
  - python_requires: apify-client, anthropic
  - env_vars: APIFY_TOKEN, ANTHROPIC_API_KEY, NOTION_API_KEY
- [ ] Module registered in `agentic-index.yaml`
- [ ] README.md with usage instructions
- [ ] Runbook documenting full workflow

---

# Story Status Tracking

## Sprint 1 (MVP)

| Story | Status | Assignee | Notes |
|-------|--------|----------|-------|
| E1-S1 | Pending | - | LinkedIn scraping |
| E1-S2 | Pending | - | Reddit scraping |
| E1-S5 | Pending | - | Unified CLI |
| E2-S1 | Pending | - | P0 file extraction |
| E2-S4 | Pending | - | Context CLI |
| E3-S1 | Pending | - | Keyword matching |
| E3-S2 | Pending | - | Claude connection finder |
| E3-S3 | Pending | - | Score calculator |
| E3-S5 | Pending | - | Matcher CLI |
| E4-S1 | Pending | - | Framework selector |
| E4-S2 | Pending | - | Hook generator |
| E4-S4 | Pending | - | Suggestion formatter |
| E5-S1 | Pending | - | Notion database |
| E5-S2 | Pending | - | Notion storage |
| E5-S5 | Pending | - | /content-ideate skill |
| E5-S6 | Pending | - | Module registration |

## Sprint 2 (Enhancements)

| Story | Status | Assignee | Notes |
|-------|--------|----------|-------|
| E1-S3 | Pending | - | Twitter scraping |
| E1-S4 | Pending | - | Hacker News scraping |
| E2-S2 | Pending | - | Weekly report extraction |
| E2-S3 | Pending | - | README extraction |
| E3-S4 | Pending | - | Audience fit scoring |
| E4-S3 | Pending | - | Pillar assigner |
| E5-S3 | Pending | - | n8n workflow |
| E5-S4 | Pending | - | Slack notification |

---

# Definition of Done

For each story to be considered complete:

- [ ] Code written and tested locally
- [ ] Handles errors gracefully
- [ ] Follows existing module patterns
- [ ] Documentation updated (README, runbook)
- [ ] Works end-to-end with other components
- [ ] Reviewed against acceptance criteria

---

*Document generated from Content Opportunity Engine PRD v1.0*
