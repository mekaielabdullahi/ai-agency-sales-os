# December 9, 2025 - Invoice Automation Debug Session (Fathom Summary)

**Date:** December 9, 2025
**Type:** Google Meet Debug Session
**Recording:** [View Recording](https://fathom.video/share/qgxzxQA7UufN2XUBykxyUVGPS2nzMMhn)
**Purpose:** Review and debug the invoice automation system
**Participants:** Matt, Linh (Ascension Capital)

> **⚠️ NOTE:** The Fathom transcript may have incorrect participant names (Vince Le, Liam's Partner). This was Matt and Linh reviewing the Ascension Capital invoice automation POC.

---

## 🔴 Critical Status: System Currently Unusable

The automation is **SLOWER than manual process** due to required verification of all results.

---

## Key Issues Identified

### System Usability & Performance
- **Problem:** Automation requires manual verification, making it slower than original process
- **Root Cause:** Low accuracy rate forces double-checking, eliminating time savings
- **Target:** Need ~98% accuracy to build trust and enable high-level verification only

### Critical Bugs Found

| Invoice # | Issue | Impact |
|-----------|--------|---------|
| **1134** | Picture of receipt not processed properly | OCR failure on photo |
| **1170** | [To confirm] Receipt 2 should be minus (refund) | Need to handle negative totals for refunds |
| **1173** | Missed tax extraction | Off by $25 - Receipt was $291.14, missed $25.47 in tax |
| **1174** | Failed to process entirely | Complete failure |

### Required Feature: Per-Receipt Breakdown
- **Need:** Per-receipt breakdown in analysis email for efficient auditing
- **Format:** Display each receipt's total (e.g., "Receipt 1 Total: $X.XX")
- **Location:** After main breakdown in email

### Technical Blockers
- **Credential Expirations:** Recurring system/user credential expirations halting automation
- **Process Flaw:** Insufficient testing before deployment

---

## Action Items

### For Matt/Vince:
1. ✅ Add numbered per-receipt totals to analysis email
2. ✅ Fix credential expiration - implement long-term solution
3. ✅ Fix OCR for photo receipts
4. ✅ Fix refund detection logic for negative totals
5. ✅ Fix tax calculation logic (Invoice 1173)
6. ✅ Ensure latest invoice instance is processed
7. ✅ Run automation on ALL "Walnut" invoices (July 10, 2025 → present)
8. ✅ Then run "Woodbury" invoices
9. ✅ Delete payment reminder emails from processing queue

### For Linh/Liam's Partner:
1. Email Daniel Shahada (CC Liam) for clarification on "Daniel" bid
2. Audit portable toilet invoices - confirm monthly charges and gaps

---

## Next Steps

### Immediate Fixes Needed:
1. **Per-receipt breakdown** - Essential for auditing
2. **Refund logic** - Must subtract negative totals
3. **OCR improvement** - Photo receipts failing
4. **Tax calculation** - Incorrect inclusion in totals
5. **Credential management** - Long-term solution needed

### Testing Plan:
1. Run on ALL Walnut invoices (Jul 10, 2025 → present)
2. Comprehensive test before next review
3. Then process Woodbury invoices

---

## Impact Analysis

### Current State:
- ❌ System unusable in production
- ❌ Slower than manual process
- ❌ Multiple critical bugs
- ❌ Missing essential features

### Required for Production:
- ✅ 98% accuracy minimum
- ✅ Per-receipt breakdown
- ✅ All bugs fixed
- ✅ Credential stability
- ✅ Comprehensive testing complete

---

## Technical Details

### Failed Invoices (Corrected Details):
- **Invoice 1134:** Picture of receipt not processed properly (OCR failure)
- **Invoice 1170:** [To confirm] Receipt 2 should be minus - refund handling needed
- **Invoice 1173:** Tax extraction error - Off by $25 (Receipt $291.14, missed $25.47 tax)
- **Invoice 1174:** Complete processing failure

### System Requirements:
- Stable credential management system
- Improved OCR for photo/image receipts
- Proper negative value handling
- Accurate tax extraction and calculation
- Per-receipt reporting in emails

---

## Meeting Timestamps

Key moments from recording:
- [1:37:7.9999](https://fathom.video/share/qgxzxQA7UufN2XUBykxyUVGPS2nzMMhn?timestamp=1377.9999) - Per-receipt totals discussion
- [2:15:6.9999](https://fathom.video/share/qgxzxQA7UufN2XUBykxyUVGPS2nzMMhn?timestamp=2156.9999) - Credential expiration issue
- [3:36:4.9999](https://fathom.video/share/qgxzxQA7UufN2XUBykxyUVGPS2nzMMhn?timestamp=3364.9999) - Portable toilet invoice audit
- [5:13:6.9999](https://fathom.video/share/qgxzxQA7UufN2XUBykxyUVGPS2nzMMhn?timestamp=5136.9999) - OCR photo receipt fix
- [6:51:4.9999](https://fathom.video/share/qgxzxQA7UufN2XUBykxyUVGPS2nzMMhn?timestamp=6514.9999) - Total extraction fix

---

## Conclusion

**Project Status:** 🔴 BLOCKED - System not production-ready

The automation is currently **worse than manual processing** due to accuracy issues and missing features. All critical bugs must be fixed and the per-receipt breakdown feature added before the system can provide value.

**Priority Actions:**
1. Fix all identified bugs
2. Add per-receipt breakdown
3. Solve credential expiration
4. Run comprehensive testing on ALL invoices
5. Achieve 98% accuracy before next review

---

*Note: This appears to be a different invoice automation project from the Ascension Capital POC, possibly for a different client (references to Walnut, Woodbury, portable toilets suggest construction/service industry)*