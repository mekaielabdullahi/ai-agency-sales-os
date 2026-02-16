# AI Personalization Pipeline
## n8n Workflow Spec for Automated Lead Research + Icebreaker Generation

---

## Overview

Matthew builds this as an n8n workflow. Automates the research and icebreaker generation for each new lead added to the Google Sheet.

**Manual first:** Mekaiel manually personalizes the first 50 leads (25 printing, 25 homestead) via ChatGPT while Matthew builds the automation. ~2.5 hours. Validates copy quality before automation scales it.

---

## Workflow Steps

### Step 1: Google Sheet Trigger
- **Trigger:** New row added OR status changed to "New"
- **Sheet:** Cold Outreach Tracker > Lead Tracker tab
- **Fields passed:** Company Name, Owner Name, Website, Vertical, Social Media URL

### Step 2: Perplexity Research
- **Input:** Company name + website URL
- **API:** Perplexity API
- **Prompt:**

```
Research this company and return the following in JSON format:
- company_description: One sentence describing what they do (max 20 words)
- recent_news: Any recent news, blog post, social media activity, or notable event (max 25 words). If nothing found, return null.
- likely_challenge: Based on their size and industry, their most likely operational challenge (max 20 words)
- specific_detail: One specific, verifiable detail about the company (product they sell, service they offer, location they serve, equipment they use) (max 15 words)

Company: [Company Name]
Website: [Website URL]
Vertical: [Printing/Homestead]
```

- **Output:** JSON with 4 fields

### Step 3: ChatGPT Icebreaker Generation
- **Input:** Perplexity research JSON + Vertical + Owner first name
- **API:** OpenAI API (GPT-4)
- **Prompt:**

```
You are writing the opening line of a cold email. The tone should be:
- Humble and curious (not salesy)
- Specific to the company (not generic)
- Under 25 words
- Shows you actually looked at their business

Company: [Company Name]
Owner: [First Name]
Vertical: [Printing/Homestead]
Company Description: [from Perplexity]
Recent News: [from Perplexity]
Specific Detail: [from Perplexity]

Write ONE icebreaker sentence. Examples of good icebreakers:
- "Saw [Company] handles HP wide-format service across [state] -- keeping those machines running is no joke."
- "Your spring seed collection looks incredible -- your community clearly loves what you're building."
- "Noticed you service Canon plotters for the [city] area -- that's a niche that doesn't get enough credit."

Return ONLY the icebreaker sentence. No quotes, no explanation.
```

- **Output:** Single sentence icebreaker

### Step 4: Write Back to Google Sheet
- **Update fields:**
  - `Icebreaker`: Generated icebreaker sentence
  - `Research Notes`: Full Perplexity research JSON
  - `Status`: Changed from "New" to "Ready to Send"
  - `Personalized Date`: Today's date

---

## Quality Controls

### Icebreaker Validation
Before writing back, check:
1. Length < 25 words (reject if over)
2. Contains company name or specific detail (reject if generic)
3. No salesy language ("amazing", "incredible opportunity", "game-changer")
4. If validation fails: Flag for manual review (Status = "Needs Manual Review")

### Perplexity Research Fallback
If Perplexity returns insufficient data:
1. Try Google search API as backup
2. If still insufficient: Flag for manual research (Status = "Needs Research")
3. Don't generate an icebreaker from bad data -- generic is worse than no email

---

## Manual Personalization Process (First 50 Leads)

While Matthew builds the automation, Mekaiel manually processes leads:

### For Each Lead (~3 min per lead):
1. Visit company website (30s)
2. Check social media / recent posts (30s)
3. Note one specific detail about the company (15s)
4. Open ChatGPT and paste:

```
Write a cold email icebreaker for [First Name] at [Company].
They [what they do]. I noticed [specific detail].
Keep it under 25 words, humble, and specific. No sales language.
```

5. Copy icebreaker to Google Sheet (15s)
6. Set status to "Ready to Send" (5s)

### Time Estimate:
- 25 printing leads x 3 min = 75 min
- 25 homestead leads x 3 min = 75 min
- **Total: ~2.5 hours**

---

## Automation Scale Plan

| Phase | Leads/Day | Method |
|-------|-----------|--------|
| Week 0 | 10-15 | Manual (Mekaiel via ChatGPT) |
| Week 1 | 15-25 | Semi-automated (n8n pipeline with manual QA) |
| Week 2+ | 25-50 | Fully automated (n8n pipeline, spot-check QA) |

---

## n8n Workflow Nodes

```
[Google Sheet Trigger]
    → [Perplexity API Call]
    → [Parse Research JSON]
    → [ChatGPT Icebreaker Call]
    → [Validate Icebreaker]
    → [If Valid: Write Back to Sheet]
    → [If Invalid: Flag for Manual Review]
```

---

## API Costs (Estimated)

| Service | Cost per Lead | Monthly (at 150 leads) |
|---------|--------------|----------------------|
| Perplexity API | ~$0.02 | ~$3 |
| OpenAI GPT-4 | ~$0.05 | ~$7.50 |
| **Total** | **~$0.07** | **~$10.50** |

---

## Testing

- [ ] Run 5 printing leads through pipeline. Verify icebreakers are specific, not generic.
- [ ] Run 5 homestead leads through pipeline. Verify icebreakers are specific, not generic.
- [ ] Verify fallback works when Perplexity returns insufficient data.
- [ ] Verify validation rejects generic icebreakers.
- [ ] Verify Google Sheet is updated correctly (all fields populated, status changed).
- [ ] Compare automated icebreakers to Mekaiel's manual ones -- quality should be equivalent.
