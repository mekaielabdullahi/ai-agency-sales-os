# S&S Wolf Sheds - Process Map

**Created:** December 28, 2025
**Source:** Discovery Call - December 22, 2025
**Updated:** December 28, 2025 (Post-Discovery Session)
**Status:** Current State + MVP Target State

---

## Business Process Overview

S&S Wolf Sheds operates as a Graceland Sheds dealer with three lots in Northern Arizona. The business involves on-lot lead capture, sales, order processing through Graceland, and delivery coordination. Chris Andrade (GC license via Remus Development) is driving a platform vision for dealer network expansion.

---

## Core Workflows

### 1. On-Lot Visitor Flow (CURRENT STATE - PRIMARY PAIN POINT)

```
┌─────────────────────────────────────────────────────────────────────┐
│                 ON-LOT VISITOR FLOW (Current State)                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────┐                                           │
│  │   Visitor Arrives    │  ← Single entry/exit point                │
│  │   at Lot             │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Browse ~20 Buildings│  ← Self-directed browsing                 │
│  │  on Lot              │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│     ┌───────┴───────┐                                               │
│     │               │                                                │
│ ATTENDANT      ATTENDANT                                            │
│   FREE          BUSY                                                │
│     │               │                                                │
│     ▼               ▼                                                │
│ ┌─────────┐   ┌──────────────────────────┐                          │
│ │ Engage  │   │  ⚠️ LEAD LEAKAGE         │                          │
│ │ Visitor │   │                          │                          │
│ └────┬────┘   │  • Visitor browses alone │                          │
│      │        │  • No contact captured   │                          │
│      │        │  • No follow-up possible │                          │
│      │        │  • Lost opportunity      │                          │
│      │        └──────────────────────────┘                          │
│      │                                                               │
│      ▼                                                               │
│  ┌──────────────────────┐                                           │
│  │   Manual Capture     │  ← Paper/verbal only                      │
│  │   (if remembered)    │                                           │
│  └──────────────────────┘                                           │
│                                                                      │
│  ⚠️ CRITICAL GAP: No mechanism to capture multiple simultaneous    │
│                   visitors or track interest without attendant      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Pain Points:**
- Single attendant cannot capture multiple simultaneous visitors
- No self-service lead capture mechanism
- No tracking of which buildings visitors looked at
- No follow-up possible for browsers who leave without engaging
- No measurement of traffic vs conversion

---

### 2. On-Lot Visitor Flow (MVP TARGET STATE)

```
┌─────────────────────────────────────────────────────────────────────┐
│                 ON-LOT VISITOR FLOW (MVP Target)                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────┐                                           │
│  │   Visitor Arrives    │  ← Vehicle count via camera (future)      │
│  │   at Lot             │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Browse Buildings    │  ← Each slot has fixed QR code            │
│  │  See QR Code on Each │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  ✅ SCAN QR CODE     │  ← Self-service engagement                │
│  │  (Slot-based)        │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Intake Form Opens   │  ← Guided capture flow                    │
│  │  • Contact info      │                                           │
│  │  • Interest level    │                                           │
│  │  • Questions         │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│     ┌───────┴───────────────────────┐                               │
│     │                               │                                │
│     ▼                               ▼                                │
│ ┌─────────────┐          ┌──────────────────────┐                   │
│ │ Instant     │          │ Lead Captured        │                   │
│ │ Attendant   │          │ • Linked to building │                   │
│ │ Notification│          │ • Multi-scan tracked │                   │
│ │ (SMS/Email) │          │ • Follow-up enabled  │                   │
│ └─────────────┘          └──────────────────────┘                   │
│                                                                      │
│  ✅ SOLVED: Multiple visitors captured simultaneously               │
│  ✅ SOLVED: Interest tracked even if attendant busy                │
│  ✅ SOLVED: Follow-up possible for all interested visitors         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 3. QR Slot Management Process (NEW - MVP)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     QR SLOT MANAGEMENT                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  INITIAL SETUP (One-Time):                                          │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Create 20 Fixed QR Codes per Lot                            │  │
│  │  • Slot 1, Slot 2, Slot 3... Slot 20                         │  │
│  │  • Physical codes printed and mounted                        │  │
│  │  • Backend maps slot → current inventory                     │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ONGOING MANAGEMENT:                                                │
│  ┌──────────────────────┐                                           │
│  │  Inventory Changes   │  ← Building sold or moved               │
│  │  (Building moves to  │                                           │
│  │   different slot)    │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Update Backend      │  ← Admin remaps slot to new building     │
│  │  Slot → Building     │                                           │
│  │  Mapping             │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  QR Code Unchanged   │  ← No physical maintenance needed        │
│  │  (Points to slot,    │                                           │
│  │   not building)      │                                           │
│  └──────────────────────┘                                           │
│                                                                      │
│  ✅ LOW MAINTENANCE: Fixed codes, backend-only updates             │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 4. Lead Generation & Marketing Flow (Updated)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     LEAD GENERATION (Updated)                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐            │
│  │  Facebook    │   │   Website    │   │  Google Ads  │            │
│  │  Marketplace │   │  (WordPress) │   │  (Limited)   │            │
│  │  Daily Posts │   │              │   │              │            │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘            │
│         │                  │                  │                     │
│         └─────────┬────────┴──────────────────┘                     │
│                   │                                                  │
│                   ▼                                                  │
│  ┌──────────────────────────────────────────────────────┐          │
│  │                LEAD CAPTURE POINTS                    │          │
│  │                                                       │          │
│  │  ┌─────────────────────────────────────────────┐     │          │
│  │  │  ✅ NEW: On-Lot QR Scans                    │     │          │
│  │  │  • Self-service capture                     │     │          │
│  │  │  • Linked to specific building              │     │          │
│  │  │  • Instant attendant notification           │     │          │
│  │  └─────────────────────────────────────────────┘     │          │
│  │                                                       │          │
│  │  ┌─────────────────────────────────────────────┐     │          │
│  │  │  ✅ NEW: Website Intake Form                │     │          │
│  │  │  • Guided flow                              │     │          │
│  │  │  • Contact + preferences                    │     │          │
│  │  │  • Instant notification                     │     │          │
│  │  └─────────────────────────────────────────────┘     │          │
│  │                                                       │          │
│  │  • Facebook messages (existing)                       │          │
│  │  • Phone calls to lots (existing)                    │          │
│  │  • Walk-in lot visits (enhanced with QR)             │          │
│  │                                                       │          │
│  └──────────────────────────────────────────────────────┘          │
│                                                                      │
│  ⚠️ DEPRIORITIZED: Paid ads restart (capture first, then traffic) │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 5. Customer Inquiry & Sales Flow (Updated)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CUSTOMER INQUIRY FLOW (Updated)                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────┐                                           │
│  │   Incoming Inquiry   │                                           │
│  │   (QR/Web/Phone/FB)  │  ← Now includes QR scans                 │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  ✅ CAPTURED IN CRM  │  ← Linked to building if QR scan        │
│  │  • Contact info      │                                           │
│  │  • Building interest │                                           │
│  │  • Scan history      │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Attendant Response  │  ← Notified instantly via SMS/email      │
│  │  (informed by data)  │                                           │
│  │                      │                                           │
│  │  Knows:              │                                           │
│  │  • Which buildings   │                                           │
│  │  • Interest level    │                                           │
│  │  • Questions asked   │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │   Lead Qualified?    │                                           │
│  └──────┬───────┬───────┘                                           │
│         │       │                                                    │
│        YES      NO                                                   │
│         │       │                                                    │
│         │       ▼                                                    │
│         │  ┌────────────────────────┐                               │
│         │  │ ✅ FOLLOW-UP ENABLED   │  ← Can nurture later          │
│         │  │ (Contact captured,     │                               │
│         │  │  interest tracked)     │                               │
│         │  └────────────────────────┘                               │
│         │                                                            │
│         ▼                                                            │
│  ┌──────────────────────┐                                           │
│  │   Continue to Sale   │                                           │
│  └──────────────────────┘                                           │
│                                                                      │
│  ⚠️ PHASE 2: AI Chatbot for FAQ automation (deprioritized)        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 6. Sales & Order Processing Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SALES & ORDER PROCESSING                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────┐                                           │
│  │   Customer at Lot    │                                           │
│  │   or Phone/Online    │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │   Sales Discussion   │                                           │
│  │   • Pricing          │                                           │
│  │   • Customization    │                                           │
│  │   • RTO Terms        │                                           │
│  │   • Timeline         │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │   Order Placed       │                                           │
│  │   (Custom specs)     │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Submit to Graceland │ ← Dealer enters in system                 │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Graceland Validates │ ← 24-48 hours                             │
│  │  (NetSuite system)   │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │   Order Confirmed    │                                           │
│  │   → Build Queue      │                                           │
│  └──────────────────────┘                                           │
│                                                                      │
│  ✅ Generally works, but custom specs can get lost                  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 7. Manufacturing & Delivery Flow (Updated)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MANUFACTURING & DELIVERY (Updated)               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────┐                                           │
│  │   Graceland Plant    │                                           │
│  │   Builds Shed        │                                           │
│  │                      │                                           │
│  │   Winter: 6-8 weeks  │                                           │
│  │   Spring: 3-5 weeks  │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Quality Check       │  ← Scott inspects at plant                │
│  │  (12-15% error rate  │                                           │
│  │   on custom orders)  │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  ✅ NEW: DELIVERY    │  ← MVP includes this artifact             │
│  │  HANDOFF ARTIFACT    │                                           │
│  │                      │                                           │
│  │  Link shared with    │                                           │
│  │  driver containing:  │                                           │
│  │  • Site map          │                                           │
│  │  • Access road info  │                                           │
│  │  • Clearance notes   │                                           │
│  │  • Customer contact  │                                           │
│  │  • Load orientation  │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │   Dispatch/Schedule  │  ← Graceland dispatcher (Chris)           │
│  │   (NetSuite)         │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │  Scott Contacts      │  ← Now has site specifics                 │
│  │  Customer            │                                           │
│  └──────────┬───────────┘                                           │
│             │                                                        │
│             ▼                                                        │
│  ┌──────────────────────┐                                           │
│  │   Delivery Complete  │  ← Reduced failed deliveries              │
│  └──────────────────────┘                                           │
│                                                                      │
│  ⚠️ REMAINING ISSUE: NetSuite passes minimal info to dealers       │
│  ✅ IMPROVED: Driver has site specs before arrival                 │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 8. Analytics & Measurement Flow (MVP Target)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ANALYTICS (MVP Target)                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  DATA SOURCES (MVP):                                                │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐            │
│  │   QR Scan    │   │   Intake     │   │   Vehicle    │            │
│  │   Events     │   │   Form       │   │   Counter    │            │
│  │              │   │   Submissions│   │   (Future)   │            │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘            │
│         │                  │                  │                     │
│         └──────────────────┼──────────────────┘                     │
│                            │                                         │
│                            ▼                                         │
│  ┌──────────────────────────────────────────────────────┐          │
│  │               MVP METRICS TRACKED                     │          │
│  │                                                       │          │
│  │   • Scans per building                               │          │
│  │   • Scans per user (multi-scan tracking)             │          │
│  │   • Form submissions                                  │          │
│  │   • Time: scan → submission                          │          │
│  │   • Interest by building type/size                   │          │
│  │   • Hot leads (high engagement)                      │          │
│  │                                                       │          │
│  └──────────────────────────────────────────────────────┘          │
│                                                                      │
│  COMPARISON BASELINE:                                               │
│  ┌──────────────────────────────────────────────────────┐          │
│  │   Historical Sales (2-3 years available)             │          │
│  │   • Monthly/weekly sales trends                      │          │
│  │   • Seasonal patterns                                │          │
│  │   • Conversion improvement tracking                  │          │
│  └──────────────────────────────────────────────────────┘          │
│                                                                      │
│  ⚠️ PHASE 2: Full dashboard connecting website, ads, Facebook, Zoho│
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Process Efficiency Analysis

### Time Waste Identification (Updated)

| Process Area | Issue | Impact | MVP Addresses? |
|-------------|-------|--------|----------------|
| **On-Lot Capture** | Multiple visitors lost | Lead leakage, no follow-up | ✅ YES - Primary focus |
| **Customer Inquiries** | Repetitive FAQ answering | Time drain | ⏸️ Phase 2 - Chatbot |
| **Marketing** | Manual Facebook posts daily | Labor intensive | ⏸️ White-label option |
| **Build Errors** | 12-15% custom order error rate | 2+ week delays | ⏸️ Phase 2 - SOP |
| **Delivery** | Drivers lack site specifics | Failed deliveries | ✅ YES - Handoff artifact |
| **Analytics** | No footfall measurement | Can't measure conversion | ✅ YES - Scan tracking |

### Bottleneck Summary (Updated)

```
MVP BOTTLENECKS (Immediate Action - This Sprint):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ON-LOT LEAD LEAKAGE ← PRIMARY MVP TARGET
   └── Single attendant can't capture multiple visitors
   └── No self-service capture mechanism
   └── No tracking of building interest
   SOLUTION: QR/Slot system + intake form

2. DELIVERY FRICTION
   └── Drivers lack site specifics
   └── Failed deliveries waste time/cost
   SOLUTION: Delivery handoff artifact

3. NO CONVERSION MEASUREMENT
   └── Can't measure footfall vs sales
   └── No data for inventory decisions
   SOLUTION: Scan analytics + historical comparison


PHASE 2 BOTTLENECKS (After MVP Success):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4. REPETITIVE FAQ TIME DRAIN
   └── Same questions answered repeatedly
   └── No 24/7 coverage
   DEPRIORITIZED: Chatbot is Phase 2

5. LEAD GENERATION VOLUME
   └── Paid ads paused → traffic drop
   └── SEO visibility issues
   DEPRIORITIZED: Capture first, then traffic

6. BUILD QUALITY CONTROL
   └── 12-15% custom order error rate
   └── No verification checklist
   DEPRIORITIZED: SOP is Phase 2+
```

---

## Current Tech Stack (Updated)

| System | Owner | Purpose | Status |
|--------|-------|---------|--------|
| WordPress | Alex | Website | Broken images, needs fixes |
| Rank Math SEO | Alex | SEO | Visibility dropped |
| Google Analytics | Alex | Web tracking | Limited understanding |
| Google Ads | Alex | Paid search | Limited use |
| Facebook/Marketplace | Alex | Social/listings | Primary channel |
| Zoho | Team | CRM/business suite | Not integrated |
| Excel | Team | Inventory/slot mapping | May have external refs |
| Graceland Portal | Graceland | Inventory serials/specs | Read-only |
| NetSuite | Graceland | Orders/dispatch | Limited dealer access |
| AmericanSteelInc.com | Team | Metal building quotes | Current builder tool |
| iMessage | Team | Internal comms | Group chat |

### Proposed Tech (MVP)

| System | Purpose | Notes |
|--------|---------|-------|
| Dynamic QR/Link Mgmt | Slot QR codes | Bitly/Dubb-like |
| Intake Forms | Lead capture | Lovable/Bolt.new |
| Notification System | Attendant alerts | Email/SMS/push |
| AI Doc Processing | SOT extraction | Google AI Studio/Gemini |

---

## MVP Success Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Leads captured per lot/week | Unknown (currently 0 for browsers) | Track all scans |
| Form submissions per lot/week | Unknown | Measure |
| Scan-to-submission rate | N/A | Establish baseline |
| Attendant response time | Unknown | Under 5 minutes |
| Buildings with scan activity | 0 | All 20 per lot |

---

**Last Updated:** December 28, 2025
**Status:** Post-Discovery Update Complete
**Next Review:** After MVP deployment
