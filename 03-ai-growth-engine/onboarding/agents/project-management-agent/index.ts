/**
 * Project Management Agent
 *
 * Tracks project timelines, monitors win conditions, alerts on delays,
 * and generates delivery reports.
 *
 * Trigger: Daily at 9am PT + win condition completion events
 *
 * Responsibilities:
 * 1. Track project timeline against milestones
 * 2. Alert on delays (task overdue > 24 hours)
 * 3. Verify win conditions are being tracked
 * 4. Generate delivery reports at project close
 */

import {
  getActiveProjects,
  getProjectMilestones,
  getWinConditions,
  updateProjectStatus,
  Project,
  Milestone,
  WinCondition,
} from './handlers/notion';
import { postMessage } from './handlers/slack';
import { generateDeliveryReport } from './handlers/reports';

export interface PMCheckResult {
  success: boolean;
  projects_checked: number;
  delays_found: DelayAlert[];
  win_conditions_complete: WinConditionComplete[];
  delivery_reports_generated: string[];
  timestamp: string;
}

export interface DelayAlert {
  project_id: string;
  project_name: string;
  milestone_name: string;
  days_overdue: number;
  original_due_date: string;
}

export interface WinConditionComplete {
  project_id: string;
  project_name: string;
  condition_name: string;
  completed_at: string;
}

/**
 * Main PM check execution
 * Run daily at 9am PT
 */
export async function executePMCheck(): Promise<PMCheckResult> {
  const result: PMCheckResult = {
    success: false,
    projects_checked: 0,
    delays_found: [],
    win_conditions_complete: [],
    delivery_reports_generated: [],
    timestamp: new Date().toISOString(),
  };

  console.log('[PMAgent] Starting daily project check...');

  try {
    const projects = await getActiveProjects();

    for (const project of projects) {
      result.projects_checked++;

      // Check milestones for delays
      const milestones = await getProjectMilestones(project.id);
      const delays = checkForDelays(project, milestones);
      result.delays_found.push(...delays);

      // Alert team about delays
      for (const delay of delays) {
        await alertDelay(delay, project);
      }

      // Check win conditions
      const winConditions = await getWinConditions(project.id);
      const allComplete = winConditions.every((wc) => wc.status === 'Complete');

      // Track newly completed conditions
      for (const wc of winConditions) {
        if (wc.status === 'Complete' && wc.completed_at) {
          // Check if completed in last 24 hours
          const completedAt = new Date(wc.completed_at);
          const oneDayAgo = new Date(Date.now() - 24 * 60 * 60 * 1000);

          if (completedAt > oneDayAgo) {
            result.win_conditions_complete.push({
              project_id: project.id,
              project_name: project.name,
              condition_name: wc.name,
              completed_at: wc.completed_at,
            });
          }
        }
      }

      // Generate delivery report if all conditions complete
      if (allComplete && winConditions.length > 0) {
        console.log(`[PMAgent] All win conditions complete for ${project.name}, generating delivery report...`);

        try {
          await generateDeliveryReport(project, winConditions);
          result.delivery_reports_generated.push(project.name);

          // Update project status
          await updateProjectStatus(project.id, 'Delivered');

          // Notify team
          await notifyDeliveryReady(project);
        } catch (error) {
          console.error(`[PMAgent] Failed to generate delivery report for ${project.name}:`, error);
        }
      }
    }

    result.success = true;
    console.log(
      `[PMAgent] Check complete. ${result.projects_checked} projects, ${result.delays_found.length} delays, ${result.delivery_reports_generated.length} reports generated`
    );
  } catch (error) {
    console.error('[PMAgent] Error during check:', error);
  }

  return result;
}

/**
 * Check milestones for delays
 */
function checkForDelays(project: Project, milestones: Milestone[]): DelayAlert[] {
  const delays: DelayAlert[] = [];
  const now = new Date();

  for (const milestone of milestones) {
    if (milestone.status === 'Complete') continue;

    const dueDate = new Date(milestone.due_date);
    if (dueDate < now) {
      const daysOverdue = Math.ceil((now.getTime() - dueDate.getTime()) / (1000 * 60 * 60 * 24));

      delays.push({
        project_id: project.id,
        project_name: project.name,
        milestone_name: milestone.name,
        days_overdue: daysOverdue,
        original_due_date: milestone.due_date,
      });
    }
  }

  return delays;
}

/**
 * Alert team about delay
 */
async function alertDelay(delay: DelayAlert, project: Project): Promise<void> {
  const internalChannel = `client-${project.slack_channel}-internal`;

  await postMessage(internalChannel, {
    text: `⚠️ Milestone delay: ${delay.milestone_name}`,
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '⚠️ Milestone Delay Alert',
          emoji: true,
        },
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Project:*\n${delay.project_name}`,
          },
          {
            type: 'mrkdwn',
            text: `*Milestone:*\n${delay.milestone_name}`,
          },
          {
            type: 'mrkdwn',
            text: `*Days Overdue:*\n${delay.days_overdue}`,
          },
          {
            type: 'mrkdwn',
            text: `*Original Due:*\n${delay.original_due_date}`,
          },
        ],
      },
      {
        type: 'context',
        elements: [
          {
            type: 'mrkdwn',
            text: 'Please update the milestone status or communicate delay to client.',
          },
        ],
      },
    ],
  });
}

/**
 * Notify team that delivery report is ready
 */
async function notifyDeliveryReady(project: Project): Promise<void> {
  const internalChannel = `client-${project.slack_channel}-internal`;

  await postMessage(internalChannel, {
    text: `🎉 Delivery report ready for ${project.name}`,
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '🎉 Project Ready for Delivery!',
          emoji: true,
        },
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `All win conditions for *${project.name}* are complete!\n\nA delivery report has been generated and is ready for review.`,
        },
      },
      {
        type: 'actions',
        elements: [
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: '📄 View Report',
              emoji: true,
            },
            url: `https://notion.so/${project.id.replace(/-/g, '')}`,
            action_id: 'view_report',
          },
          {
            type: 'button',
            text: {
              type: 'plain_text',
              text: '✅ Approve & Send to Client',
              emoji: true,
            },
            style: 'primary',
            action_id: 'approve_delivery',
          },
        ],
      },
    ],
  });
}

/**
 * Handle win condition completion event
 */
export async function handleWinConditionComplete(
  projectId: string,
  conditionName: string
): Promise<void> {
  console.log(`[PMAgent] Win condition completed: ${conditionName} for project ${projectId}`);

  // Check if all conditions are now complete
  const winConditions = await getWinConditions(projectId);
  const allComplete = winConditions.every((wc) => wc.status === 'Complete');

  if (allComplete) {
    console.log(`[PMAgent] All conditions complete, triggering delivery report generation`);
    // This will be picked up by the daily check, or we can trigger immediately
  }
}

export default executePMCheck;
