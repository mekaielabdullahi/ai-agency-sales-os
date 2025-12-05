# ARISEGROUP WEBSITE - Complete Functional System

**Tech Stack:** Next.js 14 + React + TypeScript + Tailwind CSS
**Database:** PostgreSQL (via Supabase) or MongoDB
**CRM Integration:** Notion API
**Calendar:** Calendly embed + webhook
**Email:** SendGrid or Resend
**Analytics:** Google Analytics 4 + Plausible
**Hosting:** Vercel (recommended) or AWS

---

## SITE STRUCTURE

```
/                           → Homepage
/about                      → Team & Story
/verticals                  → All 4 verticals overview
  /defense                  → Defense vertical page (Mekaiel)
  /industrial               → Industrial vertical page (4.0 Hero)
  /ecommerce                → E-commerce vertical page (Matthew)
  /construction             → Construction vertical page (Chris)
/case-studies               → Client success stories (empty initially)
/insights                   → Blog/thought leadership
/contact                    → Contact form + calendar booking
/book-discovery             → Direct booking page
/thank-you                  → Post-submission confirmation
/api                        → Backend API routes
  /contact                  → Contact form handler
  /book-call                → Booking handler
  /newsletter               → Email capture
  /notion-sync              → Sync leads to Notion CRM
```

---

## FUNCTIONAL COMPONENTS

### 1. Contact Form
- Captures: Name, Email, Company, Vertical, Message
- Validates input
- Sends to Notion CRM
- Sends confirmation email
- Redirects to /thank-you

### 2. Discovery Call Booking Widget
- Calendly embed for each founder
- Routes based on vertical selection
- Captures pre-call info (Q1-Q5 prep)
- Syncs to Notion automatically

### 3. Email Capture (Newsletter)
- Inline CTAs throughout site
- Exit intent popup
- Syncs to email service + Notion

### 4. Lead Routing System
- Auto-assigns leads to correct founder based on vertical
- Slack notification to #pipeline channel
- Email notification to assigned founder

### 5. Analytics & Tracking
- Page views
- Form submissions
- Booking conversions
- Traffic sources

---

## INTEGRATIONS

### Notion CRM (Primary)
- New leads create Notion database entry
- Fields: Name, Email, Company, Vertical, Source, Status, Assigned To, Date
- API webhook on form submit

### Calendly (Booking)
- 4 separate calendars (one per founder)
- Webhook sends booking data to Notion
- Pre-call questionnaire embedded

### SendGrid/Resend (Email)
- Confirmation emails
- Founder notifications
- Newsletter automation

### Slack (Team Notifications)
- #pipeline channel: New leads
- #wins channel: Bookings confirmed
- #website channel: Form errors/issues

---

## DEPLOYMENT

**Environment Variables Needed:**
```
NEXT_PUBLIC_SITE_URL=https://arisegroup.ai
NOTION_API_KEY=secret_xxx
NOTION_DATABASE_ID=xxx
SENDGRID_API_KEY=xxx
CALENDLY_API_KEY=xxx
SLACK_WEBHOOK_URL=xxx
GA_TRACKING_ID=G-xxx
```

**Deploy to Vercel:**
```bash
npm install
npm run build
vercel deploy
```

---

## FILES IN THIS PROJECT

- `package.json` - Dependencies
- `next.config.js` - Next.js configuration
- `tailwind.config.js` - Tailwind CSS config
- `/src/pages/` - All website pages
- `/src/components/` - Reusable components
- `/src/api/` - Backend API routes
- `/src/lib/` - Utility functions (Notion, email, etc.)
- `/src/content/` - Page content and copy
- `/public/` - Static assets

---

## GETTING STARTED

```bash
cd arisegroup-website
npm install
npm run dev
# Opens on http://localhost:3000
```

---

**Built for AriseGroup by Mekaiel | December 4, 2025**
