# Invoice Template

**Stages:** 3 (Audit), 4 (Implementation)
**Touchpoints:** #13, #19
**Type:** Document
**Automation:** Auto-generate (populate with deal details)

---

## Purpose

Invoice for audit and implementation services.

---

## Invoice Layout

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  [LOGO]                                                     │
│                                                             │
│  AriseGroup.ai                                              │
│  [Address Line 1]                                           │
│  [Address Line 2]                                           │
│  [Email] | [Phone]                                          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INVOICE                                                    │
│                                                             │
│  Invoice #: [INV-XXXX]                                      │
│  Date: [Date]                                               │
│  Due Date: [Date]                                           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BILL TO:                                                   │
│  [Client Company Name]                                      │
│  [Client Contact Name]                                      │
│  [Client Address]                                           │
│  [Client Email]                                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DESCRIPTION                              AMOUNT            │
│  ─────────────────────────────────────────────────          │
│  [Service/Project Name]                   $[Amount]         │
│  [Description line 1]                                       │
│  [Description line 2]                                       │
│                                                             │
│  ─────────────────────────────────────────────────          │
│                                                             │
│                              Subtotal:    $[Amount]         │
│                              Tax ([X]%):  $[Amount]         │
│                              ─────────────────────          │
│                              TOTAL DUE:   $[Amount]         │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PAYMENT METHODS                                            │
│                                                             │
│  Bank Transfer (ACH):                                       │
│  Bank: [Bank Name]                                          │
│  Routing: [Routing Number]                                  │
│  Account: [Account Number]                                  │
│                                                             │
│  Credit Card:                                               │
│  Pay online: [Payment Link]                                 │
│  (+3% processing fee)                                       │
│                                                             │
│  Check:                                                     │
│  Make payable to: AriseGroup.ai                             │
│  Mail to: [Address]                                         │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NOTES                                                      │
│  [Any special terms or notes]                               │
│                                                             │
│  Payment due within 30 days.                                │
│  Late payments subject to 1.5% monthly fee.                 │
│                                                             │
│  Questions? Contact [email] or [phone]                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Invoice Types

### AI Audit Invoice

```
DESCRIPTION                                    AMOUNT

AI Audit - [Company Name]                      $[Amount]
- Business Functions Mapping
- Opportunity Matrix
- PRD + Roadmap + Money Slide
- 2-4 hours of discovery sessions

                                    TOTAL:     $[Amount]
```

### Implementation Invoice (Deposit)

```
DESCRIPTION                                    AMOUNT

[Project Name] - Deposit ([X]%)                $[Amount]
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]
(Remaining balance due at [milestone])

                                    TOTAL:     $[Amount]
```

### Implementation Invoice (Final)

```
DESCRIPTION                                    AMOUNT

[Project Name] - Final Payment ([X]%)          $[Amount]
- Project completion
- Go-live support
- [X] days post-launch support

Previous Payments:                             -$[Amount]
                                    ──────────────────
                                    BALANCE DUE: $[Amount]
```

---

## Variables to Auto-Fill

| Variable | Source |
|----------|--------|
| Invoice Number | Auto-increment |
| Date | Current date |
| Due Date | Date + 30 days |
| Client Name | CRM |
| Client Address | CRM |
| Client Email | CRM |
| Project Name | Deal |
| Amount | Deal |
| Description | Template by type |

---

## Implementation Notes

**Generate Using:**
- Stripe Invoicing
- QuickBooks
- Wave
- Custom PDF generator
- Notion + PDF export

**Workflow:**
1. Deal marked ready for invoice
2. Invoice auto-generated
3. Sent to client via email
4. Payment tracked
5. Receipt sent upon payment
6. Next stage triggered

**Payment Link:**
- Use Stripe payment links
- Or embed in invoice PDF

---

## Automation Rules

| Trigger | Action |
|---------|--------|
| Audit offer accepted | Generate audit invoice |
| Proposal accepted | Generate deposit invoice |
| Milestone reached | Generate milestone invoice |
| Project complete | Generate final invoice |
| Payment received | Send receipt, update status |
