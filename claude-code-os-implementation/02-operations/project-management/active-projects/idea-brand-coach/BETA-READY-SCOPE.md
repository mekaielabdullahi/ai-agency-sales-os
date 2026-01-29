# Beta Ready Scope - $1000 (PAID)

**Status:** IN PROGRESS (~80% complete)
**Payment:** $1000 received
**Last Updated:** January 9, 2026

---

## Beta Success Criteria (Updated Jan 9)

> "The criteria that says it's ready for beta is that all the inputs end up on the same document."
> — Trevor, Dec 12

> "As long as it produces good outputs, that's the core value add... communicate that we're refining this tool, it's not 100% ready."
> — Matt, Jan 9

**Beta Ready = Usable strategy document output + clear user flow + feedback mechanism**

---

## BETA READY SCOPE

### 1. Single Consolidated Output Document (PRIMARY)
**Status:** CODE COMPLETE - AWAITING TREVOR'S FRESH TEST

- [x] All Avatar Builder inputs compiled into export
- [x] All Brand Canvas data included
- [x] Copy Generator outputs included (if used)
- [x] Brand Coach conversation insights included
- [x] Single "Download Complete Report" button (PDF + Markdown)
- [x] PDF formatting clean and presentable
- [ ] **NEEDS:** Trevor to test with fresh project and report on content quality

**Decision (Jan 9):** Blue headings are off-brand but acceptable for beta. Defer styling to post-beta.

---

### 2. Interactive Insights Module Fix (NEW - Jan 9)
**Status:** NEEDS WORK

**Problems Identified:**
- Duplicates data entry from Avatar 2.0 (confusing user flow)
- "Get AI Suggestions" produces instructions, not content
- Truncated "current content" display (can't scroll)
- Inconsistent UX vs Canvas accept/reject pattern

**Required Fixes:**
- [ ] Fix truncated content UI and scrolling
- [ ] Wire module to pull data from Avatar 2.0
- [ ] Add dynamic prompts based on Avatar inputs
- [ ] Port accept/reject pattern from Canvas
- [ ] Standardize on "Get AI Help" button

**Framing:** Avatar 2.0 = high-level initial builder; Insights = deeper dive with context-aware prompts

---

### 3. Journey Page Scope for Beta
**Status:** DECISION PENDING

**Current State:** Diagnostic and Insights active; Distinctive/Empathetic/Authentic are non-functional placeholders (Phase 2).

**Options:**
1. Hide inactive sections with "coming soon" labels
2. Remove inactive sections entirely for beta
3. Keep as-is with video explanation

**Action:** Matt to propose approach; Trevor to approve.

---

### 4. Beta Testing Feedback Flow (NEW - Jan 9)
**Status:** NEEDS RE-ENABLING

**Prior State:** Beta test pages exist but archived; Google Sheets was clunky.

**Required:**
- [ ] Re-add Beta Test to app menu
- [ ] Opens in new tab alongside app
- [ ] Trevor to update copy via Lovable chat (NOT direct edits)
- [ ] Multi-path feedback: Loom recording OR short form
- [ ] Avoid per-feature embedded fields (too much dev cost)

---

### 5. Onboarding Videos
**Status:** TREVOR'S TASK

- [ ] Trevor creates brief (3-4 min) AI avatar videos per module
- [ ] Screenshots showing copy-paste workflow into Brand Coach
- [ ] Explains "learning only" modules for beta
- [ ] Culminates in strategy document export
- [ ] Matt post-processes into written SOP

---

### 6. Cost Model & Usage Caps (NEW - Jan 9)
**Status:** NEEDS DOCUMENTATION

**Concerns:**
- Token usage costs at scale
- OpenAI vector store storage costs
- Risk of surprise bills during beta

**Required:**
- [ ] Document token + storage cost assumptions
- [ ] Define scaling thresholds
- [ ] Implement free-tier caps for beta
- [ ] Review with coaches before finalizing

---

### 7. Previously Completed Items

- [x] Strategic Brand Building Journey page reinstated
- [x] Collapsible video component (collapse/expand, localStorage persistence)
- [x] Diagnostic removed from post-login nav
- [x] Avatar renamed to "Avatar 2.0"
- [x] Knowledge base infrastructure (Supabase + OpenAI vector store)
- [x] Document upload with view/delete UI

---

## Progress Summary

| Item | Status | % Complete |
|------|--------|------------|
| 1. Consolidated Output Document | Awaiting Test | 95% |
| 2. Interactive Insights Fix | Needs Work | 30% |
| 3. Journey Page Decision | Pending | 50% |
| 4. Beta Feedback Flow | Needs Re-enable | 40% |
| 5. Onboarding Videos | Trevor's Task | 0% |
| 6. Cost Model | Needs Doc | 0% |
| 7. Prior Completed | Done | 100% |

**Overall: ~80% complete** (up from 75% - PDF now presentable)

---

## EXPLICITLY DEFERRED

| Item | Why Deferred |
|------|--------------|
| PDF heading colors (blue → black) | Post-beta polish |
| Google Drive knowledge base | Evaluate after Trevor testing |
| Multi-brand selector | Phase 2 feature |
| Contextual coach widget (Trevor avatar) | Future vision |
| Heavy UI investments | Dynamic UI landscape shifting |
| Payment/Stripe integration | Phase 4 |
| Per-feature feedback fields | Dev cost too high |

---

## Key Principles (Jan 9)

1. **Occam's Razor:** Simplest solution, reduce scope, ship faster
2. **Output Quality > UI Polish:** Usable strategy doc is the value
3. **Defer Heavy UI:** Google GenTabs/Disco may obsolete bespoke builds
4. **Chat is Anchor:** Voice/text LLM interaction stays constant
5. **Beta = Learning:** Communicate we're iterating, collect feedback

---

## Immediate Next Actions

### Matt
1. Fix Interactive Insights UI (truncate/scroll + accept/reject)
2. Wire Insights to pull from Avatar 2.0
3. Propose Journey page approach for beta
4. Re-enable Beta Test pages after Trevor's copy

### Trevor
1. Deep-dive test with fresh project → feedback to Matt
2. Draft beta journey copy via Lovable chat
3. Create module walkthrough videos

---

## Definition of Done (Updated)

Beta is ready when:
1. [x] User can go through Avatar 2.0 → Insights → Canvas → Brand Coach flow
2. [ ] All inputs appear in single downloadable document - **TREVOR TESTING**
3. [ ] Interactive Insights pulls from Avatar 2.0 (no duplication) - **MATT FIXING**
4. [ ] AI suggestions use accept/reject pattern consistently - **MATT FIXING**
5. [ ] Journey page shows only functional modules - **DECISION PENDING**
6. [ ] Beta feedback mechanism re-enabled - **AFTER TREVOR COPY**
7. [ ] Module walkthrough videos available - **TREVOR CREATING**
8. [ ] Usage caps in place to prevent cost overruns - **MATT DOC**

---

**Remember:** Every "good idea" goes to Phase 2/3. Beta = working basics + feedback mechanism.
