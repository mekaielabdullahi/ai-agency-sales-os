# Job Checklist App - Implementation Plan

**Priority:** P0 - TOP OF GOLDFINCH ROADMAP
**Status:** Planning
**Created:** 2025-12-30
**Compute Strategy:** Use monthly compute credits efficiently

---

## Overview

A web app (then native mobile) that enables businesses to create and assign checklists to employees per job type. All data stored in backend.

**Target Users:** Field service businesses, contractors, franchises - anyone needing standardized job completion verification.

---

## Core Features (MVP)

### Business Admin Portal (Web)
- [ ] Create/edit job types (e.g., "HVAC Install", "Plumbing Repair", "Site Inspection")
- [ ] Create checklists per job type
- [ ] Assign employees to job types
- [ ] View completion reports
- [ ] Export data

### Employee Interface (Web → Native)
- [ ] View assigned jobs
- [ ] Complete checklists (checkboxes, photos, signatures, notes)
- [ ] Submit completed checklists
- [ ] Offline support (queue submissions)

### Backend
- [ ] User authentication (business admins, employees)
- [ ] Job type CRUD
- [ ] Checklist template CRUD
- [ ] Checklist submission storage
- [ ] Multi-tenant (each business has their own data)

---

## Development Phases

### Phase 1: Web MVP (Priority - Use Compute Now)
**Goal:** Working web app with core functionality

**Tech Stack:**
- Frontend: React/Next.js or Svelte (fast to build)
- Backend: Supabase or Firebase (fast auth + database)
- Hosting: Vercel/Netlify

**Deliverables:**
1. Admin can create job types
2. Admin can create checklists for job types
3. Employee can view and complete checklists
4. Data persists in database

**Estimated Effort:** 20-40 compute hours

---

### Phase 2: Production Hardening
**Goal:** Ready for real users

- [ ] User management (invite employees)
- [ ] Role-based access control
- [ ] Completion history/audit trail
- [ ] Basic reporting/dashboard
- [ ] Email notifications

**Estimated Effort:** 20-30 compute hours

---

### Phase 3: Native Mobile (Background with Autoclaude)
**Goal:** iOS + Android apps

**Tech Options:**
- React Native (share web logic)
- Flutter
- Kotlin Multiplatform (aligns with Goldfinch components)

**Key Features:**
- [ ] Offline-first (complete checklists without internet)
- [ ] Photo capture from device camera
- [ ] Push notifications for new assignments
- [ ] Background sync

**Strategy:** Run autoclaude sessions in background while doing client work

---

## Data Model

```
Business
├── id
├── name
├── subscription_tier
└── created_at

User
├── id
├── business_id
├── role (admin | employee)
├── name
├── email
└── created_at

JobType
├── id
├── business_id
├── name
├── description
└── created_at

ChecklistTemplate
├── id
├── job_type_id
├── name
├── items[] (JSON array of checklist items)
└── created_at

ChecklistItem (within template)
├── order
├── label
├── type (checkbox | text | photo | signature)
├── required (boolean)

ChecklistSubmission
├── id
├── checklist_template_id
├── user_id (employee)
├── job_reference (optional - external job ID)
├── responses[] (JSON - completed items)
├── status (draft | submitted | approved)
├── submitted_at
└── created_at
```

---

## Compute Credit Strategy

**Available:** 1 month of credits
**Priority:** Ship web MVP this month

### Week 1: Foundation
- Set up project structure
- Authentication + user roles
- Basic database schema
- Job type CRUD

### Week 2: Core Features
- Checklist template builder
- Employee checklist view
- Submission flow
- Basic admin dashboard

### Week 3: Polish
- UI/UX improvements
- Error handling
- Mobile-responsive design
- Basic reporting

### Week 4: Buffer + Native Start
- Fix bugs from testing
- Begin native app scaffolding (background)
- Deploy to production

---

## Monetization Potential

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | 1 admin, 3 employees, 5 job types |
| Pro | $29/mo | 5 admins, 25 employees, unlimited job types |
| Business | $99/mo | Unlimited, custom branding, API access |

---

## Agency Value

1. **Demo Asset:** Show clients what we can build
2. **Case Study:** Document build process for content
3. **Revenue:** Potential SaaS income
4. **Client Upsell:** Offer to clients needing job tracking
5. **Component Library:** Extract reusable pieces for Goldfinch

---

## Connection to Client Projects

| Client | How This Helps |
|--------|----------------|
| Plotter Mechanix | Service call checklists for technicians |
| S&S Wolf Sheds | Installation completion verification |
| Maples Apothecary | Inventory check procedures |

---

## Next Action

Start Phase 1 web development using compute credits.

**First Session Goal:**
- Project setup (Next.js + Supabase)
- Authentication working
- Basic job type CRUD

---

**"Ship web MVP this month. Native runs in background with autoclaude."**
