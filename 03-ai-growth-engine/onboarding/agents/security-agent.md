# Security Agent

**Type:** Claude Code Agent
**Status:** Specification
**Created:** 2026-01-18

---

## Purpose

Manage password vault access, enforce role-based credential access, monitor for credential expiry, and execute credential revocation at project close.

---

## Trigger

- **Event-based:** New credential stored, access granted, project closed
- **Scheduled:** Weekly credential audit (Sundays 6am PT)
- **Manual:** Credential revocation request

---

## Responsibilities

### 1. Manage Password Vault Access
- Create client vault/folder on project start
- Grant access to authorized team members
- Track all access grants with timestamps

### 2. Enforce Role-Based Access
- Verify access requests against role permissions
- Deny unauthorized access attempts
- Log all access events

### 3. Monitor Credential Health
- Check OAuth token expiry dates
- Alert on expiring API keys (30 days before)
- Flag unused credentials (no access > 30 days)

### 4. Execute Credential Revocation
- Trigger on project close
- Revoke team access to client vault
- Generate access audit log
- Archive vault (don't delete)

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Vault/Folder ID | 1Password/Bitwarden | Yes |
| Team Members | Notion/Config | Yes |
| Role Definitions | Config | Yes |
| Project Status | Notion | Yes |
| Credential Metadata | Vault API | Yes |

---

## Outputs

| Output | Destination | Format |
|--------|-------------|--------|
| Access Grant Confirmation | Slack/Notion | Notification |
| Expiry Alert | Slack #ops | Notification |
| Access Audit Log | Project folder | CSV/JSON |
| Revocation Confirmation | Slack + Email | Notification |

---

## Role-Based Access Control

### Role Definitions

| Role | Access Level | Credentials Visible | Duration |
|------|--------------|---------------------|----------|
| **Project Lead** | Full | All client credentials | Project duration |
| **Developer** | Limited | Assigned platforms only | Task duration |
| **Contractor** | Temporary | Specific items only | Time-limited (7 days max) |
| **Client** | Owner | Their own vault | Permanent |

### Access Matrix

```yaml
roles:
  project_lead:
    can_view: all
    can_edit: all
    can_share: true
    can_revoke: true

  developer:
    can_view: assigned_only
    can_edit: false
    can_share: false
    can_revoke: false

  contractor:
    can_view: specified_items
    can_edit: false
    can_share: false
    can_revoke: false
    time_limit: 7 days
```

---

## Credential Lifecycle

### 1. Creation (Logistics Onboarding Call)

```
[Client on Logistics Call]
        │
        ▼
[Screen share active]
        │
        ▼
[Client enters credentials into 1Password]
        │
        ▼
[Security Agent: Log credential creation]
        │
        ▼
[Grant Project Lead access]
        │
        ▼
[Log access grant to Notion]
```

### 2. Usage (Project Duration)

```
[Developer requests access]
        │
        ▼
[Security Agent: Verify role]
        │
        ├── Authorized ──▶ [Grant limited access]
        │                         │
        │                         ▼
        │                  [Log access grant]
        │
        └── Not Authorized ──▶ [Deny + Alert]
```

### 3. Review (Monthly Audit)

```
[Monthly Audit Trigger]
        │
        ▼
[Get all active credentials]
        │
        ▼
[For Each Credential]
        │
        ├──▶ [Check last accessed]
        │           │
        │           └── > 30 days ──▶ [Flag as unused]
        │
        ├──▶ [Check expiry date]
        │           │
        │           └── < 30 days ──▶ [Alert: Expiring soon]
        │
        └──▶ [Verify role still valid]
                    │
                    └── Role ended ──▶ [Revoke access]
```

### 4. Revocation (Project Close)

```
[Project Status → Completed]
        │
        ▼
[Security Agent: Revocation triggered]
        │
        ▼
[Get all team access grants for project]
        │
        ▼
[For Each Grant]
        │
        ├──▶ [Revoke access via vault API]
        │
        └──▶ [Log revocation]
        │
        ▼
[Generate Access Audit Log]
        │
        ▼
[Archive vault (don't delete)]
        │
        ▼
[Notify: "Credentials revoked for {{project}}"]
```

---

## Implementation

### 1Password CLI Integration

```bash
# Create client vault
op vault create "Client - {{client_name}}"

# Grant access to team member
op vault user grant \
  --vault "Client - {{client_name}}" \
  --user "{{team_member_email}}" \
  --permissions "view_items"

# Revoke access
op vault user revoke \
  --vault "Client - {{client_name}}" \
  --user "{{team_member_email}}"

# List vault access
op vault user list \
  --vault "Client - {{client_name}}"

# Get item metadata (for expiry check)
op item get "{{item_id}}" --format json
```

### Access Log Format

```json
{
  "event_id": "uuid",
  "timestamp": "2026-01-18T12:00:00Z",
  "event_type": "access_granted | access_revoked | credential_created | credential_accessed",
  "vault_id": "vault-uuid",
  "vault_name": "Client - Acme Corp",
  "item_id": "item-uuid (optional)",
  "item_name": "Make.com API Key (optional)",
  "actor": "security-agent | user@email.com",
  "target_user": "developer@arisegroup.ai",
  "role": "developer",
  "reason": "Project assignment | Project close | Manual revocation",
  "expires": "2026-01-25T12:00:00Z (optional)"
}
```

### Notion Credential Log Schema

```yaml
fields:
  - event_id: Text (title)
  - timestamp: Date
  - event_type: Select
  - project: Relation → Projects
  - client: Relation → Clients
  - vault_name: Text
  - item_name: Text
  - actor: Text
  - target_user: Text
  - role: Select
  - reason: Text
  - expires: Date
```

---

## Alerts

### Expiry Alert (30 days before)

```
:key: CREDENTIAL EXPIRY WARNING

Credential: {{item_name}}
Client: {{client_name}}
Expires: {{expiry_date}} ({{days_remaining}} days)

Action needed: Renew or rotate credential
Vault: {{vault_link}}
```

### Unused Credential Alert

```
:question: UNUSED CREDENTIAL

Credential: {{item_name}}
Client: {{client_name}}
Last Accessed: {{last_accessed}} ({{days_ago}} days ago)

Action: Verify if still needed or archive
Vault: {{vault_link}}
```

### Revocation Confirmation

```
:lock: CREDENTIALS REVOKED

Project: {{project_name}}
Client: {{client_name}}

Access Revoked For:
{{#each revoked_users}}
- {{email}} ({{role}})
{{/each}}

Total Credentials Archived: {{credential_count}}
Audit Log: {{audit_log_link}}

Vault Status: Archived (read-only)
```

---

## Security Policies

### Policy 1: No Plaintext Credentials
- Never store credentials in Slack, Email, or Notion
- Always use vault links, never copy credential values
- Alert if credential-like patterns detected in messages

### Policy 2: Minimum Necessary Access
- Grant access only to required credentials
- Use time-limited access for contractors
- Review and revoke unused access monthly

### Policy 3: Audit Trail
- Log all access events
- Retain logs for 12 months minimum
- Generate audit report on project close

### Policy 4: Secure Handoff
- At project close, client receives their vault ownership
- Team access revoked within 24 hours
- Credential rotation recommended post-handoff

---

## Error Handling

| Error | Action |
|-------|--------|
| Vault API unreachable | Retry 3x, alert ops, pause operations |
| Revocation fails | Log, retry, escalate to manual |
| Access grant fails | Notify requestor, log, investigate |
| Unauthorized access attempt | Block, alert security, investigate |

---

## Monitoring

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Revocation on project close | < 24 hours | > 48 hours |
| Expired credentials | 0 | Any expired |
| Unauthorized access attempts | 0 | Any attempt |
| Audit log completeness | 100% | Any gap |

---

## Configuration

```yaml
security_agent:
  vault_provider: "1password"  # or "bitwarden"

  role_definitions:
    project_lead:
      permissions: ["view_items", "edit_items", "share_items"]
    developer:
      permissions: ["view_items"]
    contractor:
      permissions: ["view_items"]
      max_duration_days: 7

  alerts:
    expiry_warning_days: 30
    unused_threshold_days: 30

  audit:
    retention_months: 12
    log_destination: "notion"  # or "file"

  policies:
    revoke_on_project_close: true
    archive_vault_on_close: true
    delete_vault_on_close: false
```

---

## Dependencies

- 1Password Teams/Business OR Bitwarden Organization
- 1Password CLI (`op`) or Bitwarden CLI (`bw`)
- Notion API for logging
- Slack API for notifications
- Cron scheduler for weekly audit
