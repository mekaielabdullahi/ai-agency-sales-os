/**
 * n8n Webhook Handler for Onboarding Agent
 *
 * This file provides the webhook endpoint handler for n8n integration.
 * Deploy this as a serverless function or integrate with your n8n instance.
 *
 * Trigger Sources:
 * 1. Stripe Webhook: payment_intent.succeeded
 * 2. Notion Webhook: Status changed to "Paid"
 */

import { executeOnboarding, OnboardingPayload, OnboardingResult } from './index';
import { findClientByEmail, createClient } from './handlers/notion';

interface StripePaymentEvent {
  type: 'payment_intent.succeeded';
  data: {
    object: {
      id: string;
      amount: number;
      currency: string;
      customer_email: string;
      metadata?: {
        client_name?: string;
        project_type?: string;
      };
    };
  };
}

interface NotionWebhookEvent {
  type: 'page.updated';
  page: {
    id: string;
    properties: {
      Status: { select: { name: string } };
      Name: { title: [{ plain_text: string }] };
      Email: { email: string };
      'Project Type': { select: { name: string } };
      Amount: { number: number };
    };
  };
}

/**
 * Handle Stripe payment webhook
 */
export async function handleStripeWebhook(event: StripePaymentEvent): Promise<OnboardingResult> {
  const payment = event.data.object;

  // Extract client info from payment
  const email = payment.customer_email;
  const name = payment.metadata?.client_name || email.split('@')[0];
  const projectType = payment.metadata?.project_type || 'AI Automation';
  const amount = payment.amount / 100; // Convert cents to dollars

  // Find or create client in Notion
  let clientId: string;
  const existingClient = await findClientByEmail(email);

  if (existingClient) {
    clientId = existingClient.id;
  } else {
    clientId = await createClient({
      name,
      email,
      projectType,
      amount,
    });
  }

  // Execute onboarding workflow
  const payload: OnboardingPayload = {
    client_id: clientId,
    client_name: name,
    client_email: email,
    project_type: projectType,
    amount,
    payment_id: payment.id,
  };

  return await executeOnboarding(payload);
}

/**
 * Handle Notion status change webhook
 */
export async function handleNotionWebhook(event: NotionWebhookEvent): Promise<OnboardingResult | null> {
  const page = event.page;
  const status = page.properties.Status?.select?.name;

  // Only trigger on "Paid" status
  if (status !== 'Paid') {
    console.log(`[Webhook] Ignoring status change to: ${status}`);
    return null;
  }

  // Extract client info
  const payload: OnboardingPayload = {
    client_id: page.id,
    client_name: page.properties.Name?.title?.[0]?.plain_text || 'Unknown',
    client_email: page.properties.Email?.email || '',
    project_type: page.properties['Project Type']?.select?.name || 'AI Automation',
    amount: page.properties.Amount?.number || 0,
  };

  // Validate required fields
  if (!payload.client_email) {
    console.error('[Webhook] Missing client email, cannot proceed with onboarding');
    return null;
  }

  return await executeOnboarding(payload);
}

/**
 * n8n HTTP Request Node handler
 * Use this in your n8n workflow's "Respond to Webhook" node
 */
export async function handleN8nWebhook(body: any, headers: any): Promise<{
  statusCode: number;
  body: any;
}> {
  try {
    // Determine source from headers or body
    const isStripe = headers['stripe-signature'] || body.type?.startsWith('payment');
    const isNotion = body.type === 'page.updated';

    let result: OnboardingResult | null;

    if (isStripe) {
      result = await handleStripeWebhook(body as StripePaymentEvent);
    } else if (isNotion) {
      result = await handleNotionWebhook(body as NotionWebhookEvent);
    } else {
      return {
        statusCode: 400,
        body: { error: 'Unknown webhook source' },
      };
    }

    if (!result) {
      return {
        statusCode: 200,
        body: { message: 'Webhook received but no action taken' },
      };
    }

    return {
      statusCode: result.success ? 200 : 500,
      body: result,
    };
  } catch (error) {
    console.error('[Webhook] Error:', error);
    return {
      statusCode: 500,
      body: { error: String(error) },
    };
  }
}

// Export default for n8n Function node
export default handleN8nWebhook;
