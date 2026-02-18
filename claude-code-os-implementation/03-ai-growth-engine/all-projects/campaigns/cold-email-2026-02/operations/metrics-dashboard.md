# Metrics Dashboard
## Tracking Framework + Red Flags

---

## Weekly Metrics Review (Every Monday 8 AM)

| Metric | Red Flag | Acceptable | Golden Zone |
|--------|----------|------------|-------------|
| Bounce Rate | >5% | 2-5% | <2% |
| Open Rate | <20% | 20-35% | 35%+ |
| Reply Rate | <2% | 2-5% | 5-10% |
| Positive Reply % | <40% of replies | 40-50% | 50%+ |

---

## Diagnostic Tree

### Open Rate < 20%
**Cause:** Subject lines aren't compelling OR emails landing in spam.

**Fix:**
1. Test subject lines with personal Gmail first
2. Check spam placement (send test from each inbox to Gmail, check "Show original")
3. If spam: Review DNS records, check if inbox is blacklisted
4. If not spam: A/B test new subject lines (see email sequence files)
5. Try different send times (shift by 1-2 hours)

### Reply Rate < 2%
**Cause:** Bad list OR deliverability issues.

**Fix:**
1. Check bounce rate first -- if bounces are high, list quality is the issue
2. Re-verify emails through Hunter.io or similar
3. Check if emails are landing in spam (test with personal Gmail)
4. Review the email copy -- is the offer clear? Is the CTA simple?
5. Review the ICP -- are you targeting the right companies?

### Reply Rate 2-5% but < 40% Positive
**Cause:** Copy/offer doesn't resonate. Reaching the right people but wrong message.

**Fix:**
1. **Printing:** Strengthen proof (add more specific Kelsey/Plotter Mechanix metrics)
2. Review negative replies for patterns -- what objections keep coming up?
3. A/B test offer framing

### Reply Rate 5-10%
**Status:** Golden zone. Optimize conversion to calls.

**Action:**
1. Focus on response speed (<1 hour)
2. Optimize discovery call booking rate
3. Consider scaling send volume
4. Document what's working for consistency

---

## A/B Testing Schedule

### Week 3: Subject Line Variants
| Test | Variant A | Variant B |
|------|-----------|-----------|
| Printing | Curiosity: `quick q about [Company]'s service ops` | Benefit: `saw [Company] services [HP/Canon] -- had a thought` |

**How to test:** Split lead list 50/50. Run for 1 week. Compare open rates.

### Week 4: Offer Framing
| Test | Variant A | Variant B |
|------|-----------|-----------|
| Printing | "free automation" | "free audit" |

**How to test:** Split lead list 50/50. Run for 1 week. Compare reply rates and positive reply %.

---

## ICP Refinement Tracking

After every positive reply, log in the ICP Refinement tab:

| Field | Purpose |
|-------|---------|
| Company | Who responded |
| Sub-niche | Specific type within vertical |
| Size (employees) | Pattern detection |
| Revenue (est.) | Pattern detection |
| Responder Title | Who's reading the emails |
| Pain Point (their words) | Exact language to use in future copy |
| Outcome | Call booked, proposal sent, closed, etc. |

**After 25 positive replies:** Analyze patterns and double down on the highest-converting sub-niche, size, and pain point.

---

## Scale Triggers

Add 3 more domains when ALL of these are true:
- [ ] Warmup period > 30 days
- [ ] Open rate > 30%
- [ ] Reply rate > 3%
- [ ] Bounce rate < 3%
- [ ] You can handle the reply volume (not a bottleneck)

---

## Dashboard Layout (Google Sheet Tab 1)

### Section 1: Overview
```
Total Leads: ___    Emails Sent (all time): ___    This Week: ___
Printing Leads: ___
```

### Section 2: Deliverability
```
Bounce Rate: ___% (Target: <2%)
Open Rate: ___% (Target: 30%+)
Active Inboxes: ___ / 15
Paused Inboxes: ___
```

### Section 3: Engagement
```
Reply Rate: ___% (Target: 5-10%)
Positive Replies: ___ (___%)
Neutral Replies: ___ (___%)
Negative Replies: ___ (___%)
```

### Section 4: Pipeline
```
Discovery Calls Booked: ___
Calls Completed: ___
Proposals Sent: ___
Deals Closed: ___
Revenue: $___
```

### Section 5: Per Inbox Health
```
[Table showing each inbox's: sends today, sends this week, bounce rate, status]
```
