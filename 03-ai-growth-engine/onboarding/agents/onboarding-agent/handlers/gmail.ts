/**
 * Gmail Handler for Onboarding Agent
 *
 * Sends personalized emails using Gmail API
 */

import { getFirstName } from '../utils';

// Environment variables (set in .env)
const GMAIL_CLIENT_ID = process.env.GMAIL_CLIENT_ID;
const GMAIL_CLIENT_SECRET = process.env.GMAIL_CLIENT_SECRET;
const GMAIL_REFRESH_TOKEN = process.env.GMAIL_REFRESH_TOKEN;
const CALENDAR_LINK = process.env.CALENDAR_LINK || 'https://cal.com/arisegroup/logistics';
const FROM_EMAIL = process.env.FROM_EMAIL || 'hello@arisegroup.ai';

interface EmailParams {
  to: string;
  clientName: string;
  projectType: string;
}

/**
 * Send gratitude email immediately after payment
 */
export async function sendGratitudeEmail(params: EmailParams): Promise<void> {
  const { to, clientName, projectType } = params;
  const firstName = getFirstName(clientName);

  const subject = "Welcome to AriseGroup! We're excited to work with you";

  const htmlBody = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
      <p>Hi ${firstName},</p>

      <p>Thank you for choosing AriseGroup! We're genuinely excited to partner with you on <strong>${projectType}</strong>.</p>

      <p>Your payment has been received and your project is now officially underway.</p>

      <h3 style="color: #333;">What happens next:</h3>
      <ul>
        <li>You'll receive a detailed "Next Steps" email in about 5 minutes with everything you need to get started</li>
        <li>Our team has been notified and is preparing your project workspace</li>
        <li>We'll reach out within 24 hours to schedule your Logistics Onboarding Call</li>
      </ul>

      <p>In the meantime, if you have any questions, reply to this email or message us on Slack (invite coming soon!).</p>

      <p>Let's build something great together.</p>

      <p>Best,<br>The AriseGroup Team</p>

      <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
      <p style="color: #666; font-size: 12px;"><em>AriseGroup.ai - AI Solutions That Actually Work</em></p>
    </div>
  `;

  await sendEmail({ to, subject, htmlBody });
}

/**
 * Send next steps email with calendar link and platform guide
 */
export async function sendNextStepsEmail(params: EmailParams): Promise<void> {
  const { to, clientName, projectType } = params;
  const firstName = getFirstName(clientName);

  const subject = 'Your AriseGroup Onboarding - Next Steps Inside';

  const htmlBody = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
      <p>Hi ${firstName},</p>

      <p>Great to have you on board! Here's everything you need to get started with your <strong>${projectType}</strong> project.</p>

      <h2 style="color: #333;">Your Next Steps</h2>

      <h3 style="color: #555;">1. Schedule Your Logistics Onboarding Call (15-30 min)</h3>
      <p>This is where we'll collect all the platform access we need to start building. We'll handle any two-factor authentication live on the call so you don't have to worry about codes later.</p>
      <p><a href="${CALENDAR_LINK}" style="display: inline-block; background: #4F46E5; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">Schedule Your Call →</a></p>

      <h3 style="color: #555;">2. Review the Attached Platform Guide</h3>
      <p>I've attached a PDF with the platforms we'll need access to. Don't worry about setting anything up beforehand - we'll walk through everything together on the call.</p>

      <h3 style="color: #555;">3. Join Our Slack Workspace</h3>
      <p>You'll receive a Slack invite shortly. This is where all project communication will happen. We're available for quick questions during our daily window (12-2pm PT).</p>

      <h2 style="color: #333;">What to Expect</h2>
      <ul>
        <li><strong>Logistics Call:</strong> We collect platform access and handle 2FA</li>
        <li><strong>Kickoff Call (60 min):</strong> We present your audit findings and walk through the solutions</li>
        <li><strong>Build Phase:</strong> We build your systems with 2x weekly progress updates</li>
        <li><strong>Delivery:</strong> You receive a complete delivery report with all documentation</li>
      </ul>

      <h2 style="color: #333;">Communication Protocol</h2>
      <ul>
        <li><strong>Progress Updates:</strong> Tuesdays and Fridays</li>
        <li><strong>Slack Availability:</strong> 12-2pm PT daily</li>
        <li><strong>Urgent Issues:</strong> Flag with "URGENT" in Slack for priority response</li>
      </ul>

      <p>If you have any questions before our call, reply to this email or reach out on Slack.</p>

      <p>Looking forward to building with you!</p>

      <p>Best,<br>The AriseGroup Team</p>

      <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
      <p style="color: #666; font-size: 12px;"><em>AriseGroup.ai - AI Solutions That Actually Work</em></p>
    </div>
  `;

  // TODO: Attach PDF based on projectType
  await sendEmail({ to, subject, htmlBody });
}

/**
 * Internal function to send email via Gmail API
 */
async function sendEmail(params: { to: string; subject: string; htmlBody: string }): Promise<void> {
  const { to, subject, htmlBody } = params;

  // Create raw email in base64
  const rawEmail = [
    `From: AriseGroup <${FROM_EMAIL}>`,
    `To: ${to}`,
    `Subject: ${subject}`,
    'MIME-Version: 1.0',
    'Content-Type: text/html; charset=utf-8',
    '',
    htmlBody,
  ].join('\r\n');

  const encodedEmail = Buffer.from(rawEmail).toString('base64url');

  // Get access token
  const accessToken = await getAccessToken();

  // Send via Gmail API
  const response = await fetch('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${accessToken}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ raw: encodedEmail }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Gmail API error: ${response.status} ${error}`);
  }

  console.log(`[Gmail] Email sent to ${to}: ${subject}`);
}

/**
 * Get OAuth access token from refresh token
 */
async function getAccessToken(): Promise<string> {
  const response = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      client_id: GMAIL_CLIENT_ID!,
      client_secret: GMAIL_CLIENT_SECRET!,
      refresh_token: GMAIL_REFRESH_TOKEN!,
      grant_type: 'refresh_token',
    }),
  });

  if (!response.ok) {
    throw new Error(`Failed to refresh Gmail token: ${response.status}`);
  }

  const data = await response.json();
  return data.access_token;
}
