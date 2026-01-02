# Component Pricing Calculator

## Quick Pricing Formula

```javascript
function calculatePrice(component) {
  const baseCost = component.implementationHours * hourlyRate;
  const customizationCost = component.customizationHours * hourlyRate;
  const totalCost = baseCost + customizationCost + monthlyServices;

  // Pricing strategies
  const costPlus = totalCost * 3;  // 3x markup (67% margin)
  const valueBased = clientValueCreated * 0.25;  // 25% of value
  const marketRate = competitorPrice * 0.9;  // 10% under market

  return Math.max(costPlus, Math.min(valueBased, marketRate));
}
```

## Component Pricing Matrix

### Invoice Automation Pricing

| Scenario | Dev Hours | Dev Cost | Your Price | Margin | Notes |
|----------|-----------|----------|------------|--------|-------|
| **First Build** | 40 hrs | $4,000 | $12,000 | 67% | Building from scratch |
| **Template Exists** | 8 hrs | $800 | $8,000 | 90% | Using component library |
| **Simple Config** | 2 hrs | $200 | $5,000 | 96% | Just branding changes |
| **With Integration** | 16 hrs | $1,600 | $10,000 | 84% | QuickBooks/Xero addon |

### Authentication System Pricing

| Scenario | Dev Hours | Dev Cost | Your Price | Margin | Notes |
|----------|-----------|----------|------------|--------|-------|
| **Clerk Setup** | 2 hrs | $200 | $2,000 | 90% | Standard implementation |
| **+ Social Login** | 4 hrs | $400 | $3,000 | 87% | Google/GitHub OAuth |
| **+ Role System** | 8 hrs | $800 | $4,500 | 82% | RBAC implementation |
| **Enterprise SSO** | 16 hrs | $1,600 | $8,000 | 80% | SAML/AD integration |

### AI Chatbot Pricing

| Scenario | Dev Hours | Dev Cost | Your Price | Margin | Notes |
|----------|-----------|----------|------------|--------|-------|
| **Basic Chatbot** | 8 hrs | $800 | $5,000 | 84% | GPT-4 with context |
| **+ Knowledge Base** | 16 hrs | $1,600 | $8,000 | 80% | Vector DB + RAG |
| **+ Voice Interface** | 24 hrs | $2,400 | $12,000 | 80% | ElevenLabs integration |
| **Custom Training** | 40 hrs | $4,000 | $20,000 | 80% | Fine-tuned model |

## Value-Based Pricing Worksheet

### Step 1: Calculate Client Value

```
Annual Manual Cost = (Hours/Week × 52) × Hourly Rate
Example: (10 hrs/week × 52) × $50/hr = $26,000/year

Efficiency Gain = Current Cost × Automation %
Example: $26,000 × 0.80 = $20,800 saved/year

Error Reduction Value = Errors/Year × Cost per Error
Example: 100 errors × $500/error = $50,000/year

Total Annual Value = Efficiency + Error Reduction + Speed Value
Example: $20,800 + $50,000 + $10,000 = $80,800/year
```

### Step 2: Price Determination

```
One-Time Setup = Annual Value × 0.25
Example: $80,800 × 0.25 = $20,200

Monthly Subscription = Annual Value / 12 × 0.15
Example: $80,800 / 12 × 0.15 = $1,010/month

Recommended Package:
- Setup: $15,000 (leaving room for negotiation)
- Monthly: $800 (attractive price point)
- Client ROI: 3 months
```

## Package Templates

### Starter Package
```
Perfect for: Small businesses, simple needs
Components: 1 core feature
Customization: Minimal (branding only)
Support: Email only
Setup: $2,500-5,000
Monthly: $199-399
Margin Target: 85%+
```

### Professional Package
```
Perfect for: Growing companies
Components: 2-3 integrated features
Customization: Moderate
Support: Priority email + monthly call
Setup: $7,500-15,000
Monthly: $599-999
Margin Target: 80%+
```

### Enterprise Package
```
Perfect for: Large organizations
Components: Full system
Customization: Extensive
Support: Dedicated slack channel
Setup: $20,000-50,000
Monthly: $1,999-4,999
Margin Target: 75%+
```

## Upsell Opportunities

| Add-On | Hours | Cost | Price | Margin |
|--------|-------|------|-------|--------|
| API Access | 4 | $400 | $2,000 | 80% |
| Custom Reports | 8 | $800 | $3,500 | 77% |
| Additional Integration | 8 | $800 | $4,000 | 80% |
| White Label | 2 | $200 | $2,500 | 92% |
| Priority Support | 0 | $50/mo | $500/mo | 90% |
| Training Session | 2 | $200 | $1,000 | 80% |
| Custom ML Model | 40 | $4,000 | $15,000 | 73% |

## Competitive Pricing Analysis

### Invoice Automation Market
- **Canned Solutions**: $50-200/month (limited customization)
- **Enterprise Software**: $50,000-200,000 (overkill for SMB)
- **Your Sweet Spot**: $5,000-15,000 setup + $500-1,500/month
- **Why You Win**: Custom fit, faster implementation, better ROI

### AI Chatbot Market
- **Basic Bots**: $50-500/month (template-based)
- **Custom Development**: $30,000-100,000 (agencies)
- **Your Sweet Spot**: $5,000-20,000 setup + $500-2,000/month
- **Why You Win**: Real AI, custom training, integrated with their systems

## Discounting Strategy

### Never Discount More Than 20%

```
Original Quote: $10,000
Max Discount: $2,000 (20%)
Final Price: $8,000
Still Maintaining: 75% margin

If client needs lower price:
- Remove features instead
- Extend timeline
- Reduce support level
```

### Bundle Discounts

```
Component A: $5,000
Component B: $5,000
Component C: $5,000

Individual Total: $15,000
Bundle Price: $12,000 (20% off)
Bundle Margin: Still 85%+
```

## Payment Terms

### Standard Terms
```
Option 1: Net 30
- 50% on contract signing
- 50% on delivery
- Premium: 0%

Option 2: Extended Payment
- 33% on signing
- 33% at milestone 1
- 34% on completion
- Premium: 10% added to total

Option 3: Monthly Installments
- 12-month payment plan
- Premium: 20% added to total
```

### Incentives for Fast Payment
```
Pay in Full Upfront: 10% discount
Net 10: 5% discount
Credit Card: Add 3% processing fee
```

## ROI Pitch Templates

### For CFOs/Financial Decision Makers
```
Investment: $15,000 setup + $800/month
Year 1 Cost: $24,600

Current Process Cost: $80,000/year
After Automation: $16,000/year
Savings: $64,000/year

ROI: 260% in Year 1
Payback Period: 4.6 months
5-Year NPV: $241,000
```

### For Operations Managers
```
Current: 40 hours/week on invoice processing
After: 4 hours/week on exceptions only
Time Freed Up: 36 hours/week

Value of Freed Time:
36 hours × $75/hour × 52 weeks = $140,400/year
Investment: $24,600/year
Net Benefit: $115,800/year
```

## Margin Protection Rules

1. **Never go below 3x cost** (67% margin minimum)
2. **Add 20% buffer** for scope creep
3. **Charge for everything** (meetings, revisions, support)
4. **Value price enterprise** (they have budget)
5. **Bundle for higher margins** (economies of scale)

## Quick Quote Generator

```javascript
// Copy this into your calculations

const quickQuote = {
  // Base costs (your internal)
  componentCost: 1000,      // From library
  customizationHours: 8,    // Client specific
  hourlyRate: 100,          // Developer rate

  // Calculate
  totalCost: function() {
    return this.componentCost + (this.customizationHours * this.hourlyRate);
  },

  // Pricing options
  aggressive: function() { return this.totalCost() * 5; },    // 80% margin
  standard: function() { return this.totalCost() * 3.5; },    // 71% margin
  competitive: function() { return this.totalCost() * 2.5; }, // 60% margin

  // Monthly recurring
  monthly: function() { return Math.round(this.standard() * 0.08); }
};

// Example output:
// Cost: $1,800
// Aggressive: $9,000
// Standard: $6,300
// Competitive: $4,500
// Monthly: $504
```

## Remember

- **Price for value, not time**
- **Higher prices = perceived higher quality**
- **Always present 3 options** (anchor high)
- **Focus on ROI, not cost**
- **Document everything for next time**