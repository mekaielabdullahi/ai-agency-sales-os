/**
 * Client Communication Agent
 *
 * Monitors client Slack channels for messages, flags urgent issues,
 * and generates progress update drafts.
 *
 * Trigger: Scheduled (2x daily at 9am and 4pm PT) + event-based
 *
 * Responsibilities:
 * 1. Monitor client Slack channels for new messages
 * 2. Flag urgent messages (keywords: "urgent", "blocker", "ASAP")
 * 3. Generate 2x weekly progress update drafts (Tue & Fri)
 * 4. Track response times for SLA compliance
 */

import { getClientChannels, getChannelMessages, postMessage, flagMessage } from './handlers/slack';
import { getActiveProjects, logCommunication, getProjectProgress } from './handlers/notion';
import { generateProgressUpdate } from './handlers/updates';

export interface CommunicationCheckResult {
  success: boolean;
  channels_checked: number;
  urgent_messages: UrgentMessage[];
  sla_violations: SLAViolation[];
  progress_updates_generated: string[];
  timestamp: string;
}

export interface UrgentMessage {
  channel: string;
  client_name: string;
  message_ts: string;
  text: string;
  keyword_matched: string;
  flagged_at: string;
}

export interface SLAViolation {
  channel: string;
  client_name: string;
  message_ts: string;
  wait_time_hours: number;
  sla_limit_hours: number;
}

// Urgent keywords to flag
const URGENT_KEYWORDS = ['urgent', 'asap', 'blocker', 'blocked', 'emergency', 'critical', 'help'];

// SLA limits
const SLA_URGENT_HOURS = 2;
const SLA_NORMAL_HOURS = 24;
const SLACK_AVAILABILITY_START = 12; // 12pm PT
const SLACK_AVAILABILITY_END = 14;   // 2pm PT

/**
 * Main communication check execution
 * Run this on a schedule (recommended: 9am and 4pm PT)
 */
export async function executeCommuncationCheck(): Promise<CommunicationCheckResult> {
  const result: CommunicationCheckResult = {
    success: false,
    channels_checked: 0,
    urgent_messages: [],
    sla_violations: [],
    progress_updates_generated: [],
    timestamp: new Date().toISOString(),
  };

  console.log('[CommunicationAgent] Starting communication check...');

  try {
    // Get all active projects and their Slack channels
    const projects = await getActiveProjects();
    const clientChannels = await getClientChannels();

    for (const channel of clientChannels) {
      result.channels_checked++;

      // Get recent messages (last 24 hours)
      const messages = await getChannelMessages(channel.id, 24);

      for (const message of messages) {
        // Skip bot messages
        if (message.bot_id) continue;

        // Check for urgent keywords
        const urgentKeyword = checkForUrgentKeywords(message.text);
        if (urgentKeyword) {
          const urgentMsg: UrgentMessage = {
            channel: channel.name,
            client_name: channel.client_name || channel.name,
            message_ts: message.ts,
            text: message.text.substring(0, 200),
            keyword_matched: urgentKeyword,
            flagged_at: new Date().toISOString(),
          };
          result.urgent_messages.push(urgentMsg);

          // Flag the message in Slack with emoji reaction
          await flagMessage(channel.id, message.ts, 'rotating_light');

          // Notify team
          await notifyTeamOfUrgent(urgentMsg);
        }

        // Check SLA compliance
        const slaViolation = checkSLACompliance(message, channel);
        if (slaViolation) {
          result.sla_violations.push(slaViolation);
        }
      }
    }

    // Generate progress updates if it's Tuesday or Friday
    const today = new Date().getDay();
    const isTuesday = today === 2;
    const isFriday = today === 5;

    if (isTuesday || isFriday) {
      for (const project of projects) {
        try {
          const update = await generateProgressUpdate(project);
          if (update) {
            result.progress_updates_generated.push(project.name);
          }
        } catch (error) {
          console.error(`[CommunicationAgent] Failed to generate update for ${project.name}:`, error);
        }
      }
    }

    result.success = true;
    console.log(`[CommunicationAgent] Check complete. ${result.channels_checked} channels, ${result.urgent_messages.length} urgent, ${result.sla_violations.length} SLA violations`);

  } catch (error) {
    console.error('[CommunicationAgent] Error during check:', error);
  }

  return result;
}

/**
 * Check message text for urgent keywords
 */
function checkForUrgentKeywords(text: string): string | null {
  const lowerText = text.toLowerCase();
  for (const keyword of URGENT_KEYWORDS) {
    if (lowerText.includes(keyword)) {
      return keyword;
    }
  }
  return null;
}

/**
 * Check if message violates SLA
 */
function checkSLACompliance(message: any, channel: any): SLAViolation | null {
  const messageTime = new Date(parseFloat(message.ts) * 1000);
  const now = new Date();
  const hoursElapsed = (now.getTime() - messageTime.getTime()) / (1000 * 60 * 60);

  // Determine SLA limit based on urgency
  const isUrgent = checkForUrgentKeywords(message.text) !== null;
  const slaLimit = isUrgent ? SLA_URGENT_HOURS : SLA_NORMAL_HOURS;

  // Check if message has a reply
  if (!message.reply_count && hoursElapsed > slaLimit) {
    return {
      channel: channel.name,
      client_name: channel.client_name || channel.name,
      message_ts: message.ts,
      wait_time_hours: Math.round(hoursElapsed * 10) / 10,
      sla_limit_hours: slaLimit,
    };
  }

  return null;
}

/**
 * Notify team of urgent message
 */
async function notifyTeamOfUrgent(urgent: UrgentMessage): Promise<void> {
  const internalChannel = `${urgent.channel}-internal`;

  await postMessage(internalChannel, {
    text: `🚨 Urgent message from client`,
    blocks: [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: '🚨 Urgent Client Message',
          emoji: true,
        },
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `*Channel:* #${urgent.channel}\n*Keyword:* "${urgent.keyword_matched}"\n*Message:* ${urgent.text}`,
        },
      },
      {
        type: 'context',
        elements: [
          {
            type: 'mrkdwn',
            text: `SLA: Respond within 2 hours | <slack://channel?id=${urgent.channel}&message=${urgent.message_ts}|View Message>`,
          },
        ],
      },
    ],
  });
}

/**
 * Check if currently within Slack availability window (12-2pm PT)
 */
export function isWithinAvailabilityWindow(): boolean {
  const now = new Date();
  const ptTime = new Date(now.toLocaleString('en-US', { timeZone: 'America/Los_Angeles' }));
  const hour = ptTime.getHours();
  return hour >= SLACK_AVAILABILITY_START && hour < SLACK_AVAILABILITY_END;
}

export default executeCommuncationCheck;
