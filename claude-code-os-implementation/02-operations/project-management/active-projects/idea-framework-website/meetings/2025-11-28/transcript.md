# IDEA Framework Website - November 28, 2025 Meeting Transcript

**Recording:** https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH
**Duration:** 85 minutes
**Attendees:** Matthew Kerns, client Bradford

---

## Meeting Summary

Phase 1 demo completed. Payment processing (bank transfer, 2-3 day delay expected). Scoped Phase 2 work (chat sessions, PDF improvements, privacy updates). Discussed beta testing flow and paywall strategy. Identified Phase 3 features (training videos, document upload, monetization).

---

## Key Decisions

| Decision | Owner | Status |
|----------|-------|--------|
| Phase 1 payment via bank transfer (2-3 days) | client | Pending |
| Merge Phase 1 changes after payment received | Matt | Pending payment |
| Phase 2 scope: Chat sessions + PDF + Privacy | Matt | Agreed |
| PDF output: Simple, markdown format, no logo | Both | Agreed |
| Training videos: External hosting with links (not embedded) | Both | Agreed for Phase 1 |
| Beta paywall: Show page, no actual payment processing | Matt | Build for Phase 2 |
| Lovable subscription: Research pause/cancel policy | Matt | Action required by Dec 1 |
| Document upload: After diagnostic, system knowledge base | Both | Phase 3 |
| Pricing model: Subscription (not one-time payment) | client | TBD (beta feedback) |

---

## Action Items (Extracted from Fathom)

### Administrative (Pre-Phase 2)
1. **Pay Matt via new link; then Matt merges Phase 1** - [5:13](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=312.9999)
   - **Owner:** Client
   - **Status:** Pending (bank transfer, 2-3 days)
   - **Next:** Matt merges after payment confirmation

2. **Confirm Lovable cancellation/pause policy; WhatsApp client by Dec 1** - [33:28](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2020.9999)
   - **Owner:** Matt
   - **Deadline:** Before Dec 1 (renewal date)
   - **Context:** Subscription renews Monday, Dec 1; lots of unused credits

3. **Send Fathom recording link to client** - [36:36](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2197.9999)
   - **Owner:** Matt
   - **Status:** Complete (in progress)
   - **Purpose:** client needs notes for reference

---

### Phase 2 Work Items ($500)

4. **Test Phase 1 end-to-end; start new brand** - [21:48](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=1303.9999)
   - **Owner:** Matt (with client testing after)
   - **Scope:** New user flow, diagnostic → auth → chat
   - **Estimate:** 2 hours testing + fixes
   - **Context:** client will test over weekend after Phase 1 merge

5. **Improve Canvas PDF export w/ Markdown; remove logo; test** - [38:47](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2317.9999)
   - **Owner:** Matt
   - **Scope:** Markdown formatting, remove broken logo, improve layout
   - **Estimate:** 2-3 hours (timeboxed)
   - **Context:** Current PDF quality is "crappy", needs tidier output

6. **Update privacy statement across instances** - [39:21](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2369.9999)
   - **Owner:** Matt
   - **Scope:** Find all privacy instances, get updated text from client, apply consistently
   - **Estimate:** 1 hour
   - **Locations:** Footer, auth modal, settings, legal pages

7. **Finish chat sessions feature; add history/title/expand; test** - [1:19:07](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=4770.9999)
   - **Owner:** Matt
   - **Status:** ~90% complete (shown in demo)
   - **Remaining:** Expand functionality, full testing
   - **Estimate:** 2-3 hours
   - **Context:** Chat history sidebar shown, auto-title working, needs polish

---

### Phase 3 Work Items (Likely $1000)

8. **Research Gamma/Google Docs for Canvas export; report to client** - [26:39](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=1599.9999)
   - **Owner:** Matt
   - **Scope:** Evaluate Gamma API vs Google Docs for professional PDF output
   - **Estimate:** Research (2 hours) + implementation (4-6 hours)
   - **Context:** Gamma produces professional presentations, Google Docs is simpler/cheaper

9. **Draft NotebookLM prompts for brand doc pre-fill** - [40:52](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2452.9999)
   - **Owner:** Matt
   - **Scope:** Create prompts for users to pre-fill diagnostic data from existing documents
   - **Estimate:** 3-4 hours (prompt design + testing)
   - **Context:** Higher sellers won't want to type everything manually

10. **Prototype training video UI (link vs embed); send client demo video** - [45:28](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2731.9999)
    - **Owner:** Matt
    - **Scope:** Test external link vs embedded video, show client options
    - **Estimate:** 1 hour prototype + demo
    - **Context:** client has ElevenLabs + HeyGen videos ready, needs hosting solution
    - **Decision:** External links preferred for MVP (simpler)

11. **Build beta paywall page; enable free-tier upgrade; embed client's upsell video** - [1:01:46](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=3695.9999)
    - **Owner:** Matt
    - **Scope:** Paywall page UI, upgrade flow (no Stripe integration for beta), embedded upsell video
    - **Estimate:** 6-8 hours
    - **Context:** Beta testers bypass payment but see full flow

12. **Draft beta tester questionnaire incl. pricing feedback** - [1:04:10](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=3852.9999)
    - **Owner:** Client
    - **Scope:** Questionnaire to gather feedback on pricing, features, UX
    - **Estimate:** 2-3 hours
    - **Context:** Need to determine subscription pricing (Client unsure on $97 vs other)

13. **Provide client monthly hosting/AI cost estimates** - [1:10:25](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=4257.9999)
    - **Owner:** Matt
    - **Scope:** Estimate monthly costs (hosting, AI compute, tools) for 100-500 users
    - **Estimate:** 1-2 hours analysis
    - **Context:** client needs to understand burn rate to price subscription

14. **Schedule coach review of client's project** - [1:17:02](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=4637.9999)
    - **Owner:** Matt
    - **Scope:** Present project to development coach for product viability feedback
    - **Estimate:** External meeting
    - **Context:** Matt has access to coaching network, wants expert feedback

---

## Technical Discussion Notes

### Brand Coach GPT - Knowledge Base Strategy
**Context:** [9:48 - 20:40]

**Current State:**
- Using OpenAI Responses API (between ChatGPT and OpenAI base)
- User knowledge base implemented (diagnostic data stored as vectors)
- No system knowledge base yet

**client's Concern:**
- Custom GPT has 2 years of training + uploaded documents
- Worried about hallucinations without defined knowledge base
- Wants to ensure outputs align with IDEA Framework

**Decision:**
- Build system knowledge base (Matt's job)
- Don't redirect to custom GPT (loses control, siloed)
- Keep Brand Coach page (more personal, less "just another GPT")
- Future: Add personalized training based on user interactions

**Quote (Trevor, 14:47):**
> "The essential promise that we're making to the user is that this is not just another GPT with a wrap around it. It's actually trained on all of the right documentation."

---

### PDF Export Options
**Context:** [25:00 - 32:08]

**Options Discussed:**
1. **Gamma.app** - Professional presentations
   - Pros: Beautiful output, API available
   - Cons: $8-20/month subscription, need to verify programmatic access
   - Status: Matt testing for other projects

2. **Google Docs** - Standard documents
   - Pros: Familiar format, likely cheaper, API available
   - Cons: Less professional than Gamma
   - Status: Viable option

3. **Improved PDF (Markdown)** - Current system enhanced
   - Pros: Simplest, no new dependencies, timebox-able
   - Cons: Less impressive than Gamma
   - Status: **Selected for Phase 2**

**Decision (Trevor, 29:28):**
> "The simplest solution is often the best one... If we manage expectations in the MVP to say, you're going to get a PDF output, so long as it looks tidy and well presented, then they can build their own library of brand documents."

---

### Training Videos - Hosting Strategy
**Context:** [45:28 - 53:43]

**client's Setup:**
- ElevenLabs voice training (full day of work)
- HeyGen avatar ("first try, looks amazing")
- Mastermind.com membership (has video hosting capabilities)

**Options:**
1. **Embedded in app** - Integrated video player
   - Pros: Seamless UX
   - Cons: Engineering effort, video file management

2. **External links** - Hosted on Mastermind.com
   - Pros: Simple, reusable, community access potential
   - Cons: Requires separate account
   - Status: **Selected for MVP**

**Decision (Trevor, 51:56):**
> "I'm happy to do whatever you feel with that, but I think it just seems very straightforward."

Matt's principle applied:
> "If there's a good solution where something doesn't need to be built and engineered, that's usually preferable, especially with prototyping and beta testing."

---

### Beta Testing Flow
**Context:** [53:43 - 1:04:10]

**User Journey:**
1. Free diagnostic (no signup required)
2. Download diagnostic PDF (requires email/account)
3. Paywall page (upsell to premium tools)
   - For beta: Show page, bypass payment
   - For production: Stripe integration
4. Access Brand Coach, Canvas, Copy Generator

**Pricing Strategy (TBD):**
- client uncertain: $97 one-time? Subscription?
- Matt recommends: Subscription (to cover ongoing AI compute)
- Beta tester feedback will inform final pricing
- Need cost analysis from Matt first

**Quote (Trevor, 1:05:55):**
> "What I don't want to do is build myself a liability where everybody pays once and uses it forever."

---

### Document Upload Feature
**Context:** [40:03 - 44:36]

**Use Case:**
- Higher sellers have existing brand documents
- Don't want to manually type diagnostic data
- Upload PDFs → Auto-fill diagnostic fields

**Implementation Plan:**
1. Upload page after diagnostic
2. Multi-document upload supported
3. Feed to vector knowledge base
4. Pre-fill diagnostic fields with extracted data

**Alternative (Matt, 40:52):**
- NotebookLM prompts to convert existing docs → diagnostic format
- User uploads to NotebookLM, gets structured output, pastes into app
- Lower engineering cost, leverages free tool

**Decision:** Phase 3 feature (higher complexity)

---

### Lovable Subscription Decision
**Context:** [33:16 - 35:51]

**Situation:**
- Subscription renews Monday, Dec 1
- Lots of unused credits
- Lovable handles hosting + deployment currently
- Codebase is exportable

**Questions to Research:**
1. Can Lovable be paused instead of cancelled?
2. Does cancellation preserve code access?
3. Does cancellation stop deployment capability?
4. What's migration cost to free-tier hosting?

**Decision:** Matt to research and WhatsApp client before Dec 1

---

### Titan AI Competition
**Context:** [1:12:00 - 1:18:06]

**client's Concern:**
- Titan launching their own AI (Copilot)
- Generic in brand space so far
- Members might resist paying for external tool

**Counter-Arguments:**
1. client's AI has superior brand-specific training (IDEA Framework)
2. Custom GPT + book IP = authority
3. Could license to Titan later (after MVP proves value)

**Strategy:**
- Get MVP working first
- Collect beta tester testimonials
- Then approach Titan leadership with proof

**Quote (Matt, 1:14:39):**
> "If they're smart, they're going to get the experts to input into the AI. They're not just going to rely on the AI to do everything."

---

## Meeting Outcomes

### Immediate Next Steps (Nov 29 - Dec 1)
1. ✅ Matt sends Fathom recording to client
2. ⏳ client processes Phase 1 payment (bank transfer)
3. ⏳ Matt researches Lovable cancellation policy
4. ⏳ Matt merges Phase 1 to production (after payment)
5. ⏳ client tests Phase 1 end-to-end over weekend

### Phase 2 Scope Confirmed ($500)
- Chat sessions (finish + test)
- PDF export improvements (Markdown, remove logo)
- Privacy statement updates
- End-to-end testing and bug fixes

**Estimated Effort:** 5-6 hours
**Target Delivery:** Dec 5-6
**Invoice Date:** Dec 9

### Phase 3 Scope Emerging ($1000)
- Training video integration
- Document upload + pre-fill
- Beta paywall page (no Stripe, just UI)
- Cost analysis for client
- NotebookLM prompt templates
- Gamma/Google Docs research

**Estimated Effort:** 20-29 hours
**Target Delivery:** Mid-December

---

## Key Quotes

### On Vibe Coding Reality
**Client (1:09:05):**
> "I drank the Kool-Aid when people were selling the AI divide... Reality set in when Livable went off the rails, and I realised that, in truth, you can't just do vibe coding for everything and expect it to work properly."

### On Product Positioning
**Client (20:40):**
> "I prefer not to get rid of the Brand Coach page because it makes it feel more personal between the user and myself. They feel that effectively they can have access to my knowledge 24 hours a day."

### On MVP Philosophy
**Matt (51:56):**
> "If there's a good solution where something doesn't need to be built and engineered, that's usually preferable, especially with prototyping and beta testing."

### On Cost Structure
**Matt (1:07:20):**
> "The AI can do it faster and more efficiently a lot of times if it's designed right, but there is a cost with replacing all those human hours. So the core kind of metric is like human hours using this AI tool."

---

## Timeline & Availability

**Matt's Travel:** Nov 30 - Dec 3 (helping aunt move, limited reception)
**Phase 1 Payment:** Expected Dec 2-3 (bank processing)
**Phase 2 Start:** Dec 3-4 (after payment confirmation)
**Phase 2 Delivery:** Dec 5-6
**Phase 2 Invoice:** Dec 9
**Phase 2 Payment:** Dec 11-12 (estimated)

---

## Technical Debt & Future Considerations

### System Knowledge Base
- **Priority:** High (affects output quality)
- **Scope:** Upload client's documents, integrate with RAG
- **Benefit:** Reduce hallucinations, ensure IDEA Framework alignment

### Personalized Training
- **Priority:** Medium (post-MVP)
- **Scope:** ChatGPT-style learning from user interactions
- **Benefit:** Improve response quality over time per user

### Stripe Integration
- **Priority:** Medium (post-beta)
- **Scope:** Payment processing for production launch
- **Dependency:** Pricing model finalized from beta feedback

### Migration from Lovable
- **Priority:** Low (unless subscription becomes burden)
- **Scope:** Move to free-tier hosting (Vercel, Netlify, etc.)
- **Cost:** Time investment for migration

---

## Revenue Projection

| Phase | Amount | Status | Expected Payment |
|-------|--------|--------|------------------|
| Phase 1 | $500 | Invoiced Nov 28 | Dec 2-3, 2025 |
| Phase 2 | $500 | Not invoiced | Dec 11-12, 2025 |
| Phase 3 | $1000 | Not scoped | Late December |
| **Total** | **$2000** | **In progress** | **Dec 2025** |

---

## Notes for Future Reference

### client's Marketing Channels
- Titan membership (~700 members, target 50% adoption = 350 users)
- Outside Titan (estimated 200 users)
- Titan party London (next week, Dec 5-ish) - potential announcement

### Hosting & Compute Costs
- Action: Matt to provide estimates for 100-500 user scenarios
- Includes: Hosting, AI compute, third-party tools
- Needed to inform subscription pricing strategy

### Beta Tester Selection
- Likely from Titan network
- Need questionnaire for pricing feedback
- Free access during beta period
