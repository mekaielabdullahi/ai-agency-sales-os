# Plotter Mechanix Phase 2

**Status:** Ready for internal team review
**Investment:** $47,000
**Expected ROI:** $116,600/year (248% return, 4.8 month payback)
**Timeline:** 4-6 weeks
**Team:** Mekaiel, Trent, Chris, Matthew

---

## Folder Structure

```
phase-2/
├── README.md (this file)                    # 📍 YOU ARE HERE
│
├── to-review/                               # ✅ FINAL DELIVERABLES (start here)
│   ├── README.md
│   ├── PHASE-2-PROPOSAL.md                  # Client-facing $47k proposal
│   ├── VALIDATION-ACTION-PLAN.md            # 2-3 week validation process
│   ├── QUICK-START-GUIDE.md                 # Team execution guide
│   └── to-send/                             # 6 ready-to-send emails
│       ├── 01-email-to-kelsey-validation-kickoff.md
│       ├── 02-alyssa-time-tracking-template.md
│       ├── 03-kelsey-time-tracking-template.md
│       ├── 04-megan-interview-scheduling.md
│       ├── 05-andrew-interview-scheduling.md
│       └── 06-jobber-data-request.md
│
├── internal/                                # ✅ CURRENT REFERENCE (3 docs)
│   ├── README.md
│   ├── business-problems-analysis.md        # 10x scale framework
│   ├── pricing-strategy.md                  # How we arrived at $47k
│   └── quo-ply-integration-technical.md     # Chat agent technical deep dive
│
└── historical/                              # ⚠️ OUTDATED (do not use)
    ├── README.md                            # ⚠️ Clear warnings
    ├── gap-analysis.md
    ├── implementation-plan.md
    ├── pricing-breakdown.md
    └── roi-validation-plan.md
```

**Legend:**
- ✅ **CURRENT** - Safe to review and use
- ⚠️ **OUTDATED** - Historical context only, do not use for decisions

---

## 🚀 Quick Start (Team Review)

### Step 1: Review Final Deliverables (Start Here)

**📂 Go to:** `to-review/`

1. **Read first:** `QUICK-START-GUIDE.md` (15 min)
   - Internal review checklist
   - Your role-specific tasks
   - Go/no-go decision framework

2. **Review main proposal:** `PHASE-2-PROPOSAL.md` (30 min)
   - Client-facing $47k proposal
   - 10x scale framework
   - 5 deliverables breakdown
   - Pricing justification

3. **Review validation plan:** `VALIDATION-ACTION-PLAN.md` (20 min)
   - 2-3 week validation process
   - Time tracking templates
   - Interview guides

### Step 2: Review Supporting Analysis (Optional)

**📂 Go to:** `internal/`

- `business-problems-analysis.md` - 10x scale framework details
- `pricing-strategy.md` - How we arrived at $47k (AAA framework)
- `quo-ply-integration-technical.md` - Chat agent technical approach

**⚠️ Do NOT review:** `historical/` folder (outdated docs)

### Step 3: Complete Your Review Tasks

**Mekaiel:** Pricing strategy + technical approach
**Trent:** Business case + ROI calculations
**Chris:** Filming/training feasibility
**Matthew:** Validation process + overall proposal

### Step 4: Team Discussion

- Developer capacity?
- Margin validation (40-50% target)?
- 2-3 week availability for validation phase?
- **Go/no-go decision**

---

## 📧 After Team Approval (Client Communication)

**Only proceed after internal review complete and go decision made:**

1. **Send:** `to-review/to-send/01-email-to-kelsey-validation-kickoff.md`
2. **Run validation:** 2-3 week data collection process
3. **Update proposal:** With validated ROI numbers
4. **Present:** `to-review/PHASE-2-PROPOSAL.md` to Kelsey/Nikki/Megan
5. **Close:** $42k-$57k range

---

## What This Phase Includes

### Deliverables ($47,000)

| Deliverable | Investment | Annual ROI | Timeline |
|-------------|------------|------------|----------|
| **Training System** | $18,000 | $39,000 | Chris filming, 25-30 videos, knowledge base |
| **Equipment CRM** | $10,000 | $37,600 | Customer equipment database, service contract scoring |
| **Unified Chat Agent** | $10,000 | $25,000 | Single interface for Ply, Quo, Jobber, QuickBooks |
| **Email Automation** | $5,000 | $15,000 | Vendor pricing extraction, RMA routing, PO tracking |
| **Integration Work** | $4,000 | Efficiency | Connect all systems via n8n |
| **TOTAL** | **$47,000** | **$116,600** | **4-6 weeks** |

### Timeline

- **Week 1:** Discovery, interviews (Megan, Andrew), Equipment CRM design, Chris filming setup
- **Week 2-3:** Parallel build (Equipment CRM, 15 training videos, chat agent foundation, email automation)
- **Week 4-5:** Integration, 10+ additional videos, all systems connected
- **Week 6:** Training, testing, handoff (optional polish week)

---

## Current Status

### ✅ Complete
- [x] Business problems analysis (10x scale framework)
- [x] Pricing strategy using AAA framework (2.5:1 value-to-price ratio)
- [x] Technical architecture (chat agent approach)
- [x] Client-facing proposal
- [x] Validation action plan with templates
- [x] Ready-to-send emails (6 templates)

### 🔄 In Progress
- [ ] **Internal team review** (Mekaiel, Trent, Chris, Matthew)
- [ ] Developer capacity validation
- [ ] Margin analysis
- [ ] Go/no-go decision

### ⏳ Pending (After Internal Review)
- [ ] Send validation kickoff email to Kelsey
- [ ] Run 2-3 week validation phase
- [ ] Update proposal with validated ROI
- [ ] Present Phase 2 to client
- [ ] Close deal ($42k-$57k range)

---

## Key Decisions

### Pricing: $47,000
- AAA framework: $153,600 ÷ 2.5 = $61,440 recommended
- Our price: $47,000 (23% below to account for vendor fatigue)
- Value-to-price ratio: 3.3:1 (client gets $3.30 per $1 invested)

### Technical Approach
- **Chat Agent** (solves "can't modify Quo UI" constraint)
- Tool access to: Ply, Quo, Jobber, QuickBooks, Equipment CRM
- Auto-populates customer context when calls come in
- Natural language queries eliminate context-switching

### Support, Don't Replace
- **Megan's Ply:** We query via API, fill gaps (equipment history, used parts)
- **Andrew's supplies:** Interview first, build tools that FIT his workflow
- **Phase 1 foundation:** Build on existing Quo→Jobber webhook infrastructure

---

## Internal Review Checklist

**Before contacting Kelsey, team must complete:**

- [ ] **Mekaiel** reviews pricing strategy and technical approach
- [ ] **Trent** reviews business case and ROI calculations
- [ ] **Chris** reviews filming/training deliverables for feasibility
- [ ] **Matthew** reviews validation process and overall proposal
- [ ] Team validates developer capacity
- [ ] Team validates margin (40-50% target)
- [ ] Team confirms 2-3 week availability for validation phase
- [ ] **Go/no-go decision** before sending any client emails

---

## Validation Phase (2-3 Weeks)

**Purpose:** Replace assumptions with real data from Plotter Mechanix

### Week 1-2: Data Collection
- Time tracking: Alyssa (5 activities) + Kelsey (training time)
- Interviews: Megan (Ply status), Andrew (supplies process)
- Jobber data export: Customers, jobs, service frequency
- Business financials: Revenue, customer count

### Week 3: Analysis & Update
- Compile validation data into ROI report
- Update PHASE-2-PROPOSAL.md with validated numbers
- Adjust pricing if ROI doesn't support $47k (maintain 2.5:1+ ratio)

### Week 4: Present & Close
- Present proposal with data-backed ROI
- Handle objections
- Close at $42k-$57k (depending on validated scope)

---

## Success Criteria

### Internal Review Success
- ✅ All 4 team members reviewed and approved
- ✅ Developer capacity confirmed
- ✅ Margin validated (40-50%)
- ✅ Technical feasibility confirmed
- ✅ Go decision made

### Validation Phase Success
- ✅ 70%+ of ROI assumptions replaced with validated data
- ✅ Megan and Andrew interviews completed
- ✅ Time tracking data collected (5 days minimum)
- ✅ Jobber data analyzed
- ✅ Confidence level HIGH before presenting

### Close Success
- ✅ Contract signed at $42k-$57k
- ✅ 50% deposit collected ($21k-$28.5k)
- ✅ Client confident in value (not just hoping it works)
- ✅ Delivery timeline agreed (4-6 weeks)

---

## Risk Mitigation

### Risk 1: Validated ROI Lower Than Estimated
**Mitigation:** Adjust price or scope to maintain 2.5:1+ value-to-price ratio

### Risk 2: Team Capacity Constraint
**Mitigation:** Defer Phase 2, focus on other priorities, revisit in 1-2 months

### Risk 3: Ply API Doesn't Exist or Is Limited
**Mitigation:** Build standalone inventory lookup tool (fallback option)

### Risk 4: Budget Ceiling Lower Than $47k
**Mitigation:** Offer phased delivery (Phase 2A + 2B) or modular approach

---

## Next Steps

1. **Team reviews internal/to-review folders** (this week)
2. **Team discusses capacity, margin, go/no-go** (team meeting)
3. **If go:** Send validation kickoff email to Kelsey
4. **If no-go:** Document decision and revisit timeline

---

## Questions?

- **"What if internal review shows $47k is too high?"** → Adjust price/scope or defer
- **"What if we don't have developer capacity?"** → Defer or find external developer
- **"What if Chris can't do 25-30 videos in 4-6 weeks?"** → Reduce scope or extend timeline
- **"What if Ply API doesn't exist?"** → Fallback to standalone tool (less elegant but works)

---

*Last Updated: January 24, 2026*
*Owner: Matthew Kerns*
*Status: Awaiting internal team review*
