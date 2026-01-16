#!/bin/bash
# Evening Routine Hook - Triggers productivity assessment
# Run this at 5:30 PM or when ending your work day

# Configuration
LOG_FILE="$HOME/.claude/logs/evening-routine.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

echo "[$TIMESTAMP] Evening routine triggered" >> "$LOG_FILE"

# Display evening prompt
cat << 'EOF'

================================================================================
                        TIME FOR YOUR DAILY ASSESSMENT
================================================================================

Let's review your day objectively. Please provide:

1. TIER 1 TASKS - What was planned vs completed?
   - Task 1: [Planned X hours] → [Completed? Y/N, Actual time]
   - Task 2: [Planned X hours] → [Completed? Y/N, Actual time]
   - Task 3: [Planned X hours] → [Completed? Y/N, Actual time]

2. THE ONE THING - Did you complete it?
   - [Your ONE THING]: [Completed / Partial / Not Done]

3. DISTRACTIONS - Total unplanned interruption time?
   - Estimated: [X minutes/hours]

4. ENERGY - How did your energy levels play out?
   - Morning: [High/Medium/Low]
   - Afternoon: [High/Medium/Low]

5. BLOCKERS - What got in your way?
   - [Any challenges or obstacles]

Once you share this, I'll run /assess to calculate your productivity score
and generate tomorrow's recovery plan.

================================================================================

EOF

echo "[$TIMESTAMP] Evening routine completed" >> "$LOG_FILE"
