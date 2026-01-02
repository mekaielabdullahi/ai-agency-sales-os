# QA Testing Protocol

## Purpose
Ensure every delivery meets quality standards through systematic testing, catching issues before they reach clients and maintaining our reputation for excellence.

## The Testing Pyramid

```
                /\
               /E2E\        (5%) - Full user flows
              /────\
             / Integ \      (20%) - API & Integration
            /────────\
           /   Unit   \     (75%) - Individual functions
          /────────────\
```

---

## Testing Checklist by Phase

### Pre-Development Testing
```markdown
## Before Code Starts
- [ ] Requirements testable
- [ ] Acceptance criteria clear
- [ ] Test data identified
- [ ] Test environment ready
- [ ] Testing tools selected
```

### During Development Testing
```markdown
## While Building
- [ ] Unit tests written
- [ ] Code coverage >80%
- [ ] Linting passes
- [ ] Local testing done
- [ ] Peer review completed
```

### Pre-Delivery Testing
```markdown
## Before Client Sees
- [ ] All automated tests pass
- [ ] Manual testing complete
- [ ] Cross-browser tested
- [ ] Mobile responsive verified
- [ ] Performance acceptable
- [ ] Security scan clean
- [ ] Accessibility checked
```

---

## Test Types & Coverage

### Unit Testing Standards
```javascript
// Every function should have tests
describe('calculateTotal', () => {
  test('calculates sum correctly', () => {
    expect(calculateTotal([10, 20, 30])).toBe(60);
  });

  test('handles empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });

  test('handles negative numbers', () => {
    expect(calculateTotal([-10, 20])).toBe(10);
  });

  test('throws on invalid input', () => {
    expect(() => calculateTotal('invalid')).toThrow();
  });
});

// Coverage requirements
// Statements: >80%
// Branches: >75%
// Functions: >80%
// Lines: >80%
```

### Integration Testing
```python
# Test API endpoints
def test_user_creation_flow():
    # Create user
    response = client.post('/users', data={
        'email': 'test@example.com',
        'password': 'secure123'
    })
    assert response.status_code == 201
    user_id = response.json()['id']

    # Verify user can login
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'secure123'
    })
    assert response.status_code == 200
    assert 'token' in response.json()

    # Verify user can access protected route
    token = response.json()['token']
    response = client.get(f'/users/{user_id}',
                         headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
```

### End-to-End Testing
```javascript
// Cypress E2E test example
describe('User Journey', () => {
  it('completes full purchase flow', () => {
    cy.visit('/');
    cy.contains('Sign Up').click();
    cy.get('#email').type('test@example.com');
    cy.get('#password').type('secure123');
    cy.get('#submit').click();

    cy.url().should('include', '/dashboard');
    cy.contains('Welcome').should('be.visible');

    cy.get('.product-card').first().click();
    cy.contains('Add to Cart').click();
    cy.contains('Checkout').click();

    cy.get('#card-number').type('4242424242424242');
    cy.get('#exp-date').type('12/25');
    cy.get('#cvc').type('123');
    cy.contains('Complete Purchase').click();

    cy.contains('Order Confirmed').should('be.visible');
  });
});
```

---

## Manual Testing Protocols

### Smoke Test Checklist
```markdown
## Quick Smoke Test (5 minutes)
- [ ] Application loads
- [ ] Can login
- [ ] Main navigation works
- [ ] Core feature functions
- [ ] No console errors
- [ ] Logout works
```

### Comprehensive Test Plan
```markdown
## Full Manual Test Suite

### Authentication
- [ ] Registration with valid data
- [ ] Registration with invalid data
- [ ] Login with correct credentials
- [ ] Login with wrong password
- [ ] Password reset flow
- [ ] Session timeout
- [ ] Concurrent sessions
- [ ] Social login (if applicable)

### Core Features
For each feature:
- [ ] Happy path
- [ ] Edge cases
- [ ] Error states
- [ ] Loading states
- [ ] Empty states
- [ ] Permission checks
- [ ] Data validation

### Cross-Platform
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

### Performance
- [ ] Page load <3 seconds
- [ ] API responses <1 second
- [ ] Smooth scrolling
- [ ] No memory leaks
- [ ] Handles slow network

### Security
- [ ] SQL injection attempts
- [ ] XSS attempts
- [ ] CSRF protection
- [ ] Secure headers
- [ ] HTTPS only
- [ ] No sensitive data in logs
```

---

## Bug Tracking & Resolution

### Bug Report Template
```markdown
## Bug Report #[Number]

**Reporter**: [Name]
**Date**: [Date]
**Severity**: 🔴 Critical / 🟡 Major / 🟢 Minor
**Status**: New / In Progress / Fixed / Verified

### Description
[What's wrong]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Expected Behavior
[What should happen]

### Actual Behavior
[What actually happens]

### Environment
- Browser: [Version]
- OS: [Version]
- User Role: [Role]

### Screenshots/Videos
[Attachments]

### Notes
[Any additional context]
```

### Bug Severity Matrix
| Severity | Description | Response Time | Examples |
|----------|-------------|---------------|----------|
| 🔴 Critical | System unusable | Fix immediately | Can't login, data loss, security breach |
| 🟡 Major | Feature broken | Fix in 24 hours | Can't complete flow, wrong calculations |
| 🟢 Minor | Cosmetic/UX | Fix in milestone | Typos, alignment, minor UX issues |
| ⚪ Low | Enhancement | Consider for next phase | Nice-to-haves, optimizations |

---

## Performance Testing

### Load Testing Checklist
```markdown
## Performance Baselines
- [ ] Response time <1s (95th percentile)
- [ ] Throughput >100 requests/second
- [ ] Error rate <1%
- [ ] CPU usage <80%
- [ ] Memory stable over time

## Tools
- Load testing: K6, JMeter
- Monitoring: New Relic, Datadog
- Profiling: Chrome DevTools
```

### Performance Test Script
```javascript
// K6 load test example
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 100 }, // Ramp up
    { duration: '5m', target: 100 }, // Stay at 100 users
    { duration: '2m', target: 200 }, // Ramp up more
    { duration: '5m', target: 200 }, // Stay at 200 users
    { duration: '2m', target: 0 },   // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<1000'], // 95% of requests under 1s
    http_req_failed: ['rate<0.01'],    // Error rate under 1%
  },
};

export default function() {
  let response = http.get('https://api.example.com/endpoint');
  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

---

## Security Testing

### Security Checklist
```markdown
## OWASP Top 10 Check
- [ ] Injection (SQL, NoSQL, Command)
- [ ] Broken Authentication
- [ ] Sensitive Data Exposure
- [ ] XML External Entities (XXE)
- [ ] Broken Access Control
- [ ] Security Misconfiguration
- [ ] Cross-Site Scripting (XSS)
- [ ] Insecure Deserialization
- [ ] Using Components with Vulnerabilities
- [ ] Insufficient Logging & Monitoring

## Additional Checks
- [ ] HTTPS everywhere
- [ ] Secure cookies
- [ ] Rate limiting
- [ ] Input validation
- [ ] Output encoding
- [ ] Dependency scanning
```

---

## Accessibility Testing

### WCAG 2.1 Compliance
```markdown
## Level A (Minimum)
- [ ] Images have alt text
- [ ] Videos have captions
- [ ] Content readable without CSS
- [ ] Keyboard navigable
- [ ] Focus indicators visible

## Level AA (Target)
- [ ] Color contrast 4.5:1 (normal text)
- [ ] Color contrast 3:1 (large text)
- [ ] Text resizable to 200%
- [ ] No keyboard traps
- [ ] Error identification clear

## Tools
- axe DevTools
- WAVE
- Lighthouse
- Screen readers (NVDA, JAWS)
```

---

## Test Data Management

### Test Data Strategy
```markdown
## Data Sets
1. **Minimum**: Just enough to test
2. **Typical**: Average use case
3. **Maximum**: Stress test limits
4. **Edge Cases**: Unusual but valid

## Data Privacy
- Never use production data in dev
- Anonymize any real data
- Create realistic fake data
- Document test accounts
```

### Test Account Matrix
| Role | Username | Password | Purpose |
|------|----------|----------|---------|
| Admin | admin@test.com | Test123! | Full access testing |
| User | user@test.com | Test123! | Standard user flow |
| Limited | limited@test.com | Test123! | Restricted access |
| Demo | demo@test.com | Demo123! | Client demonstrations |

---

## Quality Gates

### Definition of Done
```markdown
## Feature is "Done" When:
- [ ] Code complete
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Manual testing complete
- [ ] No critical/major bugs
- [ ] Performance acceptable
- [ ] Security scan clean
- [ ] Deployed to staging
- [ ] Product owner approved
```

### Release Criteria
```markdown
## Ready for Production When:
- [ ] All "Done" criteria met
- [ ] E2E tests pass
- [ ] Load testing complete
- [ ] Security audit done
- [ ] Rollback plan ready
- [ ] Monitoring configured
- [ ] Documentation complete
- [ ] Training provided
- [ ] Client sign-off received
```

---

## Testing Metrics

### Track Quality Trends
| Metric | Target | Calculation |
|--------|--------|-------------|
| Defect Density | <5 per KLOC | Bugs / Lines of Code × 1000 |
| Test Coverage | >80% | Lines Tested / Total Lines |
| Defect Escape Rate | <10% | Prod Bugs / Total Bugs |
| Mean Time to Detect | <1 day | Average detection time |
| Mean Time to Resolve | <4 hours | Average fix time |
| Regression Rate | <5% | Reintroduced bugs / Fixed bugs |

---

## The Testing Mantras

```
"Test early, test often"
"Automate the repetitive, manual the creative"
"A bug found early costs 10x less"
"No code without tests"
"Quality is everyone's responsibility"
```