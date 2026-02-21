---
source: https://www.youtube.com/watch?v=oC0mPBSmzfQ
channel: Liam Ottley
title: "How to Automate Your Work with Claude Code (Beginner Breakdown)"
date: 2026-01-14
duration: "27:09"
extracted: 2026-02-20
---

## Executive Summary

Liam Ottley and Peter Yang walk through a beginner-friendly tutorial on using Claude Code to automate repetitive workflows, demonstrating the full process from installation to building a YouTube channel research tool. The core message is that Claude Code is not about writing code -- it's about describing what you want in plain English, planning well, and reviewing AI output, making automation accessible to non-developers.

## Key Topics

- Installing and setting up Claude Code (terminal and Cursor IDE)
- Identifying high-leverage workflows to automate
- The 4-step Claude Code workflow: explore, plan, build, review
- Building a YouTube channel research slash command
- Using Plan Mode to write specs before code
- Chaining slash commands for layered automation
- Voice dictation (Whisper Flow) to speed up interaction
- The future of AI agents as personalized tools
- Mindset shift: from coder to reviewer/planner

## Detailed Notes

### Installation and Setup

Claude Code is installed via a terminal command from the Claude Code website. You type `claude` in the terminal to open it. Peter recommends using Cursor IDE alongside Claude Code because it lets you browse and review the files Claude creates visually. To open Claude Code inside Cursor, open a terminal within Cursor and type `claude`.

### Identifying What to Automate

The first step is inventorying your week and identifying what takes the most time. Peter uses the example of YouTube thumbnail/title research -- a time-consuming task for creators. The framework generalizes to any repetitive knowledge work: competitor research, newsletter curation, content writing, etc. The key question to ask Claude: "I'm spending a lot of time on X -- is there a way to make this simpler?"

### The 4-Step Claude Code Workflow

1. **Explore solutions** -- Ask Claude for multiple approaches with pros/cons. Peter asked for three ways to fetch YouTube data (official API, web scraping, third-party services) and pushed for a simpler free alternative (yt-dlp)
2. **Write a spec/plan** -- Use Plan Mode (Shift+Tab) to prevent Claude from writing code prematurely. Get Claude to write a requirements document first. Peter emphasizes that 70-80% of the work is writing the plan, not the code
3. **Build** -- Tell Claude to implement the spec. It writes the slash command, creates files, and sets up the workflow
4. **Review and iterate** -- Check the output, fix bugs, refine. AI tends to over-build, so cutting unnecessary requirements is important

### Plan Mode

Plan Mode is activated by pressing Shift+Tab until it says "plan mode." In this mode, Claude cannot modify code -- it can only write plans and documents. This is critical because the model likes to jump to writing code, but the quality of the final output depends entirely on the quality of the spec. Peter's background as a product leader reinforces this: always write the requirements document first, then have AI build from it.

### Building the YouTube Research Command

The slash command `/youtube [channel-name]` was built to: fetch 20 recent videos via yt-dlp, show top 10 by views (title, view count, duration), and include key insights about what content is working for the channel. After building the single-channel version, they extended it to process multiple channels from a `channels.md` file, demonstrating how to layer functionality.

### Chaining Slash Commands

Once the research command worked, they discussed extending it by adding context files (e.g., `pdang-core-context.md` with personal info, goals, content style) and creating a new `/write` slash command that takes a video idea, combines the research data with personal context, and drafts scripts. This shows how small automations can be layered into comprehensive workflows.

### Voice Dictation Productivity

Both hosts recommend voice dictation tools (Whisper Flow mentioned specifically) for dramatically faster input. Instead of typing feedback into Claude Code, you speak it and paste the transcript. Liam estimates it saves tens of hours per week. Peter notes even his 7-year-old can voice-dictate to Claude.

### Future of AI Agents

Peter sees Claude Code as the first true general agent -- it can do whatever you tell it to. The shift is from using pre-built applications (Workday, Twitter) to building hyper-personalized agents trained on your specific use case. Liam suggests this will evolve into a central operating system where MCP-like protocols let agents access functionality from various applications.

## Key Quotes

> "70 or 80% of the time, you're actually just writing documents with AI. You're making the plan because the actually coding step AI will actually do it."

> "It seems really intimidating. It's all about code, but in reality, it should really be Claude General Agent... you're just chatting with somebody."

> "I think the difference between a complete new beginner and the first step is realizing that the value is in the plan."

> "If you have a problem, just ask the AI how you can do this stuff. And it'll probably tell you... thinking like, I have a problem, can I build something for this? Because building is now accessible."

> "I've been able to let run for like 13 hours straight and code overnight for me and build an entire MVP."

## Action Items / Takeaways

- [ ] Install Claude Code via the terminal command from the official website
- [ ] Inventory your week to identify the most time-consuming repetitive task
- [ ] Use Cursor IDE alongside Claude Code for visual file browsing
- [ ] Always use Plan Mode (Shift+Tab) to write specs before building
- [ ] Push Claude for free/simple API alternatives when exploring solutions (e.g., yt-dlp over YouTube official API)
- [ ] Create context files (markdown) about yourself, your business, and goals to personalize Claude's output
- [ ] Layer slash commands: build simple ones first, then chain them into more complex workflows
- [ ] Adopt voice dictation (Whisper Flow or similar) to speed up AI interaction
- [ ] Ask Claude "what's the lowest hanging fruit?" when you're unsure where to start automating
