# Human-AI Oversight Design

## Core Philosophy

**The Architect's role is to thoughtfully integrate AI and software into organizations - automating the right things while ensuring humans maintain oversight where it matters.**

---

## The Key Question Framework

Before automating any step, ask:

1. **Why should AI do this?** What makes AI better at this than a human?
2. **Why should a human do this?** What requires human judgment, accountability, or oversight?
3. **How do we combine AI efficiency with human judgment?**

---

## Invoice/Receipts Processing: Human-AI Balance

### What AI Should Handle (Routine + Pattern Recognition)
- Email monitoring and ingestion
- Document classification (invoice vs receipt)
- OCR and text extraction
- Data field extraction (vendor, amount, date, etc.)
- Validation against business rules
- Flagging anomalies or low-confidence items
- Generating summaries and recommendations

### What Humans Should Handle (Judgment + Accountability)
- **Final approval** before data goes into financial systems
- Resolving flagged anomalies
- Handling edge cases AI can't classify
- Accountability for financial accuracy
- Business rule exceptions

---

## The Critical Question: Does Linh Still Check Every Single One?

### Current State (Manual)
- Linh checks every invoice/receipt manually
- Time: 15-20 hours/month
- Error rate: ~5%

### Proposed AI-Assisted State

**Option A: AI Pre-processes, Human Verifies All**
```
AI extracts data → AI generates analysis + recommendation → Linh verifies each one
```
- Linh still sees everything
- Faster per-item (data already extracted)
- But still touches 200+ items/month
- Time savings: ~50% (10 hours/month instead of 20)

**Option B: AI Pre-processes, Human Spot-Checks**
```
AI extracts data → AI flags confidence levels → Linh reviews LOW confidence only
```
- High confidence (>95%): Auto-approved, Linh sees summary
- Medium confidence (80-95%): Quick review
- Low confidence (<80%): Full manual review
- Time savings: ~80% (4 hours/month)
- Risk: Errors in "high confidence" items slip through

**Option C: AI Pre-processes, Human Approves Batches**
```
AI extracts data → AI generates batch report → Linh approves batches
```
- Daily/weekly batch summaries
- Linh reviews totals and anomalies
- Individual items only if flagged
- Time savings: ~90% (2 hours/month)
- Risk: Less visibility into individual transactions

---

## Recommended Approach: Tiered Review System

### Tier 1: Auto-Process (No Human Touch)
**Criteria:**
- AI confidence >98%
- Amount under $500
- Known vendor (seen 5+ times)
- Matches expected patterns

**Human sees:** End-of-day summary only

### Tier 2: Quick Review (Human Glance)
**Criteria:**
- AI confidence 90-98%
- Amount $500-$5,000
- Known vendor with slight variations
- Minor anomalies flagged

**Human sees:** Pre-filled form, just confirm or edit

### Tier 3: Full Review (Human Decision)
**Criteria:**
- AI confidence <90%
- Amount >$5,000
- New vendor
- Significant anomalies
- Refunds, credits, unusual items

**Human sees:** Full document + AI analysis + recommendation

---

## What This Means for the Build

### Current System (Fix First)
- Get accuracy to 98%+ (currently <80%)
- This unlocks the ability to trust AI for Tier 1

### Enhancement Needed
- **Confidence scoring** per extraction
- **Vendor recognition** (learn from history)
- **Anomaly detection** (flag unusual amounts, patterns)
- **Tiered review interface** (not just one view for all)
- **Summary dashboard** (batch approval capability)

### UI Changes
- Don't show Linh everything equally
- Highlight what needs attention
- Make high-confidence items dismissable in bulk
- Focus human time on low-confidence items

---

## The ROI Shift

### Old Thinking
"Automate everything, human just clicks approve"

### New Thinking
"AI handles the routine, human handles the judgment"

### Practical Impact
- If 80% of invoices are routine → AI handles fully
- If 15% need quick review → 30 seconds each
- If 5% need full review → 3-5 minutes each

**200 invoices/month:**
- 160 auto-processed (0 min) = 0 hours
- 30 quick review (0.5 min each) = 15 min
- 10 full review (4 min each) = 40 min
- **Total: ~1 hour/month** (vs 15-20 hours manual)

---

## Questions to Answer with Linh

1. What's his comfort level with auto-approving high-confidence items?
2. What dollar threshold requires his eyes?
3. What vendor types always need review?
4. Is daily batch review acceptable, or does he need real-time?
5. What anomalies should always escalate to him?

---

## Next Steps

1. [ ] Fix accuracy to 98%+ (prerequisite for trust)
2. [ ] Add confidence scoring to extractions
3. [ ] Build tiered review interface
4. [ ] Discuss thresholds with Linh
5. [ ] Implement batch approval for Tier 1
6. [ ] Measure actual time savings

---

**Key Insight:** The goal isn't to remove Linh from the process. It's to focus his time on the 5-20% that actually needs human judgment, while AI handles the 80%+ that's routine.

---

*Added: December 13, 2024*
*Context: Thinking during hike about the right balance of AI efficiency + human oversight*
