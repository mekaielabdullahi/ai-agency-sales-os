# Christmas Lights Voice Agent - Project Brief

**Project Start:** December 11, 2025
**Go-Live Target:** December 12, 2025
**Purpose:** Handle intake calls for Christmas light installation service
**Secondary Value:** Reusable for ALL future projects

---

## 🎯 PROJECT OBJECTIVES

### Primary Goal:
Create voice agent that handles Christmas light installation inquiries, collects customer info, and alerts me when to take over the call.

### Business Impact:
- Handle 5x more inquiries while doing data annotation
- Same-day cash flow ($200-600 per job)
- Reusable infrastructure for all services
- Professional presence without constant availability

---

## 📞 VOICE AGENT REQUIREMENTS

### Core Features:
1. **Answer calls professionally** using my cloned voice
2. **Collect customer information:**
   - Name and address
   - House size (single/two story)
   - Linear feet estimate
   - Desired installation date
   - Budget range
3. **Quote price ranges** based on house size
4. **Schedule installation time**
5. **Alert me** when human takeover needed
6. **Record and transcribe** all calls

### Voice Script Flow:
```
"Hi, this is Matthew with Christmas Light Installation.
Thanks for calling! I can help you get a quote for
professional Christmas light installation.

First, can I get your name and the address where
you'd like the lights installed?

[Collect info]

Is this a single story or two story home?

[Based on answer, provide price range]

We typically charge $200-300 for single story homes
and $400-500 for two story, depending on the linear
footage.

When were you hoping to have the installation done?

[Check availability]

Great! I can schedule you for [date/time]. We require
payment on completion - cash, Venmo, or Zelle.

[If complex or questions]
Let me connect you with Matthew directly to discuss
the details...
[Alert me to take over]
```

---

## 🛠 TECHNICAL STACK

### Option A: Vapi.ai Stack (Recommended)
- **Phone:** Twilio number ($1/mo + usage)
- **Voice:** ElevenLabs (my voice clone) ($22/mo)
- **Agent:** Vapi.ai ($49/mo starter)
- **Alerts:** SMS via Twilio
- **Recording:** Built-in with transcription
- **Total:** ~$75/month

### Option B: Bland.ai Stack
- **Phone:** Bland provides number
- **Voice:** Bland's voice clone
- **Agent:** Bland.ai ($100/mo)
- **Alerts:** Built-in
- **Recording:** Built-in
- **Total:** ~$100/month

### Option C: DIY Stack (Complex but cheap)
- **Phone:** Google Voice (free) or Twilio
- **Voice:** ElevenLabs
- **Agent:** Custom with OpenAI
- **Framework:** FastAPI + Twilio
- **Total:** ~$25/month + development time

---

## 📋 IMPLEMENTATION PLAN

### Day 1 (Dec 11) - Setup:
**Morning (after 8hr data annotation):**
1. [ ] Set up Twilio account and phone number
2. [ ] Create ElevenLabs account and clone voice (30 min recording)
3. [ ] Set up Vapi.ai account
4. [ ] Create basic agent with intake script

**Afternoon:**
5. [ ] Test agent with personal phone
6. [ ] Set up SMS alerts for takeover
7. [ ] Configure recording and transcription
8. [ ] Create simple tracking spreadsheet

### Day 2 (Dec 12) - Launch:
**Morning (after data annotation):**
1. [ ] Final testing with friends/family
2. [ ] Create Craigslist ad with new number
3. [ ] Post on Nextdoor
4. [ ] Post in local Facebook groups
5. [ ] Print 50 door hangers with QR code

**Afternoon:**
6. [ ] Distribute door hangers in target neighborhoods
7. [ ] Monitor first calls
8. [ ] Adjust script based on feedback
9. [ ] Book first installations

---

## 💰 REVENUE MODEL

### Pricing Structure:
| Service Level | Price | Time | Profit |
|--------------|-------|------|--------|
| Basic (single story, <100 ft) | $200-250 | 1.5 hrs | $150/hr |
| Standard (single, 100-200 ft) | $300-350 | 2 hrs | $150/hr |
| Premium (two story, <150 ft) | $400-450 | 2.5 hrs | $160/hr |
| Deluxe (two story, 150+ ft) | $500-600 | 3 hrs | $180/hr |

### Materials:
- Customer provides lights OR
- We provide at 2x retail markup
- Basic 100ft set: $30 cost → $60 charge

### Payment:
- Same day cash preferred
- Venmo/Zelle accepted
- No checks, no "bill me later"

---

## 📢 MARKETING MESSAGES

### Craigslist Post:
```
LAST MINUTE CHRISTMAS LIGHT INSTALLATION - Professional Service
Still need your lights up? We've got you covered!
✓ Professional installation
✓ Same-day service available
✓ You provide lights or we can supply
✓ Fully insured
✓ Single story: $200-350
✓ Two story: $400-600
Call or text: [PHONE NUMBER]
Available Dec 12-23 - Don't miss out!
```

### Nextdoor/Facebook:
```
🎄 Neighbor offering Christmas Light Installation! 🎄
Hi neighbors! I know it's getting late in the season,
but if you still need help getting your lights up,
I'm here to help!

Professional installation at fair prices:
• Single story homes: starting at $200
• Two story homes: starting at $400
• Same-day service available
• Safe, insured, reliable

Call [PHONE] to schedule. Availability limited!
- Matthew (your local neighbor)
```

### Door Hanger:
```
STILL NEED YOUR CHRISTMAS LIGHTS UP?
We can help - TODAY!

Professional Installation
✓ Safe ✓ Fast ✓ Affordable

Single Story: From $200
Two Story: From $400

CALL NOW: [PHONE]
Or scan QR code →

Limited availability Dec 12-23
Don't let another year pass without lights!
```

---

## 🎯 SUCCESS METRICS

### Week 1 Goals (Dec 12-16):
- [ ] Voice agent handling 20+ calls
- [ ] 5 jobs booked
- [ ] $1,500+ revenue
- [ ] 90% customer satisfaction

### Total Goals (Dec 12-24):
- [ ] 100+ calls handled by agent
- [ ] 20-30 jobs completed
- [ ] $5,000+ revenue
- [ ] Voice agent ready for next business

---

## 🔄 FUTURE APPLICATIONS

This same voice agent infrastructure will handle:

1. **Plotter Mechanix Remote Support**
   - $175/session intake
   - Scheduling and troubleshooting

2. **Agency Sales Calls**
   - Qualify leads
   - Book discovery calls
   - Collect project details

3. **Any Service Business**
   - Lawn care
   - Pressure washing
   - Handyman services
   - IT support

4. **Demo Scheduling**
   - Handle inbound interest
   - Book demo slots
   - Send calendar invites

---

## ⚡ QUICK START CHECKLIST

### Today (Dec 10):
- [x] Create project plan
- [ ] Research Vapi.ai vs Bland.ai (evening)
- [ ] Record 30 min voice samples (evening)

### Tomorrow (Dec 11):
- [ ] Complete 8hr data annotation first
- [ ] Set up voice agent (2 hrs)
- [ ] Test thoroughly (1 hr)
- [ ] Create marketing materials (1 hr)

### Dec 12:
- [ ] Complete 8hr data annotation first
- [ ] Launch marketing campaign
- [ ] Handle first calls
- [ ] Book first jobs

---

## 📝 NOTES

**Why This Project:**
1. Immediate cash flow (same-day payment)
2. Reusable infrastructure (not throwaway work)
3. High hourly rate ($150-180/hr)
4. Tests voice agent for bigger projects
5. Builds local reputation and network

**Risk Mitigation:**
- Simple service (low complexity)
- Cash upfront (no collection issues)
- Limited time window (Dec 12-24 only)
- Voice agent handles volume
- Can refer overflow to competitors

**This is a PERFECT test case for voice agent technology that we'll use everywhere.**