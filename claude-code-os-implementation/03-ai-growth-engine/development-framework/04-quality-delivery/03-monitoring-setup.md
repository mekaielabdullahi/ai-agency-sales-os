# Monitoring & Observability Setup

## Purpose
Ensure production systems are observable, issues are detected proactively, and operational insights drive continuous improvement through comprehensive monitoring and alerting.

## The Three Pillars of Observability

```
METRICS: What's happening (numbers)
    ├── Response times
    ├── Error rates
    └── Resource usage

LOGS: Why it happened (events)
    ├── Application logs
    ├── System logs
    └── Audit trails

TRACES: How it happened (flow)
    ├── Request path
    ├── Service calls
    └── Timing breakdown
```

---

## Essential Monitoring Stack

### Core Components
```yaml
# docker-compose.monitoring.yml
version: '3.8'

services:
  # Metrics collection
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  # Visualization
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

  # Log aggregation
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.15.0
    environment:
      - discovery.type=single-node

  # Log shipper
  filebeat:
    image: docker.elastic.co/beats/filebeat:7.15.0
    volumes:
      - ./filebeat.yml:/usr/share/filebeat/filebeat.yml

  # Alerting
  alertmanager:
    image: prom/alertmanager
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
```

---

## Application Metrics

### Key Metrics to Track
```javascript
// Prometheus metrics setup
const promClient = require('prom-client');

// Request duration histogram
const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.1, 0.3, 0.5, 0.7, 1, 3, 5, 7, 10]
});

// Request counter
const httpRequestTotal = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code']
});

// Active connections gauge
const activeConnections = new promClient.Gauge({
  name: 'active_connections',
  help: 'Number of active connections'
});

// Business metrics
const ordersProcessed = new promClient.Counter({
  name: 'orders_processed_total',
  help: 'Total orders processed',
  labelNames: ['status', 'payment_method']
});

// Middleware to track metrics
app.use((req, res, next) => {
  const start = Date.now();

  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration
      .labels(req.method, req.route?.path || 'unknown', res.statusCode)
      .observe(duration);

    httpRequestTotal
      .labels(req.method, req.route?.path || 'unknown', res.statusCode)
      .inc();
  });

  next();
});
```

### Custom Business Metrics
```javascript
// Track business-specific metrics
function trackBusinessMetrics() {
  // Revenue metrics
  db.orders.sum('amount').then(total => {
    revenueGauge.set(total);
  });

  // User activity
  db.users.count({ lastActive: { $gt: new Date(Date.now() - 86400000) } })
    .then(count => {
      activeUsersGauge.set(count);
    });

  // Conversion funnel
  conversionRate.set({
    step: 'view_product',
    rate: viewToCart / totalViews
  });

  conversionRate.set({
    step: 'add_to_cart',
    rate: cartToCheckout / totalCarts
  });

  conversionRate.set({
    step: 'checkout',
    rate: checkoutToOrder / totalCheckouts
  });
}

// Run every minute
setInterval(trackBusinessMetrics, 60000);
```

---

## Logging Configuration

### Structured Logging Setup
```javascript
// Winston configuration
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'api',
    environment: process.env.NODE_ENV,
    version: process.env.APP_VERSION
  },
  transports: [
    // Console output (development)
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    }),
    // File output (production)
    new winston.transports.File({
      filename: 'logs/error.log',
      level: 'error',
      maxsize: 5242880, // 5MB
      maxFiles: 5
    }),
    new winston.transports.File({
      filename: 'logs/combined.log',
      maxsize: 5242880,
      maxFiles: 5
    })
  ]
});

// Request logging middleware
app.use((req, res, next) => {
  const requestId = uuid.v4();
  req.requestId = requestId;

  logger.info('Request received', {
    requestId,
    method: req.method,
    path: req.path,
    query: req.query,
    ip: req.ip,
    userAgent: req.headers['user-agent']
  });

  const originalSend = res.send;
  res.send = function(data) {
    logger.info('Request completed', {
      requestId,
      statusCode: res.statusCode,
      responseTime: Date.now() - req.startTime
    });
    originalSend.call(this, data);
  };

  req.startTime = Date.now();
  next();
});
```

### Log Aggregation Pattern
```yaml
# filebeat.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/app/*.log
    json.keys_under_root: true
    json.add_error_key: true
    fields:
      app: myapp
      env: production

output.elasticsearch:
  hosts: ["elasticsearch:9200"]
  index: "app-logs-%{+yyyy.MM.dd}"

processors:
  - add_host_metadata:
      when.not.contains:
        tags: forwarded
  - add_docker_metadata: ~
```

---

## Health Checks & Uptime

### Health Check Endpoints
```javascript
// Basic health check
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage(),
    version: process.env.APP_VERSION
  });
});

// Detailed readiness check
app.get('/ready', async (req, res) => {
  const checks = {
    database: 'unknown',
    redis: 'unknown',
    external_api: 'unknown'
  };

  // Check database
  try {
    await db.ping();
    checks.database = 'healthy';
  } catch (error) {
    checks.database = 'unhealthy';
  }

  // Check Redis
  try {
    await redis.ping();
    checks.redis = 'healthy';
  } catch (error) {
    checks.redis = 'unhealthy';
  }

  // Check external API
  try {
    await axios.get('https://api.example.com/health', { timeout: 5000 });
    checks.external_api = 'healthy';
  } catch (error) {
    checks.external_api = 'unhealthy';
  }

  const allHealthy = Object.values(checks).every(status => status === 'healthy');

  res.status(allHealthy ? 200 : 503).json({
    status: allHealthy ? 'ready' : 'not_ready',
    checks,
    timestamp: new Date().toISOString()
  });
});
```

### Uptime Monitoring
```yaml
# uptime-kuma configuration
services:
  uptime-kuma:
    image: louislam/uptime-kuma
    ports:
      - "3001:3001"
    volumes:
      - uptime-data:/app/data

# Monitors to configure:
# - HTTPS: https://app.example.com (60s interval)
# - API Health: https://api.example.com/health (30s interval)
# - Database: postgresql://host:5432 (60s interval)
# - SSL Certificate: Check expiry (daily)
```

---

## Alert Configuration

### Alert Rules
```yaml
# prometheus/alerts.yml
groups:
  - name: application
    interval: 30s
    rules:
      # High error rate
      - alert: HighErrorRate
        expr: rate(http_requests_total{status_code=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value }} errors per second"

      # Slow response time
      - alert: SlowResponseTime
        expr: histogram_quantile(0.95, http_request_duration_seconds) > 1
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "95th percentile response time > 1s"

      # Low disk space
      - alert: LowDiskSpace
        expr: disk_free_percentage < 10
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Less than 10% disk space remaining"

      # High memory usage
      - alert: HighMemoryUsage
        expr: memory_usage_percentage > 90
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Memory usage above 90%"
```

### Alert Routing
```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m

route:
  group_by: ['alertname', 'cluster', 'service']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'default'
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty'
      continue: true
    - match:
        severity: warning
      receiver: 'slack'

receivers:
  - name: 'default'
    email_configs:
      - to: 'team@example.com'

  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: 'YOUR_PD_SERVICE_KEY'

  - name: 'slack'
    slack_configs:
      - api_url: 'YOUR_SLACK_WEBHOOK'
        channel: '#alerts'
        title: 'Alert: {{ .GroupLabels.alertname }}'
```

---

## Dashboard Templates

### Grafana Dashboard JSON
```json
{
  "dashboard": {
    "title": "Application Overview",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [{
          "expr": "rate(http_requests_total[5m])"
        }],
        "type": "graph"
      },
      {
        "title": "Error Rate",
        "targets": [{
          "expr": "rate(http_requests_total{status_code=~'5..'}[5m])"
        }],
        "type": "graph"
      },
      {
        "title": "Response Time (p95)",
        "targets": [{
          "expr": "histogram_quantile(0.95, http_request_duration_seconds)"
        }],
        "type": "graph"
      },
      {
        "title": "Active Users",
        "targets": [{
          "expr": "active_users"
        }],
        "type": "stat"
      }
    ]
  }
}
```

---

## Performance Monitoring

### APM Setup (Application Performance Monitoring)
```javascript
// New Relic setup
require('newrelic');

// DataDog APM
const tracer = require('dd-trace').init({
  service: 'my-app',
  env: process.env.NODE_ENV,
  version: process.env.APP_VERSION,
  analytics: true,
  logInjection: true,
  runtimeMetrics: true,
  profiling: true
});

// Custom spans for business logic
async function processOrder(orderId) {
  const span = tracer.startSpan('order.process');
  span.setTag('order.id', orderId);

  try {
    // Validate order
    const validationSpan = tracer.startSpan('order.validate', {
      childOf: span
    });
    await validateOrder(orderId);
    validationSpan.finish();

    // Process payment
    const paymentSpan = tracer.startSpan('payment.process', {
      childOf: span
    });
    const payment = await processPayment(orderId);
    paymentSpan.setTag('payment.amount', payment.amount);
    paymentSpan.finish();

    // Send confirmation
    const emailSpan = tracer.startSpan('email.send', {
      childOf: span
    });
    await sendConfirmation(orderId);
    emailSpan.finish();

    span.setTag('order.status', 'completed');
  } catch (error) {
    span.setTag('error', true);
    span.setTag('error.message', error.message);
    throw error;
  } finally {
    span.finish();
  }
}
```

---

## Client-Side Monitoring

### Browser Monitoring
```javascript
// Real User Monitoring (RUM)
window.addEventListener('load', () => {
  const perfData = performance.getEntriesByType('navigation')[0];

  // Send to monitoring service
  fetch('/api/metrics/browser', {
    method: 'POST',
    body: JSON.stringify({
      url: window.location.href,
      loadTime: perfData.loadEventEnd - perfData.loadEventStart,
      domContentLoaded: perfData.domContentLoadedEventEnd - perfData.domContentLoadedEventStart,
      firstPaint: performance.getEntriesByName('first-paint')[0]?.startTime,
      firstContentfulPaint: performance.getEntriesByName('first-contentful-paint')[0]?.startTime
    })
  });
});

// Error tracking
window.addEventListener('error', (event) => {
  fetch('/api/metrics/error', {
    method: 'POST',
    body: JSON.stringify({
      message: event.message,
      source: event.filename,
      lineno: event.lineno,
      colno: event.colno,
      stack: event.error?.stack,
      userAgent: navigator.userAgent,
      url: window.location.href
    })
  });
});
```

---

## Monitoring Checklist

### Pre-Production
```markdown
## Monitoring Setup Checklist
- [ ] Health check endpoints configured
- [ ] Metrics collection enabled
- [ ] Logs structured and aggregated
- [ ] Alerts configured
- [ ] Dashboards created
- [ ] APM installed
- [ ] Error tracking enabled
- [ ] Uptime monitoring active
```

### Production Handover
```markdown
## Monitoring Documentation for Client

### Access Points
- Grafana Dashboard: [URL]
- Uptime Monitor: [URL]
- Log Viewer: [URL]
- Alert Manager: [URL]

### Key Metrics to Watch
- Request rate: Normal range 100-500 req/s
- Error rate: Should be <1%
- Response time: Target <500ms p95
- CPU usage: Alert at >80%
- Memory usage: Alert at >90%

### Alert Recipients
- Critical: [Phone numbers]
- Warning: [Email addresses]
- Info: [Slack channel]

### Runbooks
- High error rate: [Link to runbook]
- Database down: [Link to runbook]
- Out of memory: [Link to runbook]
```

---

## Cost Optimization

### Monitoring Costs
| Service | Free Tier | Paid | Our Recommendation |
|---------|-----------|------|-------------------|
| Prometheus | Unlimited | N/A | Use for metrics |
| Grafana | Unlimited | Cloud: $49/mo | Self-host |
| ELK Stack | Unlimited | Cloud: $95/mo | Self-host initially |
| Sentry | 5k events/mo | $26/mo | Use free tier |
| New Relic | 100GB/mo | $99/mo | Use for complex apps |
| Datadog | 5 hosts | $15/host/mo | Enterprise only |

---

## The Monitoring Mantras

```
"Measure everything, alert on what matters"
"Observability before optimization"
"Dashboards for insight, alerts for action"
"Logs tell why, metrics tell what, traces tell how"
"Monitor the business, not just the system"
```