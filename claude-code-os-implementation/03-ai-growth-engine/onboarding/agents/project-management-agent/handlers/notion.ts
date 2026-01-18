/**
 * Notion Handler for Project Management Agent
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PROJECTS_DB = process.env.NOTION_PROJECTS_DATABASE_ID;
const NOTION_MILESTONES_DB = process.env.NOTION_MILESTONES_DATABASE_ID;
const NOTION_WIN_CONDITIONS_DB = process.env.NOTION_WIN_CONDITIONS_DATABASE_ID;
const NOTION_VERSION = '2022-06-28';

export interface Project {
  id: string;
  name: string;
  client_name: string;
  status: string;
  slack_channel: string;
  start_date: string;
  target_date: string;
  project_lead: string;
}

export interface Milestone {
  id: string;
  name: string;
  project_id: string;
  status: 'Not Started' | 'In Progress' | 'Complete';
  due_date: string;
  completed_at?: string;
}

export interface WinCondition {
  id: string;
  name: string;
  project_id: string;
  description: string;
  status: 'Not Started' | 'In Progress' | 'Complete' | 'Blocked';
  evidence_link?: string;
  completed_at?: string;
}

/**
 * Get all active projects
 */
export async function getActiveProjects(): Promise<Project[]> {
  const response = await fetch(`https://api.notion.com/v1/databases/${NOTION_PROJECTS_DB}/query`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({
      filter: {
        property: 'Status',
        select: { equals: 'Active' },
      },
    }),
  });

  const data = await response.json();
  if (!data.results) return [];

  return data.results.map((page: any) => ({
    id: page.id,
    name: extractTitle(page.properties['Name']),
    client_name: extractRelationTitle(page.properties['Client']),
    status: extractSelect(page.properties['Status']),
    slack_channel: extractRichText(page.properties['Slack Channel']),
    start_date: extractDate(page.properties['Start Date']),
    target_date: extractDate(page.properties['Target Date']),
    project_lead: extractPeople(page.properties['Project Lead']),
  }));
}

/**
 * Get milestones for a project
 */
export async function getProjectMilestones(projectId: string): Promise<Milestone[]> {
  const response = await fetch(`https://api.notion.com/v1/databases/${NOTION_MILESTONES_DB}/query`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({
      filter: {
        property: 'Project',
        relation: { contains: projectId },
      },
      sorts: [{ property: 'Due Date', direction: 'ascending' }],
    }),
  });

  const data = await response.json();
  if (!data.results) return [];

  return data.results.map((page: any) => ({
    id: page.id,
    name: extractTitle(page.properties['Name']),
    project_id: projectId,
    status: extractSelect(page.properties['Status']) as Milestone['status'],
    due_date: extractDate(page.properties['Due Date']),
    completed_at: extractDate(page.properties['Completed At']),
  }));
}

/**
 * Get win conditions for a project
 */
export async function getWinConditions(projectId: string): Promise<WinCondition[]> {
  const response = await fetch(
    `https://api.notion.com/v1/databases/${NOTION_WIN_CONDITIONS_DB}/query`,
    {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${NOTION_API_KEY}`,
        'Content-Type': 'application/json',
        'Notion-Version': NOTION_VERSION,
      },
      body: JSON.stringify({
        filter: {
          property: 'Project',
          relation: { contains: projectId },
        },
      }),
    }
  );

  const data = await response.json();
  if (!data.results) return [];

  return data.results.map((page: any) => ({
    id: page.id,
    name: extractTitle(page.properties['Name']),
    project_id: projectId,
    description: extractRichText(page.properties['Description']),
    status: extractSelect(page.properties['Status']) as WinCondition['status'],
    evidence_link: extractUrl(page.properties['Evidence']),
    completed_at: extractDate(page.properties['Completed At']),
  }));
}

/**
 * Update project status
 */
export async function updateProjectStatus(projectId: string, status: string): Promise<void> {
  await fetch(`https://api.notion.com/v1/pages/${projectId}`, {
    method: 'PATCH',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({
      properties: {
        Status: { select: { name: status } },
      },
    }),
  });

  console.log(`[Notion] Updated project ${projectId} status to ${status}`);
}

/**
 * Create delivery report page in Notion
 */
export async function createDeliveryReport(data: {
  project_id: string;
  project_name: string;
  client_name: string;
  content: string;
}): Promise<string> {
  const response = await fetch('https://api.notion.com/v1/pages', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({
      parent: { page_id: data.project_id },
      properties: {
        title: {
          title: [{ text: { content: `Delivery Report - ${data.project_name}` } }],
        },
      },
      children: [
        {
          object: 'block',
          type: 'paragraph',
          paragraph: {
            rich_text: [{ type: 'text', text: { content: data.content } }],
          },
        },
      ],
    }),
  });

  const page = await response.json();
  return page.id;
}

// Helper functions
function extractTitle(prop: any): string {
  return prop?.title?.[0]?.plain_text || '';
}

function extractSelect(prop: any): string {
  return prop?.select?.name || '';
}

function extractRichText(prop: any): string {
  return prop?.rich_text?.[0]?.plain_text || '';
}

function extractDate(prop: any): string {
  return prop?.date?.start || '';
}

function extractUrl(prop: any): string {
  return prop?.url || '';
}

function extractPeople(prop: any): string {
  return prop?.people?.[0]?.name || '';
}

function extractRelationTitle(prop: any): string {
  // Would need to fetch the related page to get the title
  return prop?.relation?.[0]?.id || '';
}
