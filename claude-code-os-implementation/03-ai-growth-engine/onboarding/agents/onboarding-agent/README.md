# Onboarding Agent

Automates the post-payment client onboarding workflow for AriseGroup.ai.

## Overview

When a client pays an invoice, this agent:

1. **Sends Gratitude Email** (< 30 seconds) - Personalized welcome email
2. **Updates Notion** - Records onboarding timestamps
3. **Waits 5 minutes** - Prevents overwhelming the client
4. **Sends Next Steps Email** - Calendar link + platform guide PDF
5. **Creates Slack Channels** - `client-{name}` and `client-{name}-internal`
6. **Notifies Team** - Posts to #new-clients

## Triggers

- **Stripe Webhook:** `payment_intent.succeeded`
- **Notion Automation:** Status changed to "Paid"

## Setup

### 1. Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
# Gmail API
GMAIL_CLIENT_ID=your-client-id
GMAIL_CLIENT_SECRET=your-client-secret
GMAIL_REFRESH_TOKEN=your-refresh-token
FROM_EMAIL=hello@arisegroup.ai

# Slack API
SLACK_BOT_TOKEN=xoxb-your-bot-token
NEW_CLIENTS_CHANNEL=new-clients

# Notion API
NOTION_API_KEY=secret_your-api-key
NOTION_CLIENTS_DATABASE_ID=your-database-id

# Calendar
CALENDAR_LINK=https://cal.com/arisegroup/logistics
```

### 2. Gmail Setup

1. Create a Google Cloud project
2. Enable Gmail API
3. Create OAuth credentials
4. Generate refresh token with scopes: `gmail.send`

### 3. Slack Setup

1. Create a Slack app at api.slack.com
2. Add bot token scopes:
   - `channels:manage`
   - `channels:read`
   - `chat:write`
   - `users:read`
3. Install to workspace and copy bot token

### 4. Notion Setup

1. Create an internal integration at notion.so/my-integrations
2. Share your Clients database with the integration
3. Copy the integration token and database ID

### 5. n8n Integration

1. Create a webhook node triggered by Stripe
2. Add a Function node with this code:
   ```javascript
   const { handleN8nWebhook } = require('./n8n-webhook');
   return await handleN8nWebhook($input.body, $input.headers);
   ```
3. Deploy the workflow

## File Structure

```
onboarding-agent/
├── index.ts              # Main agent orchestration
├── utils.ts              # Utility functions
├── n8n-webhook.ts        # Webhook handlers
├── handlers/
│   ├── gmail.ts          # Email sending
│   ├── slack.ts          # Channel creation
│   └── notion.ts         # Database updates
├── templates/
│   ├── gratitude-email.md
│   └── next-steps-email.md
├── .env.example
└── README.md
```

## Notion Database Schema

Required properties on your Clients database:

| Property | Type | Description |
|----------|------|-------------|
| Name | Title | Client name |
| Email | Email | Client email |
| Project Type | Select | Type of project |
| Amount | Number | Invoice amount |
| Status | Select | Paid, Onboarding, Active, etc. |
| Onboarding Started | Date | When onboarding began |
| Gratitude Email Sent | Date | Timestamp |
| Next Steps Email Sent | Date | Timestamp |
| Slack Channels Created | Date | Timestamp |
| Team Notified | Date | Timestamp |

## Usage

### Direct Execution

```typescript
import { executeOnboarding } from './index';

const result = await executeOnboarding({
  client_id: 'notion-page-id',
  client_name: 'John Doe',
  client_email: 'john@example.com',
  project_type: 'AI Automation',
  amount: 5000,
});

console.log(result);
// {
//   success: true,
//   client_id: 'notion-page-id',
//   steps_completed: ['gratitude_email', 'notion_initial_update', ...],
//   errors: [],
//   timestamps: { ... }
// }
```

### Via n8n Webhook

POST to your n8n webhook URL with Stripe payment event or Notion webhook payload.

## Error Handling

- Each step runs independently - failures don't block other steps
- Errors are logged and collected in the result
- Success = at least 4 of 6 steps completed
- All steps are idempotent (safe to retry)

## Testing

```bash
# Run with test payload
npx ts-node test.ts

# Or use curl
curl -X POST http://localhost:5678/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{"client_id":"test","client_name":"Test Client","client_email":"test@example.com","project_type":"AI Automation","amount":5000}'
```
