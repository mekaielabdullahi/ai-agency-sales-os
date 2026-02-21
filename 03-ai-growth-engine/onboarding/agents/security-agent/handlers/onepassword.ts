/**
 * 1Password Handler for Security Agent
 *
 * Uses 1Password CLI (op) for vault management.
 * Requires: 1Password CLI installed and signed in
 */

import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

// 1Password service account token (for automation)
const OP_SERVICE_ACCOUNT_TOKEN = process.env.OP_SERVICE_ACCOUNT_TOKEN;

export interface VaultItem {
  id: string;
  title: string;
  category: string;
  vault: string;
  created_at: string;
  updated_at: string;
  expires_at?: string;
  days_until_expiry?: number;
}

export interface AccessLog {
  user_email: string;
  action: 'read' | 'write' | 'delete';
  item_id: string;
  timestamp: string;
}

/**
 * Execute 1Password CLI command
 */
async function opCommand(args: string): Promise<any> {
  const env = OP_SERVICE_ACCOUNT_TOKEN
    ? { ...process.env, OP_SERVICE_ACCOUNT_TOKEN }
    : process.env;

  const { stdout } = await execAsync(`op ${args} --format json`, { env });
  return JSON.parse(stdout);
}

/**
 * Create a new vault for a client
 */
export async function createClientVault(name: string, description: string): Promise<string> {
  try {
    const result = await opCommand(`vault create "${name}" --description "${description}"`);
    console.log(`[1Password] Created vault: ${name}`);
    return result.id;
  } catch (error: any) {
    // Vault might already exist
    if (error.message.includes('already exists')) {
      console.log(`[1Password] Vault ${name} already exists`);
      const vaults = await opCommand('vault list');
      const vault = vaults.find((v: any) => v.name === name);
      return vault?.id || '';
    }
    throw error;
  }
}

/**
 * Grant user access to vault
 */
export async function grantVaultAccess(
  vaultName: string,
  email: string,
  role: string
): Promise<void> {
  // Map role to 1Password permissions
  const permissions = getPermissionsForRole(role);

  try {
    await opCommand(
      `vault user grant --vault "${vaultName}" --user "${email}" --permissions "${permissions}"`
    );
    console.log(`[1Password] Granted ${role} access to ${email} for vault ${vaultName}`);
  } catch (error: any) {
    console.error(`[1Password] Failed to grant access: ${error.message}`);
    throw error;
  }
}

/**
 * Revoke user access to vault
 */
export async function revokeVaultAccess(vaultName: string, email: string): Promise<void> {
  try {
    await opCommand(`vault user revoke --vault "${vaultName}" --user "${email}"`);
    console.log(`[1Password] Revoked access for ${email} from vault ${vaultName}`);
  } catch (error: any) {
    // User might not have access (already revoked)
    if (error.message.includes('not found') || error.message.includes('no access')) {
      console.log(`[1Password] User ${email} already has no access to ${vaultName}`);
      return;
    }
    throw error;
  }
}

/**
 * Get all items in a vault
 */
export async function getVaultItems(vaultName: string): Promise<VaultItem[]> {
  try {
    const items = await opCommand(`item list --vault "${vaultName}"`);
    return items.map((item: any) => ({
      id: item.id,
      title: item.title,
      category: item.category,
      vault: vaultName,
      created_at: item.created_at,
      updated_at: item.updated_at,
    }));
  } catch (error) {
    console.error(`[1Password] Failed to list items in ${vaultName}`);
    return [];
  }
}

/**
 * Get items expiring within N days
 */
export async function getExpiringItems(vaultName: string, days: number): Promise<VaultItem[]> {
  const items = await getVaultItems(vaultName);
  const expiringItems: VaultItem[] = [];

  for (const item of items) {
    // Get full item details to check expiry
    try {
      const details = await opCommand(`item get "${item.id}" --vault "${vaultName}"`);

      // Check for expiry fields (varies by item type)
      const expiryDate = findExpiryDate(details);

      if (expiryDate) {
        const daysUntil = Math.ceil(
          (new Date(expiryDate).getTime() - Date.now()) / (1000 * 60 * 60 * 24)
        );

        if (daysUntil <= days && daysUntil > 0) {
          expiringItems.push({
            ...item,
            expires_at: expiryDate,
            days_until_expiry: daysUntil,
          });
        }
      }
    } catch (error) {
      // Skip items we can't read
    }
  }

  return expiringItems;
}

/**
 * Get access logs for a vault (requires 1Password Business)
 */
export async function getAccessLogs(vaultName: string): Promise<AccessLog[]> {
  // Note: Activity logs require 1Password Business and API access
  // This is a placeholder - actual implementation would use 1Password Events API
  console.log(`[1Password] Access logs requested for ${vaultName} (requires Business plan)`);
  return [];
}

/**
 * Create a login item in vault
 */
export async function createLoginItem(
  vaultName: string,
  title: string,
  username: string,
  password: string,
  url?: string,
  notes?: string
): Promise<string> {
  let command = `item create --category login --vault "${vaultName}" --title "${title}"`;
  command += ` username="${username}" password="${password}"`;

  if (url) command += ` url="${url}"`;
  if (notes) command += ` notesPlain="${notes}"`;

  const result = await opCommand(command);
  console.log(`[1Password] Created login item: ${title} in ${vaultName}`);
  return result.id;
}

/**
 * Create an API credential item in vault
 */
export async function createAPICredential(
  vaultName: string,
  title: string,
  apiKey: string,
  apiSecret?: string,
  notes?: string
): Promise<string> {
  let command = `item create --category "API Credential" --vault "${vaultName}" --title "${title}"`;
  command += ` credential="${apiKey}"`;

  if (apiSecret) command += ` 'api secret'="${apiSecret}"`;
  if (notes) command += ` notesPlain="${notes}"`;

  const result = await opCommand(command);
  console.log(`[1Password] Created API credential: ${title} in ${vaultName}`);
  return result.id;
}

/**
 * Delete an item from vault
 */
export async function deleteItem(vaultName: string, itemId: string): Promise<void> {
  await opCommand(`item delete "${itemId}" --vault "${vaultName}"`);
  console.log(`[1Password] Deleted item ${itemId} from ${vaultName}`);
}

// Helper functions

function getPermissionsForRole(role: string): string {
  switch (role) {
    case 'PROJECT_LEAD':
      return 'manage_vault,view_items,edit_items';
    case 'DEVELOPER':
      return 'view_items';
    case 'CONTRACTOR':
      return 'view_items';
    case 'CLIENT':
      return 'view_items';
    default:
      return 'view_items';
  }
}

function findExpiryDate(itemDetails: any): string | null {
  // Check common expiry field locations
  const fields = itemDetails.fields || [];

  for (const field of fields) {
    const label = (field.label || '').toLowerCase();
    if (
      label.includes('expir') ||
      label.includes('valid until') ||
      label.includes('expires')
    ) {
      return field.value;
    }
  }

  // Check for credit card expiry
  if (itemDetails.category === 'CREDIT_CARD') {
    return itemDetails.expiry_date;
  }

  return null;
}
