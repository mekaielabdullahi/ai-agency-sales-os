# Business Funnel

> How Arise Group converts attention into revenue.
> Created during Daily Brief setup. Read by /prime and Daily Brief.

## Currency
USD

## Stages

### 1. Awareness
Website traffic and content reach.
- Sessions → ga4_daily.sessions
- New Users → ga4_daily.new_users
- Pageviews → ga4_daily.pageviews

### 2. Leads
Contacts generated from outreach channels.
- Total Leads → leads.count (WHERE stage='lead')
- Cold Email Leads → leads.count (WHERE source='cold_email')
- Warm Leads → leads.count (WHERE source='warm')
- Networking Leads → leads.count (WHERE source='networking')

### 3. Discovery Calls
Meetings booked with qualified prospects.
- Calls Booked → meetings.count (WHERE department='sales')

### 4. Proposals
Quotes sent to qualified prospects.
- Proposals Sent → leads.count (WHERE stage='proposal')

### 5. Closed Deals
Revenue from signed clients.
- Closed Deals → leads.count (WHERE stage='closed')
- Revenue → leads.sum(value) (WHERE stage='closed')

## Monthly Targets
- Leads: 50
- Discovery Calls: 10
- Proposals: 5
- Closed Deals: 2
- Revenue: $10,000

## Notes
- Primary offer: $5K AI Integration Sprint
- Case study benchmark: Plotter Mechanix ($5K → $50K revenue enabled)
- Channels: Cold email, warm contacts, door knocking/networking
