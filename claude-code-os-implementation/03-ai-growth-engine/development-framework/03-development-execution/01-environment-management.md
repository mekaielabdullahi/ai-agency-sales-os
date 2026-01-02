# Environment Management System

## Purpose
Maintain strict separation between development, staging, and production environments to ensure quality, protect client assets, and maintain payment leverage.

## The Three-Environment Model

```
DEVELOPMENT (We Control)
    ↓ Push when stable
STAGING (We Control, Client Views)
    ↓ Push when paid
PRODUCTION (Client Controls)
```

---

## Environment Setup Checklist

### Development Environment
```markdown
## Dev Environment Setup
**Purpose**: Rapid iteration and testing
**Access**: Developers only
**Deployment**: Continuous

### Infrastructure
- [ ] Git repository created
- [ ] Branch protection disabled (move fast)
- [ ] CI/CD pipeline configured
- [ ] Error reporting enabled (verbose)
- [ ] Test data loaded

### Configuration
- [ ] Environment variables set
- [ ] API keys (dev versions)
- [ ] Database (separate instance)
- [ ] Debug mode enabled
- [ ] Hot reload enabled

### Access Control
- [ ] Developers have full access
- [ ] Basic auth or VPN required
- [ ] Not indexed by search engines
- [ ] No production data

### URL Structure
- dev.projectname.ourcompany.com
- dev-api.projectname.ourcompany.com
```

### Staging Environment
```markdown
## Staging Environment Setup
**Purpose**: Client review and approval
**Access**: Client + Us
**Deployment**: On milestone completion

### Infrastructure
- [ ] Separate server/instance
- [ ] Production-like configuration
- [ ] SSL certificate installed
- [ ] Automated backups enabled
- [ ] Monitoring configured

### Configuration
- [ ] Environment variables (staging)
- [ ] API keys (staging/sandbox)
- [ ] Database (staging copy)
- [ ] Debug mode disabled
- [ ] Performance monitoring on

### Access Control
- [ ] Client has read access
- [ ] We have full control
- [ ] Password protected
- [ ] Not indexed by search engines
- [ ] Activity logging enabled

### URL Structure
- staging.projectname.ourcompany.com
- staging-api.projectname.ourcompany.com
```

### Production Environment
```markdown
## Production Environment Setup
**Purpose**: Live system
**Access**: Client controls
**Deployment**: After payment

### Infrastructure
- [ ] Client's infrastructure
- [ ] High availability setup
- [ ] SSL certificate (client's)
- [ ] Automated backups
- [ ] Full monitoring suite

### Configuration
- [ ] Environment variables (production)
- [ ] API keys (production)
- [ ] Database (production)
- [ ] Debug mode disabled
- [ ] Error reporting (summary only)

### Access Control
- [ ] Client has full control
- [ ] We have no access (unless contracted)
- [ ] Public facing
- [ ] SEO optimized
- [ ] Security hardened

### URL Structure
- www.clientdomain.com
- api.clientdomain.com
```

---

## Environment Variables Management

### Structure Template
```env
# .env.development
NODE_ENV=development
API_URL=http://localhost:3000
DATABASE_URL=postgresql://dev:dev@localhost/dev_db
DEBUG=true
LOG_LEVEL=verbose
STRIPE_KEY=sk_test_...
ERROR_REPORTING=verbose

# .env.staging
NODE_ENV=staging
API_URL=https://staging-api.project.com
DATABASE_URL=postgresql://staging:pass@staging-db/staging
DEBUG=false
LOG_LEVEL=info
STRIPE_KEY=sk_test_...
ERROR_REPORTING=summary

# .env.production
NODE_ENV=production
API_URL=https://api.clientdomain.com
DATABASE_URL=postgresql://prod:secure@prod-db/production
DEBUG=false
LOG_LEVEL=error
STRIPE_KEY=sk_live_...
ERROR_REPORTING=critical
```

### Security Rules
1. **Never commit .env files** (use .env.example)
2. **Different keys per environment**
3. **Rotate keys regularly**
4. **Use secrets management in production**
5. **Audit access logs**

---

## Deployment Pipeline

### Development → Staging
```yaml
# Automated deployment on merge to main
on:
  push:
    branches: [main]

deploy-staging:
  - run: npm test
  - run: npm build
  - deploy: staging-server
  - notify: slack-channel
  - create: deployment-log
```

### Staging → Production
```yaml
# Manual deployment after payment confirmed
manual-deploy-production:
  requires:
    - payment-confirmed
    - client-approval
    - staging-tested

  steps:
    - backup: current-production
    - deploy: production-server
    - smoke-test: critical-paths
    - notify: client
    - transfer: credentials
```

---

## Database Management

### Data Separation Strategy
```
Development DB:
├── Fake data only
├── Can be reset anytime
├── Used for testing
└── No PII

Staging DB:
├── Anonymized production copy
├── OR clean test data
├── Safe for demos
└── Regular refreshes

Production DB:
├── Real data
├── Never touch directly
├── Backed up continuously
└── Client owns
```

### Migration Management
```bash
# Development
npm run migrate:dev  # Run all migrations
npm run seed:dev     # Load test data

# Staging
npm run migrate:staging  # Run pending migrations
npm run seed:staging     # Load demo data

# Production
# Client runs after handover
npm run migrate:production  # With backup first
```

---

## Infrastructure as Code

### Terraform Example
```hcl
# environments/staging/main.tf
module "app" {
  source = "../../modules/app"

  environment = "staging"
  instance_type = "t3.small"
  min_instances = 1
  max_instances = 2

  domain = "staging.project.ourcompany.com"
  ssl_cert = var.staging_ssl_cert

  database_size = "db.t3.micro"
  backup_retention = 7
}

# environments/production/main.tf
module "app" {
  source = "../../modules/app"

  environment = "production"
  instance_type = "t3.large"
  min_instances = 2
  max_instances = 10

  domain = "www.clientdomain.com"
  ssl_cert = var.production_ssl_cert

  database_size = "db.r5.large"
  backup_retention = 30
}
```

---

## Cost Management

### Environment Costs
| Environment | Infrastructure | Monthly Cost | Who Pays |
|-------------|---------------|--------------|----------|
| Development | Minimal | $50-100 | Us (overhead) |
| Staging | Production-like | $100-500 | Project budget |
| Production | Full scale | $500-5000+ | Client |

### Cost Optimization
1. **Dev**: Use local or minimal cloud
2. **Staging**: Scale down when not in use
3. **Production**: Client's responsibility
4. **Cleanup**: Terminate after project

---

## Access Control Matrix

| Role | Development | Staging | Production |
|------|------------|---------|------------|
| Our Developers | Full | Full | None |
| Our Architect | Full | Full | Emergency only |
| Client Tech Team | None | Read | Full |
| Client Business | None | Read | Read |
| End Users | None | None | Access |

---

## The Handover Protocol

### Pre-Handover Checklist
```markdown
## Ready for Production Transfer

### Payment Status
- [ ] All invoices paid
- [ ] No outstanding amounts
- [ ] Payment confirmed in bank

### Technical Readiness
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Client trained
- [ ] Staging approved
- [ ] Backups configured

### Transfer Package
- [ ] Source code repository
- [ ] Environment variables
- [ ] Database schemas
- [ ] API documentation
- [ ] Deployment guide
- [ ] Support handover doc
```

### Handover Steps
1. **Payment Confirmation** (Finance clears)
2. **Transfer Meeting** (Screen share walkthrough)
3. **Repository Transfer** (Add client as owner)
4. **Credential Handover** (Secure transmission)
5. **Production Deployment** (With client watching)
6. **Verification** (Client confirms working)
7. **Our Access Removal** (Clean break)

---

## Environment Security

### Security Checklist
```markdown
## Per Environment Security

### Development
- [ ] No production data
- [ ] VPN or IP whitelist
- [ ] Regular dependency updates
- [ ] Code scanning enabled

### Staging
- [ ] Password protected
- [ ] SSL enforced
- [ ] Rate limiting enabled
- [ ] Security headers configured
- [ ] No sensitive data in logs

### Production
- [ ] WAF enabled
- [ ] DDoS protection
- [ ] Automated security patches
- [ ] Intrusion detection
- [ ] Compliance requirements met
```

---

## Monitoring & Alerts

### Environment Monitoring
| Environment | Monitoring Level | Alert Threshold | Response Time |
|-------------|-----------------|-----------------|---------------|
| Development | Basic | Errors only | Next day |
| Staging | Enhanced | Errors + Performance | 4 hours |
| Production | Full | All issues | Client's SLA |

### Key Metrics to Track
```
Development:
- Build success rate
- Test coverage
- Error frequency

Staging:
- Page load time
- API response time
- Error rate
- Uptime

Production:
- All of above
- User analytics
- Business metrics
- Security events
```

---

## Rollback Procedures

### Quick Rollback Strategy
```bash
# Staging rollback (our control)
git revert <commit>
npm run deploy:staging

# Production rollback (client executes)
# 1. Restore from backup
# 2. OR revert to previous version
# 3. Document in incident report
```

---

## Environment Rules

1. **Never test in production**
2. **Never use production data in dev**
3. **Always test in staging before production**
4. **No production access without payment**
5. **Document every environment change**

---

## The Golden Rules

```
"Development is ours to break"
"Staging is where clients approve"
"Production is theirs after payment"
"No payment, no production"
```