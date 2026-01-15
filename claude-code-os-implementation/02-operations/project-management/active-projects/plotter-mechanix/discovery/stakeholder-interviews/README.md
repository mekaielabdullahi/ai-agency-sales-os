# Stakeholder Interviews

Interview guides and notes for Plotter Mechanix team members.

## Interview Schedule

| Stakeholder | Role | Duration | Status | Key Focus |
|-------------|------|----------|--------|-----------|
| Nikki | Co-Owner / Bookkeeping | 30 min | Scheduled | Day-to-day workflow, Kelsey pain points, single phone number decision |
| Kelsey | Owner / Lead Tech | 45 min | Pending | Phone number strategy, call routing rules, Vonage 2FA access |
| Alyssa | Office Manager | 30 min | Pending | Time validation, call handling capability, Request queue workflow |
| Joe | Technician in Training | 20 min | Pending | Solo capability %, routing eligibility |

## Interview Files

- [nikki-interview.md](./nikki-interview.md) - Day-to-day, pain points with Kelsey's workflow, Kelsey's time
- [kelsey-interview.md](./kelsey-interview.md) - Phone number strategy, call routing design, Vonage access
- [alyssa-interview.md](./alyssa-interview.md) - Time validation, call handling, Request queue
- [joe-interview.md](./joe-interview.md) - Capability assessment, routing eligibility

## Critical Decisions Needed

### 1. Single Primary Business Number
Must choose ONE phone number as the primary business contact:
- Option A: Port Vonage number to Quo
- Option B: Get new Quo number, retire Vonage
- Option C: Use Kelsey's cell (not recommended - no separation)

**Who decides:** Kelsey + Nikki together

### 2. Call Routing Logic
Need to define rules for how calls route:
- New customer calls → ?
- Existing customer (active job) → ?
- After-hours → ?
- Emergency → ?
- Kelsey unavailable → Alyssa? Voicemail?

**Gather from:** Kelsey + Alyssa interviews

### 3. Vonage IVR Verification
- Have documented IVR from Dec 22 transcript
- Need to verify in Vonage admin (requires Kelsey's 2FA)
- Schedule separate session for Vonage walkthrough

## Data Already Gathered

- ✅ Phone provider account # and PIN for porting
- ✅ Vonage IVR menu options (5 options documented)
- ✅ Jobber cost ($379/month)
- ✅ Quo cost ($69/month base)

## Data Collection Summary

See [stakeholder-questions-roi.md](../stakeholder-questions-roi.md) for the master tracking document.

---

**Created:** January 6, 2026
**Last Updated:** January 6, 2026
