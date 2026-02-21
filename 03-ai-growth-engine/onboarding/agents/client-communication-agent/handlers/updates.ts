/**
 * Progress Update Generator for Client Communication Agent
 */

import { Project, getProjectProgress, getWinConditions } from './notion';
import { postMessage } from './slack';

export interface ProgressUpdate {
  project_id: string;
  project_name: string;
  date: string;
  completed_this_period: string[];
  in_progress: string[];
  blockers: string[];
  next_steps: string[];
  win_condition_status: { name: string; status: string }[];
}

/**
 * Generate progress update for a project
 * Posts draft to internal channel for review before sending to client
 */
export async function generateProgressUpdate(project: Project): Promise<ProgressUpdate | null> {
  console.log(`[Updates] Generating progress update for ${project.name}`);

  const progress = await getProjectProgress(project.id);
  const winConditions = await getWinConditions(project.id);

  const update: ProgressUpdate = {
    project_id: project.id,
    project_name: project.name,
    date: new Date().toISOString().split('T')[0],
    completed_this_period: [],
    in_progress: [],
    blockers: [],
    next_steps: [],
    win_condition_status: winConditions.map((wc) => ({
      name: wc.name,
      status: wc.status,
    })),
  };

  // Generate update message
  const updateMessage = formatProgressUpdate(update, project);

  // Post to internal channel for review
  const internalChannel = `${project.slack_channel}-internal`;
  await postMessage(internalChannel, {
    text: `Progress update draft for ${project.client_name}`,
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '📝 Progress Update Draft',
          emoji: true,
        },
      },
      {
        type: 'context',
        elements: [
          {
            type: 'mrkdwn',
            text: `*Project:* ${project.name} | *Client:* ${project.client_name} | *Date:* ${update.date}`,
          },
        ],
      },
      {
        type: 'divider',
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: updateMessage,
        },
      },
      {
        type: 'divider',
      },
      {
        type: 'actions',
        elements: [
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: '✅ Approve & Send',
              emoji: true,
            },
            style: 'primary',
            action_id: 'approve_update',
            value: JSON.stringify({ project_id: project.id, channel: project.slack_channel }),
          },
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: '✏️ Edit',
              emoji: true,
            },
            action_id: 'edit_update',
          },
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: '🚫 Skip',
              emoji: true,
            },
            action_id: 'skip_update',
          },
        ],
      },
    ],
  });

  return update;
}

/**
 * Format progress update as markdown
 */
function formatProgressUpdate(update: ProgressUpdate, project: Project): string {
  const lines: string[] = [];

  lines.push(`## Progress Update: ${update.date}`);
  lines.push('');

  lines.push('### Completed This Period');
  if (update.completed_this_period.length > 0) {
    update.completed_this_period.forEach((item) => lines.push(`• ${item}`));
  } else {
    lines.push('• _Tasks in progress, update coming soon_');
  }
  lines.push('');

  lines.push('### In Progress');
  if (update.in_progress.length > 0) {
    update.in_progress.forEach((item) => lines.push(`• ${item}`));
  } else {
    lines.push('• _No active tasks_');
  }
  lines.push('');

  if (update.blockers.length > 0) {
    lines.push('### Blockers');
    update.blockers.forEach((item) => lines.push(`• ⚠️ ${item}`));
    lines.push('');
  }

  lines.push('### Next Steps');
  if (update.next_steps.length > 0) {
    update.next_steps.forEach((item) => lines.push(`• ${item}`));
  } else {
    lines.push('• _Will be updated after current tasks complete_');
  }
  lines.push('');

  lines.push('### Win Condition Progress');
  if (update.win_condition_status.length > 0) {
    update.win_condition_status.forEach((wc) => {
      const emoji = wc.status === 'Complete' ? '✅' : wc.status === 'In Progress' ? '🔄' : '⬜';
      lines.push(`• ${emoji} ${wc.name}: ${wc.status}`);
    });
  } else {
    lines.push('• _Win conditions not yet defined_');
  }
  lines.push('');

  lines.push('---');
  lines.push(`*Next update: ${getNextUpdateDate()}*`);

  return lines.join('\n');
}

/**
 * Get next update date (Tuesday or Friday)
 */
function getNextUpdateDate(): string {
  const now = new Date();
  const day = now.getDay();

  let daysUntilNext: number;
  if (day < 2) {
    daysUntilNext = 2 - day; // Until Tuesday
  } else if (day < 5) {
    daysUntilNext = 5 - day; // Until Friday
  } else {
    daysUntilNext = (7 - day) + 2; // Until next Tuesday
  }

  const nextDate = new Date(now);
  nextDate.setDate(now.getDate() + daysUntilNext);

  return nextDate.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
}

/**
 * Send approved update to client channel
 */
export async function sendApprovedUpdate(
  projectId: string,
  clientChannel: string,
  message: string
): Promise<void> {
  await postMessage(clientChannel, {
    text: message,
    blocks: [
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: message,
        },
      },
    ],
  });
}
