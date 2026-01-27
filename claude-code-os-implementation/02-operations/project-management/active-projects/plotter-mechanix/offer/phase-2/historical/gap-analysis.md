# Phase 2 Gap Analysis - Draft-02 vs Current Plan

**Created:** January 24, 2026
**Purpose:** Identify missing deliverables and validate business problems → time spent → ROI

---

## Executive Summary

**Problem:** Current Phase 2 plan is missing critical deliverables from draft-02, particularly:
1. **Email automation** (validated pain point for Alyssa)
2. **Unified Ops Hub / Chat Agent** (eliminates context-switching)
3. Quo-Ply integration assumed we could modify Quo UI (we can't)

**Solution:** Revise Phase 2 to work from validated business problems → measured time waste → process improvement → solutions

---

## Comparison: Draft-02 vs Current Plan

### Draft-02 Had (Dec 2025)

| Deliverable | Investment | Key Features |
|-------------|------------|--------------|
| **1. Working Inventory System** | ~$10k | Product database, stock levels, usage tracking, reorder alerts, RMA tracking, integrations to Jobber/QuickBooks/Shopify |
| **2. Unified Ops Hub** | ~$10k | Chat agent expansion, job dashboard, financial snapshot, inventory status, customer 360 view |
| **3. Complete SOP & Training Library** | ~$10k | Core workflow SOPs, technical knowledge base, training curriculum, video library, passive knowledge capture |
| **TOTAL** | **$30k** | 16 weeks |

**Key Insight:** Draft-02 had **email automation built into inventory system**:
> "Email | Vendor pricing updates auto-extracted and applied"

---

### Current Plan Has (Jan 2026)

| Deliverable | Investment | Key Features |
|-------------|------------|--------------|
| **1. Training System** | $18k | Chris filming, 25-30 videos, knowledge base |
| **2. Equipment CRM** | $10k | Customer equipment database, service contract scoring, maintenance history |
| **3. Ply Enhancements** | $8k | Used parts tracking, Quo↔Ply integration, custom config |
| **4. Integration Work** | $5k | Connect all systems via n8n |
| **5. Discovery & Collaboration** | $4k | Megan/Andrew interviews, SOP audit |
| **TOTAL** | **$45k** | 4-6 weeks |

**Key Changes:**
- Assumed Megan is handling inventory via Ply (not building custom inventory system)
- Equipment CRM is different from parts inventory
- No email automation
- No chat agent / unified ops hub
- Higher price, shorter timeline

---

## What We're Missing

### 1. Email Automation (HIGH PRIORITY) ❌

**Business Problem (From Draft-02):**
- Alyssa manages 10 inboxes manually
- Vendor pricing updates buried in emails
- RMA communications scattered
- Purchase orders lost in threads

**Validated Time Spent:**
- Alyssa: Inbox management = **X hours/week** (NEED TO VALIDATE)
- Email processing = **Y hours/week** (NEED TO VALIDATE)

**Solution from Draft-02:**
| System | Integration |
|--------|-------------|
| **Email** | Vendor pricing updates auto-extracted and applied |
| **Email** | Connected, pricing patterns identified |

**What This Means:**
- N8N monitors vendor emails (HP, Canon, Epson, etc.)
- Extracts pricing from PDFs/attachments
- Updates inventory system with new costs
- Flags RMAs for action
- Routes POs to appropriate person

**ROI Calculation (NEEDS VALIDATION):**
- Current: Alyssa spends ?? hrs/week on email processing
- After: 50-80% automated
- Savings: ?? hrs/week × $25/hr = $??k/year

**Investment Estimate:** $3,000-5,000

---

### 2. Unified Ops Hub / Chat Agent Expansion (MEDIUM PRIORITY) ⚠️

**Business Problem:**
- Context-switching between systems (Quo, Jobber, Ply, QuickBooks)
- "Do we have X?" requires checking Ply manually
- Can't find customer info quickly
- No single source of truth

**Current State (From Draft-02):**
> "Every piece of technology I've added has added a bigger headache." - Chris

**Solution from Draft-02:**

**Chat Agent Capabilities:**
- "Do we have HP 730 ink in stock?" → Queries Ply
- "What's our revenue this month?" → Queries QuickBooks
- "Show me everything about ABC Printing" → Aggregates from Jobber + Ply + Quo
- "What jobs are scheduled for tomorrow?" → Queries Jobber
- "Which invoices are overdue?" → Queries QuickBooks

**Technical Approach (Per User Feedback):**
> "Create a custom chat agent anyone at the company can use that has tool access to Ply, Quo, and Jobber"

**How This Works:**
- Web-based chat interface (already built foundation in Phase 1)
- Agent has API access to:
  - Ply (inventory queries)
  - Quo (call logs, customer context)
  - Jobber (jobs, customers, invoices)
  - QuickBooks (financial data)
  - Equipment CRM (from Phase 2)
- Natural language queries → Tool calls → Formatted responses

**Example Workflow:**

**Alyssa during call:**
> "Does ABC Graphics have any open invoices?"

**Agent response:**
> "Yes, 2 open invoices:
> - Invoice #1234: $850, due Jan 30
> - Invoice #1189: $1,200, overdue by 5 days
>
> Last service: Jan 15 (HP T730 maintenance)
> Equipment: HP T730 (Serial ABC123), Canon iPF9400 (Serial XYZ789)
> Parts in stock for their equipment: ✅ T730 maintenance kit, ❌ iPF9400 ink"

**ROI Calculation (NEEDS VALIDATION):**
- Current: ?? minutes per day context-switching
- After: Single interface for all queries
- Savings: ?? hrs/week × $25/hr = $??k/year

**Investment Estimate:** $5,000-8,000

---

### 3. Quo-Ply Integration Needs Revision (CONSTRAINT) 🔴

**User Feedback:**
> "We can't really update the Quo interface."

**Current Plan (Won't Work):**
- Option 1: Embedded panel in Quo ❌ (can't modify Quo UI)
- Option 2: Standalone tool ⚠️ (still requires context-switching)
- Option 3: Notifications ⚠️ (marginal improvement)

**Better Approach (Chat Agent Integration):**

**When customer calls:**
1. Quo webhook → N8N (already working from Phase 1)
2. N8N identifies customer → Looks up equipment
3. **NEW:** N8N sends context to Chat Agent
4. Chat Agent proactively displays:
   - Customer name
   - Equipment list
   - Common parts in stock for their equipment
   - Recent service history

**Alyssa workflow:**
- Customer calls (Quo handles call)
- Glances at Chat Agent window (auto-populated with customer context)
- Sees inventory status WITHOUT asking
- If customer asks about other parts, types in chat: "Do we have T730 belt?"
- Agent responds instantly

**Investment:** Included in Chat Agent expansion ($5k-8k)

---

## Validated Business Problems Framework

**User's Guidance:**
> "We need to work from business problems with validated time spent by employees → process improvement → solutions development"

### Problem → Time → ROI → Solution Mapping

| Problem | Who | Time Spent | Annual Cost | Solution | Expected Savings | Investment |
|---------|-----|------------|-------------|----------|------------------|------------|
| **Email inbox management** | Alyssa | ?? hrs/week | $??,000 | Email automation | ??% reduction | $3k-5k |
| **Context-switching between systems** | Alyssa | ?? min/day | $??,000 | Chat agent hub | ??% reduction | $5k-8k |
| **"Do we have X?" interruptions** | Kelsey/Alyssa | 10/day × 5 min | $62,500 | Ply API + Chat agent | 80% reduction | Included |
| **Training new techs** | Kelsey | 5 hrs/week | $78,000 | Video library | 50% reduction | $18k |
| **Equipment service history lookups** | Kelsey/Alyssa | ?? min/customer | $??,000 | Equipment CRM | ??% reduction | $10k |
| **Used parts revenue lost** | Business | $50k inventory | $5k-15k/year | Used parts tracking | $5k-15k recovery | Included |

**What We NEED to Validate:**
- ❌ Alyssa's email processing time (hrs/week)
- ❌ Alyssa's context-switching time (min/day)
- ❌ Equipment service history lookup time (min/customer)
- ✅ "Do we have X?" interruptions (10/day estimated, needs 1-week tracking)
- ✅ Kelsey's training time (5 hrs/week estimated, needs 1-week tracking)

---

## Revised Phase 2 Deliverables (Proposal)

### Option A: Add Missing Deliverables to Current Plan

| Deliverable | Investment | Status |
|-------------|------------|--------|
| 1. Training System | $18,000 | ✅ Keep |
| 2. Equipment CRM | $10,000 | ✅ Keep |
| 3. Ply Enhancements | $8,000 | 🔄 Revise (can't modify Quo) |
| 4. Integration Work | $5,000 | ✅ Keep |
| 5. Discovery & Collaboration | $4,000 | ✅ Keep |
| **6. Email Automation (NEW)** | **$5,000** | ➕ **Add** |
| **7. Chat Agent Hub (NEW)** | **$7,000** | ➕ **Add** |
| **TOTAL** | **$57,000** | Revised |

**Timeline:** 6-8 weeks (adding complexity)

**Problem:** Price increasing from $45k to $57k

---

### Option B: Replace Ply Enhancements with Chat Agent Hub

| Deliverable | Investment | Rationale |
|-------------|------------|-----------|
| 1. Training System | $18,000 | Core outcome: Kelsey scales |
| 2. Equipment CRM | $10,000 | Core outcome: Customer history |
| 3. **Chat Agent Hub (REVISED)** | **$10,000** | Replaces Quo-Ply integration + adds email automation + unified hub |
| 4. Integration Work | $5,000 | Connect Equipment CRM to Chat Agent |
| 5. Discovery & Collaboration | $4,000 | Validate with Megan/Andrew |
| **TOTAL** | **$47,000** | |

**Timeline:** 4-6 weeks

**Chat Agent Hub Includes:**
- Ply inventory queries ("Do we have X?")
- Quo call context (customer identified → equipment shown)
- Jobber job lookups
- Email automation (vendor pricing extraction)
- Equipment CRM queries
- All accessible via conversational interface

**Rationale:**
- Can't modify Quo UI anyway
- Chat Agent is more flexible (works on phone, desktop, anywhere)
- Solves multiple problems with one interface
- Email automation fits naturally into agent capabilities
- Higher ROI than trying to embed panels in Quo

---

### Option C: Modular Approach (Pick 5 from 7)

**Core Deliverables (Must Have):**
1. Training System - $18k ✅
2. Equipment CRM - $10k ✅
3. Discovery & Collaboration - $4k ✅

**Choose 2 from:**
4. Email Automation - $5k
5. Chat Agent Hub - $7k
6. Ply API Integration (standalone tool) - $6k
7. Advanced Integration Work - $5k

**Total:** $32k (core) + $10k-14k (choose 2) = **$42k-46k**

**Benefit:** Client chooses based on pain point priority

---

## Recommendations

### 1. Validate Time Spent FIRST (Week 1-2)

**Before finalizing Phase 2 scope:**

| Person | Track What | Duration | Purpose |
|--------|-----------|----------|---------|
| **Alyssa** | Email processing time | 5 days | Validate email automation ROI |
| **Alyssa** | Context-switching (system to system) | 5 days | Validate chat agent ROI |
| **Alyssa** | "Do we have X?" interruptions | 5 days | Validate Ply integration ROI |
| **Kelsey** | Training time with Joe | 5 days | Validate training system ROI |
| **Alyssa** | Equipment/service history lookups | 5 days | Validate Equipment CRM ROI |

**Deliverable:** Time-tracking report with actual hours/day per activity

---

### 2. Interview Megan About Ply (Week 1)

**Critical Questions:**
1. Does Ply have an API we can use?
2. What's included in Ply that we DON'T need to build?
3. What's NOT in Ply that the business needs?
4. How far along is Ply implementation (% complete)?
5. What help does Megan need from us?

**Purpose:** Don't build what Ply already does, fill the gaps

---

### 3. Choose Revised Approach (Week 2)

**After validation data + Megan interview:**

**If Ply API exists + Megan's making good progress:**
→ **Option B (Chat Agent Hub)** - $47k
- Ply handles inventory
- We build chat agent that queries Ply
- Add email automation
- Add Equipment CRM

**If Ply API limited or Megan needs help:**
→ **Option A (Full Build)** - $57k
- Build more custom inventory features
- Chat agent + email automation
- Help Megan with Ply config

**If budget constrained:**
→ **Option C (Modular)** - $42k-46k
- Client chooses 2 add-ons based on priority

---

## Open Questions

### For Matthew/Team:
1. What's our actual cost to build Chat Agent Hub? ($7k-10k estimate)
2. Can we deliver email automation in 4-6 week timeline?
3. What's our margin target on Phase 2? (currently 50% at $45k)
4. Do we have developer capacity for $47k-57k scope?

### For Kelsey/Nikki:
1. What's your budget ceiling for Phase 2?
2. Which pain points are MOST urgent?
   - Email overwhelm?
   - Context-switching?
   - Training Joe/hiring Steve?
   - Equipment history?
3. How much has been invested in Ply already?
4. Is Megan available to collaborate, or should we take over?

### For Megan (Interview):
1. Ply API capabilities?
2. What Ply covers vs. gaps?
3. Implementation status?
4. Where do you need help?

---

## Next Steps

### Immediate (This Week):
1. **Set up time tracking studies** with Alyssa/Kelsey
2. **Schedule Megan interview** to validate Ply status
3. **Confirm budget** with Kelsey/Nikki before finalizing scope

### Week 2:
4. **Compile validation data** (time tracking + Megan interview)
5. **Update Phase 2 scope** based on data
6. **Revise pricing** to match validated ROI
7. **Choose Option A, B, or C**

### Week 3:
8. **Present revised Phase 2** with data-backed ROI
9. **Close at $42k-57k** depending on scope
10. **Begin Phase 2 delivery**

---

*Created: January 24, 2026*
*Status: Gap analysis complete, awaiting validation data*
*Decision Required: Choose Option A, B, or C after Megan interview + time tracking*
