# Onboarding Playbook for Automation Clients

> Source: [Nick's Onboarding Framework](https://www.youtube.com/watch?v=hRBL6ISvB3s)

## Core Purpose of Onboarding

- Onboarding is a **leverage** tool to:
  - Minimize buyer remorse right after payment.
  - Set clear, realistic client expectations.
  - Front-load logistical headaches (credentials, platforms, access) so they do not drag projects out.
- Good onboarding turns a small first project (1-3K) into a long-term 5K/month+ client by improving retention and upsell potential.

---

## Three Problems Onboarding Must Solve

### 1. Buyer Remorse

- Any time a client sends money, doubt appears: "Did I choose the right provider / solution?"
- Onboarding should rapidly convert remorse into gratitude and excitement to start.

Key mechanisms:
- Immediate evidence of professionalism (receipts, emails).
- Clear next steps within minutes.
- Visible movement on their project so they feel progress, not silence.

### 2. Client Expectations

- Automation has extreme scope-creep risk because there are "5 million sub-services" (scoping, flow-charting, scenarios, APIs, CRMs, etc.).
- Sales incentives push you to oversell; delivery incentives push you to simplify and narrow scope. Onboarding is where you reconcile this tension.

Goals:
- Define exactly how you will communicate.
- Define how long things will take and what happens when.
- Define what "done" looks like (win condition) so you are not trapped in endless revisions.

### 3. Logistics

- Automation = juggling many tools and accounts: CRMs, email tools, Make/Zapier, 2FA, subscription tiers, sub-accounts, passwords, etc.
- If you do not front-load this, you end up in a "cat and mouse" game of chasing codes, logins, and permissions over weeks.

Goal:
- Minimize friction and get all required access within the first day so you never have to chase basic credentials mid-project.

---

## Solutions Overview

Nick's process solves the three problems with six concrete levers: three for remorse and three for expectations/logistics.

### Buyer Remorse: Three Levers

1. **Transactional Alerts (Receipt)**
   - Client should receive a proper receipt within ~30 seconds of payment.
   - Configure your payment processor (e.g., Stripe -> Settings -> Customer emails -> Successful payments) to send branded receipts automatically.
   - Make sure receipts are on-brand (logo, colors) and feel high-quality and professional.

2. **Gratitude Email**

   Purpose:
   - Express sincere thanks for their trust, time, and money.
   - Signal that a real human cares about the relationship.
   - Increase perceived professionalism and long-term ROI from that client.

   Characteristics:
   - Short, friendly, text-like tone (not a corporate sequence).
   - Sent within minutes of payment (often automated off a payment webhook).

   Example structure (Nick's pattern):
   - "Hey [Name], thanks for taking care of that invoice so promptly."
   - "I'm really excited that we get to work together and to nail this for you."
   - "I'll send onboarding instructions + a calendar link in a moment so we can book a kickoff call."
   - "Appreciate your business."

3. **Perception of Progress / Next Steps Email**

   Purpose:
   - Within ~5 minutes of payment, the client should see exactly what happens next.
   - They should feel "things are already moving" instead of wondering if you disappeared.

   Content:
   - Clear next steps you are taking.
   - What they need to do (if anything) before the onboarding call.
   - Link to a booking calendar for the onboarding call.

   Implementation pattern:
   - Payment event (e.g., Stripe) triggers:
     - Receipt (processor-native).
     - Thank-you email.
     - A slightly delayed next-steps email (e.g., via Make.com with 4-5 minute delay).

   Result:
   - Within a short window, client gets 3-4 emails: receipt, gratitude, next steps.
   - This creates a strong impression of organization and experience.

---

## System Design: Automating the Early Emails

### High-Level Automation Flow

- Trigger: Payment or "new deal won" event (via payment processor or CRM).
- Step 1: Fetch client details (name, email) from CRM or event payload.
- Step 2: Send gratitude email.
- Step 3: Sleep/delay a few minutes.
- Step 4: Send onboarding / next-steps email with:
  - Simple explanation of what happens now.
  - Calendar link to book onboarding call.
  - Optional attached or linked onboarding instructions.

Nick's demo stack:
- Uses Make.com:
  - Webhook or "Watch events" module (e.g., Stripe "payment_intent" events).
  - Variables (name, email) pulled or mocked from CRM.
  - Gmail module to send emails (HTML with `<br>` for line breaks and `<a>` tags for links).
  - Sleep modules to stagger messages so they feel hand-written.

Key principle:
- The copy should sound casual and human, even though it is automated.

---

## Managing Client Expectations

### 1. Defining Communication Style and Frequency

Why:
- Most agencies never explicitly decide "how we communicate," which causes anxiety and random pings.

What to define:
- **Channel:** Slack, email, Teams, etc. (choose what is sustainable for you and acceptable for them).
- **Availability:** For example:
  - "I'm available on Slack from 12-2 pm PT weekdays; you can expect responses within 10-15 minutes during that window."
- **Update cadence:** For example:
  - 1-2 progress updates per week (e.g., Tuesdays and Fridays EOD).

Insights from Nick:
- Once-per-week updates were sometimes too sparse; clients felt out of the loop even if they were told the schedule.
- Moving to twice-per-week updates plus defined Slack availability dramatically reduced issues.
- You do not need the theoretically "perfect" cadence; simply stating and keeping your promise beats most competitors.

### 2. Setting the Timeline

Problems:
- Most service timelines are optimistically wrong and projects end up late.
- Many automation tasks can be done in hours, but they get padded or scheduled poorly.

Approach:
- Break project into phases (e.g., prompt engineering, scenario building, testing/delivery) with date ranges.
- Choose a **reasonably generous** schedule you can beat, not an aggressive one you will miss.

Example pattern:
- Prompt design: July 19-22.
- Scenario building in Make.com: July 23-26.
- Testing and delivery: July 27-30.

Execution:
- Tell the client this plan during onboarding.
- Then deliver early (e.g., deliver on July 27 instead of July 30) and explicitly frame it as "ahead of schedule."

Effect:
- Over-delivery on time builds trust and opens the door for more work.

### 3. Defining the Win Condition ("Done")

Problem:
- If you never define what "done" is, your definition and the client's definition diverge.
- This leads to scope creep and "just one more thing" cycles after you think you've finished.

Solution:
- Explicitly describe, in concrete terms, the state of the system at project completion.

Example for a lead gen automation:
- By July 30:
  - An Airtable that automatically populates with positive replies from Smartlead campaigns.
  - Campaign sending Monday-Friday, 7 am-7 pm, using your best-in-class copy formula.
  - Slack notifications on each positive response.
  - An SOP sheet for managing responses or training an outreach manager.
  - A walkthrough video showing the system end-to-end.

Rule:
- If every item is checked, the project is done.
- If not, your side is incomplete.

Result:
- Less scope creep, fewer revision loops, and clearer handoff to potential retainers.

---

## Logistics and Access Management

### 1. Itemizing Platforms

Purpose:
- Remove friction on the onboarding call and avoid improvising what they need to sign up for.

Steps:
- Beforehand, list every platform the client needs for this project:
  - Automation layer (e.g., Make.com).
  - CRM.
  - Email tools.
  - Any third-party connectors, schedulers, etc.
- For each platform, write simple, step-by-step sign-up instructions:
  - Example: "Go to make.com; click Sign up; use this email; select region US; click Register."

Delivery:
- Send these instructions with the onboarding email or as a PDF/Doc and also paste into Zoom/Meet chat at the start of the call.

Impact:
- The client perceives you as organized and experienced.
- The onboarding call becomes execution, not confusion.

### 2. Onboarding Call as Logistics Engine

Purpose:
- Do not "automate away" the highest-leverage human moment.
- Use the call to:
  - Handle 2FA live.
  - Recover forgotten passwords.
  - Set expectations verbally.
  - Transfer all necessary access in ~15-20 minutes.

Why not just forms:
- Two-factor codes expire quickly and are hard to coordinate asynchronously.
- Many clients are not comfortable with or good at handling technical steps alone.
- Being there live lets them feel more in control and safer with their data.

Psychological benefit:
- They feel secure because they are not emailing plain-text passwords around.
- You get credit for "guiding them through the scary tech," not just building automations.

### 3. Secure / Structured Credential Handling

Challenges:
- OAuth, 2FA, and security flows are the "bane" of automation engineers.

Onboarding call advantages:
- You can say:
  - "You'll get a code by text right now; just read it to me and we'll be done."
  - "Share your screen; click here, then here, then reset your password."
- You clear multiple edge cases (forgotten logins, locked accounts, strange security flows) in one session.

Outcome:
- By the end of the call, you should have:
  - Access to every necessary account.
  - All 2FA steps completed at least once.
  - The client feeling safe and confident.

---

## Onboarding Call SOP (Structure)

Nick's template flow for the call:

1. **Open with gratitude**
   - Thank them for joining and for choosing to work with you.

2. **Explain why onboarding matters**
   - Logistics (2FA, passwords, platforms) are the #1 cause of delays and frustration in automation projects.
   - This call front-loads all of that so the project can move smoothly.

3. **Outline the call roadmap**
   - First: Cover timelines and communication expectations.
   - Second: Sign up for and configure all listed platforms.
   - Third: Handle any 2FA flows live.
   - Fourth: Quick Q&A.

4. **Execute from top to bottom**
   - Walk through your prepared platform list with the client screen-sharing.
   - Use live codes and flows to finalize access.
   - Confirm they understand the schedule and win condition before ending.

Notes:
- You do not need a big team on these calls; solo is enough.
- Avoid bringing the whole company onto the call just to "look big" -- it is overkill.

---

## Business Impact of Strong Onboarding

- Consistent onboarding dramatically increases:
  - Client retention rate.
  - Average revenue per client (small one-offs converting into retainers).
  - Referral volume (clients talk about how easy and professional the process felt).
- The upfront work is modest (maybe an hour to think through processes and 5 minutes to build core automations), but returns can be "thousands to tens of thousands" over 12 months.
- Automation is the multiplier: once the flow is built, each new client experiences a high-end onboarding with almost no additional manual effort.
