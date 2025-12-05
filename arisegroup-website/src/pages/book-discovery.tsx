// Book Discovery Call Page
import { useState } from 'react'
import BookingWidget, { VerticalSelector } from '../components/BookingWidget'

export default function BookDiscoveryPage() {
  const [selectedVertical, setSelectedVertical] = useState<string | null>(null)

  return (
    <div className="min-h-screen py-20 px-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Book Your Discovery Call
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            15 minutes. 5 questions. No pitch. Just a diagnostic conversation to understand your operation.
          </p>
        </div>

        {!selectedVertical ? (
          <>
            {/* Vertical Selection */}
            <div className="mb-12">
              <h2 className="text-2xl font-bold mb-6 text-center">
                Step 1: Select Your Vertical
              </h2>
              <VerticalSelector onSelect={setSelectedVertical} />
            </div>

            {/* What to Expect */}
            <div className="mt-16 bg-gray-50 p-8 rounded-xl max-w-3xl mx-auto">
              <h3 className="text-2xl font-bold mb-6">What to Expect on the Call</h3>

              <div className="space-y-4">
                <div>
                  <h4 className="font-bold text-lg mb-2">Before the call:</h4>
                  <p className="text-gray-600">
                    You'll answer a few pre-call questions (takes 2 minutes). This helps us make the most of our 15 minutes together.
                  </p>
                </div>

                <div>
                  <h4 className="font-bold text-lg mb-2">During the call:</h4>
                  <ul className="space-y-2 text-gray-600">
                    <li>• Q1: What do you do (specifically)?</li>
                    <li>• Q2: What does this cost you monthly?</li>
                    <li>• Q3: What have you tried before?</li>
                    <li>• Q4: Why didn't it work?</li>
                    <li>• Q5: Magic wand solution?</li>
                  </ul>
                </div>

                <div>
                  <h4 className="font-bold text-lg mb-2">After the call:</h4>
                  <p className="text-gray-600">
                    Within 48 hours, you'll receive a custom proposal showing prerequisites-first approach, timeline, and pricing based on your Q2 monthly cost.
                  </p>
                </div>

                <div>
                  <h4 className="font-bold text-lg mb-2">No pressure:</h4>
                  <p className="text-gray-600">
                    If we're not the right fit, we'll tell you. And if you decide not to move forward, no worries—you'll still walk away with a clear understanding of what prerequisites you need.
                  </p>
                </div>
              </div>
            </div>
          </>
        ) : (
          <>
            {/* Booking Widget */}
            <div className="mb-8">
              <button
                onClick={() => setSelectedVertical(null)}
                className="text-primary-600 hover:text-primary-700 font-medium mb-4"
              >
                ← Change Vertical
              </button>
              <h2 className="text-2xl font-bold mb-2">
                Step 2: Choose Your Time ({selectedVertical})
              </h2>
              <p className="text-gray-600 mb-6">
                Select a time that works for you. You'll receive a calendar invite and pre-call questionnaire.
              </p>
            </div>

            <BookingWidget
              vertical={selectedVertical as any}
            />
          </>
        )}
      </div>
    </div>
  )
}
