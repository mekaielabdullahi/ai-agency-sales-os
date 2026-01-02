# BMAD + AutoClaude + Plotter Mechanix Sync Up

**Date:** December 28, 2025
**Duration:** 119 minutes
**Type:** Toolchain & Process Alignment
**Attendees:** Matthew Kerns, Mekaiel Abdullahi
**Recording:** [Fathom Recording](https://fathom.video/share/SMHiqxvHdseaLkrp1vD_T6ZH76xZBDtJ)

---

## Meeting Purpose

Align on toolchain and process for Plotter Mechanics project; set near-term priorities: PRD creation, clarify deliverables vs SOW, and divide responsibilities between product/process (Mekaiel) and build (Matthew).

**Outcome:** Created [January 2026 Team Roles document](../../../strategic-alignment/strategic-objectives/2026-01-january-team-roles.md) defining all team member responsibilities and the PRD-first development process.

---

## Updates

### Mekaiel Abdullahi

**Check-in:**
- Exploring AskTactic/Tactic.ai for live transcripts/AI prompts in Meet
- Setting up Autocloud and BMAD on Windows; resolved Python path issue

**Progress on Priorities Since We Last Met:**
- Installed BMAD Method in SalesOS; began learning Analyst/PM workflows
- Initiated Autocloud setup; connected repo and ran context/ideation
- Drafted thinking on process guardrails: PRD-first development, client comms boundaries

**Priorities Until We Meet Again:**
- Create draft PRD for Plotter Mechanics using BMAD (Analyst/PM) to become single source of truth
- Share Miro "deliverables" board and align it with SOW in a refined internal deliverables list
- Define client interaction protocol (windows, channels) and escalation path
- Prep personal socials/brand to support mid-Jan event promo; document process

**In Need of Assistance / Blocked On:**
- PRD structure expectations/examples; wants Matthew's feedback on first PRD draft
- Clarification on Autocloud vs CloudCode OS scope in planning vs execution

### Matthew Kerns

**Check-in:**
- Expecting potential client work via contact closing soon; possible larger event company lead
- Will be offline for a workout/family block; back later today

**Progress on Priorities Since We Last Met:**
- Oriented Mekaiel to BMAD (Analyst "Mary"), Autocloud roadmap/worktrees, and CloudCode OS organization
- Conducted Analyst investigations: mapped Jobber/Quo APIs, open questions, and preliminary roadmap (e.g., status bot, comms hub)
- Moved discovery transcripts to the Agency OS; improved repo organization practices

**Priorities Until We Meet Again:**
- Review Mekaiel's PRD draft; identify high-certainty items safe to implement
- Constrain early builds until PRD v0 is approved to avoid rework
- Sync with Trent to reconcile SOW deliverables vs internal deliverables (Miro) and tighten future SOW specificity

**In Need of Assistance / Blocked On:**
- Deliverables clarity: ensure quick-win sprint outputs map precisely to signed agreement
- Decision on SMS/voice provider abstraction (Twilio vs Quo) pending cost/fit

---

## Topics Discussed

### 1. Tactic.ai Trial
- **Purpose:** Lightweight transcription/AI during Meet without bot invites
- **Notes:** Live key points/follow-ups; likely transcript-only, not video

### 2. BMAD Method Overview and Install
- **Purpose:** Use Analyst/Architect/Dev/PM agents to drive SDLC
- **Actions:** Installed BMAD in repos; avoid "Agent Vibes"; leverage slash commands; Analyst created investigations and open question lists

### 3. Autocloud Usage and Value
- **Purpose:** Planning → roadmap → implementation with AI; creates worktrees for human review
- **Key:** Run context → ideation → roadmap; set models to balanced; enable competitor analysis as needed; expect buggy UI but functional backend

### 4. CloudCode OS vs BMAD vs Autocloud
- **Purpose:** Define roles:
  - **CloudCode OS** = centralized planning/context/docs
  - **BMAD** = structured analysis/PRD/epics/stories
  - **Autocloud** = code planning/execution/review via worktrees

### 5. Plotter Mechanics Deliverables Alignment
- **Purpose:** Ensure quick-win sprint outputs match SOW
- **Findings:** SOW is intentionally high-level (SOPs, comms protocol, training, blueprint); internal Miro deliverables (how-to guides, 3 automations, form) to be mapped into PRD and future SOWs

### 6. PRD-First Operating Model
- **Purpose:** Avoid scope creep/rework; create single source of truth
- **Plan:** Sales/Discovery feeds PRD; builds only execute from PRD; changes must flow through business funnel and PRD change control

### 7. Provider Choice Abstraction (Twilio vs Quo)
- **Purpose:** Control costs and flexibility
- **Plan:** Build interface/adapter to swap providers; don't block early planning; defer final choice pending cost analysis and feature needs

### 8. Client Communication Boundaries
- **Purpose:** Protect dev focus/time
- **Plan:** Define Slack availability windows, weekly check-ins, emergency line; set expectations during onboarding

### 9. Team Process and Scale Readiness
- **Purpose:** Prepare for more pipeline and February event
- **Plan:** Document everything; divide and conquer: Mekaiel PM/PRD/client bridge; Matthew build/review; use BMAD/Autocloud to multiply output

---

## Action Items

| Owner | Action | Due |
|-------|--------|-----|
| Mekaiel | Draft PRD v0 for Plotter Mechanics in BMAD; share for review | Next check-in |
| Mekaiel | Post Miro deliverables link + context in Plotter channel; map to SOW items | - |
| Matthew | Review PRD v0; mark "build-safe" items; propose initial epics/stories | After PRD draft |
| Both | Meet with Trent to align SOW vs internal deliverables and tighten future SOW templates | - |
| Matthew | Keep Autocloud from running ahead of PRD; pause/redirect tasks as needed | Ongoing |
| Both | Define provider abstraction approach and preliminary choice criteria (cost, features, support) | - |
| Mekaiel | Draft client comms policy (availability windows, channels, escalation) for team approval | - |
| Mekaiel | Document socials/brand rollout process; share guide with team | - |
| Both | Regroup later today to assign tasks Kanban-style and finalize immediate priorities | Today |

---

## Key Decisions

1. **PRD-First Development:** No builds without PRD approval to avoid rework
2. **Tool Roles Defined:** CloudCode OS (docs/context), BMAD (analysis/PRD), Autocloud (code execution)
3. **Role Division:** Mekaiel = PM/PRD/client bridge; Matthew = build/review
4. **Provider Abstraction:** Build interface layer to swap Twilio/Quo without rewriting

---

## Key Quotes from Meeting

**On Developer Protection:**
> "Bro, you have to protect your time. Because people will be people. And it's like, cool, but you have to set up a system that protects you from the chaos of the client."

> "Keep Matthew as far away from the client as possible, because what you should be working out of is the structure. The client is chaos. You should only be working on it through the business frame."

**On PRD-First Development:**
> "Before you change the PRD, it has to come from a business funnel. If you're putting outputs in, they should be coming from inputs from a business funnel - not from whatever the customer wants."

> "At a certain stage, when we start building - we can't go back. We deliver what was promised. New requests go to next phase."

**On AutoClaude Multiplier:**
> "This is how we can optimize - we pay like $100-200/month for Claude subscription. AutoClaude can be running, as long as we keep it running on stuff, it'll just keep building. It'll work for us."

**On Matthew's Role:**
> "If I have clear things that I need to build, there's so many tools that I can build stuff quickly. But I also need to work through all the issues - there's gonna be so many issues that come up in development, even with all the AI tools in the world. There's things where it just doesn't work. And that's why I have a job."

**On Mekaiel's Background:**
> "My last job with the DOS - at any given time, there's at least five to six technical security integrations going on in a month. And I did that for two and a half years. The coordination is crazy."

---

## Annotations/Highlights

- [Matthew says goodbye](https://fathom.video/share/SMHiqxvHdseaLkrp1vD_T6ZH76xZBDtJ?timestamp=7111.657403999999)
- [Draft Plotter Mechanics PRD discussion](https://fathom.video/share/SMHiqxvHdseaLkrp1vD_T6ZH76xZBDtJ?timestamp=6661.9999)

---

## Related Documents

- [January 2026 Team Roles](../../../strategic-alignment/strategic-objectives/2026-01-january-team-roles.md) - Created from this meeting
- [Development Framework Overview](../../../../03-ai-growth-engine/development-framework/FRAMEWORK-OVERVIEW.md)
- [Internal Development OS](../../../../03-ai-growth-engine/development-framework/03-development-execution/00-INTERNAL-DEVELOPMENT-OS.md)
