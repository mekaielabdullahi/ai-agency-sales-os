# STATEMENT OF WORK

## Phase 1: Foundation Sprint

**SOW Number:** ARISE-SSWOLF-P1-2026-001
**Effective Date:** Upon signature and payment
**Version:** 1.0

---

## 1. Parties

**Service Provider:**
Arise Group AI ("AriseGroup" or "Provider")
[Address]
[Contact Email]

**Client:**
S&S Wolf Sheds ("Client")
Sandy Williams, Owner
[Address]
[Contact Email]

---

## 2. Project Overview

### 2.1 Project Name
S&S Wolf Sheds — Phase 1 Foundation Sprint

### 2.2 Project Description
Provider will deliver a 2-week engagement establishing operational foundations for Client, including stakeholder interviews, ROI assessment, website repairs, database foundation, and lead capture system implementation.

### 2.3 Project Objectives
- Establish validated baseline metrics through stakeholder interviews
- Repair website credibility issues (images, mobile, performance)
- Create centralized database foundation for inventory and costs
- Implement lead capture system with automated notifications
- Document initial Standard Operating Procedures (SOPs)

---

## 3. Scope of Work

### 3.1 Deliverable 1: ROI Assessment & Stakeholder Interviews

**Description:** Structured interviews with key stakeholders to gather baseline metrics and document operational processes.

**Tasks:**
| Task | Description | Duration |
|------|-------------|----------|
| 1.1 | Sandy Williams Interview (Owner) | 30 minutes |
| 1.2 | Matthew Williams Interview (Operations) | 20 minutes |
| 1.3 | Alex Interview (Website/Marketing) | 15 minutes |
| 1.4 | Scott Interview (Driver/Delivery) | 15 minutes |
| 1.5 | ROI Calculator Population | 2 hours |
| 1.6 | CODB Validation | 1 hour |
| 1.7 | Lead Handling SOP Documentation | 2 hours |
| 1.8 | Lot Operations SOP Documentation | 2 hours |
| 1.9 | Validation Workshop with Sandy | 45 minutes |

**Deliverables:**
- [ ] Completed interview recordings (with permission)
- [ ] Populated ROI Calculator with validated data
- [ ] CODB (Cost of Doing Business) validation report
- [ ] Lead Handling SOP document
- [ ] Lot Operations SOP document
- [ ] Validation workshop summary

**Acceptance Criteria:**
- All 4 interviews completed
- 7 data gaps in ROI Calculator filled
- CODB validated (not estimated)
- 2 SOPs documented and approved by Client
- Validation workshop completed

---

### 3.2 Deliverable 2: Website Quick Fixes

**Description:** Repair critical website issues affecting credibility and user experience.

**Tasks:**
| Task | Description | Duration |
|------|-------------|----------|
| 2.1 | Website image audit | 2 hours |
| 2.2 | Fix broken/blank images | 4 hours |
| 2.3 | Repair broken embeds | 2 hours |
| 2.4 | Mobile responsive CSS fixes | 4 hours |
| 2.5 | Image compression & lazy loading | 2 hours |
| 2.6 | Northern AZ schema markup (local SEO) | 2 hours |
| 2.7 | Cross-device testing | 2 hours |

**Deliverables:**
- [ ] All product page images loading correctly
- [ ] All embeds functional
- [ ] Mobile-optimized layouts
- [ ] Page load time under 3 seconds
- [ ] Local SEO schema markup implemented

**Acceptance Criteria:**
- Zero broken images on product pages
- Website displays correctly on mobile devices (iOS/Android)
- Page load time < 3 seconds (measured via PageSpeed Insights)
- Schema markup verified via Google Rich Results Test

---

### 3.3 Deliverable 3: Database Foundation

**Description:** Establish centralized data infrastructure for inventory and financial tracking.

**Tasks:**
| Task | Description | Duration |
|------|-------------|----------|
| 3.1 | Firebase/cloud account setup (CEO-owned) | 1 hour |
| 3.2 | Developer access configuration (Editor only) | 30 minutes |
| 3.3 | Data structure design (snake_case standards) | 2 hours |
| 3.4 | Sheet 1: Master Shed Data migration | 4 hours |
| 3.5 | Sheet 7: CODB Calculator setup | 2 hours |
| 3.6 | Data validation and cleanup | 2 hours |
| 3.7 | Documentation of data standards | 1 hour |

**Deliverables:**
- [ ] CEO-owned Firebase/cloud account active
- [ ] Developer access configured (Editor permissions only)
- [ ] Sheet 1: Master Shed Data populated
- [ ] Sheet 7: CODB Calculator populated
- [ ] Data standards documentation

**Acceptance Criteria:**
- All products migrated with snake_case compliance
- Pure numbers (no currency symbols in data fields)
- CODB Calculator populated from ROI Assessment data
- Client retains full ownership of all accounts and data

**Data Standards (Contractual):**
| Standard | Requirement |
|----------|-------------|
| Field naming | snake_case (e.g., `base_price`, `model_id`) |
| Numbers | Pure numeric values (e.g., `1499.99` not `$1,499.99`) |
| No special characters | Numeric fields contain digits and decimals only |

---

### 3.4 Deliverable 4: Customer Onboarding Form

**Description:** Implement lead capture system to convert website visitors into tracked prospects.

**Tasks:**
| Task | Description | Duration |
|------|-------------|----------|
| 4.1 | Form design (mobile-first) | 2 hours |
| 4.2 | Form implementation | 4 hours |
| 4.3 | Auto-responder configuration | 1 hour |
| 4.4 | Sales notification setup | 1 hour |
| 4.5 | Homepage deployment | 1 hour |
| 4.6 | Contact page deployment | 1 hour |
| 4.7 | Product page deployment | 2 hours |
| 4.8 | Testing and QA | 2 hours |

**Form Fields:**
| Field | Type | Required |
|-------|------|----------|
| `full_name` | Text | Yes |
| `email` | Email | Yes |
| `phone` | Phone | Yes |
| `interested_in` | Dropdown | Yes |
| `preferred_size` | Dropdown | No |
| `timeline` | Dropdown | Yes |
| `how_did_you_hear` | Dropdown | Yes |
| `message` | Textarea | No |
| `preferred_lot` | Dropdown | No |

**Deliverables:**
- [ ] Mobile-friendly intake form
- [ ] Auto-responder configured
- [ ] Sales team notification system (within 5 minutes)
- [ ] Form deployed on homepage, contact page, and product pages

**Acceptance Criteria:**
- Form submissions captured successfully
- Auto-responder sends within 60 seconds
- Sales team notified within 5 minutes of submission
- Form displays correctly on mobile and desktop

---

## 4. Project Timeline

### 4.1 Duration
Total project duration: **2 weeks (10 business days)**

### 4.2 Schedule

| Phase | Duration | Dates | Deliverables |
|-------|----------|-------|--------------|
| Week 1 | 5 days | Days 1-5 | D1 (Interviews/ROI), D2 (Website) |
| Week 2 | 5 days | Days 6-10 | D3 (Database), D4 (Form) |

### 4.3 Milestones

| Milestone | Target | Criteria |
|-----------|--------|----------|
| M1: Interviews Complete | Day 3 | All 4 interviews conducted |
| M2: Website Fixed | Day 5 | Zero broken images, mobile working |
| M3: Validation Workshop | Day 5 | Priorities confirmed with Client |
| M4: Database Live | Day 8 | Master data and CODB populated |
| M5: Form Live | Day 10 | Leads capturing, notifications working |
| M6: Project Complete | Day 10 | All deliverables accepted |

---

## 5. Client Responsibilities

### 5.1 Required Participation
Client agrees to provide:

| Requirement | Timing | Duration |
|-------------|--------|----------|
| Sandy interview | Week 1, Day 1-2 | 30 minutes |
| Matthew interview | Week 1, Day 1-2 | 20 minutes |
| Alex interview | Week 1, Day 2-3 | 15 minutes |
| Scott interview | Week 1, Day 2-3 | 15 minutes |
| Validation workshop | Week 1, Day 5 | 45 minutes |
| Firebase account creation | Week 2, Day 1 | 15 minutes |

**Total Client Time Required:** Approximately 2.5 hours over 2 weeks

### 5.2 Access Requirements
Client will provide within 48 hours of project start:
- [ ] Website admin/hosting credentials
- [ ] Existing inventory spreadsheets
- [ ] Existing financial/cost data
- [ ] Email addresses for sales notifications
- [ ] Firebase/Google Cloud account (CEO-created, Week 2)

### 5.3 Response Time
Client agrees to respond to Provider questions/requests within **2 business days**.

---

## 6. Investment and Payment Terms

### 6.1 Total Investment
**$5,000.00 USD**

### 6.2 Payment Breakdown

| Component | Value |
|-----------|-------|
| ROI Assessment & Interviews | $1,500 |
| Website Quick Fixes | $1,000 |
| Database Foundation | $1,500 |
| Customer Onboarding Form | $1,000 |
| **Total** | **$5,000** |

### 6.3 Payment Schedule

**Option A: Full Payment (Recommended)**
- $5,000 due upon SOW execution
- Project begins within 48 hours of payment

**Option B: Split Payment**
- $2,500 (50%) due upon SOW execution
- $2,500 (50%) due at start of Week 2

### 6.4 Payment Method
- Stripe invoice
- Bank transfer (ACH)
- Check (must clear before project start)

### 6.5 Late Payment
Payments more than 7 days overdue may result in project pause until payment is received.

---

## 7. Intellectual Property and Ownership

### 7.1 Client Ownership
Upon full payment, Client owns:
- All data created or migrated
- All SOPs and documentation
- All form designs and implementations
- All database structures and accounts
- All website modifications

### 7.2 Provider Retention
Provider retains rights to:
- Methodologies and frameworks used
- Generic templates (not Client-specific content)
- Knowledge gained for future client work (anonymized)

### 7.3 Account Ownership
All accounts created (Firebase, hosting, etc.) will be:
- Created by Client (CEO)
- Owned by Client
- Provider granted Editor/Developer access only
- Provider access revocable by Client at any time

---

## 8. Acceptance Process

### 8.1 Deliverable Review
For each deliverable:
1. Provider notifies Client of completion
2. Client has **3 business days** to review
3. Client provides acceptance or specific revision requests
4. Provider addresses revisions within **2 business days**
5. Process repeats until acceptance

### 8.2 Acceptance Criteria
Deliverables are considered accepted when:
- All acceptance criteria listed in Section 3 are met
- Client provides written acceptance (email sufficient)
- OR 5 business days pass without Client response

### 8.3 Final Acceptance
Project is complete when:
- All 4 deliverables accepted
- All milestones achieved
- Final payment received (if split payment)

---

## 9. Warranty and Support

### 9.1 Warranty Period
Provider warrants all deliverables for **14 days** after final acceptance.

### 9.2 Warranty Coverage
During warranty period, Provider will fix at no charge:
- Bugs or errors in implemented solutions
- Issues with form functionality
- Database structure problems
- Any deliverable not meeting acceptance criteria

### 9.3 Exclusions
Warranty does not cover:
- Issues caused by Client modifications
- Third-party service outages (Firebase, hosting, etc.)
- New feature requests beyond original scope
- Training beyond initial handoff

---

## 10. Change Management

### 10.1 Change Request Process
Any scope changes require:
1. Written change request from either party
2. Impact assessment (timeline and cost)
3. Written approval from both parties
4. SOW amendment if significant

### 10.2 Minor Changes
Changes that do not affect timeline or cost may be approved verbally and documented via email.

### 10.3 Significant Changes
Changes affecting timeline by >2 days or cost by >$500 require written SOW amendment.

---

## 11. Confidentiality

### 11.1 Confidential Information
Both parties agree to keep confidential:
- Client business data and financials
- Provider methodologies and pricing
- Interview recordings and transcripts
- Any information marked "confidential"

### 11.2 Permitted Disclosure
Provider may disclose:
- Anonymized case study information (with Client permission)
- Client name as a reference (with Client permission)

---

## 12. Limitation of Liability

### 12.1 Liability Cap
Provider's total liability shall not exceed the total amount paid under this SOW ($5,000).

### 12.2 Exclusions
Neither party shall be liable for:
- Indirect, incidental, or consequential damages
- Lost profits or revenue
- Third-party claims

### 12.3 ROI Projections
ROI projections in proposal materials are estimates based on discovery data. Provider does not guarantee specific financial outcomes.

---

## 13. Termination

### 13.1 Termination for Convenience
Either party may terminate with **7 days written notice**.

### 13.2 Termination for Cause
Either party may terminate immediately if:
- Material breach not cured within 14 days of notice
- Bankruptcy or insolvency
- Illegal activity discovered

### 13.3 Effect of Termination
Upon termination:
- Client pays for work completed to date
- Provider delivers all work product created
- Provider removes access to Client systems

### 13.4 Refund Policy
- Termination before Week 1 start: Full refund minus $500 admin fee
- Termination during Week 1: 50% refund
- Termination during Week 2: No refund (work substantially complete)

---

## 14. General Provisions

### 14.1 Independent Contractor
Provider is an independent contractor, not an employee of Client.

### 14.2 Entire Agreement
This SOW constitutes the entire agreement for Phase 1. Any modifications require written amendment.

### 14.3 Governing Law
This agreement is governed by the laws of [State/Jurisdiction].

### 14.4 Dispute Resolution
Disputes will be resolved through:
1. Good faith negotiation (30 days)
2. Mediation (if negotiation fails)
3. Binding arbitration (if mediation fails)

---

## 15. Signatures

### Provider: Arise Group AI

**Signature:** _________________________________

**Printed Name:** _________________________________

**Title:** _________________________________

**Date:** _________________________________

---

### Client: S&S Wolf Sheds

**Signature:** _________________________________

**Printed Name:** Sandy Williams

**Title:** Owner

**Date:** _________________________________

---

## Appendix A: Deliverables Checklist

### Deliverable 1: ROI Assessment & Stakeholder Interviews
- [ ] Sandy Williams interview completed
- [ ] Matthew Williams interview completed
- [ ] Alex interview completed
- [ ] Scott interview completed
- [ ] ROI Calculator populated (7 data gaps filled)
- [ ] CODB validated
- [ ] Lead Handling SOP documented
- [ ] Lot Operations SOP documented
- [ ] Validation workshop completed

### Deliverable 2: Website Quick Fixes
- [ ] Image audit completed
- [ ] All broken images fixed
- [ ] All embeds functional
- [ ] Mobile responsive
- [ ] Page load < 3 seconds
- [ ] Local SEO schema implemented

### Deliverable 3: Database Foundation
- [ ] Firebase account created (CEO-owned)
- [ ] Developer access configured
- [ ] Sheet 1: Master Shed Data populated
- [ ] Sheet 7: CODB Calculator populated
- [ ] Data standards compliance verified

### Deliverable 4: Customer Onboarding Form
- [ ] Form designed and implemented
- [ ] Auto-responder configured
- [ ] Sales notifications working
- [ ] Deployed on homepage
- [ ] Deployed on contact page
- [ ] Deployed on product pages
- [ ] Mobile and desktop tested

---

## Appendix B: Contact Information

### Provider Contacts

**Primary Contact:**
- Name: Chris Andrade
- Role: Project Lead
- Email: [email]
- Phone: [phone]

**Technical Contact:**
- Name: Matthew Kerns
- Role: Technical Lead
- Email: [email]
- Phone: [phone]

### Client Contacts

**Primary Contact:**
- Name: Sandy Williams
- Role: Owner
- Email: [email]
- Phone: [phone]

**Technical Contact:**
- Name: [Name]
- Role: [Role]
- Email: [email]
- Phone: [phone]

---

**Document Information:**
- SOW Number: ARISE-SSWOLF-P1-2026-001
- Version: 1.0
- Created: January 4, 2026
- Last Updated: January 4, 2026
