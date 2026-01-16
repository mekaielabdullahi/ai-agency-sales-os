#!/bin/bash
# Weekly Planning Hook - Triggers strategic week planning
# Run this Sunday evening at 6:00 PM

# Configuration
LOG_FILE="$HOME/.claude/logs/weekly-planning.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
WEEK_NUM=$(date "+%V")

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

echo "[$TIMESTAMP] Weekly planning triggered for Week $WEEK_NUM" >> "$LOG_FILE"

# Display weekly planning prompt
cat << EOF

================================================================================
                    WEEKLY STRATEGIC PLANNING - WEEK $WEEK_NUM
================================================================================

Time to plan your most productive week yet!

LAST WEEK REVIEW - Please provide:

1. PRODUCTIVITY SCORES
   - Daily scores: [Mon, Tue, Wed, Thu, Fri]
   - Average: [Calculate or estimate]

2. COMPLETION RATES
   - Tier 1 tasks: [X/Y completed = %]
   - THE ONE THING: [X/5 days = %]

3. WINS - What went well?
   - [Victory 1]
   - [Victory 2]

4. GAPS - What didn't work?
   - [Challenge 1]
   - [Challenge 2]

THIS WEEK - What's ahead:

5. FIXED COMMITMENTS
   - [Meetings, deadlines, appointments]

6. KEY PROJECTS
   - [Project 1 - Status]
   - [Project 2 - Status]

7. OBG STATUS
   - Current progress: [X%]
   - This week's target: [What to advance]

Once you share this, I'll run /weekly-plan to create your strategic week roadmap.

================================================================================

EOF

echo "[$TIMESTAMP] Weekly planning prompt displayed" >> "$LOG_FILE"
