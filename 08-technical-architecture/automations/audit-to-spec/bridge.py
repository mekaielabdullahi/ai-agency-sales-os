#!/usr/bin/env python3
"""
Audit-to-Spec Bridge
====================
Converts AI audit outputs (audit.json) into Auto-Claude buildable specs.

This bridges the Onboarding OS → Development OS in your agency workflow.

Usage:
    python bridge.py --audit path/to/audit.json --output path/to/project
    python bridge.py --audit audit.json --output ./build --top 3
    python bridge.py --audit audit.json --list  # List opportunities only
"""

import json
import os
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional


def load_audit(audit_path: str) -> dict:
    """Load and validate audit.json file."""
    with open(audit_path, 'r', encoding='utf-8') as f:
        audit = json.load(f)

    required_fields = ['audit_brief', 'ai_opportunity_matrix']
    for field in required_fields:
        if field not in audit:
            raise ValueError(f"Audit missing required field: {field}")

    return audit


def extract_opportunities(audit: dict) -> list:
    """Extract and rank opportunities from audit."""
    opportunities = audit.get('ai_opportunity_matrix', [])

    # Also check current_state_maps for pain points that could be opportunities
    pain_points = []
    for process in audit.get('current_state_maps', []):
        for pp in process.get('pain_points', []):
            if pp.get('impact') in ['CRITICAL', 'high']:
                pain_points.append({
                    'process_name': process.get('name'),
                    'description': pp.get('description'),
                    'impact': pp.get('impact'),
                    'revenue_impact': pp.get('revenue_impact', 'Unknown'),
                    'quote': pp.get('kelce_quote') or pp.get('alyssa_quote', '')
                })

    # Sort opportunities by priority_score (descending)
    sorted_opps = sorted(
        opportunities,
        key=lambda x: x.get('priority_score', 0),
        reverse=True
    )

    return sorted_opps, pain_points


def generate_spec_md(audit: dict, opportunity: dict, pain_points: list) -> str:
    """Generate Auto-Claude spec.md from audit and opportunity."""

    brief = audit.get('audit_brief', {})
    company = brief.get('company_name', 'Unknown Company')
    industry = brief.get('industry', 'Unknown Industry')

    # Find related pain points
    related_pains = [
        pp for pp in pain_points
        if opportunity.get('process_id', '') in pp.get('process_name', '').lower() or
           any(word in pp.get('description', '').lower()
               for word in opportunity.get('description', '').lower().split()[:3])
    ]

    # Build the spec
    spec = f"""# Specification: {company} - {opportunity.get('process_name', 'AI Solution')}

## Overview

{opportunity.get('description', 'AI-powered automation solution')} for {company}, a {industry} business.

**Source**: AriseGroup AI Audit ({audit.get('client_id', 'unknown')})
**Priority Score**: {opportunity.get('priority_score', 'N/A')}/10
**Category**: {opportunity.get('category', 'Automation')}

## Workflow Type

**Type**: {opportunity.get('type', 'feature').lower()}

**Rationale**: {_get_workflow_rationale(opportunity)}

## Business Context

**Client**: {company}
**Industry**: {industry}
**Company Size**: {brief.get('company_size', 'Unknown')}
**Annual Revenue**: {brief.get('annual_revenue', 'Unknown')}

### Key Stakeholders
"""

    # Add stakeholders
    stakeholders = brief.get('stakeholders', {})
    if stakeholders.get('primary_contact'):
        contact = stakeholders['primary_contact']
        spec += f"- **{contact.get('name', 'Primary Contact')}** ({contact.get('role', 'Unknown Role')})\n"

    for dm in stakeholders.get('decision_makers', []):
        spec += f"- {dm}\n"

    spec += f"""
## Task Scope

### Impact Assessment
- **Time Saved**: {opportunity.get('impact_details', {}).get('time_saved', 'TBD')}
- **Cost Reduction**: {opportunity.get('impact_details', {}).get('cost_reduction', 'TBD')}
- **Revenue Impact**: {opportunity.get('impact_details', {}).get('revenue_impact', 'TBD')}
- **Quality Improvement**: {opportunity.get('impact_details', {}).get('quality_improvement', 'TBD')}

### This Task Will:
"""

    # Generate task items from opportunity details
    for i, dep in enumerate(opportunity.get('dependencies', []), 1):
        spec += f"- [ ] {dep}\n"

    if not opportunity.get('dependencies'):
        spec += f"- [ ] Implement {opportunity.get('description', 'solution')}\n"
        spec += f"- [ ] Integrate with existing systems\n"
        spec += f"- [ ] Test and validate functionality\n"

    spec += f"""
### Out of Scope:
"""
    for item in brief.get('scope', {}).get('out_of_scope', ['Items not specified in requirements']):
        spec += f"- {item}\n"

    spec += f"""
## Technical Context

### Existing Tech Stack
"""
    for tech in brief.get('tech_stack', ['Not specified']):
        spec += f"- {tech}\n"

    spec += f"""
### Integration Points
"""
    for i, point in enumerate(opportunity.get('data_requirements', ['TBD']), 1):
        spec += f"{i}. {point}\n"

    spec += f"""
## Pain Points Addressed
"""
    if related_pains:
        for pp in related_pains[:3]:
            quote = f'\n   > "{pp["quote"]}"' if pp.get('quote') else ''
            spec += f"""
### {pp.get('description', 'Pain Point')[:80]}
- **Impact**: {pp.get('impact', 'Unknown')}
- **Revenue Impact**: {pp.get('revenue_impact', 'Unknown')}{quote}
"""
    else:
        spec += "- See audit.json for detailed pain point analysis\n"

    spec += f"""
## Requirements

### Functional Requirements
"""
    # Generate from opportunity
    spec += f"""
1. **Core Functionality**
   - Description: {opportunity.get('description', 'TBD')}
   - Acceptance: System performs as specified

2. **Integration**
   - Description: Connects with existing {', '.join(brief.get('tech_stack', ['systems'])[:2])}
   - Acceptance: Data flows correctly between systems

3. **User Experience**
   - Description: Minimal training required for staff
   - Acceptance: Staff can use within 30 minutes of introduction

### Edge Cases
"""
    for risk in opportunity.get('risks', []):
        spec += f"1. **{risk.get('risk', 'Unknown Risk')}** - {risk.get('mitigation', 'Handle gracefully')}\n"

    if not opportunity.get('risks'):
        spec += "1. **System offline** - Queue operations and retry\n"
        spec += "2. **Invalid input** - Validate and provide clear error messages\n"

    spec += f"""
## Implementation Notes

### Effort Estimate
- **Technical Complexity**: {opportunity.get('effort_details', {}).get('technical_complexity', opportunity.get('effort', 'medium'))}
- **Integration Points**: {opportunity.get('effort_details', {}).get('integration_points', 'TBD')}
- **Estimated Build Time**: {opportunity.get('effort_details', {}).get('estimated_build_time', opportunity.get('speed_to_value', 'TBD'))}

### Constraints
"""
    constraints = brief.get('constraints', {})
    if constraints.get('budget'):
        spec += f"- **Budget**: {constraints['budget']}\n"
    if constraints.get('timeline'):
        spec += f"- **Timeline**: {constraints['timeline']}\n"
    for tech_constraint in constraints.get('technical', [])[:3]:
        spec += f"- {tech_constraint}\n"

    spec += f"""
### DO
- Follow existing patterns in the client's tech stack
- Prioritize reliability over features
- Document all API integrations
- Create clear error messages for users

### DON'T
- Over-engineer the solution
- Require extensive training
- Break existing workflows
- Store sensitive data insecurely

## Success Criteria

The task is complete when:

1. [ ] Core functionality works as specified
2. [ ] Integrates with existing systems ({', '.join(brief.get('tech_stack', ['TBD'])[:2])})
3. [ ] Staff can use without extensive training
4. [ ] Error handling covers edge cases
5. [ ] Documentation is complete
6. [ ] Client accepts the solution

## QA Acceptance Criteria

### Functional Tests
| Test | What to Verify |
|------|----------------|
| Happy path | Core workflow completes successfully |
| Error handling | System recovers gracefully from failures |
| Integration | Data syncs correctly with existing systems |

### User Acceptance
| Check | Expected |
|-------|----------|
| Staff can complete workflow | Within 5 minutes |
| No training required | Self-explanatory UI |
| Errors are clear | Users know how to resolve |

### QA Sign-off Requirements
- [ ] All functional tests pass
- [ ] Integration tests pass
- [ ] User acceptance verified
- [ ] No security vulnerabilities
- [ ] Documentation reviewed

---

## Audit Reference

**Audit ID**: {audit.get('client_id', 'unknown')}
**Audit Date**: {audit.get('created_date', 'Unknown')}
**Audit Status**: {audit.get('audit_status', 'Unknown')}

### ROI Calculation
- **Speed to Value**: {opportunity.get('speed_to_value', 'TBD')}
- **Priority Score**: {opportunity.get('priority_score', 'N/A')}/10

### Notes from Audit
"""
    for note in audit.get('notes', [])[-3:]:
        spec += f"- [{note.get('date', '')}] {note.get('note', '')[:100]}...\n"

    return spec


def _get_workflow_rationale(opportunity: dict) -> str:
    """Generate workflow type rationale."""
    opp_type = opportunity.get('type', 'Automation').lower()
    if 'automation' in opp_type:
        return "New automation system to replace manual processes"
    elif 'enhancement' in opp_type:
        return "AI enhancement to existing workflow"
    elif 'integration' in opp_type:
        return "Integration between existing systems"
    else:
        return "Feature implementation based on audit findings"


def generate_requirements_json(audit: dict, opportunity: dict) -> dict:
    """Generate Auto-Claude requirements.json from audit and opportunity."""

    brief = audit.get('audit_brief', {})

    return {
        "task_description": opportunity.get('description', 'AI automation solution'),
        "workflow_type": opportunity.get('type', 'feature').lower().replace(' ', '_'),
        "source": {
            "type": "ai_audit",
            "audit_id": audit.get('client_id', 'unknown'),
            "audit_date": audit.get('created_date', 'Unknown'),
            "opportunity_id": opportunity.get('id', 'unknown'),
            "priority_score": opportunity.get('priority_score', 0),
            "category": opportunity.get('category', 'Automation')
        },
        "client": {
            "name": brief.get('company_name', 'Unknown'),
            "industry": brief.get('industry', 'Unknown'),
            "primary_contact": brief.get('stakeholders', {}).get('primary_contact', {}).get('name', 'Unknown'),
            "company_size": brief.get('company_size', 'Unknown'),
            "annual_revenue": brief.get('annual_revenue', 'Unknown')
        },
        "impact": {
            "time_saved": opportunity.get('impact_details', {}).get('time_saved', 'TBD'),
            "cost_reduction": opportunity.get('impact_details', {}).get('cost_reduction', 'TBD'),
            "revenue_impact": opportunity.get('impact_details', {}).get('revenue_impact', 'TBD'),
            "quality_improvement": opportunity.get('impact_details', {}).get('quality_improvement', 'TBD')
        },
        "effort": {
            "complexity": opportunity.get('effort_details', {}).get('technical_complexity', opportunity.get('effort', 'medium')),
            "integration_points": opportunity.get('effort_details', {}).get('integration_points', 0),
            "estimated_time": opportunity.get('effort_details', {}).get('estimated_build_time', opportunity.get('speed_to_value', 'TBD'))
        },
        "acceptance_criteria": [
            "Core functionality works as specified",
            f"Integrates with existing systems: {', '.join(brief.get('tech_stack', ['TBD'])[:3])}",
            "Staff can use without extensive training",
            "Error handling covers edge cases",
            "Documentation is complete"
        ],
        "constraints": brief.get('constraints', {}),
        "risks": opportunity.get('risks', []),
        "dependencies": opportunity.get('dependencies', []),
        "data_requirements": opportunity.get('data_requirements', []),
        "generated_at": datetime.now().isoformat(),
        "generated_by": "audit-to-spec-bridge"
    }


def create_project_folder(output_path: str, spec_name: str) -> Path:
    """Create project folder with git init if needed."""
    project_path = Path(output_path)
    spec_dir = project_path / '.auto-claude' / 'specs' / spec_name

    # Create directories
    spec_dir.mkdir(parents=True, exist_ok=True)

    # Git init if not already a repo
    git_dir = project_path / '.git'
    if not git_dir.exists():
        subprocess.run(['git', 'init'], cwd=project_path, capture_output=True)
        print(f"  Initialized git repo: {project_path}")

    return spec_dir


def list_opportunities(audit: dict) -> None:
    """Print list of opportunities from audit."""
    import sys
    import io
    # Fix Windows encoding issues
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    opportunities, pain_points = extract_opportunities(audit)

    brief = audit.get('audit_brief', {})
    print(f"\n{'='*60}")
    print(f"AUDIT: {brief.get('company_name', 'Unknown')} ({audit.get('client_id', 'unknown')})")
    print(f"{'='*60}")
    print(f"Industry: {brief.get('industry', 'Unknown')}")
    print(f"Revenue: {brief.get('annual_revenue', 'Unknown')}")
    print(f"Status: {audit.get('audit_status', 'Unknown')}")

    print(f"\n{'='*60}")
    print("AI OPPORTUNITIES (sorted by priority)")
    print(f"{'='*60}")

    for i, opp in enumerate(opportunities, 1):
        print(f"\n{i}. [{opp.get('priority_score', '?')}/10] {opp.get('process_name', 'Unknown')}")
        print(f"   Type: {opp.get('type', 'Unknown')} | Category: {opp.get('category', 'Unknown')}")
        print(f"   Impact: {opp.get('impact', 'Unknown')} | Effort: {opp.get('effort', 'Unknown')}")
        print(f"   Speed to Value: {opp.get('speed_to_value', 'TBD')}")
        desc = opp.get('description', 'No description')[:80]
        print(f"   {desc}...")

    print(f"\n{'='*60}")
    print(f"CRITICAL PAIN POINTS ({len([p for p in pain_points if p.get('impact') == 'CRITICAL'])} critical)")
    print(f"{'='*60}")

    for pp in pain_points[:5]:
        print(f"\n- [{pp.get('impact', '?')}] {pp.get('description', 'Unknown')[:70]}...")
        if pp.get('quote'):
            print(f'  > "{pp["quote"][:60]}..."')


def generate_specs(
    audit_path: str,
    output_path: str,
    top_n: int = 1,
    opportunity_id: Optional[str] = None
) -> list:
    """Generate Auto-Claude specs from audit."""

    audit = load_audit(audit_path)
    opportunities, pain_points = extract_opportunities(audit)

    if opportunity_id:
        # Find specific opportunity
        opportunities = [o for o in opportunities if o.get('id') == opportunity_id]
        if not opportunities:
            raise ValueError(f"Opportunity not found: {opportunity_id}")

    # Take top N opportunities
    selected = opportunities[:top_n]
    generated = []

    brief = audit.get('audit_brief', {})
    company_slug = brief.get('company_name', 'unknown').lower().replace(' ', '-')

    for i, opp in enumerate(selected, 1):
        opp_slug = opp.get('process_name', f'opp-{i}').lower().replace(' ', '-').replace('&', 'and')[:30]
        spec_name = f"{str(i).zfill(3)}-{company_slug}-{opp_slug}"

        print(f"\nGenerating spec {i}/{len(selected)}: {spec_name}")

        # Create project folder and spec directory
        spec_dir = create_project_folder(output_path, spec_name)

        # Generate spec.md
        spec_content = generate_spec_md(audit, opp, pain_points)
        spec_file = spec_dir / 'spec.md'
        spec_file.write_text(spec_content, encoding='utf-8')
        print(f"  Created: {spec_file}")

        # Generate requirements.json
        req_content = generate_requirements_json(audit, opp)
        req_file = spec_dir / 'requirements.json'
        req_file.write_text(json.dumps(req_content, indent=2), encoding='utf-8')
        print(f"  Created: {req_file}")

        generated.append({
            'spec_name': spec_name,
            'spec_path': str(spec_file),
            'requirements_path': str(req_file),
            'opportunity': opp.get('process_name'),
            'priority_score': opp.get('priority_score')
        })

    return generated


def main():
    parser = argparse.ArgumentParser(
        description='Convert AI audit to Auto-Claude specs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python bridge.py --audit audit.json --list
  python bridge.py --audit audit.json --output ./build
  python bridge.py --audit audit.json --output ./build --top 3
  python bridge.py --audit audit.json --output ./build --id opp_001
        """
    )

    parser.add_argument(
        '--audit', '-a',
        required=True,
        help='Path to audit.json file'
    )

    parser.add_argument(
        '--output', '-o',
        help='Output project directory (will create if needed)'
    )

    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List opportunities without generating specs'
    )

    parser.add_argument(
        '--top', '-t',
        type=int,
        default=1,
        help='Number of top opportunities to generate specs for (default: 1)'
    )

    parser.add_argument(
        '--id', '-i',
        help='Generate spec for specific opportunity ID'
    )

    args = parser.parse_args()

    # Validate audit file exists
    if not os.path.exists(args.audit):
        print(f"Error: Audit file not found: {args.audit}")
        return 1

    if args.list:
        # Just list opportunities
        audit = load_audit(args.audit)
        list_opportunities(audit)
        return 0

    if not args.output:
        print("Error: --output required when generating specs")
        return 1

    # Generate specs
    print(f"\n{'='*60}")
    print("AUDIT-TO-SPEC BRIDGE")
    print(f"{'='*60}")
    print(f"Audit: {args.audit}")
    print(f"Output: {args.output}")
    print(f"Top N: {args.top}")

    generated = generate_specs(
        args.audit,
        args.output,
        top_n=args.top,
        opportunity_id=args.id
    )

    print(f"\n{'='*60}")
    print("GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Generated {len(generated)} spec(s):\n")

    for g in generated:
        print(f"  [{g['priority_score']}/10] {g['opportunity']}")
        print(f"         → {g['spec_path']}")

    print(f"\nNext steps:")
    print(f"  1. Open Auto-Claude")
    print(f"  2. Open project: {args.output}")
    print(f"  3. Start the build from the Kanban board")

    return 0


if __name__ == '__main__':
    exit(main())
