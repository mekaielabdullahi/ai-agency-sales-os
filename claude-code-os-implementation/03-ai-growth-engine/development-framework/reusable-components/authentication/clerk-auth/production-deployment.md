# Clerk Production Deployment Guide

> **Source:** InfinityVault implementation
> **Last Updated:** 2025-12-07
> **Cost:** $20/month for Pro tier (up to 10,000 monthly active users)

## Quick Start Checklist

### 1. Create Production Instance
- [ ] Navigate to [Clerk Dashboard](https://dashboard.clerk.com)
- [ ] Clone development settings (recommended)
- [ ] Get production keys (`pk_live_...`, `sk_live_...`)

### 2. DNS Configuration
- [ ] Add CNAME record for satellite domain (e.g., `clerk.yourdomain.com`)
- [ ] Wait for DNS propagation (5-15 minutes typical)
- [ ] Deploy certificates in Clerk Dashboard

### 3. Environment Variables

**Frontend (Vercel/Amplify):**
```bash
VITE_CLERK_PUBLISHABLE_KEY=pk_live_...
# or NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY for Next.js
```

**Backend (Convex):**
```bash
CLERK_JWT_ISSUER_DOMAIN=clerk.yourdomain.com  # NO https://
ALLOWED_ORIGINS=https://yourdomain.com,...
```

### 4. Security Configuration

**CSP Headers (in deployment config):**
```yaml
Content-Security-Policy:
  script-src:
    - 'https://*.clerk.accounts.dev'
    - 'https://clerk.yourdomain.com'
  connect-src:
    - 'https://clerk.yourdomain.com'
  frame-src:
    - 'https://clerk.yourdomain.com'
```

## Common Patterns

### JWT Authentication (Recommended)
- No webhooks needed
- Simpler backend integration
- Works with Convex out of the box

### OAuth Setup (Optional)
1. Enable in Clerk Dashboard
2. Get OAuth credentials from provider
3. Configure redirect URLs
4. Test authentication flow

## Troubleshooting

### "Not authenticated" errors
- Check `CLERK_JWT_ISSUER_DOMAIN` (no https://)
- Verify CORS/ALLOWED_ORIGINS includes your domain

### CSP blocking Clerk
- Update CSP headers to include Clerk domains
- Check browser console for violations

### JWT validation fails
- Decode publishable key to verify domain matches
- Ensure backend has matching issuer domain

## Implementation Examples

### React + Vite
```tsx
// main.tsx
import { ClerkProvider } from '@clerk/clerk-react'

const clerkPubKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

<ClerkProvider publishableKey={clerkPubKey}>
  <App />
</ClerkProvider>
```

### Next.js
```tsx
// app/layout.tsx
import { ClerkProvider } from '@clerk/nextjs'

export default function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

### Convex Backend
```ts
// convex/auth.config.ts
export default {
  providers: [
    {
      domain: process.env.CLERK_JWT_ISSUER_DOMAIN!,
      applicationID: "convex",
    },
  ],
}
```

## Cost Optimization

- **Free tier:** Up to 10,000 monthly active users
- **Pro tier ($20/mo):** Unlimited users, priority support
- **Enterprise:** Custom pricing for advanced features

## Resources

- [Official Clerk Docs](https://clerk.com/docs)
- [Clerk + Convex Integration](https://docs.convex.dev/auth/clerk)
- [InfinityVault Full Implementation](/Users/matthewkerns/workspace/InfinityVaultWebsite/docs/production/CLERK_PRODUCTION_DEPLOYMENT.md)