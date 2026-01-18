/**
 * Slack Handler for Project Management Agent
 */

const SLACK_BOT_TOKEN = process.env.SLACK_BOT_TOKEN;

/**
 * Post message to a channel
 */
export async function postMessage(
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

/**
 * Send DM to user
 */
export async function sendDM(userId: string, message: string): Promise<void> {
  // Open DM channel
  const openResponse = await fetch('https://slack.com/api/conversations.open', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${SLACK_BOT_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ users: userId }),
  });

  const openData = await openResponse.json();
  if (!openData.ok) {
    console.error(`[Slack] Failed to open DM: ${openData.error}`);
    return;
  }

  // Send message
  await postMessage(openData.channel.id, { text: message });
}

/**
 * Get user by email
 */
export async function getUserByEmail(email: string): Promise<string | null> {
  const response = await fetch(
    `https://slack.com/api/users.lookupByEmail?email=${encodeURIComponent(email)}`,
    { headers: { Authorization: `Bearer ${SLACK_BOT_TOKEN}` } }
  );

  const data = await response.json();
  return data.ok ? data.user.id : null;
}
