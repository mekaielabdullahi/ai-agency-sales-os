# Notion Fields Specification

**Purpose:** Define required fields for task management and ensure consistency across all Notion entries created by the Meeting to Notion Task Agent.

**Created:** January 11, 2026

---

## Task Database Schema

### Required Fields

| Field Name | Property Type | Required | Options/Format | Validation Rules |
|------------|---------------|----------|----------------|------------------|
| **Title** | Title | Yes | Text | Must be actionable verb phrase |
| **Owner** | Person | Yes | Team member | Single owner only, no multi-select |
| **Status** | Select | Yes | See options below | Must be valid status |
| **Priority** | Select | Yes | P0, P1, P2, P3, P4, P5 | Must align with OBG |
| **Type** | Select | Yes | See options below | Must match owner role |
| **Sprint** | Relation | Yes | Sprint database | Link to active sprint |
| **Project** | Relation | Yes | Project database | Link to client project |

### Conditional Fields

| Field Name | Property Type | Required When | Options/Format |
|------------|---------------|---------------|----------------|
| **Due Date** | Date | Deadline mentioned | YYYY-MM-DD |
| **Estimated Hours** | Number | Owner is Maker | In hours (4-hour blocks for makers) |
| **Dependencies** | Relation | Has blockers | Task database |
| **Blocked By** | Relation | Status = Blocked | Task or external |

### Optional Fields

| Field Name | Property Type | Purpose |
|------------|---------------|---------|
| **Notes** | Text | Context from conversation |
| **Source** | Select | Meeting, Async, Planning |
| **Created By** | Person | Who created (agent or human) |
| **Meeting Link** | URL | Link to recording/transcript |

---

## Field Options

### Status Options

| Status | Meaning | Next Actions |
|--------|---------|--------------|
| **Pending** | Not yet started | Can be picked up |
| **In Progress** | Actively being worked | Single owner working |
| **Blocked** | Cannot proceed | Requires dependency resolution |
| **In Review** | Work complete, needs review | Awaiting sign-off |
| **Complete** | Done and verified | Archive eligible |

### Priority Options

| Priority | Focus Area | Examples |
|----------|------------|----------|
| **P0** | Revenue (close, deliver, collect) | Client deliverables, proposals, invoicing |
| **P1** | Agency infrastructure | Role clarity, process docs, templates |
| **P2** | Developer pipeline | Recruitment, evaluation, onboarding |
| **P3** | Developer Academy | Training content, certification |
| **P4** | Credibility assets | Case studies, demos, testimonials |
| **P5** | Content/inbound | YouTube, blog, social (DEFERRED) |

### Type Options

| Type | For Role | Description |
|------|----------|-------------|
| **Deep Work** | Makers | 4-hour focus blocks, no interruptions |
| **Coordination** | Managers | Meetings, communications, planning |
| **Review** | Both | Code review, document review, sign-off |
| **Meeting** | Both | Scheduled sync, client call |
| **Admin** | Both | Invoicing, documentation, setup |

---

## Validation Rules

### Owner-Type Alignment

```
IF Owner is Maker (Matthew, Trent):
  - Type should be: Deep Work, Review
  - Type should NOT be: Coordination, Meeting (unless in sync windows)
  - Must have: Estimated Hours

IF Owner is Manager (Mekaiel, Chris):
  - Type can be: Coordination, Review, Meeting, Admin
  - Does NOT need: Estimated Hours in blocks
```

### Priority-OBG Alignment

```
P0 tasks must:
  - Directly impact revenue
  - Have clear deliverable
  - Have deadline (implicit or explicit)

P5 tasks:
  - Should be flagged for deferral
  - Ask: "Is this contributing to $50k/mo goal?"
```

### Maker Time Budget

```
Per Week per Maker:
  - Maximum 10 four-hour blocks available
  - Maximum 3 hours in meetings
  - Sync windows only: 07:00-07:30, 11:30-12:00, 17:00-17:30

Validation:
  - Sum of Estimated Hours for maker should not exceed 40/week
  - Sum of Meeting-type tasks should not exceed 3 hours/week
```

---

## Sprint Database Schema

| Field Name | Property Type | Required | Notes |
|------------|---------------|----------|-------|
| **Sprint Name** | Title | Yes | "Jan 11-14, 2026" format |
| **Start Date** | Date | Yes | Sprint start |
| **End Date** | Date | Yes | Sprint end |
| **Focus** | Text | Yes | Primary objectives |
| **Tasks** | Relation | Yes | Linked tasks |
| **Status** | Select | Yes | Planning, Active, Complete |

---

## Project Database Schema

| Field Name | Property Type | Required | Notes |
|------------|---------------|----------|-------|
| **Project Name** | Title | Yes | Client-facing name |
| **Client** | Relation | Yes | Client database |
| **Phase** | Select | Yes | Discovery, Phase 1, Phase 2, etc. |
| **Status** | Select | Yes | Active, Paused, Complete |
| **Revenue** | Number | Yes | Total contract value |
| **Tasks** | Relation | Yes | Linked tasks |
| **Owner** | Person | Yes | Primary point of contact |

---

## Example Task Creation

### Good Task Entry

```json
{
  "Title": "Complete S&S Wolf inventory API integration",
  "Owner": "Matthew Kerns",
  "Status": "In Progress",
  "Priority": "P0",
  "Type": "Deep Work",
  "Sprint": "Jan 11-14, 2026",
  "Project": "S&S Wolf Sheds",
  "Due Date": "2026-01-14",
  "Estimated Hours": 8,
  "Notes": "Part of Phase 1 delivery. Focus on error handling."
}
```

### Bad Task Entry (Violations)

```json
{
  "Title": "Help with stuff",           // Not actionable
  "Owner": ["Matthew", "Trent"],         // Multiple owners
  "Status": "Maybe",                     // Invalid status
  "Priority": "High",                    // Not P0-P5 format
  "Type": "Work",                        // Invalid type
  // Missing: Sprint, Project
}
```

---

## Agent Validation Checklist

Before creating a task, the Meeting to Notion Task Agent should verify:

### Required Field Check
- [ ] Title is actionable (starts with verb)
- [ ] Single owner assigned
- [ ] Status is valid option
- [ ] Priority is P0-P5
- [ ] Type matches owner role
- [ ] Sprint is linked
- [ ] Project is linked

### Maker Time Check (if Owner is Maker)
- [ ] Estimated Hours provided
- [ ] Within weekly capacity
- [ ] Not exceeding meeting budget
- [ ] Scheduled within sync windows (if meeting)

### Priority Alignment Check
- [ ] P0 tasks have revenue impact
- [ ] P5 tasks flagged for deferral
- [ ] Aligns with current sprint focus

### Dependency Check
- [ ] Dependencies identified and linked
- [ ] Blocked status used appropriately
- [ ] Circular dependencies avoided

---

## Notion API Integration Notes

### Database IDs (Configure per workspace)

```
TASKS_DATABASE_ID=<your-tasks-database-id>
SPRINTS_DATABASE_ID=<your-sprints-database-id>
PROJECTS_DATABASE_ID=<your-projects-database-id>
TEAM_DATABASE_ID=<your-team-database-id>
```

### Property Mappings

The agent needs to map field names to Notion property IDs. Create a configuration:

```json
{
  "fields": {
    "title": "title",
    "owner": "Owner",
    "status": "Status",
    "priority": "Priority",
    "type": "Type",
    "sprint": "Sprint",
    "project": "Project",
    "due_date": "Due Date",
    "estimated_hours": "Estimated Hours",
    "dependencies": "Dependencies",
    "notes": "Notes"
  }
}
```

### Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| Invalid owner | Person not in workspace | Check team member spelling |
| Missing relation | Sprint/Project not found | Verify database links |
| Validation failed | Required field missing | Prompt for missing info |
| Rate limited | Too many API calls | Batch operations, add delays |

---

## Maintenance

### Weekly Tasks
- Review task completion rates
- Archive completed sprints
- Update project phases as needed

### Monthly Tasks
- Audit field usage patterns
- Remove unused options
- Update validation rules as team evolves

### When Team Changes
- Update Owner options
- Adjust Maker/Manager mappings
- Review capacity calculations

---

*This specification should be reviewed whenever Notion database structure changes or team composition evolves.*
