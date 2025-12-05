# ARISEGROUP WEBSITE - DEPLOYMENT GUIDE

## STEP 1: SETUP INTEGRATIONS

### 1.1 Notion CRM Setup

**Create Notion Database:**

1. Go to Notion.so
2. Create new database called "AriseGroup CRM"
3. Add these columns:
   - `Contact` (Title)
   - `Email` (Email)
   - `Company` (Text)
   - `Vertical` (Select: Defense, Industrial, E-commerce, Construction, Other)
   - `Status` (Select: Outreach, Discovery, Proposal, Negotiation, Closed-Won, Closed-Lost)
   - `Source` (Select: website-contact, website-booking, newsletter)
   - `Assigned To` (Select: Mekaiel, 4.0 Hero, Matthew, Chris)
   - `Q1` (Text - Long)
   - `Q2` (Text - Long)
   - `Q3` (Text - Long)
   - `Q4` (Text - Long)
   - `Q5` (Text - Long)
   - `Phone` (Phone)
   - `Call Date` (Date)
   - `Deal Size` (Number)
   - `Notes` (Text - Long)

4. Get API credentials:
   - Go to https://www.notion.so/my-integrations
   - Click "+ New integration"
   - Name it "AriseGroup Website"
   - Copy the `Internal Integration Token` → This is your `NOTION_API_KEY`

5. Get Database ID:
   - Open your database in Notion
   - Click "Share" → "Copy link"
   - URL format: `https://notion.so/{workspace}/{DATABASE_ID}?v=...`
   - Extract the `DATABASE_ID` (32-character string)

6. Give integration access:
   - In your database, click "•••" → "Add connections"
   - Select "AriseGroup Website" integration

---

### 1.2 SendGrid Email Setup

1. Go to https://sendgrid.com/
2. Sign up for free account (100 emails/day free)
3. **Verify sender email:**
   - Settings → Sender Authentication
   - Verify `hello@arisegroup.ai` (or your domain)
4. **Create API key:**
   - Settings → API Keys
   - Create key with "Full Access"
   - Copy key → This is your `SENDGRID_API_KEY`

**Alternative: Use Resend**
- Simpler setup, better dev experience
- Go to https://resend.com/
- Get API key
- Update `src/lib/email.ts` to use Resend instead of SendGrid

---

### 1.3 Calendly Setup

1. Each founder creates Calendly account:
   - Go to https://calendly.com/
   - Create 15-minute "Discovery Call" event
   - Add pre-call questions:
     - "What industry/vertical are you in?"
     - "What's your company name?"
     - "What do you do (in 1-2 sentences)?"

2. Get Calendly URLs:
   - Each founder: Share event → Copy link
   - Add to `.env.local`:
     ```
     CALENDLY_URL_DEFENSE=https://calendly.com/mekaiel-arisegroup/discovery
     CALENDLY_URL_INDUSTRIAL=https://calendly.com/40hero-arisegroup/discovery
     ...
     ```

3. Set up webhook (optional but recommended):
   - Calendly → Integrations → Webhooks
   - Add webhook URL: `https://arisegroup.ai/api/calendly-webhook`
   - Select event: `invitee.created`
   - This auto-syncs bookings to Notion

---

### 1.4 Slack Notifications Setup

1. Create Slack channels:
   - `#pipeline` - New leads
   - `#wins` - Bookings/closes
   - `#website` - Website errors

2. Create webhook for each channel:
   - Channel → Integrations → Add app → "Incoming Webhooks"
   - Create webhook → Copy URL
   - Add to `.env.local`:
     ```
     SLACK_WEBHOOK_PIPELINE=https://hooks.slack.com/services/xxx
     SLACK_WEBHOOK_WINS=https://hooks.slack.com/services/xxx
     SLACK_WEBHOOK_WEBSITE=https://hooks.slack.com/services/xxx
     ```

---

## STEP 2: LOCAL DEVELOPMENT

```bash
# Clone and install
cd arisegroup-website
npm install

# Copy environment variables
cp .env.example .env.local
# Fill in your actual keys in .env.local

# Run development server
npm run dev
# Opens on http://localhost:3000

# Test integrations:
# 1. Submit contact form → Check Notion + Email + Slack
# 2. Book discovery call → Check Notion + Slack
# 3. Sign up for newsletter → Check Email
```

---

## STEP 3: DEPLOY TO VERCEL

### 3.1 Connect Repository

1. Push code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial AriseGroup website"
   git remote add origin https://github.com/arisegroup/website.git
   git push -u origin main
   ```

2. Go to https://vercel.com/
3. Sign in with GitHub
4. Click "Add New Project"
5. Import your repository

### 3.2 Configure Environment Variables

In Vercel dashboard:
- Settings → Environment Variables
- Add ALL variables from `.env.local`
- **IMPORTANT:** Mark sensitive keys (API keys) as "Secret"

### 3.3 Deploy

- Click "Deploy"
- Wait 2-3 minutes
- Vercel gives you URL: `https://arisegroup-website.vercel.app`

### 3.4 Add Custom Domain

1. Buy domain: `arisegroup.ai` (Namecheap, Google Domains, etc.)
2. In Vercel:
   - Settings → Domains
   - Add `arisegroup.ai` and `www.arisegroup.ai`
3. Update DNS records (in your domain registrar):
   ```
   A record: @ → 76.76.21.21
   CNAME: www → cname.vercel-dns.com
   ```
4. Wait 5-60 minutes for DNS propagation

---

## STEP 4: POST-DEPLOYMENT CHECKS

### 4.1 Test All Forms

- [ ] Contact form submits successfully
- [ ] Lead appears in Notion CRM
- [ ] Confirmation email received
- [ ] Founder notification email received
- [ ] Slack notification in #pipeline

### 4.2 Test Booking Flow

- [ ] Select vertical
- [ ] Calendly widget loads
- [ ] Book fake test call
- [ ] Booking appears in Notion (if webhook configured)
- [ ] Slack notification in #wins

### 4.3 Test Newsletter

- [ ] Newsletter form submits
- [ ] Welcome email received
- [ ] Subscriber added to Notion (optional)

### 4.4 Check Analytics

- [ ] Google Analytics tracking code fires
- [ ] Page views showing up in GA dashboard

---

## STEP 5: ONGOING MAINTENANCE

### Monitor Form Submissions

**Daily:**
- Check Notion CRM for new leads
- Respond to inquiries within 24 hours
- Update lead status as you progress

**Weekly:**
- Review in team sync (Friday 6pm)
- Track conversion rates (form → discovery → proposal → close)
- Identify drop-off points

### Update Content

**When to update:**
- New case study → Add to `/case-studies`
- New insight → Add to `/insights` blog
- Pricing changes → Update `src/content/homepage.ts`
- New vertical → Add to verticals section

**How to update:**
1. Edit files locally
2. Commit and push to GitHub
3. Vercel auto-deploys in ~2 minutes

---

## TROUBLESHOOTING

### Forms not submitting

**Check:**
1. Browser console for errors
2. Network tab → API call status
3. Vercel logs (Dashboard → Functions → Logs)
4. Environment variables are set correctly

### Notion sync failing

**Check:**
1. `NOTION_API_KEY` is correct
2. `NOTION_DATABASE_ID` is correct
3. Integration has access to database (Share → Connections)
4. Database columns match exactly (case-sensitive)

### Emails not sending

**Check:**
1. `SENDGRID_API_KEY` is correct
2. Sender email is verified in SendGrid
3. Check Sendgrid dashboard → Activity for error logs
4. Check spam folder

### Calendly webhook not working

**Check:**
1. Webhook URL is correct: `https://arisegroup.ai/api/calendly-webhook`
2. Webhook is active in Calendly dashboard
3. Check Vercel logs for incoming webhook requests

---

## PERFORMANCE OPTIMIZATION

### After 100+ form submissions:

1. **Add database indexing** (if using PostgreSQL instead of Notion)
2. **Implement rate limiting** on API routes (prevent spam)
3. **Add Redis caching** for frequently accessed data
4. **Enable ISR** (Incremental Static Regeneration) for blog posts

### After 10K+ monthly visitors:

1. **Implement CDN** for images (Cloudinary, Imgix)
2. **Add edge caching** with Vercel Edge Functions
3. **Optimize images** with next/image
4. **Lazy load** heavy components

---

## SECURITY CHECKLIST

- [ ] All API keys are in environment variables (not in code)
- [ ] `.env.local` is in `.gitignore` (never commit secrets)
- [ ] CORS is configured properly (only allow your domain)
- [ ] Rate limiting on API routes (prevent abuse)
- [ ] Input validation on all forms (prevent XSS/injection)
- [ ] HTTPS enabled (automatic with Vercel)
- [ ] CSP headers configured (Content Security Policy)

---

## SUPPORT

**If stuck:**
- Check Vercel logs first (most errors show here)
- Check Notion API docs: https://developers.notion.com/
- Check SendGrid docs: https://docs.sendgrid.com/
- Ask in AriseGroup Slack #website channel

**Emergency contact:**
- Email: mekaiel@arisegroup.ai
- Slack: @mekaiel

---

**Website is ready to launch!**

Next steps:
1. Complete Step 1 (Setup Integrations)
2. Test locally (Step 2)
3. Deploy to Vercel (Step 3)
4. Test live site (Step 4)
5. Monitor and iterate (Step 5)

Go time: Monday, December 2, 2025 🚀
