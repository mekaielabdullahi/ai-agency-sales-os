# Sync Call Part 1 - January 9, 2026

## Idea Brand Coach - Trevor

### Summary

Impromptu Zoom Meeting - January 09
VIEW RECORDING: https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe

**Meeting Purpose:**
Align on readiness for beta: connect Avatar 2.0 → Interactive Insights → Canvas → PDF export; decide AI assist UX (help vs suggestions), and identify must-do fixes to get a usable strategy document in testers' hands.

---

## Issues & Tickets

### 1. Knowledge Base Integration (Avatar 2.0 → Insights → Document)

**Context:** Team discussed ensuring data entered in Avatar 2.0 powers Interactive Insights and downstream chat/document outputs; avoid duplicate entry.

**Status:** Avatar 2.0 content is saved to Supabase and embedded to vector store; Insights fields now mapped to chat and export. Google Drive knowledge base folder not yet hooked up.

**Concerns, Challenges, and Blockers:**
- Potential duplication between Avatar 2.0 and Insights; unclear user flow
- Uncertain if Insights currently pulls from Avatar 2.0 for AI suggestions
- Google Drive knowledge base ingestion not implemented

**Ideas and Explanations:**
- Treat Avatar 2.0 as high-level "initial builder," Insights as deeper dive, with copy that references prior selections (e.g., buyer intent)
- Dynamic prompts in Insights based on Avatar inputs

**Decisions and Next Steps:**
- Trevor to test end-to-end with a fresh project and provide specific feedback on document quality. **Owner: Trevor**
- Matt to verify and, if needed, wire Insights AI to pull from Avatar 2.0 data and embeddings. **Owner: Matt**
- Evaluate priority and approach to connect Google Drive knowledge base; decide after Trevor's testing. **Owner: Matt**

**Current Objective:** Single-source-of-truth flow where Avatar inputs populate Insights and inform AI generation for chat and strategy doc.

---

### 2. AI Assist UX: "Get AI Help" vs "Get AI Suggestions"

**Context:** Two current buttons create confusion; Canvas has accept/reject UX that's preferred.

**Status:** Canvas has accept/reject for AI suggestions. Insights still uses instruction-style suggestions; not content generation. Some suggestion outputs appear deterministic.

**Concerns, Challenges, and Blockers:**
- Fragmented UX; users copy-paste to Brand Coach chat to get leverage
- "Get AI suggestions" doesn't generate directly applicable content
- Truncated "current content" display in Insights (can't scroll)

**Ideas and Explanations:**
- Consolidate to "Get AI Help" with accept/reject flow identical to Canvas
- Future: side "coach" widget that knows context (section-aware), optionally branded as Trevor's avatar; iterative, ChatGPT-like prompts

**Decisions and Next Steps:**
- Standardize on "Get AI Help"; port accept/reject pattern to Insights. **Owner: Matt**
- Fix truncated current content UI and scrolling. **Owner: Matt**
- Long-term: explore contextual coach widget; not for beta. **Owner: Matt (design spike later)**

**Current Objective:** Provide in-place, section-aware AI assistance that generates content suggestions users can accept/reject.

---

### 3. Strategy Document / PDF Export Quality

**Context:** PDF output recently improved; brand styling secondary to content for beta.

**Status:** PDF now clean/presentable; headings currently blue (off brand). Content was generic in prior test due to older inputs.

**Concerns, Challenges, and Blockers:**
- Off-brand color headings (blue); minor
- Content quality hinges on updated knowledge base and fresh run

**Ideas and Explanations:**
- For beta, prioritize usable content over polished branding; defer visual tweaks

**Decisions and Next Steps:**
- Defer color/styling changes to post-beta polish list; option to switch to black headings later. **Owner: Matt**
- Trevor to run a fresh project with updated pipeline and assess content specificity. **Owner: Trevor**

**Current Objective:** Export a clear, usable strategy document that reflects Avatar/Insights inputs; visual polish later.

---

### 4. Journey Page Scope for Beta

**Context:** Journey landing page shows Diagnostic and Insights active; Distinctive/Empathetic/Authentic are largely non-functional (phase 2).

**Status:** Live but partially non-functional; risk of user confusion.

**Concerns, Challenges, and Blockers:**
- Non-functional modules may confuse beta users and dilute perceived value

**Ideas and Explanations:**
- Consider removing or hiding inactive sections for beta, or clearly labeling as "coming soon"

**Decisions and Next Steps:**
- Matt to propose a beta-friendly Journey experience (hide/disable with clear labels vs remove). **Owner: Matt**
- Trevor to weigh in after seeing proposal. **Owner: Trevor**

**Current Objective:** A coherent beta flow surfacing only functional modules to minimize confusion.

---

### 5. Onboarding/Instructions (Video + SOP)

**Context:** Need lightweight guidance for beta testers; discussion of Loom vs AI avatar videos.

**Status:** Trevor prefers AI-generated avatar videos for speed and consistency; Loom SOP generator may be paid-only.

**Concerns, Challenges, and Blockers:**
- Time cost of manual Loom recordings

**Ideas and Explanations:**
- Ship short AI avatar walkthrough videos; generate written SOP from those via AI later

**Decisions and Next Steps:**
- Trevor to create brief module walkthrough videos culminating in document export. **Owner: Trevor**
- Post-process videos into a simple written guide for beta. **Owner: Matt**

**Current Objective:** Provide just-enough onboarding to enable smooth beta usage.

---

## Other & Incidental Topics

**Holiday catch-up and availability:** Light personal updates; Trevor had limited connectivity over holidays, now catching up and will deep-dive over the weekend.

**Branding/personal coach concept:** Future idea: in-app "Trevor" coach (HeyGen/ElevenLabs) to guide users contextually; strong personal brand leverage for later phases.

---

## Action Items Summary

| Action | Owner | Clip |
|--------|-------|------|
| Deep-dive app/code review; send feedback to Matt | Trevor | [Watch](https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe?timestamp=126.9999) |
| Fix Interactive Insights UI: truncate/scroll + accept/reject; then wire Avatar 2.0 + dynamic prompts | Matt | [Watch](https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe?timestamp=487.9999) |
| Decide Journey page for beta; if kept, add placeholder text | Matt | [Watch](https://fathom.video/share/eFMC8aNnU3TuSk8dVTNCRovmjLPJRtxe?timestamp=1713.9999) |
