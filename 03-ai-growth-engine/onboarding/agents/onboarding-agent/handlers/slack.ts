/**
 * Slack Handler for Onboarding Agent
 *
 * Creates channels and sends notifications via Slack API
 */

import { formatCurrency } from '../utils';

const SLACK_BOT_TOKEN = process.env.SLACK_BOT_TOKEN;
const NEW_CLIENTS_CHANNEL = process.env.NEW_CLIENTS_CHANNEL || 'new-clients';

interface CreateChannelsParams {
  clientName: string;
  clientEmail: string;
  slug: string;
}

interface NotifyParams {
  clientName: string;
  projectType: string;
  amount: number;
}

/**
 * Create client Slack channels
 * - client-{slug}: Client-facing channel (client invited)
 * - client-{slug}-internal: Team-only channel
 */
export async function createClientChannels(params: CreateChannelsParams): Promise<string[]> {
  const { clientName, clientEmail, slug } = params;
  const channels: string[] = [];

  // Create public client channel
  const publicChannel = `client-${slug}`;
  const publicChannelId = await createChannel(publicChannel, false);
  if (publicChannelId) {
    channels.push(publicChannel);

    // Set channel topic
    await setChannelTopic(
      publicChannelId,
      `Project channel for ${clientName} | Contact: ${clientEmail}`
    );

    // Post welcome message
    await postMessage(publicChannelId, {
      text: `Welcome to your AriseGroup project channel, ${clientName}! :wave:`,
      blocks: [
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `*Welcome to your AriseGroup project channel!* :wave:\n\nHi ${clientName}, this is where all project communication will happen.`,
          },
        },
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: '*Communication Protocol:*\n• Progress updates: Tuesdays & Fridays\n• Team availability: 12-2pm PT daily\n• Urgent issues: Tag with "URGENT" for priority',
          },
        },
      ],
    });

    // TODO: Invite client via email
  }

  // Create internal team channel
  const internalChannel = `client-${slug}-internal`;
  const internalChannelId = await createChannel(internalChannel, false);
  if (internalChannelId) {
    channels.push(internalChannel);

    // Set channel topic
    await setChannelTopic(
      internalChannelId,
      `Internal channel for ${clientName} project - TEAM ONLY`
    );

    // Post context message
    await postMessage(internalChannelId, {
      text: `Internal channel created for ${clientName}`,
      blocks: [
        {
          type: 'section',
          text: {
            type: 'mrkdwn',
            text: `*Internal Project Channel: ${clientName}*\n\nThis channel is for team discussions only. Client-facing comms go in #${publicChannel}`,
          },
        },
      ],
    });
  }

  return channels;
}

/**
 * Notify team about new client in #new-clients
 */
export async function notifyNewClient(params: NotifyParams): Promise<void> {
  const { clientName, projectType, amount } = params;

  // Find #new-clients channel
  const channelId = await findChannelByName(NEW_CLIENTS_CHANNEL);
  if (!channelId) {
    throw new Error(`Channel #${NEW_CLIENTS_CHANNEL} not found`);
  }

  await postMessage(channelId, {
    text: `New client: ${clientName}`,
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: ':tada: New Client Signed!',
          emoji: true,
        },
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Client:*\n${clientName}`,
          },
          {
            type: 'mrkdwn',
            text: `*Project:*\n${projectType}`,
          },
          {
            type: 'mrkdwn',
            text: `*Amount:*\n${formatCurrency(amount)}`,
          },
          {
            type: 'mrkdwn',
            text: `*Status:*\nOnboarding emails sent :white_check_mark:`,
          },
        ],
      },
      {
        type: 'context',
        elements: [
          {
            type: 'mrkdwn',
            text: 'Slack channels created. Waiting for logistics call scheduling.',
          },
        ],
      },
    ],
  });
}

/**
 * Create a Slack channel
 */
async function createChannel(name: string, isPrivate: boolean = false): Promise<string | null> {
  const response = await fetch('https://slack.com/api/conversations.create', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${SLACK_BOT_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name,
      is_private: isPrivate,
    }),
  });

  const data = await response.json();

  if (!data.ok) {
    // Channel might already exist
    if (data.error === 'name_taken') {
      console.log(`[Slack] Channel #${name} already exists, finding it...`);
      return await findChannelByName(name);
    }
    console.error(`[Slack] Failed to create channel #${name}: ${data.error}`);
    return null;
  }

  console.log(`[Slack] Created channel #${name}`);
  return data.channel.id;
}

/**
 * Find channel by name
 */
async function findChannelByName(name: string): Promise<string | null> {
  const response = await fetch(
    `https://slack.com/api/conversations.list?types=public_channel,private_channel&limit=1000`,
    {
      headers: {
        Authorization: `Bearer ${SLACK_BOT_TOKEN}`,
      },
    }
  );

  const data = await response.json();

  if (!data.ok) {
    console.error(`[Slack] Failed to list channels: ${data.error}`);
    return null;
  }

  const channel = data.channels.find((c: any) => c.name === name);
  return channel?.id || null;
}

/**
 * Set channel topic
 */
async function setChannelTopic(channelId: string, topic: string): Promise<void> {
  await fetch('https://slack.com/api/conversations.setTopic', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${SLACK_BOT_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      channel: channelId,
      topic,
    }),
  });
}

/**
 * Post message to channel
 */
async function postMessage(
  channelId: string,
  message: { text: string; blocks?: any[] }
): Promise<void> {
  const response = await fetch('https://slack.com/api/chat.postMessage', {
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

  const data = await response.json();

  if (!data.ok) {
    console.error(`[Slack] Failed to post message: ${data.error}`);
  }
}
