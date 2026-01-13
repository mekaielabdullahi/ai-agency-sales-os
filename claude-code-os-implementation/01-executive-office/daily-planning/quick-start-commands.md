# Executive Office - Daily Planning Quick Start

## Instant Commands

### 1. Generate Today's Plan (Basic)
```bash
# Minimal input - let the system figure it out
"Generate my daily roadmap for today"
```

### 2. Generate with Context
```bash
# Provide yesterday's status and today's priorities
"Generate my daily roadmap. Yesterday: Completed API docs but not deployment. Today: Client demo at 2 PM. OBG: Scale to 100 customers."
```

### 3. Generate from Context File
```bash
# Use prepared context file
"Generate my daily roadmap using the context in today's planning file"
```

### 4. Quick Adjustment
```bash
# Adjust existing plan
"Move [task] to Tier 1, it's now urgent"
"Add [new task] to today's plan, it's blocking the team"
"My energy is low today, adjust the plan accordingly"
```

## Daily Planning Workflow (Mentor-Aligned)

### Morning Routine (Total: 5 minutes)

#### Step 1: Prepare Context (1 minute)
```markdown
Yesterday status: [2-3 bullet points]
Today's TOP 2-3: [ONLY the most important]
Today's NO list: [What I'm NOT doing]
Open loops to close: [What ends today]
Today's fixed: [meetings/calls]
Energy level: [high/medium/low]
```

#### Step 2: Generate Plan (1 minute)
```bash
"Generate my daily roadmap with this context: [paste context]
REMEMBER: Only TOP 2-3 things matter. Everything else is a NO."
```

#### Step 3: Review & Adjust (2 minutes)
- Verify TOP 2-3 are truly most important
- Check NO list is explicit and protective
- Confirm open loops will actually close
- Ensure completion is realistic

#### Step 4: Commit (1 minute)
```bash
"I commit to completing my TOP 2-3 today: [state them clearly]
I will say NO to everything else. Time is my most valuable asset."
```

## Planning Scenarios

### Scenario 1: Monday Morning Fresh Start
```
"Generate Monday roadmap. Starting fresh this week. OBG: [your goal].
This week's priority: [specific deliverable]. Full energy, no meetings until 11 AM."
```

### Scenario 2: Mid-Week Catch-Up
```
"Generate Wednesday roadmap. Behind on [project]. Must complete [urgent task] today.
Medium energy. Meetings: 10 AM, 2 PM. Help me catch up."
```

### Scenario 3: Friday Wind-Down
```
"Generate Friday roadmap. Week was intense. Need to wrap up [tasks],
prepare for next week, and maintain sanity. Low energy expected."
```

### Scenario 4: Crisis Mode
```
"Emergency planning. [Crisis description]. Everything else on hold.
Must fix [issue] today. Generate focused crisis plan."
```

## Quick Templates

### The One Thing Focus
```
THE ONE THING: [Specific deliverable]
Why it matters: [Impact]
Success looks like: [Measurable outcome]
Time needed: [Hours]
Best time to work: [Energy window]
```

### Tier 1 Task Template
```
Task: [Name]
Estimate: [X hours]
Dependencies: [What needs to happen first]
Success criteria: [What done looks like]
Risk: [What could go wrong]
```

### Energy Check-In
```
Current energy: [1-10]
Peak expected: [Time window]
Crash expected: [Time window]
Mitigation: [Walk/break/coffee/food]
```

## Real-Time Adjustments

### When Things Go Wrong
```bash
# Meeting ran over
"My 10 AM meeting ran 1 hour over. Adjust today's plan for remaining time."

# Energy crash
"Energy crash at 2 PM. Swap complex tasks for simple ones."

# Urgent request
"CEO urgent request: [task]. Reprioritize today keeping THE ONE THING if possible."

# Complete blocker
"THE ONE THING blocked by [issue]. Generate alternative plan for today."
```

### When Things Go Right
```bash
# Ahead of schedule
"Finished THE ONE THING 2 hours early! What should I tackle next?"

# Energy surge
"Unexpected high energy. Can I add a Tier 2 to Tier 1?"

# Help available
"Team member available to help. How to maximize today with extra hands?"
```

## Quick Metrics Check

### End of Day Commands
```bash
# Quick score
"Rate today: THE ONE THING [done/progress], Tier 1 [X/Y done], Energy [managed/crashed]"

# Full assessment
"Assess today's productivity. Completed: [list]. Missed: [list]. Score and advise for tomorrow."

# Pattern check
"Any patterns from today? Should I adjust tomorrow's planning?"
```

## Power User Tips

### 1. Batch Planning Context
Create a template with your common context and just update the changing parts:
```markdown
STANDARD CONTEXT:
- OBG: Scale to 100 customers
- Peak energy: 8-10 AM
- Lunch break: 12-1 PM
- END standard

TODAY'S VARIABLES:
- Yesterday: [Quick update]
- Meetings: [Today's specific]
- Priority: [Today's focus]
```

### 2. Stack Commands
```bash
"Generate daily plan AND create calendar blocks AND set focus mode reminders"
```

### 3. Theme Days
```bash
# Monday = Planning
"Generate Monday roadmap with focus on weekly planning and setup"

# Tuesday = Building
"Generate Tuesday roadmap optimized for deep work and building"

# Wednesday = Communicating
"Generate Wednesday roadmap with time for meetings and collaboration"

# Thursday = Shipping
"Generate Thursday roadmap focused on deployment and delivery"

# Friday = Improving
"Generate Friday roadmap with review, optimization, and next week prep"
```

### 4. Energy Patterns
```bash
# Track your patterns
"My energy pattern: Peak 8-10, Good 10-12, Crash 2-3, Recovery 3-5. Plan accordingly."
```

## Emergency Commands

### Complete Do-Over
```bash
"It's 2 PM and nothing went as planned. Generate recovery plan for remaining hours."
```

### Sick Day Adjustment
```bash
"Feeling sick. Generate minimum viable plan. Only absolutely critical tasks."
```

### Weekend Catch-Up
```bash
"Working Saturday morning, 4 hours available. What's the highest impact from missed week items?"
```

## Pro Configuration

### Set Your Defaults
Create a `planning-defaults.md` file:
```markdown
DEFAULT_OBG: "Scale to 100 customers by Q2"
DEFAULT_PEAK_HOURS: "8-10 AM"
DEFAULT_LUNCH: "12-1 PM"
DEFAULT_WORKDAY_END: "5:30 PM"
DEFAULT_ENERGY_PATTERN: "High morning, crash after lunch, recovery at 3"
DEFAULT_MEETING_DAYS: ["Tuesday", "Thursday"]
DEFAULT_DEEP_WORK_DAYS: ["Monday", "Wednesday", "Friday"]
```

Then use:
```bash
"Generate today's roadmap using my defaults"
```

## Success Patterns

### What Working Plans Look Like
- THE ONE THING is crystal clear and achievable
- Tier 1 totals 4-5 hours (not 8!)
- Energy mapping matches your patterns
- Kill list includes real temptations
- Success metrics are measurable
- Plan generated in <60 seconds
- You feel confident, not overwhelmed

### Red Flags to Avoid
- Tier 1 with 5+ items (too many)
- No buffers between tasks (unrealistic)
- Complex work in low energy slots (recipe for failure)
- Vague success criteria (unclear done state)
- No kill list (everything is not a priority)
- Perfect day planning (no room for reality)

---

Ready to start? Your first command:
```bash
"Generate my daily roadmap for today. I'm ready to be productive!"
```
