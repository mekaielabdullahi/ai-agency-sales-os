# Andrew & Kelsey Deep Dive - January 14, 2026

**Recording:** https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg

## Attendees
- Matthew
- Chris
- Mekaiel
- Trent
- Andrew (E-commerce expert, ex-Amazon - potential JV partner)
- Kelsey (Plotter Mechanix)

## Meeting Purpose
Introduce Andrew for potential supplies JV and align on automation priorities.

---

## Key Takeaways

1. **Supplies JV:** Andrew (e-commerce expert, ex-Amazon) exploring JV to manage Plotter Mechanics' supplies business. Strategy: build direct, local supply chain, avoiding Amazon FBA risks.

2. **Phone System Migration:** Kelsey migrating from Vonage to Quo. Will centralize communications and auto-transcribe calls, solving major info-silo problem.

3. **Inventory Management:** Key priority - implement system to track ~$50k in inventory (parts, consumables, used equipment). Enables accurate costing, reduces waste, creates new revenue from used parts.

4. **Jobber Automation:** Building N8N workflow to log Quo call transcripts in Jobber. Challenge: defining when to create new "Request" vs. adding notes to existing one.

---

## Phase 1 Relevant Information
*Context that affects current delivery work*

### Phone System (Quo) - ACTIVE PRIORITY
- Kelsey successfully tested forwarding personal cell to Quo - app rings and records
- **Plan:** Port main Vonage business number AND Kelsey's cell to Quo
- **Users:** Start with 3 users (Kelsey, Alyssa, Joe)
- Need to replicate Vonage IVR menu system in Quo
- Alyssa needs Quo installed and trained to answer after 4 rings

### Jobber Automation Workflow - ACTIVE
- Goal: Auto-log Quo call transcripts as notes in Jobber
- **Challenge:** Jobber Request status doesn't update automatically
- Must define logic for new Request vs. adding notes to existing
- **Breakthrough:** Discovered how to use Claude Code to query Jobber GraphQL API - full schema access for robust logic

### Immediate Technical Tasks
- Disable Vonage admin 2FA
- Document existing IVR
- Prep port to Quo (Vonage + Kelsey cell)
- Merge plotter-mechanics-linux repo into main plotter-mechanics repo
- Merge n8n workflows into Plotter Mechanics repo

---

## Phase 2+ Roadmap Items
*Future considerations for proposal and planning*

### The Core Problem (Context for All Future Work)
Plotter Mechanics' growth constrained by manual, siloed processes:
- **Communication Gaps:** Kelsey's service focus leaves no time for sales/quoting. Alyssa lacks industry knowledge for effective follow-up.
- **Inventory Chaos:** No system for ~$50k in parts, consumables, used equipment
  - Impact: Inaccurate costing, wasted parts, missed sales
  - Example: $1,200 power supplies from parted-out machines lost without system
- **Cash Flow Issues:** AR reached $100k due to poor payment follow-up

### Inventory Management System
- Kelsey demoing "Ply" on Friday
- Need to design data model and integrate with Jobber
- Used parts from parted-out machines = new revenue stream

### Supplies JV Opportunity (Andrew)
- **Andrew's approach:**
  - Avoids Amazon FBA (brand-holder focus, account suspension risk, poor customer service)
  - Prefers direct fulfillment to control customer experience and provide expert support
  - Local, direct-to-customer model = better prices and service than Amazon
- **Kelsey's vision:**
  - Partner to manage all supplies logistics (sourcing, shipping, quotes)
  - Strategy: Free compatible ink trials to build customer confidence

### Revenue Protection
- Implement $75 non-refundable travel fee in Jobber
- Collect CC on file

### Content & Marketing
- Create shared Dropbox folder for social media content
- Export contacts from Capsule for team review

---

## Action Items

### Kelsey
- [x] Forward personal cell to Quo for live test
- [ ] Install Quo on Alyssa's phone for temporary call handling
- [ ] Create shared Dropbox folder for social media content
- [ ] Export contacts from Capsule for team review
- [ ] Demo "Ply" inventory software on Friday and report back
- [ ] Disable Vonage admin 2FA
- [ ] Document existing IVR

### Trent & Matthew
- [ ] Begin number porting process (Vonage + Kelsey's cell to Quo)
- [ ] Configure Quo to replicate Vonage menu system
- [ ] Refine N8N → Jobber workflow to handle Request statuses correctly
- [ ] Merge plotter-mechanics-linux repo into main plotter-mechanics repo
- [ ] Merge n8n workflows into Plotter Mechanics repo; push to GitHub

### Matthew
- [ ] Contact FBM network to investigate Andrew's Amazon account suspension

### Team
- [ ] Schedule 2nd Alyssa meeting
- [ ] Schedule Joe meeting
- [ ] Create Dropbox folder for Kelsey; share w/ Chris, Matthew, Trent

---

## Timestamped References
- [Dropbox folder creation](https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg?timestamp=2581.9999)
- [Alyssa/Joe meeting scheduling](https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg?timestamp=2605.9999)
- [Vonage 2FA/IVR/porting](https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg?timestamp=2835.9999)
- [Capsule export](https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg?timestamp=3769.9999)
- [$75 travel fee implementation](https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg?timestamp=4678.9999)
- [Quo on Alyssa's phone](https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg?timestamp=7950.9999)
- [N8N workflow merge](https://fathom.video/share/QaQrA5ztXaSzEH63m7HWY_pK_dJvhNLg?timestamp=10979.9999)
