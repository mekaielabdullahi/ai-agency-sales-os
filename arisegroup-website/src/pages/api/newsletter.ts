// API Route: /api/newsletter
import type { NextApiRequest, NextApiResponse } from 'next'
import { createLeadInNotion } from '../../lib/notion'
import { sendEmail } from '../../lib/email'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  try {
    const { email, source } = req.body

    // Validation
    if (!email) {
      return res.status(400).json({ error: 'Email is required' })
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(email)) {
      return res.status(400).json({ error: 'Invalid email address' })
    }

    // Create minimal lead in Notion
    await createLeadInNotion({
      name: 'Newsletter Subscriber',
      email,
      vertical: 'Other',
      source: source || 'newsletter-signup',
      url: req.headers.referer || 'direct',
    })

    // Send welcome email
    await sendEmail({
      to: email,
      subject: 'Welcome to AriseGroup Insights',
      html: `
        <div style="font-family: system-ui, sans-serif; max-width: 600px; margin: 0 auto;">
          <h2>Thanks for subscribing!</h2>

          <p>You'll now receive our insights on AI transformation, including:</p>
          <ul>
            <li>Case studies from Defense, Industrial, E-commerce, and Construction</li>
            <li>Prerequisites-first methodology breakdowns</li>
            <li>What works (and what doesn't) in AI adoption</li>
            <li>Behind-the-scenes founder learnings</li>
          </ul>

          <p>First up: <strong>"Why 80% of AI Projects Fail (And How to Be in the 20%)"</strong></p>
          <p><a href="https://arisegroup.ai/insights/why-ai-projects-fail" style="display: inline-block; padding: 10px 20px; background: #000; color: #fff; text-decoration: none; border-radius: 4px;">Read the article →</a></p>

          <p>Questions? Just reply to this email.</p>

          <p>— Mekaiel & the AriseGroup team</p>

          <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;" />
          <p style="font-size: 12px; color: #666;">
            AriseGroup | AI Transformation<br />
            <a href="https://arisegroup.ai">arisegroup.ai</a> | <a href="https://arisegroup.ai/unsubscribe">Unsubscribe</a>
          </p>
        </div>
      `,
    })

    return res.status(200).json({
      success: true,
      message: 'Successfully subscribed to newsletter',
    })
  } catch (error) {
    console.error('Newsletter signup error:', error)
    return res.status(500).json({
      error: 'Internal server error',
      message: 'Failed to subscribe. Please try again.',
    })
  }
}
