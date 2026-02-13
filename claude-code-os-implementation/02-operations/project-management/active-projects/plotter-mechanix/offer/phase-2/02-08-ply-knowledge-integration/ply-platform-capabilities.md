# Ply Platform Capabilities Reference

**Last Updated:** February 8, 2026
**Source:** Ply + Jobber Integration Overview (19-page deck)
**Status:** Production-ready platform with 3,000+ supplier integrations

---

## Platform Overview

Ply is a **production-ready inventory management platform** designed for contractors, with native integrations to QuickBooks, Jobber, and 3,000+ supplier branches.

---

## Core Features

### 1. Smart Catalog Management

**Auto-Built Catalog:**
- Automatically builds catalog from actual purchases and stock
- Folders/Kits for common job material collections
- Auto-pricing adjustments pulled from purchasing data
- Supports 3M+ products from 3,000+ supplier branches

**Key Capabilities:**
- Material categorization and organization
- Bulk pricing updates from supplier integrations
- Custom material folders for job types
- Kit creation for common material bundles

---

### 2. Inventory Management

**Stock Location Management:**
- Track quantity, location, and pricing across multiple locations
- Support for warehouses, shops, and individual trucks
- Per-location min/max thresholds
- Real-time quantity tracking

**Barcode System:**
- Create and import barcodes for materials
- Brother Mobile Solutions printer integration
- Mobile barcode scanning via iOS/Android app
- Barcode-based inventory intake workflow

**Mobile App:**
- iOS and Android native apps
- Barcode scanning capability
- Field inventory management
- Real-time sync with central system

**Auto-Replenishment:**
- Min/max logic triggers
- Per-location replenishment thresholds
- Automatic replenishment list generation
- Integration with purchasing workflow

**Transfer Management:**
- Materials/tools transfer between locations
- Picklists for job-specific material pulls
- Reconciliation without scanning every item
- Transfer history and audit trail

---

### 3. Tools Tracking (NEW FEATURE)

**Virtual Toolbox:**
- Status tracking (Available, In Use, Maintenance, etc.)
- Location assignment for tools
- Tech assignment for accountability
- Serial number tracking (one tool = many serialized versions)

**Use Cases:**
- Track high-value equipment
- Monitor tool location and assignment
- **POTENTIAL:** Track used parts from parted-out machines
- Serial number management for warranty/maintenance

---

### 4. Purchasing & RFQ Management

**RFQ Management:**
- Create RFQs from replenishment lists
- Generate RFQs from project BOMs
- Multi-supplier quote comparison
- Centralized purchasing workflow

**Pricing Visibility:**
- Auto-pull supplier pricing for comparison
- Historical pricing data
- Price trend analysis
- Best-price recommendations

**Purchasing Activities:**
- Centralized purchase order management
- Supplier order tracking
- Receiving workflow
- Purchase history and analytics

---

### 5. Supplier Integrations

**Pre-Integrated Suppliers:**
- Winsupply
- Hajoca
- Ferguson
- Reece Group

**Network Scale:**
- 3,000+ supplier branches nationwide
- 3M+ products available
- Real-time pricing data
- Automatic catalog updates

---

### 6. Software Integrations

**QuickBooks Integration:**
- Auto-update Accounts Receivable (A/R)
- Auto-update Accounts Payable (A/P)
- Cash flow synchronization
- Real-time financial data sync

**Banking Integration:**
- Enhanced credit facilities
- Net terms support
- Payment processing integration

**Jobber Integration (Native, Bidirectional):**
- Material sync (Jobber ↔ Ply)
- Job sync (Jobber → Ply)
- User sync (Jobber → Ply)
- User assignment sync (Jobber → Ply)
- Real-time webhook-based updates

---

## Jobber Integration Details

| Sync Type | Direction | Description | Update Method |
|-----------|-----------|-------------|---------------|
| **Material Sync** | Bidirectional | Materials (NOT services) sync between Jobber and Ply catalogs | Webhooks (real-time) |
| **Job Sync** | Jobber → Ply | Jobs in Jobber sync directly to Ply | Webhooks (real-time) |
| **User Sync** | Jobber → Ply | Jobber users automatically added to Ply | Webhooks (real-time) |
| **User Assignment** | Jobber → Ply | Users assigned to jobs sync with Ply | Webhooks (real-time) |

**Key Points:**
- ✅ Integration is NATIVE, not custom-built
- ✅ Real-time sync via webhooks (no manual sync button)
- ✅ Materials sync bidirectionally
- ⚠️ Services do NOT sync (materials only)
- ✅ Job context flows from Jobber to Ply automatically

---

## Implementation Services

### Ply's Warehouse Audit Service

**Scope:**
- 1-3 trucks configured during initial implementation
- 3-step audit process: Evaluation → Counting/Barcoding → Presentation
- Team training for independent inventory management

**Cost:**
- Starting at $5K (scope-dependent)
- Focused on 1-3 trucks for initial rollout

**Timeline:**
- 4-week onboarding journey

**Deliverable:**
- Partially implemented system
- Team empowered to finish implementation independently
- **NOT** fully turnkey - requires ongoing client effort

### 4-Week Onboarding Journey

| Week | Focus | Activities |
|------|-------|------------|
| **Week 1** | Auditing | Initial evaluation, Q&A, system setup |
| **Week 2** | Purchasing | RFQ process, supplier setup, Q&A |
| **Week 3** | Projects | Project setup, order workflow, Q&A |
| **Week 4** | Suppliers | Supplier integrations, reports, final Q&A |

---

## ROI Case Study

**Example: $3M Contractor Business**

| Metric | Before Ply | After Ply | Impact |
|--------|-----------|-----------|--------|
| Material Spend % | 22% of revenue | 20% of revenue | 2% decrease |
| Annual Material Spend | $660K | $600K | $60K savings |
| Hidden Costs (JIT, tech time) | Not tracked | Eliminated | +$15-20K savings |
| **Total Annual Savings** | — | — | **$75-80K** |

**Savings Breakdown:**
- Material cost optimization: $60K
- Eliminated rush orders/JIT purchases: $10-15K
- Reduced tech time searching for materials: $5K

**Payback Period:**
- Platform cost typically recovered in 6-12 months
- Ongoing savings compound annually

---

## Plotter Mechanix Application

**Current Revenue:** ~$700-800K/year

**Projected Impact:**
- 2% material spend improvement = $14-16K/year savings
- Reduced tech time on inventory management = $3-5K/year
- Eliminated emergency purchases = $2-4K/year
- **Total potential savings: $19-25K/year**

**Key Use Cases:**
1. Track used parts from parted-out machines (Tools feature)
2. Manage new parts inventory across warehouse + trucks
3. Integration with Jobber for job-based material tracking
4. Supplier pricing comparison for parts procurement

---

## Technical Specifications

### API Access
- REST API available
- Webhook support for real-time integrations
- API credentials required for custom integrations

### Mobile Apps
- iOS: Native app with barcode scanning
- Android: Native app with barcode scanning
- Offline mode for field work
- Real-time sync when online

### Data Model
- Materials catalog
- Locations (warehouses, shops, trucks)
- Jobs (synced from Jobber)
- Users (synced from Jobber)
- Tools/equipment tracking
- Purchase orders
- Transfers between locations

---

## Integration Opportunities

### What Ply DOES Have
- ✅ Jobber integration (native, bidirectional)
- ✅ QuickBooks integration
- ✅ Supplier integrations (3,000+ branches)
- ✅ Mobile apps with barcode scanning
- ✅ Tools tracking for serialized equipment

### What Ply DOES NOT Have
- ❌ Quo integration (no native support)
- ❌ Custom workflow automation (requires external tools)
- ❌ Advanced reporting beyond built-in dashboards
- ❌ AI-powered chat interface for inventory queries

---

## Strategic Implications for Our Work

### What We Should NOT Build
1. **Jobber ↔ Ply sync** - Already native, real-time via webhooks
2. **Basic inventory tracking** - Ply handles this natively
3. **Barcode system** - Ply provides this with mobile apps
4. **Supplier integrations** - Already built-in for major suppliers

### What We SHOULD Build
1. **Quo ↔ Ply integration** - No native support, major gap
2. **Chat agent for inventory queries** - "Do we have X in stock?" during Quo calls
3. **Used parts tracking workflow** - May leverage Ply's Tools feature
4. **Custom automation on top of Ply** - Workflow enhancements beyond Ply's core

### Questions to Answer with Megan
1. What Ply features are actively being used?
2. Is Jobber ↔ Ply sync already active?
3. Did they purchase Ply's $5K warehouse audit service?
4. How are used parts currently tracked?
5. What API access do they have?

---

## References

- **Source Document:** Ply + Jobber Integration Overview (19-page deck)
- **Platform Website:** [Ply website - to be confirmed with Megan]
- **Support Resources:** 4-week onboarding program included with implementation

---

*Last Updated: February 8, 2026*
*Next Review: After Megan interview*
