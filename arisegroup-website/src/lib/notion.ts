// Notion CRM Integration
import { Client } from '@notionhq/client'

const notion = new Client({
  auth: process.env.NOTION_API_KEY,
})

const DATABASE_ID = process.env.NOTION_DATABASE_ID || ''

export interface Lead {
  name: string
  email: string
  company?: string
  vertical: 'Defense' | 'Industrial' | 'E-commerce' | 'Construction' | 'Other'
  message?: string
  phone?: string
  source: string // 'website-contact' | 'website-booking' | 'newsletter'
  url?: string // Page they submitted from
}

export async function createLeadInNotion(lead: Lead) {
  try {
    const response = await notion.pages.create({
      parent: { database_id: DATABASE_ID },
      properties: {
        'Contact': {
          title: [
            {
              text: {
                content: lead.name,
              },
            },
          ],
        },
        'Email': {
          email: lead.email,
        },
        'Company': {
          rich_text: [
            {
              text: {
                content: lead.company || '',
              },
            },
          ],
        },
        'Vertical': {
          select: {
            name: lead.vertical,
          },
        },
        'Status': {
          select: {
            name: 'Outreach',
          },
        },
        'Source': {
          select: {
            name: lead.source,
          },
        },
        'Assigned To': {
          select: {
            name: getAssignedFounder(lead.vertical),
          },
        },
        'Q1': {
          rich_text: [
            {
              text: {
                content: lead.message || '',
              },
            },
          ],
        },
        'Phone': {
          phone_number: lead.phone || null,
        },
        'Call Date': {
          date: {
            start: new Date().toISOString(),
          },
        },
      },
    })

    return { success: true, id: response.id }
  } catch (error) {
    console.error('Error creating lead in Notion:', error)
    return { success: false, error }
  }
}

function getAssignedFounder(vertical: string): string {
  const assignments: Record<string, string> = {
    'Defense': 'Mekaiel',
    'Industrial': '4.0 Hero',
    'E-commerce': 'Matthew',
    'Construction': 'Chris',
    'Other': 'Mekaiel', // Default to Mekaiel for routing
  }
  return assignments[vertical] || 'Mekaiel'
}

export async function updateLeadStatus(pageId: string, status: string) {
  try {
    await notion.pages.update({
      page_id: pageId,
      properties: {
        'Status': {
          select: {
            name: status,
          },
        },
      },
    })
    return { success: true }
  } catch (error) {
    console.error('Error updating lead status:', error)
    return { success: false, error }
  }
}
