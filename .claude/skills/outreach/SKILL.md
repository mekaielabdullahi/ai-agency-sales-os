---
name: outreach
description: Universal lead outreach command. Works with direct input OR pulls from Notion. Creates Gmail drafts, Notion tasks, and personalized emails. Gracefully degrades when APIs unavailable.
---

# /outreach - Universal Lead Outreach

One command for all outreach needs. Portable, flexible, and fully automated when your stack is configured.

## Usage

```bash
# Direct input (works anywhere)
/outreach Brad Ellison, Ellyson Enterprises, metal fab, referred by Kelsey

# Pull from Notion
/outreach --notion "Brad Ellison"

# List leads in Notion pipeline
/outreach --list

# Force cold outreach (ignore transcripts)
/outreach --cold Brad Ellison, Ellyson Enterprises

# Include proposal draft
/outreach --proposal Brad Ellison, Ellyson Enterprises
```

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        /outreach                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INPUT (choose one):                                            │
│  ├── Direct: Name, Company, Context, Referral source...        │
│  └── Notion: --notion "Name" (pulls full lead profile)          │
│                                                                 │
│  ENRICHMENT (automatic):                                        │
│  ├── Web search company (if website provided)                  │
│  ├── Search transcripts (Fireflies, Team Meetings)             │
│  └── Pull Notion context (if --notion mode)                    │
│                                                                 │
│  OUTPUT (adapts to what's configured):                          │
│  ├── Gmail draft ──────── OR ──── Copyable email text          │
│  ├── Notion follow-up tasks ─ OR ─ Manual reminder             │
│  ├── Contact status update ── OR ─ Skip                        │
│  └── LinkedIn message draft                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Workflow

### Step 1: Parse Input

**Direct Input Mode:**
Extract from the input string:
- **Name**: First/last name of contact
- **Company**: Company name
- **Context**: Industry, size, pain points, needs
- **Referral**: Who referred them (if any)
- **Email**: If provided
- **Website**: If provided

**Notion Mode (`--notion`):**
```bash
cd agentic && python3 modules/notion/tool/fetch_lead.py "[NAME]"
```

If Notion not configured, fall back to direct input mode.

### Step 2: Enrich Lead (Optional)

**If website available:**
Use WebFetch to gather:
- What they do
- Company size signals
- Recent news
- Pain points

**Search for transcripts:**
```bash
cd agentic && python3 modules/notion/tool/fetch_transcripts.py "[NAME]"
```

If transcripts found:
- Reference specific topics discussed
- Follow up on action items
- Personalize based on their words

If no transcripts or script unavailable, proceed with cold outreach template.

### Step 3: Qualify Lead

Score against ICP (1-10):
- **Company Size**: 20-500 employees (+2)
- **Revenue signals**: $2M-50M (+2)
- **Decision maker role**: Founder/CEO/COO (+2)
- **Pain signals**: Mentioned specific needs (+2)
- **Referral**: Warm intro (+2)

Output qualification summary.

### Step 4: Generate Outreach

**Email Template Selection:**

**If Referral (warm intro):**
```
Subject: [Referrer] mentioned we should connect

Hi [First Name],

[Referrer] over at [Referrer Company] mentioned we should talk. [He/She] said [context about why they connected you].

We help [industry] businesses [specific value prop based on their context].

Would you be open to a quick 20-minute call this week? No pitch - just want to understand what you're working on and see if there's a fit.

[Time options or calendar link]

Best,
[Your name]
AriseGroup.ai

P.S. [Personal touch based on context]
```

**If Follow-up (transcript exists):**
```
Subject: Following up on [topic from conversation]

Hi [First Name],

[Reference specific point from conversation - "When we spoke about..."]

[Connect their stated need to our solution]

[Propose concrete next step based on where conversation left off]

Best,
[Team member who had the conversation]

---
AriseGroup.ai
```

**If Cold (no prior contact):**
```
Subject: [Personalized based on industry/pain point]

Hi [First Name],

[Opening hook - specific observation about their company]

[Value proposition - what we can help with]

[Social proof - relevant result or case study]

[Soft CTA - discovery call or quick chat]

Best,
[Your name]
AriseGroup.ai
```

**LinkedIn Message (shorter):**
```
Hi [Name],

[Referrer] suggested I reach out. We help [industry] companies [specific outcome].

Worth a quick chat this week?
```

### Step 5: Create Outputs

**Gmail Draft (if configured):**
```bash
python3 agentic/modules/google/gmail_draft.py --check
```

If configured:
```bash
python3 agentic/modules/google/gmail_draft.py \
  --to "[EMAIL]" \
  --subject "[SUBJECT]" \
  --body "[BODY]"
```

If not configured, output copyable email block:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📧 EMAIL DRAFT (Copy to Gmail)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

To: [email]
Subject: [subject]

[body]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Notion Follow-up Tasks (if configured):**
```bash
python3 agentic/modules/notion/tool/create_follow_up.py \
  --contact "[NAME]" \
  --email "[EMAIL]" \
  --outreach-type [cold|warm|followup]
```

Creates:
- +3 days: Follow up if no response (High)
- +7 days: Second follow up (Medium)
- +14 days: Final follow up / nurture decision (Low)

If not configured, output reminder:
```
⚠️ Manual follow-up needed:
   - Day 3: Follow up if no response
   - Day 7: Second follow up
   - Day 14: Decide to nurture or close
```

**Notion Contact Update (if configured):**
```bash
python3 agentic/modules/notion/tool/update_contact.py \
  --contact-id "[ID]" \
  --outreach "[SUBJECT]"
```

### Step 6: Output Summary

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📧 OUTREACH: [Contact Name] @ [Company]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lead Profile
Name: [Name]
Company: [Company]
Industry: [Industry]
Source: [Referral/Inbound/Cold]
Lead Score: [X]/10

## Context Found
[Transcript summary OR research findings OR "No prior context"]

## Email Draft
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Full email here]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## LinkedIn Message
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Short LinkedIn message]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Automation Status
├── Gmail Draft: ✅ Created / ⚠️ Copy above (not configured)
├── Notion Tasks: ✅ Created / ⚠️ Add manually
└── Contact Update: ✅ Updated / ⚠️ Update manually

## Next Steps
1. [Review and send email]
2. [Add to CRM if not auto-added]
3. [Set calendar reminder if tasks not auto-created]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## AriseGroup Team Context

When drafting, represent AriseGroup.ai appropriately:

**AriseGroup.ai** - AI Solutions Agency
- **Focus:** Helping businesses implement AI to transform operations
- **Approach:** Start with business outcomes, rapid prototyping, focus on ROI
- **Services:** AI Strategy, Custom AI Development, Process Automation, Integration

**Team:**
- **Mekaiel** - Founder/CEO, leads strategy and client relationships
- **Trent** - Technical Lead, implementation and development
- **Chris** - Sales & Partnerships

**Tone:** Professional but approachable, outcome-focused (not jargon), partnership-oriented

---

## Configuration Status Check

Run this to see what's configured:

```bash
# Check Gmail
python3 agentic/modules/google/gmail_draft.py --check

# Check Notion
python3 agentic/modules/notion/tool/fetch_tasks.py 2>&1 | head -5
```

**Full automation requires:**
- `agentic/.env` with `NOTION_API_KEY`
- `agentic/modules/google/credentials.json` for Gmail
- Notion Contacts database shared with integration
- Notion Tasks database shared with integration

**Without configuration:**
- Command still works
- Outputs copyable text instead of creating drafts
- Reminds you to add follow-ups manually

---

## Examples

**Example 1: Referral (direct input)**
```
/outreach Brad Ellison, Ellyson Enterprises, metal fabricator,
referred by Kelsey from Plotter Mechanix, $100K/week payroll,
50-60 employees, scaling fast
```

**Example 2: Pull from Notion**
```
/outreach --notion "Randy Tech"
```

**Example 3: Quick cold outreach**
```
/outreach --cold John Smith, Acme Corp, CEO, john@acme.com
```

**Example 4: With proposal**
```
/outreach --proposal Brad Ellison, Ellyson Enterprises
```

---

## Flags Reference

| Flag | Description |
|------|-------------|
| `--notion "Name"` | Pull lead from Notion instead of direct input |
| `--list` | List all leads in Notion pipeline |
| `--cold` | Force cold template (skip transcript search) |
| `--proposal` | Also generate proposal draft |
| `--no-tasks` | Skip creating follow-up tasks |
| `--linkedin-only` | Only generate LinkedIn message |

---

## Integration Points

| Feature | Tool | Required |
|---------|------|----------|
| Lead data | `fetch_lead.py` | Optional (Notion) |
| Transcripts | `fetch_transcripts.py` | Optional (Notion) |
| Gmail draft | `gmail_draft.py` | Optional (OAuth) |
| Follow-up tasks | `create_follow_up.py` | Optional (Notion) |
| Contact update | `update_contact.py` | Optional (Notion) |
| Company research | WebFetch | Built-in |

---

## Portability

This command works in three modes:

1. **Full Stack** (all APIs configured): Complete automation
2. **Partial** (some APIs): Uses what's available, falls back on rest
3. **Portable** (no APIs): Just Claude Code, outputs copyable text

You can use this on any machine, any environment. Configure more = more automation.
