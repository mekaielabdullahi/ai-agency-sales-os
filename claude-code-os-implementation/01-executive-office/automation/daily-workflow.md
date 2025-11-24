# Executive Office - Automated Daily Workflow

## Complete Daily Automation Setup

This guide provides ready-to-use automation for your daily Executive Office workflow with Claude Code.

## 🌅 Morning Automation (6:00 AM)

### Step 1: Context Gathering Script
Create a file `gather-context.md` that automatically updates:

```markdown
<!-- gather-context.md -->
# Daily Context - [DATE]

## Yesterday's Status
<!-- Pull from yesterday's assessment -->
[Yesterday's productivity score: X/10]
[Completed: List]
[Incomplete: List]

## Today's Landscape
<!-- Pull from calendar -->
[Fixed commitments]
[Deadlines]

## Active Projects
<!-- Pull from project tracker -->
[Project statuses]

## Energy Forecast
<!-- Based on patterns -->
[Expected energy level based on day of week]

## Strategic Context
OBG: [Your constant goal]
Week Priority: [This week's focus]
Month Milestone: [This month's target]
```

### Step 2: Morning Planning Command
```bash
# Create alias for daily planning
alias morning-plan='claude-exec "Generate my daily roadmap using context from gather-context.md. Today is $(date +%A), $(date +%B) $(date +%d). Energy pattern: High 8-10 AM, Good 10-12, Low 2-3 PM, Recovery 3-5 PM."'

# Execute
morning-plan
```

### Step 3: Auto-Save Plan
```bash
# Save today's plan with timestamp
claude-exec "Generate my daily roadmap" > "plans/$(date +%Y-%m-%d)-plan.md"

# Open in editor
code "plans/$(date +%Y-%m-%d)-plan.md"
```

## 🏃 Execution Phase Automation

### Task Status Tracking
```bash
# Mark task as started
alias task-start='claude-exec "Marking task as in-progress: $1. Time: $(date +%H:%M)"'

# Mark task as complete
alias task-done='claude-exec "Task completed: $1. Time: $(date +%H:%M). Actual time: $2 hours"'

# Quick status check
alias status='claude-exec "Current status: Working on $1. Progress: $2%"'
```

### Real-Time Adjustments
```bash
# Energy crash adjustment
alias energy-crash='claude-exec "Energy crash at $(date +%H:%M). Adjust remaining plan for low energy tasks only"'

# Urgent interruption
alias urgent='claude-exec "Urgent request: $1. Reprioritize today keeping THE ONE THING if possible"'

# Meeting overrun
alias meeting-overrun='claude-exec "Meeting ran $1 minutes over. Compress remaining schedule"'
```

## 🌆 Evening Automation (5:30 PM)

### Assessment Generation
```bash
# Generate assessment with context
alias evening-assess='claude-exec "Generate productivity assessment. Completed: $(cat ~/.completed-today). Incomplete: $(cat ~/.incomplete-today). Energy management: $(cat ~/.energy-log)"'

# Save assessment
evening-assess > "assessments/$(date +%Y-%m-%d)-assessment.md"
```

### Pattern Tracking
```bash
# Log patterns
alias log-pattern='echo "$(date +%Y-%m-%d): $1" >> ~/.productivity-patterns'

# View patterns
alias show-patterns='tail -20 ~/.productivity-patterns'
```

## 📅 Weekly Automation

### Sunday Planning Setup
```bash
# Sunday evening weekly planning
alias week-plan='claude-exec "Generate strategic week plan. Week number: $(date +%V). Last week average: $(cat ~/.week-average). OBG: $(cat ~/.obg)"'

# Auto-schedule
crontab -e
# Add: 0 18 * * 0 week-plan > ~/weekly-plans/week-$(date +%V).md
```

### Wednesday Checkpoint
```bash
# Mid-week checkpoint
alias week-check='claude-exec "Wednesday checkpoint. Week ONE THING progress: $1%. Adjust remaining days if needed"'
```

### Friday Review
```bash
# Week completion
alias week-done='claude-exec "Week complete. Average score: $1. ONE THING: $2. Generate lessons learned"'
```

## 🤖 Full Automation Pipeline

### Complete Morning Routine Script
Create file: `morning-routine.sh`

```bash
#!/bin/bash
# Executive Office Morning Routine

echo "☀️ Starting Executive Office Morning Routine..."
echo "Date: $(date '+%A, %B %d, %Y')"
echo ""

# Step 1: Gather context
echo "📊 Gathering context..."
YESTERDAY_SCORE=$(cat ~/.productivity-score 2>/dev/null || echo "No data")
INCOMPLETE=$(cat ~/.incomplete-tasks 2>/dev/null || echo "None")
CALENDAR=$(cal -h | grep -E "$(date +%d)")

# Step 2: Generate plan
echo "🎯 Generating daily roadmap..."
PLAN=$(claude-exec "Generate my daily roadmap.
Yesterday score: $YESTERDAY_SCORE
Incomplete: $INCOMPLETE
Today is $(date +%A)
OBG: $(cat ~/.obg)")

# Step 3: Save plan
echo "$PLAN" > "$HOME/daily-plans/$(date +%Y-%m-%d).md"

# Step 4: Extract THE ONE THING
THE_ONE_THING=$(echo "$PLAN" | grep -A1 "THE ONE THING" | tail -1)

# Step 5: Set focus reminder
echo "🎯 Today's THE ONE THING: $THE_ONE_THING"

# Step 6: Create calendar blocks
echo "📅 Creating calendar blocks..."
# Add calendar integration here

# Step 7: Set up environment
echo "🖥️ Setting up work environment..."
# Open necessary apps, close distractions

echo "✅ Morning routine complete!"
echo "THE ONE THING: $THE_ONE_THING"
echo ""
echo "Let's execute! 🚀"
```

### Complete Evening Routine Script
Create file: `evening-routine.sh`

```bash
#!/bin/bash
# Executive Office Evening Routine

echo "🌙 Starting Executive Office Evening Routine..."
echo "Date: $(date '+%A, %B %d, %Y')"
echo ""

# Step 1: Collect today's data
echo "📊 Collecting today's performance data..."
read -p "THE ONE THING completed? (y/n): " ONE_THING_DONE
read -p "Tier 1 tasks completed (X/Y): " TIER1_DONE
read -p "Energy management (good/crashed): " ENERGY_MGMT

# Step 2: Generate assessment
echo "📈 Generating productivity assessment..."
ASSESSMENT=$(claude-exec "Generate productivity assessment.
THE ONE THING: $ONE_THING_DONE
Tier 1: $TIER1_DONE
Energy: $ENERGY_MGMT
Time: $(date +%H:%M)")

# Step 3: Calculate score
SCORE=$(echo "$ASSESSMENT" | grep "SCORE:" | cut -d: -f2)
echo "$SCORE" > ~/.productivity-score

# Step 4: Save assessment
echo "$ASSESSMENT" > "$HOME/assessments/$(date +%Y-%m-%d).md"

# Step 5: Extract patterns
PATTERNS=$(echo "$ASSESSMENT" | grep -A3 "Patterns")
echo "$(date +%Y-%m-%d): $PATTERNS" >> ~/.patterns-log

# Step 6: Prepare tomorrow
echo "📅 Preparing for tomorrow..."
TOMORROW_PREP=$(echo "$ASSESSMENT" | grep -A5 "Tomorrow")
echo "$TOMORROW_PREP" > ~/.tomorrow-prep

# Step 7: Display summary
echo ""
echo "📊 Today's Score: $SCORE"
echo "✨ Key Learning: $(echo "$PATTERNS" | head -1)"
echo "🎯 Tomorrow's Focus: $(cat ~/.tomorrow-prep | head -1)"
echo ""
echo "Rest well! Tomorrow you'll be even better! 💪"
```

## ⚡ Quick Commands Reference

### Daily Operations
```bash
# Planning
morning-plan              # Generate daily roadmap
quick-plan [context]      # Quick plan with context
adjust-plan [change]      # Adjust current plan

# Execution
start [task]             # Mark task started
done [task] [hours]      # Mark task complete
block [reason]           # Log blocker
energy [level]           # Log energy level

# Assessment
assess                   # Generate assessment
score [1-10]            # Quick score log
pattern [observation]    # Log pattern

# View
today                   # Show today's plan
status                  # Current status
metrics                 # Today's metrics
```

### Weekly Operations
```bash
# Planning
week-plan               # Generate weekly strategic plan
week-adjust            # Adjust week plan
brutal-prioritize      # Apply brutal prioritization

# Checkpoints
monday-start           # Monday kickoff
wednesday-check        # Wednesday checkpoint
friday-review          # Friday week review

# Analysis
week-patterns          # Show week's patterns
week-metrics          # Show week's metrics
week-lessons          # Extract lessons learned
```

## 🔧 Configuration Files

### Create `.executive-office-config`
```bash
# Executive Office Configuration
OBG="Scale to 100 customers by Q2"
PEAK_HOURS="8-10"
GOOD_HOURS="10-12"
LOW_HOURS="14-17"
PLAN_TIME="06:00"
ASSESS_TIME="17:30"
WORK_DAYS="Mon-Fri"
DEEP_WORK_DAYS="Mon,Wed,Fri"
MEETING_DAYS="Tue,Thu"
```

### Create `.productivity-aliases`
```bash
# Source this file in .bashrc or .zshrc
source ~/.executive-office-config

# Quick aliases
alias mp='morning-plan'
alias ep='evening-assess'
alias tot='echo "THE ONE THING: " && head -n 20 ~/daily-plans/$(date +%Y-%m-%d).md | grep -A1 "THE ONE THING"'
alias score='echo -n "Quick score (1-10): " && read SCORE && echo "$(date): $SCORE" >> ~/.scores'
```

## 📱 Mobile Quick Commands

For phone/tablet access, create shortcuts:

```bash
# iOS Shortcuts / Android Automate
"Hey Claude, morning plan"
"Hey Claude, mark [task] done"
"Hey Claude, energy crash help"
"Hey Claude, assess my day"
```

## 🎯 Success Verification

Your automation is working when:
- Morning plan generates in <60 seconds
- Evening assessment takes <2 minutes input
- Patterns are automatically detected
- Weekly plans align with daily execution
- You spend <10 minutes/day on planning overhead

## 🚀 Next Steps

1. Install scripts in your path
2. Set up cron jobs for automation
3. Configure your personal defaults
4. Test for one week
5. Refine based on patterns

Ready to automate your Executive Office? Start with:
```bash
chmod +x morning-routine.sh evening-routine.sh
./morning-routine.sh
```