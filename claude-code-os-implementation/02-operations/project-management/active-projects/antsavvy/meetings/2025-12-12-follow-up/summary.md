# Impromptu Google Meet Meeting - December 12, 2025

**Recording:** https://fathom.video/share/RZW5u6-xp8xyD2DvTG327oHyWYPrQZde
**Duration:** ~2 hours
**Attendees:** Matthew, Christian

---

## Meeting Purpose

Define an AI solution to fix Ant Savvy's event costing errors.

---

## Key Takeaways

- **The Problem:** Ant Savvy loses money on events by failing to include "hidden costs" (e.g., logistics, setup) in client budgets, a systemic issue driven by high-volume operations and inexperienced staff.
- **The Solution:** "Accounts Copilot," a Chrome extension that prompts staff with a checklist of hidden cost types during client calls. This avoids sensitive number-sharing while ensuring no cost category is missed.
- **The Blocker:** Development is blocked until Ant Savvy provides historical project data (line items and their associated hidden cost categories) to train the AI.
- **The Path Forward:** Christian will secure data, while Matthew researches the extension's technical feasibility, including handling "Tanglish" (Tagalog/English) audio.

---

## Topics

### The Problem: Leaking Money on Events

- Ant Savvy's accounts team consistently misses "hidden costs" when budgeting, causing the company to absorb the difference.
- **Example:** A $6,000 budget for an event with $1,250 in hidden costs results in a $250 loss if the client is charged $7,000 (a typical 1k profit margin).
- **Root Cause:** A lack of training and systems for inexperienced staff, who operate under extreme pressure (e.g., 50 events/day) and cut corners instead of consulting documentation.

### The Solution: Accounts Copilot

- **Initial Idea:** A RAG chatbot to provide real-time cost estimates.
- **Pivot Rationale:** The team pivoted from providing numbers to providing a checklist of cost types to overcome two key hurdles:
  1. **Data Sensitivity:** Ant Savvy is highly private about financial data.
  2. **Process Accuracy:** Many hidden costs are variable (e.g., travel distance) and require real quotes, which are not available during the initial client call.
- **Core Function:** A Chrome extension that prompts staff with a checklist of potential hidden costs for each event item discussed (e.g., for a "DJ Booth," prompt for "setup," "transport," "power").

### Development Roadmap & Data Needs

- **Data Required:** Historical project data, specifically:
  - Line items (e.g., "Speakers," "Retail Booth")
  - Associated hidden cost types (e.g., "Logistics," "Setup")
- **Data Strategy:**
  - **Primary:** Request as much recent data as possible.
  - **Fallback:** Use data from a recently closed production unit, as its operational structure is identical.
- **Technical Considerations:**
  - **Language:** The bot must handle "Tanglish" (Tagalog/English) audio. Matthew will test this capability.
  - **Platform:** A Chrome extension is preferred over a web widget for better user experience and training.

---

## Next Steps

### Christian:
- Secure historical project data from Ant Savvy (line items & hidden cost types).
- Obtain a "Tanglish" audio/transcript sample for testing.
- Contact Turtle to involve them in the project.

### Matthew:
- Research technical feasibility of a Chrome extension overlay.
- Test LLM performance on a "Tanglish" audio sample.

---

## Action Items

1. Ask Trissy for recent project data (hidden cost types, line items, regions); if declined, request production-house data
   - [WATCH (5 secs)](https://fathom.video/share/RZW5u6-xp8xyD2DvTG327oHyWYPrQZde?timestamp=5335.9999)

2. Explore Chrome extension vs overlay widget for Accounts Copilot
   - [WATCH (5 secs)](https://fathom.video/share/RZW5u6-xp8xyD2DvTG327oHyWYPrQZde?timestamp=7224.9999)
