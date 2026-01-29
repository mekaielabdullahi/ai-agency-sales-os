# Goldfinch Component Roadmap

**Philosophy:** Build general-purpose, reusable components that accelerate future mobile development for any client.

---

## P0-URGENT: Job Checklist App (NEW - Dec 2025)

**Status:** TOP PRIORITY - Use monthly compute credits
**Plan:** [apps/job-checklist-app/IMPLEMENTATION-PLAN.md](apps/job-checklist-app/IMPLEMENTATION-PLAN.md)

### What
Web app (then native) for businesses to assign checklists to employees per job type.

### Why This First
1. **Compute credits available** - 1 month to use efficiently
2. **Agency demo asset** - Show clients what we can build
3. **Revenue potential** - SaaS product
4. **Client alignment** - Plotter, S&S, Maples could all use this

### Development Strategy
| Phase | Platform | Approach |
|-------|----------|----------|
| Phase 1 | Web | Active development with compute credits |
| Phase 2 | Web | Production hardening |
| Phase 3 | iOS/Android | Background with autoclaude |

### This Month's Goal
**Ship web MVP:** Admin creates checklists per job type → Employees complete them → Data stored in backend

---

## Priority Framework

| Priority | Criteria |
|----------|----------|
| **P0** | Universal - needed in almost any app |
| **P1** | Common - needed in most business apps |
| **P2** | Specialized - needed for specific use cases |

---

## P0: Universal Components (Build First)

### 1. Chat Widget
**What:** Embeddable chat interface for any application
**Why Universal:** Every app eventually needs user interaction/support
**Features:**
- [ ] Message list with bubbles (user/assistant)
- [ ] Text input with send button
- [ ] Typing indicators
- [ ] Message timestamps
- [ ] Scroll behavior (auto-scroll to bottom)
- [ ] Customizable theming (colors, fonts)
- [ ] Backend-agnostic (works with any API)

**Reusability:** Can be embedded in any app for customer support, AI assistant, team chat

---

### 2. Voice/Audio Streaming
**What:** Real-time audio capture and streaming to backend
**Why Universal:** Voice interaction is becoming standard in business apps
**Features:**
- [ ] Microphone permission handling
- [ ] Audio capture and buffering
- [ ] WebSocket streaming to backend
- [ ] Visual feedback (waveform, recording indicator)
- [ ] Start/stop/pause controls
- [ ] Background audio handling

**Reusability:** Voice commands, meeting transcription, voice notes, AI voice agents

---

### 3. Authentication Module
**What:** Standard auth flows (login, signup, password reset)
**Why Universal:** Every app needs user authentication
**Features:**
- [ ] Login screen
- [ ] Signup screen
- [ ] Password reset flow
- [ ] OAuth support (Google, Apple)
- [ ] Token storage and refresh
- [ ] Session management

**Reusability:** Drop-in auth for any client app

---

## P1: Common Business Components (Build Second)

### 4. Dashboard Framework
**What:** Configurable dashboard with cards/widgets
**Why Common:** Most business apps need a home screen with key metrics
**Features:**
- [ ] Card-based layout system
- [ ] Metric display widgets (numbers, percentages)
- [ ] Chart components (line, bar, pie)
- [ ] List widgets (recent items, notifications)
- [ ] Pull-to-refresh
- [ ] Loading states and skeletons

**Reusability:** Home screen for any business app

---

### 5. Form Builder
**What:** Dynamic form rendering and validation
**Why Common:** Data collection is core to business apps
**Features:**
- [ ] Text inputs, dropdowns, checkboxes
- [ ] Date/time pickers
- [ ] File/image upload
- [ ] Form validation rules
- [ ] Error display
- [ ] Submit handling

**Reusability:** Any data entry screen (quotes, intake, settings)

---

### 6. Notification System
**What:** Push notifications + in-app notification center
**Why Common:** User engagement and alerts
**Features:**
- [ ] Push notification handling
- [ ] In-app notification list
- [ ] Read/unread states
- [ ] Deep linking from notifications
- [ ] Notification preferences

**Reusability:** Any app needing user alerts

---

### 7. Offline-First Data Layer
**What:** Local storage with sync to backend
**Why Common:** Field workers often have poor connectivity
**Features:**
- [ ] Local database (SQLite/Room)
- [ ] Background sync
- [ ] Conflict resolution
- [ ] Sync status indicators
- [ ] Retry logic

**Reusability:** Any app used in the field

---

## P2: Specialized Components (Build As Needed)

### 8. Document Scanner
**What:** Camera-based document capture and OCR
**Use Cases:** Receipt capture, invoice scanning, ID verification

### 9. Location Services
**What:** GPS tracking, geofencing, map display
**Use Cases:** Field service, delivery tracking, territory management

### 10. Barcode/QR Scanner
**What:** Camera-based code scanning
**Use Cases:** Inventory, asset tracking, check-in systems

### 11. Calendar/Scheduling
**What:** Event display, booking, availability
**Use Cases:** Appointments, resource scheduling

### 12. Media Capture
**What:** Photo/video capture with annotation
**Use Cases:** Site documentation, before/after photos

---

## Current Focus: Chat Voice Agent Widget

**Why This First:**
1. Combines Chat Widget (#1) + Voice Streaming (#2)
2. Highest impact component
3. Enables AI assistant in any app
4. Foundation for client projects needing AI interaction

**Implementation Order:**
1. Basic chat UI (messages, input)
2. Voice recording button
3. Audio streaming to backend
4. Response handling (text + audio playback)
5. Theming and customization

---

## Build Log

| Date | Component | Progress | Hours |
|------|-----------|----------|-------|
| 2025-12-17 | Chat Voice Widget | Starting | - |

---

## Notes

- All components built with Kotlin Multiplatform for Android (iOS later)
- Focus on clean APIs that are easy to integrate
- Each component should be standalone and composable
- Document integration examples for each component

---

**Created:** 2025-12-17
**Last Updated:** 2025-12-17
