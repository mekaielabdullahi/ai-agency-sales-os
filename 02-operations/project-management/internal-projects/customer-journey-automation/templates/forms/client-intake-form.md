# Client Intake Form

**Stage:** 2 - Discovery
**Touchpoint:** #6
**Type:** Form
**Automation:** Auto-send (triggered by booking confirmation)

---

## Purpose

Collect key information from prospects before the discovery call to make the call more productive.

---

## Form Fields

### Section 1: Contact Information

| Field | Type | Required |
|-------|------|----------|
| Full Name | Text | Yes |
| Email | Email | Yes |
| Phone | Phone | Yes |
| Company Name | Text | Yes |
| Website | URL | No |
| Job Title | Text | Yes |

### Section 2: Company Profile

| Field | Type | Required |
|-------|------|----------|
| Industry | Dropdown | Yes |
| Number of Employees | Dropdown (1-10, 11-25, 26-50, 51+) | Yes |
| Annual Revenue Range | Dropdown | No |
| How did you hear about us? | Dropdown + Other | Yes |

### Section 3: Current Situation

| Field | Type | Required |
|-------|------|----------|
| What's your biggest operational challenge right now? | Long text | Yes |
| What tools/systems do you currently use? | Checkboxes + Other | Yes |
| Have you tried to solve this before? If so, what happened? | Long text | No |

### Section 4: Goals

| Field | Type | Required |
|-------|------|----------|
| What would success look like for you? | Long text | Yes |
| What's your timeline for making a decision? | Dropdown | Yes |
| Is there a budget allocated for this? | Dropdown (Yes/No/Exploring) | No |

### Section 5: Meeting Prep

| Field | Type | Required |
|-------|------|----------|
| Who else should be on the call? | Text | No |
| Anything specific you want to cover? | Long text | No |

---

## Dropdown Options

### Industry
- Professional Services
- Marketing/Agency
- Real Estate
- Healthcare
- E-commerce
- SaaS/Technology
- Construction
- Legal
- Financial Services
- Other

### Tools/Systems (Checkboxes)
- CRM (HubSpot, Salesforce, etc.)
- Email Marketing (Mailchimp, ActiveCampaign, etc.)
- Project Management (Asana, Monday, etc.)
- Accounting (QuickBooks, Xero, etc.)
- Communication (Slack, Teams, etc.)
- Scheduling (Calendly, Acuity, etc.)
- Other

### Timeline
- Immediately (within 2 weeks)
- Soon (1-2 months)
- Planning ahead (3+ months)
- Just exploring

---

## Automation Flow

1. Prospect books discovery call
2. Form automatically sent via email
3. Responses saved to CRM
4. Sales rep notified when form completed
5. Responses visible before call

---

## Implementation Notes

**Platform Options:**
- Typeform
- Google Forms
- Notion Form
- HubSpot Forms
- Custom form

**Integration Needs:**
- CRM sync (create/update contact)
- Email notification to sales rep
- Calendar event update with form link

---

## Form Messaging

### Email Subject
```
Quick prep for our call on [Date]
```

### Email Body
```
Hey [First Name],

Looking forward to our call on [Date] at [Time]!

To make the most of our time together, please take 5 minutes to fill out this quick form:

[FORM LINK]

This helps me come prepared with relevant examples and ideas for your situation.

See you soon!
[Signature]
```
