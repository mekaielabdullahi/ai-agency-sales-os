# agentic-module-proposal

Generate sales proposals and create Google Slides presentations from templates.

## Features

- Validate proposal JSON structure (24 required fields)
- Copy Google Slides templates
- Replace text placeholders with proposal data
- Support for Service Account and OAuth authentication

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-proposal
```

## Setup

### Google OAuth

1. Create OAuth credentials in Google Cloud Console
2. Download `credentials.json` to workspace root
3. Run any command - it will prompt for authorization
4. `token.json` will be created for future use

### Environment Variables

```
GOOGLE_SLIDES_TEMPLATE_ID=your-template-id
```

## Slash Commands

```
/proposal <company_info>
```

## CLI Usage

```bash
# Validate proposal JSON
echo '<json>' | ./run tools/generate_proposal.py

# Generate slides from validated JSON
echo '<json>' | ./run tools/generate_proposal.py | ./run tools/copy_slides_template.py <template_id>
```

## Workflow

1. Gather prospect information (name, website, problem, solution, timeline)
2. Generate proposal JSON following the schema
3. Validate with `/proposal` command
4. Review the generated Google Slides presentation

## Proposal Schema

The proposal requires exactly 24 fields including:
- Title and subtitle
- Overview and objective
- 4 problem statements
- 3 process steps with descriptions
- Deliverables
- 3 benefit metrics with values (max 6 chars each)

See `runbook/generate_proposal.md` for the complete schema and field generation rules.
