# S&S Wolf Sheds Post-Discovery Update

**Date:** December 28, 2025
**Type:** Working Session / Post-Discovery Update
**Recording:** [Fathom Recording](https://fathom.video/share/DB8EPPNDUmnRMsex7xSZCoaeAq5kCXXw)

---

## Attendees

**S&S Wolf Sheds / Remus Development:**
- Chris Andrade (Owner/Operator - GC license via Remus Development)

**Arise Group:**
- Trent Christopher
- Mekaiel Abdullahi
- Matthew

---

## Call Context

Working session reviewing Chris's "Source of Truth v1" (~300 pages) and aligning on MVP for S&S Wolfsheds. This call significantly evolved the project scope from the December 22 discovery.

**Key Shift:** Focus moved from marketing/chatbot quick wins to a **lot-level lead capture and inventory management MVP** as the primary deliverable.

---

## Major Evolution from December 22 Discovery

### Original Understanding (Dec 22)
- Primary pain: Lead volume collapse from pausing ads
- Focus: AI chatbot, website fixes, paid ads restart
- Budget: $5,000 quick win + $5,000 Phase 2

### New Understanding (Dec 28)
- Primary pain: **On-lot lead leakage** - visitors browse and leave without capture
- Focus: **QR/slot system + intake form + lightweight CRM**
- New scope: MVP lot attendant system with inventory tie-in
- Long-term vision: **Platformizable solution for Graceland dealer network**

---

## New Pain Points Identified

### 1. On-Lot Lead Leakage (NEW - CRITICAL)
- Single attendant cannot capture multiple simultaneous visitors
- Prospects browse lot and leave without contact captured
- No way to follow up with interested parties who didn't buy
- **This is the new #1 priority**

### 2. Lack of Lot Analytics (NEW)
- No quantification of lot traffic vs conversion
- Can't measure footfall to close rate
- Weak feedback loop for inventory mix decisions
- Historical sales data exists (2-3 years) but no visit data

### 3. Last-Mile Delivery Friction (EXPANDED)
- Drivers lack site specifics before delivery
- Failed/infeasible deliveries due to site constraints
- Wastes time and money on re-attempts
- Customer frustration from failed deliveries

### 4. Missed Upsell Revenue (NEW)
- Dealers lack structured path to offer ancillary services
- Potential services: pads, septic, access roads
- Losing high-value contractor revenue
- Graceland dealers have GC licenses they don't leverage

---

## Specific Requirements Captured

### MVP P0: On-Lot QR/Slot System
| Requirement | Detail |
|-------------|--------|
| **QR Code Approach** | 20 fixed "slot" QR codes per lot (not per-building) |
| **Mapping** | Backend maps slot → current inventory in that position |
| **Intake Form** | Captures email/phone, auto-tags building scanned |
| **Multi-Scan Tracking** | Track multiple scans per user across buildings |
| **Notifications** | Instant alerts to attendant on form submission |

### MVP P1: Website Quick Fixes
| Requirement | Detail |
|-------------|--------|
| **Fix Rendering** | Broken images, basic UX issues |
| **Add Intake Flow** | Guided form to capture contact + preferences |
| **Route to Attendant** | Instant notifications via email/SMS |

### MVP P2: Lightweight CRM
| Requirement | Detail |
|-------------|--------|
| **Lead-to-Inventory Tie** | Link scans to specific buildings |
| **Customer Portfolio** | Track interest history per customer |
| **Question Set** | Engineered questions to segment buyers |

### Future/Optional
- Camera-based vehicle counting (single entry/exit supports this)
- App-based incentives (10% off drawings)
- Geo-fence follow-ups
- "View in your space" visualization
- Contractor marketplace integration
- Content generation for marketing

---

## Current Tech Stack (Updated)

| System | Purpose | Status |
|--------|---------|--------|
| Excel | Inventory/slot mapping | In use - may migrate to Sheets |
| Graceland Portal | Serials/specs/pictures | Read-only access |
| AmericanSteelInc.com | Metal building quotes | Builder tool |
| Website CMS | Lead capture | Broken - needs fixes |
| **NEW** Dynamic QR/Link Mgmt | Slot QR codes | Proposed (Bitly/Dubb-like) |
| **NEW** Intake Forms | Lead capture | Proposed (Lovable/Bolt.new) |
| **NEW** Notifications | Attendant alerts | Proposed (email/SMS/push) |

---

## Budget Context (Updated)

| Item | Amount | Notes |
|------|--------|-------|
| Marketing ad spend | $2,500/mo | Comfortable with promo spend |
| White-label social | $1,000-$2,800/mo | Krista Green option discussed |
| MVP development | Not specified | To be scoped |

---

## Timeline

- **This week:** MVP scope alignment
- **Website access:** Ready "whenever"
- **Target:** MVP onboarding by Friday if scope defined
- **Parallel:** 2-3 discovery calls next week for other prospects
- **Early mornings:** Working sessions ongoing

---

## Key Decisions Made

1. **QR Code Strategy:** Fixed slot-based QR codes (not per-building) to reduce maintenance
2. **Website Approach:** Patch now + intake form, full revamp later
3. **Data Processing:** Use AI (Google AI Studio/Gemini) to parse 300-page SOT
4. **Notifications:** Low-latency email/SMS/push on form submissions
5. **Measurement:** Start capturing new metrics, compare to historical sales

---

## Objections Addressed

| Objection | Resolution |
|-----------|------------|
| 300-page SOT complexity | Pre-process with headings/mind maps, AI extraction, focus MVP |
| Website rework vs patch | Patch + intake now for immediate ROI, plan full revamp later |
| QR maintenance burden | Fixed slot codes (20 per lot), backend remap on inventory change |

---

## Graceland Network Opportunity (EXPANDED)

Chris articulated a **platformizable vision**:
- Prove value at S&S Wolfsheds first
- Expand to Arizona Graceland dealer network
- Portable buildings, greenhouses, shipping containers, metal buildings
- Contractor services marketplace (leverage GC licenses)

**This changes the engagement from one-off client to potential platform play.**

---

## Questions Asked

### We Asked:
1. Can we restate the project goal?
2. What's the MVP with highest near-term impact?
3. How are inventory and slot mapping managed today?
4. Do you have baseline metrics (footfall vs close rate)?
5. Is there one-way in/out to facilitate counting?
6. How will we process the 300-page SOT?
7. Should we fix current site or wait for rebuild?

### They Asked:
1. How to implement QR codes without heavy maintenance?
2. Can website changes be iterative?
3. How to get instantaneous attendant alerts?
4. How to manage internal vs external app views?
5. How to quantify ROI without full data?
6. What scheduling platform to unify calendars?

---

## Action Items

| Owner | Action | Status |
|-------|--------|--------|
| Chris | Upload SOT v1 'Keys to the Castle' to Slack | Pending |
| Matthew | Check SNS Excel for external refs/macros, migrate to online | Pending |
| Team | 6am Dec 29 sync re: priorities/MVP | Scheduled |
| Team | Set up shared client intake/pre-call file structure | Pending |
| Team | Research Calendly sync options (Cal.com?) | Pending |
| Team | Re-run SNS onboarding flow in AI Studio | Pending |
| Chris/Matthew | Grant website access, fix images, add intake form | Pending |
| Team | Review Krista Green white-label sheet | Pending |

---

## Links

### Meeting Recording
- [Fathom Recording](https://fathom.video/share/DB8EPPNDUmnRMsex7xSZCoaeAq5kCXXw)
- SOT Upload Action: [Clip](https://fathom.video/share/DB8EPPNDUmnRMsex7xSZCoaeAq5kCXXw?timestamp=153.9999)
- Website Access Action: [Clip](https://fathom.video/share/DB8EPPNDUmnRMsex7xSZCoaeAq5kCXXw?timestamp=5276.9999)

### Demos Created During Call
- [Google AI Studio Demo](https://ai.studio/apps/drive/1IVAPcSR98Qqt9Fnkz4UZYs_N0ZycrrtN) - Website update with onboarding form
- [NotebookLM Demo](https://notebooklm.google.com/notebook/0d9bc650-b425-424c-a005-25fb11610c71) - SOT mind map visualization

### Client Resources
- [SOT v1 Workbook 1](https://drive.google.com/file/d/1Uhg0XNy_954pVHHTDCAotJJ-9pVl6XXi/view?usp=drive_link) - "Keys to the Castle" (~300 pages)

### White-Label Services
- [White-Label Agency Google Doc](https://docs.google.com/document/d/1BDxsLHTvvrQq3ERSLB84EQ98soJD4pgVlAFOwBaFFIE/edit?tab=t.0) - Krista Green pricing/terms

---

## Key Quotes from Transcript

### Chris on the Core Problem
> "A lot of the issues that they talked about is, like, sometimes if there's 15 people, or 10 people, or five people at a dealership and we only have one attendant, right? Who's to say that out of that five people, one of them was able to slip away without even being noticed, right? And I'm trying to capture those guys."

### Chris on the Hyperlink/QR Strategy
> "The original idea here is to create a lot attendant. So if somebody was to roll up onto the dealership, they would interact with the hyperlink. The hyperlink would be able to, like, they would be incentivized to give us their name, phone number, and email. Then, from that ability, they'd be like, okay, walk along the dealership, scan the hyperlink, right? And then get your information about the building."

### Chris on Customer Portfolio & Delivery
> "The second one is to connect that portfolio to the driver. Then as the customer has access to their portfolio, when they get that call the night before... the driver gets all the maps, all the details. They know how, if I load the building on this way, then I can just back up to the thing. And I don't have to unload the building and put it on wheels. And I just save you 45 minutes."

### Chris on the Platform Vision
> "Gentlemen, we can charge a monthly fee to manage other people's dealerships. And the cool thing about it is that it doesn't have to be just portable buildings. Like, if you break it down, it can be inventory management of a multitude of different types of things."

### Trent on Slot-Based QR Approach
> "Building one always has the same QR code. Building two always has the same QR code... So the trickiest part there is creating a simple QR code to a web address is quite literally just encoded in the QR. But you can do dynamic ones."

### Matthew on Website Strategy
> "The easiest way that we're going to be able to set that up is through the website. Creating an Android app is going to take longer. Adding something to the existing website, which is a new path, will be the lowest hanging fruit."

### Chris on Inventory Constraints
> "Every dealership only can do, let's just say 20 buildings, right? They can't have more than 20 buildings on that lot."

### Trent on Graceland Portal Integration
> "The good thing about Excel is that you can build structure and you can make it whatever you want. The bad thing about Excel is that you can make it whatever you want and people break it all the time. So the idea would be to migrate away from Excel, but meet where they are now to try to integrate what they have."

### Chris on the Contractor Services Opportunity
> "The opportunity that comes through these gates for upsell for like myself with the GC license is truly like a lot of missed opportunities. Oh, you need a concrete pad? Oh, yeah, let me get Remus Development over here. Oh, you need a septic system going? Oh, yeah, I got EUS Underground."

### Chris on Archiefab Partnership
> "I just got Archie Fab who is waiting to meet you guys. He can do the conceptual, he can do the architectural, and send off the permitting for the client and completely handle the whole turnkey solution. Anything metal for us from now on."

---

## Technical Details from Discussion

### Graceland Portal Access
- Chris demonstrated live access to Graceland portal during call
- Shows inventory by lot with serial numbers, specs, diagrams
- Format: Serial number like "GSX" = Garden Shed + dimensions
- Portal provides pictures and specifications for each building

### American Steel Builder Tool
- Currently using AmericanSteelInc.com Build & Price tool for metal building quotes
- Has "View in your space" feature that S&S wants for Graceland buildings
- Tool is successful and profitable for its creator
- Graceland reportedly working on similar builder tool

### AI Processing Approach (Discussed)
- Team tested uploading SOT to Google AI Studio during call
- Created mind map visualization of 300-page document
- Discussed using embeddings/RAG for semantic search
- Mekaiel demonstrated Bolt.new intake form prototype live on call

### Intake Form Prototype (Live Demo)
Matthew demoed a Bolt.new-generated intake form during call:
- 10% off special offer entry point
- Email/phone capture
- Building type selection (storage shed, utility, etc.)
- Size preferences
- Timeline questions
- Schedule consultation CTA
- Built in "single shot" from one prompt

---

## White-Label Marketing Services Discussed

### Krista Green Wholesale Pricing (Accelerator Members)
| Service | Wholesale | Suggested Resale |
|---------|-----------|------------------|
| 12 posts/month | $1,000 | $1,200-$2,800 |
| 8 posts/month | TBD | TBD |
| Business website (8 pages) | $2,500 | $6,000-$10,000 |

**Chris's Interest:**
> "I will pay for that 12th post, like right, like tomorrow. I got 30 hours worth of time. High-end videos of drones, videos of deliveries, pictures, like, I don't have to worry about that."

**Team agreed** to review Krista Green's white-label sheet for potential SNS marketing upsell.

---

## Arizona Graceland Dealer Network Context

Chris explained unique Arizona market dynamics:
- ~6 key dealers in Arizona Graceland network
- Arizona/New Mexico have unique terrain challenges (hard ground)
- Graceland spends extra money for AZ/NM due to terrain
- Arizona dealers have different challenges than other regions
- Chris knows all 6 key players personally
- Strategy: Prove value at S&S, then leverage for network rollout

> "We build this out, leverage the system to force Graceland to kind of adhere to, because what happens in Arizona is very unique to Arizona and Arizona only because of the terrain."

---

## Incentive Strategy Discussed

Chris mentioned Graceland's new commission structure enables incentives:
- "$50 off if you answer these 7 questions"
- Engineered questions to profile customer type
- Data helps with inventory decisions and ad targeting
- Potential shed giveaway ($2,600 mini-shed + $2,500 ad campaign)
- App entry could give double entries for followers

---

**Created:** December 28, 2025
**Updated:** December 28, 2025 (Added transcript details)
**Status:** Working Session Complete - MVP Alignment in Progress
