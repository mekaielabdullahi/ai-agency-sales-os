# S&S Wolf Sheds - Phase 1 Scope (FINAL)

**Status:** Ready for Team Review
**Date:** January 27, 2026
**Source:** Sync with Chris - Phase 1 Deliverables Defined

---

## Executive Summary

**Investment:** $5,000
**Timeline:** 2-3 weeks
**Goal:** Stop lead leakage by capturing organic lot visitors

### ROI Justification

| Metric | Conservative | Optimistic |
|--------|--------------|------------|
| Year 1 Additional Revenue | +$99,400 | +$148,400 |
| Net Year 1 Benefit | +$93,600 | +$142,600 |
| **Year 1 ROI** | **1,015%** | **2,459%** |

**Break-even:** Converting just ONE additional lead ($8k avg sale) pays for the entire Phase 1 investment.

**See:** [Full Cost-Benefit Analysis](./cost-benefit-analysis.md) for detailed projections.

---

## Strategic Value: April Ad Campaign Enablement

Phase 1 isn't just about capturing leads - it's about **fixing the $400/mo Meta ad spend** that's currently "shotgunning" with no targeting or ROI visibility.

### Current State (Before Phase 1)
| Metric | Status |
|--------|--------|
| Monthly ad spend | $400/mo on Meta |
| Targeting approach | "Shotgunning" - no data |
| ROI tracking | None |
| Ideal Customer Profile | Unknown |
| Lot visitor data | Zero capture |

### April Campaign Readiness (After Phase 1)
| Capability | How Phase 1 Enables It |
|------------|------------------------|
| **Meta Pixel tracking** | Installed on lead capture page - links lot visits to digital touchpoints |
| **Ideal Customer Profile** | Built from captured lead data + 3 years historical sales |
| **Targeted audiences** | Create Meta lookalike audiences from actual buyers |
| **CPL/CAC/ROAS tracking** | Lead source attribution shows which ads drive sales |
| **Seasonal campaign data** | Know which sheds sell when, target accordingly |

### Ad Spend Improvement Projection

| Metric | Current | With Phase 1 Data |
|--------|---------|-------------------|
| Ad spend | $400/mo | $400/mo (same) |
| Targeting | Random | Data-driven ICP |
| Expected ROAS | Unknown | 2-3x |
| Wasted spend | ~50% | <20% |
| Leads per $100 spent | Unknown | Tracked & optimized |

### Timeline to April Campaign

```
Feb (Weeks 1-3): Phase 1 deployment + lead capture begins
        ↓
March: 30-60 leads captured, patterns emerge
        ↓
Late March: ICP defined from captured data + historical sales
        ↓
April: Launch targeted Meta campaigns with:
       - Lookalike audiences from QR sign-ups
       - Retargeting pixel on captured visitors
       - Seasonal messaging based on data
       - Full attribution tracking
```

### Key Metadata for Ad Targeting Accuracy

Phase 1 captures specific data points that directly improve Meta ads performance:

#### Customer Profile Data (from Clerk.com signup)
| Data Point | Ad Targeting Use |
|------------|------------------|
| **Name** | Custom Audience matching |
| **Phone number** | High-match-rate identifier for Meta |
| **Email address** | Primary identifier for lookalike audiences |
| **Geographic location** | Derived from lot_location parameter |

#### Behavioral Data (from QR scans)
| Data Point | Ad Targeting Use |
|------------|------------------|
| **shed_id** | Which shed types attract interest (size, style, price range) |
| **lot_location** | Which markets have most organic traffic |
| **Visit timestamp** | Time-of-day and day-of-week patterns |
| **Multi-scan behavior** | Browsing patterns showing purchase intent level |

#### Attribution Data
| Data Point | Ad Targeting Use |
|------------|------------------|
| **"How did you hear about us?"** | Validates which channels work before spending more |
| **Source tracking** | Distinguishes organic visitors from referrals |

#### Meta Pixel Events
| Event | Purpose |
|-------|---------|
| **PageView** | Track landing page visits |
| **Lead** | Fire on form completion |
| **User IDs** | Enable retargeting and suppression lists |

#### ICP-Building Data (cross-referenced with 3-year sales history)
- Which customer profiles actually convert
- Average order value by customer segment
- Geographic and seasonal patterns

### How This Transforms Ad Spend

| Before Phase 1 | After Phase 1 |
|----------------|---------------|
| "Shotgunning" with no targeting | **Custom Audiences** from actual leads |
| No conversion data | **Lookalike Audiences** from converted customers |
| Wasted spend on existing leads | **Suppression lists** for existing leads |
| Generic messaging | Target by **shed type interest** and **proximity** to lots |

**Bottom line:** Phase 1 turns S&S's blind ad spend into a data-driven customer acquisition machine by April.

---

## The Problem

S&S Wolf Sheds currently captures **zero information** from organic visitors who browse the lot and leave. This "lead leakage" represents:
- Significant lost revenue
- No data for decision-making
- No way to follow up with interested visitors
- No insight into lot traffic patterns

---

## Phase 1 Solution: Foundational Lead Capture

### What We're Building

```
Visitor Scans QR Code
        ↓
   Lead Capture Page
   (Name + Phone Number)
        ↓
   Visitor Gets Incentive
   (10% off your order = $300 value)
        ↓
   Data Flows to Google Sheet
        ↓
   Staff Gets Gmail Notification
   (Instant alert with lead info)
        ↓
   Simple Dashboard
   (Organic lead health monitor)
```

---

## Deliverables Checklist

### Core System
- [ ] Dynamic QR codes for each shed placard
- [ ] Lead capture landing page on S&S website
- [ ] Incentive offer: 10% off your order ($300 value)
- [ ] Google Sheet integration for lead storage
- [ ] Gmail notification automation for lot staff

### User Management
- [ ] Clerk.com integration for customer profiles
  - Free tier (up to 10,000 users)
  - Sign-in with Google or phone number
  - Enables future personalization

### Dashboard (Simple v1)
- [ ] Daily QR scan count
- [ ] New leads captured
- [ ] Basic organic lead health metrics

### Follow-Up System
- [ ] Single automated email campaign for captured leads

### Ad Campaign Foundation (for April)
- [ ] Meta Pixel installed on lead capture page
- [ ] Lead source attribution tracking ("How did you hear about us?")
- [ ] Basic ICP report from captured data + historical sales
- [ ] Targeted audience definitions ready for Meta

---

## Technology Stack

| Component | Tool | Cost |
|-----------|------|------|
| QR Codes | Dynamic QR generator | Minimal |
| User Profiles | Clerk.com | Free (up to 10k users) |
| Lead Storage | Google Sheets | Free |
| Notifications | Gmail automation | Free |
| Dashboard | TBD (simple) | Included |
| Ad Tracking | Meta Pixel | Free |
| Attribution | Lead source field | Free |

---

## Technical Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         S&S WOLF SHEDS LOT                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │  Shed A  │  │  Shed B  │  │  Shed C  │  │  Shed N  │            │
│  │  QR #1   │  │  QR #2   │  │  QR #3   │  │  QR #N   │            │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘            │
│       │             │             │             │                   │
│       └─────────────┴─────────────┴─────────────┘                   │
│                           │                                         │
└───────────────────────────┼─────────────────────────────────────────┘
                            │ Visitor scans
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    S&S WEBSITE (WordPress)                          │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │                  LEAD CAPTURE PAGE                          │    │
│  │  ┌─────────────┐  ┌────────────────────────────────────┐   │    │
│  │  │  Clerk.com  │◄─│  Sign in with Google / Phone       │   │    │
│  │  │  Auth SDK   │  │  "Get 10% off your order ($300)"     │   │    │
│  │  └──────┬──────┘  └────────────────────────────────────┘   │    │
│  │         │                                                   │    │
│  │         ▼                                                   │    │
│  │  ┌─────────────────────────────────────────────────────┐   │    │
│  │  │  User Profile Created in Clerk                       │   │    │
│  │  │  - Name, Phone, Email                                │   │    │
│  │  │  - Which QR code scanned (shed ID)                   │   │    │
│  │  │  - Timestamp                                         │   │    │
│  │  └──────┬──────────────────────────────────────────────┘   │    │
│  └─────────┼──────────────────────────────────────────────────┘    │
└────────────┼────────────────────────────────────────────────────────┘
             │ Webhook trigger
             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      AUTOMATION LAYER (n8n)                         │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │  Webhook receives new user data                             │    │
│  │         │                                                   │    │
│  │         ├──────► Google Sheets (append row)                 │    │
│  │         │        - Name, Phone, Email, Shed ID, Timestamp   │    │
│  │         │                                                   │    │
│  │         ├──────► Gmail (send notification)                  │    │
│  │         │        - To: lot-staff@snswolfsheds.com           │    │
│  │         │        - Subject: "New Lead: [Name] at [Shed]"    │    │
│  │         │                                                   │    │
│  │         └──────► Dashboard Update (increment counters)      │    │
│  └────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                  │
│  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐   │
│  │   Google Sheet   │  │   Clerk Dashboard │  │  Simple Dashboard│   │
│  │   "S&S Leads"    │  │   User Management │  │  Lead Metrics    │   │
│  └──────────────────┘  └──────────────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Component Details

#### 1. Dynamic QR Codes
- **Tool:** QR Code Generator Pro or similar
- **Format:** Each QR code encodes URL: `snswolfsheds.com/scan?shed=ABC123`
- **Dynamic:** Can update destination URL without reprinting
- **Tracking:** Each shed has unique ID for attribution

#### 2. Lead Capture Page (WordPress)
- **Route:** `/scan` or `/welcome`
- **Query param:** `?shed=ABC123` identifies which building
- **Clerk integration:** WordPress plugin or custom embed
- **Mobile-first:** 90%+ of scans will be mobile

#### 3. Clerk.com Integration
- **Auth methods:** Google OAuth, Phone (SMS verification)
- **User data captured:**
  - Full name
  - Phone number
  - Email (optional, from Google)
  - Custom metadata: `shed_id`, `lot_location`, `first_scan_date`
- **Webhook:** Fires on `user.created` event

#### 4. n8n Automation Workflow
- **Trigger:** Clerk webhook (`user.created`)
- **Actions:**
  1. Parse user data from webhook payload
  2. Append row to Google Sheet
  3. Send Gmail notification to staff
  4. (Optional) Update dashboard metrics

#### 5. Google Sheet Structure
| Column | Data | Example |
|--------|------|---------|
| Timestamp | Auto | 2026-01-28 14:32:00 |
| Name | From Clerk | John Smith |
| Phone | From Clerk | 602-555-1234 |
| Email | From Clerk | john@email.com |
| Shed ID | From QR param | SPC-16W-001 |
| Lot Location | Derived | Flagstaff |
| Source | Fixed | QR Scan |
| Status | Manual update | New / Contacted / Sold |

#### 6. Gmail Notification Template
```
Subject: 🏠 New Lead at [Lot]: [Name]

New visitor just scanned a QR code!

Name: John Smith
Phone: 602-555-1234
Shed: Side Porch Cabin 16W (#SPC-16W-001)
Time: 2:32 PM

They're browsing the lot now - great time to say hello!

---
Sent automatically by S&S Lead Capture System
```

---

## User Flows

### Flow 1: Visitor Experience (Happy Path)

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: ARRIVAL                                                 │
│ ─────────────────────────────────────────────────────────────── │
│ Visitor arrives at S&S Wolf Sheds lot                           │
│ Parks in designated spot with welcome signage                   │
│ Sees wooden placard: "Welcome! Scan for 10% off your order"       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: SCAN                                                    │
│ ─────────────────────────────────────────────────────────────── │
│ Visitor opens phone camera                                      │
│ Scans QR code on placard                                        │
│ Phone opens: snswolfsheds.com/scan?shed=SPC-001                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: SIGN UP (Mobile Screen)                                 │
│ ─────────────────────────────────────────────────────────────── │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │  🏠 S&S Wolf Sheds                                      │    │
│ │                                                          │    │
│ │  Welcome to our lot!                                     │    │
│ │                                                          │    │
│ │  Sign up to receive:                                     │    │
│ │  ✓ 10% off your order ($300+ value)                       │    │
│ │  ✓ Exclusive sale notifications                         │    │
│ │  ✓ Your personal shed wishlist                          │    │
│ │                                                          │    │
│ │  ┌──────────────────────────────────────────────────┐   │    │
│ │  │ 🔵 Continue with Google                          │   │    │
│ │  └──────────────────────────────────────────────────┘   │    │
│ │                                                          │    │
│ │  ┌──────────────────────────────────────────────────┐   │    │
│ │  │ 📱 Continue with Phone                           │   │    │
│ │  └──────────────────────────────────────────────────┘   │    │
│ │                                                          │    │
│ │  Takes 10 seconds • We don't spam                       │    │
│ └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: CONFIRMATION                                            │
│ ─────────────────────────────────────────────────────────────── │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │  ✅ You're all set, John!                               │    │
│ │                                                          │    │
│ │  Your 10% order discount is saved.                       │    │
│ │  Just mention it when you're ready to buy!               │    │
│ │                                                          │    │
│ │  Now go explore our sheds - we have some                 │    │
│ │  great deals right now! 🏠                               │    │
│ │                                                          │    │
│ │  ┌──────────────────────────────────────────────────┐   │    │
│ │  │ View Today's Specials                            │   │    │
│ │  └──────────────────────────────────────────────────┘   │    │
│ └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: BROWSE                                                  │
│ ─────────────────────────────────────────────────────────────── │
│ Visitor browses the lot freely                                  │
│ Staff receives notification and can approach naturally          │
│ "Hi! I see you're looking at the Side Porch Cabin - great       │
│ choice! That one actually has a special going on right now..."  │
└─────────────────────────────────────────────────────────────────┘
```

### Flow 2: Staff Experience

```
┌─────────────────────────────────────────────────────────────────┐
│ STAFF IN OFFICE                                                 │
│ ─────────────────────────────────────────────────────────────── │
│ Staff member working at desk                                    │
│ Gmail open on computer or phone                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ NOTIFICATION ARRIVES                                            │
│ ─────────────────────────────────────────────────────────────── │
│ 🔔 *ding*                                                       │
│                                                                  │
│ From: S&S Lead Capture <noreply@snswolfsheds.com>               │
│ Subject: 🏠 New Lead at Flagstaff: John Smith                   │
│                                                                  │
│ Name: John Smith                                                 │
│ Phone: 602-555-1234                                             │
│ Shed: Side Porch Cabin 16W (#SPC-16W-001)                       │
│ Time: 2:32 PM                                                    │
│                                                                  │
│ They're browsing the lot now!                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STAFF RESPONSE                                                  │
│ ─────────────────────────────────────────────────────────────── │
│ Staff waits 2-3 minutes (let visitor browse)                    │
│ Walks to Side Porch Cabin area                                  │
│ Natural approach: "Hi there! I'm Chris. That's a beautiful      │
│ cabin you're looking at - it's actually our only 16-foot wide.  │
│ Can I tell you about it?"                                       │
└─────────────────────────────────────────────────────────────────┘
```

### Flow 3: Visitor Declines to Sign Up

```
Visitor scans QR → Sees sign-up page → Closes browser
                              │
                              ▼
         No data captured (we can't force it)
                              │
                              ▼
         Staff never notified (no different from today)
                              │
                              ▼
         FUTURE: Add "Browse without signing up" option
         that still tracks anonymous scan for metrics
```

### Flow 4: Multi-Scan Visitor (Already Signed Up)

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: VISITOR SCANS SECOND SHED                               │
│ ─────────────────────────────────────────────────────────────── │
│ John already signed up at Shed A (Side Porch Cabin)             │
│ Now browsing Shed B (Lofted Barn) and scans QR code             │
│ Phone opens: snswolfsheds.com/scan?shed=LB-12W-003              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: CLERK RECOGNIZES RETURNING USER                         │
│ ─────────────────────────────────────────────────────────────── │
│ Clerk detects existing session/cookie                           │
│ No sign-up form shown - user already authenticated              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: WELCOME BACK SCREEN                                     │
│ ─────────────────────────────────────────────────────────────── │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │  👋 Welcome back, John!                                 │    │
│ │                                                          │    │
│ │  You're checking out the Lofted Barn 12W - nice choice! │    │
│ │                                                          │    │
│ │  Your 10% discount is still saved.                       │    │
│ │                                                          │    │
│ │  Sheds you've viewed today:                              │    │
│ │  • Side Porch Cabin 16W                                  │    │
│ │  • Lofted Barn 12W ← You are here                        │    │
│ │                                                          │    │
│ │  ┌──────────────────────────────────────────────────┐   │    │
│ │  │ Compare These Sheds                              │   │    │
│ │  └──────────────────────────────────────────────────┘   │    │
│ └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: PROFILE UPDATED (Backend)                               │
│ ─────────────────────────────────────────────────────────────── │
│ Clerk user metadata updated:                                    │
│   sheds_viewed: ["SPC-16W-001", "LB-12W-003"]                   │
│   last_scan: "2026-01-28T14:45:00"                              │
│                                                                  │
│ Webhook fires: user.updated event                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: STAFF NOTIFICATION (Optional)                           │
│ ─────────────────────────────────────────────────────────────── │
│ From: S&S Lead Capture <noreply@snswolfsheds.com>               │
│ Subject: 🏠 John Smith now viewing Lofted Barn 12W              │
│                                                                  │
│ Existing lead John Smith is still browsing!                     │
│                                                                  │
│ Now viewing: Lofted Barn 12W (#LB-12W-003)                      │
│ Previously viewed: Side Porch Cabin 16W                         │
│ Time on lot: 12 minutes                                         │
│                                                                  │
│ 💡 They're comparing options - good time to engage!             │
└─────────────────────────────────────────────────────────────────┘
```

**Why this matters:**
- Captures full browsing behavior (which sheds interest them)
- Shows purchase intent level (more scans = more serious buyer)
- Gives staff better context for conversation
- Builds richer customer profiles for future marketing

---

## Implementation Steps

### Week 1: Foundation (Days 1-5)

| Day | Task | Owner | Acceptance Criteria |
|-----|------|-------|---------------------|
| 1 | Clerk.com account setup | Matthew | Account created, API keys secured |
| 1 | QR code generator account | Matthew | Can create dynamic QR codes |
| 1 | Create Google Sheet structure | Matthew | All columns defined per spec |
| 2 | WordPress page creation | Matthew | `/scan` route exists, mobile responsive |
| 2 | Clerk WordPress integration | Matthew | Sign-in widget renders correctly |
| 3 | Test Clerk user creation | Matthew | Can sign up, user appears in Clerk dashboard |
| 3 | Generate test QR codes (5) | Matthew | QR codes link to correct URLs with shed params |
| 4 | Clerk webhook configuration | Matthew | Webhook fires on user.created |
| 5 | Integration testing | Matthew + Trent | End-to-end flow works on mobile |

**Week 1 Milestone:** Can scan QR → Sign up → See user in Clerk

### Week 2: Automation (Days 6-10)

| Day | Task | Owner | Acceptance Criteria |
|-----|------|-------|---------------------|
| 6 | n8n workflow: Clerk webhook receiver | Matthew | Webhook data logs correctly |
| 6 | n8n workflow: Google Sheets append | Matthew | New users appear in sheet |
| 7 | n8n workflow: Gmail notification | Matthew | Email sends within 30 seconds |
| 7 | Email template design | Mekaiel | Approved by Chris |
| 8 | Multi-lot support (if needed) | Matthew | Different lots route to different staff |
| 9 | Error handling & retry logic | Matthew | Failed webhooks retry 3x |
| 10 | Staff training documentation | Mekaiel | One-pager for lot staff |

**Week 2 Milestone:** Full automation working - scan to notification in < 1 minute

### Week 3: Dashboard & Polish (Days 11-15)

| Day | Task | Owner | Acceptance Criteria |
|-----|------|-------|---------------------|
| 11 | Simple dashboard design | TBD | Mockup approved by team |
| 12 | Dashboard build | Matthew | Shows daily scans, total leads |
| 13 | Follow-up email automation | Matthew | Sends 24hr after sign-up |
| 13 | Follow-up email content | Mekaiel + Chris | Copy approved |
| 14 | Production QR code generation | Matthew | All sheds have codes ready |
| 14 | QR code delivery to Chris | Matthew | Files sent for printing |
| 15 | Final testing with Chris | Matthew + Chris | Live test at one lot |
| 15 | Handoff documentation | Matthew | Staff guide complete |

**Week 3 Milestone:** System live and staff trained

---

## Risks & Dependencies

### Critical Dependencies (Blockers)

| Dependency | Owner | Risk Level | Mitigation |
|------------|-------|------------|------------|
| Sandra approves incentive offer | Chris | HIGH | Need confirmation before page copy finalized |
| Clerk works with WordPress | Matthew | MEDIUM | Research spike Day 1; fallback to custom form |
| S&S staff have Gmail access | Chris | LOW | Verify during Week 1 |
| Physical placards ready | Chris | MEDIUM | Can use temporary printed QR codes initially |

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Clerk doesn't integrate cleanly with WP | Medium | High | Day 1 spike; fallback to embedded iframe or custom |
| Webhook delivery unreliable | Low | High | n8n retry logic; alert on failures |
| Mobile experience poor | Low | Medium | Test on 3+ devices before launch |
| QR codes don't scan well | Low | Medium | Test print quality; use high-contrast design |

### Scope Creep Risks

| Request | Response |
|---------|----------|
| "Can we track which sheds they look at?" | Phase 2 - requires per-shed QR scans |
| "Can we add a chatbot?" | Phase 2 - would delay launch |
| "Can staff respond via the system?" | Phase 2 - Gmail reply works for now |
| "Can we see conversion rates?" | Phase 2 - need to integrate with sales data |

### Contingency Plans

| Scenario | Plan B |
|----------|--------|
| Clerk doesn't work | Use simple Typeform → Zapier → Sheet |
| n8n has issues | Use Zapier or Make.com |
| Dashboard takes too long | Launch without; add in Week 4 |
| WordPress hosting issues | Temporarily host on Vercel/Netlify |

---

## Timeline

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | Build & Deploy | QR codes, lead capture page, Clerk integration |
| Week 2 | Connect & Test | Sheet integration, Gmail alerts, testing |
| Week 3 | Dashboard & Polish | Simple dashboard, follow-up email, refinement |

**Note:** Under-promising to enable over-delivery. May complete faster.

---

## What's NOT in Phase 1

These are future phase opportunities:
- [ ] Customer profiles tracking which sheds they scanned
- [ ] Sales dashboard with conversion rates
- [ ] Advanced automated follow-up sequences
- [ ] Value-added service referrals (site prep, tree trimming)
- [ ] Lot-by-lot comparison analytics
- [ ] Integration with existing sales data (3 years)

---

## Success Metrics

### Leading Indicators (Weekly)
| Metric | Target |
|--------|--------|
| QR scans per day | 5-10 |
| Sign-up conversion rate | 40%+ |
| Staff notification response | < 5 min |

### Lagging Indicators (Monthly)
| Metric | Target |
|--------|--------|
| Total leads captured | 60+ |
| Credit redemptions | 20%+ |
| Attributable sales | 2+ |
| Monthly revenue from program | $16,000+ |

---

## Client Requirements (Chris)

- [ ] Confirm incentive offer with Sandra (10% off your order or alternative)
- [ ] Create Google Drive folder with:
  - New S&S logo
  - Shed naming SOP
  - Inventory CSV
  - Any existing storyboard assets
- [ ] Begin work on physical shed placards (for QR code placement)

---

## Team Assignments

| Task | Owner |
|------|-------|
| Update Gamma presentation | Mekaiel |
| Clerk.com + WordPress research | Matthew |
| Define technical architecture | Matthew + Trent |
| QR code system setup | Matthew |
| Dashboard design | TBD |
| Client communication | Chris |

---

## Next Steps

1. **Team Review** - Review this scope document
2. **Trent Alignment** - Confirm technical feasibility and timeline
3. **Gamma Update** - Mekaiel updates presentation per notes
4. **Client Presentation** - Schedule with S&S (Sandra + team)

---

## Closing Pitch (for presentation)

> "This is Case Study #2 for Arise Group. Plotter Mechanics was our first. We succeed only if you succeed - that's why we're starting with this foundational system that pays for itself with a single converted lead. We're your transformation partner, not a vendor who takes money and disappears."

---

**Document Owner:** Matthew Kerns
**Last Updated:** January 28, 2026
**Status:** READY FOR TEAM REVIEW

---

## Revision History

| Date | Change | Author |
|------|--------|--------|
| Jan 27, 2026 | Initial scope from Chris sync call | Matthew |
| Jan 28, 2026 | Added technical architecture, user flows, implementation steps, risks | Matthew |
| Jan 28, 2026 | Added metadata details for Meta ads targeting accuracy | Matthew |
| Jan 28, 2026 | Added Flow 4: Multi-Scan Visitor user flow | Matthew |
