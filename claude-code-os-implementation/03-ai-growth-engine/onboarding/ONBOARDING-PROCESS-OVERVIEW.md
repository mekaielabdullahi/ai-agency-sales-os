# Client Onboarding Process Overview

**Purpose:** Master reference for the complete client onboarding flow from payment to project start.

**Last Updated:** January 2026

---

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     CLIENT PAYS INVOICE                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  AUTOMATED (via n8n)                                             │
│  ────────────────────                                            │
│  1. Update Notion: Status = "Paid"                               │
│  2. Gratitude email sent (immediate)                             │
│  3. Wait 5 minutes                                               │
│  4. Next Steps email sent (with calendar link)                   │
│  5. Slack channels created (#client, #client-internal)           │
│  6. Team notified in #new-clients                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  LOGISTICS ONBOARDING CALL (15-30 min)                           │
│  ─────────────────────────────────────                           │
│  • Client books via calendar link                                │
│  • Collect all platform access live                              │
│  • Handle 2FA codes in real-time                                 │
│  • Quick expectations setting                                    │
│  • Confirm win condition                                         │
│  • Schedule Project Kickoff                                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PROJECT KICKOFF CALL (60 min)                                   │
│  ─────────────────────────────                                   │
│  • Present audit findings                                        │
│  • Walk through proposed solutions                               │
│  • Confirm detailed timeline                                     │
│  • Communication protocol review                                 │
│  • Q&A                                                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PROJECT EXECUTION BEGINS                                        │
│  ────────────────────────                                        │
│  • You're unblocked - all access collected                       │
│  • Client knows exactly what to expect                           │
│  • Win condition documented                                      │
│  • Communication channel established                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Three Problems We're Solving

| Problem | Solution | When |
|---------|----------|------|
| **Buyer Remorse** | Immediate emails showing professionalism and progress | Within 5 min of payment |
| **Unclear Expectations** | Communication doc + Win condition template | Logistics Call |
| **Logistics Drag** | All access collected live on one call | Logistics Call |

---

## Automation Flow (n8n)

**Workflow:** `client-onboarding-sequence`

**Trigger:** Notion database update → Status = "Paid"

```
[Notion Trigger]
     │
     ▼
[Get Client Data]
     │ • Name
     │ • Email
     │ • Project type
     │
     ▼
[Send Gratitude Email]
     │
     ▼
[Wait 5 Minutes]
     │
     ▼
[Send Next Steps Email]
     │ • Calendar link
     │ • Platform list
     │
     ▼
[Create Slack Channels]
     │ • #clientname
     │ • #clientname-internal
     │
     ▼
[Update Notion]
     │ • Onboarding Started = timestamp
     │
     ▼
[Notify Team]
     • Post in #new-clients
```

---

## Templates & Documents

### Core Templates

| Document | Location | Purpose |
|----------|----------|---------|
| **Gratitude Email** | `templates/emails/gratitude-email.md` | Immediate post-payment thanks |
| **Next Steps Email** | `templates/emails/next-steps-email.md` | Calendar link + what's next |
| **Win Condition** | `templates/win-condition-template.md` | Define "done" to prevent scope creep |
| **Communication Expectations** | `templates/communication-expectations.md` | Channel, cadence, availability |
| **Platform Sign-up Instructions** | `templates/platform-signup-instructions.md` | Step-by-step for each platform |

### Call SOPs

| Document | Location | Purpose |
|----------|----------|---------|
| **Logistics Onboarding Call** | `checklists/logistics-onboarding-call-sop.md` | 15-30 min access collection |
| **Project Kickoff Call** | `checklists/kickoff-call-agenda.md` | 60 min project presentation |

### Supporting Documents

| Document | Location | Purpose |
|----------|----------|---------|
| **Access Collection Protocol** | `templates/access-collection-protocol.md` | Security standards + tracking |
| **Client Intake Form** | `checklists/client-intake-form.md` | Initial information gathering |
| **Onboarding Playbook** | `playbooks/automation-client-onboarding-playbook.md` | Full reference (Nick's framework) |

---

## Timeline

| Day | What Happens | Owner |
|-----|--------------|-------|
| **Day 0** | Payment received | Client |
| **Day 0** | Automated emails + Slack setup | System |
| **Day 1-2** | Logistics Onboarding Call | You + Client |
| **Day 3-5** | Project Kickoff Call | You + Client |
| **Day 5+** | Project execution begins | You |

---

## Checklist: Ready for Next Client

Before signing your next client, verify:

### Automation
- [ ] n8n workflow deployed and tested
- [ ] Gmail/SMTP configured for sending
- [ ] Notion database has "Paid" status option
- [ ] Slack channels auto-create working
- [ ] Calendar link active (Calendly/Cal.com)

### Templates
- [ ] Gratitude email personalized with your info
- [ ] Next Steps email has correct calendar link
- [ ] Win condition template ready to customize
- [ ] Communication expectations reflects your actual availability
- [ ] Platform instructions cover your common tech stack

### Process
- [ ] Logistics call SOP reviewed
- [ ] Project kickoff agenda ready
- [ ] Access collection protocol understood
- [ ] Team knows the new process

---

## Quick Reference

### Immediate Post-Payment (Automated)
1. Gratitude email → Shows human care
2. Next Steps email → Shows organization
3. Slack channels → Creates workspace
4. Team notification → Everyone knows

### Logistics Call (15-30 min)
1. Thank them for joining
2. Explain why logistics matter
3. Quick expectations (channel, cadence, timeline)
4. Platform walkthrough with screen share
5. Handle 2FA live
6. Confirm win condition
7. Schedule Project Kickoff

### Project Kickoff (60 min)
1. Team introductions
2. Audit presentation
3. Proposed solutions
4. Detailed timeline
5. Communication protocol
6. Access verification
7. Q&A
8. Next steps

---

## Metrics to Track

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Time to first email | < 1 min | n8n logs |
| Logistics call booked | < 48 hours | Calendar |
| All access collected | 1 call | Post-call checklist |
| Project start delay | 0 days | Kickoff date vs payment date |
| Client satisfaction | High | Post-onboarding feedback |

---

## Troubleshooting

### "Client didn't book the logistics call"
- Follow up in 24 hours via email
- Emphasize: "15 minutes now saves 2-3 weeks later"
- Offer alternative times

### "Missing access after logistics call"
- Send specific request same day
- Follow up daily until resolved
- This is the #1 blocker - don't let it slide

### "Client wants to skip logistics call"
- Explain the value: "This is the #1 thing that speeds up projects"
- Offer: "Just 15 minutes, I promise it's worth it"
- If they insist: Send async access request, but expect delays

### "Automation didn't trigger"
- Check Notion status field
- Verify n8n workflow is active
- Send emails manually if needed (don't let client wait)

---

## Revision History

| Date | Change | Author |
|------|--------|--------|
| Jan 2026 | Initial creation | [Your Name] |
