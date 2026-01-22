# Speed to Lead Command

Rapidly respond to a new inbound lead with personalized outreach and discovery call booking.

> **This is the fast-response mode of the [client-outreach skill](../.claude/skills/client-outreach/SKILL.md)**
> Use `/speed-to-lead` for inbound leads that need immediate response.
> Use `/client-outreach` for proactive campaign planning and pipeline management.

## Usage
```
/speed-to-lead [lead info]
```

## Input Required
Provide any of the following about the new lead:
- Name
- Company
- Email
- LinkedIn URL
- How they found us (source)
- Any context about their needs

## What This Command Does

### Step 1: Lead Enrichment
Research the lead to gather:
- Company size, industry, and revenue signals
- Recent company news or announcements
- LinkedIn activity and posts
- Tech stack indicators
- Pain point signals

### Step 2: ICP Qualification
Check against AriseGroup.ai Ideal Client Profile (see full criteria in [client-outreach skill](../.claude/skills/client-outreach/SKILL.md#ideal-client-profile-icp)):
- **Company Size**: 20-500 employees
- **Revenue**: $2M-50M annually
- **Industry**: Professional services, SaaS, consulting, agencies
- **Role**: Founder, CEO, COO, VP Operations
- **Budget Signals**: Recent funding, growth, hiring

### Step 3: Personalized Outreach Draft
Generate a personalized message using the framework from client-outreach:
1. **Hook**: Specific observation about them/their company
2. **Credibility**: Relevant AriseGroup.ai background
3. **Value Offer**: Free AI Readiness Audit
4. **CTA**: Calendar link for discovery call

### Step 4: Output Package
Deliver:
1. **Lead Score** (1-10) with qualification notes
2. **LinkedIn Message** (ready to send)
3. **Email Draft** (backup channel)
4. **Suggested Call Times** (based on their timezone)
5. **Discovery Call Prep Notes** (talking points specific to them)

---

## Speed Targets
- **Response Time**: < 5 minutes from lead received
- **Personalization Depth**: At least 2 specific observations
- **Call Booking**: Within 24-48 hours of first contact

## Integration Points
- **Cal.com**: https://cal.com/arisegroup (for booking links)
- **CRM**: Log interaction to HubSpot/Notion after outreach
- **Follow-up**: Set reminder for Day 3 if no response
- **Templates**: Uses templates from client-outreach skill

---

## Example Usage

**Input:**
```
/speed-to-lead John Smith, CEO of TechFlow Solutions, found us through LinkedIn post about AI automation, email: john@techflow.io
```

**Output:**
I'll research TechFlow Solutions, score the lead, and generate personalized outreach ready to send within 2 minutes.

---

## Related

- **[client-outreach skill](../.claude/skills/client-outreach/SKILL.md)** - Full outreach system with campaign planning, templates, pipeline tracking
- **[comprehensive-ai-audit skill](../.claude/skills/comprehensive-ai-audit/SKILL.md)** - For post-discovery audit workflow
