/**
 * Notion Handler for Onboarding Agent
 *
 * Updates client database with onboarding timestamps and status
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_DATABASE_ID = process.env.NOTION_CLIENTS_DATABASE_ID;
const NOTION_VERSION = '2022-06-28';

interface OnboardingStatusUpdate {
  status?: string;
  onboarding_started?: string;
  gratitude_email_sent?: string;
  next_steps_email_sent?: string;
  slack_channels_created?: string;
  team_notified?: string;
}

interface ClientData {
  id: string;
  name: string;
  email: string;
  project_type: string;
  status: string;
}

/**
 * Update client's onboarding status in Notion
 */
export async function updateOnboardingStatus(
  clientId: string,
  updates: OnboardingStatusUpdate
): Promise<void> {
  const properties: Record<string, any> = {};

  if (updates.status) {
    properties['Status'] = {
      select: { name: updates.status },
    };
  }

  if (updates.onboarding_started) {
    properties['Onboarding Started'] = {
      date: { start: updates.onboarding_started },
    };
  }

  if (updates.gratitude_email_sent) {
    properties['Gratitude Email Sent'] = {
      date: { start: updates.gratitude_email_sent },
    };
  }

  if (updates.next_steps_email_sent) {
    properties['Next Steps Email Sent'] = {
      date: { start: updates.next_steps_email_sent },
    };
  }

  if (updates.slack_channels_created) {
    properties['Slack Channels Created'] = {
      date: { start: updates.slack_channels_created },
    };
  }

  if (updates.team_notified) {
    properties['Team Notified'] = {
      date: { start: updates.team_notified },
    };
  }

  const response = await fetch(`https://api.notion.com/v1/pages/${clientId}`, {
    method: 'PATCH',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({ properties }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Notion API error: ${response.status} ${error}`);
  }

  console.log(`[Notion] Updated client ${clientId} with:`, Object.keys(updates).join(', '));
}

/**
 * Get client data from Notion by page ID
 */
export async function getClientData(clientId: string): Promise<ClientData> {
  const response = await fetch(`https://api.notion.com/v1/pages/${clientId}`, {
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Notion-Version': NOTION_VERSION,
    },
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Notion API error: ${response.status} ${error}`);
  }

  const page = await response.json();

  return {
    id: page.id,
    name: extractTitle(page.properties['Name']),
    email: extractEmail(page.properties['Email']),
    project_type: extractSelect(page.properties['Project Type']),
    status: extractSelect(page.properties['Status']),
  };
}

/**
 * Find client by email in Notion database
 */
export async function findClientByEmail(email: string): Promise<ClientData | null> {
  const response = await fetch(`https://api.notion.com/v1/databases/${NOTION_DATABASE_ID}/query`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({
      filter: {
        property: 'Email',
        email: { equals: email },
      },
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Notion API error: ${response.status} ${error}`);
  }

  const data = await response.json();

  if (data.results.length === 0) {
    return null;
  }

  const page = data.results[0];

  return {
    id: page.id,
    name: extractTitle(page.properties['Name']),
    email: extractEmail(page.properties['Email']),
    project_type: extractSelect(page.properties['Project Type']),
    status: extractSelect(page.properties['Status']),
  };
}

/**
 * Create a new client record in Notion
 */
export async function createClient(data: {
  name: string;
  email: string;
  projectType: string;
  amount: number;
}): Promise<string> {
  const response = await fetch('https://api.notion.com/v1/pages', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({
      parent: { database_id: NOTION_DATABASE_ID },
      properties: {
        Name: {
          title: [{ text: { content: data.name } }],
        },
        Email: {
          email: data.email,
        },
        'Project Type': {
          select: { name: data.projectType },
        },
        Amount: {
          number: data.amount,
        },
        Status: {
          select: { name: 'Paid' },
        },
      },
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Notion API error: ${response.status} ${error}`);
  }

  const page = await response.json();
  console.log(`[Notion] Created client record: ${page.id}`);

  return page.id;
}

// Helper functions to extract Notion property values
function extractTitle(prop: any): string {
  return prop?.title?.[0]?.plain_text || '';
}

function extractEmail(prop: any): string {
  return prop?.email || '';
}

function extractSelect(prop: any): string {
  return prop?.select?.name || '';
}
