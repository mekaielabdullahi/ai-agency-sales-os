// Email Service (SendGrid/Resend)
import sgMail from '@sendgrid/mail'

sgMail.setApiKey(process.env.SENDGRID_API_KEY || '')

const FROM_EMAIL = 'hello@arisegroup.ai'
const FROM_NAME = 'AriseGroup'

export interface EmailData {
  to: string
  subject: string
  html: string
  text?: string
}

export async function sendEmail(data: EmailData) {
  try {
    await sgMail.send({
      from: {
        email: FROM_EMAIL,
        name: FROM_NAME,
      },
      to: data.to,
      subject: data.subject,
      html: data.html,
      text: data.text || data.html.replace(/<[^>]*>?/gm, ''),
    })
    return { success: true }
  } catch (error) {
    console.error('Error sending email:', error)
    return { success: false, error }
  }
}

// Confirmation email to lead
export async function sendContactConfirmation(name: string, email: string, vertical: string) {
  const founderName = getFounderName(vertical)

  const html = `
    <div style="font-family: system-ui, sans-serif; max-width: 600px; margin: 0 auto;">
      <h2>Thanks for reaching out, ${name}</h2>

      <p>We received your message and ${founderName} (our ${vertical} specialist) will review it shortly.</p>

      <p><strong>What happens next:</strong></p>
      <ol>
        <li>${founderName} will review your inquiry within 24 hours</li>
        <li>If it's a good fit, we'll schedule a 15-minute discovery call</li>
        <li>During the call, we'll ask 5 questions to understand your operation</li>
        <li>Then we'll provide a custom roadmap (no generic pitch)</li>
      </ol>

      <p>In the meantime, you might find these insights helpful:</p>
      <ul>
        <li><a href="https://arisegroup.ai/insights">Latest AI transformation insights</a></li>
        <li><a href="https://arisegroup.ai/verticals/${vertical.toLowerCase()}">How we help ${vertical} companies</a></li>
      </ul>

      <p>Talk soon,</p>
      <p><strong>AriseGroup Team</strong></p>

      <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;" />
      <p style="font-size: 12px; color: #666;">
        AriseGroup | AI Transformation for ${vertical}<br />
        <a href="https://arisegroup.ai">arisegroup.ai</a>
      </p>
    </div>
  `

  return sendEmail({
    to: email,
    subject: `We received your message - AriseGroup`,
    html,
  })
}

// Notification email to founder
export async function sendFounderNotification(lead: {
  name: string
  email: string
  company?: string
  vertical: string
  message?: string
  phone?: string
}) {
  const founderEmail = getFounderEmail(lead.vertical)

  const html = `
    <div style="font-family: monospace; max-width: 600px; margin: 0 auto;">
      <h2>🎯 New Lead: ${lead.vertical}</h2>

      <table style="width: 100%; border-collapse: collapse;">
        <tr>
          <td style="padding: 8px; font-weight: bold;">Name:</td>
          <td style="padding: 8px;">${lead.name}</td>
        </tr>
        <tr>
          <td style="padding: 8px; font-weight: bold;">Email:</td>
          <td style="padding: 8px;"><a href="mailto:${lead.email}">${lead.email}</a></td>
        </tr>
        <tr>
          <td style="padding: 8px; font-weight: bold;">Company:</td>
          <td style="padding: 8px;">${lead.company || 'Not provided'}</td>
        </tr>
        <tr>
          <td style="padding: 8px; font-weight: bold;">Phone:</td>
          <td style="padding: 8px;">${lead.phone || 'Not provided'}</td>
        </tr>
        <tr>
          <td style="padding: 8px; font-weight: bold;">Vertical:</td>
          <td style="padding: 8px;">${lead.vertical}</td>
        </tr>
      </table>

      <h3>Message:</h3>
      <p style="background: #f5f5f5; padding: 15px; border-left: 3px solid #333;">
        ${lead.message || 'No message provided'}
      </p>

      <hr style="margin: 30px 0;" />

      <p><strong>Next Steps:</strong></p>
      <ol>
        <li>Review in Notion CRM (already synced)</li>
        <li>Reply within 24 hours</li>
        <li>Book discovery call if qualified</li>
      </ol>

      <p><a href="https://notion.so" style="display: inline-block; padding: 10px 20px; background: #000; color: #fff; text-decoration: none; border-radius: 4px;">View in Notion CRM →</a></p>
    </div>
  `

  return sendEmail({
    to: founderEmail,
    subject: `New ${lead.vertical} Lead: ${lead.name} from ${lead.company || 'website'}`,
    html,
  })
}

function getFounderName(vertical: string): string {
  const names: Record<string, string> = {
    'Defense': 'Mekaiel',
    'Industrial': '4.0 Hero',
    'E-commerce': 'Matthew',
    'Construction': 'Chris',
  }
  return names[vertical] || 'Mekaiel'
}

function getFounderEmail(vertical: string): string {
  const emails: Record<string, string> = {
    'Defense': 'mekaiel@arisegroup.ai',
    'Industrial': '40hero@arisegroup.ai',
    'E-commerce': 'matthew@arisegroup.ai',
    'Construction': 'chris@arisegroup.ai',
  }
  return emails[vertical] || 'mekaiel@arisegroup.ai'
}
