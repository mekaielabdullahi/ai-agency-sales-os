// Contact Page
import ContactForm from '../components/ContactForm'
import Link from 'next/link'

export default function ContactPage() {
  return (
    <div className="min-h-screen py-20 px-6">
      <div className="max-w-5xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Let's Talk About Your AI Transformation
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            No generic pitch. We'll ask 5 questions to understand your operation, then give you a custom roadmap.
          </p>
        </div>

        {/* Two Column Layout */}
        <div className="grid md:grid-cols-2 gap-12">
          {/* Left: Contact Form */}
          <div>
            <h2 className="text-2xl font-bold mb-6">Send Us a Message</h2>
            <ContactForm />
          </div>

          {/* Right: Info & CTA */}
          <div className="space-y-8">
            <div>
              <h2 className="text-2xl font-bold mb-4">
                Or Book a Discovery Call
              </h2>
              <p className="text-gray-600 mb-6">
                Prefer to talk directly? Book 15 minutes with the founder who specializes in your vertical.
              </p>
              <Link
                href="/book-discovery"
                className="inline-block px-6 py-3 bg-black text-white font-semibold rounded-lg hover:bg-gray-800"
              >
                Book Discovery Call →
              </Link>
            </div>

            <div className="bg-gray-50 p-6 rounded-xl">
              <h3 className="text-lg font-bold mb-4">What Happens Next?</h3>
              <ol className="space-y-3">
                <li className="flex gap-3">
                  <span className="flex-shrink-0 w-6 h-6 bg-black text-white rounded-full flex items-center justify-center text-sm font-bold">
                    1
                  </span>
                  <span className="text-gray-700">
                    We'll review your message within 24 hours
                  </span>
                </li>
                <li className="flex gap-3">
                  <span className="flex-shrink-0 w-6 h-6 bg-black text-white rounded-full flex items-center justify-center text-sm font-bold">
                    2
                  </span>
                  <span className="text-gray-700">
                    If it's a good fit, we'll schedule a 15-minute discovery call
                  </span>
                </li>
                <li className="flex gap-3">
                  <span className="flex-shrink-0 w-6 h-6 bg-black text-white rounded-full flex items-center justify-center text-sm font-bold">
                    3
                  </span>
                  <span className="text-gray-700">
                    We'll ask Q1-Q5 to understand your operation
                  </span>
                </li>
                <li className="flex gap-3">
                  <span className="flex-shrink-0 w-6 h-6 bg-black text-white rounded-full flex items-center justify-center text-sm font-bold">
                    4
                  </span>
                  <span className="text-gray-700">
                    Within 48 hours, you get a custom proposal
                  </span>
                </li>
              </ol>
            </div>

            <div className="border-l-4 border-primary-500 pl-6 py-4">
              <p className="text-gray-700 italic">
                "We're not a typical AI agency. We build the foundation first: documentation, integration, infrastructure. Then AI on top. That's why our projects actually work."
              </p>
              <p className="mt-3 font-semibold">— Mekaiel, AriseGroup Defense</p>
            </div>

            <div>
              <h3 className="text-lg font-bold mb-3">Direct Contact</h3>
              <p className="text-gray-600 mb-2">
                Email: <a href="mailto:hello@arisegroup.ai" className="text-primary-600 hover:underline">hello@arisegroup.ai</a>
              </p>
              <p className="text-gray-600">
                LinkedIn: <a href="https://linkedin.com/company/arisegroup" target="_blank" rel="noopener noreferrer" className="text-primary-600 hover:underline">@arisegroup</a>
              </p>
            </div>
          </div>
        </div>

        {/* Verticals Quick Links */}
        <div className="mt-20">
          <h2 className="text-2xl font-bold mb-6 text-center">
            Select Your Vertical
          </h2>
          <div className="grid md:grid-cols-4 gap-4">
            {['Defense', 'Industrial', 'E-commerce', 'Construction'].map((vertical) => (
              <Link
                key={vertical}
                href={`/verticals/${vertical.toLowerCase()}`}
                className="p-6 border-2 border-gray-200 rounded-xl hover:border-primary-500 hover:bg-primary-50 transition-all text-center group"
              >
                <h3 className="font-bold group-hover:text-primary-600">
                  {vertical} →
                </h3>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
