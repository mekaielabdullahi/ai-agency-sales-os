/**
 * Slack Handler for Client Communication Agent
 */

const SLACK_BOT_TOKEN = process.env.SLACK_BOT_TOKEN;

export interface SlackChannel {
  id: string;
  name: string;
  client_name?: string;
}

export interface SlackMessage {
  ts: string;
  text: string;
  user: string;
  bot_id?: string;
  reply_count?: number;
}

/**
 * Get all client channels (those starting with "client-")
 */
export async function getClientChannels(): Promise<SlackChannel[]> {
  const response = await fetch(
    'https://slack.com/api/conversations.list?types=public_channel&limit=1000',
    {
      headers: { Authorization: `Bearer ${SLACK_BOT_TOKEN}` },
    }
  );

  const data = await response.json();
  if (!data.ok) {
    throw new Error(`Slack API error: ${data.error}`);
  }

  return data.channels
    .filter((c: any) => c.name.startsWith('client-') && !c.name.endsWith('-internal'))
    .map((c: any) => ({
      id: c.id,
      name: c.name,
      client_name: c.name.replace('client-', '').replace(/-/g, ' '),
    }));
}

/**
 * Get messages from a channel within the last N hours
 */
export async function getChannelMessages(
  channelId: string,
  hoursBack: number = 24
): Promise<SlackMessage[]> {
  const oldest = Math.floor((Date.now() - hoursBack * 60 * 60 * 1000) / 1000);

  const response = await fetch(
    `https://slack.com/api/conversations.history?channel=${channelId}&oldest=${oldest}&limit=100`,
    {
      headers: { Authorization: `Bearer ${SLACK_BOT_TOKEN}` },
    }
  );

  const data = await response.json();
  if (!data.ok) {
    console.error(`[Slack] Failed to get messages for ${channelId}: ${data.error}`);
    return [];
  }

  return data.messages.map((m: any) => ({
    ts: m.ts,
    text: m.text || '',
    user: m.user,
    bot_id: m.bot_id,
    reply_count: m.reply_count || 0,
  }));
}

/**
 * Add emoji reaction to flag a message
 */
export async function flagMessage(
  channelId: string,
  messageTs: string,
  emoji: string = 'eyes'
): Promise<void> {
  await fetch('https://slack.com/api/reactions.add', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${SLACK_BOT_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      channel: channelId,
      timestamp: messageTs,
      name: emoji,
    }),
  });
}

/**
 * Post message to channel
 */
export async function postMessage(
  channel: string,
  message: { text: string; blocks?: any[] }
): Promise<void> {
  // Find channel ID if name is provided
  let channelId = channel;
  if (!channel.startsWith('C')) {
    const channels = await fetch(
      'https://slack.com/api/conversations.list?types=public_channel,private_channel&limit=1000',
      { headers: { Authorization: `Bearer ${SLACK_BOT_TOKEN}` } }
    );
    const data = await channels.json();
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

/**
 * Get response time stats for a channel
 */
export async function getChannelResponseStats(channelId: string): Promise<{
  avg_response_time_hours: number;
  messages_without_reply: number;
}> {
  const messages = await getChannelMessages(channelId, 7 * 24); // Last 7 days

  let totalResponseTime = 0;
  let responseCount = 0;
  let unreplied = 0;

  for (const message of messages) {
    if (message.bot_id) continue;

    if (message.reply_count && message.reply_count > 0) {
      // Has replies - would need to fetch thread to get actual response time
      responseCount++;
    } else {
      unreplied++;
    }
  }

  return {
    avg_response_time_hours: responseCount > 0 ? totalResponseTime / responseCount : 0,
    messages_without_reply: unreplied,
  };
}
