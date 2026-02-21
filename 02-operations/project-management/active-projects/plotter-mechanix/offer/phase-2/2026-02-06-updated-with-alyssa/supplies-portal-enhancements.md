# Supplies Portal Enhancement Specifications
## Based on Alyssa Part 2 Interview Findings

**Date:** February 6, 2026
**Current Demo:** ~/workspace/plotter-mechanix/demo-site-v2/src/app/dashboard/supplies/

---

## Current Portal Features (Already Built)

### ✅ What's Working in Demo
- Basic inventory table with search/filter
- Stock level tracking (quantity, min stock)
- Location tracking (Warehouse A/B, Truck 1/2)
- Category organization (Printheads, Maintenance, Parts, Ink, Blades)
- Status indicators (In Stock, Low Stock, Out of Stock)
- Total value calculation
- Basic add/remove buttons

---

## Required Enhancements (From Alyssa Interview)

### 1. 🔴 CRITICAL: Barcode System Integration

**Alyssa's Pain Point:**
> *"If we had barcodes, that would be so much easier... I'd be able to know exactly and what date it was"*

**New Features Needed:**
```typescript
// Add to inventory item model
interface InventoryItem {
  // Existing fields...
  barcode: string;
  poNumber: string;
  receiveDate: Date;
  vendorId: string;
  deliverySlipId?: string;
  serialNumber?: string;
}
```

**UI Components:**
- Barcode scanner button (mobile camera integration)
- "Receive Shipment" workflow with PO linking
- Print barcode labels function
- Quick scan lookup field

---

### 2. 🔴 CRITICAL: PO Number Tracking & RMA Management

**Alyssa's Pain Point:**
> *"We don't know which POs everything's from... pile of RMA stuff from last year"*

**New Features Needed:**
- PO history tab for each item
- RMA tracking dashboard
- Vendor claim status
- Automated follow-up reminders

**New Page:** `/dashboard/supplies/rma`
```jsx
// RMA Dashboard showing:
- Pending RMAs with age
- Required documentation checklist
- Vendor response tracking
- Credit/replacement status
- Link to original PO and delivery slip
```

---

### 3. 🟡 HIGH: Parts Lookup & Compatibility Database

**Alyssa's Pain Point:**
> *"It takes me about half an hour to try and figure it out because I don't know parts"*

**New Features Needed:**
- "Find Parts by Printer" search
- Compatibility matrix
- Cross-reference tool
- Integration with Alyssa's "Printer Info for Dummies"

**New Component:** Parts Finder Widget
```jsx
<PartsFinder>
  - Select printer brand → model → part type
  - Shows compatible SKUs with stock status
  - Links to vendor catalogs
  - Displays Alyssa's notes/tips
</PartsFinder>
```

---

### 4. 🟡 HIGH: Vendor Integration & Automated Ordering

**Alyssa's Pain Point:**
> *"30 minutes research plus 15 minutes vendor communication per order"*

**New Features Needed:**
- Vendor catalog API integration
- Quick quote generator
- One-click reorder for common items
- Order history by vendor
- Price comparison tool

**Vendor Quick Actions:**
```jsx
// For each low-stock item:
- "Get Quote" → auto-emails vendors
- "View Last Order" → shows previous PO
- "Reorder Same" → duplicates last order
- "Find Alternatives" → shows substitutes
```

---

### 5. 🟡 HIGH: Real-Time Multi-Location Sync

**Alyssa's Pain Point:**
> *"I manually check the inventory... check to see if we actually have it"*

**New Features Needed:**
- Live sync with Jobber job completion
- Truck inventory mobile app
- Transfer between locations workflow
- "Where is it?" search across all locations

**Location Features:**
```jsx
// Enhanced location tracking:
- Warehouse A: Shelves 1-10 with bin locations
- Warehouse B: Shelves 1-5 with bin locations
- Truck 1: Current tech, route, inventory
- Truck 2: Current tech, route, inventory
- In Transit: Items being moved
```

---

### 6. 🟢 MEDIUM: Customer Self-Service Integration

**Alyssa's Pain Point:**
> *"I don't know what paper goes to what plotter"*

**New Features Needed:**
- Public "What supplies do I need?" tool
- Customer portal supplies ordering
- Auto-generate quotes from compatibility
- Send direct Jobber quotes

**Customer Portal Addition:** `/portal/supplies`
```jsx
// Customer sees:
- Their equipment on file
- Compatible supplies for each
- Current stock status
- One-click order request
- Order history
```

---

### 7. 🟢 MEDIUM: Email Integration for Order Processing

**Alyssa's Pain Point:**
> *"10 email inboxes... receipts from vendors go to sales, some go to accounting"*

**New Features Needed:**
- Email parser for vendor receipts
- Auto-import tracking numbers
- PO matching from email invoices
- Unified vendor communication log

---

## Implementation Priorities

### Week 1: Quick Fixes
1. Add PO number field to existing inventory
2. Add barcode field (manual entry initially)
3. Create basic RMA tracking list

### Weeks 2-4: Barcode System
1. Implement barcode scanning (mobile)
2. Receiving workflow with PO linking
3. Label printing functionality
4. Delivery slip attachment

### Weeks 5-6: Parts Database
1. Import Alyssa's "Printer Info for Dummies"
2. Build compatibility matrix
3. Create parts finder interface
4. Add to customer portal

### Weeks 7-8: Vendor Integration
1. Email parsing for receipts
2. Quote request automation
3. Reorder shortcuts
4. Price tracking

---

## Database Schema Updates

```sql
-- Add to inventory table
ALTER TABLE inventory ADD COLUMN barcode VARCHAR(50);
ALTER TABLE inventory ADD COLUMN po_number VARCHAR(50);
ALTER TABLE inventory ADD COLUMN receive_date TIMESTAMP;
ALTER TABLE inventory ADD COLUMN vendor_id INTEGER;
ALTER TABLE inventory ADD COLUMN delivery_slip_url TEXT;

-- New tables needed
CREATE TABLE purchase_orders (
  id SERIAL PRIMARY KEY,
  po_number VARCHAR(50) UNIQUE,
  vendor_id INTEGER,
  order_date TIMESTAMP,
  receive_date TIMESTAMP,
  total_amount DECIMAL(10,2),
  status VARCHAR(20),
  notes TEXT
);

CREATE TABLE rma_tracking (
  id SERIAL PRIMARY KEY,
  inventory_id INTEGER,
  po_number VARCHAR(50),
  issue_date TIMESTAMP,
  vendor_response TEXT,
  status VARCHAR(20),
  resolution TEXT,
  credit_amount DECIMAL(10,2)
);

CREATE TABLE printer_compatibility (
  id SERIAL PRIMARY KEY,
  printer_brand VARCHAR(50),
  printer_model VARCHAR(100),
  part_sku VARCHAR(50),
  part_type VARCHAR(50),
  notes TEXT -- Alyssa's tips
);
```

---

## Mobile App Requirements

### Warehouse Receiving App
- Camera barcode scanning
- PO lookup and verification
- Location assignment (shelf/bin)
- Delivery slip photo capture
- Quick receive workflow

### Truck Inventory App
- Check stock on truck
- Transfer items between locations
- Use parts on jobs (auto-deduct)
- Request supplies from warehouse
- End-of-day inventory count

---

## Success Metrics

### 30 Days
- All items have PO numbers attached
- Barcode scanning operational
- RMA backlog documented
- Parts finder launched

### 60 Days
- 50% reduction in parts research time
- Zero "I think we have it" responses
- All RMAs tracked and followed up
- Customer self-service reducing calls by 20%

### 90 Days
- Full vendor integration
- Automated reordering for common items
- Complete inventory visibility
- 45 min → 10 min parts ordering time

---

## Alyssa's Specific Requests to Include

1. **Barcode everything** - "That would probably speed up the RMA process a lot"
2. **Link to PO numbers** - "We don't know which POs everything's from"
3. **Printer specs database** - Using her "Printer Info for Dummies" as foundation
4. **HP parts specialist** - Flag complex HP parts that need specialist help
5. **Delivery slip storage** - Digital archive of all delivery documents
6. **Vendor pestering automation** - "About five times a month I have to pester people"

---

## ROI from These Enhancements

### Time Savings
- **Parts research:** 30 min → 5 min = 25 min/order saved
- **Inventory checking:** 10 min → instant = 10 min/check saved
- **RMA processing:** 1.5 hrs → 30 min = 1 hr/RMA saved
- **Customer questions:** 5 min → self-service = 5 min/call saved

### Weekly Impact
- 2-3 parts orders × 25 min = 50-75 min saved
- 10 inventory checks × 10 min = 100 min saved
- 1 RMA × 60 min = 60 min saved
- 10 customer calls × 5 min = 50 min saved
- **Total: 4.3-5.1 hours/week saved**

### Annual Value
- 4.5 hrs/week average × 52 weeks = 234 hours
- 234 hours × $25/hr = **$5,850/year saved**
- Plus: Reduced stockouts, faster RMA credits, fewer errors

---

## Next Steps

1. Review enhancement priorities with team
2. Validate barcode scanner requirements
3. Get vendor API documentation
4. Import Alyssa's printer database
5. Design mobile app workflows
6. Plan phased rollout

---

*"The supplies portal exists - now we make it actually solve Alyssa's problems."*