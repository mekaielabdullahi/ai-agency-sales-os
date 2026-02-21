# S&S Wolf Sheds - Opportunity Matrix

**Created:** December 28, 2025
**Source:** Discovery Call - December 22, 2025
**Updated:** December 28, 2025 (Post-Discovery Working Session)
**Status:** MVP Scope Defined

---

## Opportunity Classification

### Impact vs Effort Matrix

```
                          IMPACT
                    LOW         HIGH
              ┌───────────┬───────────┐
         LOW  │           │  MVP      │
              │  DEFER    │  QUICK    │
    EFFORT    │           │  WINS     │
              │           │  ★★★★★   │
              ├───────────┼───────────┤
              │           │ STRATEGIC │
         HIGH │  AVOID    │ PLATFORM  │
              │           │  ★★★★☆   │
              └───────────┴───────────┘
```

---

## PRIORITY SHIFT NOTICE

**December 28 Update:** Based on working session with Chris Andrade, priorities have significantly shifted from original discovery:

| Original Priority | New Priority |
|------------------|--------------|
| AI Chatbot | **QR/Slot Capture System** |
| Resume Paid Ads | **Website Intake Form** |
| Website Fixes | **Attendant Notifications** |
| Analytics Dashboard | **Lead-to-Building Tracking** |

**Reason:** On-lot lead leakage identified as primary pain point (visitors browse and leave without capture). Focus shifted from traffic generation to capture optimization.

---

## MVP Quick Wins (High Impact, Low-Medium Effort)

### MVP-1: QR/Slot On-Lot Capture System

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Single attendant cannot capture multiple simultaneous visitors; prospects leave without contact captured |
| **Solution** | 20 fixed slot-based QR codes per lot, backend maps slot to current inventory, self-service scan + intake |
| **Impact** | Capture leads from ALL visitors, not just those attendant engages; enable follow-up for browsers |
| **Effort** | Medium - 1-2 weeks for core implementation |
| **Investment** | Part of MVP scope (to be defined) |
| **Dependencies** | Website access, QR management tool selection |
| **Success Metrics** | Scans per lot/week, form submissions, scan-to-submission rate |
| **Priority** | ★★★★★ #1 MVP PRIORITY |

**Why First:**
- Addresses the #1 pain point identified in working session
- Enables data collection on visitor interest
- Low maintenance (fixed slot codes, backend-only updates)
- Foundation for all other analytics

---

### MVP-2: Website Intake Form + Notifications

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No guided capture flow on website; attendant not notified of new leads |
| **Solution** | Add intake form with guided flow; instant SMS/email notification to attendant |
| **Impact** | Capture online leads with preferences; enable immediate response |
| **Effort** | Low - 1 week implementation |
| **Investment** | Part of MVP scope |
| **Dependencies** | Website admin access |
| **Success Metrics** | Form submissions, response time, conversion rate |
| **Priority** | ★★★★★ #2 MVP PRIORITY |

**Why Included:**
- Quick to implement alongside QR system
- Same notification infrastructure
- Fixes "leaky bucket" on website

---

### MVP-3: Lead-to-Building Tracking

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No visibility into which buildings interest visitors |
| **Solution** | Link QR scans to specific buildings, track multi-scan behavior per user |
| **Impact** | Data-driven inventory decisions, personalized follow-up |
| **Effort** | Low-Medium - Included in QR system design |
| **Investment** | Part of MVP scope |
| **Dependencies** | QR system, simple CRM or tracking sheet |
| **Success Metrics** | Building interest heat map, repeat visitor identification |
| **Priority** | ★★★★★ #3 MVP PRIORITY |

---

### MVP-4: Website Quick Fixes

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Broken image rendering, UX issues hurting credibility and conversion |
| **Solution** | Fix image issues, basic UX improvements (patch approach, not full rebuild) |
| **Impact** | Better first impression, improved conversion |
| **Effort** | Low - 1 week |
| **Investment** | Part of MVP scope |
| **Dependencies** | Website admin access |
| **Success Metrics** | Images loading, mobile UX improved |
| **Priority** | ★★★★☆ INCLUDE IN MVP |

**Why Included:**
- Consensus from working session: patch now, rebuild later
- Low effort, immediate credibility improvement
- Required before intake form is useful

---

## Strategic Initiatives (High Impact, Medium-High Effort)

### SI-1: Delivery Handoff Artifact

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Drivers lack site specifics; failed deliveries due to access constraints |
| **Solution** | Customer-to-driver link with maps, access instructions, clearance notes, load orientation |
| **Impact** | Reduced failed deliveries, better customer experience |
| **Effort** | Medium - 1-2 weeks |
| **Investment** | $2,000-$3,000 or part of expanded MVP |
| **Dependencies** | Customer data collection during sale |
| **Success Metrics** | Failed delivery rate, driver prep time |
| **Priority** | ★★★★☆ PHASE 1.5 |

**Why Important:**
- Directly addresses delivery friction pain point
- Simple to implement (link with form data)
- High value for relatively low effort

---

### SI-2: Traffic Counting / Analytics

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No measurement of lot traffic vs conversion; can't quantify improvement |
| **Solution** | Camera-based vehicle counting at single entry/exit point |
| **Impact** | Baseline for conversion measurement, ROI quantification |
| **Effort** | Medium - Hardware + setup |
| **Investment** | $1,500-$3,000 |
| **Dependencies** | Single entry/exit confirmed; camera selection |
| **Success Metrics** | Daily vehicle counts, dwell time, conversion rate |
| **Priority** | ★★★☆☆ PHASE 2 |

**Why Important:**
- Enables true conversion measurement
- Compares to 2-3 years of historical sales
- Foundation for ROI calculation

---

### SI-3: Lightweight CRM with Customer Portfolio

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No integrated view of customer interest, scan history, follow-up status |
| **Solution** | Simple CRM or structured spreadsheet tracking customer portfolios |
| **Impact** | Better follow-up, personalized engagement |
| **Effort** | Medium - 2-3 weeks |
| **Investment** | $3,000-$5,000 or Zoho enhancement |
| **Dependencies** | QR system feeding data |
| **Success Metrics** | Follow-up rate, lead-to-close time |
| **Priority** | ★★★☆☆ PHASE 2 |

---

## Deprioritized from Original Discovery

### DEP-1: AI Chatbot for FAQ Automation

| Attribute | Detail |
|-----------|--------|
| **Original Priority** | ★★★★★ #1 Quick Win |
| **New Priority** | ★★☆☆☆ PHASE 2+ |
| **Reason for Deprioritization** | On-lot capture is higher priority; chatbot doesn't solve lead leakage problem |
| **Revised Approach** | Consider after QR system proves value; may not be needed if capture works |

---

### DEP-2: Resume Paid Ads with Attribution

| Attribute | Detail |
|-----------|--------|
| **Original Priority** | ★★★★★ #2 Quick Win |
| **New Priority** | ★★☆☆☆ PHASE 2+ |
| **Reason for Deprioritization** | "Capture first, then traffic" - need to fix leaky bucket before adding water |
| **Revised Approach** | Resume after QR capture system is working |

---

### DEP-3: Full Analytics Dashboard

| Attribute | Detail |
|-----------|--------|
| **Original Priority** | ★★★★☆ Sprint 2 |
| **New Priority** | ★★☆☆☆ PHASE 2 |
| **Reason for Deprioritization** | MVP scan tracking provides immediate data; full dashboard can wait |
| **Revised Approach** | Build after capture data starts flowing |

---

### DEP-4: Order Verification SOP

| Attribute | Detail |
|-----------|--------|
| **Original Priority** | ★★★★☆ High |
| **New Priority** | ★☆☆☆☆ PHASE 3+ |
| **Reason for Deprioritization** | Not in MVP scope; lead capture is primary focus |
| **Revised Approach** | Address after MVP success |

---

## Transformation Opportunities (High Impact, High Effort)

### TR-1: Platform for Graceland Dealer Network

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Other Graceland dealers have same pain points |
| **Solution** | Package S&S MVP as repeatable solution for dealer network |
| **Impact** | Recurring revenue, network effect, strategic positioning |
| **Effort** | High - 2-3 months after MVP proven |
| **Investment** | $20,000-$50,000 for platform |
| **Dependencies** | MVP success at S&S, Graceland corporate buy-in |
| **Success Metrics** | Dealers onboarded, MRR from platform |
| **Priority** | ★★★★☆ LONG-TERM VISION |

**Why Important:**
- Chris articulated platform vision in working session
- Changes engagement from one-off to recurring
- Significant upside potential

---

### TR-2: Contractor Services Integration

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | GC license underutilized; losing contractor revenue on pads, septic, access roads |
| **Solution** | Integrate contractor services offer into delivery workflow |
| **Impact** | New revenue stream, higher customer lifetime value |
| **Effort** | High - requires service delivery capacity |
| **Investment** | $5,000-$10,000 for integration |
| **Dependencies** | Remus Development capacity, pricing model |
| **Success Metrics** | Contractor services attach rate |
| **Priority** | ★★★☆☆ FUTURE |

---

### TR-3: Full Website Rebuild

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Fundamental mobile UX issues, hosting instability |
| **Solution** | Complete mobile-first website rebuild |
| **Impact** | Professional presence, better conversion |
| **Effort** | High - 4-6 weeks |
| **Investment** | $10,000-$15,000 |
| **Dependencies** | Content strategy, design decisions |
| **Success Metrics** | Mobile conversion, SEO rankings |
| **Priority** | ★★☆☆☆ CONSIDER AFTER MVP |

**Status:** Deprioritized per working session - patch first, rebuild later if needed.

---

## MVP Implementation Sequence

### Sprint 1: Core Capture (Week 1-2)

| # | Opportunity | Investment | Deliverables |
|---|-------------|------------|--------------|
| 1 | MVP-1: QR/Slot System | Included | 20 QR codes, backend mapping, scan tracking |
| 2 | MVP-2: Intake Form + Notifications | Included | Website form, SMS/email alerts |
| 3 | MVP-4: Website Quick Fixes | Included | Image fixes, basic UX |

### Sprint 2: Enhanced Capture (Week 2-3)

| # | Opportunity | Investment | Deliverables |
|---|-------------|------------|--------------|
| 4 | MVP-3: Lead-to-Building Tracking | Included | Customer portfolio, scan history |
| 5 | SI-1: Delivery Handoff | Included or add-on | Driver info link |

### Phase 2: Optimization (Month 2)

| # | Opportunity | Investment | Deliverables |
|---|-------------|------------|--------------|
| 6 | SI-2: Traffic Counting | $1,500-$3,000 | Vehicle counter, baseline data |
| 7 | SI-3: Lightweight CRM | $3,000-$5,000 | Customer management |
| 8 | DEP-2: Paid Ads | $1,500 + ad spend | Attribution tracking |

### Future Phases

| # | Opportunity | Investment | Trigger |
|---|-------------|------------|---------|
| 9 | DEP-1: AI Chatbot | $2,500-$3,500 | If FAQ burden remains high |
| 10 | TR-1: Platform | $20,000+ | After MVP success proven |
| 11 | TR-2: Contractor Services | $5,000-$10,000 | After delivery integration |
| 12 | TR-3: Website Rebuild | $10,000-$15,000 | If patches insufficient |
| 13 | MKT-1: White-label Social Media | $1,000/mo + markup | Chris has content ready |

---

## Marketing Services Opportunity (NEW from Transcript)

### MKT-1: White-Label Social Media Management

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No consistent social media presence; manual Facebook posts |
| **Solution** | Krista Green white-label services (accelerator partner) |
| **Wholesale Cost** | $1,000/mo for 12 posts |
| **Suggested Resale** | $1,200-$2,800/mo |
| **Margin Potential** | $200-$1,800/mo per client |
| **Chris's Assets** | 30 hours of drone footage, delivery videos, pictures ready |
| **Priority** | ★★★☆☆ PHASE 2 - After MVP capture working |

**Why Interesting:**
- Chris expressed immediate interest: "I will pay for that 12th post, like right, like tomorrow"
- He has significant existing content (30 hours of high-end video)
- Low-risk resale opportunity with accelerator partner
- Could be ongoing revenue stream

---

### MKT-2: Website Rebuild (White-Label Option)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Current website has broken images, poor mobile UX |
| **Solution** | Krista Green white-label website build |
| **Wholesale Cost** | $2,500 for 8-page website |
| **Suggested Resale** | $6,000-$10,000 |
| **Margin Potential** | $3,500-$7,500 per project |
| **Priority** | ★★☆☆☆ CONSIDER - If patches insufficient |

**Note:** Current strategy is patch first, but this is an option if full rebuild needed.

---

## ROI Considerations

**Note:** Per discovery process guidelines, we do NOT fabricate ROI projections.

### Qualitative Impact Assessment (Updated)

| Opportunity | Qualitative ROI Justification |
|-------------|------------------------------|
| **QR/Slot System** | Currently capturing 0% of browsers when attendant busy. Any capture is infinite improvement. |
| **Intake Form** | Same notification infrastructure enables immediate response vs. delayed discovery. |
| **Lead-to-Building Tracking** | Can follow up on specific interest vs. generic "you visited our lot." |
| **Website Fixes** | Broken images create unprofessional impression; fixing is table stakes. |
| **Delivery Handoff** | Failed deliveries have direct cost (driver time, customer frustration). |

### Baseline Data Available

- 2-3 years of historical sales data
- Will establish scan/submission baseline in Week 1
- Single entry/exit enables traffic counting

---

## Risk Assessment

### Implementation Risks (Updated)

| Opportunity | Risk Level | Key Risk | Mitigation |
|-------------|------------|----------|------------|
| QR/Slot System | MEDIUM | Low scan adoption | Prominent signage, incentive option |
| Intake Form | LOW | Form abandonment | Keep form short, progressive disclosure |
| Website Fixes | LOW | Hosting instability | Document issues, recommend hosting if severe |
| Delivery Handoff | LOW | Driver adoption | Involve Scott in design |
| Traffic Counting | MEDIUM | Hardware complexity | Start with simple counter |

### Scope Creep Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| 300-page SOT processing | High | AI extraction, focus on MVP-relevant content only |
| Platform vision expansion | High | Define MVP success criteria before discussing platform |
| Feature requests during build | Medium | Change control process, Phase 2 parking lot |

---

## Success Criteria

### MVP Success (Weeks 1-3)

- [ ] QR codes deployed at one lot (proof of concept)
- [ ] Intake form live on website
- [ ] Attendant notifications working
- [ ] First scans and submissions captured
- [ ] Baseline metrics established
- [ ] Client satisfied, ready for rollout to other lots

### Phase 1 Success (Month 1)

- [ ] QR system at all 3 lots
- [ ] Scan tracking across buildings
- [ ] Delivery handoff artifact in use
- [ ] Improvement measurable vs baseline
- [ ] Chris ready to discuss platform vision

### Platform Trigger Metrics

- [ ] 50+ leads captured via QR system
- [ ] Measurable conversion improvement
- [ ] Positive testimonial from Chris/Sandra
- [ ] Interest from other Graceland dealers

---

## Appendix: Opportunity ID Reference (Updated)

| ID | Opportunity | Category | Status |
|----|-------------|----------|--------|
| MVP-1 | QR/Slot On-Lot Capture System | MVP | ★★★★★ Active |
| MVP-2 | Website Intake Form + Notifications | MVP | ★★★★★ Active |
| MVP-3 | Lead-to-Building Tracking | MVP | ★★★★★ Active |
| MVP-4 | Website Quick Fixes | MVP | ★★★★☆ Active |
| SI-1 | Delivery Handoff Artifact | Strategic | ★★★★☆ Phase 1.5 |
| SI-2 | Traffic Counting / Analytics | Strategic | ★★★☆☆ Phase 2 |
| SI-3 | Lightweight CRM | Strategic | ★★★☆☆ Phase 2 |
| DEP-1 | AI Chatbot for FAQ Automation | Deprioritized | ★★☆☆☆ Phase 2+ |
| DEP-2 | Resume Paid Ads with Attribution | Deprioritized | ★★☆☆☆ Phase 2+ |
| DEP-3 | Full Analytics Dashboard | Deprioritized | ★★☆☆☆ Phase 2 |
| DEP-4 | Order Verification SOP | Deprioritized | ★☆☆☆☆ Phase 3+ |
| TR-1 | Platform for Graceland Network | Transformation | ★★★★☆ Long-term |
| TR-2 | Contractor Services Integration | Transformation | ★★★☆☆ Future |
| TR-3 | Full Website Rebuild | Transformation | ★★☆☆☆ If needed |
| MKT-1 | White-Label Social Media | Marketing Services | ★★★☆☆ Phase 2 |
| MKT-2 | Website Rebuild (White-Label) | Marketing Services | ★★☆☆☆ If needed |

---

## Upsell Partnerships (from Transcript)

### Archiefab (Metal Fabrication)
- **Contact:** James at Archiefab
- **Services:** Conceptual design, architectural, permitting, turnkey metal solutions
- **Status:** Waiting to meet Arise team
- **Value:** Handles shipping containers, metal buildings, custom fabrication
- **Integration:** Could be offered to customers wanting container homes, garages

### Contractor Referral Network
Chris mentioned several contractor partnerships:
- **Remus Development (Chris's company):** Concrete pads, site prep, access roads
- **EUS Underground:** Septic systems
- **Other GCs:** Fencing, tree clearing, road building

**Opportunity:** Structure these as referral fees or integrated service packages.

---

**Last Updated:** December 31, 2025 (Added Dec 30 expansion meeting)
**Status:** Scope expanded - multi-location accountability system added
**Next Sync:** TBD - Clarify QR vs Accountability priority

---

## DECEMBER 30 UPDATE: Scope Expansion

### NEW: Dealer Accountability System (OPSYS-1)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Multi-location dealer management; staffing quality issues; inconsistent customer experience |
| **Solution** | Proprietary app with individual logins for daily checklist, photo uploads, deposit verification |
| **Impact** | Scalable operations across multiple dealerships; performance metrics for bonuses; foundation for expansion |
| **Effort** | Medium-High - 2-4 weeks for core system |
| **Investment** | $10,000 phased ($5k + $5k by Feb 1, 2024) |
| **Dependencies** | Requirements definition, lot-specific customization |
| **Success Metrics** | Compliance rate, response time, deposit accuracy, monthly performance scores |
| **Priority** | **POTENTIAL NEW #1 PRIORITY** - Needs clarification |

**Daily Checklist Features:**
- Lot maintenance check
- Gas checks
- Lighting verification
- Customer interaction logging
- Quality photo uploads (inventory)
- 360-degree inventory images
- Deposit verification (photo + security camera sync)
- Clock-out only after deposit confirmation

**Why This Emerged:**
- Expansion to Kayenta hub requires standardized operations
- Can't scale with current ad-hoc management
- Creates foundation for multi-state expansion (AZ > UT > OR > WA > MT > ID)

---

### NEW: Kayenta Hub Expansion Support (EXP-1)

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Geographic concentration risk; logistics inefficiency |
| **Solution** | New dealership hub in Kayenta, AZ with Southern Utah expansion |
| **Impact** | Centralized deliveries, diversified presence, regional growth |
| **Effort** | High - Involves site prep, licensing, security, staffing |
| **Investment** | $3,000-$4,000 office retrofit + security systems |
| **Dependencies** | Gray Eyes licensing, lot leases, Clay finishing work |
| **Timeline** | Operational by end of Feb/March 2024 |
| **Priority** | ★★★☆☆ PARALLEL INITIATIVE (Client-led, we support) |

---

### Revised Priority Matrix

```
                          IMPACT
                    LOW         HIGH
              ┌───────────┬───────────┐
         LOW  │           │  QR MVP   │
              │  DEFER    │  (if      │
    EFFORT    │           │  still    │
              │           │  wanted)  │
              ├───────────┼───────────┤
              │           │ OPSYS-1   │
         HIGH │  AVOID    │ Dealer    │
              │           │ Account.  │
              └───────────┴───────────┘
```

### CONFIRMED: Dual-System Scope

**Both systems are in scope and complement each other:**

| System | Focus | Investment |
|--------|-------|------------|
| QR/Slot Capture (MVP-1 to MVP-4) | Lead capture & tracking | Part of $10k |
| Dealer Accountability (OPSYS-1) | Ops management & scaling | Part of $10k |

**Integration Points:**
- QR system captures leads → feeds into accountability metrics
- Accountability system tracks dealer performance → includes lead handling
- Both support multi-location expansion (Kayenta hub)
