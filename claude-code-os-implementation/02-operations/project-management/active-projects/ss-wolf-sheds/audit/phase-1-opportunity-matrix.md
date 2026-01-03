# S&S Wolf Sheds - Phase 1 Opportunity Matrix

**Created:** January 3, 2026
**Phase:** 1 of 4 - Foundation Sprint
**Investment:** $5,000
**Timeline:** 2 weeks
**Source:** [Phase 1 PRD](../docs-workbook1/PRD-phase-1-database-foundation.md)

---

## Executive Summary

Phase 1 establishes the business case and operational foundation before building advanced systems. The **ROI Assessment** is the quick win that delivers immediate value while producing the baseline metrics needed for all future phases.

---

## Impact vs Effort Matrix

```
                          IMPACT
                    LOW         HIGH
              ┌───────────┬───────────┐
         LOW  │           │  P1-ROI   │
              │           │  P1-WEB   │
    EFFORT    │           │  P1-FORM  │
              │           │  ★★★★★   │
              ├───────────┼───────────┤
              │           │  P1-DB    │
         MED  │           │  ★★★★★   │
              │           │           │
              └───────────┴───────────┘
```

**All Phase 1 opportunities are HIGH IMPACT.** The differentiation is effort level.

---

## Phase 1 Opportunities

### P1-ROI: ROI Assessment & Stakeholder Interviews

**Status:** ★★★★★ WEEK 1 QUICK WIN

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Shooting in the dark without baseline metrics; can't prove ROI without knowing starting point; no standardized processes documented |
| **Solution** | Structured stakeholder interviews to gather financial/operational baseline AND document current processes |
| **Impact** | HIGH - Client understands their own numbers; trust built through collaborative discovery; immediate SOP value |
| **Effort** | LOW - No development required; 4 interviews (~90 min total) |
| **Investment** | Part of Phase 1 ($5,000) |
| **Dependencies** | Stakeholder availability |
| **IP Risk** | LOW - Interview process, not proprietary data |
| **Timeline** | Week 1 |

#### Deliverables

| Deliverable | Description | Status |
|-------------|-------------|--------|
| Sandy Interview | Revenue, pricing, lead flow, close rate | ⬜ Pending |
| Matthew Interview | Operating costs, payroll, time tracking | ⬜ Pending |
| Alex Interview | Website traffic, social data, repetitive inquiries | ⬜ Pending |
| Scott Interview | Delivery data, build error frequency | ⬜ Pending |
| ROI Calculator | Populated with validated baseline metrics | ⬜ Pending |
| CODB Validation | Daily operating cost breakdown verified | ⬜ Pending |
| Lead Handling SOP | Process documentation from interviews | ⬜ Pending |
| Lot Operations SOP | Process documentation from interviews | ⬜ Pending |

#### Why This Is THE Quick Win

1. **Immediate Value** - Client learns their own business better (valuable even if we did nothing else)
2. **No Development** - Just structured conversations; can happen immediately
3. **Builds Trust** - Collaborative discovery, not sales pitch
4. **Dual Output** - ROI data + SOPs from same interviews
5. **Foundation** - All future ROI claims based on THEIR numbers

#### Interview → Output Mapping

| Stakeholder | Duration | ROI Output | SOP Output |
|-------------|----------|------------|------------|
| Sandy (Owner) | 30 min | Revenue, pricing, close rate | Lead Handling SOP |
| Matthew (Williams) | 20 min | Operating costs, CODB | Time tracking baseline |
| Alex (Website) | 15 min | Website traffic, lead sources | Repetitive inquiry patterns |
| Scott (Driver) | 15 min | Delivery data, build errors | Lot Operations SOP |

#### Success Metrics

- [ ] All 7 data gaps in ROI Calculator filled
- [ ] CODB validated (currently $400/day estimate)
- [ ] 2 initial SOPs created
- [ ] ROI presentation prepared for Sandy

**See:** [Stakeholder Questions](./stakeholder-questions-roi.md) | [ROI Calculator](./roi-calculator.md)

---

### P1-WEB: Website Quick Fixes

**Status:** ★★★★★ WEEK 1 PARALLEL

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Broken/blank images, broken embeds, mobile layout issues, slow load times, poor local SEO |
| **Solution** | Image audit and repair, embed fixes, responsive CSS, image compression, Northern AZ schema markup |
| **Impact** | HIGH - Immediate credibility improvement; better first impression; improved conversion |
| **Effort** | LOW - 3-5 days |
| **Investment** | Part of Phase 1 ($5,000) |
| **Dependencies** | Website admin access, hosting credentials |
| **IP Risk** | LOW - Standard website maintenance |
| **Timeline** | Week 1 (parallel with ROI Assessment) |

#### Deliverables

| Issue | Fix | Status |
|-------|-----|--------|
| Blank/broken images | Audit URLs, re-upload assets, fix CDN paths | ⬜ Pending |
| Broken embeds | Update embed codes, fix HTTPS mixed content | ⬜ Pending |
| Mobile layout | Responsive CSS, cross-device testing | ⬜ Pending |
| Slow load | Compress images, lazy loading | ⬜ Pending |
| Local SEO | Alt text, Northern AZ schema markup | ⬜ Pending |

#### Success Metrics

- [ ] Zero broken images on product pages
- [ ] Mobile UX score improved
- [ ] Page load < 3 seconds
- [ ] "Sheds near me" visibility improved

---

### P1-DB: Database Foundation

**Status:** ★★★★★ WEEK 2 FOUNDATION

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No centralized source of truth for inventory or overhead costs; data scattered across spreadsheets |
| **Solution** | Firestore collections for `products`, `financial_inputs`, `sops`, and `leads` with strict data hygiene |
| **Impact** | HIGH - Foundation for all subsequent tools (configurator, CRM, dashboards); enables accurate pricing |
| **Effort** | LOW-MEDIUM - 1 week for initial setup |
| **Investment** | Part of Phase 1 ($5,000) |
| **Dependencies** | Firebase/Google Cloud account (CEO-owned), existing inventory data |
| **IP Risk** | LOW - Generic product catalog structure |
| **Timeline** | Week 2 |

#### Deliverables

| Component | Description | Status |
|-----------|-------------|--------|
| Sheet 1: Master Shed Data | Centralized inventory with model_id, prices, specs | ⬜ Pending |
| Sheet 7: CODB Calculator | Fixed/variable costs, daily operating cost | ⬜ Pending |
| Firebase Setup | CEO-owned account, developer Editor access | ⬜ Pending |
| Data Migration | Products and financial inputs to Firestore | ⬜ Pending |

#### Data Standards

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Pure numbers | `1499.99` | `$1,499.99` |
| snake_case | `base_price` | `Base Price` |
| No symbols | `2500` | `2,500` |

#### Success Metrics

- [ ] All products migrated with clean data
- [ ] CODB Calculator populated from ROI Assessment
- [ ] snake_case compliance verified
- [ ] Developer access configured (Editor only)

---

### P1-FORM: Customer Onboarding Form

**Status:** ★★★★★ WEEK 2 PARALLEL

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | No guided lead capture on website; visitors leave without contact captured; 0% current capture rate |
| **Solution** | Mobile-friendly intake form with auto-responder and sales team notifications |
| **Impact** | HIGH - Start building CRM pipeline immediately; capture visitor intent and source |
| **Effort** | LOW - 3-5 days |
| **Investment** | Part of Phase 1 ($5,000) |
| **Dependencies** | Website access, Firestore setup (or temp Google Sheet), notification service |
| **IP Risk** | LOW - Standard form implementation |
| **Timeline** | Week 2 |

#### Form Fields

| Field | Type | Required |
|-------|------|----------|
| `full_name` | Text | Yes |
| `email` | Email | Yes |
| `phone` | Phone | Yes |
| `interested_in` | Dropdown (Shed types) | Yes |
| `preferred_size` | Dropdown | No |
| `timeline` | Dropdown (Immediate / 1-3 mo / 3-6 mo / Browsing) | Yes |
| `how_did_you_hear` | Dropdown (Facebook, Google, Referral, Drove by, Other) | Yes |
| `message` | Textarea | No |
| `preferred_lot` | Dropdown (Tuba City, Flagstaff, Williams) | No |

#### Placement

- Homepage (above fold CTA)
- Contact page
- Product pages (sidebar/footer)

#### Success Metrics

- [ ] Form submissions captured
- [ ] Auto-responder working
- [ ] Sales notified within 5 minutes
- [ ] First leads captured

---

## Consolidated Summary

| ID | Opportunity | Impact | Effort | Week | Priority |
|----|-------------|--------|--------|------|----------|
| **P1-ROI** | **ROI Assessment + Stakeholder Interviews** | ★★★★★ | **LOW** | 1 | **#1 QUICK WIN** |
| **P1-WEB** | **Website Quick Fixes** | ★★★★★ | LOW | 1 | #2 Parallel |
| **P1-DB** | **Database Foundation** | ★★★★★ | LOW-MED | 2 | #3 Foundation |
| **P1-FORM** | **Customer Onboarding Form** | ★★★★★ | LOW | 2 | #4 Parallel |

---

## Implementation Schedule

### Week 1: Quick Wins

```
Day 1-2: Schedule and conduct Sandy + Matthew interviews
Day 2-3: Conduct Alex + Scott interviews
Day 3-4: Populate ROI Calculator, draft initial SOPs
Day 1-5: Website fixes (parallel track)
Day 5:   ROI presentation prep
```

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Schedule interviews | AriseGroup | 1 | ⬜ |
| Sandy interview | AriseGroup | 1-2 | ⬜ |
| Matthew interview | AriseGroup | 1-2 | ⬜ |
| Alex interview | AriseGroup | 2-3 | ⬜ |
| Scott interview | AriseGroup | 2-3 | ⬜ |
| ROI Calculator populated | AriseGroup | 3-4 | ⬜ |
| Lead Handling SOP draft | AriseGroup | 4 | ⬜ |
| Lot Operations SOP draft | AriseGroup | 4 | ⬜ |
| Website image audit | Developer | 1-2 | ⬜ |
| Image fixes | Developer | 2-4 | ⬜ |
| Mobile fixes | Developer | 4-5 | ⬜ |
| SEO fixes | Developer | 5 | ⬜ |

### Week 2: Foundation

```
Day 1-2: Firebase setup, data migration start
Day 2-3: Sheet 1 (Master Data) + Sheet 7 (CODB) population
Day 3-4: Onboarding form build
Day 4-5: Form deployment + testing + handoff
```

| Task | Owner | Day | Status |
|------|-------|-----|--------|
| Firebase account setup | Sandy (CEO) | 1 | ⬜ |
| Developer access config | AriseGroup | 1 | ⬜ |
| Products collection setup | Developer | 1-2 | ⬜ |
| Sheet 1 data migration | Developer | 2-3 | ⬜ |
| Sheet 7 CODB population | AriseGroup | 2-3 | ⬜ |
| Onboarding form design | Developer | 3 | ⬜ |
| Form implementation | Developer | 3-4 | ⬜ |
| Notifications setup | Developer | 4 | ⬜ |
| Testing | All | 5 | ⬜ |

---

## Risk Assessment

| Opportunity | Risk Level | Key Risk | Mitigation |
|-------------|------------|----------|------------|
| P1-ROI | LOW | Stakeholder availability | Schedule early, flexible timing |
| P1-WEB | LOW | Hosting complexity | Document issues, escalate if needed |
| P1-DB | LOW | Data quality | Strict hygiene rules, validation |
| P1-FORM | LOW | Form abandonment | Keep short, progressive disclosure |

---

## Dependencies Map

```
P1-ROI (Week 1)
    │
    └──► P1-DB (Week 2) - CODB data feeds into Sheet 7

P1-WEB (Week 1)
    │
    └──► P1-FORM (Week 2) - Website must be credible before form drives traffic

P1-DB (Week 2)
    │
    └──► P1-FORM (Week 2) - Leads collection needs Firestore setup
```

---

## Success Criteria

### Phase 1 Complete When:

- [ ] ROI Calculator fully populated with validated data
- [ ] CODB verified (not estimated)
- [ ] Website images loading, mobile working
- [ ] Onboarding form live and capturing leads
- [ ] Database foundation in place
- [ ] Client (Sandy) confident in baseline numbers

### Handoff to Phase 2:

- [ ] All Phase 1 deliverables complete
- [ ] ROI presentation delivered to Sandy
- [ ] Phase 2 scope confirmed
- [ ] Second payment ($5,000) scheduled

---

## ROI Justification (From Discovery)

**Known Reference Points:**

| Factor | Value | Source |
|--------|-------|--------|
| Build error cost | $24,000 lost sale | Dec 22 Discovery |
| Build error frequency | 5-6 per 40 orders/year | Dec 22 Discovery |
| Lead drop after pausing ads | 75% decline | Dec 22 Discovery |
| Current lead capture rate | 0% | Dec 28 Meeting |
| Current monthly revenue | ~$20,000 | Dec 30 Meeting |
| Target monthly revenue | $50,000 | Dec 30 Meeting |

**Phase 1 ROI Potential:**

| Improvement | Conservative Impact |
|-------------|---------------------|
| SOPs prevent 1 build error | $24,000 saved |
| Form captures 5 leads/month | 5 × $5,000 × 25% = $6,250/month |
| Website fixes improve conversion | Unmeasured until baseline set |

**Total Phase 1 Investment:** $5,000
**Potential Annual Impact:** $50,000+ (conservative)
**ROI:** 900%+ (to be validated with actual data)

---

## Related Documents

- [Phase 1 PRD](../docs-workbook1/PRD-phase-1-database-foundation.md)
- [ROI Calculator](./roi-calculator.md)
- [Stakeholder Questions](./stakeholder-questions-roi.md)
- [Main Opportunity Matrix](./opportunity-matrix.md)

---

**Last Updated:** January 3, 2026
**Status:** Ready for execution
**Next Action:** Schedule stakeholder interviews
