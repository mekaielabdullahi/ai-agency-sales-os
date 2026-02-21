# Megan Interview Preparation - Ply Implementation Status

**Interview Target:** Megan (Plotter Mechanix - Inventory/Operations Lead)
**Scheduled:** ASAP (before Saturday, Feb 15 Kelsey call)
**Duration:** 45-60 minutes
**Purpose:** Validate Ply implementation status to accurately scope Phase 2 work

---

## Interview Objectives

### Primary Goals
1. **Determine what's already implemented** - Avoid duplicating work Megan is already getting from Ply
2. **Identify real gaps** - What Ply can't do vs. what isn't configured yet
3. **Validate our $8K "Ply Enhancements" scope** - Is this still the right price/scope?
4. **Get API access info** - Required for Quo ↔ Ply integration

### Success Criteria
- ✅ Clear understanding of Ply implementation status (0-100%)
- ✅ Confirmation of Jobber ↔ Ply sync status (active/inactive)
- ✅ Used parts tracking approach validated (native Tools feature vs. custom build)
- ✅ API credentials obtained or path to obtaining them confirmed
- ✅ Revised Phase 2 scope ready for Saturday's Kelsey call

---

## Questions (Priority Order)

### Section 1: Implementation Status (P0 - BLOCKING)

**1. Did you purchase Ply's warehouse audit/implementation service ($5K+)?**
- [ ] Yes - they purchased it
- [ ] No - just using Ply software alone
- [ ] Don't know / unsure

**If YES, follow-up:**
- What week of the 4-week onboarding are you currently in?
- Who from Ply is your implementation contact?
- What's been completed so far vs. still in progress?

---

**2. What Ply features are actively being used RIGHT NOW?**

Check all that apply:
- [ ] Smart Catalog Management (materials organized in Ply)
- [ ] Stock Location Management (warehouses + trucks configured)
- [ ] Barcode System (barcodes created, scanning active)
- [ ] Mobile App (iOS/Android - team using it?)
- [ ] Auto-Replenishment (min/max thresholds set)
- [ ] Transfer Management (moving materials between locations)
- [ ] Tools Tracking (new feature - tracking serialized equipment)
- [ ] Purchasing & RFQ Management (managing purchase orders in Ply)
- [ ] Supplier Integrations (Winsupply, Ferguson, etc. connected)
- [ ] QuickBooks Integration (A/R, A/P syncing)
- [ ] Jobber Integration (materials, jobs, users syncing)

**For each checked feature, ask:**
- How long have you been using it?
- Is it working as expected?
- Any pain points or limitations?

---

**3. Which features are planned but NOT YET implemented?**

List features from above that are:
- [ ] Planned for future (when?)
- [ ] Not sure how to set up
- [ ] Blocked by something (what?)
- [ ] Not relevant to Plotter Mechanix

---

### Section 2: Jobber Integration (P0 - BLOCKING)

**4. Is the Jobber ↔ Ply material sync currently ACTIVE?**
- [ ] Yes - materials are syncing
- [ ] No - not set up yet
- [ ] Partially - some sync, some don't
- [ ] Don't know / unsure

**If YES, follow-up:**
- When was it activated?
- Are there any sync issues or errors?
- Which direction is working? (Jobber → Ply, Ply → Jobber, both?)

---

**5. Are jobs from Jobber syncing to Ply automatically?**
- [ ] Yes - jobs appear in Ply
- [ ] No - not syncing
- [ ] Don't know / unsure

**If YES, follow-up:**
- Can you see job details in Ply (customer, address, assigned tech, etc.)?
- Can you allocate materials to jobs in Ply?

---

**6. How often does the sync run? Real-time or scheduled?**
- [ ] Real-time (webhooks - instant updates)
- [ ] Scheduled (every X hours/minutes)
- [ ] Manual (have to press a sync button)
- [ ] Don't know / unsure

---

### Section 3: Used Parts & Tools Tracking (P0 - BLOCKING)

**7. How are you CURRENTLY tracking used parts from parted-out machines?**

Current method:
- [ ] Spreadsheet (Excel, Google Sheets)
- [ ] Jobber (as materials?)
- [ ] Ply (in some way?)
- [ ] Paper-based system
- [ ] Not tracking at all
- [ ] Other: _______________

**Follow-up:**
- What information do you track? (part type, machine source, condition, price, location?)
- Who is responsible for updating this?
- How do Kelsey/Andrew know if a used part is in stock during a Quo call?

---

**8. Have you explored Ply's "Tools" tracking feature for used parts?**
- [ ] Yes - already using it for used parts
- [ ] Yes - aware of it but not using it yet
- [ ] No - didn't know this feature existed
- [ ] No - not sure what this feature does

**If aware of Tools feature:**
- Why haven't you used it for used parts yet?
- What would it take to start using it?

---

**9. What's preventing used parts from being tracked in Ply TODAY?**

Potential blockers:
- [ ] Don't know how to set it up
- [ ] Ply doesn't support this use case
- [ ] Team doesn't have time to configure it
- [ ] Waiting for someone (Ply support? Us?) to help
- [ ] Process isn't defined yet (when to add, who adds it, etc.)
- [ ] Other: _______________

---

### Section 4: Technical Integration (P1 - IMPORTANT)

**10. Do you have API access credentials for Ply?**
- [ ] Yes - have API key/token
- [ ] No - don't have it yet
- [ ] Don't know / unsure what this means

**If YES:**
- Can you share the API credentials (securely)?
- Have you used the API for anything else?

**If NO:**
- Can you request API access from Ply support?
- Who needs to approve this?

---

**11. What custom material categories have you created in Ply?**

Examples:
- New parts (ink cartridges, printheads, belts, etc.)
- Used parts (salvaged from parted machines)
- Consumables (paper, cleaning supplies)
- Tools/equipment
- Other: _______________

**Follow-up:**
- How are categories organized? (by machine model? by part type?)
- Are used parts in a separate category?

---

**12. Are barcodes being used for inventory intake?**
- [ ] Yes - all inventory is barcoded
- [ ] Partially - some items have barcodes
- [ ] No - not using barcodes yet
- [ ] Don't know / unsure

**If YES or PARTIALLY:**
- Who creates the barcodes? (Ply auto-generates? Manual entry?)
- What barcode scanner/printer are you using?
- Is the team actually scanning items in the field?

**If NO:**
- What's blocking barcode implementation?
- Is this something you want to implement?

---

### Section 5: Pain Points & Gaps (P1 - IMPORTANT)

**13. What's the BIGGEST gap in Ply that still causes problems?**

Open-ended - let Megan talk. Listen for:
- Integration gaps (e.g., "Quo can't see Ply data")
- Workflow gaps (e.g., "Can't track used parts properly")
- Usability gaps (e.g., "Too complicated for techs to use")
- Data gaps (e.g., "Pricing data is wrong")

---

**14. Where does Ply fall short for Plotter Mechanix's specific needs?**

Potential areas:
- Used parts workflow
- Integration with Quo
- Custom reporting
- Mobile app usability for techs
- Barcode scanning workflow
- Other: _______________

---

**15. What manual workarounds are you STILL doing despite having Ply?**

Examples:
- Manually checking inventory in spreadsheets
- Calling warehouse to check stock during Quo calls
- Manually updating Jobber with inventory changes
- Manually tracking used parts outside Ply
- Other: _______________

---

### Section 6: Quo Integration Context (P1)

**16. When Kelsey/Andrew are on a Quo call and a customer asks "Do you have X in stock?", what do they do TODAY?**

Current process:
1. _______________
2. _______________
3. _______________

**Follow-up:**
- How long does this take?
- How often does this happen per day?
- Do they sometimes give wrong answers because data is out of date?

---

**17. What would the IDEAL experience be for checking inventory during a Quo call?**

Megan's vision:
- _______________

**Probe for:**
- Just quantity? Or also location (warehouse vs. truck)?
- Need pricing info too?
- Need to see used parts vs. new parts separately?
- Need to reserve/allocate part during the call?

---

## Interview Format

### Opening (5 min)
- **Purpose:** "We want to make sure Phase 2 delivers real value and doesn't duplicate work you're already getting from Ply's native features."
- **Context:** "We've been studying Ply's capabilities and realized it's MORE powerful than we initially thought. We need to understand what's already working vs. what still needs to be built."
- **Logistics:** "This should take 45-60 minutes. I'll be taking notes and may ask follow-up questions to clarify."

### Main Interview (35-45 min)
- Work through questions in priority order (P0 first)
- Take detailed notes on answers
- Ask follow-ups to clarify ambiguities
- Record specific examples and pain points

### Closing (5-10 min)
- **Recap:** Summarize what we learned
- **Next Steps:** "Based on this, we'll revise the Phase 2 scope and pricing. We'll present the updated proposal on Saturday's call with Kelsey."
- **Action Items:** Any credentials, screenshots, or access Megan needs to provide

---

## Notes Template

### Section 1: Implementation Status
**Q1 - Warehouse Audit Service:**
- Answer: _______________
- Follow-up notes: _______________

**Q2 - Active Features:**
- Features in use: _______________
- Pain points: _______________

**Q3 - Planned Features:**
- Not yet implemented: _______________
- Blockers: _______________

---

### Section 2: Jobber Integration
**Q4 - Material Sync Status:**
- Answer: _______________
- Notes: _______________

**Q5 - Job Sync Status:**
- Answer: _______________
- Notes: _______________

**Q6 - Sync Frequency:**
- Answer: _______________
- Notes: _______________

---

### Section 3: Used Parts Tracking
**Q7 - Current Method:**
- Answer: _______________
- Notes: _______________

**Q8 - Tools Feature Awareness:**
- Answer: _______________
- Notes: _______________

**Q9 - Blockers:**
- Answer: _______________
- Notes: _______________

---

### Section 4: Technical Integration
**Q10 - API Access:**
- Answer: _______________
- Notes: _______________

**Q11 - Custom Categories:**
- Answer: _______________
- Notes: _______________

**Q12 - Barcode Status:**
- Answer: _______________
- Notes: _______________

---

### Section 5: Pain Points & Gaps
**Q13 - Biggest Gap:**
- Answer: _______________

**Q14 - Ply Shortcomings:**
- Answer: _______________

**Q15 - Manual Workarounds:**
- Answer: _______________

---

### Section 6: Quo Integration
**Q16 - Current Inventory Check Process:**
- Answer: _______________

**Q17 - Ideal Experience:**
- Answer: _______________

---

## Post-Interview Action Items

### Immediate (Same Day)
- [ ] Compile interview notes into summary document
- [ ] Identify which Phase 2 scope items are still valid
- [ ] Flag any scope items that overlap with Ply native features
- [ ] Draft revised Phase 2 pricing based on findings

### Before Saturday Call
- [ ] Update Phase 2 proposal with revised scope
- [ ] Create ROI slide using Ply's $60K case study
- [ ] Prepare talking points for Kelsey call
- [ ] Share updated proposal with team for review

---

## Key Insights to Look For

### Red Flags (Scope Reduction)
- ✅ Jobber ↔ Ply sync is already active and working
- ✅ Used parts tracking is already solved with Ply's Tools feature
- ✅ Megan purchased Ply's $5K warehouse audit service
- ✅ Most Ply features are actively being used

**IMPLICATION:** Our $8K scope may drop to $5K (Quo integration only)

---

### Green Flags (Scope Validation)
- ❌ Jobber ↔ Ply sync is NOT active or working
- ❌ Used parts tracking is still manual (spreadsheets, etc.)
- ❌ Megan did NOT purchase Ply's warehouse audit service
- ❌ Many Ply features are not configured or not being used

**IMPLICATION:** Our $8K scope (or higher) is justified

---

### Mixed Signals (Partial Scope)
- ⚠️ Some features are working, others are not
- ⚠️ Ply is partially implemented but team needs training
- ⚠️ Used parts tracking is partially in Ply but not working well

**IMPLICATION:** Scope somewhere between $5K-8K, focused on completion + integration

---

## Expected Outcome

By the end of this interview, we should be able to answer:

1. **What percentage of Ply's capabilities is Plotter Mechanix actively using?**
   - Estimate: ____%

2. **Is the $8K "Ply Enhancements" scope still valid?**
   - [ ] Yes - keep as-is
   - [ ] No - reduce to $5K (Quo integration only)
   - [ ] No - increase to $10K+ (more work than we thought)
   - [ ] Revise - different scope entirely

3. **What is the #1 deliverable that would provide immediate value?**
   - Answer: _______________

4. **Can we confidently present a revised Phase 2 proposal on Saturday?**
   - [ ] Yes - ready to present
   - [ ] No - need more research/clarification

---

*Created: February 8, 2026*
*Interview Target: ASAP (before Feb 15)*
*Next Action: Schedule interview with Megan*
