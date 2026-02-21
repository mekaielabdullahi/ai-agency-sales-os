---
source: https://www.youtube.com/watch?v=UGIZnh6HNLc
channel: Nate Herk | AI Automation
title: "Claude Code + Trigger.dev: I'm Never Building Agents the Same Way"
date: 2026-02-20
duration: "20:57"
extracted: 2026-02-20
---

## Executive Summary

Nate Herk demonstrates how combining Claude Code (an AI coding assistant) with Trigger.dev (a cloud-based task orchestration platform) enables rapid creation of production-ready automations and AI agents using only natural language prompts. Within 90 minutes of first opening Trigger.dev, he built multiple working automations including a YouTube news digest, a ClickUp-integrated company research agent, and a dental lead generator -- all deployed to production via GitHub integration.

## Key Topics

- Claude Code + Trigger.dev integration workflow
- Building automations with natural language prompts
- Trigger.dev dashboard, scheduling, retries, and orchestration
- Live demo: AI research agent with ClickUp integration
- Building a dental lead generator from scratch
- Environment variables and API key management
- Dev vs. production environments
- Deploying to production via GitHub sync
- Iterating and debugging (deduplication, plan mode)

## Detailed Notes

### Claude Code + Trigger.dev Architecture

Claude Code is used to describe desired automations in plain English. It interprets vague requests, asks clarifying questions, writes TypeScript code, and organizes it into task files. Trigger.dev then hosts and runs those tasks in the cloud with built-in scheduling, automatic retries, queuing, and orchestration. The workflow is: describe in Claude Code -> code gets written -> push to Trigger.dev -> runs autonomously.

Nate chose Trigger.dev over Modal (used in previous videos) because it offers scheduled runs, automatic retries, queuing, orchestration across tasks, and a cleaner UI.

### Live Demo: Company Research Agent

A ClickUp-integrated agent watches a task list. When a new company name is added as a task, the agent triggers, researches the company using web search tools, and posts a structured research brief as a comment on the ClickUp task. The agent also supports follow-up conversation -- Nate asked "does this company have a recent valuation?" and it performed additional research and responded. This is a non-deterministic agent with tool selection and looping, not a rigid step-by-step automation.

### Building a Dental Lead Generator from Scratch

Nate walks through building a new automation from a blank folder:

1. **Setup**: Drop in a `CLAUDE.md` file (project instructions) and a `TriggerRef.md` file (Trigger.dev API reference/TypeScript patterns) from his free School community
2. **Prompt**: Gave a vague request -- "build an automation that runs every Monday, searches the web, finds dental practices I can sell websites to"
3. **Clarification**: Claude Code asked about delivery destination (ClickUp), search scope (nationwide), and available APIs (none yet -- user wanted free options)
4. **Architecture**: Claude Code planned two separate tasks -- `FindDentalLeads` (scrape leads) and `CreateDentalLead` (write to ClickUp) -- with built-in idempotency/deduplication
5. **API pivot**: Originally chose Yelp Fusion API (free), discovered the free tier was discontinued, automatically switched to SerpAPI
6. **Result**: 25 dental leads created in ClickUp in 9 seconds across 5 cities, with address, phone, rating, and website data

### Environment Variables and API Key Security

API keys go in a `.env` file locally. The `.env` is excluded from git commits (files starting with `.` are hidden from commits). For Trigger.dev to access these keys at runtime, they must be manually added to Trigger.dev's Environment Variables settings. Nate emphasizes adding keys to both Development and Production environments. He also advises never pasting secrets directly into the Claude Code chat -- instead, ask Claude to create a placeholder in `.env` and paste there.

### Dev vs. Production and GitHub Deployment

- **Development**: Requires a local dev server connection to Trigger.dev to be open; tasks stop running when the connection closes
- **Production**: Tasks run autonomously 24/7 in the cloud
- **Deployment path**: Push code to GitHub -> connect GitHub repo to Trigger.dev project settings -> every push to master auto-deploys to production
- Manual deployment is also possible as a fallback if GitHub integration doesn't work

### Iterating and Debugging

After the initial build, Nate discovered duplicate leads despite the planned idempotency. He asked Claude Code to fix it, which added a ClickUp search-before-create step and a place ID for deduplication. This required multiple iterations to get right, highlighting the importance of using Claude Code's plan mode for complex automations rather than one-shot prompting. The final result: 48 unique leads with proper deduplication filtering.

### Trigger.dev MCP Server

Nate mentions a Trigger.dev MCP server configuration file that can be added to the project. This gives Claude Code direct integration with Trigger.dev for triggering test runs and managing deployments from within the coding environment.

## Key Quotes

> "I opened up Trigger.dev for the first time, I'm not kidding you, like an hour and a half ago, and I've already got a couple really nice automations and agents set up."

> "This is not just a deterministic 1, 2, 3, 4, 5 type of automation. This is a non-deterministic, I have different tools, I need to decide what loop I need to go in."

> "You no longer having to write code but you having to be the person that assures the quality and make sure that it's on track."

> "This example showed really why you need to plan harder because the search criteria wasn't very big and it had a weird way of deduplication."

> "AI is still very much a black box. These models are insanely smart, you can see what they do, but you also saw in this video how I had to talk so much to it and I had to be very clear."

## Action Items / Takeaways

- [ ] Try Claude Code + Trigger.dev combo for building cloud-hosted automations with natural language
- [ ] Use `CLAUDE.md` and `TriggerRef.md` reference files in project root to improve Claude Code's output quality
- [ ] Always use `.env` files for API keys; never paste secrets directly in chat or commit them to GitHub
- [ ] Add environment variables to both Dev and Production in Trigger.dev dashboard
- [ ] Use Claude Code's plan mode for complex automations to avoid iteration cycles on architecture decisions
- [ ] Connect Trigger.dev to GitHub for automatic production deployments on push
- [ ] Implement idempotency/deduplication logic early when building lead generation or data collection workflows
- [ ] Consider adding the Trigger.dev MCP server config for tighter Claude Code integration
