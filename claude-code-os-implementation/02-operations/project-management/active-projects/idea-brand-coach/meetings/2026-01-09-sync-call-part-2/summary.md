# Sync Call Part 2 - January 9, 2026

## Idea Brand Coach - Trevor

### Summary

Impromptu Google Meet Meeting - January 09
VIEW RECORDING: https://fathom.video/share/avhrhbZs_ZdGnX19UKagbzPLGCiDeui3

**Meeting Purpose:**
Align on near-term UX approach, cost controls, and beta feedback workflow for the brand strategy app while avoiding over-building UI amid rapid LLM/UI shifts.

---

## Issues & Tickets

### 1. Low-functionality modules and interim UX

**Context:** Some modules provide guidance and action steps but lack adjacent input tools/fields.

**Status:** Modules currently show instructions without capture mechanisms; chat exists separately.

**Concerns, Challenges, and Blockers:**
- Risk of user confusion when action prompts lack input fields
- Building forms now may be wasted effort given emerging dynamic UIs

**Ideas and Explanations:**
- Use short avatar/talking-head videos per module to teach workflow
- Recommend copy-paste into chat/brand coach as a temporary "workaround" to progress

**Decisions and Next Steps:**
- Trevor to create brief module videos (3–4 min) with screenshots explaining copy-paste workflow. **Owner: Trevor**
- Keep existing structure; do not add new form inputs at this phase. **Owner: Matt**

**Current Objective:** Preserve learning value; enable progress via chat while deferring heavier UI build.

---

### 2. Future UI direction (dynamic/generated UI)

**Context:** Discussion of Google GenTabs/"Disco" dynamic UI generation and implications.

**Status:** Awareness raised; no immediate integration.

**Concerns, Challenges, and Blockers:**
- Building bespoke UI now may date quickly
- Unclear path to implement dynamic UI yet

**Ideas and Explanations:**
- Focus on robust inputs/outputs via chat/voice; keep a chat widget accessible across modules
- Consider user-customizable learning modalities (video, images, text) later

**Decisions and Next Steps:**
- Defer heavy UI investments; optimize chat and content quality first. **Owner: Matt**
- Matthew to keep exploring labs; inform future iterations. **Owner: Matt**

**Current Objective:** Anchor on LLM interaction (voice/text) and avoid over-committing to fixed UI.

---

### 3. Document upload, storage, and costs

**Context:** Users can upload docs; Matthew tested Trevor's doc; storage spans local state, Supabase, and OpenAI vector store.

**Status:** Working; per-user vectorization in OpenAI; basic UI to view/delete uploads exists.

**Concerns, Challenges, and Blockers:**
- Uncertain ongoing costs (token usage, storage) at scale; risk of surprise bills
- Large-context prompts can spike costs without retrieval optimization

**Ideas and Explanations:**
- Credit-based pricing tiers (free, paid) with usage caps
- Retrieval engineering to minimize tokens and avoid packing whole PDFs

**Decisions and Next Steps:**
- Matthew to produce a cost model/plan: token + storage assumptions, scaling, thresholds, and safeguards for beta. **Owner: Matt**
- Implement usage limits/free-tier caps to prevent overages during beta. **Owner: Matt**

**Current Objective:** Quantify and cap costs; design pricing/credits aligned to LLM and storage usage.

---

### 4. Beta testing feedback flow

**Context:** Prior beta pages exist (tester registration, journey, feedback) but are outdated; earlier separate Google Sheets were clunky.

**Status:** Beta menu item was removed/archived; content needs revision to current app.

**Concerns, Challenges, and Blockers:**
- Friction collecting actionable feedback; dev cost of placing fields beside each tool
- Tester fatigue with long forms; risk of low-quality feedback

**Ideas and Explanations:**
- Re-enable a simple in-app Beta Test entry that opens a structured feedback journey in a new tab
- Encourage screen+voice capture (e.g., free Loom 5-min segments); also offer a short, structured questionnaire
- Use Lovable chat to draft updated beta journey/questions per module

**Decisions and Next Steps:**
- Re-add Beta Test to app menu (opens journey/feedback in new tab). **Owner: Matt**
- Trevor to use Lovable chat to propose updated tester prompts/journey; then review copy vs. each module; share with Matthew. **Owner: Trevor**
- Provide multi-path feedback options: Loom recording and concise form; avoid per-feature embedded fields for now. **Owner: Both**

**Current Objective:** Lower friction, gather high-signal feedback quickly, and iterate to "beta-ready."

---

### 5. App viability and competitive positioning

**Context:** Trevor asked if current app is competitive; Matthew emphasized quality of outputs over perfect UI during beta.

**Status:** Chat is usable but siloed from lessons; potential for a companion/widget approach later.

**Concerns, Challenges, and Blockers:**
- Disjointed experience between learning modules and chat
- Market moving quickly; risk of staleness

**Ideas and Explanations:**
- Focus beta on ensuring strong outputs and clear path to brand strategy document
- Transparently communicate "beta" status and rapid iteration intent

**Decisions and Next Steps:**
- Prioritize output quality testing and guidance clarity in beta plan. **Owner: Both**
- Consider integrated chat widget in future pass based on feedback. **Owner: Matt**

**Current Objective:** Validate value via output quality; refine UX post-feedback.

---

## Other & Incidental Topics

**Occam's razor as product principle:** Emphasis on reducing/simplifying scope to ship faster and avoid throwaway work.

**Voice as primary interaction:** Matthew favors voice for speed; grounding interactions in voice/text expected to remain constant.

**Lovable usage boundaries:** Trevor to avoid direct edits; will use Lovable chat for suggestions; Matthew prefers Claude Code for reliability.

**Fathom meeting link follow-up:** Matthew to send Fathom recording link post-call.

---

## Action Items Summary

| Action | Owner | Clip |
|--------|-------|------|
| Draft cost/scaling plan for AI tokens + storage; review w/ coaches; send to Trevor | Matt | [Watch](https://fathom.video/share/avhrhbZs_ZdGnX19UKagbzPLGCiDeui3?timestamp=1311.9999) |
| Re-enable Beta Test pages; add menu link; open in new tab; then Trevor update copy via Lovable chat | Matt/Trevor | [Watch](https://fathom.video/share/avhrhbZs_ZdGnX19UKagbzPLGCiDeui3?timestamp=1811.9999) |
| Send Fathom recording link to Trevor | Matt | [Watch](https://fathom.video/share/avhrhbZs_ZdGnX19UKagbzPLGCiDeui3?timestamp=2456.9999) |
