# Plotter Mechanix - Agent Context Handoff

**Last Updated:** February 22, 2026
**Operator:** Mekaiel Abdullahi (Product Manager & Client Activation Lead)
**Client:** Kelsey Hartzell, Plotter Mechanix (plotter/printer repair business in Arizona)

---

## Quick Summary

Plotter Mechanix is an active client of Arise AI Group. **Phase 1 is complete and over-delivered.** We are now preparing **Phase 2 proposal ($15,000 / 2-3 weeks)** focused on Shopify integration and scaling supply sales.

---

## Client Profile

| Field | Value |
|-------|-------|
| **Company** | Plotter Mechanix (DBA of MYTPIX LLC) |
| **Owner** | Kelsey Hartzell |
| **Location** | Glendale, AZ |
| **Business** | Large format printer/plotter repair, supplies, equipment sales |
| **Team** | Kelsey (owner/technician), Alyssa (office admin), Andrew (sales), Joe (technician), Megan (operations) |
| **Tech Stack** | Jobber (CRM/scheduling), Quo (phone system), Ply (inventory), Shopify (e-commerce), QuickBooks, Capsule (legacy CRM), Microsoft Exchange |

---

## Phase 1 - COMPLETED

### Contract Details
- **Project Name:** PlotterOps Quick Win Sprint
- **Value:** $5,000 (paid in full upfront)
- **Signed:** December 22, 2025
- **Duration:** 4 weeks + 30-day support

### Original SOW Deliverables
1. Supporting SOPs for Quo/Jobber integrations
2. Communication Protocol Guide
3. Training Videos
4. Live Training Session
5. PlotterOps Blueprint

### What Was Actually Delivered (Over-Delivered)
Phase 1 **significantly exceeded scope** - built production software instead of just documentation:

1. **Complete Phone System Migration**
   - Ported Kelsey's cell (602-722-8932) from Verizon to Quo
   - Ported office number (602-606-8845) from Vonage to Quo
   - 3 Quo users configured (Kelsey, Alyssa, Andrew)
   - IVR menu: Press 1=Service, 2=Supplies, 3=Printing, 4=Equipment
   - Business hours configuration (8 AM - 6 PM MST)
   - AI virtual assistant for after-hours

2. **Custom Quo-to-Jobber Integration (n8n)**
   - Automated workflow creates Jobber requests from Quo calls
   - AI extracts customer info, service issues, supplies needed
   - Call transcripts auto-logged to requests
   - Fixed duplicate client creation issues

3. **AI Call Intelligence**
   - Real-time transcription
   - AI categorization (service/supplies/sales)
   - Entity extraction (model numbers, part numbers, error codes)

4. **Compliance**
   - SMS privacy policy added to website
   - Hiya/Free Caller Registry registration
   - A2P carrier registration for texting

5. **Knowledge Base**
   - Claude AI project with PlotterMechanix.com content
   - Service manuals in Google Drive

### Phase 1 Report Location
`/plotter-mechanix/phase-1-accomplishment-report.md`

---

## Phase 2 - IN PROPOSAL

### Scope (from Feb 20, 2026 meeting)

**Budget:** $15,000
**Timeline:** 2-3 weeks

### Core Deliverables

1. **Ply → Shopify Integration**
   - Sync inventory between Ply and Shopify
   - Automate supply sales and order tracking
   - Remove manual inventory update bottleneck
   - Megan is connecting Ply to Jobber (supports this)

2. **Service Request Form Redo**
   - Fix confusing Jobber form
   - Fields needed: Company, Address, Contact Name, Cell#, Office#, Email, Machine Manufacturer (dropdown), Machine Model, Issue Description, Error Codes
   - Add photo/video upload capability

3. **Service Manuals Behind Login**
   - Move public manuals to members-only area
   - Legal/competitive protection
   - Shopify members-only tag system

4. **Communication Center Refinements**
   - Ongoing Quo improvements
   - Contact syncing fixes
   - Vendor vs customer call differentiation

5. **SOPs and Training**
   - One-page Quo workflow do's/don'ts
   - Training videos for team
   - Phase completion sign-off ceremony

### Additional Opportunities Discussed

- **Voice AI Agent** - Dual-purpose for lead capture + appointment setting
- **Lead Nurture System** - Auto cloud code for follow-up automation
- **Outbound Calling** - Air Call auto dialer integration

---

## Mekaiel's Current Action Items

| Priority | Task | Notes |
|----------|------|-------|
| 1 | Package Phase 1 deliverables | Compile videos, chats, report into Google Drive folder |
| 2 | Draft Phase 2 SOW | $15k, 2-3 weeks, Ply-Shopify + form + manuals |
| 3 | Create Quo SOP one-pager | Do's and don'ts for workflow adoption |
| 4 | Design retainer tiers | Post-Phase 2 support pricing (different SLA levels) |
| 5 | PlotterOps Blueprint | Visual roadmap showing phases and optimizations |
| 6 | Review Scaling Supplies PRD | Align scope with current proposal |

---

## Matthew's Current Action Items

- Redo service request form in Jobber (~30 min estimate)
- Move service manuals behind login
- Develop Ply-Shopify demo integration
- Compile training videos
- Push lead nurture system repo
- Collaborate with Trent on timeline estimates

---

## Key Pain Points to Solve

1. **Manual inventory updates** - Shopify not synced with Ply, causing delays
2. **Contact chaos** - Multiple systems (Quo, Jobber, Capsule, Exchange, iPhone) not synced
3. **Vendor calls creating requests** - Need to differentiate vendors from customers
4. **Form confusion** - Current service request form too complicated
5. **Team adoption** - Alyssa, Andrew, Joe need clearer workflows
6. **After-hours calls** - Some customers hanging up on AI voice (want Kelsey's voice)

---

## Client Relationship Context

- Kelsey is enthusiastic but overwhelmed (wearing many hats)
- He provides referrals actively (gave us 4 leads during Phase 1)
- Quick to give feedback via WhatsApp (sometimes frustrated with learning curve)
- Values personal touch - wants his voice on greetings, not AI
- Working 14+ hour days, needs systems that reduce his load
- Wife + family time is important to him (wants after-hours protection)

---

## Referrals from Kelsey (Potential Leads)

| Name | Business | Notes |
|------|----------|-------|
| Brad Ellyson | Metal fabrication | $100k/week payroll, 50-60 employees |
| Alex | Restaurant consulting | Italian restaurant needs AI receptionist |
| Rolling Landscape | Landscaping | 100+ employees, interested in AI |

---

## Key Files in Project Folder

```
plotter-mechanix/
├── phase-1-accomplishment-report.md    # Completed Phase 1 analysis
├── agent-context-handoff.md            # This file
├── roi-calculator-presentation-data.md # ROI data for sales
├── audit/
│   ├── README.md
│   └── kelsey-revenue-scaling-vision.md
└── offer/
    └── phase-2/
        ├── README.md
        └── 2026-02-20-closing-call/
            └── sales-call-prep.md
```

---

## Team Roles (Arise AI Group)

| Person | Role | Focus |
|--------|------|-------|
| Mekaiel | PM & Client Activation | Sales calls, proposals, PRDs, client comms |
| Matthew Kerns | Production Engineer | Code, integrations, n8n workflows |
| Trent Christopher | Technical Lead | Architecture, Quo setup, delivery testing |
| Chris Andrade | Lead Generator | Relationships, referrals, support |

---

## Next Steps

1. **Finalize Phase 2 SOW** - Get sign-off from Kelsey
2. **Create Phase 1 sign-off package** - Google Drive folder with all deliverables
3. **Coordinate with Matthew + Trent** - Timeline and hours estimate
4. **Design retainer model** - For post-Phase 2 ongoing support

---

## WhatsApp Chat Context

The WhatsApp group "Plotter Mechanix" contains all project communication from Jan 16 - Feb 21, 2026. Key participants:
- Kelsey (~Kelsey)
- Matthew Kerns
- Trent AAA
- Chris AAA
- Mekaiel A.

Chat export analyzed and summarized in `phase-1-accomplishment-report.md`.

---

*This context document enables any agent to pick up the Plotter Mechanix project with full understanding of history, current state, and next actions.*
