# Ascension Capital - Critical Action Items

**Generated From:** December 9, 2025 Debug Session
**Priority:** 🔴 CRITICAL - System Currently Unusable
**Target:** Achieve 98% accuracy to make system faster than manual

---

## Immediate Bug Fixes Required

### 1. Fix OCR for Photo Receipts
**Invoice:** 1134
**Issue:** Picture of receipt not processed properly
**Impact:** Core functionality broken for photo receipts
**Solution:**
- Enhance OCR preprocessing for photo images
- Add image quality enhancement before OCR
- Test with multiple photo receipt samples

### 2. Fix Refund Detection Logic
**Invoice:** 1170
**Issue:** Receipt 2 should be minus (refund) but processed as positive
**Impact:** Financial totals incorrect
**Solution:**
- Implement negative total detection
- Add refund keyword detection
- Handle parentheses and minus signs in amounts

### 3. Fix Tax Extraction Errors
**Invoice:** 1173
**Issue:** Off by $25 - Receipt was $291.14, missed $25.47 in tax
**Impact:** Tax calculations wrong
**Solution:**
- Fix tax line item detection
- Ensure all tax amounts are captured
- Validate tax calculations against totals

### 4. Debug Complete Processing Failures
**Invoice:** 1174
**Issue:** Complete failure to process
**Impact:** Some invoices not processing at all
**Solution:**
- Add comprehensive error logging
- Implement fallback processing
- Identify root cause of failures

---

## Required Features

### 5. Add Per-Receipt Breakdown
**Need:** Per-receipt totals in analysis email
**Format:**
```
Receipt 1 Total: $X.XX
Receipt 2 Total: $Y.YY
Receipt 3 Total: $Z.ZZ
```
**Location:** After main breakdown in email
**Purpose:** Essential for efficient auditing

### 6. Fix Credential Expiration
**Issue:** Recurring credential expirations halting automation
**Current:** Manual intervention required frequently
**Solution:**
- Implement long-term credential solution
- Add automatic renewal mechanism
- Monitor and alert before expiration

---

## Testing Requirements

### 7. Comprehensive Invoice Testing
**Scope:** ALL Walnut invoices (July 10, 2025 → present)
**Process:**
1. Run automation on all historical invoices
2. Compare results with manual processing
3. Document accuracy rates
4. Fix any new issues found

### 8. Process Woodbury Invoices
**When:** After Walnut testing complete
**Scope:** All Woodbury invoices
**Purpose:** Validate fixes work across different invoice types

### 9. Delete Payment Reminders
**Task:** Remove payment reminder emails from processing queue
**Why:** These are not invoices and cause processing errors

---

## Success Metrics

### Target Accuracy
- **Current:** < 80% (unusable)
- **Required:** 98% minimum
- **Goal:** 99%+ for production

### Processing Speed
- **Current:** SLOWER than manual (due to verification needs)
- **Target:** 90% faster than manual
- **Metric:** < 30 seconds per invoice with no manual verification

### Reliability
- **Uptime:** 99.9%
- **Error Rate:** < 2%
- **Credential Issues:** Zero

---

## Timeline

### Week 1 (This Week)
- [ ] Fix all critical bugs (1-4)
- [ ] Add per-receipt breakdown (5)
- [ ] Fix credential issues (6)
- [ ] Begin comprehensive testing (7)

### Week 2
- [ ] Complete Walnut testing
- [ ] Process Woodbury invoices
- [ ] Achieve 98% accuracy
- [ ] Production deployment

### Week 3
- [ ] Client training
- [ ] Monitor production
- [ ] POC sign-off
- [ ] Phase 2 discovery discussion

---

## Developer Tasks

### Backend Fixes
```python
# Priority 1: Fix OCR for photos
- enhance_image_quality()
- preprocess_photo_receipts()
- add_ocr_confidence_scoring()

# Priority 2: Fix refund detection
- detect_negative_amounts()
- identify_refund_keywords()
- handle_parentheses_in_amounts()

# Priority 3: Fix tax extraction
- improve_tax_line_detection()
- validate_tax_calculations()
- cross_check_with_totals()
```

### Frontend Updates
```typescript
// Add per-receipt breakdown display
- ShowReceiptBreakdown component
- Email template updates
- Audit trail enhancements
```

### Infrastructure
```yaml
# Credential management
- Implement OAuth refresh tokens
- Add credential monitoring
- Set up expiration alerts
```

---

## Communication

### For Linh
- System currently being fixed
- Will achieve 98% accuracy before next review
- Comprehensive testing in progress
- Production deployment delayed until fixes complete

### Internal Team
- All hands on fixing critical bugs
- No new features until accuracy achieved
- Daily progress updates required

---

## Definition of Done

✅ All invoices process successfully
✅ 98% accuracy achieved consistently
✅ Per-receipt breakdown working
✅ No credential expiration issues
✅ Comprehensive testing complete
✅ Client can use without manual verification
✅ System faster than manual process

---

*Critical: Do not proceed to production until ALL items are complete and tested.*