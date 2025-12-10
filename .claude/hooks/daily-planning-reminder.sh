#!/bin/bash

# Daily Planning Reminder Hook
# Triggers on SessionStart to remind user to plan if 6+ hours have passed

# State file to track last reminder time
STATE_FILE="$HOME/.claude/last-planning-reminder.txt"
CURRENT_TIME=$(date +%s)

# Check if state file exists
if [ ! -f "$STATE_FILE" ]; then
    # First time - show reminder
    SHOW_REMINDER=true
    HOURS_PASSED="N/A"
else
    # Read last reminder time
    LAST_REMINDER=$(cat "$STATE_FILE")
    SECONDS_PASSED=$(( CURRENT_TIME - LAST_REMINDER ))
    HOURS_PASSED=$(( SECONDS_PASSED / 3600 ))

    # Show reminder if 6+ hours have passed
    if [ "$HOURS_PASSED" -ge 6 ]; then
        SHOW_REMINDER=true
    else
        SHOW_REMINDER=false
    fi
fi

# If we should show reminder
if [ "$SHOW_REMINDER" = true ]; then
    # Update state file
    echo "$CURRENT_TIME" > "$STATE_FILE"

    # Output reminder message that Claude will see as context
    cat <<'EOF'
⏰ DAILY PLANNING REMINDER

Time to review your daily plan! Consider:
- What are your top 3 priorities for the next 6 hours?
- What progress have you made since last planning session?
- Are you still aligned with your 90-day strategic goals?

Quick planning prompts:
- "Help me plan my next 6 hours"
- "Review my progress and adjust priorities"
- "What should I focus on right now based on AriseGroup strategy?"

EOF
fi

exit 0
