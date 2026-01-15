# Action Items - Internal PRD Review
**Date:** January 5, 2026
**Source:** Internal team huddle (Matthew, Trent, Mekaiel, Chris)

---

## Immediate (This Week)

### Technical Validation
| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 1 | Validate voicemail-only Quo line costs | Matthew | P0 | Open |
| 2 | Test Quo contact handling (new vs existing contacts) | Trent | P1 | Open |
| 3 | Document current Vonage IVR menu options to replicate | Team | P1 | Open |
| 4 | Research if Quo can route based on contact status | Trent | P1 | Open |

### Process Design
| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 5 | Define Jobber Request lifecycle (how to mark "done") | Matthew | P1 | Open |
| 6 | Draft SOP for Alyssa's Request queue processing | Matthew | P2 | Open |

---

## Before Number Porting

| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 7 | Complete Quo IVR configuration | Team | P0 | Blocked |
| 8 | Test all routing scenarios | Team | P0 | Blocked |
| 9 | Coordinate Vonage 2FA access with Kelsey | Matthew | P1 | Open |
| 10 | Confirm no Vonage data export needed | Matthew | P2 | Open |

---

## Backlog (Phase 2 Prep)

| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 11 | Investigate ChatGPT → Jobber integration as backup | Matthew | P3 | Backlog |
| 12 | Research Sona voice agent scripts for client calls | Team | P3 | Backlog |
| 13 | Scope "suggested updates" automation for Request processing | Matthew | P3 | Backlog |

---

## Key Decisions Made

1. **Phase 1 = Routing only** (no Sona credits)
2. **Email automation stays deprioritized**
3. **Manual processing preferred** over risky automated updates
4. **Voicemail-only line is primary** for UC-1, ChatGPT is backup
5. **System must be ready BEFORE** initiating number port

---

## Notes for Nikki Interview (Tomorrow)

Chris has stakeholder interview questions to review before meeting with Nikki. Key things to confirm:
- Does Nikki take client calls? (Determines if she needs Quo line)
- What's her current workflow with Jobber?
- Any communication pain points specific to her role?
