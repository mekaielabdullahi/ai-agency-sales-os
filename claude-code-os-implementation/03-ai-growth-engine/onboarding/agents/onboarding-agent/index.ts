/**
 * Onboarding Agent
 *
 * Automates post-payment client onboarding workflow for AriseGroup.ai
 *
 * Trigger: Stripe payment webhook OR Notion status = "Paid"
 *
 * Workflow:
 * 1. Send gratitude email immediately (< 30 seconds)
 * 2. Update Notion with onboarding timestamps
 * 3. Wait 5 minutes
 * 4. Send next steps email with platform PDF
 * 5. Create Slack channels (client-{name}, client-{name}-internal)
 * 6. Notify team in #new-clients
 */

import { sendGratitudeEmail, sendNextStepsEmail } from './handlers/gmail';
import { createClientChannels, notifyNewClient } from './handlers/slack';
import { updateOnboardingStatus, getClientData } from './handlers/notion';
import { generateSlug, sleep } from './utils';

export interface OnboardingPayload {
  client_id: string;
  client_name: string;
  client_email: string;
  project_type: string;
  amount: number;
  payment_id?: string;
}

export interface OnboardingResult {
  success: boolean;
  client_id: string;
  steps_completed: string[];
  errors: string[];
  timestamps: {
    gratitude_email_sent?: string;
    next_steps_email_sent?: string;
    slack_channels_created?: string;
    team_notified?: string;
  };
}

/**
 * Main onboarding agent execution
 */
export async function executeOnboarding(payload: OnboardingPayload): Promise<OnboardingResult> {
  const result: OnboardingResult = {
    success: false,
    client_id: payload.client_id,
    steps_completed: [],
    errors: [],
    timestamps: {},
  };

  console.log(`[OnboardingAgent] Starting onboarding for ${payload.client_name}`);

  // Step 1: Send gratitude email immediately
  try {
    await sendGratitudeEmail({
      to: payload.client_email,
      clientName: payload.client_name,
      projectType: payload.project_type,
    });
    result.timestamps.gratitude_email_sent = new Date().toISOString();
    result.steps_completed.push('gratitude_email');
    console.log(`[OnboardingAgent] Gratitude email sent to ${payload.client_email}`);
  } catch (error) {
    result.errors.push(`Gratitude email failed: ${error}`);
    console.error(`[OnboardingAgent] Gratitude email error:`, error);
    // Continue - don't block other steps
  }

  // Step 2: Update Notion with initial onboarding status
  try {
    await updateOnboardingStatus(payload.client_id, {
      status: 'Onboarding',
      gratitude_email_sent: result.timestamps.gratitude_email_sent,
      onboarding_started: new Date().toISOString(),
    });
    result.steps_completed.push('notion_initial_update');
    console.log(`[OnboardingAgent] Notion updated for ${payload.client_id}`);
  } catch (error) {
    result.errors.push(`Notion initial update failed: ${error}`);
    console.error(`[OnboardingAgent] Notion update error:`, error);
  }

  // Step 3: Wait 5 minutes before next steps email
  console.log(`[OnboardingAgent] Waiting 5 minutes before next steps email...`);
  await sleep(5 * 60 * 1000); // 5 minutes

  // Step 4: Send next steps email with PDF
  try {
    await sendNextStepsEmail({
      to: payload.client_email,
      clientName: payload.client_name,
      projectType: payload.project_type,
    });
    result.timestamps.next_steps_email_sent = new Date().toISOString();
    result.steps_completed.push('next_steps_email');
    console.log(`[OnboardingAgent] Next steps email sent to ${payload.client_email}`);
  } catch (error) {
    result.errors.push(`Next steps email failed: ${error}`);
    console.error(`[OnboardingAgent] Next steps email error:`, error);
  }

  // Step 5: Create Slack channels
  try {
    const slug = generateSlug(payload.client_name);
    const channels = await createClientChannels({
      clientName: payload.client_name,
      clientEmail: payload.client_email,
      slug,
    });
    result.timestamps.slack_channels_created = new Date().toISOString();
    result.steps_completed.push('slack_channels');
    console.log(`[OnboardingAgent] Slack channels created: ${channels.join(', ')}`);
  } catch (error) {
    result.errors.push(`Slack channels failed: ${error}`);
    console.error(`[OnboardingAgent] Slack channels error:`, error);
  }

  // Step 6: Notify team in #new-clients
  try {
    await notifyNewClient({
      clientName: payload.client_name,
      projectType: payload.project_type,
      amount: payload.amount,
    });
    result.timestamps.team_notified = new Date().toISOString();
    result.steps_completed.push('team_notification');
    console.log(`[OnboardingAgent] Team notified in #new-clients`);
  } catch (error) {
    result.errors.push(`Team notification failed: ${error}`);
    console.error(`[OnboardingAgent] Team notification error:`, error);
  }

  // Step 7: Final Notion update with all timestamps
  try {
    await updateOnboardingStatus(payload.client_id, {
      slack_channels_created: result.timestamps.slack_channels_created,
      next_steps_email_sent: result.timestamps.next_steps_email_sent,
      team_notified: result.timestamps.team_notified,
    });
    result.steps_completed.push('notion_final_update');
  } catch (error) {
    result.errors.push(`Notion final update failed: ${error}`);
  }

  // Determine overall success
  result.success = result.steps_completed.length >= 4; // At least 4 of 6 steps completed

  console.log(`[OnboardingAgent] Onboarding complete for ${payload.client_name}`);
  console.log(`[OnboardingAgent] Steps completed: ${result.steps_completed.join(', ')}`);
  if (result.errors.length > 0) {
    console.log(`[OnboardingAgent] Errors: ${result.errors.join('; ')}`);
  }

  return result;
}

// Export for use as n8n webhook handler
export default executeOnboarding;
