# Platform Sign-Up Instructions

**Purpose:** Step-by-step instructions for each platform so onboarding calls run smoothly.

> "Remove friction on the onboarding call and avoid improvising what they need to sign up for."

---

## How to Use This Document

1. Before the Logistics Onboarding Call, identify which platforms apply to this project
2. Copy the relevant sections into a client-specific document
3. Send to client before the call AND paste in chat during the call
4. Walk through each one together with client screen-sharing

---

## Platform Instructions

### Make.com (Automation Platform)

**Account Type Needed:** Free tier is fine to start

**Steps:**
1. Go to [make.com](https://www.make.com)
2. Click "Get started free" (top right)
3. Enter your work email: `[client email]`
4. Create a password (save it somewhere!)
5. Select region: **US** (or closest to your location)
6. Click "Create account"
7. Verify email if prompted
8. Once logged in, go to **Organization > Teams > Invite**
9. Add: `[your team email]` as Admin

**Access we need:** Admin access to your organization

---

### n8n (Automation Platform - Self-Hosted)

**Note:** We host n8n for you. No signup needed.

**What we need from you:**
- Confirmation of which integrations you want
- API keys for your other platforms (covered separately)

**What you'll receive:**
- Login credentials to your n8n instance
- Direct link to your workflow dashboard

---

### Notion (Project Management)

**If you already have Notion:**
1. Log in to your workspace
2. Go to **Settings & Members > Members**
3. Click "Add members"
4. Enter: `[your team email]`
5. Set permission: **Can edit**

**If you need a new account:**
1. Go to [notion.so](https://www.notion.so)
2. Click "Get Notion free"
3. Sign up with your work email
4. Create a workspace name: `[Client Name]`
5. Invite us using the steps above

**Access we need:** Edit access to the project workspace

---

### Slack (Communication)

**Joining our workspace:**
1. You'll receive an email invite to join `[workspace name]`
2. Click "Join Now" in the email
3. Create your account or sign in with existing Slack
4. You'll be added to: `#[clientname]` (your project channel)

**If you prefer we join YOUR workspace:**
1. Go to your Slack workspace
2. Click **Settings & administration > Invite people**
3. Enter: `[your team email]`
4. We'll join and create a dedicated project channel

---

### Google Workspace (Calendar, Drive, Email)

**Calendar access:**
1. Go to [calendar.google.com](https://calendar.google.com)
2. Find your calendar in the left sidebar
3. Click the three dots > **Settings and sharing**
4. Scroll to "Share with specific people"
5. Click "Add people"
6. Enter: `[your team email]`
7. Set permission: **Make changes to events**

**Drive folder access:**
1. Go to [drive.google.com](https://drive.google.com)
2. Right-click the project folder
3. Select "Share"
4. Enter: `[your team email]`
5. Set permission: **Editor**

---

### GoHighLevel (CRM)

**Adding us as a user:**
1. Log in to your GoHighLevel account
2. Go to **Settings > My Staff**
3. Click "Add Employee"
4. Enter our details:
   - Name: `[Your Name]`
   - Email: `[your team email]`
   - Role: **Admin** (needed for API access)
5. We'll receive an invite and set up our login

**API Key (if needed):**
1. Go to **Settings > Business Profile**
2. Scroll to "API Key"
3. Copy the key and paste in chat (we'll store it securely)

---

### HubSpot (CRM)

**Adding us as a user:**
1. Log in to HubSpot
2. Click the settings gear (top right)
3. Go to **Users & Teams**
4. Click "Create user"
5. Enter: `[your team email]`
6. Set permissions: **Super Admin** (for integration setup)
7. Click "Send invite"

**API Key:**
1. Go to **Settings > Integrations > Private Apps**
2. Click "Create a private app"
3. Name it: `[Project Name] Integration`
4. Select scopes: (we'll guide you on which ones)
5. Create the app and copy the access token

---

### Calendly (Scheduling)

**Adding us to your account:**
1. Log in to [calendly.com](https://calendly.com)
2. Click your profile (top right) > **Admin Center**
3. Go to **Users**
4. Click "Add users"
5. Enter: `[your team email]`
6. Set role: **Admin**

**API Key (for automation):**
1. Go to **Integrations > API & Webhooks**
2. Click "Generate new token"
3. Name it: `[Project Name]`
4. Copy the token and paste in chat

---

### Stripe (Payments)

**Adding us as a team member:**
1. Log in to [dashboard.stripe.com](https://dashboard.stripe.com)
2. Click the gear icon > **Team**
3. Click "Invite"
4. Enter: `[your team email]`
5. Set role: **Developer** (or Admin if needed)
6. Click "Send invite"

**API Keys:**
1. Go to **Developers > API Keys**
2. Copy both:
   - Publishable key: `pk_live_...`
   - Secret key: `sk_live_...` (click "Reveal" first)
3. Paste in chat (we'll store securely)

**Important:** We typically use TEST mode keys first, then switch to live.

---

### Twilio (SMS/Voice)

**Account credentials:**
1. Log in to [twilio.com/console](https://www.twilio.com/console)
2. On the dashboard, you'll see:
   - **Account SID:** `AC...`
   - **Auth Token:** Click to reveal, then copy
3. Paste both in chat

**Phone number:**
1. Go to **Phone Numbers > Manage > Active Numbers**
2. Note your Twilio phone number(s)
3. Share which one(s) should be used for this project

---

### Mailchimp (Email Marketing)

**API Key:**
1. Log in to Mailchimp
2. Click your profile (bottom left) > **Account & Billing**
3. Go to **Extras > API Keys**
4. Click "Create A Key"
5. Name it: `[Project Name]`
6. Copy the key and paste in chat

**Audience ID (for specific lists):**
1. Go to **Audience > All Contacts**
2. Click **Settings > Audience name and defaults**
3. Find "Audience ID" at the bottom
4. Copy and share

---

### ActiveCampaign (Email Marketing)

**API Credentials:**
1. Log in to ActiveCampaign
2. Go to **Settings > Developer**
3. Copy:
   - **URL:** `https://[youraccount].api-us1.com`
   - **Key:** Your API key
4. Paste both in chat

---

### Airtable (Database)

**Adding us to your base:**
1. Open your Airtable base
2. Click "Share" (top right)
3. Click "Invite by email"
4. Enter: `[your team email]`
5. Set permission: **Editor**

**API Key (for automation):**
1. Go to [airtable.com/account](https://airtable.com/account)
2. Under "API", click "Generate API key"
3. Copy the key and paste in chat

**Base ID:**
1. Open your base
2. Go to **Help > API Documentation**
3. The Base ID starts with `app...`
4. Copy and share

---

## Security Notes

- **Never email credentials** - We'll only collect them via screen share or encrypted vault
- **You control access** - You can revoke our access anytime
- **We use encrypted storage** - All credentials go in our password vault
- **Project-end cleanup** - We remove all access 30 days after project completion

---

## Troubleshooting

### "I can't find where to add users"

Share your screen and we'll navigate together - every platform hides it differently!

### "I forgot my password"

Click "Forgot Password" and we'll reset it together on the call.

### "I'm not sure which account to use"

We'll figure it out - start by trying your work email on the login page.

### "I don't have admin access"

Let us know who does - we can coordinate with them directly or have a quick call together.

---

## Custom Platforms

If your project uses platforms not listed here, we'll create custom instructions before the call. Just let us know what tools you use!
