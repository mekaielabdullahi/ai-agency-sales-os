# Quo ↔ Ply Integration - Technical Deep Dive

**Created:** January 24, 2026
**Purpose:** Explain what "see inventory during calls" actually means
**Investment:** Part of $8,000 Ply Enhancement Layer

---

## The Problem (Current State)

### Scenario: Customer calls Alyssa

**Customer:** "Hi, do you have a maintenance kit for my HP DesignJet T730?"

**Alyssa's Current Process:**
1. "Let me check, can you hold?"
2. Opens Ply on her computer (separate app)
3. Searches for "HP DesignJet T730 maintenance kit"
4. Checks stock level
5. Returns to call: "Yes, we have 2 in stock"
6. Customer asks: "What about the plotter belt?"
7. Repeat steps 1-5

**Problems:**
- Interrupts call flow 10+ times/day
- Customer on hold (poor experience)
- Alyssa context-switching (computer → phone → computer)
- Increases call time 2-5 minutes per call
- Sometimes forgets to return to customer
- Can't quote accurately on first call = callbacks

**Annual Cost:** ~$62,500/year in Kelsey's time wasted (10 interruptions/day × 5 min × $300/hr × 250 days)

---

## The Solution (Integrated State)

### Same Scenario: Customer calls Alyssa

**Customer:** "Hi, do you have a maintenance kit for my HP DesignJet T730?"

**Alyssa's New Process:**
1. While on call, she's already looking at Quo interface
2. Quo shows: "Customer: ABC Graphics, Last Call: Jan 15"
3. **NEW: Ply inventory panel appears in Quo**
4. She types "T730 maintenance" in search box
5. Sees: "✅ **HP T730 Maintenance Kit** - 2 in stock, Bin A3"
6. Immediately answers: "Yes, we have 2 in stock. Anything else?"
7. Customer asks: "What about the plotter belt?"
8. Types "T730 belt" → sees: "❌ **HP T730 Belt** - Out of stock, ETA Jan 30"
9. Answers: "We're out but have one arriving Jan 30. Want me to reserve it?"

**Outcome:**
- No hold time
- Instant answers
- Customer impressed
- Call time reduced 2-5 minutes
- Can quote full job on first call

---

## What "Integration" Means Technically

### Option 1: Ply API → N8N → Quo Custom Panel (Recommended)

**How It Works:**

1. **Ply has an API** (we need to validate this with Megan/Ply documentation)
   - GET `/inventory/items` - List all inventory
   - GET `/inventory/search?query=X` - Search by part name/SKU
   - GET `/inventory/item/{id}` - Get specific item details

2. **N8N middleware layer** (building on Phase 1 infrastructure)
   - Listens to Quo webhook: "Call started from 480-555-1234"
   - Identifies customer from Jobber (already built in Phase 1)
   - If customer identified → fetch their recent jobs from Jobber
   - Extract equipment types from job history (e.g., "HP DesignJet T730")
   - Pre-fetch common parts for that equipment from Ply
   - Send inventory data to Quo interface

3. **Quo Custom Panel** (if Quo supports embedded panels/widgets)
   - Displays inventory search box
   - Shows pre-loaded common parts for customer's equipment
   - Real-time search as Alyssa types
   - Stock levels, bin locations, pricing

**Technical Stack:**
```
Quo Call Start Webhook
    ↓
N8N Workflow
    ↓
Jobber API (get customer + equipment from jobs)
    ↓
Ply API (search inventory for common parts)
    ↓
Quo Custom Panel/Widget (display inventory)
```

**Challenge:** Does Quo support custom panels/widgets? Need to research Quo API.

---

### Option 2: Standalone Inventory Lookup Tool (Fallback)

**If Quo doesn't support custom panels:**

Build a simple web app that Alyssa keeps open next to Quo:

**How It Works:**

1. Alyssa has two screens:
   - **Screen 1:** Quo call interface (as usual)
   - **Screen 2:** Inventory Lookup Tool (web app)

2. When call starts in Quo:
   - Quo webhook fires to N8N
   - N8N identifies customer
   - N8N sends customer info to Inventory Lookup Tool
   - Tool auto-updates with customer context

3. Inventory Lookup Tool shows:
   - Customer name (synced from Quo call)
   - Equipment types (from Jobber history)
   - Common parts pre-loaded (from Ply)
   - Search box for other parts
   - Real-time stock levels

**Technical Stack:**
```
Quo Call Start → N8N → Web App (auto-populates)
                    ↓
                 Ply API (inventory data)
```

**Benefit:** Works regardless of Quo's capabilities
**Downside:** Still requires Alyssa to look at two screens

---

### Option 3: Ply Desktop App + Call Context (Simplest)

**If Ply already has good search:**

Just make Ply aware of WHO is calling:

**How It Works:**

1. Quo webhook → N8N
2. N8N identifies customer + equipment
3. N8N sends notification to Alyssa's computer
4. Notification shows: "Call from ABC Graphics - Equipment: HP T730, Canon iPF9400"
5. Alyssa opens Ply, searches with context

**Benefit:** Minimal custom development
**Downside:** Still requires context-switching, but FASTER switching

---

## What Data Gets Surfaced?

### Inventory Fields to Display

| Field | Example | Why Important |
|-------|---------|---------------|
| **Part Name** | HP T730 Maintenance Kit | Quick identification |
| **SKU** | HP-T730-MK-001 | Precise ordering |
| **Stock Level** | 2 in stock | Availability |
| **Bin Location** | Bin A3, Shelf 2 | Alyssa can physically check |
| **Price** | $145.00 | Quote on call |
| **Condition** | New / Used / Refurbished | For used parts tracking |
| **Source** | Purchased / Parted from Machine #X | For used parts |
| **ETA if out of stock** | Jan 30, 2026 | Customer expectations |
| **Jobber PO Link** | PO #12345 | If already ordered |

---

## Customer Context Integration

**Smart Pre-Loading:**

When customer calls, auto-display THEIR common parts:

**Example: ABC Graphics calls**

Equipment CRM knows ABC Graphics has:
- HP DesignJet T730 (Serial: ABC123, installed 2022)
- Canon iPF9400 (Serial: XYZ789, installed 2019)

Ply integration pre-loads:
- ✅ HP T730 Maintenance Kit - 2 in stock
- ✅ HP T730 Printhead - 1 in stock
- ❌ Canon iPF9400 Ink (Black) - Out of stock, ETA Jan 28
- ✅ Canon iPF9400 Maintenance Kit - 3 in stock

**Alyssa sees this BEFORE customer even asks.**

**Result:** She can proactively say:
> "Hi ABC Graphics! I see you have the T730 and the iPF9400. We have maintenance kits in stock for both if you need them."

---

## Technical Requirements & Validation

### Questions We Need to Answer (Megan Interview)

1. **Does Ply have a public API?**
   - Yes → Option 1 or 2 is feasible
   - No → Option 3 only, or manual integration

2. **What's Ply's search performance?**
   - Fast (<500ms) → Real-time search works
   - Slow (2-3 sec) → Need to pre-load common parts

3. **Does Ply support webhooks?**
   - Yes → We can get real-time stock updates
   - No → Need to poll Ply API every X minutes

4. **How is Ply organized?**
   - Categories (plumbing, HVAC) → Need custom "printer parts" category
   - SKUs → We can search by SKU
   - Barcodes → Could integrate barcode scanning later

5. **What's Ply's data refresh rate?**
   - Real-time → Always accurate
   - Batched (hourly) → Might show stale data

### Questions About Quo

6. **Does Quo support custom panels/widgets?**
   - Yes → Option 1 (embedded panel)
   - No → Option 2 (standalone tool) or Option 3 (notifications)

7. **Can Quo webhooks include call metadata?**
   - Caller ID, customer name, call start time
   - Already know: Yes (Phase 1 working)

8. **Can we embed external web apps in Quo interface?**
   - iframe support?
   - API for custom UI?

---

## Implementation Plan

### Week 1: Research & Validation
- [ ] Interview Megan about Ply API capabilities
- [ ] Review Ply API documentation (if available)
- [ ] Test Ply search performance
- [ ] Research Quo custom panel capabilities
- [ ] Decide: Option 1, 2, or 3

### Week 2-3: Build Integration
- [ ] N8N workflow: Quo call → Customer lookup → Equipment identification
- [ ] Ply API connector in N8N (or polling mechanism)
- [ ] Build inventory lookup interface (web app or Quo panel)
- [ ] Connect Equipment CRM → Common parts pre-loading logic
- [ ] Test with sample customer data

### Week 4: Test & Refine
- [ ] Alyssa testing with real calls
- [ ] Measure: Time saved per call
- [ ] Refine search UX based on feedback
- [ ] Add frequently requested parts to quick access

### Week 5-6: Rollout & Training
- [ ] Train Alyssa on new workflow
- [ ] Document common searches
- [ ] Create SOP for using inventory lookup during calls
- [ ] Measure adoption and impact

---

## Success Metrics

| Metric | Baseline | Target | How to Measure |
|--------|----------|--------|----------------|
| **Avg call time** | 8-10 min | 5-7 min | Quo call logs |
| **"Do we have X?" interruptions** | 10/day | 1-2/day | Alyssa's log |
| **Calls answered on first contact** | 60% | 90%+ | Track callbacks |
| **Time to answer inventory question** | 2-5 min | <10 seconds | Stopwatch during calls |
| **Customer satisfaction (inventory availability)** | Unknown | Measured via survey | Post-call survey |

---

## Alternative: "Inventory Copilot" Approach

**If Ply API is limited:**

Build an AI assistant that listens to calls and proactively shows inventory:

**How It Works:**

1. Quo call starts → N8N sends audio to transcription
2. Real-time transcription identifies when customer asks about parts
3. AI extracts part name/model from transcript
4. Searches Ply via API (or screen scraping if no API)
5. Displays result to Alyssa BEFORE she has to check

**Example:**

Customer says: "Do you have a maintenance kit for the T730?"

AI copilot:
- Transcribes in real-time
- Detects "maintenance kit" + "T730"
- Searches Ply
- Shows: "✅ HP T730 Maintenance Kit - 2 in stock"
- Alyssa glances at screen, answers immediately

**Pro:** Works even if Alyssa forgets to search
**Con:** Requires Phase 1 transcription to be real-time (currently post-call)

---

## ROI Calculation

### Current State:
- Interruptions: 10/day
- Time per interruption: 5 min (searching, context-switching)
- Daily time wasted: 50 min
- Annual time wasted: 50 min × 250 days = 12,500 min = 208 hours
- Cost: 208 hrs × $300/hr (Kelsey's time) = **$62,500/year**

### After Integration:
- Interruptions: 1-2/day (only for complex/unusual requests)
- Time per "interruption": <30 seconds (quick search in integrated panel)
- Daily time wasted: 1-2 min
- Annual time wasted: ~8 hours
- Cost: 8 hrs × $300 = $2,400/year
- **Savings: $60,100/year**

### Conservative Estimate (50% adoption):
- **Savings: $30,000/year**
- Plus better customer experience (fewer hold times)
- Plus higher close rate (quote on first call vs. callback)

---

## User Experience Mockup

```
┌─────────────────────────────────────────────────────────────┐
│ Quo Call Interface                                          │
├─────────────────────────────────────────────────────────────┤
│ 📞 Incoming Call: (480) 555-1234                           │
│ Customer: ABC Graphics (Matched from Jobber)               │
│ Last Contact: Jan 15, 2026                                 │
│ Equipment: HP T730, Canon iPF9400                          │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ 📦 INVENTORY (Ply Integration)                          │ │
│ │                                                           │ │
│ │ Search: [HP T730 maintenance________] 🔍                │ │
│ │                                                           │ │
│ │ Common Parts for This Customer:                          │ │
│ │ ✅ HP T730 Maintenance Kit - 2 in stock (Bin A3) $145   │ │
│ │ ✅ HP T730 Printhead - 1 in stock (Bin B1) $280          │ │
│ │ ❌ Canon iPF9400 Ink (Black) - Out of stock, ETA Jan 28 │ │
│ │ ✅ Canon iPF9400 Maintenance Kit - 3 in stock (Bin A5)  │ │
│ │                                                           │ │
│ │ [View Full Inventory] [Add to Quote]                    │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                              │
│ Call Notes:                                                  │
│ [Customer asking about T730 maintenance kit...]             │
│                                                              │
│ [Answer Call] [Transfer] [Hold] [End Call]                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Next Steps

1. **Validate with Megan:**
   - Does Ply have an API we can use?
   - How is inventory currently organized in Ply?
   - What search methods does Ply support?

2. **Research Quo capabilities:**
   - Custom panels/widgets support?
   - Embedding external web apps?
   - API documentation

3. **Prototype Options:**
   - If Quo supports custom panels → Build Option 1
   - If Quo doesn't → Build Option 2 (standalone tool)
   - Fallback → Option 3 (notifications + Ply desktop)

4. **Define Success Criteria:**
   - What does "success" look like for Alyssa?
   - How do we measure time saved?
   - When do we consider this "done"?

---

*Created: January 24, 2026*
*Status: Technical design, pending Megan interview for validation*
*Investment: Part of $8,000 Ply Enhancement Layer in Phase 2*
