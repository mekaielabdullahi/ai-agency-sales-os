# YouTube Learnings

**Purpose**: Capture insights from YouTube videos, interviews, and tutorials relevant to AI agency growth.

---

## Folder Structure

```
/youtube/
├── /raw-transcripts/     # Raw YouTube transcripts for processing
├── /processed/           # Processed insights (use capture template)
└── README.md
```

---

## Workflow

### 1. Capture Raw Transcript
Drop raw transcripts into `/raw-transcripts/` with naming:
```
YYYY-MM-DD-channel-name-video-title.md
```

### 2. Process Through OS
When processing a transcript, run it against:
- **Objectives**: Does this align with current agency goals?
- **Playbooks**: Should this update an existing playbook?
- **Gaps**: Does this fill a knowledge gap we have?
- **Actions**: What specific actions does this suggest?

### 3. Extract & Structure
Move actionable insights to `/processed/` using the capture template from `../README.md`

### 4. Integrate
Validated insights get promoted to `/agency-playbooks/` or update relevant sections of the OS.

---

## Processing Prompt Template

When asking Claude to process a transcript:

```
Review this YouTube transcript against my agency objectives and operating system.

1. What are the key insights relevant to AI agency sales/delivery?
2. Does this contradict or validate anything in my current playbooks?
3. What specific tactics should I test?
4. What updates (if any) should I make to my OS based on this?

Transcript:
[paste transcript]
```

---

## Priority Sources

| Channel | Focus | Why Follow |
|---------|-------|------------|
| *Add channels you follow* | - | - |

---

*YouTube is a goldmine of agency tactics. Systematically capture what works.*
