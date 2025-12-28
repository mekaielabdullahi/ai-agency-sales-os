# Email Classification Automation

## Purpose
Automatically classify incoming Gmail emails into **Marketing** or **Expenses/Receipts** categories, apply Gmail labels, log classifications to n8n's internal data table, and send a weekly summary report to Slack.

## When to Use
- Trigger phrases: "email classification", "sort my emails", "label emails", "email report"
- This automation runs automatically once activated - no manual intervention needed
- Weekly reports are sent every Monday at 9:00 AM

## Components

### Workflow 1: Email Classifier
- **ID:** `KBUbyqanpMdscxhd`
- **File:** `workflows/email_classifier.json`
- **Trigger:** Gmail Trigger (polls every minute)
- **Status:** Inactive (requires setup)

**What it does:**
1. Detects new emails in Gmail inbox
2. Fetches full email content (sender, subject, body)
3. Uses Google Gemini AI to classify into: Marketing, Expenses, or Other
4. Applies Gmail label for Marketing and Expenses emails
5. Logs classified emails to n8n data table
6. Ignores "Other" emails (leaves them in inbox untouched)

### Workflow 2: Weekly Report
- **ID:** `9vNLNpOpSFDpDEJx`
- **File:** `workflows/email_weekly_report.json`
- **Trigger:** Schedule (Monday 9:00 AM)
- **Status:** Inactive (requires setup)

**What it does:**
1. Queries data table for emails classified in the last 7 days
2. Generates summary with counts, top senders, expense list
3. Posts report to Slack channel

## Setup Required (Manual Steps)

### 1. Create Gmail Labels
In Gmail, create these labels:
- **Marketing** (or "AI/Marketing")
- **Expenses** (or "AI/Expenses")

Then get the Label IDs:
```
Go to Gmail → Settings → Labels → Click the label
The URL will contain the label ID, e.g., Label_1234567890
```

### 2. Create n8n Data Table
In n8n:
1. Go to **Data Tables** (left sidebar)
2. Create new table called `email_classifications`
3. Add columns:
   - `email_id` (text)
   - `from_address` (text)
   - `from_name` (text)
   - `subject` (text)
   - `category` (text)
   - `classified_at` (text/datetime)
4. Copy the Data Table ID from the URL

### 3. Configure Workflows

**Email Classifier workflow:**
1. Open workflow `KBUbyqanpMdscxhd` in n8n
2. Configure Gmail credentials on:
   - Gmail Trigger node
   - Get Email Details node
   - Add Marketing Label node
   - Add Expenses Label node
3. Update label IDs:
   - Add Marketing Label → replace `REPLACE_WITH_MARKETING_LABEL_ID`
   - Add Expenses Label → replace `REPLACE_WITH_EXPENSES_LABEL_ID`
4. Configure Google Gemini credentials on Google Gemini node
5. Update Data Table ID on:
   - Log Marketing Email node
   - Log Expenses Email node

**Weekly Report workflow:**
1. Open workflow `9vNLNpOpSFDpDEJx` in n8n
2. Update Data Table ID on Get Last 7 Days node
3. Configure Slack credentials on Send to Slack node
4. Update Slack channel ID (replace `REPLACE_WITH_SLACK_CHANNEL_ID`)

### 4. Activate Workflows
Once configured, activate both workflows in n8n.

## Classification Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Marketing** | Promotional content | Newsletters, sales pitches, ads, product announcements, discount offers |
| **Expenses** | Financial transactions | Receipts, invoices, subscriptions, billing statements, payment confirmations |
| **Other** | Everything else | Personal emails, work conversations, questions (left unlabeled) |

## Credentials Required
- Gmail OAuth2 (for reading/labeling emails)
- Google Gemini API (for AI classification)
- Slack OAuth2 (for weekly report)

## Weekly Report Format

```
*Weekly Email Classification Report*
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*Summary (Nov 25 - Dec 2)*
• Marketing: 23 emails
• Expenses/Receipts: 8 emails

*Top Marketing Senders:*
  - newsletter@company.com (5)
  - promo@store.com (3)
  ...

*Recent Expenses:*
  - Your Netflix receipt (Netflix)
  - AWS Invoice (Amazon Web Services)
  ...

_Processed 31 total emails this week_
```

## Troubleshooting

### Emails not being classified
- Check Gmail Trigger is receiving emails (view execution history)
- Verify Gmail OAuth credentials are valid
- Check Gemini API key is configured

### Labels not being applied
- Ensure Gmail labels exist with exact names
- Verify Label IDs are correct in workflow
- Check Gmail credentials have write permissions

### Weekly report not sending
- Verify Schedule Trigger is set correctly
- Check Slack credentials and channel ID
- Ensure Data Table has data from the past 7 days

### Data table errors
- Verify Data Table ID is correct
- Check column names match workflow field mappings

## Edge Cases & Learnings

- Gemini classifies based on sender + subject + body content
- Very short emails may be harder to classify accurately
- Newsletter-style expense notifications (e.g., "Your subscription renewed") may occasionally be classified as Marketing - this is a known edge case
- The "Other" category is a catch-all to avoid over-labeling personal/work emails

---

*Last updated: December 2025*
