/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['arisegroup.ai', 'cdn.arisegroup.ai'],
  },
  env: {
    NEXT_PUBLIC_SITE_URL: process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000',
    NEXT_PUBLIC_GA_ID: process.env.NEXT_PUBLIC_GA_ID,
  },
  async redirects() {
    return [
      {
        source: '/book',
        destination: '/book-discovery',
        permanent: true,
      },
    ]
  },
}

module.exports = nextConfig
