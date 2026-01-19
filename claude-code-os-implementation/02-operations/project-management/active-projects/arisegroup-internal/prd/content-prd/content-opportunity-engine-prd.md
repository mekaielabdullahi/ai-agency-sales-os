# Product Requirements Document (PRD)
# Content Opportunity Engine

**Project:** AriseGroup Internal Content Automation
**Version:** 1.0
**Date:** January 18, 2026
**Author:** AriseGroup.ai
**Status:** Planning

---

## 1. Executive Summary

### 1.1 Overview

The Content Opportunity Engine is an automation system that bridges external content trends with AriseGroup's internal work context to generate actionable LinkedIn content suggestions. It scrapes trending AI/automation discussions from LinkedIn, Reddit, Twitter, and Hacker News, compares them against current client projects and strategic priorities, and outputs content ideas mapped to existing frameworks and hook formulas.

### 1.2 Problem Statement

AriseGroup's content strategy is mature (5 AI agents, 7 frameworks, 10 hook formulas) but content ideation remains manual and time-consuming:

- **Trend Blindness:** No systematic way to track what's trending in the AI/automation space
- **Context Disconnect:** External trends aren't connected to internal work (client projects, wins, learnings)
- **Ideation Friction:** Content planning requires manual research + brainstorming each week
- **Missed Opportunities:** Build-in-public moments pass without being captured as content

**Root Cause:** No automated bridge between "what the world is talking about" and "what we're actually doing."

### 1.3 Guiding Principle

> **Content suggestions must connect external trends to real AriseGroup work.**

Generic content ideas aren't valuable. The engine's power comes from finding non-obvious connections between trending topics and Plotter Mechanix, Wolf Sheds, or other active projects. If suggestions don't reference real work, they're just noise.

**Implications:**
- Every suggestion must include a "Work Connection" field
- Prioritize depth of connection over volume of suggestions
- Low-relevance ideas (<50 score) should be filtered out
- Build-in-Public pillar (40% of content) requires genuine project references

### 1.4 Investment & Timeline

| Attribute | Value |
|-----------|-------|
| Investment | Internal development (no external cost) |
| Ongoing Cost | ~$40-70/month (Apify + Claude API) |
| Timeline | 2-3 weeks for MVP |
| Target Delivery | End of January 2026 |

---

## 2. Use Cases (Problems)

### UC-1: Weekly Content Planning (Sunday)

**Current State:**
- Mekaiel manually brainstorms content topics during weekly planning
- No visibility into what's trending in AI/automation space
- Ideas come from memory, not systematic research
- Often defaults to same topics repeatedly

**Pain Quantification:**
- 1-2 hours/week on content ideation
- Miss trending topics that could drive engagement
- Content pillars become imbalanced without tracking

**User Quote:**
> "I know what I'm working on, but I don't know what the world is talking about this week."

---

### UC-2: Capturing Build-in-Public Moments

**Current State:**
- Client wins, system builds, and learnings happen continuously
- No prompt to turn these into content
- By the time weekly planning arrives, details are forgotten
- 40% content pillar (Build-in-Public) is hardest to fill

**Pain Quantification:**
- Genuine stories go untold
- Content feels forced when memory fades
- Authenticity suffers without real-time capture

**User Quote:**
> "We built something cool for Plotter Mechanix on Tuesday, but by Sunday I can't remember the details."

---

### UC-3: Connecting Trends to Work

**Current State:**
- See interesting posts on LinkedIn/Twitter
- Don't immediately see how it connects to AriseGroup work
- Opportunity passes; no action taken
- Later realize "we actually solved that problem last week"

**Pain Quantification:**
- Reactive instead of proactive content
- Missed thought leadership positioning
- External validation of our approach goes uncaptured

---

### UC-4: Framework & Hook Selection

**Current State:**
- 7 LinkedIn frameworks exist but selection is intuitive
- 10 hook formulas available but choice is overwhelming
- No guidance on which framework fits which topic
- Hooks often reused without variation

**Pain Quantification:**
- Underutilization of content templates
- Repetitive post structures
- Hook quality varies without structured guidance

---

## 3. Solution Summary

### 3.1 Core Approach

Implement a **Content Opportunity Engine** as an agentic module that:
1. Scrapes trending AI/automation content daily (Apify)
2. Extracts current work context from project files
3. Matches trends to work using Claude API
4. Generates suggestions mapped to existing frameworks/hooks
5. Stores in Notion, notifies via Slack

### 3.2 Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  TREND SCRAPER  │ →  │ CONTEXT EXTRACTOR │ →  │ OPPORTUNITY     │
│  LinkedIn       │    │ P0 files         │    │ MATCHER         │
│  Reddit         │    │ Weekly reports   │    │ Claude API      │
│  Twitter        │    │ Project READMEs  │    │ Relevance score │
│  Hacker News    │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                       ↓
                              ┌──────────────────────────────────┐
                              │  SUGGESTION GENERATOR            │
                              │  - Maps to 7 LinkedIn frameworks │
                              │  - Picks from 10 hook formulas   │
                              │  - Assigns content pillar        │
                              │  - Drafts 3 hook options         │
                              └──────────────────────────────────┘
                                                       ↓
                              ┌──────────────────────────────────┐
                              │  STORAGE & DELIVERY              │
                              │  Notion "Content Ideas" database │
                              │  Slack notification (top 3/day)  │
                              └──────────────────────────────────┘
```

**Visual Diagram:** `arisegroup-internal/diagrams/content-opportunity-engine-dataflow.excalidraw`

### 3.3 How Each Use Case is Solved

| Use Case | Current | Solution | Outcome |
|----------|---------|----------|---------|
| UC-1: Weekly Planning | Manual brainstorming | Pre-generated ideas in Notion | 5-10 vetted suggestions ready each Sunday |
| UC-2: Build-in-Public | Forgotten moments | Context extractor reads P0 files daily | Real project details auto-suggested |
| UC-3: Connecting Trends | Manual correlation | Claude API finds connections | Non-obvious angles surfaced automatically |
| UC-4: Framework Selection | Intuitive choice | AI maps topic to best framework | Each suggestion includes framework + 3 hooks |

### 3.4 Integration Pattern

**Hybrid: n8n Scheduled + On-Demand Skill**

| Component | Trigger | Function |
|-----------|---------|----------|
| n8n Workflow | Daily 6 AM | Scrape all sources, store raw trends |
| `/content-ideate` Skill | On-demand | Match trends to context, generate suggestions |
| Notion Database | Continuous | Store all ideas with status tracking |
| Slack Notification | After n8n run | Surface top 3 ideas to #content channel |

### 3.5 Data Sources

**External (Trend Scraper):**

| Source | What to Scrape | Apify Actor | Frequency |
|--------|----------------|-------------|-----------|
| LinkedIn | AI agency posts, thought leaders | `apify/linkedin-scraper` | Daily |
| Reddit | r/ChatGPT, r/artificial, r/smallbusiness | `trudax/reddit-scraper` | Daily |
| Twitter/X | AI influencers, agency accounts | `apidojo/tweet-scraper` | Daily |
| Hacker News | AI/automation discussions | `drobnikj/hackernews-scraper` | Daily |

**Internal (Context Extractor):**

| Source | Path | What It Provides |
|--------|------|------------------|
| P0 Files | `active-projects/*/status/P0-ACTIVE-NOW.md` | Current client work |
| Weekly Reports | `02-operations/weekly-reports/weekly-report-*.md` | Recent progress & wins |
| Project READMEs | `active-projects/*/README.md` | Client context & industries |
| Content History | `04-content-team/linkedin-posts/*.md` | What's already been posted |

### 3.6 Relevance Scoring

Each scraped idea scored 0-100:

| Factor | Weight | What It Measures |
|--------|--------|------------------|
| Topic Alignment | 40% | Matches niche keywords (AI, automation, agency) |
| Work Connection | 30% | Ties to current projects (Plotter, Wolf Sheds) |
| Audience Fit | 20% | Relevant to founders, small business owners |
| Timeliness | 10% | Trending now vs. old content |

**Threshold:** Only ideas scoring 50+ are surfaced. Ideas 80+ get Slack notification.

---

## 4. Requirements

### 4.1 Functional Requirements

#### FR-1: Trend Scraper Module

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-1.1 | Scrape LinkedIn posts matching niche keywords | Must Have | Pending |
| FR-1.2 | Scrape Reddit posts from target subreddits | Must Have | Pending |
| FR-1.3 | Scrape Twitter/X from AI influencer accounts | Should Have | Pending |
| FR-1.4 | Scrape Hacker News AI-tagged discussions | Should Have | Pending |
| FR-1.5 | Store raw scraped data in `.tmp/trends_*.json` | Must Have | Pending |
| FR-1.6 | Configurable keywords list for niche targeting | Must Have | Pending |
| FR-1.7 | Rate limiting to avoid API bans | Must Have | Pending |

#### FR-2: Context Extractor Module

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-2.1 | Read P0-ACTIVE-NOW.md files from active projects | Must Have | Pending |
| FR-2.2 | Parse weekly reports for recent wins/progress | Must Have | Pending |
| FR-2.3 | Extract client names, industries, technologies used | Must Have | Pending |
| FR-2.4 | Track content already posted (avoid repetition) | Should Have | Pending |
| FR-2.5 | Generate structured work context JSON | Must Have | Pending |

#### FR-3: Opportunity Matcher Module

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-3.1 | Keyword matching for topic alignment (fast path) | Must Have | Pending |
| FR-3.2 | Claude API integration for connection finding | Must Have | Pending |
| FR-3.3 | Calculate relevance score (0-100) | Must Have | Pending |
| FR-3.4 | Filter out low-relevance ideas (<50) | Must Have | Pending |
| FR-3.5 | Identify specific work connection for each idea | Must Have | Pending |

#### FR-4: Suggestion Generator Module

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-4.1 | Map each idea to best LinkedIn framework | Must Have | Pending |
| FR-4.2 | Assign appropriate content pillar | Must Have | Pending |
| FR-4.3 | Generate 3 hook options using 10 formulas | Must Have | Pending |
| FR-4.4 | Include body direction (2-3 sentences) | Should Have | Pending |
| FR-4.5 | Output structured markdown per suggestion | Must Have | Pending |

#### FR-5: Storage & Delivery

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-5.1 | Create Notion "Content Ideas" database | Must Have | Pending |
| FR-5.2 | Store all suggestions with required fields | Must Have | Pending |
| FR-5.3 | n8n scheduled workflow (daily 6 AM) | Must Have | Pending |
| FR-5.4 | Slack notification for top 3 ideas/day | Should Have | Pending |
| FR-5.5 | `/content-ideate` skill for on-demand generation | Must Have | Pending |
| FR-5.6 | Track idea status (Pending/In Progress/Published) | Must Have | Pending |

### 4.2 Non-Functional Requirements

| ID | Requirement | Target | Priority |
|----|-------------|--------|----------|
| NFR-1 | Apify scraping reliability | >90% success rate | Must Have |
| NFR-2 | Claude API response quality | Useful connections | Must Have |
| NFR-3 | Daily run completion | <10 minutes | Should Have |
| NFR-4 | Monthly cost | <$75 | Must Have |
| NFR-5 | Suggestion relevance | >60% marked "useful" | Must Have |

---

## 5. Notion Database Schema

### "Content Ideas" Database

| Property | Type | Purpose | Values |
|----------|------|---------|--------|
| Title | Title | Opportunity name | Free text |
| Status | Select | Workflow state | Pending, In Progress, Published, Rejected |
| Relevance Score | Number | Match quality | 0-100 |
| Source | Select | Where scraped from | LinkedIn, Reddit, Twitter, HN, Manual |
| Source URL | URL | Original content link | URL |
| Content Pillar | Select | Strategic category | Build-in-Public, AI Insights, Productivity, Case Studies |
| Framework | Select | Post structure | PSV, Listicle, Story Arc, Contrarian, Quick Win, Question, Data |
| Hook Formula | Select | Opening approach | Curiosity, Contrarian, Pattern Interrupt, Authority, Problem, etc. |
| Work Connection | Multi-select | Related projects | Plotter Mechanix, Wolf Sheds, AntSavvy, Internal, General |
| Draft Hooks | Rich Text | 3 hook options | Markdown |
| Body Direction | Rich Text | Suggested content | Markdown |
| Generated Date | Date | When created | Auto |
| Published Date | Date | When posted | Manual |
| Published URL | URL | Link to LinkedIn post | Manual |
| Notes | Rich Text | Additional context | Free text |

---

## 6. User Stories

### 6.1 Mekaiel (Founder/Content Creator)

**US-1:** As Mekaiel, I want content ideas waiting for me on Sunday morning, so I can plan the week's posts in 30 minutes instead of 2 hours.

**Acceptance Criteria:**
- [ ] 5-10 vetted suggestions in Notion by Sunday
- [ ] Each suggestion includes framework + pillar + 3 hooks
- [ ] At least 3 suggestions connect to real client work
- [ ] Can filter by content pillar

**US-2:** As Mekaiel, I want suggestions that connect trending topics to my actual work, so my content feels authentic and timely.

**Acceptance Criteria:**
- [ ] Each suggestion shows specific work connection
- [ ] Build-in-Public ideas reference real projects
- [ ] Can see why each idea scored highly

**US-3:** As Mekaiel, I want Slack notifications for high-scoring ideas, so I can capture timely opportunities without checking Notion.

**Acceptance Criteria:**
- [ ] Top 3 ideas posted to #content daily
- [ ] Notification includes title, score, work connection
- [ ] Can click through to full suggestion in Notion

### 6.2 Content Team (AI Agents)

**US-4:** As the Content Director agent, I want structured suggestions to delegate to specialists, so content creation can proceed without manual ideation.

**Acceptance Criteria:**
- [ ] Each suggestion includes recommended framework
- [ ] Hook options are diverse (not all same formula)
- [ ] Body direction provides enough context to draft

---

## 7. Implementation Plan

### 7.1 Module Structure

```
agentic/modules/content-ideation/
├── agentic-module.yaml
├── README.md
├── tool/
│   ├── scrape_trends.py        # Apify scraping
│   ├── extract_context.py      # Read project files
│   ├── match_opportunities.py  # Score + connect
│   └── generate_suggestions.py # Output formatting
├── runbook/
│   └── content_ideation.md     # Orchestration
└── commands/
    └── ideate.md               # /content-ideate skill
```

### 7.2 Timeline

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Phase 1: Core Module | 3-4 days | scrape_trends.py, extract_context.py, match_opportunities.py, generate_suggestions.py |
| Phase 2: Integration | 2-3 days | Notion database, n8n workflow, /content-ideate skill, Slack notifications |
| Phase 3: Refinement | Ongoing | Add sources, tune weights, track effectiveness |

### 7.3 Phase 1 Tasks

1. Create module skeleton with `agentic-module.yaml`
2. Build `scrape_trends.py` (LinkedIn + Reddit first)
3. Build `extract_context.py` (P0 files + weekly reports)
4. Build `match_opportunities.py` (keyword + Claude matching)
5. Build `generate_suggestions.py` (framework/hook mapping)
6. Test end-to-end with sample data

### 7.4 Phase 2 Tasks

1. Create Notion "Content Ideas" database with schema
2. Connect via existing `modules/notion/tool/notion_api.py`
3. Build n8n workflow for daily scheduling
4. Create `/content-ideate` skill definition
5. Add Slack notification node to workflow
6. Document in runbook

---

## 8. Success Metrics

### 8.1 Quantitative Metrics

| Metric | Baseline | Week 2 | Week 4 | 30-Day |
|--------|----------|--------|--------|--------|
| Ideas generated/week | 0 | 30+ | 50+ | 50+ |
| Ideas marked "useful" | 0% | 50% | 60% | 70%+ |
| Ideas → Published posts | 0% | 10% | 20% | 25%+ |
| Hours saved on ideation | 0 | 0.5 | 1.0 | 1.5+ |
| Build-in-Public ideas/week | Manual | 5+ | 10+ | 10+ |

### 8.2 Qualitative Metrics

| Outcome | Success Statement | Validated? |
|---------|-------------------|------------|
| Time Savings | "Sunday planning takes 30 min instead of 2 hours" | ☐ |
| Relevance | "Suggestions actually connect to what I'm doing" | ☐ |
| Freshness | "I'm posting about current trends, not stale topics" | ☐ |
| Authenticity | "Build-in-public content feels genuine" | ☐ |
| Framework Utilization | "I'm using more of the 7 frameworks now" | ☐ |

### 8.3 Cost Analysis

| Component | Monthly Cost |
|-----------|--------------|
| Apify (LinkedIn + Reddit + Twitter + HN) | $30-60 |
| Claude API (matching ~50 items/day) | $5-10 |
| Notion | $0 (existing) |
| n8n | $0 (existing) |
| **Total** | **$35-70/month** |

**ROI:** 1.5 hrs/week × 4 weeks = 6 hrs/month saved. At $100/hr founder time = $600 value. ROI = 8-17x.

---

## 9. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Apify scraping blocked | Medium | High | Use multiple actors; rotate user agents; respect rate limits |
| Low suggestion relevance | Medium | High | Tune scoring weights; iterate on Claude prompts; filter threshold |
| Notion API limits | Low | Medium | Batch writes; use existing module patterns |
| Source quality varies | Medium | Medium | Weight sources by historical quality; allow manual source filtering |
| Over-automation | Low | Medium | Keep human in loop for final content decisions; suggestions not auto-posts |
| Claude API costs spike | Low | Medium | Set daily limits; cache similar queries; use Haiku for simple tasks |

---

## 10. Dependencies

### 10.1 Existing Infrastructure Required

| Dependency | Status | Notes |
|------------|--------|-------|
| Apify account + API token | Required | Used by leads module already |
| Anthropic API key | Required | Used throughout system |
| Notion workspace | Required | Existing databases |
| Slack workspace | Required | #content channel |
| n8n instance | Required | Existing workflows |

### 10.2 Content System Dependencies

| Dependency | Location | Usage |
|------------|----------|-------|
| 7 LinkedIn Frameworks | `04-content-team/content-templates/social/linkedin-post-frameworks.md` | Map suggestions to frameworks |
| 10 Hook Formulas | `04-content-team/agents/prompts/hook-specialist-agent.md` | Generate hook options |
| Content Pillars | `04-content-team/content-strategy/` | Assign pillar to each suggestion |
| Brand Guidelines | `04-content-team/arisegroup-tone-and-brand-guide.md` | Ensure voice consistency |

---

## 11. Open Questions

1. **Source Prioritization:** Should LinkedIn be weighted higher than Reddit since that's the target platform?
2. **Influencer List:** Which specific LinkedIn/Twitter accounts should be tracked for thought leadership?
3. **Content Pillar Balance:** Should the engine enforce the 40-30-20-10 ratio or just report it?
4. **Rejection Feedback:** When ideas are marked "Rejected," should reasons be captured to improve matching?
5. **Engagement Tracking:** Should published post performance feed back into relevance scoring?
6. **Team Access:** Should other team members (Nikhil, Brian) have access to the Content Ideas database?

---

## 12. Out of Scope (Future Phases)

| Feature | Reason | Future Phase |
|---------|--------|--------------|
| Auto-posting to LinkedIn | Human-in-loop preferred | Phase 2 |
| Multi-platform posting | LinkedIn-first focus | Phase 2 |
| Engagement analytics integration | Need baseline data first | Phase 2 |
| Newsletter scraping (RSS) | Lower priority source | Phase 1.5 |
| Video content suggestions | Different content type | Phase 3 |
| Competitor analysis | Separate initiative | Phase 3 |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-18 | AriseGroup.ai | Initial PRD created based on content ideation automation planning session |

---

*This PRD is a living document. Requirements will be refined based on Phase 1 implementation results and user feedback.*
