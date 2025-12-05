// Homepage - Main Landing Page
import { homepageContent } from '../content/homepage'
import ContactForm from '../components/ContactForm'
import NewsletterForm from '../components/NewsletterForm'
import Link from 'next/link'

export default function HomePage() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-gray-50 to-white py-20 px-6">
        <div className="max-w-6xl mx-auto text-center">
          <p className="text-primary-600 font-semibold mb-4">
            {homepageContent.hero.eyebrow}
          </p>
          <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
            {homepageContent.hero.headline}
          </h1>
          <p className="text-xl md:text-2xl text-gray-600 mb-10 max-w-4xl mx-auto">
            {homepageContent.hero.subheadline}
          </p>
          <div className="flex gap-4 justify-center">
            <Link
              href="/book-discovery"
              className="px-8 py-4 bg-black text-white font-semibold rounded-lg hover:bg-gray-800 transition-colors"
            >
              {homepageContent.hero.cta.primary} →
            </Link>
            <Link
              href="/verticals"
              className="px-8 py-4 border-2 border-black text-black font-semibold rounded-lg hover:bg-gray-50 transition-colors"
            >
              {homepageContent.hero.cta.secondary}
            </Link>
          </div>
        </div>
      </section>

      {/* Problem Section */}
      <section className="py-20 px-6 bg-red-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-center">
            {homepageContent.problem.headline}
          </h2>
          <p className="text-xl text-gray-700 mb-12 text-center max-w-3xl mx-auto">
            {homepageContent.problem.description}
          </p>

          <div className="grid md:grid-cols-3 gap-8">
            {homepageContent.problem.stats.map((stat, i) => (
              <div key={i} className="bg-white p-8 rounded-xl text-center">
                <div className="text-5xl font-bold text-red-600 mb-2">
                  {stat.number}
                </div>
                <p className="text-gray-600">{stat.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Solution Section */}
      <section className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-center">
            {homepageContent.solution.headline}
          </h2>
          <p className="text-xl text-gray-600 mb-12 text-center max-w-3xl mx-auto">
            {homepageContent.solution.description}
          </p>

          <div className="grid md:grid-cols-4 gap-6">
            {homepageContent.solution.phases.map((phase, i) => (
              <div key={i} className="bg-gray-50 p-6 rounded-xl">
                <div className="text-sm font-bold text-primary-600 mb-2">
                  {phase.phase}
                </div>
                <h3 className="text-xl font-bold mb-3">{phase.title}</h3>
                <p className="text-gray-600 mb-4 text-sm">{phase.description}</p>
                <p className="text-xs text-gray-500 font-medium">
                  Duration: {phase.duration}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Verticals Section */}
      <section className="py-20 px-6 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-center">
            {homepageContent.verticals.headline}
          </h2>
          <p className="text-xl text-gray-600 mb-12 text-center max-w-3xl mx-auto">
            {homepageContent.verticals.description}
          </p>

          <div className="grid md:grid-cols-2 gap-8">
            {homepageContent.verticals.list.map((v, i) => (
              <div key={i} className="bg-white p-8 rounded-xl">
                <div className="text-5xl mb-4">{v.icon}</div>
                <h3 className="text-2xl font-bold mb-2">{v.vertical}</h3>
                <p className="text-gray-600 mb-4">
                  <strong>{v.founder}</strong> • {v.credentials}
                </p>
                <p className="text-sm font-semibold text-gray-700 mb-2">
                  Common Pain Points:
                </p>
                <ul className="space-y-1 mb-6">
                  {v.painPoints.map((pain, j) => (
                    <li key={j} className="text-sm text-gray-600">
                      → {pain}
                    </li>
                  ))}
                </ul>
                <Link
                  href={`/verticals/${v.vertical.toLowerCase()}`}
                  className="inline-block px-6 py-3 bg-black text-white font-semibold rounded-lg hover:bg-gray-800"
                >
                  {v.cta} →
                </Link>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Q1-Q5 Framework Section */}
      <section className="py-20 px-6">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-center">
            {homepageContent.methodology.headline}
          </h2>
          <p className="text-xl text-gray-600 mb-12 text-center">
            {homepageContent.methodology.description}
          </p>

          <div className="space-y-6">
            {homepageContent.methodology.questions.map((q, i) => (
              <div key={i} className="bg-gray-50 p-6 rounded-xl">
                <h3 className="text-lg font-bold mb-2">{q.question}</h3>
                <p className="text-gray-600 text-sm">
                  <strong>Purpose:</strong> {q.purpose}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Founders Section */}
      <section className="py-20 px-6 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold mb-12 text-center">
            {homepageContent.social_proof.headline}
          </h2>

          <div className="grid md:grid-cols-2 gap-8">
            {homepageContent.social_proof.founders.map((founder, i) => (
              <div key={i} className="bg-white p-8 rounded-xl">
                <h3 className="text-2xl font-bold mb-2">
                  {founder.name} • {founder.vertical}
                </h3>
                <p className="text-gray-600 mb-4">{founder.bio}</p>
                <a
                  href={founder.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-primary-600 hover:text-primary-700 font-medium"
                >
                  Connect on LinkedIn →
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-center">
            {homepageContent.pricing.headline}
          </h2>
          <p className="text-xl text-gray-600 mb-12 text-center max-w-3xl mx-auto">
            {homepageContent.pricing.description}
          </p>

          <div className="bg-gray-50 p-8 rounded-xl mb-12 max-w-3xl mx-auto">
            <h3 className="text-xl font-bold mb-4">Our Pricing Formula:</h3>
            <div className="space-y-3 text-gray-700">
              <p>• {homepageContent.pricing.formula.base}</p>
              <p>• {homepageContent.pricing.formula.prerequisites}</p>
              <p>• {homepageContent.pricing.formula.retainer}</p>
            </div>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {homepageContent.pricing.tiers.map((tier, i) => (
              <div key={i} className="bg-white border-2 border-gray-200 p-6 rounded-xl">
                <h3 className="text-xl font-bold mb-3">{tier.tier}</h3>
                <p className="text-sm text-gray-600 mb-4">
                  <strong>When:</strong> {tier.whenToUse}
                </p>
                <p className="text-sm text-gray-600 mb-4">
                  <strong>Structure:</strong> {tier.structure}
                </p>
                <p className="text-lg font-bold text-primary-600">
                  {tier.typical}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Newsletter Section */}
      <section className="py-20 px-6 bg-gray-50">
        <div className="max-w-2xl mx-auto">
          <NewsletterForm source="homepage-newsletter" />
        </div>
      </section>

      {/* Final CTA Section */}
      <section className="py-20 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            {homepageContent.cta.headline}
          </h2>
          <p className="text-xl text-gray-600 mb-12">
            {homepageContent.cta.description}
          </p>

          <div className="bg-gray-50 p-8 rounded-xl mb-10 text-left max-w-2xl mx-auto">
            <ol className="space-y-4">
              {homepageContent.cta.steps.map((step, i) => (
                <li key={i} className="flex gap-3">
                  <span className="flex-shrink-0 w-8 h-8 bg-black text-white rounded-full flex items-center justify-center font-bold">
                    {i + 1}
                  </span>
                  <span className="text-gray-700">{step}</span>
                </li>
              ))}
            </ol>
          </div>

          <Link
            href="/book-discovery"
            className="inline-block px-10 py-5 bg-black text-white text-xl font-semibold rounded-lg hover:bg-gray-800 transition-colors"
          >
            {homepageContent.cta.button} →
          </Link>
        </div>
      </section>
    </div>
  )
}
