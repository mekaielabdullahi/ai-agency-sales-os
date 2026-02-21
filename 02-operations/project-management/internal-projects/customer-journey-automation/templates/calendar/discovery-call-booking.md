# Discovery Call Booking

**Stage:** 2 - Discovery
**Touchpoint:** #5
**Type:** Calendar
**Automation:** Auto-send (booking confirmation)

---

## Purpose

Calendar invite and booking page for discovery calls.

---

## Booking Page Setup

### Meeting Details

| Setting | Value |
|---------|-------|
| Meeting Name | Discovery Call with AriseGroup.ai |
| Duration | 30 minutes |
| Location | Zoom (auto-generate link) |
| Buffer Before | 5 minutes |
| Buffer After | 10 minutes |
| Availability | [Define business hours] |

### Booking Page Copy

**Headline:**
```
Let's Talk About Your Business
```

**Description:**
```
This is a no-pressure conversation to understand your situation and see if we can help.

What we'll cover:
- Your biggest operational challenges
- What you've tried so far
- What success looks like for you

Come with questions - I'm here to help, not pitch.

Duration: 30 minutes
Location: Zoom (link provided after booking)
```

---

## Confirmation Email

**Subject:**
```
Confirmed: Discovery Call on [Date] at [Time]
```

**Body:**
```
Hey [First Name],

You're all set! Here are your call details:

📅 Date: [Date]
🕐 Time: [Time] [Timezone]
📍 Location: [Zoom Link]

**Before we meet:**
Please take 5 minutes to fill out this quick form so I can come prepared:
[INTAKE FORM LINK]

**Add to calendar:**
[Google Calendar Link] | [Outlook Link] | [iCal Link]

**Need to reschedule?**
[Reschedule Link]

Looking forward to speaking with you!

[Signature]
```

---

## Reminder Email (24 hours before)

**Subject:**
```
Reminder: Our call tomorrow at [Time]
```

**Body:**
```
Hey [First Name],

Just a quick reminder about our call tomorrow.

📅 [Date] at [Time] [Timezone]
📍 [Zoom Link]

**Quick prep:**
- Did you complete the intake form? [FORM LINK]
- Any questions you want to make sure we cover?

See you tomorrow!

[Signature]
```

---

## No-Show Follow-Up

**Trigger:** Meeting time passed, no attendance

**Subject:**
```
Missed you today - let's reschedule
```

**Body:**
```
Hey [First Name],

I was on the call but didn't see you - hope everything's okay!

Life happens. Let's find another time that works:
[RESCHEDULE LINK]

Or if something changed and you're no longer interested, just let me know - no hard feelings.

[Signature]
```

---

## Calendar Invite Details

```
Title: Discovery Call - [First Name] + AriseGroup.ai

Description:
Hi [First Name],

Looking forward to our call!

Agenda:
1. Introductions (2 min)
2. Your situation and challenges (15 min)
3. Questions and discussion (10 min)
4. Next steps (3 min)

Join Zoom:
[Zoom Link]

Need to reschedule?
[Reschedule Link]

See you soon!
[Your Name]
```

---

## Implementation Notes

**Platform Options:**
- Calendly
- Cal.com
- HubSpot Meetings
- Acuity Scheduling

**Integrations Needed:**
- Zoom (auto-generate meeting links)
- CRM (log meeting, update contact)
- Intake form (send after booking)
- Email (confirmation + reminder)

**Automation Flow:**
1. Prospect clicks booking link
2. Selects available time
3. Booking confirmed
4. Zoom link generated
5. Confirmation email sent
6. Intake form sent
7. Calendar invite added
8. Reminder sent (24hr before)
9. No-show email if missed
