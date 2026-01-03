# Phase 1 PRD: Foundation Sprint

**Project:** Lot Assistant - S&S Shed Sales System
**Phase:** 1 of 4
**Focus:** ROI Assessment + Website Quick Wins + Data Foundation
**Investment:** $5,000 (initial)
**IP Risk Level:** Low (generic product catalog)

---

## 1. Phase 1 Overview

Phase 1 establishes the business case and operational foundation before building advanced systems. This phase prioritizes:

1. **ROI Assessment** - Validate baseline metrics through stakeholder interviews
2. **Quick Wins** - Immediate visible improvements (website fixes, lead capture)
3. **Data Foundation** - Sources of truth for future phases

---

## 2. Quick Win: ROI Assessment & Stakeholder Interviews

**This is the anchor deliverable for Phase 1.** Before building systems, we must understand the business.

### 2.1 ROI Assessment Overview

| Attribute | Detail |
|-----------|--------|
| **Problem Addressed** | Shooting in the dark without baseline metrics; can't prove ROI without knowing starting point |
| **Solution** | Structured stakeholder interviews to gather financial and operational baseline data |
| **Outputs** | Completed ROI Calculator, validated CODB, initial SOPs from process discovery |
| **Timeline** | Week 1 |
| **Success Metric** | All data gaps filled in ROI Calculator; client understands their own numbers |

### 2.2 Qualification Question

**First question in any client conversation:**
> "Do you know your daily operating cost?"

| Answer | Meaning | Approach |
|--------|---------|----------|
| **Path A: Don't Know** | Flying blind operationally (most clients) | Help gather data together; discovery process IS the value |
| **Path B: Know Numbers** | Sophisticated operator (rare) | Move faster; plug into ROI model |

**Current Status:** S&S estimates ~$400/day but **unvalidated**. This is Path A.

### 2.3 Stakeholder Interview Schedule

| Stakeholder | Focus Areas | Duration | Priority |
|-------------|-------------|----------|----------|
| **Sandy (Owner)** | Revenue, pricing, lead flow, close rate | 30 min | HIGH |
| **Matthew (Williams/Analytics)** | Operating costs, payroll, time tracking | 20 min | HIGH |
| **Alex (Website/Social)** | Website traffic, social data, repetitive inquiries | 15 min | MEDIUM |
| **Scott (Driver)** | Delivery data, build error frequency | 15 min | MEDIUM |

### 2.4 Data to Gather (ROI Calculator Inputs)

**Financial Baseline:**
- Daily operating cost breakdown (validate $400/day estimate)
- Average shed sale price
- Monthly unit sales volume
- Gross margin per shed

**Lead & Conversion:**
- Current leads per month
- Close rate (leads → sales)
- Walk-in traffic per lot

**Time Tracking:**
- Hours/week on repetitive inquiries
- Hours/week on manual lead tracking
- Hours/week on pricing lookups

**See:** [Stakeholder Questions for ROI](../audit/stakeholder-questions-roi.md) | [ROI Calculator](../audit/roi-calculator.md)

### 2.5 Dual Output: ROI Data + SOPs

**Critical insight:** Stakeholder interviews produce TWO outputs:

| Output | Description | Value |
|--------|-------------|-------|
| **ROI Calculator Data** | Baseline metrics for investment justification | Proves value, enables measurement |
| **Initial SOPs** | Process documentation from "how do you currently..." questions | Operational foundation, quick win |

**Interview approach:**
1. "Walk me through how you handle a lead from first contact to close"
2. Document current process → becomes Lead Handling SOP
3. Identify gaps → becomes Phase 1 improvement opportunities
4. Capture time spent → becomes ROI savings calculation

---

## 3. Key Deliverables

Phase 1 consists of five deliverables:

### 3.1 ROI Assessment (The Business Case)

**Status:** QUICK WIN - Complete in Week 1

| Field | Description |
|-------|-------------|
| **Stakeholder Interviews** | 4 interviews (Sandy, Matthew, Alex, Scott) |
| **ROI Calculator** | Completed with validated baseline metrics |
| **CODB Validation** | Daily operating cost verified with breakdown |
| **Initial SOPs** | Process documentation from interview discovery |

**Why This Is The Quick Win:**
- Delivers immediate value (they understand their own business better)
- No development required - just structured conversations
- Builds trust through collaborative discovery
- Creates foundation for all ROI claims
- Produces SOPs as a "bonus" deliverable

**Deliverables:**
- [ ] Completed stakeholder interviews (all 4)
- [ ] ROI Calculator populated with actual data
- [ ] Daily operating cost breakdown validated
- [ ] Lead Handling SOP (from Sandy/Alex interviews)
- [ ] Lot Operations SOP (from Matthew/Scott interviews)
- [ ] ROI presentation for Sandy with HER numbers

---

### 3.2 Sheet 1: Master Shed Data (The Inventory)

A centralized log of all base models.

| Field | Description |
|-------|-------------|
| `model_id` | The unique key |
| `model_type` | Category/type of shed |
| `model_name` | Display name |
| `size` | Dimensions |
| `base_price` | Base cost (pure number) |
| `standard_features` | Included features |
| `colors` | Available colors |
| `picture_links` | URLs to product images |

**Purpose:** Acts as the database for all static specs.

---

### 3.3 Sheet 7: Operational Cost & CODB Calculator (The Financial Anchor)

A permanent log of business overhead.

| Field | Description |
|-------|-------------|
| Fixed Costs | Rent, insurance, etc. |
| Variable Costs | Fuel, supplies, etc. |
| Annual Sales Goals | Target units/revenue |

**Purpose:** Itemizes expenses to calculate the Daily Operating Cost and Cost Per Shed Sold (CODB)—the minimum revenue needed per unit to cover overhead.

**Note:** CODB Calculator is populated from ROI Assessment interviews with Sandy/Matthew.

---

### 3.4 SOP Generator (Operational Playbooks)

An AI-assisted system to generate and maintain Standard Operating Procedures for key dealership workflows.

| SOP Category | Description |
|--------------|-------------|
| **Lead Handling** | Step-by-step process from inquiry to quote |
| **Lot Operations** | Daily opening/closing checklists, inventory checks |
| **Sales Process** | Customer engagement, pricing, closing procedures |
| **Delivery Prep** | Pre-delivery checklist, site verification, driver handoff |
| **Customer Follow-up** | Post-sale follow-up cadence and scripts |

**Purpose:** Standardizes operations across all three lots (Tuba City, Flagstaff, Williams) to ensure consistent customer experience and enable scalable expansion.

**SOP Generator Features:**
- Template library for common dealership workflows
- Customizable checklists per lot/role
- Version control for procedure updates
- Mobile-accessible for field staff
- Integrates with accountability system (OPSYS-1)

**Note:** Initial SOPs (Lead Handling, Lot Operations) are created as output of ROI Assessment interviews. The SOP Generator then maintains and enhances these.

---

### 3.5 Website Quick Wins + Onboarding Form

Alongside the database foundation, Phase 1 includes critical website fixes to restore credibility and capture leads immediately.

#### Image & Display Fixes

| Issue | Description | Fix |
|-------|-------------|-----|
| **Blank/Broken Images** | Product images not loading, showing placeholder or broken icon | Audit all image URLs, re-upload missing assets, fix CDN/hosting paths |
| **Broken Embeds** | Embedded content (videos, maps, forms) not rendering | Update embed codes, check for HTTPS/HTTP mixed content issues |
| **Mobile Layout Issues** | Images/content overflowing or misaligned on mobile | Apply responsive CSS fixes, test across device sizes |
| **Storage/Hosting Errors** | Layout oddities from hosting migration | Verify asset paths, check .htaccess redirects, clear cache |

#### SEO & Performance Fixes

| Issue | Fix |
|-------|-----|
| Missing alt text on images | Add descriptive alt tags for all product images |
| Slow page load | Compress images, enable lazy loading |
| "Sheds near me" visibility | Add location-specific meta tags and schema markup for Northern AZ |

#### Customer Onboarding Form

A lead capture form embedded on the website to start building the CRM pipeline immediately.

**Form Fields:**

| Field | Type | Required |
|-------|------|----------|
| `full_name` | Text | Yes |
| `email` | Email | Yes |
| `phone` | Phone | Yes |
| `interested_in` | Dropdown (Shed types) | Yes |
| `preferred_size` | Dropdown (Sizes) | No |
| `timeline` | Dropdown (Immediate / 1-3 months / 3-6 months / Just browsing) | Yes |
| `how_did_you_hear` | Dropdown (Facebook, Google, Referral, Drove by, Other) | Yes |
| `message` | Textarea | No |
| `preferred_lot` | Dropdown (Tuba City, Flagstaff, Williams) | No |

**Form Requirements:**
- Mobile-friendly responsive design
- Submits to Firestore `leads` collection (or temporary Google Sheet until Firebase ready)
- Auto-responder email confirmation to customer
- Notification to sales team (email or SMS)
- CAPTCHA/spam protection

**Placement:**
- Homepage (above the fold CTA)
- Contact page
- Individual product pages (sidebar or footer)

---

## 4. Technical Architecture (Firebase/Firestore Migration)

For the transition to a cloud-based application, Phase 1 requires mapping these modules into Firestore Collections:

| Firestore Collection | Source | Document Key | Contents |
|---------------------|--------|--------------|----------|
| `products` | Sheet 1 | Model IDs | Base prices and specs |
| `financial_inputs` | Sheet 7 | Config docs | Fixed inputs for backend calculations |
| `sops` | SOP Generator | SOP IDs | Procedure steps, checklists, role assignments |
| `leads` | Onboarding Form | Lead IDs | Customer contact info, interests, source |

---

## 5. Data Standards & Hygiene

To prevent system failures during later phases, strict data entry rules must be followed during Phase 1:

### Pure Numerical Data

All pricing and cost columns (`base_price`, `option_price`, `monthly_amount`) must be entered as **pure numbers without currency symbols ($) or commas**.

> **Why:** Including these symbols treats the cells as "Text," which breaks the VLOOKUP and SUM formulas needed in Phase 2.

**Correct:** `1499.99`
**Incorrect:** `$1,499.99`

### Naming Conventions

All database fields must follow a `snake_case` format to ensure readability and prevent parsing errors across different programming languages.

**Examples:**
- `customer_name` ✓
- `base_price` ✓
- `CustomerName` ✗
- `Base Price` ✗

---

## 6. Project Management & IP Control

### Account Ownership
You (as the CEO) must create and own the Firebase/Google Cloud account.

### Access Control
When hiring a developer for this phase:
- ✓ Grant **Editor** or **Developer** access
- ✗ Never grant the **Owner** role

### Phased Disclosure Strategy

| Disclosure Order | Content | IP Risk |
|-----------------|---------|---------|
| **First** | Sheet 1 (Inventory), Website Fixes | Low |
| **Second** | SOP Templates, Onboarding Form | Low |
| **Later** | Sheet 7 (Financial Logic) | Medium |

Reveal the proprietary financial logic of Sheet 7 only after trust is established with the developer.

---

## 7. Implementation Roadmap

### Phase 1: Foundation Sprint (Current - $5,000)

**Week 1: ROI Assessment & Quick Wins (THE QUICK WIN)**
| Deliverable | Status | Notes |
|-------------|--------|-------|
| **ROI Assessment** | ⬜ Pending | Stakeholder interviews → Baseline metrics |
| Stakeholder Interview: Sandy | ⬜ Pending | Revenue, pricing, leads |
| Stakeholder Interview: Matthew | ⬜ Pending | Operating costs, time tracking |
| Stakeholder Interview: Alex | ⬜ Pending | Website, social data |
| Stakeholder Interview: Scott | ⬜ Pending | Delivery, build errors |
| **Initial SOPs** | ⬜ Pending | Output from interviews |
| Lead Handling SOP | ⬜ Pending | From Sandy/Alex interviews |
| Lot Operations SOP | ⬜ Pending | From Matthew/Scott interviews |
| Website Quick Fixes | ⬜ Pending | Broken images, mobile |

**Week 2: Data Foundation & Lead Capture**
| Deliverable | Status | Notes |
|-------------|--------|-------|
| Sheet 1: Master Shed Data | ⬜ Pending | Inventory database |
| Sheet 7: CODB Calculator | ⬜ Pending | Populated from ROI Assessment |
| Customer Onboarding Form | ⬜ Pending | Lead capture on website |
| SOP Generator Setup | ⬜ Pending | Template system for maintaining SOPs |

### Phase 2: Core Workflow ($5,000)
| Deliverable | Description |
|-------------|-------------|
| **Sheet 3: Optional Features Data** | Add-on pricing database for configurator (moved from Phase 1) |
| Sheet 2: Pricing Lookup Tool | Customer-facing configurator interface |
| Sheet 4: CRM & Sales Pipeline | Lead tracking with pipeline stages |
| QR/Slot Capture System | On-lot lead capture via QR codes |

### Phase 3: Intelligence Layer
| Deliverable | Description |
|-------------|-------------|
| Sheet 5: Customer Profile & Delivery Notes | Delivery logistics and site intelligence |
| Sheet 6: Financial Performance Dashboard | CPL, CAC, ROAS reporting |
| Traffic Counting / Analytics | Vehicle counting for conversion measurement |

### Phase 4: Platform Migration
| Deliverable | Description |
|-------------|-------------|
| Firebase Full Migration | All sheets → Firestore collections |
| Geofence Triggers | Automated follow-up on lot departure |
| Dealer Accountability App | Multi-location operations management |
| Platform for Graceland Network | Repeatable solution for other dealers |

---

## Summary

> Phase 1 is the "Concrete Slab" of your business house; it might look like a simple catalog of numbers, but if the slab is not perfectly level—with clean data and proper naming—every wall you build on top of it (the sales tools and dashboards) will eventually lean or crack.

---

## Phase 1 Checklist

### ROI Assessment (WEEK 1 QUICK WIN)
- [ ] Schedule stakeholder interviews (Sandy, Matthew, Alex, Scott)
- [ ] Prepare interview guides using stakeholder-questions-roi.md
- [ ] Complete Sandy interview (revenue, pricing, leads, close rate)
- [ ] Complete Matthew interview (operating costs, payroll, time tracking)
- [ ] Complete Alex interview (website traffic, social data, repetitive inquiries)
- [ ] Complete Scott interview (delivery data, build errors)
- [ ] Populate ROI Calculator with actual data
- [ ] Validate daily operating cost breakdown ($400/day estimate)
- [ ] Calculate baseline metrics (leads/month, close rate, avg sale price)
- [ ] Create Lead Handling SOP from Sandy/Alex interview insights
- [ ] Create Lot Operations SOP from Matthew/Scott interview insights
- [ ] Prepare ROI presentation for Sandy with HER numbers

### Database Foundation
- [ ] Create Firebase/Google Cloud account (CEO-owned)
- [ ] Set up `products` collection with all Model IDs
- [ ] Set up `financial_inputs` collection with overhead data
- [ ] Set up `sops` collection for procedure storage
- [ ] Set up `leads` collection for form submissions
- [ ] Validate all pricing fields are pure numbers (no $ or commas)
- [ ] Verify all field names follow snake_case convention
- [ ] Configure developer access (Editor role only)

### SOP Generator
- [ ] Define core SOP categories (Lead Handling, Lot Ops, Sales, Delivery, Follow-up)
- [ ] Create SOP template structure
- [ ] Import Lead Handling SOP from ROI Assessment interviews
- [ ] Import Lot Operations SOP from ROI Assessment interviews
- [ ] Build additional Delivery Prep SOP
- [ ] Configure mobile-accessible view for field staff
- [ ] Link SOPs to accountability system requirements

### Website Fixes
- [ ] Audit all product pages for broken/blank images
- [ ] Re-upload missing image assets
- [ ] Fix CDN/hosting paths for images
- [ ] Update broken embed codes (videos, maps)
- [ ] Fix HTTPS/HTTP mixed content issues
- [ ] Test and fix mobile layout issues
- [ ] Compress images for faster load times
- [ ] Add alt text to all product images
- [ ] Add Northern AZ location schema markup

### Onboarding Form
- [ ] Design mobile-friendly lead capture form
- [ ] Implement form fields (name, email, phone, interests, timeline, source)
- [ ] Set up form submission to Firestore `leads` collection (or temp Google Sheet)
- [ ] Configure auto-responder email to customers
- [ ] Set up sales team notifications (email/SMS)
- [ ] Add CAPTCHA/spam protection
- [ ] Embed form on homepage, contact page, and product pages

---

**Created:** January 3, 2026
**Next Phase:** Phase 2 - Core Workflow (CRM Pipeline & Pricing Lookup)
