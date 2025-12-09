# AI Audit Interview Best Practices
## Master Guide for Discovery Interviews

**Purpose**: Tactical guide for conducting high-quality stakeholder and end-user interviews that uncover real automation opportunities and build compelling business cases.

**Audience**: AriseGroup.ai consultants conducting comprehensive AI audits

**Related Resources**:
- `stakeholder-interview-questions.md` - Leadership interview template
- `end-user-interview-questions.md` - Frontline staff interview template

---

## Table of Contents

1. [Pre-Interview Preparation](#pre-interview-preparation)
2. [Interview Execution](#interview-execution)
3. [Post-Interview Analysis](#post-interview-analysis)
4. [Interview Planning & Scheduling](#interview-planning--scheduling)
5. [Recording & Transcription](#recording--transcription)
6. [Common Mistakes & How to Avoid Them](#common-mistakes--how-to-avoid-them)
7. [Advanced Techniques](#advanced-techniques)
8. [Quality Checklist](#quality-checklist)

---

## Pre-Interview Preparation

### 1. Review Available Materials (30-60 minutes before interview)

**Must Review:**
- [ ] Sales handoff packet
- [ ] Discovery call notes and recording
- [ ] Client intake form
- [ ] Company website (About, Team, Services pages)
- [ ] Interviewee's LinkedIn profile
- [ ] Any previous interviews with this client

**Why this matters**: Asking questions they already answered wastes time and makes you look unprepared. Use the interview to go deeper, not to get basics.

---

### 2. Customize Your Question Template

**Don't use generic questions.** Adapt based on:

- **Role**: CEO gets different questions than a customer service rep
- **Industry**: SaaS company vs. manufacturing vs. professional services
- **Context**: If sales already identified a pain point, dig deeper on that

**Example Customization:**

Generic: "What tools does your team use?"

Customized for SaaS Customer Success Manager: "I saw you're using Intercom and Zendesk. How do those two systems work together? Do you find yourself switching between them?"

---

### 3. Set Up Recording Tools

**Recommended Stack:**
- **Fireflies.ai** - Auto-join Zoom/Meet, transcribe, extract action items
- **Otter.ai** - Alternative with good accuracy
- **Zoom native recording** - Backup option
- **Pen and paper** - ALWAYS have this as ultimate backup

**Test Checklist:**
- [ ] Tool installed and logged in
- [ ] Test recording in a practice call
- [ ] Verify transcription accuracy
- [ ] Check audio quality
- [ ] Know how to access and share recordings

**Pro Tip**: Always have TWO recording methods running. Tech fails.

---

### 4. Prepare Your Environment

**Physical Setup:**
- [ ] Quiet room with no interruptions
- [ ] Good lighting (if video)
- [ ] Quality microphone (even cheap ones are better than laptop mics)
- [ ] Fully charged laptop
- [ ] Charger plugged in (for longer sessions)
- [ ] Water nearby
- [ ] Notebook and pen ready

**Digital Setup:**
- [ ] Close unnecessary applications
- [ ] Disable notifications (Slack, email, everything)
- [ ] Have audit.json open in another window
- [ ] Have interview template open
- [ ] Test internet connection

---

### 5. Mental Preparation

**Your Mindset Going In:**
- ✅ I'm here to listen and learn, not to pitch
- ✅ Every detail matters, even boring ones
- ✅ There are no stupid questions
- ✅ Silence is okay - let them think
- ✅ I'm an inefficiency detective

**Red Flag Mindset:**
- ❌ I already know what the problem is
- ❌ I need to impress them with my knowledge
- ❌ We need to move fast, skip the details
- ❌ This person's job is simple, won't take long

---

## Interview Execution

### The 80/20 Rule (CRITICAL)

**You should talk 20% of the time. They should talk 80%.**

**Your 20% is for:**
- Asking questions
- Clarifying what you heard
- Minimal acknowledgment ("Got it", "That makes sense", "Interesting")
- Summarizing to confirm understanding

**Their 80% is for:**
- Describing their work
- Explaining processes
- Sharing frustrations
- Telling stories
- Showing you how things work

**How to Track This:**
Set a timer for the interview. If you find yourself talking for more than 2 minutes straight, you're doing it wrong.

---

### Opening the Interview (First 3 Minutes)

**Critical Goals:**
1. Build rapport
2. Set expectations
3. Get permission to record
4. Make them comfortable being honest

**Script Template:**

"[Name], thank you so much for making time today. I really appreciate it.

The goal of our conversation is to understand [your role/your team's processes] so we can identify the best opportunities to make your work easier and more efficient.

I'm going to ask questions about your daily tasks, the tools you use, and what makes your job easier or harder. There are no right or wrong answers - I'm genuinely here to learn from you.

This should take about [30-45] minutes. I might ask you to show me your screen for some things if that's okay - it helps me understand much better than just talking about it.

Is it okay if I record this conversation so I can focus on what you're saying instead of frantically taking notes? The recording is just for my reference and won't be shared outside our team."

**Wait for explicit "yes" on recording before proceeding.**

---

### The "Why?" Technique

**Rule**: Ask "Why?" at least 3 times for every major pain point.

**Why it works**: Surface problems are rarely root problems. You need to dig.

**Example:**

**Them**: "We manually enter data from emails into spreadsheets"

**You**: "Why is it done that way?"

**Them**: "Because our CRM doesn't integrate with the website form"

**You**: "Why doesn't it integrate?"

**Them**: "We use an old CRM that doesn't have an API"

**You**: "Why haven't you switched?"

**Them**: "The sales team is comfortable with it and doesn't want to change"

**You**: "Why is the sales team resistant to change?"

**Them**: "They tried a new CRM 2 years ago and it was a disaster. Lost data, bad training, lots of complaints"

← **NOW you know the real blocker**: Change management and past bad experience, not just "old CRM"

**When to Stop:**
- When you've reached the root cause
- When they say "I don't know" genuinely (then ask who would know)
- When you've asked 5 "whys" and still haven't hit bottom (rare)

---

### Quantification (CRITICAL FOR ROI)

**Rule**: Every pain point must have numbers attached.

**The Questions to Always Ask:**

1. **Frequency**: "How often does this happen?"
   - Per hour? Per day? Per week? Per month?
   - Be specific: "About how many times per week?"

2. **Duration**: "About how long does this take?"
   - Minutes? Hours? Days?
   - For each instance? Total per week?

3. **Scope**: "How many people are affected by this?"
   - Just you? Your whole team? Multiple departments?

4. **Impact**: "What's the cost when this goes wrong?"
   - Revenue lost? Time wasted? Customer frustration?

**Example Quantification:**

❌ **Vague**:
- "Data entry takes a while"
- "It happens pretty often"
- "Several people deal with it"
- "It's annoying"

✅ **Quantified**:
- "Data entry takes about 15 minutes per lead"
- "We process 50-100 leads per week"
- "Three people on our team do this, so that's 15 min × 75 leads × 3 people = ~56 hours per week"
- "We miss about 10 leads per week due to slow response time, at ~$3,000 each, that's $30,000 in lost revenue monthly"

**Pro Tip**: Do the math WITH them on the call. "So that's 15 minutes per lead, times 75 leads, times 3 people... that's about 56 hours per week your team spends on data entry. Does that sound about right?"

This accomplishes two things:
1. They validate the number
2. They realize the magnitude (often for the first time)

---

### Active Listening Techniques

**1. Acknowledge Without Interrupting**
- "Mm-hmm"
- "I see"
- "Got it"
- Nodding

**2. Reflect Back**
- "So what I'm hearing is [summary]. Is that right?"
- "It sounds like [problem] is causing [impact]"
- "Let me make sure I understand: [repeat their point]"

**3. Validate Their Experience**
- "That sounds frustrating"
- "I can see why that would be challenging"
- "That makes total sense given [context]"

**What NOT to Do:**
- ❌ "Oh yeah, I've seen that before" (makes it about you)
- ❌ "That's terrible!" (too dramatic, makes them defensive)
- ❌ "Have you tried [solution]?" (NOT the time)
- ❌ "Let me tell you about..." (stop talking)

---

### Note-Taking Strategy

**Even if you're recording, take notes. Here's why:**
- Tech fails (it will eventually)
- Highlights key moments for later
- Shows you're engaged
- Easier to find important parts later

**What to Write:**

✅ **DO capture**:
- Exact quotes (mark with quotation marks)
- Numbers and time estimates
- Tools and systems mentioned
- Names of other people/teams mentioned
- Pain point descriptions
- Workarounds they've created
- Your follow-up questions

❌ **DON'T try to**:
- Write everything word-for-word (you have recording)
- Make it pretty (just get it down)
- Organize as you go (analyze later)

**Notation System Example:**
- `"quote"` = Exact quote
- `!!!` = Major pain point
- `$$$` = Revenue impact mentioned
- `⏱️` = Time cost mentioned
- `→` = Process flow
- `?` = Follow-up question needed

---

### Handling Difficult Situations

**Situation 1: They're Too Busy / Rushing**

❌ Don't: Rush through and get surface-level info

✅ Do: "I totally understand you're busy. Would it be better to reschedule when you have more time? I want to make sure we really understand [topic] so we can identify the best solutions for you."

**Situation 2: They're Vague or Don't Know Numbers**

❌ Don't: Accept "I don't know" and move on

✅ Do: "No problem, let's estimate together. Think about last week - about how many times did you [do task]? Okay, and each time took about how long? So roughly [X] hours per week - does that feel about right?"

**Situation 3: They're Pitching Their Own Solution**

❌ Don't: Commit to their solution or argue

✅ Do: "That's an interesting idea. Help me understand the problem you're trying to solve with that. Walk me through why that would help."

(Often their solution isn't the right one, but the problem they identified is real)

**Situation 4: They're Defensive About Current Processes**

❌ Don't: Criticize or imply they're doing it wrong

✅ Do: "The way you've set this up makes total sense given [constraint]. I'm curious - if those constraints were removed, what would you change?"

**Situation 5: They're Going Off-Topic**

❌ Don't: Let them ramble for 20 minutes

✅ Do: "That's really interesting. I want to make sure we have time to cover [main topic], so let's circle back to that. We were talking about [process]..."

---

### Screen Sharing (POWERFUL TECHNIQUE)

**Why Screen Sharing Reveals Gold:**
- People forget steps when just talking
- You see the actual UI, not their description
- You spot inefficiencies they don't notice
- You see workarounds they don't think to mention

**How to Ask:**

"This is super helpful. Would you be comfortable sharing your screen and just walking me through exactly how you do [task]? I learn much better by seeing it than just hearing about it."

**What to Watch For:**
- ✅ Switching between multiple systems
- ✅ Copy-pasting data
- ✅ Manual data entry
- ✅ Looking up information in multiple places
- ✅ Workarounds (separate spreadsheets, notes, etc.)
- ✅ Steps they didn't mention
- ✅ UI frustrations (clicking around, searching, waiting)

**Pro Tip**: Ask them to do the task for real, not just show you. "Do you have a real [lead/ticket/task] you could process while I watch? That way I see the actual process, not just the ideal process."

---

### Closing the Interview

**1. Summarize (Critical)**

"Let me make sure I understood correctly. It sounds like:
1. [Main finding 1]
2. [Main finding 2]
3. [Main finding 3]

Did I capture that right? What did I miss?"

**2. Validate Numbers**

"You mentioned spending about [X] hours per week on [task] - is that a typical week or high/low?"

**3. Get Referrals**

"This has been incredibly helpful. Who else should I definitely talk to? Who would give me the best perspective on [specific process]?"

**4. Set Next Steps**

"Here's what happens next:
1. I'll be talking to [X more people]
2. We'll analyze everything and identify the top opportunities
3. We'll present our findings on [date]
4. Can I follow up if I have any quick clarifying questions?"

**5. Thank Them Genuinely**

"Thank you so much for being so open and detailed. This is exactly what we need to find the best ways to make your work easier and free up your time for higher-value work."

---

## Post-Interview Analysis

### Immediate Actions (Within 30 Minutes)

**Why 30 minutes?** Your memory is fresh. Details fade fast.

**What to Do:**

1. **Review the recording/transcript** (at 1.5x speed is fine)
2. **Add details to your notes** while you remember
3. **Extract key quotes** (copy exact wording)
4. **Quantify everything** (if they said "a few hours", go back and get a number)
5. **List all pain points** with metrics
6. **List all tools mentioned**
7. **Note follow-up questions** needed

---

### Same-Day Actions

**1. Update audit.json**

Add complete interview data to `discovery_interviews` section:

```json
{
  "stakeholder_interviews": [
    {
      "interviewee_name": "Jane Smith",
      "role": "VP of Sales",
      "date": "2025-01-15",
      "duration_minutes": 42,
      "interview_type": "stakeholder",
      "key_findings": [
        "Team spends 15+ hours/week on manual data entry",
        "CRM doesn't integrate with website forms",
        "Losing ~10 leads/week due to slow response time",
        "Past CRM migration failed due to poor change management"
      ],
      "pain_points_mentioned": [
        {
          "description": "Manual email-to-CRM data entry",
          "frequency": "75 leads per week",
          "time_cost": "56 hours per week (team of 3)",
          "impact": "high",
          "revenue_impact": "$30,000/month in lost leads"
        }
      ],
      "tools_mentioned": ["Old CRM", "Email", "Google Sheets", "Website forms"],
      "powerful_quotes": [
        "We're spending half our time on data entry instead of actually selling",
        "We lose leads every day because we can't respond fast enough"
      ],
      "transcript_link": "link-to-fireflies",
      "notes": "Very open to automation. Main concern is adoption after past failed CRM migration."
    }
  ]
}
```

**2. Cross-Reference with Other Interviews**

Look for:
- **Patterns**: Multiple people mentioning same pain point → high priority
- **Gaps**: Stakeholder view vs. end-user reality
- **Contradictions**: Why do they see it differently?
- **Opportunities**: Where do inefficiencies cluster?

**3. Map to Ops Canvas**

Categorize processes mentioned:
- **Acquisition Engine**: How they find and sign customers
- **Delivery Engine**: How they deliver product/service
- **Support Engine**: How they handle post-sale issues

**4. Flag Quick Win Opportunities**

Look for:
- Manual data transfer between systems
- Repetitive tasks done 10+ times per week
- Errors happening >5% of the time
- Waiting for information/approvals
- Manual reporting that could be automated

---

### Analysis Checklist

Before moving to next interview, verify you have:

- [ ] **Complete process map** for critical workflows mentioned
- [ ] **Quantified time costs** (hours per week on each task)
- [ ] **Tool stack documented** (what they actually use)
- [ ] **Pain points ranked** by frequency and impact
- [ ] **Revenue/cost impact** calculated where mentioned
- [ ] **Quotes extracted** for presentation
- [ ] **audit.json updated** with all data
- [ ] **Follow-up questions** noted
- [ ] **Next interview targets** identified

---

## Interview Planning & Scheduling

### How Many Interviews Do You Need?

| Company Size | Recommended Interviews | Stakeholder:End-User Ratio |
|--------------|----------------------|----------------------------|
| 1-10 employees | 2-3 interviews | 1:1-2 |
| 10-50 employees | 3-5 interviews | 1:2-3 |
| 50-200 employees | 5-10 interviews | 2:3-7 |
| 200+ employees | 10-15 interviews | 3:7-10 |

**Always interview**:
- At least 1 stakeholder (decision maker)
- At least 2 end-users (people doing the daily work)
- Mix of roles (not all from same department)

---

### Who to Interview

**Stakeholders (Leadership Perspective)**:
- C-level (CEO, CTO, COO)
- VPs and Directors
- Department Heads
- Team Managers

**End-Users (Operational Reality)**:
- Individual contributors
- Frontline staff
- Specialists and coordinators
- Customer-facing roles

**Power Users (Hidden Gold)**:
- The person everyone goes to for help
- The person who knows all the workarounds
- The person who's been there longest
- The person who complains most about current process

---

### Scheduling Strategy

**Timing:**
- **30-45 minutes** per interview (not longer - quality drops)
- **Leave 15-minute buffer** between interviews
- **Batch interviews** into 1-2 days if possible (stay in context)
- **Morning interviews** tend to be better (people are fresher)

**Ask for screen sharing up front** in calendar invite:
"I may ask you to share your screen and walk me through how you do [task] - that helps me understand much better than just talking about it."

**Calendar Invite Template:**

```
Subject: AI Audit Interview - [Company Name]

Hi [Name],

As part of the AI audit for [Company], I'd love to learn about your day-to-day work and the processes you manage.

The goal is to understand what's working well and where there might be opportunities to make your work easier and more efficient through automation.

This will take about 30-45 minutes. I may ask you to share your screen and show me how you do certain tasks - that helps me understand much better than just talking about it.

[Calendar Link]

Looking forward to chatting!

[Your Name]
```

---

## Recording & Transcription

### Recording Best Practices

**1. Always Get Explicit Permission**

"Is it okay if I record this conversation so I can focus on what you're saying instead of taking notes? The recording is just for my reference and won't be shared outside our audit team."

Wait for clear "yes" before starting.

**2. Have Redundancy**

Run two recording methods:
- Primary: Fireflies.ai or Otter.ai (auto-transcription)
- Backup: Zoom/Meet native recording OR voice recorder app

**3. Test Everything**

Before each interview:
- Check recording tool is active
- Verify audio input source
- Test with a quick recording and playback

**4. Store Securely**

- Save recordings to client folder immediately
- Add link to audit.json
- Set appropriate permissions (client data is confidential)
- Delete from recording tool after download (if using third party)

---

### Transcription Workflow

**Option 1: Automated (Recommended)**
- Fireflies.ai - Joins calls automatically, transcribes, extracts topics
- Otter.ai - Similar functionality, good accuracy
- Rev.ai - API-based for custom workflows

**Option 2: Manual**
- Use if discussion highly confidential
- Time-consuming but ensures accuracy
- Can use transcription service (Rev.com, etc.)

**What to Do With Transcripts:**

1. **Review for accuracy** (AI transcription makes mistakes)
2. **Extract key quotes** (copy exact wording to notes)
3. **Highlight pain points** mentioned
4. **Note all numbers** (time, cost, frequency)
5. **Tag by topic** (process mapping, tools, frustrations)
6. **Save to client folder** with naming convention:
   - `interview-[date]-[name]-[role]-transcript.txt`

---

## Common Mistakes & How to Avoid Them

### Mistake 1: Only Interviewing Leadership

**Why it's bad**: Leaders often don't know the day-to-day operational reality.

**Example**:
- CEO says: "We have a CRM and it works great"
- Reality: Sales team maintains separate spreadsheets because CRM is missing fields

**Fix**: Always interview end-users who do the actual work.

---

### Mistake 2: Accepting Vague Answers

**Why it's bad**: You can't build an ROI case on "takes a while" or "happens sometimes."

**Example**:
- ❌ "Lead response takes a while" → Can't calculate savings
- ✅ "Lead response averages 4-6 hours" → Can calculate impact

**Fix**: Push for numbers. If they don't know, estimate together.

---

### Mistake 3: Talking Too Much

**Why it's bad**: You learn nothing when you're talking.

**Red Flags**:
- You're explaining how AI works
- You're telling stories about other clients
- You're pitching solutions
- You've talked for more than 2 minutes straight

**Fix**: Track your talk time. Aim for 80/20 (them/you).

---

### Mistake 4: Not Recording

**Why it's bad**:
- You'll miss details
- You'll misremember
- You can't reference exact quotes later

**Excuses people make**:
- "I have a good memory" → No you don't, nobody does
- "I'm good at notes" → You can't write and listen fully
- "They won't want to be recorded" → 95% say yes when you explain why

**Fix**: Always record. If they say no (rare), take extensive notes and confirm key points with them via email after.

---

### Mistake 5: Not Quantifying Time and Impact

**Why it's bad**: "Sounds frustrating" doesn't sell. "$30K/month in lost revenue" does.

**Common Missed Opportunities**:
- Not asking "How many times per week?"
- Not asking "About how long does that take?"
- Not calculating total time impact
- Not connecting time to money

**Fix**: For every pain point, get:
- Frequency (how often)
- Duration (how long)
- Scope (how many people)
- Impact (cost/revenue/customer experience)

---

### Mistake 6: Skipping "Boring" or "Obvious" Processes

**Why it's bad**: Boring = repetitive = high automation ROI.

**Example**:
- "I just copy data from email to the CRM" ← BORING
- But 50 times per week × 10 minutes = 8 hours per week = $20K/year in labor cost
- Plus 15% error rate = rework and lost leads
- **Easy automation with huge ROI**

**Fix**: The more boring and repetitive, the MORE questions you ask.

---

### Mistake 7: Assuming Stakeholder Knows Reality

**Why it's bad**: There's often a massive gap between what leadership thinks happens and what actually happens.

**Example**:
- **Stakeholder**: "The team uses our CRM for everything"
- **End-user reality**: "I use CRM for the basics, but I have 3 spreadsheets for the actual work because CRM doesn't do what I need"

**Fix**: Interview both stakeholders AND end-users. The gap between their answers is where opportunities hide.

---

### Mistake 8: Not Asking to See Their Screen

**Why it's bad**: People forget steps when just talking about their work.

**What You Miss**:
- Hidden manual steps
- Switching between 5 different tools
- Copy-paste operations they don't even think about anymore
- Workarounds they've created

**Fix**: "Can you share your screen and just walk me through how you do this? I learn way better by seeing it."

---

### Mistake 9: Suggesting Solutions During Interview

**Why it's bad**:
- Stops them from sharing more problems
- Makes them defensive ("why didn't we think of that")
- You don't have full context yet to suggest right solution

**Example**:
- Them: "We manually copy data between systems"
- You: "Oh, we could just automate that with Zapier!"
- Them: "Oh, okay" ← Conversation dead, you missed deeper issues

**Better**:
- Them: "We manually copy data between systems"
- You: "Tell me more about that. Which systems? How often? What happens if there's an error?"
- Them: [Reveals 5 more pain points you wouldn't have found]

**Fix**: Save solutions for later. Right now, just be curious.

---

### Mistake 10: Not Following Up When Something Sounds Weird

**Why it's bad**: Weird = inefficiency you don't understand yet.

**Example**:
- Them: "We email ourselves a copy of the report, download it, then upload it to the shared drive"
- You: "Oh, okay" ← MISSED OPPORTUNITY
- Better: "Wait, why do you email yourself? Is there no direct way to save to the drive?"

**Fix**: When a process sounds convoluted, dig deeper. There's usually a technical limitation or missing integration hiding there.

---

## Advanced Techniques

### The Silence Technique

**How it works**: After they answer, don't immediately ask next question. Wait 3-5 seconds.

**Why it works**: Most people are uncomfortable with silence and will fill it - often with the REAL answer or additional details.

**Example**:
- You: "What's the most frustrating part of your job?"
- Them: "Oh, probably the reporting"
- You: [Silent for 4 seconds]
- Them: "Actually, it's not even the reporting itself, it's that I have to pull data from 5 different systems and then manually reconcile it all. That takes hours every week and I'm terrified of making a mistake."

← **The real pain came AFTER the silence**

---

### The "Last Time" Technique

**How it works**: Ask for specific recent example instead of general description.

**Why it works**: People describe ideal process, not real process. Recent examples reveal reality.

**Example**:
- ❌ "How do you onboard a client?"
- ✅ "Tell me about the last client you onboarded. What happened?"

They'll describe actual steps, including the workarounds and problems.

---

### The Math-on-the-Call Technique

**How it works**: Calculate the impact while you're on the call with them.

**Why it works**:
1. They validate your numbers in real-time
2. They see the magnitude (often for first time)
3. Creates urgency and buy-in

**Example**:

You: "So you're saying you spend about 15 minutes per lead on data entry?"
Them: "Yeah, about that"
You: "And you process about 75 leads per week?"
Them: "Yep"
You: "And there are 3 people on your team doing this?"
Them: "Right"
You: "So that's 15 minutes times 75 leads times 3 people... that's about 3,375 minutes per week, which is about 56 hours per week your team spends on data entry. Does that sound about right?"
Them: "Wow... I never did the math. That's more than a full-time employee just doing data entry."
You: "Exactly. And at an average salary of $50,000, that's about $50K per year in labor cost just for data entry that could potentially be automated."
Them: [Now deeply interested in automation]

---

### The "Show Me" Technique

**How it works**: Don't just ask them to describe - ask them to show you on their screen.

**Why it works**: Reveals steps they forget to mention, UI issues, workarounds, inefficiencies.

**Example**:
- ❌ "How do you create a client report?"
- ✅ "Can you share your screen and actually create a report while I watch? I'll see it much better than if you just describe it."

---

### The "What Else?" Technique

**How it works**: After they answer, ask "What else?" or "Anything else?"

**Why it works**: First answer is top-of-mind. Real issues often come on 2nd or 3rd "what else?"

**Example**:

You: "What are the biggest challenges you're facing?"
Them: "Probably keeping up with all the leads coming in"
You: "What else?"
Them: "Oh, and the CRM is really slow"
You: "What else?"
Them: "Well, we also lose a lot of time because the CRM and email don't sync, so we're constantly copying data back and forth"

← **The REAL issue came on the 3rd "what else?"**

---

### The "Magic Wand" Technique

**How it works**: "If you had a magic wand and could change one thing overnight, what would it be?"

**Why it works**: Bypasses constraints and reveals their true priority.

**What you learn**:
- What they think is most important
- What they wish existed
- What they'd be willing to invest in

---

### The "Impact Chain" Technique

**How it works**: For each pain point, follow the chain: Problem → Impact → Cost

**Example**:

Problem: "We can't respond to leads fast enough"
↓
Impact: "What's the impact of slow response?"
→ "We lose leads to competitors"
↓
Cost: "About how many leads do you lose per month?"
→ "Probably 10"
↓
"What's the average value of those deals?"
→ "$3,000"
↓
**Result**: "$30,000 per month in lost revenue due to slow lead response" ← THIS is what sells

---

## Quality Checklist

### Before Each Interview

- [ ] Reviewed all available materials about the client
- [ ] Reviewed any previous interviews with this client
- [ ] Customized question template for this specific person
- [ ] Recording tools tested and ready
- [ ] Backup recording method ready
- [ ] Quiet environment confirmed
- [ ] Notifications disabled
- [ ] audit.json open and ready to update
- [ ] Permission to record confirmed in calendar invite

---

### During Each Interview

- [ ] Got explicit permission to record
- [ ] Followed 80/20 rule (they talked 80%)
- [ ] Asked "Why?" at least 3 times for major pain points
- [ ] Quantified all pain points (time, frequency, impact)
- [ ] Captured exact quotes
- [ ] Asked to see their screen for key processes
- [ ] Used silence to let them elaborate
- [ ] Asked for specific recent examples
- [ ] Calculated impact on the call with them
- [ ] Summarized understanding before closing
- [ ] Got referrals to other people to interview

---

### After Each Interview

- [ ] Reviewed recording within 30 minutes
- [ ] Added detailed notes while memory fresh
- [ ] Extracted all key quotes (exact wording)
- [ ] Quantified all pain points
- [ ] Listed all tools/systems mentioned
- [ ] Updated audit.json with complete interview data
- [ ] Cross-referenced with other interviews
- [ ] Identified 3-5 automation opportunities
- [ ] Noted follow-up questions needed
- [ ] Saved recording and transcript to client folder
- [ ] Scheduled next interview (if needed)

---

### Interview Quality Self-Assessment

**Rate yourself on these after each interview (1-5 scale):**

- [ ] I listened more than I talked (4-5 = good)
- [ ] I got specific numbers for time/cost/frequency (4-5 = good)
- [ ] I saw them work on screen (4-5 = ideal, 3 = acceptable)
- [ ] I understand the root cause of their top 3 pain points (4-5 = good)
- [ ] I can calculate ROI for at least 2 opportunities from this interview (4-5 = good)
- [ ] I have powerful quotes for the presentation (4-5 = good)
- [ ] They seemed comfortable and opened up (4-5 = good)

**If you scored below 3 on multiple items, you need more practice or a follow-up interview.**

---

## Summary: The Interview Excellence Framework

1. **PREPARE** - Review materials, customize questions, test tech
2. **LISTEN** - 80/20 rule, stay curious, resist solving
3. **QUANTIFY** - Numbers for everything (time, cost, frequency)
4. **DIG** - Ask "Why?" 3x, ask "What else?", use silence
5. **SHOW** - Get them to share screen and walk through
6. **CAPTURE** - Record, take notes, extract quotes
7. **ANALYZE** - Update audit.json same day while fresh
8. **REPEAT** - Patterns across interviews = opportunities

**The best interviews feel like conversations, not interrogations.**

**The best consultants make interviewees feel heard, not judged.**

**The best opportunities come from the "boring" repetitive tasks people don't think to mention.**

---

**Related Resources**:
- `stakeholder-interview-questions.md` - Question template for leadership
- `end-user-interview-questions.md` - Question template for frontline staff
- `opportunity-validation-workshop.md` - How to validate findings with stakeholders
- `roi-calculation-methodology.md` - How to turn interview insights into ROI cases

---

**Document Version**: 1.0
**Last Updated**: 2025-12-09
**Owner**: AriseGroup.ai Audit Team
