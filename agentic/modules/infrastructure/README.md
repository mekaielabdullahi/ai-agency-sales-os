# agentic-module-infrastructure

Manage team infrastructure with Cloudflare DNS/tunnels and Dokploy containers.

## Features

- Cloudflare DNS record management (CRUD operations)
- Cloudflare tunnel configuration and routing
- Dokploy compose service management
- Sandbox deployment automation

## Installation

```bash
agentic add github.com/arisegroup/agentic-module-infrastructure
```

## Setup

### Cloudflare

1. Create an API token at dash.cloudflare.com
2. Add to `.env`:
   ```
   CLOUDFLARE_API_TOKEN=your-token
   CLOUDFLARE_ACCOUNT_ID=your-account-id
   ```

### Dokploy

1. Get your API key from Dokploy dashboard
2. Add to `.env`:
   ```
   DOKPLOY_URL=https://your-dokploy-instance.com
   DOKPLOY_API_KEY=your-api-key
   ```

## Slash Commands

```
/dns-list                    # List all DNS records
/tunnel-status               # Check tunnel configuration
/sandbox-add <initials>      # Deploy new sandbox
/sandbox-remove <initials>   # Remove sandbox
```

## CLI Usage

### Cloudflare DNS
```bash
./run tools/cloudflare_api.py zones list
./run tools/cloudflare_api.py dns list example.com
./run tools/cloudflare_api.py dns create example.com subdomain target.cfargotunnel.com --proxied
./run tools/cloudflare_api.py dns delete example.com record-id
```

### Cloudflare Tunnels
```bash
./run tools/cloudflare_api.py tunnel list
./run tools/cloudflare_api.py tunnel config <tunnel-id>
./run tools/cloudflare_api.py tunnel route-add <tunnel-id> hostname http://localhost:port
./run tools/cloudflare_api.py tunnel route-remove <tunnel-id> hostname
```

### Dokploy Compose
```bash
./run tools/dokploy_api.py compose create <env-id> <name> --file compose.yaml
./run tools/dokploy_api.py compose update <compose-id> --env "KEY=value"
./run tools/dokploy_api.py compose deploy <compose-id>
./run tools/dokploy_api.py compose get <compose-id> -v
./run tools/dokploy_api.py compose start <compose-id>
./run tools/dokploy_api.py compose stop <compose-id>
./run tools/dokploy_api.py compose delete <compose-id>
```

## Architecture

Traffic flows through:
1. **Cloudflare DNS** - CNAME records point to tunnel
2. **Cloudflare Tunnel** - Routes hostnames to localhost ports
3. **Dokploy** - Manages container lifecycle
4. **Containers** - Run actual services

## Port Management

Each service needs a unique host port. Track assignments in the runbook to avoid conflicts.

| Service | Port |
|---------|------|
| Dokploy | 3000 |
| Production n8n | 5678 |
| Sandbox 1 | 5679 |
| Sandbox 2 | 5680 |
