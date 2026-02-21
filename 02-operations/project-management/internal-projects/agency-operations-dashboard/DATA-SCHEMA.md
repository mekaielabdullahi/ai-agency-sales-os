# Agency Operations Dashboard - Data Schema

**Purpose:** Define data structures for all dashboard tabs
**Format:** JSON (Phase 1-2), potentially migrate to database (Phase 3+)
**Created:** December 25, 2025

---

## Core Data Models

### 1. Project Model

```json
{
  "id": "proj_001",
  "name": "Trevor Bradford - IDEA Framework Website",
  "client": {
    "id": "client_001",
    "name": "Trevor Bradford",
    "company": "IDEA Brand Coach",
    "contacts": [
      {
        "name": "Trevor Bradford",
        "role": "Founder",
        "email": "trevor@example.com",
        "phone": "+1-XXX-XXX-XXXX"
      }
    ]
  },
  "phase": "quick_win",
  "phaseLabel": "Quick Win (Phase 3 Beta)",
  "status": "in_progress",
  "priority": "P0",
  "revenue": {
    "received": 500,
    "projected": 1500,
    "total": 2000,
    "breakdown": [
      {
        "phase": "Phase 2 - Foundation",
        "amount": 500,
        "status": "paid",
        "dateReceived": "2025-12-02"
      },
      {
        "phase": "Phase 3 - Beta Ready",
        "amount": 1500,
        "status": "pending",
        "dateExpected": "2025-12-30"
      }
    ]
  },
  "dates": {
    "started": "2025-11-15",
    "deadline": "2025-12-27",
    "deadlineType": "client_facing",
    "expectedCompletion": "2025-12-27"
  },
  "deliverables": [
    {
      "id": "deliv_001",
      "name": "Beta-ready website",
      "description": "Consolidated output document, UI polish, Strategic Brand Building Journey page",
      "status": "in_progress",
      "deadline": "2025-12-27",
      "owner": "Matt Kerns",
      "estimatedHours": 16,
      "hoursInvested": 0
    }
  ],
  "riskLevel": "high",
  "riskNotes": "Late delivery = lose ALL future revenue",
  "tags": ["paid", "quick_win", "ultra_critical"],
  "links": {
    "projectFolder": "/active-projects/idea-framework-website/",
    "roadmap": "/active-projects/idea-framework-website/P1-PHASE-3-ROADMAP.md",
    "demoUrl": "https://trevor-idea.demo.com"
  }
}
```

### 2. Revenue Model

```json
{
  "summary": {
    "yearToDate": 12500,
    "currentMonth": 3750,
    "projectedMonth": 8000,
    "projectedQuarter": 22500
  },
  "byProject": [
    {
      "projectId": "proj_001",
      "projectName": "Trevor Bradford - IDEA Website",
      "received": 500,
      "projected": 1500,
      "total": 2000,
      "status": "in_progress"
    }
  ],
  "byPhase": {
    "discovery": 2000,
    "quickWin": 8500,
    "phase2": 5000,
    "phase3Plus": 2000
  },
  "byStatus": {
    "received": 12500,
    "committed": 8000,
    "projected": 2000
  }
}
```

### 3. Client Model

```json
{
  "id": "client_001",
  "name": "Trevor Bradford",
  "company": "IDEA Brand Coach",
  "industry": "Coaching / Personal Development",
  "contacts": [
    {
      "name": "Trevor Bradford",
      "role": "Founder",
      "email": "trevor@example.com",
      "phone": "+1-XXX-XXX-XXXX",
      "isPrimary": true
    }
  ],
  "processMap": {
    "stages": [
      {
        "name": "Discovery",
        "status": "complete",
        "completedDate": "2025-11-10",
        "deliverables": ["Discovery call notes", "Initial requirements"]
      },
      {
        "name": "Quick Win (Phase 3)",
        "status": "current",
        "startDate": "2025-11-15",
        "expectedCompletion": "2025-12-27",
        "deliverables": ["Beta-ready website"]
      },
      {
        "name": "Phase 4+",
        "status": "upcoming",
        "expectedStart": "2026-01-10",
        "deliverables": ["TBD based on beta feedback"]
      }
    ]
  },
  "communication": {
    "lastContact": "2025-12-15",
    "lastContactType": "Email update",
    "nextMeeting": "2025-12-27",
    "nextMeetingType": "Demo / handoff",
    "notes": "3-week beta testing period expected after delivery"
  },
  "projects": ["proj_001"],
  "totalRevenue": 2000,
  "status": "active"
}
```

### 4. Opportunity Model (Sales Pipeline)

```json
{
  "id": "opp_001",
  "name": "AntSavvy - Accounts AI Assistant",
  "company": "AntSavvy",
  "contact": {
    "name": "Christian",
    "email": "christian@antsavvy.com"
  },
  "stage": "proposal",
  "expectedRevenue": 1000,
  "probability": 75,
  "weightedRevenue": 750,
  "expectedCloseDate": "2026-01-06",
  "owner": "Matt Kerns",
  "notes": "Demo delivered Dec 21, awaiting feedback",
  "nextActions": [
    "Follow up for feedback",
    "Send cost proposal",
    "Schedule finalization call"
  ],
  "history": [
    {
      "date": "2025-12-21",
      "stage": "demo",
      "notes": "Demo chatbot delivered"
    },
    {
      "date": "2025-12-25",
      "stage": "proposal",
      "notes": "Cost proposal created, ready to send"
    }
  ]
}
```

### 5. Pricing Model

```json
{
  "consultingPhases": [
    {
      "name": "Discovery Call",
      "duration": "1 hour",
      "rate": 200,
      "description": "Initial diagnostic and problem scoping"
    },
    {
      "name": "Audit / Deep Discovery",
      "duration": "2-3 hours",
      "rate": 500,
      "description": "Comprehensive audit and solution design"
    }
  ],
  "deliverablePricing": [
    {
      "id": "price_001",
      "deliverable": "Quick Win Sprint",
      "clientPrice": 5000,
      "ourCost": 2000,
      "margin": 3000,
      "marginPercent": 60,
      "clientROI": "10x - saves 20 hours/month at $50/hr = $1000/month",
      "timeEstimate": "40 hours",
      "notes": "Standard quick win pricing for automation projects"
    },
    {
      "id": "price_002",
      "deliverable": "Phase 2 Enhancement",
      "clientPrice": 10000,
      "ourCost": 4000,
      "margin": 6000,
      "marginPercent": 60,
      "clientROI": "Variable based on scope",
      "timeEstimate": "80-100 hours",
      "notes": "Typical Phase 2 pricing after successful quick win"
    }
  ],
  "historicalPricing": [
    {
      "project": "Plotter Mechanix Phase 1",
      "deliverable": "Quick Win Sprint",
      "clientPrice": 5000,
      "actualCost": 1800,
      "actualMargin": 3200,
      "actualHours": 36,
      "notes": "Under budget, efficient delivery"
    }
  ]
}
```

### 6. Deliverable Model

```json
{
  "id": "deliv_001",
  "projectId": "proj_001",
  "projectName": "Trevor Bradford - IDEA Website",
  "name": "Beta-ready website",
  "description": "Consolidated output document, UI polish, Strategic Brand Building Journey page, collapsible video component",
  "status": "in_progress",
  "priority": "P0",
  "deadline": {
    "internal": "2025-12-27",
    "clientFacing": "2025-12-27",
    "buffer": 0
  },
  "owner": "Matt Kerns",
  "estimatedHours": 16,
  "hoursInvested": 0,
  "dependencies": [],
  "blockers": [],
  "validation": {
    "internalQA": false,
    "clientDemoScheduled": false,
    "clientFeedbackReceived": false,
    "revisionsComplete": false,
    "finalSignOff": false,
    "paymentTriggered": false
  },
  "links": {
    "roadmap": "/active-projects/idea-framework-website/P1-PHASE-3-ROADMAP.md",
    "githubPR": null,
    "demoUrl": null
  }
}
```

### 7. Kanban Task Model

```json
{
  "id": "task_001",
  "deliverableId": "deliv_001",
  "projectId": "proj_001",
  "projectName": "Trevor Bradford - IDEA Website",
  "taskName": "Implement consolidated output document",
  "column": "in_progress",
  "owner": "Matt Kerns",
  "estimatedHours": 4,
  "hoursInvested": 0,
  "autoClaudeStatus": null,
  "blockers": [],
  "githubPR": {
    "url": null,
    "status": null
  },
  "notes": "Primary deliverable for Phase 3"
}
```

---

## Sample Data File (Phase 1 MVP)

### projects.json

```json
{
  "projects": [
    {
      "id": "proj_001",
      "name": "Trevor Bradford - IDEA Framework Website",
      "client": {
        "name": "Trevor Bradford",
        "company": "IDEA Brand Coach"
      },
      "phase": "quick_win",
      "phaseLabel": "Quick Win (Phase 3 Beta)",
      "status": "in_progress",
      "priority": "P0",
      "revenue": {
        "received": 500,
        "projected": 1500,
        "total": 2000
      },
      "deadline": "2025-12-27",
      "riskLevel": "high",
      "riskNotes": "Late delivery = lose ALL future revenue"
    },
    {
      "id": "proj_002",
      "name": "S&S Wolf Sheds - Process Automation",
      "client": {
        "name": "S&S Wolf Sheds",
        "company": "S&S Wolf Sheds"
      },
      "phase": "discovery",
      "phaseLabel": "Discovery Complete",
      "status": "pending",
      "priority": "P0",
      "revenue": {
        "received": 0,
        "projected": 10000,
        "total": 10000
      },
      "deadline": "2026-01-31",
      "riskLevel": "medium",
      "riskNotes": "Discovery complete, need to process and scope quick win"
    },
    {
      "id": "proj_003",
      "name": "Invoice & Receipts Processing Automation",
      "client": {
        "name": "Ascension Capital (Internal)",
        "company": "Internal"
      },
      "phase": "phase_2",
      "phaseLabel": "Phase 2 - Enhancement",
      "status": "in_progress",
      "priority": "P0",
      "revenue": {
        "received": 0,
        "projected": 2500,
        "total": 2500
      },
      "deadline": "2026-01-14",
      "riskLevel": "medium",
      "riskNotes": "Complex bug fixes, cap at 25 hours to protect margin"
    },
    {
      "id": "proj_004",
      "name": "Plotter Mechanix - Dashboard & Analytics",
      "client": {
        "name": "Plotter Mechanix",
        "company": "Plotter Mechanix"
      },
      "phase": "quick_win",
      "phaseLabel": "Quick Win (Phase 1)",
      "status": "in_progress",
      "priority": "P0",
      "revenue": {
        "received": 1250,
        "projected": 2500,
        "total": 3750
      },
      "deadline": "2026-01-15",
      "riskLevel": "low",
      "riskNotes": "Phase 1 paid, on track for Phase 2"
    },
    {
      "id": "proj_005",
      "name": "AntSavvy - Accounts AI Assistant",
      "client": {
        "name": "AntSavvy",
        "company": "AntSavvy"
      },
      "phase": "proposal",
      "phaseLabel": "Proposal Stage",
      "status": "pending",
      "priority": "P1",
      "revenue": {
        "received": 0,
        "projected": 1000,
        "total": 1000
      },
      "deadline": "2026-01-06",
      "riskLevel": "low",
      "riskNotes": "Demo delivered, awaiting feedback and close"
    },
    {
      "id": "proj_006",
      "name": "Goldfinch Data Annotation",
      "client": {
        "name": "Goldfinch (Freelance)",
        "company": "Freelance"
      },
      "phase": "execution",
      "phaseLabel": "Execution",
      "status": "in_progress",
      "priority": "P0",
      "revenue": {
        "received": 300,
        "projected": 4000,
        "total": 4300
      },
      "deadline": "2026-01-04",
      "riskLevel": "low",
      "riskNotes": "Straightforward execution, 8 hrs/day allocation"
    }
  ],
  "revenueSummary": {
    "received": 2050,
    "projected": 21500,
    "total": 23550
  }
}
```

---

## Data Sources (Phase 1)

### From Existing Documentation
1. **january-2026-revenue-kpis.md** → Revenue data
2. **january-2026-project-inventory.md** → Project list, phases, revenue
3. **active-projects/**/PROJECT-OVERVIEW.md** → Project details, status, deliverables
4. **active-projects/**/P*-ROADMAP.md** → Deliverables, timelines

### Manual Entry (Phase 1)
- Client contacts
- Process map stages
- Opportunity pipeline
- Pricing data
- Validation checklists

### Future Automation (Phase 3+)
- Parse markdown files automatically
- Sync with Git commits (auto-update)
- GitHub API for PR status
- Notion API for Kanban sync (if applicable)

---

## Database Considerations (Phase 3+)

If migrating to database (Supabase, Firebase, etc.):

### Tables
1. **projects** - Core project data
2. **clients** - Client information and contacts
3. **revenue** - Revenue breakdown by project/phase
4. **deliverables** - Deliverable tracking
5. **opportunities** - Sales pipeline
6. **pricing** - Pricing templates and history
7. **tasks** - Kanban tasks
8. **validation** - Deliverable validation checklists
9. **audit_log** - Changes and approvals

### Relationships
- `projects.client_id` → `clients.id`
- `deliverables.project_id` → `projects.id`
- `tasks.deliverable_id` → `deliverables.id`
- `revenue.project_id` → `projects.id`
- `opportunities.client_id` → `clients.id`

---

## API Endpoints (Phase 3+)

If building backend API:

### Read Operations
- `GET /api/projects` - List all projects
- `GET /api/projects/:id` - Get project details
- `GET /api/revenue/summary` - Revenue summary
- `GET /api/clients` - List all clients
- `GET /api/deliverables` - List deliverables (filter by project, status)
- `GET /api/opportunities` - Sales pipeline

### Write Operations (Phase 3+)
- `POST /api/projects` - Create new project
- `PUT /api/projects/:id` - Update project
- `PUT /api/deliverables/:id/status` - Update deliverable status
- `POST /api/validation/:id` - Update validation checklist

---

## Status Enums

### Project Status
- `not_started` - Project scoped but not begun
- `in_progress` - Active development
- `review` - In review/testing
- `blocked` - Blocked by external dependency
- `complete` - Delivered and accepted
- `on_hold` - Paused temporarily

### Deliverable Status
- `not_started` - Not yet begun
- `in_progress` - Actively working
- `review` - In review/testing
- `complete` - Done and validated

### Opportunity Stage
- `lead` - Initial contact
- `discovery` - Discovery call scheduled/complete
- `proposal` - Proposal sent
- `negotiation` - Negotiating terms
- `closed_won` - Deal closed successfully
- `closed_lost` - Opportunity lost

### Risk Level
- `low` - On track, no concerns
- `medium` - Minor issues or tight timeline
- `high` - Significant risk to delivery or revenue
- `critical` - Immediate intervention required

---

**Next Step:** Create sample data files for Phase 1 MVP (populate with current projects from january-2026-project-inventory.md)
