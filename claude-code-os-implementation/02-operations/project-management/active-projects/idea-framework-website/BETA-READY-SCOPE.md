# Beta Ready Scope - $1000 (PAID)

**Status:** IN PROGRESS (~75% complete)
**Payment:** $1000 received
**Deadline:** Before Trevor travels (Dec 25)
**Last Updated:** Dec 25, 2025

---

## Trevor's Success Criteria (Dec 12)

> "The criteria that says it's ready for beta is that all the inputs end up on the same document."

**Beta Ready = Single consolidated output document that captures all user inputs**

---

## BETA READY SCOPE (Agreed - $1000)

### 1. Single Consolidated Output Document (PRIMARY)
**Source:** Dec 12 meeting - Trevor's explicit success criteria
**Status:** CODE COMPLETE - NEEDS TESTING

- [x] All Avatar Builder inputs compiled into export
- [x] All Brand Canvas data included
- [x] Copy Generator outputs included (if used)
- [x] Brand Coach conversation insights included (up to 10 recent)
- [x] Single "Download Complete Report" button (PDF + Markdown options)
- [ ] Clean, text-based formatting (no logo issues) - **STILL HAS LOGO**

**Implementation:**
- `src/components/export/BrandCanvasPDFExport.tsx` - PDF generation
- `src/components/export/BrandMarkdownExport.tsx` - Markdown export
- `src/components/export/templates/BrandStrategyTemplate.ts` - Document orchestrator
- Supabase edge function: `generate-brand-strategy-document`

**NEEDS:** Re-test outputs to verify quality. Option to remove logo from exports.

---

### 2. UI Polish for Beta
**Source:** Dec 12 meeting action items
**Status:** PARTIALLY COMPLETE

- [ ] Fix widow on "Strategic Brand Building Journey" headline - **NOT DONE**
- [x] Remove Diagnostic from post-login nav bar - **DONE** (showInNav: false)
- [ ] Add support email link (contact@ideabrandconsultancy.com) - **NOT DONE**
- [ ] Consistent text-only exports (remove stretched logo) - **NOT DONE**

**Remaining Work:**
1. Add CSS text-balance or manual line break to headline (`src/pages/Index.tsx:128`)
2. Add support email to Start Here page or footer
3. Add option for text-only exports without logo

---

### 3. Reinstate Strategic Brand Building Journey Page
**Source:** Dec 12 meeting - Trevor realized this context was lost
**Status:** COMPLETE

- [x] Bring back IDEA framework explanation page
- [x] Position as home/landing after login (route: `/journey`)
- [x] Video placeholder ready for Trevor's content (Vimeo: 1145686648)

**Location:** `src/pages/Index.tsx` with feature config in `src/config/features.ts`

---

### 4. Collapsible Video Component
**Source:** Dec 12 meeting action items
**Status:** MOSTLY COMPLETE

- [x] Build collapse/expand functionality
- [ ] Add transcript view with copy button - **NOT IMPLEMENTED**
- [x] Place on: Start Here (Journey page)
- [x] Place on: Brand Canvas

**Implementation:** `src/components/CollapsibleVideo.tsx`
- Collapse/expand with localStorage persistence
- Supports YouTube and Vimeo
- Missing: Transcript view (Trevor would need to provide transcripts)

---

### 5. Hook Knowledge Base to AI
**Source:** Dec 19 meetings - AI outputs are generic without context
**Status:** CODE COMPLETE - NEEDS TESTING

- [x] System knowledge base infrastructure built (`src/lib/knowledge-base/`)
- [x] Document upload and processing (`document-processor` function)
- [x] OpenAI vector store integration (`sync-to-openai-vector-store`)
- [x] RAG implementation with embeddings
- [ ] **Verify Trevor's book PDF is actually uploaded and indexed**
- [ ] **Test that AI outputs reference book content**

**NEEDS:** Verification that book is in knowledge base and AI is pulling from it.

---

### 6. Brand Canvas AI Suggestions Fix
**Source:** Dec 19 Meeting 3 & 4 - Core functionality broken
**Status:** CODE COMPLETE - NEEDS TESTING

- [x] "Get AI Suggestions" generates actual content (8 field-specific prompts)
- [ ] Add Accept/Reject buttons for AI-generated content - **NOT IMPLEMENTED** (suggestions auto-apply)
- [x] AI pulls from Avatar data + user knowledge base (full context sent)

**Implementation:** `src/components/AIAssistant.tsx`
- 8 AIAssistant instances in BrandCanvas.tsx (one per field)
- Context-aware prompts for: purpose, vision, mission, values, positioning, valueProposition, personality, voice

**NEEDS:** Re-test to verify outputs are context-aware, not generic. Accept/Reject UI is a nice-to-have.

---

## Progress Summary

| Item | Status | % Complete |
|------|--------|------------|
| 1. Consolidated Output | Code Complete | 90% (test outputs, logo option) |
| 2. UI Polish | Partial | 25% (3 items remaining) |
| 3. Journey Page | Complete | 100% |
| 4. Collapsible Video | Mostly Complete | 80% (no transcript view) |
| 5. Knowledge Base + AI | Code Complete | 90% (verify book indexed) |
| 6. AI Suggestions | Code Complete | 85% (test quality, no accept/reject) |

**Overall: ~75% complete**

---

## REMAINING WORK FOR BETA

### Must Do (Critical for Beta)
1. **Test consolidated output document** - Verify all data sources appear correctly
2. **Test AI suggestions on Brand Canvas** - Verify context-aware, not generic
3. **Verify Trevor's book is in knowledge base** - Check if uploaded/indexed

### Should Do (Polish)
4. Fix widow on headline (CSS text-balance or line break)
5. Add support email to Start Here page
6. Add text-only export option (remove logo)

### Nice to Have (Can defer)
7. Transcript view for videos (requires Trevor's transcripts)
8. Accept/Reject UI for AI suggestions

---

## EXPLICITLY DEFERRED TO PHASE 3 (NOT in $1000)

These are good ideas discussed but NOT part of beta ready scope:

| Item | Source | Why Deferred |
|------|--------|--------------|
| Multi-brand selector dropdown | Dec 19 Meeting 1 | New feature, scope creep |
| Document pre-fill from uploads | Dec 12 | Complex feature |
| Comma-separated value parsing | Dec 12 | Nice-to-have |
| AI Assistant for decision factors | Dec 12 | Nice-to-have |
| OpenAI/ChatGPT user-context integration | Dec 12 | Research item |
| Stripe payment integration | Original roadmap | Phase 4 |
| Training video library | Original roadmap | Trevor's content |
| Beta tester questionnaire | Original roadmap | Product work |
| Cost analysis | Original roadmap | Business work |

---

## Key Quotes from Meetings

### Dec 12 - Success Criteria
> "The criteria that says it's ready for beta is that all the inputs end up on the same document."

### Dec 19 Meeting 1 - Focus
> "I don't want to add any more features, Matt... less is more for this, but what is there has to actually work."

### Dec 19 Meeting 2 - Minimum Bar
> "I don't mind if that Canvas output is just a text document... so long as it captures the various stages of the process and puts them all in one place."

### Dec 19 Meeting 3 - AI Problem
> "The 'Get AI Suggestions' button provides generic instructions... not a specific output for the user's brand."

### Dec 19 Meeting 4 - Root Cause
> "The AI lacks access to the user's brand context... it just gives me generic BS."

---

## Definition of Done

Beta is ready when:
1. [x] User can go through Avatar 2.0 → Brand Canvas → Brand Coach flow
2. [ ] All inputs from that journey appear in a single downloadable document - **TEST**
3. [ ] AI suggestions produce context-aware content (not generic) - **TEST**
4. [ ] UI is polished (no confusing nav, support email added, no widows) - **PARTIAL**
5. [x] Strategic Brand Building Journey page reinstated with video placeholder

---

## Next Actions

1. **Test consolidated output** - Export document and verify all sections populated
2. **Test AI suggestions** - Try "Generate with AI" on Brand Canvas fields
3. **Verify book in KB** - Check if Trevor's book PDF is indexed
4. **Quick UI fixes** - Headline widow, support email (30 min)

---

**Remember:** Every "good idea" that comes up goes to Phase 3. Beta = working basics, not perfect features.
