# Product Requirements Document (PRD)
# PlotterOps Phase 1: Communication Control System

**Project:** Plotter Mechanix Quick Win Sprint
**Version:** 1.1
**Date:** January 10, 2026
**Author:** AriseGroup.ai
**Status:** Active Development
**Updated in OS:** January 11, 2026

---

## 1. Executive Summary

### 1.1 Overview

PlotterOps Phase 1 is a communication control system that transforms Jobber into the trusted single source of truth for Plotter Mechanix. By automating the capture of all customer communications (calls, texts, emails), we eliminate the manual handoff processes that cause delays, information loss, and trust erosion.

### 1.2 Problem Statement

Plotter Mechanix, a $600K-$750K/year printer service company, suffers from critical communication chaos:

- **Trust Gap:** "My first instinct is not to go to Jobber... I don't fully trust that everything is in there"
- **Screenshot Bombing:** Text messages sent as screenshots, creating hours of delay
- **Phone Tag:** 4-6 daily handoff calls between Kelsey and Alyssa
- **Email Chaos:** 206 unread messages across 4 inboxes
- **Phone Number Confusion:** Customers confused by multiple business numbers

**The root cause:** Manual steps between customer contact and Jobber create lag time, errors, and trust erosion.

### 1.3 Key Use Cases

The problems above manifest in three specific communication use cases:

| Use Case | Current Process | Pain Points | Impact |
|----------|----------------|-------------|--------|
| **UC-1: Client Updates (Kelsey → Alyssa)** | Kelsey takes client call → Calls Alyssa to relay info → Alyssa manually enters into Jobber | Manual, synchronous, info can get lost, delays to update Jobber | 4-6 phone calls/day, hours of lag, trust erosion |
| **UC-2: Initial Client Calls to Kelsey** | New/existing client calls Kelsey → Kelsey takes notes (or doesn't) → Info eventually gets to Jobber (maybe) | Details need to be input into Jobber, can take time, info can get lost | Lost leads, incomplete records, ~$10K/year lost revenue |
| **UC-3: Follow-up Client Calls to Kelsey** | Client calls back about existing job → Kelsey discusses → Updates scattered across texts/notes | Details need to be input into Jobber, can take time, info can get lost | Incomplete job history, can't trust Jobber, rework |

### ⚠️ SCOPE CONSIDERATION: Multiple Phone Numbers

We may end up with multiple phone numbers for Phase 1:

1. Kelsey's Quo phone number for incoming client calls
2. A voicemail-only phone number for async updates from Kelsey that get auto-transcribed (free with Quo) + processed into a Jobber Request
3. Potentially Quo phone numbers for Alyssa (and Nikki? - maybe not if she doesn't take client calls)

**Question for Quick Win Sprint:** Is building the voicemail-only async update number the highest priority? It adds an extra layer of effort. If it's not the highest ROI item, we may defer to a later phase.

**Decision Needed:** Confirm scope with client before Week 2 build.

### 1.4 Solution Summary

Implement a unified communication system using:

1. **Quo** - Single business phone number with auto-sync to Jobber (addresses UC-1, UC-2, UC-3)
2. **Email Automation** - N8N workflow to create Jobber Requests from emails
3. **Communication Protocols** - Standardized rules to maintain data integrity

| Use Case | How Solution Addresses It |
|----------|--------------------------|
| **UC-1: Client Updates** | Kelsey's calls auto-transcribed → Summary synced to Jobber client record → Alyssa sees it without phone call |
| **UC-2: Initial Client Calls** | Unknown callers auto-create Jobber Request with call transcript → No manual entry needed |
| **UC-3: Follow-up Calls** | Call summary attached to existing client record → Full history in Jobber → Trust restored |

### 1.5 Success Criteria

| Metric | Current State | Target |
|--------|---------------|--------|
| Communication in Jobber | Manual, delayed | 90%+ auto-captured within 5 min |
| Screenshot handoffs | Daily bombardment | Eliminated (0/week) |
| Phone call handoffs | 4-6/day | 1-2/day max |
| Email inbox unread | 206 | <20 |
| Alyssa manual entry | 1.5+ hrs/day | <30 min/day |

**Primary Success Test:** Kelsey checks Jobber first thing and trusts it has everything.

---

## 2. Background & Context

### 2.1 Client Profile

| Attribute | Value |
|-----------|-------|
| Company | Plotter Mechanix |
| Owner | Kelsey Andrade |
| Location | Phoenix, AZ Metro Area |
| Industry | Large Format Printer Service & Repair |
| Annual Revenue | $600,000 - $750,000 |
| Team Size | 3 employees + 1 technical consultant |
| Lead Source | Chris (AriseGroup partner) |

### 2.2 Team Structure

| Name | Role | Responsibilities |
|------|------|------------------|
| Kelsey | Owner/Lead Tech | ALL technical work, customer calls |
| Alyssa | Office Manager | Scheduling, invoicing, data entry |
| Joe | Tech in Training | Learning field work, social media |
| Mike | Consultant | Systems engineering, IT advisory |

### 2.3 Strategic Context

- **First project from Chris** - high-value partner with many leads
- **Previous failure:** $7,000 paid to Malik for failed API integration
- **Change fatigue:** Client needs to SEE results, not hear promises
- **Phase 2 opportunity:** $15K-$30K inventory/operations system

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-28 | AriseGroup.ai | Initial PRD created from project documentation |
| 1.1 | 2026-01-10 | AriseGroup.ai | Restructured Section 1: Added Key Use Cases (1.3), moved Solution Summary after Use Cases, added Scope Consideration callout for multiple phone numbers |

**Document Owner:** AriseGroup.ai
**Last Updated:** January 10, 2026
**Added to OS:** January 11, 2026
**Next Review:** End of Week 1 Testing

*This PRD is a living document. Requirements will be refined based on Week 1 testing results and ongoing discovery.*
