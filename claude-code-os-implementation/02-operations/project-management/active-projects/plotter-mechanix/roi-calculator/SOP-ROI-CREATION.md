# Workflow: ROI Opportunity Validation via Fireflies

**Purpose:** Systematic process to validate new ROI opportunities using Fireflies meeting transcripts and create OPP documents.

**Status:** CAPTURE FOR SKILL CONVERSION

---

## Workflow Overview

```
1. IDENTIFY opportunity (user input)
       ↓
2. EXPLORE codebase for existing evidence
       ↓
3. GENERATE tailored Fireflies prompts
       ↓
4. USER runs prompts in Fireflies agent
       ↓
5. EXTRACT validated data points
       ↓
6. CREATE OPP-X document using template
       ↓
7. UPDATE Y-CALCULATION-WORKING-DOC.md
       ↓
8. COMMIT with source citations
```

---

## Phase 1: Opportunity Identification

**Input from user:**
- Opportunity name (e.g., "Knowledge Capture")
- Sub-components (e.g., "Training Videos, Internal Agent, Planning Assistance")

**Output:**
- Clear scope of what to validate

---

## Phase 2: Codebase Exploration

**Search for existing evidence in:**
- `roi-calculator/` - Existing OPP files, calculations
- `offer/phase-2/` - Interview insights, ROI docs
- `discovery/` - Stakeholder interviews, findings
- `meetings/` - Transcripts, notes

**Extract:**
- Existing quotes with speaker attribution
- Preliminary calculations
- Source file paths

---

## Phase 3: Fireflies Prompt Generation

### Template Structure

For each ROI opportunity, generate 5-7 prompts covering:

1. **Time/Volume Prompt** - How much time is spent on X?
2. **Pain Point Prompt** - Complaints, frustrations about X
3. **Financial Impact Prompt** - Costs, losses, revenue mentions
4. **Current Process Prompt** - How is X done today?
5. **People Involved Prompt** - Who does X? (Kelsey, Alyssa, Joe, etc.)
6. **Frequency Prompt** - How often does X happen?
7. **Wish List Prompt** - What would make X better?

### Prompt Format

```
Search all [CLIENT] meeting transcripts for:
- [Specific question 1]
- [Specific question 2]
- [Specific question 3]
- [Specific question 4]

Keywords: [keyword1], [keyword2], [keyword3], [keyword4]
```

### Data Collection Table

Always include a table for user to fill:

```markdown
| Data Point | Value | Source Meeting |
|------------|-------|----------------|
| [metric 1] | _____ | |
| [metric 2] | _____ | |
| [metric 3] | _____ | |
```

---

## Phase 4: User Runs Fireflies Prompts

User copies prompts to Fireflies agent and collects:
- Direct quotes with speaker attribution
- Specific numbers/metrics
- Meeting dates/names

---

## Phase 5: Data Extraction & Validation

Map Fireflies results to ROI framework:

### Section A: Time Cost
```
Annual Cost = Time/day × People × 260 days × Hourly Rate
```

**Data needed:**
- Time per task (hrs/day or hrs/week)
- Number of people doing task
- Their hourly rate

### Section B: Lost Revenue
```
Annual Lost = Volume/month × % Lost × Value/unit × 12
```

**Data needed:**
- What's being lost (leads, quotes, inventory, etc.)
- Volume affected per month
- Percentage lost due to problem
- Value per unit

### Section C: Revenue Upside
```
Annual Revenue = Activities/month × Conversion Rate × Value/conversion × 12
```

**Data needed:**
- New activities enabled
- Expected conversion rate
- Value per conversion

---

## Phase 6: Create OPP Document

### File Naming
`OPP-[NUMBER]-[OPPORTUNITY-NAME].md`

### Template Structure

```markdown
# OPPORTUNITY [N]: [Name]

## Solution Overview
[1-2 sentence description of what the solution does]

---

## SECTION A: WHAT THIS PROBLEM COSTS IN WASTED TIME

| Field | Value | Source | Rationale |
|-------|-------|--------|-----------|
| Time wasted per person per day (hours) | **X** | [Source] | [Why] |
| Number of people doing this task | **X** | [Source] | [Who] |
| Working days per year | **260** | Standard | Default |
| Loaded hourly cost ($) | **$X** | [Source] | [Role] |
| **ANNUAL COST OF INEFFICIENCY** | **$X** | Calculated | [Formula] |

### Fireflies Evidence (Section A):

**[Category]:**
> "[Direct quote]"
> — [Speaker]

---

## SECTION B: REVENUE YOU'RE LOSING TODAY

| Field | Value | Source | Rationale |
|-------|-------|--------|-----------|
| What is being lost? | **[Description]** | [Source] | [Details] |
| Volume affected per month | **X** | [Source] | [How calculated] |
| % lost due to this problem | **X%** | [Source] | [Benchmark or evidence] |
| Value per unit ($) | **$X** | [Source] | [Data source] |
| **ANNUAL LOST REVENUE** | **$X** | Calculated | [Formula] |

### Fireflies Evidence (Section B):

> "[Direct quote]"
> — [Speaker]

---

## SECTION C: NEW REVENUE THE SOLUTION UNLOCKS

| Field | Value | Source | Rationale |
|-------|-------|--------|-----------|
| What does saved time enable? | **[Activities]** | [Source] | [Details] |
| Additional activities per month | **X** | [Source] | [Estimate] |
| Conversion / success rate (%) | **X%** | [Source] | [Benchmark] |
| Value per conversion ($) | **$X** | [Source] | [Data] |
| **ANNUAL REVENUE UPSIDE** | **$X** | Calculated | [Formula] |

### Fireflies Evidence (Section C):

> "[Direct quote]"
> — [Speaker]

---

## TOTAL ANNUAL IMPACT (A + B + C)

| Section | Annual LOW | Annual HIGH | Status |
|---------|------------|-------------|--------|
| A: Time Cost | $X | $X | COMPLETE |
| B: Lost Revenue | $X | $X | COMPLETE |
| C: Revenue Upside | $X | $X | COMPLETE |
| **TOTAL Y** | **$X** | **$X** | **COMPLETE** |

---

## KEY VALIDATION QUOTE

> "[Most compelling quote]"
> — [Speaker], [Company]

---

## SOURCE
Fireflies Meeting: [Meeting Name](URL)

---

*Generated: [DATE]*
*Framework: Morningside AI ROI Calculator*
```

---

## Phase 7: Update Working Doc

Add new line item to `Y-CALCULATION-WORKING-DOC.md`:

```markdown
## Line Item [N]: [Opportunity Name]

### Section A: Time Cost
[Table + calculation]

### Section B: Lost Revenue
[Table + calculation]

### Section C: Revenue Upside
[Table + calculation]

### TOTAL Y ([Opportunity])
[Summary table]
```

---

## Phase 8: Commit

Commit message format:
```
docs(plotter-mechanix): Add OPP-[N] [Opportunity Name] ROI calculation

- Section A: [summary]
- Section B: [summary]
- Section C: [summary]
- Total Y: $X-$X/year

Source: [Speaker] ([Date]): "[Key quote snippet]"

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## Example: Knowledge Capture Prompts

### Prompt 1: Tech Training Time Burden
```
Search all Plotter Mechanix meeting transcripts for:
- How many hours does Kelsey spend training new technicians?
- How long did Joe's training take?
- What is Kelsey's weekly time commitment when onboarding a new tech?
- Training duration in weeks or months

Keywords: training, teach, learn, hours, weeks, months, onboarding, Joe, new tech, new hire
```

### Prompt 2: Field Escalation to Kelsey
```
Search all Plotter Mechanix meeting transcripts for:
- What percentage of service calls need Kelsey's help?
- How often does Joe call Kelsey from the field?
- What types of jobs require escalation to Kelsey?
- Minor guidance vs full assistance breakdown

Keywords: call Kelsey, help, escalate, phone, guidance, assist, stuck, don't know
```

### Prompt 3: Parts Knowledge Gaps
```
Search all Plotter Mechanix meeting transcripts for:
- How long does it take to research parts?
- Who has knowledge about parts - Kelsey, Alyssa, or vendors?
- HP parts complexity and vendor communication
- Time spent figuring out which part is needed

Keywords: parts, HP, vendor, research, figure out, don't know parts, supplier, order
```

### Prompt 4: Customer Intake Process
```
Search all Plotter Mechanix meeting transcripts for:
- How are new customer requests processed?
- Duplicate customer records and database problems
- Jobber auto-creating clients
- "Seven Daves" or similar duplicate issues

Keywords: customer, intake, new request, duplicate, Jobber, client, database, merge
```

### Prompt 5: Morning Planning & Coordination
```
Search all Plotter Mechanix meeting transcripts for:
- Daily morning planning time
- Route planning and changes
- Coordination between Kelsey, Joe, and office
- How often do routes change mid-day?

Keywords: morning, planning, route, coordinate, schedule, change, frustrating, daily
```

### Prompt 6: Inventory & RMA Knowledge
```
Search all Plotter Mechanix meeting transcripts for:
- Inventory visibility problems
- QuickBooks stock accuracy
- RMA backlog and vendor credits
- Barcode system wishes or needs

Keywords: inventory, stock, RMA, barcode, QuickBooks, don't know what we have, vendor credits, pile
```

### Prompt 7: Knowledge Transfer Pain
```
Search all Plotter Mechanix meeting transcripts for:
- What happens when Kelsey is unavailable?
- Single point of failure concerns
- Documentation or video training mentions
- Kelsey's vision for remote support or consulting

Keywords: documentation, video, knowledge, transfer, if Kelsey, unavailable, remote, Piantop
```

---

## Skill Conversion Notes

**Trigger:** `/roi-opportunity [opportunity-name]` or `/fireflies-prompts [topic]`

**Inputs:**
1. Opportunity name
2. Client name (for prompt customization)
3. Sub-components (optional)

**Outputs:**
1. Tailored Fireflies prompts (5-7)
2. Data collection table
3. OPP document template pre-filled with structure

**Future Enhancement:**
- Connect to Fireflies MCP for direct transcript search
- Auto-extract quotes from search results
- Calculate Y values from extracted data

---

*Workflow captured: 2026-02-17*
*For skill conversion after validation complete*
