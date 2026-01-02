# Error Handling Standards

## Purpose
Ensure robust, user-friendly error handling that prevents data loss, provides clear feedback, enables quick debugging, and maintains system stability under failure conditions.

## Error Handling Philosophy

```
PREVENT: Validate early, fail fast
CATCH: Handle at appropriate level
LOG: Record everything needed for debugging
RECOVER: Gracefully when possible
INFORM: Users clearly and helpfully
LEARN: From every failure
```

---

## Error Categories & Handling

### Error Classification
| Category | Description | User Message | Logging | Recovery |
|----------|-------------|--------------|---------|----------|
| Validation | Invalid input | Specific guidance | Info | Return to form |
| Business Logic | Rule violation | Explain rule | Warning | Suggest alternative |
| Integration | External service fail | "Service unavailable" | Error | Retry/fallback |
| System | Internal error | "Something went wrong" | Critical | Circuit breaker |
| Security | Auth/permission | "Access denied" | Alert | Block & monitor |

---

## Implementation Standards

### Input Validation Layer
```javascript
// Frontend validation (immediate feedback)
function validateEmail(email) {
  const errors = [];

  if (!email) {
    errors.push('Email is required');
  } else if (!email.includes('@')) {
    errors.push('Please enter a valid email address');
  } else if (email.length > 255) {
    errors.push('Email must be less than 255 characters');
  }

  return {
    isValid: errors.length === 0,
    errors
  };
}

// Backend validation (never trust frontend)
const validateUserInput = (req, res, next) => {
  const { email, password, age } = req.body;
  const errors = {};

  // Email validation
  if (!email) {
    errors.email = 'Email is required';
  } else if (!validator.isEmail(email)) {
    errors.email = 'Invalid email format';
  }

  // Password validation
  if (!password) {
    errors.password = 'Password is required';
  } else if (password.length < 8) {
    errors.password = 'Password must be at least 8 characters';
  } else if (!/\d/.test(password)) {
    errors.password = 'Password must contain at least one number';
  }

  // Age validation
  if (age !== undefined && (age < 13 || age > 120)) {
    errors.age = 'Age must be between 13 and 120';
  }

  if (Object.keys(errors).length > 0) {
    return res.status(400).json({
      success: false,
      errors,
      message: 'Validation failed'
    });
  }

  next();
};
```

### API Error Responses
```javascript
// Standardized error response format
class ApiError extends Error {
  constructor(statusCode, message, details = null) {
    super(message);
    this.statusCode = statusCode;
    this.details = details;
    this.timestamp = new Date().toISOString();
  }

  toJSON() {
    return {
      success: false,
      error: {
        message: this.message,
        details: this.details,
        timestamp: this.timestamp,
        ...(process.env.NODE_ENV === 'development' && {
          stack: this.stack
        })
      }
    };
  }
}

// Error codes mapping
const ErrorCodes = {
  VALIDATION_ERROR: 400,
  UNAUTHORIZED: 401,
  FORBIDDEN: 403,
  NOT_FOUND: 404,
  CONFLICT: 409,
  RATE_LIMITED: 429,
  INTERNAL_ERROR: 500,
  SERVICE_UNAVAILABLE: 503
};

// Usage example
router.post('/users', async (req, res, next) => {
  try {
    const user = await createUser(req.body);
    res.json({ success: true, data: user });
  } catch (error) {
    if (error.code === 'DUPLICATE_EMAIL') {
      next(new ApiError(
        ErrorCodes.CONFLICT,
        'Email already exists',
        { field: 'email', value: req.body.email }
      ));
    } else {
      next(error);
    }
  }
});
```

### Global Error Handler
```javascript
// Express global error handler
const errorHandler = (err, req, res, next) => {
  // Default to 500 server error
  let error = { ...err };
  error.message = err.message;

  // Log error
  logger.error({
    error: err,
    request: {
      method: req.method,
      url: req.url,
      body: req.body,
      user: req.user?.id
    }
  });

  // Mongoose bad ObjectId
  if (err.name === 'CastError') {
    const message = 'Resource not found';
    error = new ApiError(404, message);
  }

  // Mongoose duplicate key
  if (err.code === 11000) {
    const field = Object.keys(err.keyValue)[0];
    const message = `${field} already exists`;
    error = new ApiError(400, message);
  }

  // Mongoose validation error
  if (err.name === 'ValidationError') {
    const details = Object.values(err.errors).map(e => ({
      field: e.path,
      message: e.message
    }));
    error = new ApiError(400, 'Validation failed', details);
  }

  res.status(error.statusCode || 500).json(
    error.toJSON ? error.toJSON() : {
      success: false,
      error: {
        message: error.message || 'Server Error',
        ...(process.env.NODE_ENV === 'development' && {
          stack: err.stack
        })
      }
    }
  );
};
```

---

## Retry & Recovery Strategies

### Exponential Backoff
```javascript
async function retryWithBackoff(fn, maxRetries = 3) {
  let lastError;

  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error;

      // Don't retry on client errors
      if (error.statusCode >= 400 && error.statusCode < 500) {
        throw error;
      }

      // Calculate backoff
      const delay = Math.min(1000 * Math.pow(2, i), 10000);
      const jitter = Math.random() * 1000;

      logger.warn(`Retry ${i + 1}/${maxRetries} after ${delay + jitter}ms`);

      await new Promise(resolve => setTimeout(resolve, delay + jitter));
    }
  }

  throw lastError;
}

// Usage
const result = await retryWithBackoff(async () => {
  return await externalApi.call();
});
```

### Circuit Breaker Pattern
```javascript
class CircuitBreaker {
  constructor(fn, options = {}) {
    this.fn = fn;
    this.failures = 0;
    this.successes = 0;
    this.state = 'CLOSED'; // CLOSED, OPEN, HALF_OPEN
    this.nextAttempt = Date.now();

    this.threshold = options.threshold || 5;
    this.timeout = options.timeout || 60000;
    this.successThreshold = options.successThreshold || 2;
  }

  async call(...args) {
    if (this.state === 'OPEN') {
      if (Date.now() < this.nextAttempt) {
        throw new Error('Circuit breaker is OPEN');
      }
      this.state = 'HALF_OPEN';
    }

    try {
      const result = await this.fn(...args);
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }

  onSuccess() {
    this.failures = 0;

    if (this.state === 'HALF_OPEN') {
      this.successes++;
      if (this.successes >= this.successThreshold) {
        this.state = 'CLOSED';
        this.successes = 0;
      }
    }
  }

  onFailure() {
    this.failures++;
    this.successes = 0;

    if (this.failures >= this.threshold) {
      this.state = 'OPEN';
      this.nextAttempt = Date.now() + this.timeout;
      logger.error(`Circuit breaker opened until ${new Date(this.nextAttempt)}`);
    }
  }
}
```

---

## Logging Standards

### Log Levels & Usage
```javascript
// Log level guidelines
const LogLevels = {
  DEBUG: 'Detailed diagnostic information',
  INFO: 'General informational messages',
  WARN: 'Warning messages, potential issues',
  ERROR: 'Error events, but application continues',
  CRITICAL: 'Critical issues, immediate attention needed'
};

// Structured logging
const logger = {
  debug: (message, meta = {}) => {
    console.log(JSON.stringify({
      level: 'DEBUG',
      timestamp: new Date().toISOString(),
      message,
      ...meta
    }));
  },

  error: (message, error, meta = {}) => {
    console.error(JSON.stringify({
      level: 'ERROR',
      timestamp: new Date().toISOString(),
      message,
      error: {
        message: error.message,
        stack: error.stack,
        code: error.code
      },
      ...meta
    }));
  }
};

// Usage examples
logger.info('User logged in', {
  userId: user.id,
  ip: req.ip,
  userAgent: req.headers['user-agent']
});

logger.error('Payment processing failed', error, {
  userId: user.id,
  amount: payment.amount,
  provider: 'stripe'
});
```

### Error Context Capture
```javascript
// Capture full context for debugging
function captureErrorContext(error, req) {
  return {
    error: {
      message: error.message,
      stack: error.stack,
      code: error.code,
      statusCode: error.statusCode
    },
    request: {
      method: req.method,
      url: req.url,
      headers: req.headers,
      query: req.query,
      body: req.body, // Be careful with sensitive data
      ip: req.ip
    },
    user: req.user ? {
      id: req.user.id,
      email: req.user.email,
      roles: req.user.roles
    } : null,
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV,
    version: process.env.APP_VERSION
  };
}
```

---

## User-Friendly Error Messages

### Message Guidelines
```markdown
## Good Error Messages Have:
1. **What went wrong** (clear description)
2. **Why it went wrong** (if known)
3. **How to fix it** (actionable steps)
4. **Where to get help** (support link)

## Examples:

❌ BAD: "Error 500"
✅ GOOD: "Unable to process your payment. Please check your card details and try again."

❌ BAD: "Invalid input"
✅ GOOD: "Please enter a valid email address (example: user@example.com)"

❌ BAD: "Operation failed"
✅ GOOD: "We couldn't save your changes. Please check your internet connection and try again."
```

### Error Message Templates
```javascript
const ErrorMessages = {
  // Validation
  REQUIRED_FIELD: (field) => `${field} is required`,
  INVALID_FORMAT: (field, format) => `${field} must be in ${format} format`,
  TOO_LONG: (field, max) => `${field} must be less than ${max} characters`,
  TOO_SHORT: (field, min) => `${field} must be at least ${min} characters`,

  // Authentication
  INVALID_CREDENTIALS: 'Invalid email or password',
  SESSION_EXPIRED: 'Your session has expired. Please log in again.',
  UNAUTHORIZED: 'You don\'t have permission to perform this action',

  // Network
  NETWORK_ERROR: 'Connection error. Please check your internet and try again.',
  TIMEOUT: 'Request timed out. Please try again.',
  SERVICE_UNAVAILABLE: 'Service temporarily unavailable. Please try again later.',

  // Business Logic
  INSUFFICIENT_FUNDS: 'Insufficient funds for this transaction',
  DUPLICATE_ENTRY: 'This item already exists',
  QUOTA_EXCEEDED: 'You\'ve reached your limit. Please upgrade your plan.',

  // Generic
  UNKNOWN_ERROR: 'Something went wrong. Please try again or contact support.'
};
```

---

## Frontend Error Handling

### React Error Boundary
```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log to error reporting service
    logger.error('React error boundary caught error', {
      error: error.toString(),
      errorInfo: errorInfo.componentStack
    });

    // Send to monitoring service
    if (window.Sentry) {
      window.Sentry.captureException(error);
    }
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Oops! Something went wrong</h2>
          <p>We're sorry for the inconvenience. Please try refreshing the page.</p>
          <button onClick={() => window.location.reload()}>
            Refresh Page
          </button>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
          </details>
        </div>
      );
    }

    return this.props.children;
  }
}
```

### Form Validation Display
```jsx
function FormField({ name, label, error, ...props }) {
  return (
    <div className={`form-field ${error ? 'has-error' : ''}`}>
      <label htmlFor={name}>{label}</label>
      <input id={name} name={name} {...props} />
      {error && (
        <div className="error-message" role="alert">
          <Icon name="warning" />
          <span>{error}</span>
        </div>
      )}
    </div>
  );
}
```

---

## Monitoring & Alerting

### Error Monitoring Setup
```javascript
// Sentry configuration
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 1.0,
  beforeSend(event, hint) {
    // Filter out known issues
    if (event.exception?.values?.[0]?.type === 'NetworkError') {
      return null;
    }
    // Sanitize sensitive data
    if (event.request?.data) {
      delete event.request.data.password;
      delete event.request.data.creditCard;
    }
    return event;
  }
});
```

### Alert Thresholds
| Metric | Threshold | Action |
|--------|-----------|--------|
| Error rate | >1% | Alert immediately |
| 500 errors | >10/minute | Page on-call |
| Response time | >3 seconds | Investigate |
| Failed logins | >50/minute | Security alert |
| Out of memory | >90% | Scale up |

---

## Testing Error Handling

### Error Testing Checklist
```markdown
## Test All Error Paths
- [ ] Invalid input
- [ ] Missing required fields
- [ ] Boundary conditions
- [ ] Network failures
- [ ] Timeout scenarios
- [ ] Rate limiting
- [ ] Concurrent updates
- [ ] Permission denied
- [ ] Resource not found
- [ ] Service unavailable
```

### Error Testing Examples
```javascript
// Jest test example
describe('Error Handling', () => {
  test('handles validation errors', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'invalid' });

    expect(response.status).toBe(400);
    expect(response.body.success).toBe(false);
    expect(response.body.error.message).toContain('valid email');
  });

  test('handles network failures gracefully', async () => {
    // Mock external service failure
    jest.spyOn(externalApi, 'call').mockRejectedValue(
      new Error('Network error')
    );

    const response = await request(app)
      .post('/api/process')
      .send({ data: 'test' });

    expect(response.status).toBe(503);
    expect(response.body.error.message).toContain('temporarily unavailable');
  });
});
```

---

## The Error Handling Mantras

```
"Fail fast, recover gracefully"
"Log everything, expose nothing"
"Validate input, sanitize output"
"Expect failure, design for resilience"
"Clear messages save support tickets"
```