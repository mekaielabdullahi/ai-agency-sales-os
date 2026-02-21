/**
 * Notion Handler for Security Agent
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PROJECTS_DB = process.env.NOTION_PROJECTS_DATABASE_ID;
const NOTION_SECURITY_LOG_DB = process.env.NOTION_SECURITY_LOG_DATABASE_ID;
const NOTION_VERSION = '2022-06-28';

export interface Project {
  id: string;
  name: string;
  slug: string;
  status: string;
  completed_at: string;
}

export interface TeamMember {
  email: string;
  role: 'PROJECT_LEAD' | 'DEVELOPER' | 'CONTRACTOR' | 'CLIENT';
  name: string;
}

export interface SecurityEvent {
  project_id: string;
  event_type: string;
  details: string;
}

/**
 * Get active projects
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
    slug: generateSlug(extractTitle(page.properties['Name'])),
    status: extractSelect(page.properties['Status']),
    completed_at: '',
  }));
}

/**
 * Get completed projects (for credential revocation)
 */
export async function getCompletedProjects(): Promise<Project[]> {
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
        select: { equals: 'Delivered' },
      },
    }),
  });

  const data = await response.json();
  if (!data.results) return [];

  return data.results.map((page: any) => ({
    id: page.id,
    name: extractTitle(page.properties['Name']),
    slug: generateSlug(extractTitle(page.properties['Name'])),
    status: extractSelect(page.properties['Status']),
    completed_at: extractDate(page.properties['Completed At']),
  }));
}

/**
 * Get team members for a project
 */
export async function getProjectTeam(projectId: string): Promise<TeamMember[]> {
  // Would query a Team Members database filtered by project
  // Simplified for now
  return [];
}

/**
 * Log security event to Notion
 */
export async function logSecurityEvent(event: SecurityEvent): Promise<void> {
  if (!NOTION_SECURITY_LOG_DB) {
    console.log(`[Notion] Security log: ${event.event_type} - ${event.details}`);
    return;
  }

  await fetch('https://api.notion.com/v1/pages', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${NOTION_API_KEY}`,
      'Content-Type': 'application/json',
      'Notion-Version': NOTION_VERSION,
    },
    body: JSON.stringify({
      parent: { database_id: NOTION_SECURITY_LOG_DB },
      properties: {
        Name: {
          title: [{ text: { content: event.event_type } }],
        },
        Project: {
          relation: [{ id: event.project_id }],
        },
        Details: {
          rich_text: [{ text: { content: event.details } }],
        },
        Timestamp: {
          date: { start: new Date().toISOString() },
        },
      },
    }),
  });

  console.log(`[Notion] Logged security event: ${event.event_type}`);
}

// Helper functions
function extractTitle(prop: any): string {
  return prop?.title?.[0]?.plain_text || '';
}

function extractSelect(prop: any): string {
  return prop?.select?.name || '';
}

function extractDate(prop: any): string {
  return prop?.date?.start || '';
}

function generateSlug(name: string): string {
  return name.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-');
}
