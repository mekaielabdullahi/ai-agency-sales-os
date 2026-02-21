# Chris Fireflies Integration Session

**Date:** December 29, 2025
**Type:** Internal Training / Tooling Setup
**Attendees:** Matthew Kerns, Chris Andrade
**Recording:** [Fathom Recording](https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2)

---

## Meeting Purpose

Align on integrating Fireflies with Chris's Cloud Code OS, mirror Matthew's OS folder structures, and set up a repeatable pipeline to ingest, organize, and summarize meetings for opportunity matrices and project work.

---

## Updates

### Matthew Kerns

**Check-in:**
- Encouraged resilience when threads disappear; shared past experience rebuilding faster after loss.

**Progress on Priorities Since We Last Met:**
- Provided repo link and guided prompt engineering to replicate his Operations project/meeting structure.
- Coached on Git workflow (commit vs push), security practices (no secrets in Git), and Claude tool approvals.

**Priorities Until We Meet Again:**
- Improve summaries by integrating Fireflies Summaries API.
- Share discovery process/SOPs and next steps in Slack.

**In Need of Assistance / Is Blocked On:**
- None noted.

### Chris Andrade

**Check-in:**
- Balancing family time; motivated to hit weekly targets; energized by group momentum.

**Progress on Priorities Since We Last Met:**
- Pushed OS live on GitHub; purchased Claude credits; connected Fireflies via API.
- Mirrored Matthew's 02-operations structure for project mgmt and meetings.
- Installed Python, configured env, ran sync scripts; successfully pulled meetings (transcripts + generated summaries), created action items and structure.
- Hit weekly goal for opportunity calls: Shoe store (oppty matrix this week), S&S Woolsheds, AZ Events, Maples Apothecary queued.

**Priorities Until We Meet Again:**
- Use Fireflies to record/self-capture ideation and calls; continuously funnel into OS.
- Build opportunity matrices this week for Shoe store, S&S Woolsheds, AZ Events; run discovery for AZ Events; Maples Apothecary intro + discovery.
- Organize action items "by client" and "by type" per README; push commits so mobile can query content.

**In Need of Assistance / Is Blocked On:**
- Cost management clarity across Anthropic user vs developer billing; model selection to stretch credits (Sonnet vs Opus).
- Enhancing summaries from Fireflies vs Claude-generated; confirm best API endpoints.
- Fireflies processing cadence from phone; potential automation for post-meeting pulls.

---

## Topics Discussed

### 1. Reliability of AI Chats and Resilience Workflow
- Threads can vanish on mobile; mitigate by quickly re-summarizing key points
- Build habit of documenting progress immediately

### 2. Hitting Pipeline Goals and Opportunity Matrix Plan
- This week targets met/overfilled: Shoe store, S&S, AZ Events, Maples Apothecary
- Aim to produce multiple opportunity matrices and discovery outputs

### 3. Folder Structure Mirroring and Prompting Strategy
- Replicate Matthew's Operations: project management + meeting folders
- Store Fireflies summaries/transcripts
- Precise prompts referencing Matthew's repo

### 4. Fireflies API Integration and Local Environment Setup
- Steps: clone repo, set Fireflies API key in .env, install Python/pip, run sync_meetings.py
- Avoid committing secrets
- Approve Claude tool usage smartly

### 5. Git Hygiene and Mobile Access
- Commit frequently, push to access from phone
- Understand commit vs push difference
- Review commit messages for traceability

### 6. Action Items Extraction and Organization
- Current outputs: action_items/active, raw transcripts, per-meeting summaries
- Next: populate by-client and by-type directories per README

### 7. Cost/Billing Strategy for AI Tools
- Distinguish Anthropic user plan vs developer balance
- Switch to Sonnet for routine tasks
- Consider tier upgrades vs top-ups
- Define January tools budget

### 8. Leveraging Pre-Paid Marketing Tools
- Chris has an agency kit (QR codes, content gen, etc.)
- Plan a review to map tools to client needs (e.g., SNS QR needs)
- Reduce redundancy

### 9. Automation and Future Improvements
- Potential automatic meeting ingestion
- Enhance Fireflies Summaries API
- Extend to Fathom later
- Record training videos for client onboarding

---

## Next Steps

| Owner | Action | Due |
|-------|--------|-----|
| Matthew | Share discovery process next steps and SOP links in Slack | This week |
| Matthew | Prototype integration with Fireflies Summaries API; PR to repo for Chris to pull | This week |
| Chris | Populate "by client" and "by type" action item structures per README; test queries from mobile | This week |
| Chris | Standardize Fireflies capture (self-record + calls), then sync/push after sessions | Ongoing |
| Both | Review agency tool kit to identify usable features (QR, content gen) and retire redundant spend; propose January tools budget | This week |
| Chris | Build and deliver opportunity matrices for Shoe store, S&S Woolsheds, AZ Events; run AZ discovery; schedule Maples Apothecary intro + discovery | This week |
| Both | Record a clean tutorial pass of the Fireflies integration for client training | This week |

---

## Action Items (with timestamps)

| Action | Link |
|--------|------|
| Add Fireflies Summaries API to sync script; integrate into my OS; then Chris pulls | [WATCH](https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2?timestamp=5378.9999) |
| Post next steps in Slack to Chris | [WATCH](https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2?timestamp=5668.9999) |
| Run Maples Apothecary discovery call w/ 5-question framework; introduce Matthew & Mikael | [WATCH](https://fathom.video/share/FAR87xKdceD-xoqqchGFvu-xnAUJ5qM2?timestamp=5694.9999) |

---

## Chris's Pipeline This Week

| Client | Status | Next Action |
|--------|--------|-------------|
| Shoe Store | Opportunity call done | Build opportunity matrix |
| S&S Woolsheds | In queue | Build opportunity matrix |
| AZ Events | In queue | Run discovery |
| Maples Apothecary | In queue | Intro + discovery call |

---

## Technical Setup Completed

**Chris's Environment:**
- Fireflies API connected via .env
- Python installed, pip configured
- sync_meetings.py running successfully
- Transcripts + summaries pulling into OS
- Action items structure created
- GitHub repo live and pushing

**Git Workflow Learned:**
- Commit = save locally
- Push = upload to GitHub (enables mobile access)
- Don't commit secrets (.env files)
- Review Claude tool approvals carefully

---

## Related Documents

- [Earlier Setup Session](./2025-12-29-chris-claude-code-os-setup/summary.md)
- [Training Session Doc](../../../../05-hr-department/developer-academy/training-sessions/2025-12-29-chris-claude-code-os-setup.md)
