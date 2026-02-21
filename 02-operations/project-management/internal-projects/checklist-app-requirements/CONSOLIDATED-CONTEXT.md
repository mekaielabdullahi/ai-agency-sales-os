# Checklist App - Consolidated Context

**Created:** 2025-12-31
**Status:** Requirements Gathering

---

## Overview

A checklist app needed by multiple clients and internal use. Every deliverable needs a checklist, especially for:
- Testing and validation
- Environment separation
- Metrics dashboard
- Logs
- System visibility post-deployment

---

## Client Use Cases

### 1. Plotter Mechanix
**Reference:** `active-projects/plotter-mechanix/`

**Needs:**
- Service call checklists for technicians
- Job completion verification
- Testing protocol for Quo-Jobber integration
- Week 1 testing checklist (already documented - see `deliverables/week-1-testing-checklist.md`)

**Key Requirements:**
- 10 critical questions framework
- Go/No-Go decision matrix
- Pre-testing setup
- Post-testing actions
- Sign-off workflow

---

### 2. S&S Wolf Sheds
**Reference:** `active-projects/ss-wolf-sheds/`

**Needs:**
- QR/Slot system verification (20 fixed QR codes per lot)
- Website intake form testing
- Lead-to-building tracking validation
- Installation completion verification
- Basic scan analytics testing

**MVP Scope:**
1. QR code system works
2. Intake form captures leads correctly
3. Attendant notifications working
4. Lead tracking accurate
5. Analytics recording properly

---

### 3. Internal Agency Use
**Reference:** Every deliverable

**Needs:**
- Every deliverable = checklist approach
- Standardized testing protocols
- Environment separation verification (dev/staging/prod)
- Metrics dashboard checks
- Logs visibility confirmation
- System visibility post-deployment

---

## Common Checklist Components

### Testing & Validation
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] End-to-end tests passing
- [ ] Manual testing complete
- [ ] Edge cases documented and tested
- [ ] Error handling verified

### Environment Separation
- [ ] Development environment isolated
- [ ] Staging environment configured
- [ ] Production environment ready
- [ ] Environment variables properly set
- [ ] No dev credentials in production
- [ ] Database migrations tested on staging first

### Metrics Dashboard
- [ ] Key metrics defined
- [ ] Dashboard configured
- [ ] Data flowing correctly
- [ ] Alerts configured
- [ ] Thresholds set appropriately
- [ ] Historical data retention configured

### Logs & Visibility
- [ ] Logging implemented at key points
- [ ] Log levels appropriate (debug, info, error)
- [ ] Log retention configured
- [ ] Log search/filter working
- [ ] Error alerts connected
- [ ] Audit trail maintained

### Post-Deployment Visibility
- [ ] Health checks active
- [ ] Uptime monitoring configured
- [ ] Performance metrics tracked
- [ ] Error rates monitored
- [ ] User activity visible
- [ ] System status dashboard accessible

---

## Goldfinch Job Checklist App

**Reference:** `active-projects/goldfinch/apps/job-checklist-app/`

**Status:** Top of Goldfinch roadmap (P0)

### Features Needed
1. **Business Admin Portal (Web)**
   - Create/edit job types
   - Create checklists per job type
   - Assign employees to job types
   - View completion reports
   - Export data

2. **Employee Interface (Web → Native)**
   - View assigned jobs
   - Complete checklists (checkboxes, photos, signatures, notes)
   - Submit completed checklists
   - Offline support

3. **Backend**
   - User authentication
   - Multi-tenant data isolation
   - Checklist submission storage
   - Audit trail

### Development Phases
- **Phase 1:** Web MVP (use compute credits now)
- **Phase 2:** Production hardening
- **Phase 3:** Native mobile (autoclaude background)

### Tech Stack (Proposed)
- Frontend: Next.js
- Backend: Supabase
- Hosting: Vercel

---

## Connection Matrix

| Client | Checklist Need | Priority |
|--------|---------------|----------|
| Plotter Mechanix | Service call verification | HIGH |
| S&S Wolf Sheds | Installation verification | HIGH |
| Maples Apothecary | Inventory procedures | MEDIUM |
| Internal Agency | Every deliverable | HIGH |

---

## Auto Claude Metrics & Productionizing Work

**Goal:** Get Auto Claude working on:
1. Metrics tracking automation
2. Productionizing the checklist system
3. Background development of mobile app

**Strategy:**
- Run autoclaude sessions in background
- Use monthly compute credits efficiently
- Ship web MVP this month
- Native runs in background

---

## Next Steps

1. [ ] Review existing Plotter Mechanix testing checklist
2. [ ] Define S&S Wolf Sheds MVP checklist
3. [ ] Create internal agency deliverable checklist template
4. [ ] Set up Auto Claude for background development
5. [ ] Start Phase 1 web development

---

## Resources

- Goldfinch Implementation Plan: `active-projects/goldfinch/apps/job-checklist-app/IMPLEMENTATION-PLAN.md`
- Plotter Mechanix Testing: `active-projects/plotter-mechanix/deliverables/week-1-testing-checklist.md`
- S&S Wolf Sheds Audit: `active-projects/ss-wolf-sheds/audit/`

---
