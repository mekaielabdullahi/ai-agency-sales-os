# demo-deploy

Deploy demo applications to Dokploy with GitHub integration and Traefik routing.

## Features

- List existing demo deployments
- Check subdomain availability
- Validate compose files for Traefik compatibility
- Deploy demos with GitHub source integration
- Automatic domain configuration
- Interactive deployment workflow with verification checkpoints

## Setup

This module depends on the `infrastructure` module for Dokploy API access.

Required environment variables in `.env`:

```bash
DOKPLOY_URL=https://your-dokploy-instance.com
DOKPLOY_API_KEY=your-api-key
```

## Slash Commands

```
/demo-deploy              # Start interactive deployment workflow
/demo-deploy list         # List existing demos
/demo-deploy projects     # List available environments
/demo-deploy check <slug> # Check subdomain availability
/demo-deploy validate     # Validate compose file
/demo-deploy redeploy <n> # Redeploy existing demo
```

## CLI Usage

```bash
# List all demos
./run modules/demo-deploy/tool/demo_deploy.py list

# List projects and environments
./run modules/demo-deploy/tool/demo_deploy.py projects

# Check if subdomain is available
./run modules/demo-deploy/tool/demo_deploy.py check my-demo

# Validate compose file
./run modules/demo-deploy/tool/demo_deploy.py validate docker-compose.yml

# Deploy a new demo
./run modules/demo-deploy/tool/demo_deploy.py deploy \
  --environment "env-id" \
  --name "My Demo" \
  --repo "owner/repo" \
  --subdomain "my-demo" \
  --port 3000 \
  --service "app"

# Redeploy existing demo
./run modules/demo-deploy/tool/demo_deploy.py redeploy my-demo
```

## Compose Requirements

Demos must use proper networking for Traefik routing:

```yaml
services:
  app:
    build: .
    networks:
      - dokploy-network

networks:
  dokploy-network:
    external: true
```

See `templates/compose-demo.yaml` for a complete template.

## Architecture

Traffic flows:
1. Browser → `https://slug.arisegroup-tools.com`
2. Cloudflare (TLS) → Tunnel
3. Traefik → Container on `dokploy-network`

**No Cloudflare API interaction needed** - wildcard DNS handles all subdomains.
