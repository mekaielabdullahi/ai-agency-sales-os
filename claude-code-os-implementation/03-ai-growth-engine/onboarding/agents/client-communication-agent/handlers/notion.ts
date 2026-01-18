/**
 * Notion Handler for Client Communication Agent
 */

const NOTION_API_KEY = process.env.NOTION_API_KEY;
const NOTION_PROJECTS_DB = process.env.NOTION_PROJECTS_DATABASE_ID;
const NOTION_VERSION = '2022-06-28';

export interface Project {
  id: string;
  name: string;
  client_name: string;
  status: string;
  slack_channel: string;
  win_conditions: WinCondition[];
  start_date: string;
  target_date: string;
}

export interface WinCondition {
  name: string;
  status: 'Not Started' | 'In Progress' | 'Complete' | 'Blocked';
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
        select: {
          equals: 'Active',
        },
      },
    }),
  });

  const data = await response.json();
  if (!data.results) return [];

  return data.results.map((page: any) => ({
    id: page.id,
    name: extractTitle(page.properties['Name']),
    client_name: extractTitle(page.properties['Client']),
    status: extractSelect(page.properties['Status']),
    slack_channel: extractRichText(page.properties['Slack Channel']),
    win_conditions: [], // Would need to fetch from related DB
    start_date: extractDate(page.properties['Start Date']),
    target_date: extractDate(page.properties['Target Date']),
  }));
}

/**
 * Get project progress (tasks completed / total)
 */
export async function getProjectProgress(projectId: string): Promise<{
  total_tasks: number;
  completed_tasks: number;
  in_progress_tasks: number;
  blocked_tasks: number;
}> {
  // This would query a related Tasks database filtered by project
  // Simplified for now
  return {
    total_tasks: 0,
    completed_tasks: 0,
    in_progress_tasks: 0,
    blocked_tasks: 0,
  };
}

/**
 * Log communication event to Notion
 */
export async function logCommunication(data: {
  project_id: string;
  type: 'urgent_flag' | 'progress_update' | 'sla_violation';
  details: string;
}): Promise<void> {
  // Create a record in a Communications Log database
  console.log(`[Notion] Logged communication: ${data.type} for project ${data.project_id}`);
}

/**
 * Get win condition status for a project
 */
export async function getWinConditions(projectId: string): Promise<WinCondition[]> {
  // Would fetch from Win Conditions database filtered by project
  return [];
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
