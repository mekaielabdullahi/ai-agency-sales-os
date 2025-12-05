// API Route: /api/calendly-webhook
// Calendly sends webhook when discovery call is booked
import type { NextApiRequest, NextApiResponse } from 'next'
import { createLeadInNotion, updateLeadStatus } from '../../lib/notion'
import { notifyBooking } from '../../lib/slack'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  try {
    const { event, payload } = req.body

    // Calendly sends 'invitee.created' event when someone books
    if (event !== 'invitee.created') {
      return res.status(200).json({ message: 'Event ignored' })
    }

    const {
      name,
      email,
      text_reminder_number: phone,
      event: eventDetails,
      questions_and_answers: questionsAnswers,
    } = payload

    // Extract vertical from custom questions
    const verticalQuestion = questionsAnswers?.find(
      (qa: any) => qa.question.includes('vertical') || qa.question.includes('industry')
    )
    const vertical = verticalQuestion?.answer || 'Other'

    // Extract company from custom questions
    const companyQuestion = questionsAnswers?.find(
      (qa: any) => qa.question.includes('company') || qa.question.includes('organization')
    )
    const company = companyQuestion?.answer

    // Extract Q1 (what do you do) from custom questions
    const q1Question = questionsAnswers?.find(
      (qa: any) => qa.question.includes('What do you do') || qa.question.includes('business')
    )
    const message = q1Question?.answer

    // Create or update lead in Notion
    const notionResult = await createLeadInNotion({
      name,
      email,
      company,
      vertical,
      message,
      phone,
      source: 'website-booking',
      url: eventDetails.uri,
    })

    // If lead already exists, update status to "Discovery"
    if (notionResult.id) {
      await updateLeadStatus(notionResult.id, 'Discovery')
    }

    // Determine which founder based on vertical
    const founderName = getFounderName(vertical)

    // Send Slack notification to #wins
    await notifyBooking({
      name,
      email,
      vertical,
      date: eventDetails.start_time,
      founder: founderName,
    })

    return res.status(200).json({
      success: true,
      message: 'Booking processed successfully',
    })
  } catch (error) {
    console.error('Calendly webhook error:', error)
    return res.status(500).json({
      error: 'Internal server error',
      message: 'Failed to process booking',
    })
  }
}

function getFounderName(vertical: string): string {
  const assignments: Record<string, string> = {
    'Defense': 'Mekaiel',
    'Industrial': '4.0 Hero',
    'E-commerce': 'Matthew',
    'Construction': 'Chris',
  }
  return assignments[vertical] || 'Mekaiel'
}
