/**
 * Notifications Handler for Security Agent
 */

const SLACK_BOT_TOKEN = process.env.SLACK_BOT_TOKEN;
const SECURITY_CHANNEL = process.env.SECURITY_CHANNEL || 'security-alerts';

import { SecurityCheckResult, ExpiringCredential } from '../index';

/**
 * Send security alert to security channel
 */
export async function sendSecurityAlert(result: SecurityCheckResult): Promise<void> {
  const blocks: any[] = [
    {
      type: 'header',
      text: {
        type: 'plain_text',
        text: '🔐 Security Audit Report',
        emoji: true,
      },
    },
    {
      type: 'context',
      elements: [
        {
          type: 'mrkdwn',
          text: `*Audit completed:* ${new Date(result.timestamp).toLocaleString()}`,
        },
      ],
    },
    {
      type: 'divider',
    },
  ];

  // Summary section
  blocks.push({
    type: 'section',
    fields: [
      {
        type: 'mrkdwn',
        text: `*Vaults Audited:*\n${result.vaults_audited}`,
      },
      {
        type: 'mrkdwn',
        text: `*Expiring Credentials:*\n${result.expiring_credentials.length}`,
      },
      {
        type: 'mrkdwn',
        text: `*Access Revoked:*\n${result.access_revoked.length}`,
      },
      {
        type: 'mrkdwn',
        text: `*Security Alerts:*\n${result.security_alerts.length}`,
      },
    ],
  });

  // Security alerts (if any)
  if (result.security_alerts.length > 0) {
    blocks.push({ type: 'divider' });
    blocks.push({
      type: 'section',
      text: {
        type: 'mrkdwn',
        text: '*⚠️ Security Alerts:*',
      },
    });

    for (const alert of result.security_alerts) {
      const emoji =
        alert.severity === 'critical'
          ? '🚨'
          : alert.severity === 'high'
          ? '🔴'
          : alert.severity === 'medium'
          ? '🟠'
          : '🟡';

      blocks.push({
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `${emoji} *${alert.severity.toUpperCase()}:* ${alert.message}`,
        },
      });
    }
  }

  // Expiring credentials (if any)
  if (result.expiring_credentials.length > 0) {
    blocks.push({ type: 'divider' });
    blocks.push({
      type: 'section',
      text: {
        type: 'mrkdwn',
        text: '*⏰ Expiring Credentials:*',
      },
    });

    const expiringText = result.expiring_credentials
      .map((cred) => `• *${cred.item_name}* in \`${cred.vault}\` - ${cred.days_until_expiry} days`)
      .join('\n');

    blocks.push({
      type: 'section',
      text: {
        type: 'mrkdwn',
        text: expiringText,
      },
    });
  }

  // Revoked access (if any)
  if (result.access_revoked.length > 0) {
    blocks.push({ type: 'divider' });
    blocks.push({
      type: 'section',
      text: {
        type: 'mrkdwn',
        text: '*🔒 Access Revoked:*',
      },
    });

    const revokedText = result.access_revoked
      .map((rev) => `• ${rev.user_email} from \`${rev.vault}\` - ${rev.reason}`)
      .join('\n');

    blocks.push({
      type: 'section',
      text: {
        type: 'mrkdwn',
        text: revokedText,
      },
    });
  }

  await postToSlack(SECURITY_CHANNEL, {
    text: 'Security Audit Report',
    blocks,
  });
}

/**
 * Notify about credential expiry
 */
export async function notifyCredentialExpiry(
  credential: ExpiringCredential,
  project: any
): Promise<void> {
  const urgency =
    credential.days_until_expiry <= 3
      ? '🚨 URGENT'
      : credential.days_until_expiry <= 7
      ? '⚠️ Warning'
      : 'ℹ️ Notice';

  const internalChannel = `client-${project.slug}-internal`;

  await postToSlack(internalChannel, {
    text: `${urgency}: Credential expiring soon`,
    blocks: [
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `${urgency}: *${credential.item_name}* expires in *${credential.days_until_expiry} days*`,
        },
      },
      {
        type: 'context',
        elements: [
          {
            type: 'mrkdwn',
            text: `Vault: \`${credential.vault}\` | Expires: ${credential.expires_at}`,
          },
        ],
      },
      {
        type: 'actions',
        elements: [
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: '🔑 Open 1Password',
              emoji: true,
            },
            url: `onepassword://open-item?vault=${credential.vault}&item=${credential.item_name}`,
            action_id: 'open_1password',
          },
        ],
      },
    ],
  });
}

/**
 * Post message to Slack channel
 */
async function postToSlack(
  channel: string,
  message: { text: string; blocks?: any[] }
): Promise<void> {
  // Find channel ID if name is provided
  let channelId = channel;
  if (!channel.startsWith('C')) {
    const response = await fetch(
      'https://slack.com/api/conversations.list?types=public_channel,private_channel&limit=1000',
      { headers: { Authorization: `Bearer ${SLACK_BOT_TOKEN}` } }
    );
    const data = await response.json();
    const found = data.channels?.find((c: any) => c.name === channel);
    if (found) channelId = found.id;
  }

  await fetch('https://slack.com/api/chat.postMessage', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${SLACK_BOT_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      channel: channelId,
      text: message.text,
      blocks: message.blocks,
    }),
  });
}
