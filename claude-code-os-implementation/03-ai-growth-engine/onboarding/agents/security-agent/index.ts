/**
 * Security Agent
 *
 * Manages credential lifecycle, password vault access, and security compliance.
 *
 * Trigger: Credential events + weekly security audit (Fridays 9am PT)
 *
 * Responsibilities:
 * 1. Manage 1Password vault access (create vaults, grant/revoke access)
 * 2. Enforce role-based credential access
 * 3. Monitor for credential expiry (OAuth tokens, API keys)
 * 4. Track credential access audit logs
 * 5. Execute credential revocation at project close
 */

import {
  createClientVault,
  grantVaultAccess,
  revokeVaultAccess,
  getVaultItems,
  getExpiringItems,
  getAccessLogs,
  VaultItem,
  AccessLog,
} from './handlers/onepassword';
import {
  getActiveProjects,
  getCompletedProjects,
  logSecurityEvent,
  getProjectTeam,
} from './handlers/notion';
import { sendSecurityAlert, notifyCredentialExpiry } from './handlers/notifications';

export interface SecurityCheckResult {
  success: boolean;
  vaults_audited: number;
  expiring_credentials: ExpiringCredential[];
  access_revoked: RevokedAccess[];
  security_alerts: SecurityAlert[];
  timestamp: string;
}

export interface ExpiringCredential {
  vault: string;
  item_name: string;
  expires_at: string;
  days_until_expiry: number;
}

export interface RevokedAccess {
  vault: string;
  user_email: string;
  reason: string;
  revoked_at: string;
}

export interface SecurityAlert {
  type: 'unauthorized_access' | 'credential_exposed' | 'policy_violation';
  severity: 'low' | 'medium' | 'high' | 'critical';
  message: string;
  timestamp: string;
}

// Role-based access levels
export const ACCESS_ROLES = {
  PROJECT_LEAD: ['vault_admin', 'item_read', 'item_write'],
  DEVELOPER: ['item_read'],
  CONTRACTOR: ['item_read'], // Time-limited
  CLIENT: ['item_read'], // Own vault only
} as const;

// Credential expiry warning thresholds (days)
const EXPIRY_WARNING_DAYS = [30, 14, 7, 3, 1];

/**
 * Main security check execution
 * Run weekly on Fridays at 9am PT
 */
export async function executeSecurityAudit(): Promise<SecurityCheckResult> {
  const result: SecurityCheckResult = {
    success: false,
    vaults_audited: 0,
    expiring_credentials: [],
    access_revoked: [],
    security_alerts: [],
    timestamp: new Date().toISOString(),
  };

  console.log('[SecurityAgent] Starting weekly security audit...');

  try {
    // Get all active projects
    const activeProjects = await getActiveProjects();
    const completedProjects = await getCompletedProjects();

    // Audit each project vault
    for (const project of activeProjects) {
      result.vaults_audited++;
      const vaultName = `client-${project.slug}`;

      // Check for expiring credentials
      const expiring = await getExpiringItems(vaultName, 30);
      for (const item of expiring) {
        const credential: ExpiringCredential = {
          vault: vaultName,
          item_name: item.title,
          expires_at: item.expires_at!,
          days_until_expiry: item.days_until_expiry!,
        };
        result.expiring_credentials.push(credential);

        // Send notification if in warning threshold
        if (EXPIRY_WARNING_DAYS.includes(item.days_until_expiry!)) {
          await notifyCredentialExpiry(credential, project);
        }
      }

      // Verify team access is current
      const projectTeam = await getProjectTeam(project.id);
      const accessLogs = await getAccessLogs(vaultName);

      // Check for unauthorized access
      for (const log of accessLogs) {
        if (!projectTeam.some((member) => member.email === log.user_email)) {
          result.security_alerts.push({
            type: 'unauthorized_access',
            severity: 'high',
            message: `Unauthorized access to ${vaultName} by ${log.user_email}`,
            timestamp: log.timestamp,
          });
        }
      }
    }

    // Revoke access for completed projects (after 30 days)
    const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

    for (const project of completedProjects) {
      const completedAt = new Date(project.completed_at);
      if (completedAt < thirtyDaysAgo) {
        const vaultName = `client-${project.slug}`;

        // Revoke all team access
        const team = await getProjectTeam(project.id);
        for (const member of team) {
          if (member.role !== 'CLIENT') {
            try {
              await revokeVaultAccess(vaultName, member.email);
              result.access_revoked.push({
                vault: vaultName,
                user_email: member.email,
                reason: 'Project completed > 30 days',
                revoked_at: new Date().toISOString(),
              });
            } catch (error) {
              console.error(`[SecurityAgent] Failed to revoke access for ${member.email}:`, error);
            }
          }
        }

        // Log security event
        await logSecurityEvent({
          project_id: project.id,
          event_type: 'credential_revocation',
          details: `Revoked team access to ${vaultName} (project completed > 30 days)`,
        });
      }
    }

    result.success = true;
    console.log(
      `[SecurityAgent] Audit complete. ${result.vaults_audited} vaults, ${result.expiring_credentials.length} expiring, ${result.access_revoked.length} revoked`
    );

    // Send summary alert if issues found
    if (result.security_alerts.length > 0 || result.expiring_credentials.length > 0) {
      await sendSecurityAlert(result);
    }
  } catch (error) {
    console.error('[SecurityAgent] Error during audit:', error);
  }

  return result;
}

/**
 * Create vault for new client project
 */
export async function setupClientVault(
  projectId: string,
  clientName: string,
  projectLead: string
): Promise<string> {
  const slug = clientName.toLowerCase().replace(/[^a-z0-9]/g, '-');
  const vaultName = `client-${slug}`;

  console.log(`[SecurityAgent] Creating vault: ${vaultName}`);

  // Create vault
  await createClientVault(vaultName, `Credentials for ${clientName}`);

  // Grant project lead admin access
  await grantVaultAccess(vaultName, projectLead, 'PROJECT_LEAD');

  // Log event
  await logSecurityEvent({
    project_id: projectId,
    event_type: 'vault_created',
    details: `Created vault ${vaultName} with ${projectLead} as admin`,
  });

  return vaultName;
}

/**
 * Grant team member access to vault
 */
export async function grantTeamAccess(
  vaultName: string,
  email: string,
  role: keyof typeof ACCESS_ROLES,
  projectId: string
): Promise<void> {
  await grantVaultAccess(vaultName, email, role);

  await logSecurityEvent({
    project_id: projectId,
    event_type: 'access_granted',
    details: `Granted ${role} access to ${email} for ${vaultName}`,
  });
}

/**
 * Handle project completion - schedule credential revocation
 */
export async function handleProjectComplete(projectId: string, vaultName: string): Promise<void> {
  console.log(`[SecurityAgent] Project ${projectId} completed, scheduling credential revocation in 30 days`);

  await logSecurityEvent({
    project_id: projectId,
    event_type: 'revocation_scheduled',
    details: `Credential revocation scheduled for ${vaultName} in 30 days`,
  });

  // The weekly audit will handle actual revocation after 30 days
}

/**
 * Emergency credential revocation
 */
export async function emergencyRevoke(
  vaultName: string,
  reason: string,
  projectId: string
): Promise<void> {
  console.log(`[SecurityAgent] EMERGENCY: Revoking all access to ${vaultName}`);

  const team = await getProjectTeam(projectId);

  for (const member of team) {
    try {
      await revokeVaultAccess(vaultName, member.email);
    } catch (error) {
      console.error(`[SecurityAgent] Failed to revoke ${member.email}:`, error);
    }
  }

  await logSecurityEvent({
    project_id: projectId,
    event_type: 'emergency_revocation',
    details: `Emergency revocation: ${reason}`,
  });

  await sendSecurityAlert({
    success: true,
    vaults_audited: 1,
    expiring_credentials: [],
    access_revoked: team.map((m) => ({
      vault: vaultName,
      user_email: m.email,
      reason: `Emergency: ${reason}`,
      revoked_at: new Date().toISOString(),
    })),
    security_alerts: [
      {
        type: 'credential_exposed',
        severity: 'critical',
        message: `Emergency revocation of ${vaultName}: ${reason}`,
        timestamp: new Date().toISOString(),
      },
    ],
    timestamp: new Date().toISOString(),
  });
}

export default executeSecurityAudit;
