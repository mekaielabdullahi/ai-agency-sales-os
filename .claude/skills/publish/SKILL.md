---
name: publish
description: Publish approved content to LinkedIn. Takes brand-illustrator outputs (image + copy) and posts to LinkedIn via browser automation or API. Use when content is approved and ready to go live.
---

# Publish Skill

## Purpose

Take approved content from the brand-illustrator pipeline and publish it to LinkedIn. Handles image upload, post copy, hashtags, and scheduling.

## When to Use

- "Publish this to LinkedIn"
- "Post the approved content"
- "/publish [project-name]"
- After brand-illustrator content is approved in Slack

## Prerequisites

- Content approved via brand-illustrator workflow
- LinkedIn account access (via browser automation with Claude in Chrome MCP)
- Project folder with: image file, copy variations, hashtags

## Workflow

### Phase 1: Locate Approved Content

**If project name provided:**
```
.claude/skills/brand-illustrator/projects/[project-name]/
```

**If no project name:**
1. Scan projects folder for most recent
2. Check for `approved` marker or Slack approval timestamp
3. Confirm with user which project to publish

**Required Files:**
- `output/final-image.png` - The approved illustration
- `output/post-copy.md` - Approved copy variation
- `output/hashtags.txt` - Selected hashtags
- `prompt.md` - Original brief (for reference)

### Phase 2: Prepare Post Content

**Extract from project:**

```markdown
## Post Preview

**Image:** [filename]
**Copy:**
[Selected copy variation - typically 150-300 words]

**Hashtags:**
[Selected hashtag combination - typically 3-5 tags]

**CTA:** [If specified]
```

**Validate:**
- [ ] Image exists and is correct format (PNG/JPG)
- [ ] Copy is within LinkedIn limits (3000 chars max, ideally <1500)
- [ ] Hashtags are formatted correctly (#tag)
- [ ] No placeholder text remains

### Phase 3: Publish via Browser Automation

**Using Claude in Chrome MCP:**

1. Navigate to LinkedIn post composer
2. Upload image
3. Paste post copy
4. Add hashtags
5. Preview post
6. Confirm with user before posting
7. Click "Post"

**Manual Fallback:**
If browser automation unavailable:
1. Copy all content to clipboard
2. Provide step-by-step instructions for manual posting
3. Open LinkedIn in browser for user

### Phase 4: Post-Publish Actions

**After successful publish:**

1. **Update project status:**
   ```
   echo "published: $(date)" >> projects/[name]/status.txt
   ```

2. **Archive project:**
   Move to `projects/archive/[YYYY-MM]/[project-name]/`

3. **Log to content tracker:**
   Append to `.claude/skills/brand-illustrator/published-log.md`:
   ```markdown
   | Date | Project | Platform | Link |
   |------|---------|----------|------|
   | [DATE] | [NAME] | LinkedIn | [POST_URL] |
   ```

4. **Notify Slack:**
   Post confirmation to content channel:
   ```
   ✅ Published: [TITLE]
   Platform: LinkedIn
   Link: [POST_URL]
   ```

5. **Sync to Notion (optional):**
   Update content calendar database with published status

## Scheduling (Future Enhancement)

For scheduled posts:
- Use LinkedIn's native scheduling (if available via UI)
- Or queue in external tool (Buffer, Hootsuite, etc.)
- Store schedule in project's `schedule.json`

## Error Handling

| Error | Action |
|-------|--------|
| No approved content found | List recent projects, ask user to specify |
| Image missing | Check output folder, regenerate if needed |
| Copy too long | Suggest shortened version |
| Browser automation fails | Provide manual posting instructions |
| LinkedIn session expired | Prompt user to log in |
| Post fails | Save draft, retry, or escalate |

## Safety Checks

Before posting, always:

1. **Preview to user** - Show exactly what will be posted
2. **Confirm action** - "Ready to publish this to LinkedIn? (y/n)"
3. **Never auto-post** - Always require explicit user confirmation

## Example Usage

**User:** "/publish 2026-01-19-ai-time-savings"

**Skill Response:**
```
📤 Preparing to publish...

Project: 2026-01-19-ai-time-savings
Platform: LinkedIn

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📷 Image: final-image.png (1080x1080)

📝 Copy:
"AI didn't replace my job.
It replaced the parts I hated.

The 3-hour report that used to drain me?
Now takes 12 minutes..."

🏷️ Hashtags: #AIProductivity #FutureOfWork #Automation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready to publish to LinkedIn? (y/n)
```

## Integration Points

- **brand-illustrator** → Provides approved content
- **Claude in Chrome MCP** → Browser automation for posting
- **Slack** → Approval workflow and notifications
- **Notion** → Content calendar sync

## Future Enhancements

- [ ] Multi-platform support (Twitter/X, Instagram)
- [ ] Scheduling support
- [ ] Analytics tracking (engagement metrics)
- [ ] A/B testing support (post multiple variations)
- [ ] Thread/carousel support
