# Customer Journey Automation

Internal project to build out all touchpoint templates, forms, and automation workflows for the AriseGroup.ai customer journey.

## Project Goal

Create a complete automation system for 36 customer touchpoints across 10 stages of the customer journey.

## Key Documents

- [Customer Journey Map](./customer-journey-map.md) - Visual diagrams and stage-by-stage breakdown

## Automation Summary

| Type | Count | Status |
|------|-------|--------|
| Email Templates | 14 | Pending |
| Forms | 2 | Pending |
| Documents | 2 | Pending |
| Calendar Templates | 3 | Pending |
| **Total** | **21** | |

## Folder Structure

```
customer-journey-automation/
├── README.md
├── customer-journey-map.md
├── templates/
│   ├── emails/           # 14 email templates
│   ├── forms/            # 2 intake/onboarding forms
│   ├── documents/        # Contract + invoice templates
│   └── calendar/         # Meeting invite templates
└── automation/
    └── workflows.md      # n8n/automation specs
```

## Stages & Touchpoints

| Stage | Name | Touchpoints |
|-------|------|-------------|
| 1 | Outreach | 4 |
| 2 | Discovery | 8 |
| 3 | AI Audit (First Sale) | 3 |
| 4 | Implementation Proposal | 4 |
| 5 | Handoff | 1 |
| 6 | Onboarding | 5 |
| 7 | Build | 2 |
| 8 | Go-Live | 4 |
| 9 | Support | 3 |
| 10 | Retain | 3 |
| **Total** | | **36** |

## Next Steps

1. Create email templates (14)
2. Build intake forms (2)
3. Design contract/invoice templates (2)
4. Set up calendar templates (3)
5. Configure automation workflows in n8n
