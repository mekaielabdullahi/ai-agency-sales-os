# Slack Best Practices

## Channel Prefix Guide

| Prefix | Category | Examples |
|--------|----------|----------|
| `all-` | Company-wide | #all-ai-agency |
| `client-` | Client acquisition/onboarding | #client-acquisition, #client-new |
| `dev-` | Development work | #dev-main |
| `mktg-` | Marketing | #marketing (future: #mktg-general) |
| `ops-` | Operations/admin | #ops-general, #ops-agreements, #ops-resources |
| `sales-` | Sales & revenue | #sales-pipeline, #sales-revenue, #sales-meetings |

---

## Message Routing Decision Tree

Before posting, ask yourself:

1. **Is this about a specific client?** → client-specific channel
2. **Is this about legal/contracts?** → #ops-agreements
3. **Is this a new lead or sales activity?** → #sales-pipeline
4. **Is this about building something technical?** → #dev-main
5. **Is this a link/resource to save?** → #ops-resources
6. **Is this about content/branding?** → #marketing
7. **Is this casual coordination?** → #ops-general

---

## Best Practices

### Use Threads
Reply in threads to keep channels scannable. When someone posts a link or asks a question, reply in a thread instead of cluttering the main channel.

### Pin Important Items
Pin critical docs in their relevant channels:
- MNDA template → #ops-agreements
- JV Agreement → #ops-agreements
- Pricing docs → #ops-resources

### Add Bookmarks
Each channel can have bookmarks at the top:
- Notion workspace → #ops-resources
- GitHub repos → #dev-main

### Daily Catch-Up
If you've been away, use Slack's AI summary feature or scroll through pinned items first.

### Archive, Don't Delete
Keep history searchable by archiving completed project channels instead of deleting.

### Keep Conversations in Context
If a discussion starts in one channel but belongs elsewhere, post a summary/link in the right channel and continue there.
