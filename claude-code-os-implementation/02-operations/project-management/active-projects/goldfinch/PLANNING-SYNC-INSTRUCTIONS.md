# Goldfinch Planning Sync Instructions

This project folder contains the strategic planning docs for the Goldfinch reusable Android components project. The actual development happens in a separate workspace.

---

## Folder Mapping

| Source (This Project) | Destination (Dev Workspace) |
|-----------------------|----------------------------|
| `COMPONENT-ROADMAP.md` | `~/workspace/dataAnnotation/goldfinch/projects/smb-chat-app/docs/COMPONENT-ROADMAP.md` |
| `PROJECT-OVERVIEW.md` | Reference only (not synced) |
| `components/chat-voice-widget/*` | Reference for implementation |

---

## Sync Commands

### Sync Component Roadmap
```bash
cp /Users/matthewkerns/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/active-projects/goldfinch/COMPONENT-ROADMAP.md \
   /Users/matthewkerns/workspace/dataAnnotation/goldfinch/projects/smb-chat-app/docs/
```

### Sync All Docs (if needed)
```bash
# Component roadmap
cp /Users/matthewkerns/workspace/ai-agency-development-os/claude-code-os-implementation/02-operations/project-management/active-projects/goldfinch/COMPONENT-ROADMAP.md \
   /Users/matthewkerns/workspace/dataAnnotation/goldfinch/projects/smb-chat-app/docs/

# Add additional sync commands here as docs are added
```

---

## Development Workspace Structure

```
~/workspace/dataAnnotation/goldfinch/
├── projects/
│   └── smb-chat-app/          # Main development project
│       ├── app/               # Android app source
│       └── docs/              # <-- Synced docs go here
│           ├── COMPONENT-ROADMAP.md
│           ├── CHAT_WIDGET_IMPLEMENTATION.md
│           └── GOOGLE_DRIVE_SETUP.md
├── workflow/
│   └── documentation/
│       └── PROJECT_ROADMAP.md # Bug patterns for data annotation
└── goldfinch-001/             # First submission (completed)
```

---

## When to Sync

Sync documentation after:
1. Updating `COMPONENT-ROADMAP.md` with new components or progress
2. Adding new planning docs that developers need
3. Completing a component (update build log)

---

## Notes

- The agency project tracks strategic planning and component roadmap
- The dataAnnotation workspace is where actual coding happens
- Keep both in sync to maintain single source of truth for component planning

---

**Created:** 2025-12-26
