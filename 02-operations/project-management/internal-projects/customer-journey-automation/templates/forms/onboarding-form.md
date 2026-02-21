# Onboarding Form

**Stage:** 6 - Onboarding
**Touchpoint:** #22
**Type:** Form
**Automation:** Auto-send (triggered by welcome packet)

---

## Purpose

Collect access credentials, team contacts, and system information needed to start the project.

---

## Form Fields

### Section 1: Primary Contact

| Field | Type | Required |
|-------|------|----------|
| Primary Contact Name | Text | Yes |
| Primary Contact Email | Email | Yes |
| Primary Contact Phone | Phone | Yes |
| Preferred Communication Method | Dropdown | Yes |
| Best Time to Reach You | Text | No |

### Section 2: Additional Team Members

| Field | Type | Required |
|-------|------|----------|
| Additional Contact 1 - Name | Text | No |
| Additional Contact 1 - Email | Email | No |
| Additional Contact 1 - Role | Text | No |
| Additional Contact 2 - Name | Text | No |
| Additional Contact 2 - Email | Email | No |
| Additional Contact 2 - Role | Text | No |

### Section 3: System Access

> **Important:** We'll send a secure link to collect actual credentials. This section is just to understand what systems are involved.

| Field | Type | Required |
|-------|------|----------|
| CRM Platform | Text | Yes |
| CRM Access Level Needed | Dropdown | Yes |
| Email Marketing Platform | Text | If applicable |
| Website Platform | Text | If applicable |
| Other Systems We Need Access To | Long text | No |

### Section 4: Technical Information

| Field | Type | Required |
|-------|------|----------|
| Do you have an IT contact or developer? | Yes/No + Name/Email | No |
| Any security requirements or restrictions? | Long text | No |
| Preferred method for sharing credentials | Dropdown | Yes |

### Section 5: Project Preferences

| Field | Type | Required |
|-------|------|----------|
| Preferred meeting day/time for kickoff | Text | Yes |
| Any dates to avoid during the project? | Text | No |
| Anything else we should know? | Long text | No |

---

## Dropdown Options

### Communication Method
- Email
- Phone
- Slack
- Text/SMS
- Video Call

### CRM Access Level
- Admin (full access)
- Standard User
- Limited/Custom
- Need to create account

### Credential Sharing Method
- 1Password/LastPass share
- Secure form (we'll send)
- Temporary password via phone
- Screen share setup

---

## Automation Flow

1. Welcome packet sent
2. Onboarding form sent (same email or immediately after)
3. Responses saved to project management system
4. Delivery team notified when form completed
5. Secure credential collection triggered
6. Kickoff call scheduled based on preferences

---

## Security Note

**Never collect actual passwords through the form.**

Use one of these methods instead:
- 1Password/LastPass secure share
- Separate secure credential form (encrypted)
- Verbal via phone call
- Screen share session

---

## Form Messaging

### Email Subject
```
Onboarding Form - Let's Get Started!
```

### Email Body
```
Hey [First Name],

Welcome again! Before we can dive in, we need a few things from you.

**Please complete this form:**
[FORM LINK]

This helps us:
- Set up your project workspace
- Coordinate with the right people on your team
- Get the access we need to start building

⏱️ Takes about 10 minutes

**Note:** We'll send a separate secure link to collect any login credentials - never share passwords through regular forms.

Questions? Just reply to this email.

[Signature]
```

---

## Implementation Notes

**Platform Options:**
- Typeform (with conditional logic)
- Google Forms
- Notion Form
- Custom secure form

**Integration Needs:**
- Project management sync
- Team notification
- Calendar integration for kickoff scheduling
- Secure credential collection trigger
