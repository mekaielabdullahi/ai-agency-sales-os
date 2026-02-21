# Domain & Inbox Setup
## 3 Domains, 15 Inboxes, DNS Configuration

---

## Timeline

**Monday 2/16 Morning (8:00 - 10:15 AM)**

---

## Step 1: Buy 3 Domains (~$12 each)

| Domain | Registrar | Status |
|--------|-----------|--------|
| `arisegroupconsulting.com` | -- | [ ] Purchased |
| `getarisegroup.com` | -- | [ ] Purchased |
| `arisegroup.co` | -- | [ ] Purchased |

**Estimated cost:** ~$36 total

---

## Step 2: Create Google Workspace Inboxes

**5 inboxes per domain = 15 total**
**Cost:** $6/user/month = $90/month

### Domain 1: arisegroupconsulting.com
| Inbox | Status |
|-------|--------|
| mekaiel@arisegroupconsulting.com | [ ] Created |
| chris@arisegroupconsulting.com | [ ] Created |
| matt@arisegroupconsulting.com | [ ] Created |
| trent@arisegroupconsulting.com | [ ] Created |
| info@arisegroupconsulting.com | [ ] Created |

### Domain 2: getarisegroup.com
| Inbox | Status |
|-------|--------|
| mekaiel@getarisegroup.com | [ ] Created |
| chris@getarisegroup.com | [ ] Created |
| matt@getarisegroup.com | [ ] Created |
| trent@getarisegroup.com | [ ] Created |
| hello@getarisegroup.com | [ ] Created |

### Domain 3: arisegroup.co
| Inbox | Status |
|-------|--------|
| mekaiel@arisegroup.co | [ ] Created |
| chris@arisegroup.co | [ ] Created |
| matt@arisegroup.co | [ ] Created |
| trent@arisegroup.co | [ ] Created |
| team@arisegroup.co | [ ] Created |

---

## Step 3: DNS Configuration (Per Domain)

For each of the 3 domains, configure:

### SPF Record
```
Type: TXT
Host: @
Value: v=spf1 include:_spf.google.com ~all
```

### DKIM Record
- Generated in Google Workspace Admin > Apps > Google Workspace > Gmail > Authenticate email
- Copy the DKIM key and add as TXT record
```
Type: TXT
Host: google._domainkey
Value: [Generated DKIM key from Google Workspace]
```

### DMARC Record
```
Type: TXT
Host: _dmarc
Value: v=DMARC1; p=none; rua=mailto:dmarc-reports@[domain]
```

### Domain Verification Checklist

| Domain | SPF | DKIM | DMARC | Gmail Test |
|--------|-----|------|-------|------------|
| arisegroupconsulting.com | [ ] | [ ] | [ ] | [ ] |
| getarisegroup.com | [ ] | [ ] | [ ] | [ ] |
| arisegroup.co | [ ] | [ ] | [ ] | [ ] |

---

## Step 4: Verification

For each inbox, send a test email to your personal Gmail and verify:
- [ ] Lands in **Primary** inbox (not Promotions or Spam)
- [ ] SPF: PASS (check in Gmail "Show original")
- [ ] DKIM: PASS (check in Gmail "Show original")
- [ ] DMARC: PASS (check in Gmail "Show original")

---

## Step 5: Warmup Period

**14 days minimum before sending cold emails.**

Warmup starts: Monday 2/16
Warmup ends: Monday 3/2 (earliest cold send date from new inboxes)

During warmup:
- Inboxes email each other (automated via n8n)
- Open and reply to each other's emails
- Mark emails as important
- Move from spam to inbox if needed
- Gradually increase volume (5/day -> 10/day -> 20/day -> 30/day)

See `n8n-engine-spec.md` for Matthew's warmup workflow spec.

---

## Sending Limits

| Parameter | Limit |
|-----------|-------|
| Max emails per inbox per day | 30 |
| Max total emails per day (all 15 inboxes) | 450 |
| Pause inbox if bounce rate exceeds | 5% |
| Sending window | Tue-Thu, 9-11am local time |

---

## Monthly Cost Summary

| Item | Cost |
|------|------|
| 3 domains (annual) | ~$36/year ($3/month) |
| 15 Google Workspace accounts | $90/month |
| **Total** | **~$93/month** |
