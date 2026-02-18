# How to Use Claude System Prompts for Your AI Agency

## What Are System Prompts?

System prompts are the **instructions that tell Claude how to behave**. They're like an employee handbook - they define personality, capabilities, rules, and boundaries. When you build AI solutions for clients, you're essentially writing custom system prompts.

---

## The Anatomy of a Claude System Prompt

After analyzing the Claude Opus 4.5 prompt, here are the **key structural patterns** you can use:

### 1. **XML Tags for Organization**
Anthropic uses XML-style tags to organize instructions into clear sections:

```xml
<citation_instructions>
  Rules for how to cite sources...
</citation_instructions>

<search_instructions>
  When and how to search the web...
</search_instructions>

<tone_and_formatting>
  How to write and respond...
</tone_and_formatting>
```

**Why this matters for your agency:**
When building agents for clients, use this same structure. It makes prompts:
- Easier to maintain and update
- Clearer for the AI to follow
- More organized for debugging

---

### 2. **Behavioral Sections You Should Include**

Based on Claude's official prompts, here are the key sections to include in your client prompts:

| Section | Purpose | Example Use |
|---------|---------|-------------|
| `<role>` | Define who/what the AI is | "You are a sales assistant for [Company]" |
| `<capabilities>` | What tools/actions it can take | "You can search products, check inventory..." |
| `<tone_and_formatting>` | How to communicate | "Be professional but friendly, avoid jargon" |
| `<boundaries>` | What it can't/won't do | "Never discuss competitor pricing" |
| `<examples>` | Show correct behavior | Sample conversations |
| `<error_handling>` | What to do when stuck | "If unsure, ask for clarification" |

---

### 3. **The Search/Tool Pattern**

Claude's prompts have detailed instructions for when to use tools vs. answer directly:

```
IF info is stable (rarely changes) → answer directly
ELSE IF terms/entities unknown → search immediately
ELSE IF info changes frequently → search
ELSE → answer directly, offer to search
```

**For your agency:** Create similar decision trees for your client's AI agents. For example:
- When should the bot escalate to a human?
- When should it check the database vs. use cached info?
- When should it ask for clarification vs. make assumptions?

---

### 4. **Safety and Compliance Patterns**

Claude has extensive safety sections including:

- **Copyright compliance** - Never reproduce 15+ words from sources
- **Harmful content filtering** - Refuse certain requests
- **User wellbeing** - Watch for signs of distress
- **Privacy protection** - Never identify faces, protect personal data

**For your agency:** Include compliance sections relevant to your client's industry:
- HIPAA for healthcare
- FINRA for financial services
- GDPR for EU customers
- Industry-specific regulations

---

## Practical Template for Client Agents

Here's a starter template based on Claude's patterns:

```xml
<agent_identity>
You are [Agent Name], an AI assistant for [Company Name].
Your role is to [primary function].
</agent_identity>

<capabilities>
You can:
- [Capability 1]
- [Capability 2]
- [Capability 3]

You have access to these tools:
- [Tool 1]: [Description]
- [Tool 2]: [Description]
</capabilities>

<communication_style>
Tone: [Professional/Friendly/Technical/etc.]
Format: [Bullet points/Prose/Structured/etc.]
Length: [Concise/Detailed/Adaptive]

Do:
- [Positive behavior 1]
- [Positive behavior 2]

Don't:
- [Behavior to avoid 1]
- [Behavior to avoid 2]
</communication_style>

<decision_logic>
When user asks about [Topic A]:
→ [Action to take]

When user asks about [Topic B]:
→ [Action to take]

When uncertain:
→ [Fallback behavior]
</decision_logic>

<boundaries>
Never:
- [Hard boundary 1]
- [Hard boundary 2]

Always escalate when:
- [Escalation trigger 1]
- [Escalation trigger 2]
</boundaries>

<examples>
<example>
User: [Sample input]
Agent: [Ideal response]
</example>
</examples>
```

---

## Key Takeaways for Your Agency

1. **Structure matters** - Use XML tags to organize complex prompts
2. **Be explicit** - Don't assume the AI knows what you want
3. **Include examples** - Show, don't just tell
4. **Plan for edge cases** - Define fallback behaviors
5. **Add safety rails** - Include compliance and boundaries
6. **Test iteratively** - Refine based on real conversations

---

## Files in This Folder

| File | Best For |
|------|----------|
| `claude-opus-4.5` | Understanding premium/advanced agent design |
| `claude-sonnet-4.md` | Standard production agent patterns |
| `claude-4.5-sonnet.md` | Latest improvements and patterns |
| `claude-code.md` | Coding/technical assistant design |
| `claude-in-chrome.md` | Browser automation and web tasks |

---

## Next Steps

1. Read through `claude-opus-4.5` to see the full prompt structure
2. Identify patterns relevant to your client use cases
3. Create your own template library based on these patterns
4. Test and iterate with real conversations

The prompts in this folder are your reference library - use them to understand what works and why.
