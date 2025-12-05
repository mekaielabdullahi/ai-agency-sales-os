// API Route: /api/contact
import type { NextApiRequest, NextApiResponse } from 'next'
import { createLeadInNotion } from '../../lib/notion'
import { sendContactConfirmation, sendFounderNotification } from '../../lib/email'
import { notifyNewLead } from '../../lib/slack'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  try {
    const { name, email, company, vertical, message, phone } = req.body

    // Validation
    if (!name || !email || !vertical) {
      return res.status(400).json({
        error: 'Missing required fields: name, email, vertical',
      })
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(email)) {
      return res.status(400).json({ error: 'Invalid email address' })
    }

    // Create lead in Notion CRM
    const notionResult = await createLeadInNotion({
      name,
      email,
      company,
      vertical,
      message,
      phone,
      source: 'website-contact',
      url: req.headers.referer || 'direct',
    })

    if (!notionResult.success) {
      console.error('Notion sync failed:', notionResult.error)
      // Continue anyway - don't fail the submission
    }

    // Send confirmation email to lead
    await sendContactConfirmation(name, email, vertical)

    // Send notification email to assigned founder
    await sendFounderNotification({
      name,
      email,
      company,
      vertical,
      message,
      phone,
    })

    // Send Slack notification to #pipeline
    await notifyNewLead({
      name,
      email,
      company,
      vertical,
      source: 'website-contact',
    })

    return res.status(200).json({
      success: true,
      message: 'Contact form submitted successfully',
    })
  } catch (error) {
    console.error('Contact form error:', error)
    return res.status(500).json({
      error: 'Internal server error',
      message: 'Failed to submit form. Please try again.',
    })
  }
}
