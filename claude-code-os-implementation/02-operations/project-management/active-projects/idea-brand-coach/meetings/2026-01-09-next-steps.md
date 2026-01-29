# Next Steps - January 9, 2026 Sync Calls

**Source:** Jan 9 Part 1 + Part 2 meetings with Trevor
**Goal:** Get app to beta testers with usable strategy document output

---

## Matt's Action Items

### Critical for Beta (Do First)

1. **Fix Interactive Insights UI**
   - Fix truncated "current content" display (can't scroll)
   - Port accept/reject pattern from Canvas to Insights
   - Wire Insights AI to pull from Avatar 2.0 data and embeddings
   - Add dynamic prompts based on Avatar inputs
   - [Clip](https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe?timestamp=487.9999)

2. **Journey Page for Beta**
   - Propose beta-friendly experience: hide/disable non-functional modules (Distinctive, Empathetic, Authentic) with "coming soon" labels OR remove entirely
   - Share proposal with Trevor for feedback
   - [Clip](https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe?timestamp=1713.9999)

3. **Re-enable Beta Test Pages**
   - Re-add Beta Test to app menu
   - Configure to open in new tab alongside app
   - Update routes: `/beta-journey`, `/beta-feedback`
   - [Clip](https://fathom.video/share/avhrhbZs_ZdGnX19UKagbzPLGCiDeui3?timestamp=1811.9999)

### Important (Do Next)

4. **Cost Model & Safeguards**
   - Document token + storage cost assumptions
   - Define scaling thresholds
   - Implement usage limits/free-tier caps for beta
   - Review with coaches before sending to Trevor
   - [Clip](https://fathom.video/share/avhrhbZs_ZdGnX19UKagbzPLGCiDeui3?timestamp=1311.9999)

5. **Post-process Trevor's videos into SOP**
   - Once Trevor creates module walkthrough videos, generate written guide for beta testers

### Deferred (Post-Beta)

- PDF heading color change (blue → black or brand colors)
- Google Drive knowledge base integration
- Contextual coach widget (Trevor avatar)
- Heavy UI investments (wait for dynamic UI landscape to settle)

---

## Trevor's Action Items

### Critical for Beta

1. **Deep-dive App Review**
   - Test end-to-end with a fresh project
   - Start from Avatar 2.0 → Insights → Canvas → PDF export
   - Provide specific feedback on document quality and content specificity
   - Send feedback to Matt
   - [Clip](https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe?timestamp=126.9999)

2. **Beta Test Journey Copy**
   - Use Lovable chat to propose updated tester prompts/questions per module
   - Review copy against each module as it exists now
   - Share output with Matt (do NOT directly edit app)
   - [Clip](https://fathom.video/share/avhrhbZs_ZdGnX19UKagbzPLGCiDeui3?timestamp=1811.9999)

3. **Module Walkthrough Videos**
   - Create brief (3-4 min) AI avatar videos for each module
   - Include screenshots showing copy-paste workflow into Brand Coach chat
   - Explain that some modules are "learning only" for beta (no input fields)
   - Culminate in strategy document export

### Review/Approve

4. **Review Matt's Journey Page Proposal**
   - Weigh in on whether to hide, label, or remove non-functional modules

---

## Shared Understanding

### Beta Philosophy
- **Occam's razor:** Simplest solution, reduce scope, avoid throwaway work
- **Output quality > UI polish:** Focus on producing usable strategy documents
- **Defer heavy UI:** Dynamic UI generation (Google GenTabs/Disco) may obsolete bespoke builds
- **Chat is anchor:** Voice/text interaction with LLM expected to remain constant

### What Beta Testers Get
1. Avatar 2.0 → Interactive Insights → Brand Canvas → Brand Coach flow
2. Single downloadable strategy document (PDF)
3. Video walkthroughs explaining each module
4. Structured feedback journey (opens in new tab)
5. Option to record Loom feedback OR fill short form

### Explicitly NOT for Beta
- Multi-brand selector
- Google Drive knowledge base ingestion
- Embedded feedback fields per feature
- Perfect branding/styling
- Payment/credits system (just usage caps)

---

## Timeline

| Who | Task | Target |
|-----|------|--------|
| Matt | Insights UI fixes + accept/reject | Now (no blocker) |
| Trevor | Deep-dive testing + feedback | This weekend |
| Trevor | Beta journey copy via Lovable chat | This weekend |
| Matt | Journey page proposal | After Trevor feedback |
| Matt | Re-enable beta test pages | After copy from Trevor |
| Matt | Cost model documentation | Before beta launch |
| Trevor | Module walkthrough videos | Before beta launch |
| Both | Beta launch | ASAP after above complete |
