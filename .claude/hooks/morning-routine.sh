#!/bin/bash
# Morning Routine Hook - Triggers daily planning workflow
# Run this at 6:00 AM or when starting your work day

# Configuration
LOG_FILE="$HOME/.claude/logs/morning-routine.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

echo "[$TIMESTAMP] Morning routine triggered" >> "$LOG_FILE"

# Display morning prompt
cat << 'EOF'

================================================================================
                        GOOD MORNING! LET'S PLAN YOUR DAY
================================================================================

Before we start, I need some quick context:

1. How did yesterday go? Any incomplete tasks?
2. What's your energy level today? (high/medium/low)
3. Any fixed commitments today? (meetings, calls, etc.)
4. What's your current OBG (Overarching Business Goal)?

Once you provide this, I'll generate your daily roadmap using /daily-plan

TIP: For a quick 60-second plan, just tell me THE ONE THING and use /quick-plan

================================================================================

EOF

echo "[$TIMESTAMP] Morning routine completed" >> "$LOG_FILE"
