// Booking Widget Component (Calendly Integration)
import { InlineWidget } from 'react-calendly'
import { useState } from 'react'

interface BookingWidgetProps {
  vertical?: 'Defense' | 'Industrial' | 'E-commerce' | 'Construction'
  founderName?: string
}

export default function BookingWidget({ vertical, founderName }: BookingWidgetProps) {
  const calendlyUrl = getCalendlyUrl(vertical)

  return (
    <div className="w-full h-[700px]">
      <InlineWidget
        url={calendlyUrl}
        styles={{
          height: '100%',
          minWidth: '320px',
        }}
        prefill={{
          customAnswers: {
            a1: vertical || '',
          },
        }}
      />
    </div>
  )
}

// Vertical Selector Component
export function VerticalSelector({
  onSelect,
}: {
  onSelect: (vertical: string) => void
}) {
  return (
    <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
      <button
        onClick={() => onSelect('Defense')}
        className="p-8 border-2 border-gray-200 rounded-xl hover:border-defense hover:bg-blue-50 transition-all text-left group"
      >
        <div className="text-4xl mb-4">🛡️</div>
        <h3 className="text-xl font-bold mb-2 group-hover:text-defense">
          Defense & Government
        </h3>
        <p className="text-gray-600 mb-4">
          Security compliance, legacy systems, DoD/DoS operations
        </p>
        <p className="text-sm font-medium text-defense">
          → Book with Mekaiel (9 years DoD/DoS, Secret Clearance)
        </p>
      </button>

      <button
        onClick={() => onSelect('Industrial')}
        className="p-8 border-2 border-gray-200 rounded-xl hover:border-industrial hover:bg-green-50 transition-all text-left group"
      >
        <div className="text-4xl mb-4">🏭</div>
        <h3 className="text-xl font-bold mb-2 group-hover:text-industrial">
          Industrial & Manufacturing
        </h3>
        <p className="text-gray-600 mb-4">
          Production data, OT/IT convergence, legacy SCADA/MES systems
        </p>
        <p className="text-sm font-medium text-industrial">
          → Book with 4.0 Hero (22 years industrial automation)
        </p>
      </button>

      <button
        onClick={() => onSelect('E-commerce')}
        className="p-8 border-2 border-gray-200 rounded-xl hover:border-ecommerce hover:bg-orange-50 transition-all text-left group"
      >
        <div className="text-4xl mb-4">🛒</div>
        <h3 className="text-xl font-bold mb-2 group-hover:text-ecommerce">
          E-commerce & Retail
        </h3>
        <p className="text-gray-600 mb-4">
          Customer service, inventory chaos, content bottlenecks
        </p>
        <p className="text-sm font-medium text-ecommerce">
          → Book with Matthew (6 years Amazon, owns e-commerce business)
        </p>
      </button>

      <button
        onClick={() => onSelect('Construction')}
        className="p-8 border-2 border-gray-200 rounded-xl hover:border-construction hover:bg-yellow-50 transition-all text-left group"
      >
        <div className="text-4xl mb-4">🏗️</div>
        <h3 className="text-xl font-bold mb-2 group-hover:text-construction">
          Construction & Building
        </h3>
        <p className="text-gray-600 mb-4">
          Manual estimating, project tracking, revenue leakage
        </p>
        <p className="text-sm font-medium text-construction">
          → Book with Chris (11+ years, recovered $500K+ lost revenue)
        </p>
      </button>
    </div>
  )
}

function getCalendlyUrl(vertical?: string): string {
  // Replace with actual Calendly URLs for each founder
  const calendlyUrls: Record<string, string> = {
    Defense: 'https://calendly.com/mekaiel-arisegroup/discovery',
    Industrial: 'https://calendly.com/40hero-arisegroup/discovery',
    'E-commerce': 'https://calendly.com/matthew-arisegroup/discovery',
    Construction: 'https://calendly.com/chris-arisegroup/discovery',
  }

  return vertical && calendlyUrls[vertical]
    ? calendlyUrls[vertical]
    : 'https://calendly.com/mekaiel-arisegroup/discovery' // Default to Mekaiel
}
