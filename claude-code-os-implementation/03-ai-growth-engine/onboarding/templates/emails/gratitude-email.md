# Gratitude Email Template

**Purpose:** Express sincere thanks immediately after payment to minimize buyer remorse.

**Timing:** Within 1 minute of payment confirmation
**Tone:** Short, friendly, human (like a text message, not corporate)

---

## Template

**Subject:** Thanks [First Name]!

---

Hey [First Name],

Thanks for taking care of that invoice so promptly.

I'm really excited that we get to work together and to nail this for you.

I'll send onboarding instructions and a calendar link in a moment so we can book a quick setup call.

Appreciate your business.

[Your First Name]

---

## Variables to Personalize

| Variable | Source | Example |
|----------|--------|---------|
| `[First Name]` | CRM / Notion | "Sarah" |
| `[Your First Name]` | Static | "Matt" |

---

## Key Principles

1. **Keep it short** - This is a quick thank you, not a formal letter
2. **Sound human** - Write like you're texting a colleague
3. **No sales pitch** - They already bought, don't sell more yet
4. **Set expectation** - Tell them what's coming next (the next-steps email)
5. **Personal sign-off** - First name only, not full signature block

---

## What NOT to Do

- Don't include long signature blocks with social links
- Don't add "PS" with upsells or asks
- Don't use corporate language ("We at [Company] are thrilled to...")
- Don't include attachments - keep it simple
- Don't CC other team members - this is 1:1

---

## Variations

### Variation A: More Casual

**Subject:** Hey [First Name]!

---

Hey [First Name]!

Just wanted to say thanks - really appreciate you moving forward.

Can't wait to build this out for you. You're going to love it.

Sending you onboarding details in just a sec.

Talk soon,
[Your First Name]

---

### Variation B: Slightly More Formal

**Subject:** Thank you, [First Name]

---

Hi [First Name],

Thank you for your payment - I really appreciate the trust you're placing in us.

I'm looking forward to delivering great results on this project.

You'll receive a follow-up email shortly with next steps and a link to schedule our onboarding call.

Best,
[Your First Name]

---

## n8n/Automation Notes

**Trigger:** Notion database update (Status = "Paid")

**Variables to pull:**
- Client first name
- Client email

**Email settings:**
- From: Your personal email (not noreply@)
- Reply-to: Your personal email
- Plain text preferred (more personal feel)
- No tracking pixels if possible

**Timing:**
- Send immediately (no delay)
- The next-steps email follows 5 minutes later
