# Summary: Idea Brand Coach Update + AutoClaude Onboarding Tour Demo

**Meeting Date:** 2026-01-23

## Meeting Purpose

Review recent app updates and align on the path to beta launch.

## Key Takeaways

- **New "Field Chat" Feature:** A new inline chat allows users to refine specific fields (e.g., avatar name) with natural language and update them directly, eliminating copy-pasting.
- **Critical Beta Feedback Bug:** Feedback from the 100+ beta signups is not being saved to the database. The public beta is now unpublished to prevent further data loss.
- **AI Knowledge Base Disconnected:** The app is not using the system-wide knowledge base, which contains Trevor's book PDF. Connecting it is the top priority to improve AI output quality.
- **New Onboarding Tour:** An interactive product tour was built live using the AI coding tool "AutoClaude," demonstrating a new, highly efficient development workflow.

## Topics

### Beta Program Status

**Problem:** Feedback from the 100+ beta signups is not being saved to the database.
- **Cause:** Feedback is stored only in browser local storage, a legacy behavior.
- **Impact:** All feedback from the public beta is lost.

**Resolution:** The public beta is now unpublished. Matthew will fix the database persistence bug.

### AI Knowledge Base & Output Quality

**Problem:** AI output quality is inconsistent.

**Cause:** The app is not using the "IDEA System Knowledge Base" vector store, which contains Trevor's book PDF.
- **Current Sources:** Per-user vector store, semantic context, and user-uploaded documents.

**Resolution:** Matthew will connect the system knowledge base. Trevor will then upload additional PDFs to enrich the AI's context.

### "Field Chat" Feature

**Goal:** Replace the clunky "Generate with AI" button with a seamless, conversational workflow.

**New Flow:**
1. User clicks a "Field Chat" button on any field.
2. An inline chat window opens.
3. User refines the field's content with natural language.
4. AI provides concise suggestions (e.g., "The Sage of Strategy").
5. User clicks "Update [Field Name]" to apply the text directly.

**Known Bugs:**
- Chat context persists between fields.
- The AI doesn't always pull the latest data from other fields.

### Interactive Onboarding Tour

**Goal:** Provide a more engaging onboarding experience than simple video tutorials.

**Tool:** "AutoClaude," an AI coding tool, built the tour live during the meeting.

**Functionality:** The tour highlights key features (e.g., Brand Diagnostic, Avatar Builder) with animated overlays and explanatory text.

**Status:** The tour is functional but currently requires the user to be on the Dashboard page to activate.

### Project Acceleration & Budget

**Context:** Matthew's work on this project is deprioritized by higher-paying hourly work.

**Agreement:** To accelerate progress, Trevor will pay Matthew $50/hour.
- **Initial Budget:** Up to 3 hours to resolve critical beta blockers.

**New Workflow:** Trevor will provide detailed feedback (e.g., video walkthroughs) for Matthew to feed to AutoClaude, enabling faster iteration.
