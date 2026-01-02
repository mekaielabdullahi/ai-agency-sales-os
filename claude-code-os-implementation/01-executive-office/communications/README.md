# Communications Management System

**Last Updated:** 2025-12-12
**Purpose:** Organize and track all business communications by timeframe, business, and function

---

## Folder Structure

```
communications/
├── README.md (this file)
├── this-week/           # Current week communications
├── next-week/           # Next week planning
├── two-weeks-out/       # Future planning
└── templates/           # Reusable communication templates
```

### Each Week Folder Contains:

```
{week-folder}/
├── mindflux/
│   ├── sales/
│   │   └── christian-marangone.md
│   ├── dev/
│   │   └── turtle.md
│   └── antsavvy/
│       └── trissie.md
├── ascension-capital/
│   ├── board/
│   │   └── linh-le.md
│   └── clients/
│       └── [client-name].md
├── arisegroup/
│   ├── sales/
│   │   ├── chris-andrade.md
│   │   └── mekaiel-abdullahi.md
│   ├── dev/
│   │   └── trent-christopher.md
│   └── ops/
│       └── [team-member].md
├── brandvoice/
│   ├── client/
│   │   └── trevor-bradford.md
│   └── ops/
│       └── [team-member].md
├── plottermechanix/
│   ├── client/
│   │   └── kelce.md
│   └── ops/
│       └── [team-member].md
├── carpdigital/
│   ├── sales/
│   │   └── eric-mboura.md
│   └── prospects/
│       └── [prospect-name].md
├── icodemybusiness/
│   └── reminders/
│       └── [reminder-topic].md
└── unclassified/
    └── [person-name].md
```

---

## Business Taxonomy

### Mindflux
**Business:** Agency partner for sales + development
**Functions:**
- `sales/` - Christian Marangone (lead generation, deal closing)
- `dev/` - Turtle/Joshua (technical implementation)
- `antsavvy/` - AntSavvy project contacts (through Mindflux)
  - Trissie (Ops)

### Ascension Capital
**Business:** Linh Le's investment fund
**Functions:**
- `board/` - Linh Le (board member, strategic partner)
- `clients/` - Ascension Capital client projects (invoice automation)

### AriseGroup
**Business:** AI automation agency (our core business)
**Functions:**
- `sales/` - Chris Andrade (lead), Mekaiel Abdullahi (closer, systems)
- `dev/` - Trent Christopher (architect)
- `ops/` - Operations team

### BrandVoice
**Business:** Trevor Bradford's brand strategy company
**Functions:**
- `client/` - Trevor Bradford (paying client - IDEA Framework)
- `ops/` - BrandVoice team (if applicable)

### PlotterMechanix
**Business:** Kelce's printing/plotter services ($600K-$750K annually)
**Functions:**
- `client/` - Kelce (audit/prospect phase)
- `ops/` - PlotterMechanix team (if we engage with them)

### CarpDigital
**Business:** Eric Mboura's ecommerce company
**Functions:**
- `sales/` - Eric Mboura (ecommerce automation sales opportunity)
- `prospects/` - CarpDigital network prospects

### ICodeMyBusiness
**Business:** Matthew's personal organization
**Functions:**
- `reminders/` - Personal reminders and self-communications only
- Note: All clients now have their own business folders (BrandVoice, PlotterMechanix, CarpDigital)

### Unclassified
**Temporary holding area** for contacts where business context is not yet clear
**Action:** Each week, review and move to proper business folder

---

## Communication File Template

Each person gets a markdown file tracking their communications:

```markdown
# [Person Name] - Communications Log

**Business:** [Business Name]
**Function:** [sales/dev/ops/board/client/etc.]
**Relationship:** [Client/Partner/Team/Prospect]
**Last Contact:** [Date]

---

## This Week (Dec [X]-[Y])

### Planned Communications
- [ ] [Type] - [Purpose] - [Date]
- [ ] [Type] - [Purpose] - [Date]

### Actual Communications
- **[Date]:** [Summary of what was communicated]
- **[Date]:** [Summary of what was communicated]

### Action Items for Next Week
- [ ] [Action item]
- [ ] [Action item]

---

## Next Week (Dec [X]-[Y])

### Planned Communications
- [ ] [Type] - [Purpose] - [Date]

### Context to Remember
- [Important context for upcoming conversations]

---

## Two Weeks Out (Dec [X]-[Y])

### Planned Communications
- [ ] [Type] - [Purpose] - [Date]

---

## Communication History (Recent)

### [Date Range]
- **[Date]:** [Summary]
- **[Date]:** [Summary]

---

## Notes
- [Ongoing context, preferences, important background]
```

---

## Weekly Workflow

### Sunday Evening (Weekly Planning)
1. **Review this-week folder**
   - What got communicated?
   - What's still pending?
   - What needs to roll to next week?

2. **Plan next-week folder**
   - Move next-week → this-week
   - Move two-weeks-out → next-week
   - Create new two-weeks-out folder

3. **Classify unclassified contacts**
   - Review unclassified/ folder
   - Research business context
   - Move to proper business/function folder
   - **Goal:** Keep unclassified/ empty or minimal

### Daily Check-in
- Review this-week/ communications
- Update actual communications as they happen
- Note action items for follow-up

---

## Migration Plan

### Step 1: Extract from communications-plan.md
- [x] Create folder structure
- [x] Extract Trevor → brandvoice/client/trevor-bradford.md
- [x] Extract Eric → carpdigital/sales/eric-mboura.md
- [x] Extract Kelce → plottermechanix/client/kelce.md
- [x] Extract Chris → arisegroup/sales/chris-andrade.md
- [x] Extract Mekaiel → arisegroup/sales/mekaiel-abdullahi.md
- [x] Extract Trent → arisegroup/dev/trent-christopher.md
- [x] Extract Linh → ascension-capital/board/linh-le.md
- [x] Extract Christian → mindflux/sales/christian-marangone.md
- [x] Extract Turtle → mindflux/dev/turtle.md
- [x] Extract Trissie → mindflux/antsavvy/trissie.md

### Step 2: Populate This Week (Dec 9-15)
- [ ] Move all current-week communications to this-week/
- [ ] Create next-week/ for Dec 16-22
- [ ] Create two-weeks-out/ for Dec 23-29

### Step 3: Archive Old communications-plan.md
- [ ] Keep as archive/communications-plan-archive.md
- [ ] Reference from new system
- [ ] Update links in other documents

---

## Unclassified Workflow

**When you add someone to unclassified/:**
1. Create file: `unclassified/[firstname-lastname].md`
2. Add to weekly review checklist: "Classify [Name]"
3. Within 1 week, research:
   - What business are they in?
   - What function do they serve?
   - Where do they belong in taxonomy?
4. Move to proper folder once classified

**Example:**
```
Meet "John Smith" at networking event
→ Create unclassified/john-smith.md
→ Weekly review: Research John's business
→ Discover: John runs "Smith Consulting"
→ Decide: Create new business or map to existing?
→ Move john-smith.md to proper location
```

---

## Adding New Businesses

**When a business doesn't fit existing taxonomy:**

1. **Evaluate:** Is this recurring? Will we have multiple contacts here?
2. **If YES:** Create new business folder
   ```bash
   mkdir -p communications/this-week/[business-name]/{function1,function2}
   ```
3. **If NO:** Use icodemybusiness/prospects/ or icodemybusiness/partners/
4. **Document:** Add to this README under Business Taxonomy

---

## Business Classification Rules

### Mindflux
- People working WITH us on client projects
- Sales: Finding clients for joint delivery
- Dev: Technical implementation partners

### Ascension Capital
- Linh's investment fund and related entities
- Board: Strategic oversight, investment decisions
- Ops: Fund operations (if we interact with team)

### AriseGroup
- Our core AI automation agency
- Sales: Our sales team (Chris, Mekaiel)
- Dev: Our dev team (Trent, future hires)
- Ops: Our operations team

### ICodeMyBusiness
- Matthew's personal consulting brand
- Clients: Paying clients (Trevor, Eric, Kelce)
- Prospects: Pipeline (not yet paying)
- Partners: Referral sources, strategic allies

### When Unclear
**Start with unclassified/** - don't force premature categorization

---

## Templates

Templates are stored in `templates/` and can be copied for common communication types:

- `client-update.md` - Progress update to paying client
- `prospect-follow-up.md` - Following up with prospect
- `team-check-in.md` - Weekly partner check-in
- `project-proposal.md` - Proposal for new project
- `demo-delivery.md` - Delivering demo video

---

## Success Metrics

### Weekly Review Questions:
- [ ] Are all active communications tracked?
- [ ] Is unclassified/ folder empty or minimal?
- [ ] Are next-week communications planned?
- [ ] Are action items from this week captured?
- [ ] Do we have clear context for upcoming conversations?

### Monthly Audit:
- [ ] Review all business folders for accuracy
- [ ] Archive inactive contacts
- [ ] Update business taxonomy if needed
- [ ] Clean up any duplicates
- [ ] Ensure templates are current

---

**Created:** 2025-12-12
**Next Review:** Weekly (Sunday evenings)
**Maintained By:** Matthew (Executive Office)
