#!/bin/bash
# Session Start Hook - Runs when Claude Code starts
# Provides context-aware greeting and suggested actions

# Configuration
LOG_FILE="$HOME/.claude/logs/session-start.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
HOUR=$(date "+%H")
DAY_OF_WEEK=$(date "+%u")  # 1=Monday, 7=Sunday

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

echo "[$TIMESTAMP] Session started" >> "$LOG_FILE"

# Determine time of day greeting
if [ "$HOUR" -lt 12 ]; then
    GREETING="Good morning"
    TIME_CONTEXT="morning"
elif [ "$HOUR" -lt 17 ]; then
    GREETING="Good afternoon"
    TIME_CONTEXT="afternoon"
else
    GREETING="Good evening"
    TIME_CONTEXT="evening"
fi

# Determine day-specific suggestions
case $DAY_OF_WEEK in
    1) DAY_SUGGESTION="Monday = Foundation Day. Start strong with /daily-plan" ;;
    2) DAY_SUGGESTION="Tuesday = Building Day. Deep work time!" ;;
    3) DAY_SUGGESTION="Wednesday = Checkpoint. Mid-week progress check." ;;
    4) DAY_SUGGESTION="Thursday = Collaboration Day. Catch up on comms." ;;
    5) DAY_SUGGESTION="Friday = Ship & Plan. Wrap up and prep for next week." ;;
    6) DAY_SUGGESTION="Saturday. Rest or catch up. You choose." ;;
    7) DAY_SUGGESTION="Sunday evening? Perfect for /weekly-plan" ;;
esac

# Time-specific suggestions
if [ "$TIME_CONTEXT" = "morning" ]; then
    ACTION_SUGGESTION="Start with /daily-plan or /quick-plan"
elif [ "$TIME_CONTEXT" = "evening" ]; then
    ACTION_SUGGESTION="End your day with /assess"
else
    ACTION_SUGGESTION="Check /dashboard for your options"
fi

cat << EOF

================================================================================
$GREETING! Welcome to Claude Code OS
================================================================================

$DAY_SUGGESTION

SUGGESTED ACTION: $ACTION_SUGGESTION

QUICK COMMANDS:
  /dashboard      - See all options
  /daily-plan     - Plan your day
  /quick-plan     - 60-second planning
  /assess         - End-of-day review
  /one-thing      - Find your focus

What would you like to work on?

================================================================================

EOF

echo "[$TIMESTAMP] Session greeting displayed" >> "$LOG_FILE"
