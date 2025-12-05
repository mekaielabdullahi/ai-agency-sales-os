// Slack Notifications
export interface SlackMessage {
  channel: 'pipeline' | 'wins' | 'website'
  text: string
  blocks?: any[]
}

export async function sendSlackNotification(message: SlackMessage) {
  const webhookUrl = getWebhookUrl(message.channel)

  if (!webhookUrl) {
    console.warn(`No Slack webhook configured for channel: ${message.channel}`)
    return { success: false }
  }

  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text: message.text,
        blocks: message.blocks,
      }),
    })

    if (!response.ok) {
      throw new Error(`Slack API error: ${response.statusText}`)
    }

    return { success: true }
  } catch (error) {
    console.error('Error sending Slack notification:', error)
    return { success: false, error }
  }
}

export async function notifyNewLead(lead: {
  name: string
  email: string
  company?: string
  vertical: string
  source: string
}) {
  const blocks = [
    {
      type: 'header',
      text: {
        type: 'plain_text',
        text: '🎯 New Lead from Website',
      },
    },
    {
      type: 'section',
      fields: [
        {
          type: 'mrkdwn',
          text: `*Name:*\n${lead.name}`,
        },
        {
          type: 'mrkdwn',
          text: `*Company:*\n${lead.company || 'Not provided'}`,
        },
        {
          type: 'mrkdwn',
          text: `*Email:*\n${lead.email}`,
        },
        {
          type: 'mrkdwn',
          text: `*Vertical:*\n${lead.vertical}`,
        },
        {
          type: 'mrkdwn',
          text: `*Source:*\n${lead.source}`,
        },
        {
          type: 'mrkdwn',
          text: `*Assigned To:*\n${getAssignedFounder(lead.vertical)}`,
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
            text: 'View in Notion',
          },
          url: 'https://notion.so',
          style: 'primary',
        },
      ],
    },
  ]

  return sendSlackNotification({
    channel: 'pipeline',
    text: `New ${lead.vertical} lead: ${lead.name} from ${lead.company || 'website'}`,
    blocks,
  })
}

export async function notifyBooking(booking: {
  name: string
  email: string
  vertical: string
  date: string
  founder: string
}) {
  const blocks = [
    {
      type: 'header',
      text: {
        type: 'plain_text',
        text: '📅 Discovery Call Booked',
      },
    },
    {
      type: 'section',
      fields: [
        {
          type: 'mrkdwn',
          text: `*Prospect:*\n${booking.name}`,
        },
        {
          type: 'mrkdwn',
          text: `*Founder:*\n${booking.founder}`,
        },
        {
          type: 'mrkdwn',
          text: `*Vertical:*\n${booking.vertical}`,
        },
        {
          type: 'mrkdwn',
          text: `*Date:*\n${booking.date}`,
        },
      ],
    },
  ]

  return sendSlackNotification({
    channel: 'wins',
    text: `${booking.founder} has a discovery call booked with ${booking.name} (${booking.vertical})`,
    blocks,
  })
}

function getWebhookUrl(channel: string): string | undefined {
  const webhooks: Record<string, string | undefined> = {
    'pipeline': process.env.SLACK_WEBHOOK_PIPELINE,
    'wins': process.env.SLACK_WEBHOOK_WINS,
    'website': process.env.SLACK_WEBHOOK_WEBSITE,
  }
  return webhooks[channel]
}

function getAssignedFounder(vertical: string): string {
  const assignments: Record<string, string> = {
    'Defense': 'Mekaiel',
    'Industrial': '4.0 Hero',
    'E-commerce': 'Matthew',
    'Construction': 'Chris',
  }
  return assignments[vertical] || 'Mekaiel'
}
