---
name: tasks
description: Pull Notion tasks, leads, projects, and meetings into a prioritized dashboard. Use when starting work or checking what to focus on.
---

# /tasks - Notion Task Command Center

Pull together your Notion tasks, leads, projects, and meetings into a prioritized dashboard.

## Command Variations

| Command | Output |
|---------|--------|
| `/tasks` | Full dashboard |
| `/tasks today` | Only today's tasks |
| `/tasks overdue` | Only overdue items |
| `/tasks [project]` | Tasks for specific project |
| `/tasks update` | Interactive task update mode |

## Workflow

### Step 1: Fetch Data from Notion

Use Notion MCP tools to query the following databases:

**Tasks Database** (data_source: `collection://2d5e7406-6c7d-8151-bdda-000b46294153`)
- Filter: Status != Done, Status != Cancelled
- Sort by: Due Date ascending
- Include: Task Name, Status, Priority, Due Date, Project relation

**Projects Database** (data_source: `collection://2d5e7406-6c7d-8167-bb16-000b3ec34789`)
- Filter: Status = In Progress
- Include: Project Name, Status, Manager, related Tasks

**Meetings Database** (data_source: `collection://2d5e7406-6c7d-81c3-a4eb-000b0a3fe028`)
- Filter: Date >= 7 days ago
- Include: Name, Date, Summary, Type, Transcript Link, Status

**Contacts Database** (data_source: `collection://2d5e7406-6c7d-818c-bc3d-000b38dab7e4`)
- Filter: Status = Lead OR Status = Outreach Sent
- Include: Client Name, Status, Company, Last Contacted, Next Step, Email
- Used for: Leads Needing Attention section

### Step 2: Process & Group

Group tasks into categories:
- **Overdue**: Due date < today
- **Due Today**: Due date = today
- **Due This Week**: Due date within next 7 days
- **Upcoming**: Due date > 7 days

Additional processing:
- Match tasks to their parent projects
- Identify leads with stale contact (7+ days since last touch)
- Surface meetings with unprocessed action items
- Calculate task counts per project

### Step 3: Generate Dashboard

Output a markdown dashboard with the following sections:

```markdown
# Your Focus for [Today's Date]

## Overdue (Action Required)
| Task | Project | Due | Priority |
|------|---------|-----|----------|
| [Task name] | [Project] | Feb 7 (2d overdue) | High |

## Due Today
| Task | Project | Priority |
|------|---------|----------|
| [Task name] | [Project] | Urgent |

## This Week
| Task | Project | Due | Priority |
|------|---------|-----|----------|
| [Task name] | [Project] | Feb 12 | Medium |

## Top 3 Recommended
1. **[Task]** - [Why: overdue + high priority]
2. **[Task]** - [Why: due today + blocks other work]
3. **[Task]** - [Why: quick win, high impact]

## Leads Needing Attention
| Contact | Company | Stage | Last Touch | Action |
|---------|---------|-------|------------|--------|
| [Name] | [Co] | Discovery | 8 days ago | Follow up |

## Recent Meetings (Open Items)
| Meeting | Date | Pending Actions |
|---------|------|-----------------|
| [Name] | Feb 6 | 3 items |

## Projects Summary
| Project | Status | Your Tasks | Next Due |
|---------|--------|------------|----------|
| Plotter Phase 2 | In Progress | 5 | Feb 10 |
```

### Step 4: Interactive Options (for /tasks update)

When user runs `/tasks update`:
1. Show numbered list of tasks
2. Ask which task to update
3. Offer options: Mark complete, Change priority, Add notes
4. Use Notion MCP to update the task
5. Confirm the update

## Priority Scoring for Recommendations

Top 3 recommendations are selected based on:
1. **Overdue + High/Urgent priority** = highest score
2. **Due today + blocks other work** = high score
3. **Quick win (estimated < 30min) + high impact** = medium-high score
4. **Stale lead follow-up** = medium score
5. **Meeting action items** = medium score

## Configuration

See `tasks-config.json` for:
- `stale_lead_days`: Days before a lead is considered stale (default: 7)
- `meeting_lookback_days`: How far back to look for meetings (default: 7)
- `priority_order`: Priority levels in order of urgency
- `status_exclude`: Statuses to filter out
- `max_tasks_shown`: Maximum tasks to display per section (default: 15)

## Notion Database IDs

**Parent Pages:**
| Page | ID |
|------|-----|
| Sales | `2d5e7406-6c7d-80e7-8e3c-c69b188d5f19` |
| Sales Pipeline | `2d5e7406-6c7d-816f-9bac-f24aec6461ce` |

**Databases:**
| Database | Page ID | Data Source (for search) |
|----------|---------|--------------------------|
| Tasks | `2fce7406-6c7d-8076-ae6f-f40c4ccb8bc7` | `collection://2d5e7406-6c7d-8151-bdda-000b46294153` |
| Projects | `2d5e7406-6c7d-81c2-b56d-df1a684fc501` | `collection://2d5e7406-6c7d-8167-bb16-000b3ec34789` |
| Meetings | `2fce7406-6c7d-8026-8e5f-ea5ef0d95c5b` | `collection://2d5e7406-6c7d-81c3-a4eb-000b0a3fe028` |
| Contacts | `2d5e7406-6c7d-81df-8d4c-cd22971fc807` | `collection://2d5e7406-6c7d-818c-bc3d-000b38dab7e4` |

## Example Usage

**Full dashboard:**
```
/tasks
```

**Today only:**
```
/tasks today
```

**Filter by project:**
```
/tasks plotter
```

**Update a task:**
```
/tasks update
```
