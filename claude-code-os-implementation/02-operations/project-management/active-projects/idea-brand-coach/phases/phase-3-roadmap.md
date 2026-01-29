# IDEA Framework Website - Phase 3+ Roadmap (P1 and Beyond)

**Phase 3 Value:** $1000
**Estimated Effort:** 20-29 hours
**Target Start:** Dec 19, 2025
**Target Delivery:** Dec 25, 2025 (before Trevor travels)

---

## Dec 19 Update: Hormozi Money Model Framework

### Brand Owner Customer Needs Map

Using Matthew's experience as target customer (Infinity Vault card game brand = brand owner problems):

| Stage | Customer Problem | App Solution (Offer) | Pricing Tier |
|-------|------------------|---------------------|--------------|
| **AWARENESS** | "Is my brand working?" | Free Brand Diagnostic | FREE (Lead Magnet) |
| **DISCOVERY** | "Who is my customer really?" | Avatar Builder | CORE |
| **CLARITY** | "What's my brand strategy?" | Brand Canvas | CORE |
| **EXECUTION** | "How do I write copy that sells?" | Copy Generator | CORE |
| **GUIDANCE** | "I need expert help on demand" | AI Brand Coach | CORE |
| **VALIDATION** | "How do I test demand before investing?" | Pre-order/Crowdfunding tools | UPSELL |
| **PRODUCTION** | "I need marketing materials" | Video scripts, creative tools | UPSELL |
| **SCALING** | "How do I grow distribution?" | TikTok strategy, affiliate tools | UPSELL |
| **MASTERY** | "I want hands-on help" | 1-on-1 Consultation w/ Trevor | HIGH-TOUCH |

### Hormozi Money Model Applied

```
ATTRACTION (Free)          →  CORE ($X/mo)           →  UPSELLS              →  CONTINUITY
─────────────────────────────────────────────────────────────────────────────────────────────
• Free Diagnostic          →  • Avatar Builder       →  • Doc Pre-fill       →  • Monthly sub
• Strategic overview       →  • Brand Canvas         →  • Advanced exports   →  • Training library
• PDF download (email)     →  • Copy Generator       →  • Crowdfund tools    →  • Community
                           →  • AI Brand Coach       →  • 1-on-1 w/ Trevor   →  • Updates
```

### Phase 3 Priority: "Beta-Ready" (Single Output Document)

From Dec 12 meeting, Trevor's success criteria:
> "The criteria that says it's ready for beta is that all the inputs end up on the same document."

**Phase 3 is about PROVING VALUE to beta testers - not perfecting features.**

---

## Executive Summary

Phase 3 represents the transition from MVP to market-ready product. Focus shifts from core functionality to user experience, monetization infrastructure, and scalability. These are heavier lifts requiring new development, third-party integrations, and product strategy work.

**Strategic Goal:** Prepare for beta tester rollout with professional UX, clear value proposition, and pricing feedback mechanism.

---

## Phase 3 Deliverables - REVISED (Dec 19)

### BETA-READY PRIORITY (Must Have Before Dec 25)

**#1: Single Consolidated Output Document (4-6 hours)**
Trevor's success criteria: "All inputs end up on the same document"
- [ ] Compile Avatar Builder outputs into single export
- [ ] Include Brand Canvas data in same document
- [ ] Include Copy Generator outputs
- [ ] Single "Download Complete Report" button
- [ ] Clean, text-based formatting (consistent with existing exports)

**#2: UI Polish for Beta (2-3 hours)**
From Dec 12 meeting - quick fixes for professional appearance:
- [ ] Fix widow on "Strategic Brand Building Journey" headline
- [ ] Remove Diagnostic from post-login nav bar
- [ ] Add support email link (contact@ideabrandconsultancy.com)
- [ ] Ensure consistent text-only PDF exports across app

**#3: Reinstate Strategic Brand Building Journey Page (1-2 hours)**
- [ ] Bring back the IDEA framework explanation page
- [ ] Position as home/landing after login
- [ ] Prepare video placeholder (Trevor will provide content)

**#4: Collapsible Video Component (2-3 hours)**
Reusable component for training videos on key pages:
- [ ] Build collapse/expand functionality
- [ ] Add transcript view with copy button
- [ ] Place on: Start Here, Avatar Builder, Brand Canvas

### NICE-TO-HAVE (If Time Permits)

**#5: AI Assistant for Decision Factors (2-3 hours)**
- [ ] Add "AI Suggest" button in Buying Behavior section
- [ ] Pull from user's knowledge base to suggest factors

**#6: Comma-Separated Value Parsing (1 hour)**
- [ ] When user enters comma-separated values, split into individual tags

---

## Original Phase 3 Deliverables (Reference)

### 1. Training Video Integration (4-6 hours)

**Action Item:** [Fathom 45:28](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2731.9999)

**Scope:**
- [ ] Research embedded video vs external link UX
- [ ] Build video link buttons on each module page
- [ ] Create intro video section on document upload page
- [ ] Test video playback (desktop + mobile)
- [ ] Send demo to client for approval

**client's Assets Ready:**
- ElevenLabs voice training (1 day of work completed)
- HeyGen avatar ("first try, looks amazing")
- Mastermind.com hosting available

**Implementation Decision:**
- **MVP Approach:** External links to Mastermind.com hosted videos
- **Rationale:** Simple, no engineering overhead, reusable
- **Future Enhancement:** Embedded player if user feedback demands it

**Video Placements:**
1. Document upload page (intro/walkthrough)
2. Each diagnostic module (per-field guidance)
3. Brand Coach page (how to use consultant)
4. Canvas/Copy Generator pages (output usage)

**Deliverable:**
- Button component with icon + "Training Video" label
- Links to client's hosted videos
- Mobile-responsive placement

---

### 2. Document Upload + Pre-fill System (6-8 hours)

**Action Items:**
- [Fathom 40:03](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=2452.9999) - NotebookLM prompts
- General discussion on multi-document upload

**Problem Statement:**
Higher sellers have existing brand documents (PDFs, decks, guidelines). Manually typing diagnostic data creates friction and reduces adoption.

**Solution A: Direct Upload + Auto-fill**
- [ ] Create document upload page (after diagnostic)
- [ ] Multi-file upload support (drag & drop)
- [ ] Extract text from PDFs
- [ ] Feed to vector knowledge base
- [ ] Auto-populate diagnostic fields with extracted data
- [ ] Allow manual override/editing

**Solution B: NotebookLM Workflow (Simpler)**
- [ ] Draft NotebookLM prompts for brand doc conversion
- [ ] Provide prompts to users in app
- [ ] Users upload docs to NotebookLM (free tool)
- [ ] NotebookLM outputs structured diagnostic format
- [ ] Users paste into app fields

**Recommended Approach:**
- **Phase 3:** Solution B (NotebookLM prompts) - lower cost, faster delivery
- **Phase 4:** Solution A (direct upload) - better UX, requires more engineering

**NotebookLM Prompts to Create:**
1. Brand demographics extraction
2. Brand psychographics extraction
3. Brand positioning summary
4. Brand mission/vision/values extraction
5. Competitive landscape summary

**Deliverable:**
- 5 NotebookLM prompts (tested and refined)
- In-app instructions page: "Pre-fill your diagnostic"
- Example outputs for user reference

---

### 3. Beta Paywall Page (6-8 hours)

**Action Item:** [Fathom 1:01:46](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=3695.9999)

**Scope:**
- [ ] Design paywall page UI
- [ ] Embed client's upsell video (recorded, ready)
- [ ] Create "Upgrade to Premium" button
- [ ] Build upgrade flow (no Stripe, beta testers bypass payment)
- [ ] Free tier vs Premium feature comparison table
- [ ] Testimonials section (if available)

**User Flow:**
1. Complete free diagnostic
2. Download diagnostic PDF (requires email/account)
3. **Paywall page appears** ← THIS PAGE
4. Beta testers: Click upgrade → Granted access (no payment)
5. Production users: Click upgrade → Stripe payment → Access granted

**Page Components:**
- **Hero:** "Unlock Premium Brand Strategy Tools"
- **Video:** client's talking head upsell (embedded)
- **Feature List:**
  - ✅ Brand Coach GPT (24/7 expert consultation)
  - ✅ Brand Canvas Generator
  - ✅ Copy Generator (positioning, messaging, etc.)
  - ✅ Chat history & session management
  - ✅ Professional PDF exports
  - ✅ Training videos for each module
- **Pricing:** TBD (show placeholder or "Pricing based on your feedback")
- **CTA:** "Start Beta Testing" (for beta) / "Subscribe Now" (for production)

**Beta Logic:**
- Beta testers identified by email whitelist or beta code
- Upgrade button → Check beta status → Grant access immediately
- Track beta tester feedback for pricing

**Deliverable:**
- Paywall page live and functional
- Beta bypass working
- Video embedded and playing
- Mobile responsive

---

### 4. Advanced Canvas Export Options (4-6 hours)

**Action Item:** [Fathom 26:39](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=1599.9999)

**Research Phase (2 hours):**
- [ ] Test Gamma.app API for programmatic access
- [ ] Verify pricing ($8-20/month subscription?)
- [ ] Test Google Docs API integration
- [ ] Compare output quality (Gamma vs Google Docs vs improved PDF)
- [ ] Report findings to client with cost/benefit analysis

**Implementation Phase (4-6 hours, if approved):**
- [ ] Integrate Gamma.app API (if selected)
  - Create Gamma account + API key
  - Build integration to send brand canvas data
  - Generate presentation-quality output
  - Test download/share functionality
- [ ] OR integrate Google Docs API (if selected)
  - OAuth setup for user's Google Drive
  - Create Google Doc template
  - Populate with brand canvas data
  - Save to user's Drive automatically

**Decision Criteria:**
| Option | Quality | Cost | Complexity | Recommendation |
|--------|---------|------|------------|----------------|
| Gamma | ⭐⭐⭐⭐⭐ | $8-20/mo | Medium | If budget allows |
| Google Docs | ⭐⭐⭐ | Free* | Medium | Cost-effective |
| Improved PDF | ⭐⭐⭐ | Free | Low | Baseline (Phase 2) |

*Google Docs requires user OAuth, no subscription cost for app

**Deliverable:**
- Research report to client
- Implementation of selected option
- User testing of export quality

---

### 5. Cost Analysis & Pricing Strategy (1-2 hours)

**Action Item:** [Fathom 1:10:25](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=4257.9999)

**client's Question:**
> "If we had 100 users, 500 users, and they're each using the app regularly, what will that cost at the end of the month?"

**Analysis Required:**

**Fixed Costs (monthly):**
- [ ] Lovable hosting (or alternative after migration)
- [ ] Domain registration
- [ ] Supabase (database + auth)
- [ ] Third-party tools (Gamma, etc., if adopted)

**Variable Costs (per user/usage):**
- [ ] OpenAI API calls (diagnostic analysis)
- [ ] OpenAI embeddings (vector knowledge base)
- [ ] GPT-4 conversations (Brand Coach chat)
- [ ] File storage (uploaded documents)
- [ ] Bandwidth (PDF downloads, etc.)

**Usage Assumptions:**
- Average sessions per user per month: ___
- Average messages per session: ___
- Average diagnostic runs per user: ___
- Average documents uploaded per user: ___

**Scenarios to Model:**
| User Count | Monthly Cost | Cost/User | Suggested Pricing |
|------------|--------------|-----------|-------------------|
| 10 users | $__ | $__ | $__ |
| 50 users | $__ | $__ | $__ |
| 100 users | $__ | $__ | $__ |
| 350 users (50% Titan) | $__ | $__ | $__ |
| 500 users | $__ | $__ | $__ |

**Deliverable:**
- Cost spreadsheet with scenarios
- Pricing recommendations (subscription tiers)
- Break-even analysis
- Send to client for pricing decision

---

### 6. Beta Tester Questionnaire (2-3 hours)

**Action Item:** [Fathom 1:04:10](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=3852.9999)

**Owner:** client (with Matt's input on product questions)

**Questionnaire Sections:**

**1. User Experience**
- How intuitive was the diagnostic process? (1-5 scale)
- Did the training videos help? What was missing?
- How easy was it to navigate between modules?
- What features were confusing?
- What features did you love?

**2. Output Quality**
- How valuable was the Brand Coach's advice? (1-5 scale)
- Did the diagnostic accurately capture your brand?
- How useful were the Brand Canvas outputs?
- Did the Copy Generator meet your needs?
- What outputs would you want to see improved?

**3. Pricing & Value**
- What would you pay for this tool? (open-ended)
- Would you prefer: One-time payment, monthly subscription, or annual subscription?
- What price feels too high? Too low (seems low quality)?
- How does this compare to alternatives you've tried?
- Would you recommend this to other Titans?

**4. Feature Requests**
- What features are missing that you expected?
- What integrations would be valuable? (Canva, social media, etc.)
- Would you use a community feature for brand feedback?
- What would make this a "must-have" tool?

**5. Demographics**
- Business type (eCommerce, services, etc.)
- Revenue stage (startup, $100k+, $1M+, etc.)
- Current brand maturity (new, established, rebranding)
- Titan member? (Yes/No)

**Deliverable:**
- Google Form or Typeform questionnaire
- Shared with beta testers after 1 week of usage
- Results compiled for pricing decision

---

### 7. Coach Review & Feedback (External)

**Action Item:** [Fathom 1:17:02](https://fathom.video/share/Jpi9W9zz6dWcXBk3fLsdzj4kv8cwCvUH?timestamp=4637.9999)

**Owner:** Matt

**Scope:**
- [ ] Schedule session with development coach
- [ ] Present client project (product, tech stack, business model)
- [ ] Get feedback on:
  - Product-market fit
  - Technical architecture
  - Pricing strategy
  - Go-to-market approach
  - Scalability concerns
- [ ] Document recommendations
- [ ] Share findings with client

**Questions for Coach:**
1. Is the RAG implementation over-engineered for MVP?
2. Should we prioritize system knowledge base or user features?
3. How should we structure subscription tiers?
4. What's the biggest risk to product success?
5. How can we differentiate from ChatGPT + custom GPTs?

**Deliverable:**
- Coach feedback summary
- Recommended adjustments to roadmap
- Risk mitigation plan

---

## Phase 3 Success Criteria

### Functional Requirements
- [ ] Training videos accessible on all key pages
- [ ] Document upload working (or NotebookLM prompts available)
- [ ] Beta paywall page functional (bypass for beta testers)
- [ ] Advanced export option researched and selected
- [ ] Cost analysis completed and pricing informed

### Quality Requirements
- [ ] All features tested end-to-end
- [ ] Mobile responsive across new pages
- [ ] Video playback smooth on all devices
- [ ] Beta tester onboarding flow polished

### Business Requirements
- [ ] Beta tester questionnaire ready
- [ ] Pricing strategy drafted
- [ ] Cost model validated
- [ ] Coach feedback incorporated

---

## Phase 3 Timeline

| Date | Milestone |
|------|-----------|
| Dec 9 | Phase 2 invoice sent, Phase 3 kickoff |
| Dec 10-11 | Training video integration |
| Dec 12 | Document upload (NotebookLM prompts) |
| Dec 13 | Beta paywall page build |
| Dec 14 | Export options research |
| Dec 15 | Cost analysis + questionnaire |
| Dec 16 | Coach review session |
| Dec 17-18 | Final testing + bug fixes |
| Dec 19 | Client walkthrough |
| Dec 20 | Invoice Phase 3 ($1000) |
| Dec 23 | Receive Phase 3 payment (estimated) |

---

## Phase 4+ Ideas - Hormozi Money Model Aligned

### Phase 4: Monetization & Core Product Lock-In ($1000)
**Focus:** Convert beta users to paying customers

**CORE OFFER COMPLETION:**
- [ ] Stripe payment integration (subscription model)
- [ ] Subscription management (billing, upgrades, cancellations)
- [ ] Beta tester questionnaire → pricing validation
- [ ] Cost analysis (usage-based pricing model)
- [ ] Email notifications (payment receipts, welcome sequence)

**Estimated Effort:** 15-20 hours

---

### Phase 5: Upsell Features - Time Savers ($1000)
**Focus:** "Anticipate what they'll want next" (Hormozi)

**DOCUMENT PRE-FILL (Time Saver Upsell):**
- [ ] Upload brand documents → auto-populate Avatar fields
- [ ] NotebookLM prompts for extraction (MVP approach)
- [ ] Full auto-fill from PDF/docs (premium approach)

**ADVANCED EXPORTS (Quality Upsell):**
- [ ] Gamma.app integration for presentation-quality exports
- [ ] Google Docs integration for editable outputs
- [ ] Brand Canvas → pitch deck template

**Estimated Effort:** 20-25 hours

---

### Phase 6: Upsell Features - Validation & Production ($1000)
**Focus:** Solve the NEXT problem before they know they have it

**PRE-ORDER/CROWDFUNDING TOOLS (From WhatsApp discussion):**
- [ ] Campaign planning wizard
- [ ] Marketing asset generator for launches
- [ ] Pledge tier suggestions based on avatar data
- [ ] Email sequence templates for campaign

**VIDEO/CONTENT STRATEGY:**
- [ ] TikTok video script generator
- [ ] Affiliate outreach templates
- [ ] Creative brief generator for designers

**Estimated Effort:** 25-30 hours

---

### Phase 7: High-Touch Upsell & Continuity ($1000+)
**Focus:** "Book a meeting" path for premium clients

**1-ON-1 CONSULTATION UPSELL:**
- [ ] In-app "Book a Call with Trevor" integration
- [ ] LinkedIn diagnostic duplicate (separate funnel - Trevor may build himself)
- [ ] Lead scoring based on diagnostic + engagement
- [ ] Calendly integration with pre-filled context

**CONTINUITY/COMMUNITY:**
- [ ] Training video library (Mastermind.com integration)
- [ ] Community feedback feature
- [ ] Admin panel for Trevor (user analytics, engagement tracking)

**Estimated Effort:** TBD

---

### Phase 8: Strategic Partnerships (Negotiable)
- Titan AI integration (license IDEA Framework knowledge base)
- White-label version for Titan members
- Revenue share model with Titan
- Titan-specific features (member directory integration)

---

## Deferred Items (Not Phase 3)

### Administrative
- **Pay Matt via new link; then Matt merges Phase 1**
  - Status: Waiting on client's payment (Dec 2-3)
  - Owner: client → Matt

- **Confirm Lovable cancellation/pause policy**
  - Deadline: Before Dec 1
  - Owner: Matt
  - Context: Subscription renews Monday, need decision

### Low Priority / Future Research
- Mobile app development
- Advanced analytics dashboard
- Competitor analysis integration
- Industry-specific templates
- AI-powered brand audit automation

---

## Risk Management

### Technical Risks

**Risk:** Gamma API doesn't support programmatic access
- **Mitigation:** Fall back to Google Docs or improved PDF
- **Impact:** Medium (user experience slightly degraded)

**Risk:** NotebookLM prompts don't produce quality outputs
- **Mitigation:** Iterate prompts, provide examples, or defer to Phase 4 direct upload
- **Impact:** Medium (higher sellers may not adopt)

**Risk:** Cost analysis reveals unsustainable pricing
- **Mitigation:** Adjust features, optimize AI usage, or pivot business model
- **Impact:** High (could block production launch)

### Business Risks

**Risk:** Beta testers don't see value, won't pay
- **Mitigation:** Improve outputs, add requested features, adjust positioning
- **Impact:** High (product-market fit unclear)

**Risk:** Titan AI becomes competitive threat
- **Mitigation:** License IDEA Framework to Titan, differentiate on quality
- **Impact:** Medium (can pivot to partnership)

**Risk:** Lovable subscription cost unsustainable
- **Mitigation:** Migrate to free-tier hosting (Vercel, Netlify, Railway)
- **Impact:** Low (migration effort manageable)

---

## Revenue Tracking

| Phase | Amount | Effort (hours) | Hourly Rate | Status |
|-------|--------|----------------|-------------|--------|
| Phase 1 | $500 | ~12 | $42/hr | Invoiced Nov 28 |
| Phase 2 | $500 | ~6 | $83/hr | Queued |
| Phase 3 | $1000 | ~24 | $42/hr | Scoped |
| **Total** | **$2000** | **~42 hours** | **$48/hr avg** | **In progress** |

**Phase 3 Margin:** 100% (self-built)
**Cumulative Revenue (if all phases close):** $2000 by end of December

---

## Architect Role Transition Checkpoint

### Current State (Phases 1-3)
**Matt's Role:** Hands-on builder + architect
- Building to learn system deeply
- Developing quality standards
- Creating reusable components
- Documenting architecture

**Why This Makes Sense:**
1. Can't manage what you haven't built
2. Quality standards come from experience
3. Cost estimates accurate only after doing it
4. Developer delegation requires knowing "good"

### Future State (Phase 4+)
**Matt's Role:** Architect + manager
- Scope and estimate new phases
- Delegate builds to developers
- Manage quality and delivery
- Collect payments and margins

**Developer Handoff Criteria:**
- [ ] Core architecture documented
- [ ] Code quality standards defined
- [ ] Testing procedures established
- [ ] Developer onboarding materials ready
- [ ] Cost estimates validated from experience

**Developer Handoff Point:** After Phase 3 delivery (mid-December)

**Margin After Handoff:** 40-50%
- Developer cost: ~$50-75/hr
- Client pays: ~$100/hr (via phased deliverables)
- Matt's margin: $25-50/hr for management + oversight

---

## Strategic Questions for Phase 3

### Product Strategy
1. Should we build system knowledge base in Phase 3 or defer to Phase 5?
2. Is NotebookLM workflow acceptable UX for higher sellers?
3. How do we measure output quality improvement?

### Pricing Strategy
4. Subscription vs one-time payment? (Answer: Subscription, from meeting)
5. Tiered pricing (Free/Pro/Enterprise) or single tier?
6. What's the pricing sweet spot for Titan members specifically?

### Go-to-Market
7. Should beta testing be Titan-only or include external users?
8. When to approach Titan leadership about partnership?
9. How to position against ChatGPT + custom GPTs?

### Technical Strategy
10. When to migrate off Lovable? (Cost vs effort tradeoff)
11. Which export option provides best perceived value?
12. How to balance feature development vs output quality improvement?

---

## Next Actions (Priority Order)

### Immediate (Dec 2-3)
1. Wait for Phase 1 payment confirmation
2. Deliver Phase 2 work
3. Invoice Phase 2 ($500)

### Short-term (Dec 9-13)
4. Present Phase 3 proposal to client
5. Get Phase 3 approval
6. Start training video integration
7. Draft NotebookLM prompts

### Medium-term (Dec 14-20)
8. Build beta paywall page
9. Research export options
10. Complete cost analysis
11. Coach review session
12. Deliver Phase 3
13. Invoice Phase 3 ($1000)

---

## Notes

### Key Principle: Simplicity First
From meeting discussion, client and Matt aligned on **Occam's Razor** - simplest solution is often best for MVP. Apply this to all Phase 3 decisions:

- Training videos: External links (not embedded)
- Document upload: NotebookLM prompts (not direct integration)
- Export options: If Gamma is complex, choose Google Docs or improved PDF

### Strategic Patience
client's original model was education/courses. This app is an experiment. Don't over-engineer for scale that may not come. Build lean, validate with beta testers, then invest in production features.

### The Long Game
Phase 3 is about **proving value**, not perfecting features. Beta tester feedback will inform Phase 4+ priorities. Focus on:
1. User experience polish
2. Output quality perception
3. Pricing validation
4. Credibility building

**Success = Beta testers willing to pay. Everything else is secondary.**
