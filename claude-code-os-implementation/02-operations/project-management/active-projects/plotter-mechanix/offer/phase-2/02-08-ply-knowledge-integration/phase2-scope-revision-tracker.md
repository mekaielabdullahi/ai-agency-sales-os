# Phase 2 Scope Revision Tracker - Plotter Mechanix

**Last Updated:** February 8, 2026
**Status:** ⚠️ PENDING MEGAN INTERVIEW
**Target Delivery:** Saturday, Feb 15 (Kelsey call)

---

## Scope Revision Status

### Original Phase 2 Scope (Pre-Ply Deck Knowledge)

| Deliverable | Original Price | Status | Confidence |
|-------------|---------------|--------|------------|
| **Jobber ↔ Ply Integration** | Included in $8K | 🔴 REMOVE | High - Native feature |
| **Used Parts Tracking** | Included in $8K | 🟡 VALIDATE | Medium - May be native Tools feature |
| **Quo ↔ Ply Integration (Chat Agent)** | Included in $8K | 🟢 KEEP | High - Real gap, clear value |
| **TOTAL** | **$8,000** | **REVISION NEEDED** | — |

---

### Revised Phase 2 Scope (Post-Ply Deck Knowledge)

**SCENARIO A: If Megan Has NOT Purchased Ply Warehouse Audit**

| Deliverable | Price | Rationale |
|-------------|-------|-----------|
| **Ply Warehouse Audit** (Ply's service) | $5,000 | 1-3 trucks, 4-week onboarding, team training |
| **Quo ↔ Ply Chat Agent** (Our build) | $8,000 | Real-time inventory lookup during Quo calls |
| **Total** | **$13,000** | Ply foundation + our integration layer |

**Value Proposition:**
- Ply's service: Foundation (barcode system, mobile app, initial training)
- Our service: Integration (Quo ↔ Ply bridge, chat agent, workflow automation)

---

**SCENARIO B: If Megan ALREADY Purchased Ply Warehouse Audit**

| Deliverable | Price | Rationale |
|-------------|-------|-----------|
| **Quo ↔ Ply Chat Agent** | $5,000 | Core integration only - reduced scope |
| **Total** | **$5,000** | Leverage existing Ply implementation |

**Value Proposition:**
- Build on Ply's foundation (already paid for)
- Focus entirely on Quo ↔ Ply gap
- Fastest time to value

---

**SCENARIO C: If Ply is PARTIALLY Implemented (Most Likely)**

| Deliverable | Price | Rationale |
|-------------|-------|-----------|
| **Complete Ply Implementation** | $3,000 | Training, process adoption, barcode setup |
| **Quo ↔ Ply Chat Agent** | $5,000 | Real-time inventory lookup during Quo calls |
| **Total** | **$8,000** | Complete what Megan started + integrate |

**Value Proposition:**
- Finish Ply setup (barcode workflow, team training, process adoption)
- Build Quo ↔ Ply integration
- Used parts tracking workflow (leverage Ply's Tools feature)

---

## Decision Tree (Based on Megan Interview)

### Question 1: Did Megan Purchase Ply's Warehouse Audit Service?

**If YES:**
- Scope: Scenario B ($5K - Quo integration only)
- Deliverable: Chat agent for Quo ↔ Ply inventory lookups
- Timeline: 2-3 weeks

**If NO:**
- Scope: Scenario A ($13K - Ply service + our integration)
- Deliverable: Recommend Ply's $5K service + our $8K integration
- Timeline: 4-week Ply onboarding + 2-3 week integration

**If PARTIALLY:**
- Scope: Scenario C ($8K - complete + integrate)
- Deliverable: Finish Ply setup + build Quo integration
- Timeline: 3-4 weeks total

---

### Question 2: Is Jobber ↔ Ply Sync Active?

**If YES (Active and Working):**
- ✅ Remove from scope (native feature, $0 cost)
- Focus: Quo ↔ Ply gap only

**If NO (Not Active):**
- ⚠️ Investigate why (not configured? integration broken?)
- Deliverable: Activate native integration (1-2 hours, not $8K build)

**If PARTIALLY (Some Sync, Some Errors):**
- ⚠️ Troubleshoot configuration issues (included in "complete Ply" scope)
- Not a custom build, just configuration fix

---

### Question 3: How Are Used Parts Tracked Today?

**If Using Ply's Tools Feature:**
- ✅ Remove from scope (already solved, $0 cost)
- Focus: Ensure Tools feature is configured for used parts workflow

**If Using Spreadsheets/Manual:**
- ⚠️ Validate if Ply's Tools feature can solve this
- Deliverable: Configure Tools feature + train team ($2-3K, included in "complete Ply" scope)

**If Not Tracked At All:**
- 🔴 High-value deliverable
- Deliverable: Design used parts workflow + configure Ply Tools feature
- Price: $3-5K depending on complexity

---

## Knowledge Gap Status

### ✅ CLOSED (From Ply Deck)

| Gap | Answer |
|-----|--------|
| Ply capabilities overview | Comprehensive - 19-page deck reviewed |
| Jobber integration approach | Native, bidirectional, real-time webhooks |
| Tools tracking feature | New feature - tracks serialized equipment, could be used for parts |
| Supplier integrations | 3,000+ branches, 3M products |
| Mobile app capabilities | iOS/Android with barcode scanning |
| Implementation service | $5K+ for 1-3 trucks, 4-week onboarding |
| ROI data | $60K savings for $3M contractor |

---

### ⚠️ STILL OPEN (Blocking Megan Interview)

| Gap | Priority | Impact on Scope |
|-----|----------|-----------------|
| **Megan's Ply implementation status** | 🔴 P0 | Determines Scenario A/B/C |
| **Jobber ↔ Ply sync activation** | 🔴 P0 | If active, remove from scope |
| **Used parts tracking approach** | 🔴 P0 | If using Tools feature, remove from scope |
| **Ply API access credentials** | 🟡 P1 | Required for Quo integration build |
| **Barcode implementation status** | 🟡 P1 | Affects warehouse setup timeline |
| **Custom material categories** | 🟡 P1 | Affects used parts tracking design |

---

## Pricing Sensitivity Analysis

### Low-End Scenario ($5K)
- **Assumptions:**
  - Ply fully implemented (warehouse audit purchased)
  - Jobber ↔ Ply sync active
  - Used parts tracking solved via Tools feature
  - Only gap: Quo ↔ Ply integration

- **Deliverable:**
  - Chat agent for real-time Ply inventory lookups during Quo calls
  - API integration layer (Quo ↔ Ply)
  - Team training on using chat agent

- **Timeline:** 2-3 weeks

---

### Mid-Range Scenario ($8K) - MOST LIKELY
- **Assumptions:**
  - Ply partially implemented (features exist but not fully adopted)
  - Jobber ↔ Ply sync exists but needs configuration
  - Used parts tracking needs workflow design + Tools feature setup
  - Quo ↔ Ply integration is the main build

- **Deliverable:**
  - Complete Ply implementation (training, process adoption, barcode workflow)
  - Configure used parts tracking via Tools feature
  - Build Quo ↔ Ply chat agent integration
  - Team training on full workflow

- **Timeline:** 3-4 weeks

---

### High-End Scenario ($13K)
- **Assumptions:**
  - Ply warehouse audit NOT purchased
  - Megan wants turnkey solution (Ply foundation + our integration)
  - We recommend Ply's $5K service + our $8K work

- **Deliverable:**
  - **Ply's Service ($5K):** 1-3 trucks, barcode system, 4-week onboarding
  - **Our Service ($8K):** Quo ↔ Ply integration, used parts workflow, team training

- **Timeline:** 4-week Ply onboarding + 2-3 week our work = 6-7 weeks total

---

## ROI Justification (From Ply Case Study)

### Ply's $3M Contractor Case Study

| Metric | Before Ply | After Ply | Impact |
|--------|-----------|-----------|--------|
| Material Spend % | 22% of revenue | 20% of revenue | 2% decrease |
| Annual Material Spend | $660K | $600K | **$60K savings** |
| Hidden Costs | Not tracked | Eliminated | **$15-20K savings** |
| **Total Annual Savings** | — | — | **$75-80K** |

---

### Plotter Mechanix Projected Impact

**Assumptions:**
- Current revenue: ~$700-800K/year
- Material spend: ~22% of revenue (industry average)
- Current annual material spend: ~$154-176K

**Projected Savings (Conservative 2% Improvement):**

| Category | Annual Savings |
|----------|---------------|
| Material cost optimization | $14-16K |
| Reduced tech time on inventory | $3-5K |
| Eliminated emergency purchases | $2-4K |
| **Total Annual Savings** | **$19-25K** |

**Payback Period:**
- Mid-range scenario ($8K): **3-5 months**
- High-end scenario ($13K): **6-8 months**

**5-Year ROI:**
- Investment: $8-13K (one-time)
- 5-year savings: $95-125K
- **ROI: 730-960%**

---

## Competitive Positioning

### What Ply Provides (Already Built)
- ✅ Jobber integration (native)
- ✅ QuickBooks integration
- ✅ Supplier integrations (3,000+ branches)
- ✅ Mobile apps with barcode scanning
- ✅ Tools tracking for serialized equipment
- ✅ Auto-replenishment logic
- ✅ Transfer management

### What We Provide (Unique Value-Add)
- 🔥 **Quo ↔ Ply integration** (no native support from Ply)
- 🔥 **Chat agent for real-time inventory lookups** (during Quo calls)
- 🔥 **Used parts workflow design** (leverage Ply's Tools feature)
- 🔥 **Team training and process adoption** (completing Ply's partial implementation)
- 🔥 **Custom automation on top of Ply** (workflow enhancements beyond Ply's core)

**Key Message:** *"We're not rebuilding what Ply already does. We're completing their implementation and bridging the gap between Ply and Quo - which is the #1 pain point for Kelsey/Andrew during customer calls."*

---

## Questions for Saturday's Kelsey Call

### If We Present Mid-Range Scenario ($8K)

**Framing:**
- "Based on our research, Ply has most of the features you need already built-in."
- "The real gap is the Quo ↔ Ply integration - which is where Kelsey and Andrew feel the pain during customer calls."
- "Our $8K scope focuses on completing Megan's Ply implementation and building the Quo ↔ Ply bridge."

**Questions to Ask Kelsey:**
1. When Kelsey/Andrew are on a Quo call and a customer asks "Do you have X in stock?", what happens today?
2. How often does this happen per day/week?
3. Have you ever quoted a part you didn't have, or said you didn't have a part that was in stock?
4. What would the ideal experience be for checking inventory during a Quo call?

---

### If We Present High-Range Scenario ($13K)

**Framing:**
- "Ply offers a $5K warehouse audit service to set up your initial 1-3 trucks."
- "This includes barcode system setup, mobile app training, and 4-week onboarding."
- "We recommend combining their service with our $8K Quo ↔ Ply integration for a complete solution."

**Questions to Ask Kelsey:**
1. Has Megan purchased Ply's warehouse audit service?
2. Would you prefer a turnkey solution where Ply handles the foundation and we handle the integration?
3. Are you comfortable with a 6-7 week timeline (4 weeks Ply + 2-3 weeks us)?

---

### If We Present Low-Range Scenario ($5K)

**Framing:**
- "Great news - Megan has already implemented most of what you need in Ply."
- "The only real gap is the Quo ↔ Ply integration."
- "Our $5K scope focuses entirely on building the chat agent so Kelsey/Andrew can check inventory during Quo calls."

**Questions to Ask Kelsey:**
1. Is Megan's Ply implementation working well? Any issues?
2. Are you happy with the used parts tracking workflow?
3. Any other pain points we should address while we're building the Quo integration?

---

## Next Steps

### Before Megan Interview
- [x] Review Ply deck (COMPLETE)
- [x] Create knowledge base doc (COMPLETE)
- [x] Prepare interview questions (COMPLETE)
- [ ] Schedule Megan interview (BLOCKING)

### After Megan Interview
- [ ] Compile interview notes
- [ ] Determine Scenario A/B/C based on answers
- [ ] Draft revised Phase 2 proposal
- [ ] Create ROI slide deck for Saturday call
- [ ] Prepare talking points for Kelsey call
- [ ] Share with team for review (Chris, Mekaiel, Trent)

### For Saturday Call (Feb 15)
- [ ] Present revised Phase 2 scope
- [ ] Show Ply ROI case study ($60K savings)
- [ ] Position our work as "completing what Megan started + bridging Quo ↔ Ply gap"
- [ ] Get buy-in on scope and pricing
- [ ] Schedule Phase 2 kickoff (if approved)

---

## Decision Log

### Feb 8, 2026 - Initial Scope Revision

**What Changed:**
- Discovered Ply has MORE capabilities than we thought
- Jobber ↔ Ply integration is NATIVE (not custom build needed)
- Ply offers $5K warehouse audit service
- Tools tracking feature may solve used parts problem

**Impact:**
- Original $8K scope needs revision
- Likely range: $5K-13K depending on Megan's implementation status
- Quo ↔ Ply integration is the real value-add (not duplicating Ply)

**Next Action:**
- Interview Megan ASAP (before Saturday)

---

*Last Updated: February 8, 2026*
*Next Review: After Megan interview*
*Target Delivery: Saturday, Feb 15 (Kelsey call)*
