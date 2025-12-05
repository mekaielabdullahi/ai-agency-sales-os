// Newsletter Signup Component
import { useState } from 'react'

interface NewsletterFormProps {
  source?: string
  variant?: 'inline' | 'popup'
}

export default function NewsletterForm({ source, variant = 'inline' }: NewsletterFormProps) {
  const [email, setEmail] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [status, setStatus] = useState<'idle' | 'success' | 'error'>('idle')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    setStatus('idle')

    try {
      const response = await fetch('/api/newsletter', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          source: source || 'website-newsletter',
        }),
      })

      if (!response.ok) {
        throw new Error('Failed to subscribe')
      }

      setStatus('success')
      setEmail('')
    } catch (error) {
      console.error('Newsletter signup error:', error)
      setStatus('error')
    } finally {
      setIsSubmitting(false)
    }
  }

  if (variant === 'inline') {
    return (
      <div className="bg-gray-50 p-8 rounded-xl">
        <h3 className="text-2xl font-bold mb-2">Get AI Transformation Insights</h3>
        <p className="text-gray-600 mb-6">
          Case studies, methodologies, and what actually works (not generic "AI is great" content).
        </p>

        <form onSubmit={handleSubmit} className="flex gap-3">
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="your@email.com"
            required
            className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
          />
          <button
            type="submit"
            disabled={isSubmitting}
            className="px-6 py-3 bg-black text-white font-semibold rounded-lg hover:bg-gray-800 disabled:bg-gray-400 whitespace-nowrap"
          >
            {isSubmitting ? 'Subscribing...' : 'Subscribe'}
          </button>
        </form>

        {status === 'success' && (
          <p className="mt-3 text-green-700 font-medium">
            ✓ Subscribed! Check your email for confirmation.
          </p>
        )}

        {status === 'error' && (
          <p className="mt-3 text-red-700">
            ✗ Failed to subscribe. Please try again.
          </p>
        )}

        <p className="mt-3 text-xs text-gray-500">
          No spam. Unsubscribe anytime. We respect your inbox.
        </p>
      </div>
    )
  }

  // Popup variant (for exit intent, etc.)
  return (
    <div className="bg-white p-6 rounded-xl shadow-2xl max-w-md">
      <h3 className="text-xl font-bold mb-2">Before you go...</h3>
      <p className="text-gray-600 mb-4">
        Get our weekly insights on AI transformation (the real work, not the hype).
      </p>

      <form onSubmit={handleSubmit} className="space-y-3">
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="your@email.com"
          required
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500"
        />
        <button
          type="submit"
          disabled={isSubmitting}
          className="w-full px-6 py-2 bg-black text-white font-semibold rounded-lg hover:bg-gray-800 disabled:bg-gray-400"
        >
          {isSubmitting ? 'Subscribing...' : 'Subscribe'}
        </button>
      </form>

      {status === 'success' && (
        <p className="mt-3 text-green-700 text-sm font-medium">
          ✓ Subscribed! Check your email.
        </p>
      )}

      {status === 'error' && (
        <p className="mt-3 text-red-700 text-sm">
          ✗ Failed. Please try again.
        </p>
      )}
    </div>
  )
}
