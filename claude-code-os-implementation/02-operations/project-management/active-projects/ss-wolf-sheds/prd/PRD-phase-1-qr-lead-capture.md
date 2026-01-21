# S&S Wolf Sheds - Digital Sales Engine PRD

## Phase 1: QR Lead Capture System

**Investment:** $10,000 | **Timeline:** 3 Weeks | **Location:** Flagstaff Lot

**Document Type:** Developer Handoff Document

---

## Executive Summary

S&S Wolf Sheds is losing potential customers who browse their lot and leave without being captured. This Phase 1 engagement delivers a **QR-based lead capture system** for the Flagstaff location that captures every interested visitor, notifies attendants in real-time, and tracks leads in a simple Google Sheet.

**Process Note:** Audit Flow (internal Arise methodology) will run concurrently with Phase 1 delivery.

---

## Success Criteria

### Business Success
- **5 leads captured by Week 3** (proof of concept)
- **20 leads captured in first full month**
- Every QR scan = a lead that would have been missed (baseline is zero)
- Flagstaff success triggers rollout discussion for other lots

### User Success
- Attendant receives notification within **90 seconds** of form submission
- Attendant can engage visitors they would have otherwise missed

### Technical Success
- Form loads within 3 seconds on mobile
- No silent failures - user always sees confirmation or error

---

## User Journeys

### Journey 1: Lot Visitor
Visitor arrives at Flagstaff lot → Sees QR code on shed → Scans with phone → Completes mobile form (name, phone, email, spot, timeline, how heard, giveaway opt-in) → Sees confirmation message → Attendant notified

### Journey 2: Lot Attendant
Receives email notification → Sees lead info (name, phone, which spot, timeline) + timestamp → Engages visitor or follows up later

### Journey 3: S&S Team
Views Google Sheet → Sees all captured leads → Adds notes for follow-up

---

## Technical Architecture

### Approach
Lightweight integration using Google Apps Script + Google Sheets + email SaaS. No custom application hosting required.

| Component | Implementation |
|-----------|---------------|
| QR Codes | Static, printed, one per spot (20 codes) |
| Lead Form | Universal URL, embedded on S&S website, mobile-optimized |
| Data Processing | Google Apps Script |
| Lead Storage | Google Sheets |
| Notifications | Email service (developer's choice - SendGrid, Mailgun, or similar) |

### Form Fields

| Field | Required |
|-------|----------|
| Name | Yes |
| Phone | Yes |
| Email | Yes |
| Spot # (from QR) | Yes |
| Timeline to Buy | Yes |
| How'd You Hear About Us | Yes (dropdown: Facebook, Google, Drove By, Referral, Other) |
| Giveaway Opt-in | Yes |

---

## Functional Requirements

### QR Code System

| ID | Requirement |
|----|-------------|
| FR1 | System can generate unique QR codes for each spot on the Flagstaff lot |
| FR2 | QR codes can link to a universal lead capture form |
| FR3 | QR codes can pass spot identification to the form |

### Lead Capture Form

| ID | Requirement |
|----|-------------|
| FR4 | Visitors can access the lead capture form via QR code scan |
| FR5 | Visitors can submit their name, phone, and email |
| FR6 | Visitors can select which spot/shed they scanned |
| FR7 | Visitors can indicate their timeline to buy |
| FR8 | Visitors can select how they heard about S&S Wolf Sheds |
| FR9 | Visitors can opt-in to the giveaway drawing |
| FR10 | Form can be completed on mobile devices |
| FR11 | Form can be embedded on the existing S&S Wolf Sheds website |
| FR12 | Visitor can see confirmation message after successful form submission |
| FR13 | Visitor can see error message if form submission fails |

### Notification System

| ID | Requirement |
|----|-------------|
| FR14 | System can send email notification to attendant(s) when a form is submitted |
| FR15 | Notification can include lead info (name, phone, email, spot, timeline) |
| FR16 | Notification can include timestamp of submission |
| FR17 | System can send notification within 90 seconds of form submission |

### Lead Tracking

| ID | Requirement |
|----|-------------|
| FR18 | System can record all form submissions to a Google Sheet |
| FR19 | Google Sheet can display: timestamp, name, phone, email, spot, timeline, how heard, giveaway opt-in |
| FR20 | S&S Team can view all captured leads in the Google Sheet |
| FR21 | S&S Team can add notes to lead records |

---

## Non-Functional Requirements

### Performance

| ID | Requirement |
|----|-------------|
| NFR1 | Email notification must be sent within 90 seconds of form submission |
| NFR2 | Lead capture form must load within 3 seconds on mobile devices |
| NFR3 | Form submission must complete within 5 seconds |

### Security

| ID | Requirement |
|----|-------------|
| NFR4 | Lead data (name, phone, email) must be transmitted over HTTPS |
| NFR5 | Google Sheet must be restricted to authorized S&S team members |

### Integration

| ID | Requirement |
|----|-------------|
| NFR6 | System must write lead data to Google Sheets |
| NFR7 | System must send notification via email service |
| NFR8 | If any integration fails, user must see error message (no silent failures) |

### Reliability

| ID | Requirement |
|----|-------------|
| NFR9 | System relies on cloud infrastructure (Google Apps Script, Google Sheets, email SaaS) with standard SaaS uptime |

### Accessibility

| ID | Requirement |
|----|-------------|
| NFR10 | Form must be usable on mobile devices (responsive design) |
| NFR11 | Form fields must have clear labels |

---

## Phase 1 Deliverables Summary

### Product Deliverables (This PRD)
- 20 QR codes for Flagstaff lot spots
- Mobile-optimized lead capture form
- Email notifications to attendant(s)
- Google Sheet lead tracking

### Service Deliverables (Separate from PRD)
- 3 stakeholder interviews
- Sales data analysis
- ICP report
- Ad strategy for March/April
- Customer follow-up scripts
- Giveaway campaign plan

---

## Future Phases (Not This PRD)

| Phase | Focus | Investment |
|-------|-------|------------|
| **Phase 2** | Dealer Accountability App + expansion to other lots | $5,000-$10,000 |
| **Phase 3** | Advanced Automation + Hub Infrastructure | $7,500-$15,000 |
| **Platform** | Graceland Dealer Network Solution | TBD |

---

**Document Status:** Ready for developer handoff

**Created:** January 21, 2026

**Generated via:** BMAD PRD Workflow
