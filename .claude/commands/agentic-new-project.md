# Agentic New Project
> Create a new project in ../projects/ that uses agentic tools.

## Variables

- name: $ARGUMENTS

## Instructions

### 1. Validate Input

If no name provided, ask the user for a project name.

The name must be:
- Lowercase
- Start with a letter
- Contain only letters, numbers, and hyphens

### 2. Run Scaffold Tool

```bash
./run tools/scaffold.py project "$name"
```

This creates:
- `../projects/<name>/CLAUDE.md` - AI agent instructions
- `../projects/<name>/README.md` - Project readme
- `../projects/<name>/.gitignore` - Git ignore rules
- `../projects/<name>/notes/` - Working notes directory
- `../projects/<name>/templates/` - Document templates directory
- `../projects/<name>/deliverables/` - Final outputs directory

The tool also initializes a git repository in the project.

## Report

- Confirm project created at `../projects/<name>/`
- List the directory structure
- Provide next steps:
  1. `cd ../projects/<name>`
  2. Edit `CLAUDE.md` to add project context
  3. Open in VS Code alongside agentic workspace
