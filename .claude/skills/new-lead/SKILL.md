# New Lead Workflow

Process a new lead from Notion - pull their info, fetch conversation history, generate personalized outreach, create proposal draft, and set up follow-up tasks.

## Trigger
- `/new-lead [contact name]` - Process specific lead
- `/new-lead --list` - Show all leads in pipeline

## AriseGroup Team Context

When drafting outreach, represent the AriseGroup.ai team appropriately:

**AriseGroup.ai** - AI Solutions Agency
- **Focus:** Helping businesses implement AI to transform operations
- **Approach:** Start with business outcomes, rapid prototyping, focus on ROI
- **Core Services:**
  - AI Strategy & Consulting
  - Custom AI Development
  - Process Automation
  - AI Integration & Implementation

**Team Members:**
- **Mekaiel** - Founder/CEO, leads strategy and client relationships
- **Trent** - Technical Lead, handles implementation and development
- **Chris** - Sales & Partnerships

**Tone:** Professional but approachable, focus on outcomes not technology jargon, partnership-oriented

## Workflow

### Step 1: Fetch Lead Information

Run the fetch script to pull lead data from Notion:

```bash
cd agentic && python3 modules/notion/tool/fetch_lead.py "[CONTACT_NAME]"
```

Or list all leads:
```bash
cd agentic && python3 modules/notion/tool/fetch_lead.py --list-leads
```

This retrieves:
- Contact: Name, Email, Phone, Role, Notes
- Company: Name, Website, Industry, Notes
- Relationship history

### Step 2: Fetch Conversation History (NEW)

Search for any prior conversations/meetings with this lead:

```bash
cd agentic && python3 modules/notion/tool/fetch_transcripts.py "[CONTACT_NAME]"
```

Or search by email:
```bash
cd agentic && python3 modules/notion/tool/fetch_transcripts.py --email "[EMAIL]"
```

This searches BOTH:
- **Fireflies Transcripts** (personal recordings)
- **Team Meetings database** (shared team notes)

If transcripts are found, use them to:
- Reference specific topics discussed
- Follow up on action items mentioned
- Personalize the email based on their actual words/concerns
- Avoid repeating information already shared

### Step 3: Research & Context Gathering

If company website is available:
1. Use WebFetch to scan their website for:
   - What they do (products/services)
   - Company size indicators
   - Pain points we can address
   - Recent news or updates

2. Check existing notes in Notion for prior context

### Step 4: Generate Personalized Outreach Email

Based on lead info, transcripts, and research, draft a personalized email.

**If Previous Conversation Exists:**
```
Subject: Following up on [topic from transcript]

Hi [First Name],

[Reference specific point from conversation - "When we spoke about..."]

[Connect their stated need to our solution]

[Propose concrete next step based on where conversation left off]

Best,
[Team member who had the conversation]

---
AriseGroup.ai | AI Solutions for [Industry]
```

**If No Prior Conversation (Cold Outreach):**
```
Subject: [Personalized based on industry/role]

Hi [First Name],

[Opening hook - reference something specific about their company/role]

[Value proposition - what we can help with based on their industry]

[Social proof - relevant case study or result]

[Soft CTA - discovery call or quick chat]

Best,
[Appropriate team member]

---
AriseGroup.ai | AI Solutions for [Industry]
```

### Step 5: Create Gmail Draft

Use the Gmail integration to create draft directly:

```bash
python3 modules/google/gmail_draft.py --to "[EMAIL]" --subject "[SUBJECT]" --body "[BODY]"
```

First use will prompt for OAuth authorization.

### Step 6: Generate Proposal Draft (If Requested)

Create a markdown proposal:

```bash
python3 modules/google/docs_proposal.py --company "[COMPANY]" --contact "[NAME]" --industry "[INDUSTRY]"
```

If Google Docs API not available, outputs formatted markdown to copy/paste.

### Step 7: Update Contact Status (AUTOMATED)

After generating the email, automatically update the contact in Notion:

```bash
cd agentic && python3 modules/notion/tool/update_contact.py \
    --contact-id "[CONTACT_ID]" \
    --outreach "[EMAIL_SUBJECT]"
```

This automatically:
- Sets contact Type to "Outreach Sent"
- Updates Last Contacted to today
- Adds note with email subject and outreach type

### Step 8: Create Follow-up Tasks (AUTOMATED)

Automatically create follow-up tasks in Notion Tasks database:

```bash
cd agentic && python3 modules/notion/tool/create_follow_up.py \
    --contact "[CONTACT_NAME]" \
    --contact-id "[CONTACT_ID]" \
    --email "[EMAIL]" \
    --outreach-type cold
```

Default sequence created:
1. **+3 days:** "Follow up with [Name] if no response" (High priority)
2. **+7 days:** "Second follow up with [Name]" (Medium priority)
3. **+14 days:** "Final follow up / nurture decision for [Name]" (Low priority)

Custom sequence:
```bash
python3 modules/notion/tool/create_follow_up.py --contact "Brian" --custom-days 2,5,10
```

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📧 NEW LEAD WORKFLOW: [Contact Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lead Profile
[Contact and company summary]

## Conversation History
[Transcripts found or "No prior conversations found"]
- Key topics discussed
- Action items mentioned
- Their stated concerns/needs

## Research Insights
[Key findings from website/notes]

## Outreach Email (Ready to Send)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Full email - created as Gmail draft]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Gmail Draft Status
✅ Draft created - Open: [Gmail Drafts Link]

## Notion Updates (AUTOMATED)
✅ Contact status → "Outreach Sent"
✅ Last Contacted → Today
✅ Note added with email subject

## Follow-up Tasks Created (AUTOMATED)
✅ +3 days: Follow up with [Name] if no response (High)
✅ +7 days: Second follow up with [Name] (Medium)
✅ +14 days: Final follow up / nurture decision (Low)

## Next Steps
☐ Review and send email draft in Gmail
☐ Tasks will auto-remind you for follow-ups

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Email Templates by Industry

### Manufacturing
- Subject: "Reducing [specific pain point] with AI at [Company]"
- Hook: Reference their products or recent expansion
- Value: Predictive maintenance, quality control, process optimization

### System Integrator
- Subject: "AI capabilities for your integration projects"
- Hook: Reference their client work or expertise areas
- Value: AI tools to enhance their service offerings

### Software/Tech
- Subject: "AI-powered [specific feature] for [Product]"
- Hook: Reference their product or recent feature release
- Value: AI integration, automation, intelligent features

### Consulting
- Subject: "AI practice development for [Company]"
- Hook: Reference their consulting focus or recent thought leadership
- Value: AI service offerings they can deliver to clients

### Virtual Staffing / HR
- Subject: "AI-Powered Operations for [Company]"
- Hook: Reference their placement volume or platform integrations
- Value: AI matching, automated onboarding, quality monitoring

## Integration Points

- **Notion Contacts:** Read lead info + UPDATE status after outreach
- **Notion Transcripts:** Fetch Fireflies recordings & team meetings
- **Notion Tasks:** AUTO-CREATE follow-up tasks (3, 7, 14 day sequence)
- **WebFetch:** Research company website
- **Gmail API:** Create email drafts directly
- **Google Docs:** Create proposals (or markdown fallback)

## Automation Summary

| Action | Tool | Trigger |
|--------|------|---------|
| Fetch lead info | `fetch_lead.py` | Start of workflow |
| Search transcripts | `fetch_transcripts.py` | After lead fetch |
| Create email draft | `gmail_draft.py` | After email generated |
| Update contact status | `update_contact.py` | After email created |
| Create follow-up tasks | `create_follow_up.py` | After status updated |

## Quick Actions

After running `/new-lead`:
1. Check Gmail Drafts for the ready-to-send email
2. Review and personalize if needed
3. Send!
4. Add follow-up tasks to Notion

## Example Usage

```
User: /new-lead Randy

Claude: [Fetches Randy from Notion]
        [Finds Fireflies transcript from Jan 17 conversation]
        [Researches company website]
        [Generates follow-up email referencing their discussion]
        [Creates Gmail draft]
        [Outputs everything in formatted display]
```

## Flags

- `--list` - List all leads in pipeline
- `--no-transcript` - Skip transcript search
- `--proposal` - Also generate proposal draft
- `--cold` - Force cold outreach template (ignore transcripts)
