# Summary: Plotter Mechanix Phase 1 Quo to Jobber Integration Handoff Call

**Meeting Date:** 2026-01-23

## Meeting Purpose

Review the new Quo-to-Jobber integration and decide on deployment.

## Key Takeaways

- **New Integration Approved:** Kelsey approved deploying the custom N8N integration to Jobber this weekend for live testing, replacing the native Quo integration.
- **Rollback Plan Defined:** A clear, manual rollback process was established to revert to the native integration if issues arise, mitigating risk to Jobber data.
- **Contact Logic Prioritizes Jobber:** The integration prioritizes existing Jobber contacts by phone number and only creates new ones if no match is found, preventing data corruption.
- **SOP for User Feedback:** A simple SOP will be created for Alyssa to flag AI errors in Jobber, providing a direct feedback loop to refine the system.

## Topics

### New Quo-to-Jobber Integration

Trent demoed the new N8N-powered integration, which creates Jobber requests from Quo calls with richer, AI-extracted data.

**Key Features:**
- **AI Summaries:** Extracts caller name, equipment, issues, and next steps.
- **Dynamic Notes:** Appends new call summaries to existing requests, with the newest at the top.
- **Transcript Links:** Replaces full transcripts with Quo deep links to prevent clutter, especially on mobile.
- **Call Tags:** Automatically categorizes calls (e.g., "service," "supplies") or leaves them untagged if indeterminate.

### Contact Handling Logic

The system uses a multi-source hierarchy to ensure contact accuracy:

1. **Jobber:** Highest priority; existing Jobber contacts are used if a phone number matches.
2. **Quo:** Used if no Jobber match; pulls contact details from Quo's internal storage.
3. **Conversation:** Last resort; creates a new contact from names and info dictated during the call.

**Safety Measures:**
- **Fuzzy Matching:** Prevents duplicate contacts from minor transcript errors (e.g., "REID" vs. "R-E-I-D").
- **No Overwriting:** The system does not modify existing Jobber contact data, only adds new emails/phones or fills in placeholder names.

### Deployment & Rollback Plan

**Decision:** Deploy the integration this weekend for live testing.

**Rollback Procedure:**
1. **Disconnect N8N:** In Jobber, go to `Settings` → `Arise Testing` → `Disconnect`.
2. **Reconnect Native Quo:** In Jobber, go to `Apps` → `Quo` → `Connect`.

**Environment Strategy:**
- **Production:** A dedicated, stable N8N instance is required for the final rollout.
- **Development:** Individual sandboxes (TCN8N, MK) will be used for testing new features.
- **Licensing:** n8n requires the client to own the infrastructure for production use.

### User Feedback & SOPs

- **Initial Verification:** Alyssa must manually verify AI-generated data to build trust.
- **Feedback Mechanism:** A simple SOP will be created for Alyssa to flag AI errors in Jobber (e.g., by adding a `*` to a request name) for team review.
- **Call Quality:** Kelsey confirmed Quo's A2P registration is still pending, which is currently impacting his ability to text customers.
