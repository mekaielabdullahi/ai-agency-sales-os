# Plotter Mechanix - Hardware Rental Model Requirements

**Discovery Date:** 2025-12-09
**Source:** PDF Summary Analysis
**Priority:** P1 - New Revenue Stream
**Target Market:** AEC (Architecture, Engineering, Construction) clients

---

## 💰 Business Model Overview

### Split Revenue Structure
1. **Infrastructure Access Fee:** $300-450/month (fixed)
   - Covers equipment placement
   - Guarantees availability
   - Includes basic maintenance

2. **Variable Usage Fees:** Consumables-based
   - Ink/toner charges
   - Paper/media costs
   - **60% profit margins** on consumables

### Value Proposition
- Immediate access without asset ownership
- No capital expenditure for clients
- Avoid outsourcing delays
- On-site printing capability
- Predictable monthly costs

---

## 🎯 Target Customer Profile

### Primary: AEC Firms
- Architecture firms
- Engineering consultancies
- Construction companies
- Design studios

### Customer Needs:
- Large format printing on-demand
- No asset ownership desired
- Quick turnaround requirements
- Professional print quality
- Cost predictability

### Current Pain Points They Face:
- High equipment purchase costs
- Maintenance headaches
- Outsourcing delays
- Quality control issues
- Unpredictable print costs

---

## 📊 Revenue Model Calculations

### Example Client Scenario:
- **Base fee:** $400/month (midpoint)
- **Usage:** 200 prints/month
- **Consumable cost:** $2/print to Kelsey
- **Consumable charge:** $5/print to client (60% margin)
- **Monthly revenue:** $400 + (200 × $5) = $1,400/client

### Scale Potential:
| Clients | Fixed Revenue | Usage Revenue | Total Monthly | Annual |
|---------|--------------|---------------|---------------|---------|
| 5 | $2,000 | $5,000 | $7,000 | $84,000 |
| 10 | $4,000 | $10,000 | $14,000 | $168,000 |
| 20 | $8,000 | $20,000 | $28,000 | $336,000 |

---

## 🔧 Technical Requirements

### 1. Fleet Management System
**Purpose:** Track and manage rental equipment

**Features Needed:**
- Equipment inventory tracking
- Client assignment management
- Location tracking (which client has which printer)
- Maintenance scheduling
- Contract management
- Billing integration

**Data Points:**
- Serial numbers
- Model specifications
- Client assignments
- Installation dates
- Service history
- Usage metrics

### 2. IoT Monitoring Dashboard
**Purpose:** Real-time equipment monitoring

**Core Functions:**
- **Status Monitoring**
  - Online/offline status
  - Error states
  - Consumable levels (ink, paper)
  - Print queue status

- **Usage Tracking**
  - Page counts
  - Print job history
  - Consumable consumption
  - Peak usage times

- **Predictive Maintenance**
  - Service interval alerts
  - Part replacement predictions
  - Consumable reorder triggers
  - Failure prediction algorithms

**Technical Stack:**
- SNMP protocol for printer communication
- Cloud-based data aggregation
- Real-time dashboard (web + mobile)
- Alert system (email/SMS/app)

### 3. Automated Billing System
**Purpose:** Accurate usage-based billing

**Requirements:**
- Automatic usage data collection
- Fixed + variable fee calculation
- Invoice generation
- QuickBooks integration
- Payment processing
- Client portal access

**Billing Workflow:**
1. Daily usage data collection via IoT
2. Monthly usage aggregation
3. Calculate fixed + variable charges
4. Generate invoice in QuickBooks
5. Auto-send to client
6. Track payment status

### 4. Client Portal
**Purpose:** Self-service and transparency

**Features:**
- Real-time usage dashboard
- Current month charges
- Historical usage/billing
- Service request submission
- Consumable ordering
- Contract details

---

## 📈 Implementation Phases

### Phase 1: Foundation (Month 1)
- Set up basic fleet tracking spreadsheet
- Document rental contracts
- Manual usage tracking process
- Basic billing workflow in QuickBooks

### Phase 2: IoT Integration (Month 2-3)
- Deploy monitoring sensors/software
- Connect printers to network
- Build monitoring dashboard
- Test data collection

### Phase 3: Automation (Month 4-5)
- Automate usage data collection
- Integrate with billing system
- Launch client portal
- Automate consumable reordering

### Phase 4: Scale (Month 6+)
- Predictive maintenance algorithms
- Advanced analytics
- Mobile app for clients
- Expansion to new markets

---

## 🚨 Critical Success Factors

### Technical Requirements:
1. **Printer Compatibility**
   - Must support network monitoring
   - SNMP or proprietary protocols
   - Remote management capability

2. **Network Infrastructure**
   - Reliable internet at client sites
   - VPN or secure connections
   - Cloud platform (AWS/Azure)

3. **Data Security**
   - Encrypted communications
   - Secure client data storage
   - Compliance with data regulations

### Business Requirements:
1. **Contract Management**
   - Clear SLAs
   - Usage limits/overages
   - Termination clauses
   - Equipment insurance

2. **Service Delivery**
   - 4-hour response time
   - Remote diagnostics capability
   - Spare equipment availability
   - Consumable stock management

3. **Financial Management**
   - Accurate cost tracking
   - Margin analysis per client
   - Cash flow management
   - Equipment depreciation

---

## 💡 Competitive Advantages

### Why This Model Wins:
1. **No Competition** in local market for this model
2. **Recurring Revenue** vs one-time service calls
3. **High Margins** on consumables (60%)
4. **Scalable** without proportional labor increase
5. **Data-Driven** optimization opportunities

### Differentiation:
- On-site equipment (vs outsourcing)
- Real-time monitoring (vs reactive service)
- Predictable costs (vs per-job pricing)
- Immediate access (vs scheduling delays)
- Local support (vs remote vendors)

---

## 📋 Action Items for Rental Model

### Immediate (Week 1):
1. Identify 3-5 pilot customers
2. Survey their current print costs/volume
3. Calculate pricing for pilot program
4. Draft rental agreement template

### Short-term (Month 1):
1. Set up fleet tracking system
2. Configure QuickBooks for rental billing
3. Install monitoring software on test printer
4. Launch pilot with 1-2 clients

### Medium-term (Months 2-3):
1. Build IoT monitoring dashboard
2. Automate usage data collection
3. Integrate with billing system
4. Expand to 5-10 clients

### Long-term (Months 4-6):
1. Launch full client portal
2. Implement predictive maintenance
3. Scale to 20+ clients
4. Explore adjacent markets

---

## 🎯 Success Metrics

### Financial KPIs:
- Monthly Recurring Revenue (MRR)
- Average Revenue Per Client
- Consumable margin percentage
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)

### Operational KPIs:
- Equipment uptime percentage
- Response time to issues
- Consumable stockout incidents
- Service calls per client
- Client satisfaction score

### Growth KPIs:
- New clients per month
- Churn rate
- Expansion revenue (upsells)
- Market share in AEC segment
- Geographic coverage

---

## 🔗 Integration with Existing Systems

### Jobber Integration:
- Service scheduling for maintenance
- Client communication
- Work order management
- Field service tracking

### QuickBooks Integration:
- Automated invoice creation
- Usage data import
- Revenue recognition
- Financial reporting

### Shopify Integration:
- Consumable ordering portal
- Client self-service
- Inventory management
- E-commerce for supplies

---

## 📝 Notes & Considerations

### Risks:
- Equipment damage/theft at client sites
- Network connectivity issues
- Printer compatibility limitations
- Client payment delays
- Consumable supply chain disruptions

### Mitigation:
- Insurance requirements in contracts
- Backup connectivity options (cellular)
- Pilot with compatible equipment first
- Upfront deposits/auto-payment
- Strategic consumable inventory

### Opportunities:
- Expand to other equipment (scanners, plotters)
- Managed print services addition
- Design/print consulting services
- Software licensing bundles
- National franchise model

---

**Status:** Requirements defined - Ready for implementation planning
**Priority:** P1 - New revenue stream with high margins
**Next Steps:** Meeting with Mike to discuss technical feasibility