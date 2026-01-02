# Convex Integration Setup Guide

> **Source:** InfinityVault & Idea Brand Coach implementations
> **Last Updated:** 2025-12-07
> **Cost:** Free tier available, $25/month Pro for production

## Why Convex?

- **Real-time by default** - WebSocket subscriptions built-in
- **Type-safe** - End-to-end TypeScript
- **Vector search** - Built-in for AI applications
- **No infrastructure** - Serverless, scales automatically
- **File storage** - Integrated file handling

## Quick Setup

### 1. Initialize Convex
```bash
npm install convex
npx convex dev  # Development mode
npx convex deploy  # Production deployment
```

### 2. Basic Schema Example
```ts
// convex/schema.ts
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  documents: defineTable({
    title: v.string(),
    content: v.string(),
    status: v.union(
      v.literal("pending"),
      v.literal("approved"),
      v.literal("rejected")
    ),
    userId: v.string(),
    createdAt: v.number(),
  })
  .index("by_user", ["userId"])
  .index("by_status", ["status"]),
});
```

### 3. Real-time Query
```tsx
// React component
import { useQuery } from "convex/react";
import { api } from "@/convex/_generated/api";

function DocumentList() {
  const documents = useQuery(api.documents.list);

  // Updates automatically when data changes
  return (
    <div>
      {documents?.map(doc => (
        <div key={doc._id}>{doc.title}</div>
      ))}
    </div>
  );
}
```

### 4. Mutations
```ts
// convex/documents.ts
import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const create = mutation({
  args: {
    title: v.string(),
    content: v.string(),
  },
  handler: async (ctx, args) => {
    const identity = await ctx.auth.getUserIdentity();
    if (!identity) throw new Error("Not authenticated");

    return await ctx.db.insert("documents", {
      ...args,
      userId: identity.subject,
      status: "pending",
      createdAt: Date.now(),
    });
  },
});
```

## Vector Search Setup

### 1. Define Vector Index
```ts
// convex/schema.ts
export default defineSchema({
  knowledge: defineTable({
    text: v.string(),
    embedding: v.array(v.float64()),
  })
  .vectorIndex("by_embedding", {
    vectorField: "embedding",
    dimensions: 1536, // OpenAI embeddings
  }),
});
```

### 2. Search Implementation
```ts
// convex/search.ts
export const searchSimilar = action({
  args: { query: v.string() },
  handler: async (ctx, { query }) => {
    // Generate embedding for query
    const embedding = await generateEmbedding(query);

    // Vector search
    const results = await ctx.vectorSearch("knowledge", "by_embedding", {
      vector: embedding,
      limit: 10,
    });

    return results;
  },
});
```

## File Storage

### 1. Upload Files
```ts
// convex/files.ts
export const generateUploadUrl = mutation(async (ctx) => {
  return await ctx.storage.generateUploadUrl();
});

export const saveFile = mutation({
  args: {
    storageId: v.id("_storage"),
    fileName: v.string(),
  },
  handler: async (ctx, args) => {
    const fileId = await ctx.db.insert("files", {
      storageId: args.storageId,
      name: args.fileName,
      uploadedAt: Date.now(),
    });
    return fileId;
  },
});
```

### 2. Client Upload
```tsx
const uploadFile = async (file: File) => {
  // Get upload URL
  const uploadUrl = await generateUploadUrl();

  // Upload to Convex storage
  const result = await fetch(uploadUrl, {
    method: "POST",
    body: file,
  });
  const { storageId } = await result.json();

  // Save file reference
  await saveFile({ storageId, fileName: file.name });
};
```

## Authentication Integration

### With Clerk
```ts
// convex/auth.config.ts
export default {
  providers: [
    {
      domain: process.env.CLERK_JWT_ISSUER_DOMAIN!,
      applicationID: "convex",
    },
  ],
};
```

### With NextAuth
```ts
// convex/auth.config.ts
export default {
  providers: [
    {
      domain: process.env.AUTH_DOMAIN!,
      applicationID: "convex",
    },
  ],
};
```

## Production Deployment

### 1. Environment Variables
```bash
# .env.production
CONVEX_DEPLOYMENT=prod
NEXT_PUBLIC_CONVEX_URL=https://your-app.convex.cloud
```

### 2. Deploy Command
```bash
npx convex deploy --prod
```

### 3. Set Production Variables
```bash
npx convex env set CLERK_JWT_ISSUER_DOMAIN "your-domain.com" --prod
```

## Common Patterns

### Pagination
```ts
export const listPaginated = query({
  args: {
    cursor: v.optional(v.string()),
    limit: v.number(),
  },
  handler: async (ctx, { cursor, limit }) => {
    const results = await ctx.db
      .query("documents")
      .paginate({
        cursor: cursor || null,
        numItems: limit,
      });

    return results;
  },
});
```

### Soft Delete
```ts
export const softDelete = mutation({
  args: { id: v.id("documents") },
  handler: async (ctx, { id }) => {
    await ctx.db.patch(id, {
      deletedAt: Date.now(),
    });
  },
});
```

### Background Jobs
```ts
export const processDocument = action({
  args: { documentId: v.id("documents") },
  handler: async (ctx, { documentId }) => {
    // Long-running processing
    const result = await analyzeDocument(documentId);

    // Update when complete
    await ctx.runMutation(internal.documents.updateAnalysis, {
      documentId,
      analysis: result,
    });
  },
});
```

## Cost Optimization

- **Free tier**: 1M function calls/month
- **Pro ($25/mo)**: 25M function calls/month
- **Scale**: Pay-as-you-go after limits

### Tips
1. Use indexes for frequent queries
2. Batch operations when possible
3. Cache computed values
4. Use pagination for large datasets

## Resources

- [Convex Docs](https://docs.convex.dev)
- [Convex + Clerk](https://docs.convex.dev/auth/clerk)
- [Vector Search Guide](https://docs.convex.dev/text-search)