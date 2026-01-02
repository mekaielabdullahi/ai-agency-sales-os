# Phase 4: Validation & Testing

**Duration:** 15-30 minutes
**Tools:** Test runners, metrics tools, monitoring setup
**Gate:** All tests pass, metrics instrumented

---

## Purpose

Validate that the code produced in Phase 3 meets all requirements, handles errors properly, and has appropriate instrumentation for production.

---

## Inputs

- Feature branches with completed code (from Phase 3)
- Test specifications (from Phase 2)
- Acceptance criteria (from PRD)

---

## Validation Checklist

### 1. Automated Tests

#### Unit Tests
```bash
npm test
# or
pytest
```

- [ ] All unit tests pass
- [ ] Core logic has coverage
- [ ] Edge cases tested
- [ ] Error paths tested

#### Integration Tests
```bash
npm run test:int
```

- [ ] API endpoints validated
- [ ] Database operations verified
- [ ] External service mocks working
- [ ] Auth flows tested

#### E2E Tests (if UI)
```bash
npm run test:e2e
```

- [ ] Critical user flows pass
- [ ] Cross-browser basics verified
- [ ] Mobile responsiveness checked
- [ ] Error states display correctly

### 2. Error Handling

- [ ] All API endpoints return proper error codes
- [ ] Error messages are user-friendly
- [ ] Sensitive info not leaked in errors
- [ ] Retry logic implemented where needed
- [ ] Graceful degradation for external services

### 3. Metrics Instrumentation

| Category | What to Check |
|----------|---------------|
| **Performance** | Response times, load times, error rates |
| **Usage** | Key user actions tracked |
| **Business** | Conversion events, success metrics |
| **Technical** | CPU, memory, queue depth |

- [ ] Error tracking configured (Sentry or equivalent)
- [ ] Performance monitoring active
- [ ] Key business events tracked
- [ ] Alerting thresholds set

### 4. Logging

- [ ] Structured logging implemented
- [ ] Log levels appropriate (info, warn, error)
- [ ] No sensitive data in logs
- [ ] Correlation IDs for request tracing

---

## Metrics Instrumentation Guide

### Error Tracking (Sentry Example)
```typescript
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 1.0,
});
```

### Performance Monitoring
```typescript
// Track API response times
const startTime = Date.now();
// ... operation
const duration = Date.now() - startTime;
metrics.histogram('api.response_time', duration, { endpoint });
```

### Business Events
```typescript
// Track key user actions
analytics.track('feature_used', {
  userId,
  feature: 'dashboard_export',
  timestamp: new Date(),
});
```

---

## Test Commands

```bash
# Run all tests
npm run test:all

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- path/to/test.spec.ts

# Run E2E in headed mode (debug)
npm run test:e2e -- --headed
```

---

## Validation Process

### Step 1: Run Full Test Suite
```bash
npm run test:all
```

Document any failures and address before proceeding.

### Step 2: Manual Testing Checklist
- [ ] Happy path works as expected
- [ ] Error states handled gracefully
- [ ] Edge cases behave correctly
- [ ] Performance is acceptable

### Step 3: Metrics Verification
- [ ] Check Sentry for any captured errors
- [ ] Verify metrics appearing in dashboard
- [ ] Confirm alerting rules are active
- [ ] Test alert notifications work

### Step 4: Security Check
- [ ] No exposed secrets in code
- [ ] Auth/authz working correctly
- [ ] Input validation in place
- [ ] SQL injection prevented
- [ ] XSS prevention (if web)

---

## Outputs

- Test results report
- Coverage report
- Metrics dashboard link
- Known issues document (if any)

---

## Quality Gate: Validation Complete

Before moving to Phase 5 (Delivery):

- [ ] All automated tests pass
- [ ] Test coverage meets threshold (e.g., 80%)
- [ ] Error handling verified
- [ ] Metrics instrumentation confirmed
- [ ] Logging verified
- [ ] Security checklist complete
- [ ] No critical bugs outstanding

---

## Common Validation Issues

| Issue | Resolution |
|-------|------------|
| Flaky tests | Identify race conditions, add retries |
| Low coverage | Add tests for uncovered paths |
| Missing metrics | Add instrumentation before merge |
| Slow tests | Optimize or parallelize |
| Memory leaks | Profile and fix before production |

---

## Templates

- [Test Report Template](./templates/test-report.md)
- [Validation Checklist](./templates/validation-checklist.md)
- [Metrics Setup Guide](./templates/metrics-setup.md)
