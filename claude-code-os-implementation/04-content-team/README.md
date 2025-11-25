# Content Team (Magnetic Content OS)

## 🎯 Mission
Create high-quality, strategically-aligned content across all channels using specialized AI agents, maintaining brand voice while maximizing production efficiency.

---

## 📊 Department Overview

The Content Team is your AI-powered content creation engine. Instead of spending hours crafting every post, email, or piece of content, you orchestrate a team of specialist agents who handle creation, optimization, and quality control.

**Phase 1 (Current)**: Core 5 Agents - Essential content creation for immediate use
**Phase 2 (Future)**: Full 14+ Agent Team - Complete multi-channel content operation

---

## 🗂️ Department Structure

```
04-content-team/
├── agents/
│   └── prompts/
│       ├── content-director-agent.md       # Orchestrates all content creation
│       ├── social-media-manager-agent.md   # Platform-optimized social content
│       ├── hook-specialist-agent.md        # Attention-grabbing openings
│       ├── email-copywriter-agent.md       # Newsletters & campaigns
│       └── editor-agent.md                 # Final quality control
├── content-templates/
│   ├── social/
│   │   └── linkedin-post-frameworks.md     # 7 proven post structures
│   └── email/
│       └── email-frameworks.md             # 5 email types + formulas
├── workflows/
├── output-management/
│   ├── drafts/
│   ├── review/
│   ├── approved/
│   └── published/
└── linkedin-posts/
    └── week-1-claude-code-os-series.md     # Your first content created!
```

---

## 🤖 The Core 5 Agents

### 1. Content Director 🎯
**Role**: Orchestrator and strategic overseer

**Use When**: You need to create any content and want the system to handle it

**What It Does**:
- Receives your content request
- Validates strategic alignment
- Delegates to appropriate specialist agents
- Coordinates collaboration
- Delivers final compiled output
- Provides publishing recommendations

**Example Request**:
"I need a LinkedIn post about the value of business systems for small business owners. Include a CTA to AriseGroup.ai."

**Agent Location**: `/agents/prompts/content-director-agent.md`

---

### 2. Social Media Manager 📱
**Role**: Platform-optimized social content creator

**Use When**: Creating LinkedIn, Twitter, or social media posts

**What It Does**:
- Crafts platform-specific content
- Optimizes for engagement (likes, comments, shares)
- Maintains brand voice
- Includes appropriate CTAs and hashtags
- Predicts engagement potential

**Specializes In**:
- LinkedIn posts (150-300 words)
- Twitter threads
- Problem-Solution-Value frameworks
- Story arcs
- Listicles and how-tos

**Agent Location**: `/agents/prompts/social-media-manager-agent.md`

---

### 3. Hook Specialist 🎣
**Role**: Attention-grabbing opening creator

**Use When**: You need compelling subject lines, headlines, or post openings

**What It Does**:
- Creates 3-5 hook variations using proven formulas
- Assesses each for curiosity, clarity, pattern interrupt
- Provides A/B test recommendations
- Optimizes for platform (LinkedIn vs Twitter vs Email)

**Hook Formulas**:
1. Curiosity Gap
2. Big Promise
3. Pattern Interrupt
4. Authority Statement
5. Problem Agitation
6. Contrarian View
7. Transformation Story
8. Question Hook
9. Specific Number/Data
10. Direct Benefit

**Agent Location**: `/agents/prompts/hook-specialist-agent.md`

---

### 4. Email Copywriter ✉️
**Role**: High-converting email content creator

**Use When**: Creating newsletters, campaigns, welcome sequences, promotional emails

**What It Does**:
- Writes complete emails with subject lines
- Optimizes for opens, reads, and conversions
- Includes pre-header text
- Creates clear, compelling CTAs
- Provides send time recommendations

**Email Types**:
- Weekly newsletters (nurture)
- Welcome sequences (onboarding)
- Promotional emails (convert)
- Value bombs (pure education)
- Story-based emails (connection)

**Agent Location**: `/agents/prompts/email-copywriter-agent.md`

---

### 5. Editor 📝
**Role**: Final quality control and brand consistency

**Use When**: Content is drafted and needs final review before publishing

**What It Does**:
- Checks technical correctness (grammar, spelling, formatting)
- Ensures clarity and readability
- Verifies brand voice consistency
- Confirms strategic alignment
- Strengthens CTAs
- Approves or requests revisions

**4-Level Edit Process**:
1. Technical Correctness
2. Clarity & Readability
3. Brand Voice
4. Strategic Alignment

**Agent Location**: `/agents/prompts/editor-agent.md`

---

## 🚀 Quick Start Guide

### Creating Your First LinkedIn Post

**Option A: Using Content Director (Recommended)**

1. Open `/agents/prompts/content-director-agent.md`
2. Copy the agent prompt
3. Paste into Claude conversation
4. Request: "Create a LinkedIn post about [topic] for [audience] with CTA to [action]"
5. Content Director will coordinate specialists and deliver final output

**Option B: Direct to Social Media Manager**

1. Open `/agents/prompts/social-media-manager-agent.md`
2. Copy the agent prompt
3. Request your post directly
4. Review and publish

---

### Creating Your First Email Campaign

**Using Email Copywriter**:

1. Open `/agents/prompts/email-copywriter-agent.md`
2. Copy the agent prompt
3. Specify:
   - Email type (newsletter, promotional, etc.)
   - Objective
   - Audience
   - Key message
   - CTA
4. Receive complete email with subject line options

---

### Multi-Agent Workflow (Pro)

For best results, use multiple agents in sequence:

**Example: LinkedIn Post Creation**

1. **Hook Specialist**: "Create 3 hooks for a LinkedIn post about business systems"
   → Receive 3 compelling opening options

2. **Social Media Manager**: "Using Hook Option 2, create a full LinkedIn post using PSV framework, 250 words, CTA to AriseGroup.ai"
   → Receive complete draft

3. **Editor**: "Review this LinkedIn post for brand voice and quality"
   → Receive feedback and approval

4. **Publish**: Post goes live!

---

## 📚 Content Templates

### LinkedIn Post Frameworks

**Location**: `/content-templates/social/linkedin-post-frameworks.md`

**7 Proven Frameworks**:
1. Problem-Solution-Value (PSV) - Best for education
2. Listicle - Best for quick tips
3. Story Arc - Best for personal stories
4. Contrarian Take - Best for thought leadership
5. Quick Win/How-To - Best for actionable advice
6. Question Hook - Best for engagement
7. Data/Statistics Hook - Best for authority

**Also Includes**:
- Writing best practices
- Hook guidelines
- CTA formulas
- Platform-specific tips
- 70-20-10 content mixing strategy

---

### Email Frameworks

**Location**: `/content-templates/email/email-frameworks.md`

**5 Email Types**:
1. Weekly Newsletter - Nurture and educate
2. Welcome Email - First touch
3. Promotional/Offer - Convert
4. Value Bomb - Pure education
5. Story-Based - Build connection

**Also Includes**:
- Subject line formulas
- Pre-header best practices
- Body writing guidelines
- CTA optimization
- Sending best practices
- Performance metrics

---

## 🎯 Content Strategy for AriseGroup.ai

### Brand Voice

**Tone**: Professional yet approachable
- Expert but not elitist
- Confident but not arrogant
- Direct but not harsh
- Helpful but not hand-holding

**Style**: Clear and actionable
- Short sentences for impact
- Concrete over abstract
- Systems-focused
- Data-driven when available
- Military precision without overwhelming jargon

**Values**: Authentic and results-focused
- Honest about challenges
- Transparent about process
- Results over hype
- Systems over motivation

**What to Avoid**:
❌ Overpromising ("transform your life!")
❌ Fake urgency ("Act NOW!")
❌ Vague benefits ("boost productivity")
❌ Corporate jargon
❌ Excessive military terminology

---

### Content Mix (70-20-10 Rule)

**70% Educational/Value**:
- How-to guides
- Framework breakdowns
- System explanations
- Operational insights

**20% Inspirational/Personal**:
- Transformation stories
- Behind-the-scenes
- Lessons learned
- Personal insights

**10% Promotional**:
- Service offers
- Free audits
- Case studies
- CTAs to AriseGroup.ai

---

### Weekly Posting Cadence

**LinkedIn**:
- **Monday**: Thought leadership / Contrarian take
- **Tuesday**: Educational / How-to
- **Wednesday**: Story / Case study
- **Thursday**: Quick tips / Listicle
- **Friday**: Engagement question / Discussion

**Email**:
- **Thursday**: Weekly newsletter (nurture)
- **As needed**: Promotional campaigns

---

## 💡 Usage Examples

### Example 1: Quick LinkedIn Post

**Your Request to Content Director**:
"Create a LinkedIn post about why business owners need productivity tracking, not just gut feelings. Target: small business owners. Include AriseGroup.ai mention. 200-250 words."

**What You Get**:
- Complete LinkedIn post
- 3-5 hashtag recommendations
- Optimal posting time
- Engagement prediction
- Hook variations for A/B testing

---

### Example 2: Email Campaign

**Your Request to Email Copywriter**:
"Write a promotional email for free operations audits. Target: overwhelmed small business owners. Key points: free, 20 minutes, identifies 3 specific improvements. CTA: Book at AriseGroup.ai."

**What You Get**:
- 3 subject line options with performance predictions
- Pre-header text
- Complete email body
- CTA optimization
- Send time recommendations
- A/B test suggestions

---

### Example 3: Content Series

**Your Request to Content Director**:
"Plan a 3-post LinkedIn series on building AI-powered business systems. Each post should stand alone but build on each other."

**What You Get**:
- Strategic series outline
- 3 complete posts (one per day/week)
- Consistent messaging across series
- Publishing schedule
- Engagement hooks for each post

---

## 📈 Performance Optimization

### Track What Works

**For Social Media**:
- Engagement rate by framework
- Best performing hooks
- Optimal post length
- Peak engagement times
- Top performing topics

**For Email**:
- Open rates by subject line formula
- Click-through rates by CTA type
- Best send times
- Segmentation performance

**Use This Data**:
- Inform future content decisions
- Refine agent prompts
- Update templates
- Optimize posting strategy

---

## 🔄 Workflows

### Daily Content Creation (5-15 minutes)

1. **Morning**: Check content calendar
2. **Invoke Agent**: Content Director with request
3. **Review**: Edit provides final check
4. **Schedule**: Add to publishing queue
5. **Post**: Publish at optimal time

### Weekly Content Planning (30 minutes)

1. **Review Performance**: What worked last week?
2. **Plan Topics**: 5 posts for upcoming week
3. **Batch Create**: Use agents to draft all 5
4. **Editor Review**: Quality check all drafts
5. **Schedule**: Queue for daily posting

### Monthly Content Strategy (1 hour)

1. **Performance Analysis**: Review all content metrics
2. **Strategy Adjustment**: What to do more/less of?
3. **Template Updates**: Refine based on learnings
4. **Agent Tuning**: Update prompts with insights
5. **Plan Next Month**: Topics, themes, campaigns

---

## 🚦 Content Standards Checklist

Before publishing any content:

**Strategic**:
- [ ] Aligns with business OBG
- [ ] Serves target audience
- [ ] Fits content strategy
- [ ] Has clear objective

**Quality**:
- [ ] Hook grabs attention
- [ ] Value is clear and specific
- [ ] Examples concrete
- [ ] CTA single and clear
- [ ] Grammar/spelling perfect

**Brand**:
- [ ] Tone matches voice
- [ ] Style consistent
- [ ] Claims honest
- [ ] AriseGroup.ai mention natural

**Technical**:
- [ ] Length appropriate
- [ ] Format optimized
- [ ] Links functional
- [ ] Hashtags relevant

---

## 🔮 Future Expansion (Phase 2)

When ready to scale, add these agents:

**Content Creation**:
- YouTube Specialist (long-form video scripts)
- Blog Writer (SEO-optimized articles)
- Short Content Creator (TikTok/Reels/Shorts)

**Optimization**:
- SEO Optimizer (keyword research, optimization)
- Content Researcher (topic and trend analysis)
- Title Optimizer (headline creation)
- Thumbnail Designer (visual ideation)

**Strategy & Analytics**:
- Content Strategist (calendar and planning)
- Analytics Reviewer (performance analysis)

---

## 💡 Pro Tips

### 1. Start with Content Director
Let it coordinate specialists. More efficient than managing each agent manually.

### 2. Save Your Best Hooks
Build a swipe file of high-performing hooks for future inspiration.

### 3. Batch Create Content
Create multiple pieces at once for efficiency. Queue and schedule for consistent publishing.

### 4. A/B Test Everything
Use Hook Specialist variations to test what resonates with your audience.

### 5. Track and Iterate
Use performance data to refine your approach, not just gut feelings.

### 6. Maintain Voice Consistency
Run everything through Editor to ensure brand voice stays consistent.

### 7. Don't Over-Automate
Agents create drafts. You add the unique insights and personal touch that make it authentic.

---

## 🎯 Success Metrics

The Content Team is working well when:

✅ **Consistent Output**: 5+ posts/week without burnout
✅ **Quality Maintained**: All content passes Editor standards
✅ **Engagement Growing**: Increasing likes, comments, shares over time
✅ **Brand Recognition**: Audience recognizes your voice
✅ **Strategic Alignment**: Content advances business objectives
✅ **Time Savings**: Content creation takes minutes, not hours
✅ **Lead Generation**: Content drives traffic and conversions

---

## 📖 Further Reading

- **Implementation Plan**: `implementation-plan.md` (full 14+ agent vision)
- **Executive Office**: `/01-executive-office/README.md` (strategic planning)
- **Operations**: `/02-operations/README.md` (productivity tracking)

---

*"AI-powered content creation requires your touch, your thinking. It's always a collaboration between you, the expert with vision, and your team of AI agents."*

*Content Team - Claude Code OS*
*Version 1.0 (Phase 1: Core 5) - Built November 24, 2025*
