# Plotter Mechanix - Development Plan

**Created:** December 26, 2025
**Status:** Active Development
**Objective:** Optimize Plotter Mechanix workflow with Quo and Jobber integration

---

## Executive Summary

Deliver an **optimized workflow** where AI tools in Jobber and Quo are fully utilized. We work backwards from the final state, starting with data ingestion and workflow analysis before making changes.

**Critical Principle:** We do NOT update their live systems. All data is pulled into our separate database for analysis and testing.

---

## Technical Stack

| Component | Service | Status | Details |
|-----------|---------|--------|---------|
| Field Service | [Jobber](../integrations/JOBBER.md) | Production Ready | GraphQL API, OAuth2, 17 webhook events |
| Communications | [Quo](../integrations/QUO.md) | Core Complete | REST API, 7 webhook events, AI transcription |
| Orchestration | n8n | Ready | Custom nodes published |

See [Integration Specs](../integrations/README.md) for full technical documentation.

---

## Phase 0: Foundation (Current Priority)

### 0.1 Jobber Data Ingestion
**Objective:** Pull all historical data into isolated database

- [ ] Set up secure database
- [ ] Configure OAuth2 connection
- [ ] Pull historical data (jobs, clients, invoices, etc.)
- [ ] Implement incremental sync via webhooks
- [ ] Build backup system

**Database Architecture:**
```
plotter-mechanix-data/
├── raw/           # Exact copy of Jobber data
├── processed/     # Cleaned and normalized
├── analysis/      # Workflow insights
└── backups/       # Point-in-time snapshots
```

### 0.2 Quo Number Porting (CRITICAL PATH)

**⚠️ 5-30 day delay** - Must plan carefully.

**Pre-Port Checklist:**
- [ ] Quo account configured
- [ ] IVR/menu system tested
- [ ] Call routing rules defined
- [ ] Team trained
- [ ] Rollback plan documented

```
Day 0: Initiate port request
Day 5-30: Port completes (unpredictable)
Day X: All calls route through Quo
```

### 0.3 Integration Testing
- [ ] Verify Jobber node with client account
- [ ] Test Quo webhooks with test numbers
- [ ] Validate end-to-end workflow

---

## Phase 1: Workflow Analysis

### 1.1 Data Analysis
Once data is ingested, analyze:
- **Who** makes updates (Kelce vs Alyssa vs Joe)
- **How** updates are made (manual vs automated)
- **When** activity peaks occur
- **What** workflows are bottlenecks

### 1.2 Deliverables
- [ ] Current state workflow diagram
- [ ] Pain point inventory
- [ ] Bottleneck analysis
- [ ] Manual process list

---

## Phase 2: Business Analysis

### 2.1 BA Agent Integration
Feed to Business Analyst agent:
- Discovery call transcripts (Dec 3, 17, 22, 23)
- Workflow analysis from Phase 1
- Quo/Jobber capability matrix

### 2.2 PRD Development
- Current vs future state documentation
- Gap analysis (build vs configure)
- Implementation roadmap
- ROI projections

---

## Phase 3: Integration Workflows

### 3.1 Priority Workflows

| Workflow | Trigger | Action | Status |
|----------|---------|--------|--------|
| **Voice-to-Ticket** | Quo call → transcription | AI extract → Jobber job | Phase 1 |
| **Customer Status Bot** | Quo SMS "where's my tech?" | Jobber lookup → Quo reply | Phase 1 |
| **Data Sync** | Scheduled + webhooks | Jobber → Database | Phase 0 |
| **Communication Hub** | All Quo events | Log to dashboard | Phase 1 |

### 3.2 n8n Setup
- [ ] Deploy n8n instance
- [ ] Install custom nodes
- [ ] Configure database connectors
- [ ] Build backup workflows

```bash
npm install @arisegroup/n8n-nodes-jobber
npm install @arisegroup/n8n-nodes-quo
```

---

## Phase 4: Value Delivery

**Final State Goals:**
- AI tools fully utilized in both platforms
- Reduced manual work
- Kelce freed up 10+ hrs/week
- Joe handling 25%+ of calls
- Real-time visibility dashboard

---

## Architecture Overview

```
┌──────────────┐     ┌──────────────┐
│    JOBBER    │     │     QUO      │
│ (Field Svc)  │     │   (Comms)    │
└──────┬───────┘     └──────┬───────┘
       │ GraphQL            │ REST
       │ 17 webhooks        │ 7 webhooks
       ▼                    ▼
┌─────────────────────────────────────┐
│           N8N WORKFLOWS             │
│                                     │
│  n8n-nodes-jobber   n8n-nodes-quo  │
│  v0.1.1 ✓           v0.1.0 ✓       │
└─────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│     DATABASE (Safe Copy)            │
│  raw → processed → analysis         │
└─────────────────────────────────────┘
```

---

## Immediate Next Steps

### This Week
1. [ ] Jobber API connection + test data pull
2. [ ] Research Quo porting process
3. [ ] Design IVR menu system
4. [ ] Set up database infrastructure

### Next Week
1. [ ] Complete Jobber data ingestion
2. [ ] Begin workflow analysis
3. [ ] Prepare BA agent data package
4. [ ] Create porting readiness checklist

---

## Success Metrics

| Phase | Criteria |
|-------|----------|
| **Phase 0** | Data ingested, backups working, sync operational |
| **Phase 1** | Workflow mapped, pain points documented |
| **Phase 2** | PRD approved, roadmap finalized |
| **Final** | 10+ hrs/week saved, workflows automated |

---

## Key Principles

1. **Data Safety First** - Never modify client's live systems
2. **Understand Before Optimize** - Analyze before changing
3. **Validate Before Building** - Use BA agent to confirm approach
4. **Incremental Delivery** - Phase by phase, not big bang
5. **AI-First** - Leverage native AI before custom builds

---

## Related Documents

### Planning
- [Phase 1 Proposal](../phase-1-proposal.md) - Client deliverables
- [Roadmap](../roadmap/README.md) - Full transformation timeline

### Technical Specifications
- [Integration Overview](../integrations/README.md)
- [Jobber Integration](../integrations/JOBBER.md) - API, webhooks, n8n node
- [Quo Integration](../integrations/QUO.md) - API, webhooks, n8n node

### Repositories
| Repository | Location | Status |
|------------|----------|--------|
| n8n-nodes-jobber | `/workspace/n8n-nodes/n8n-nodes-jobber` | Production Ready |
| n8n-nodes-quo | `/workspace/n8n-nodes/n8n-nodes-quo` | Core Complete |

---

*Last Updated: December 26, 2025*
