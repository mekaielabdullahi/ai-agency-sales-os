#!/usr/bin/env python3
"""
Compress a transcript into structured knowledge base markdown using Claude.

Reads a transcript (and optional metadata), sends it to Claude Sonnet for
summarization, and outputs a structured markdown file to the knowledge base.

Usage:
    ./run modules/youtube-kb/tool/compress_to_kb.py ".tmp/youtube-kb/ABC123/transcript.txt"
    ./run modules/youtube-kb/tool/compress_to_kb.py transcript.txt --metadata metadata.json
    ./run modules/youtube-kb/tool/compress_to_kb.py transcript.txt --output custom_output.md

Output:
    knowledge-base/youtube/{channel_slug}/{date}_{video_slug}.md
    Prints the output path to stdout.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

# Provider detection: prefer ANTHROPIC, fall back to OPENAI
def _get_provider():
    """Determine which LLM provider to use based on available API keys."""
    provider = os.getenv("KB_LLM_PROVIDER", "").lower()
    anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")
    openai_key = os.getenv("OPENAI_API_KEY", "")

    # Treat placeholder values as missing
    if anthropic_key in ("", "sk-ant-xxx"):
        anthropic_key = ""
    if openai_key in ("", "sk-xxx"):
        openai_key = ""

    if provider == "openai" and openai_key:
        return "openai"
    if provider == "anthropic" and anthropic_key:
        return "anthropic"

    # Auto-detect: try anthropic first, then openai
    if anthropic_key:
        return "anthropic"
    if openai_key:
        return "openai"

    return None

KB_BASE = Path("knowledge-base/youtube")

SYSTEM_PROMPT = """You are a knowledge extraction specialist. Your job is to compress a video transcript into a structured, searchable knowledge base entry.

Rules:
- Be concise but preserve all important information
- Use clear, scannable structure with headers
- Extract direct quotes that are particularly insightful
- Identify actionable takeaways
- Do NOT invent information not present in the transcript
- Write in third person unless quoting directly"""

USER_PROMPT_TEMPLATE = """Compress the following video transcript into a structured knowledge base entry in markdown format.

{metadata_section}

Use this exact structure:

```
---
source: {url}
channel: {channel}
title: {title}
date: {date}
duration: {duration}
extracted: {extracted}
---

## Executive Summary

[2-3 sentence overview of the video's core message and value]

## Key Topics

- [Topic 1]
- [Topic 2]
- [Topic 3]
- ...

## Detailed Notes

### [Topic 1 Title]

[Detailed notes on this topic - key points, explanations, examples mentioned]

### [Topic 2 Title]

[Continue for each major topic...]

## Key Quotes

> "[Notable quote from the video]"

> "[Another key quote]"

## Action Items / Takeaways

- [ ] [Actionable takeaway 1]
- [ ] [Actionable takeaway 2]
- ...
```

IMPORTANT: Output ONLY the markdown content. No commentary before or after.

---

TRANSCRIPT:

{transcript}"""


def slugify(text):
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:80].rstrip('-')


def chunk_transcript(transcript, max_chars=150000):
    """Split transcript into chunks for very long videos (4+ hours)."""
    if len(transcript) <= max_chars:
        return [transcript]

    chunks = []
    lines = transcript.split('\n')
    current_chunk = []
    current_size = 0

    for line in lines:
        line_size = len(line) + 1
        if current_size + line_size > max_chars and current_chunk:
            chunks.append('\n'.join(current_chunk))
            current_chunk = []
            current_size = 0
        current_chunk.append(line)
        current_size += line_size

    if current_chunk:
        chunks.append('\n'.join(current_chunk))

    return chunks


def _build_user_prompt(transcript_chunk, metadata, chunk_num=None, total_chunks=None):
    """Build the user prompt for a transcript chunk."""
    url = metadata.get("url", "unknown")
    channel = metadata.get("channel", "Unknown")
    title = metadata.get("title", "Untitled")
    date = metadata.get("upload_date", "unknown")
    duration = metadata.get("duration_string", str(metadata.get("duration", "unknown")))
    extracted = datetime.now().strftime("%Y-%m-%d")

    metadata_section = ""
    if metadata.get("description"):
        desc = metadata["description"][:500]
        metadata_section = f"Video description: {desc}\n"

    if chunk_num is not None:
        metadata_section += f"\nThis is part {chunk_num} of {total_chunks} of a long transcript.\n"
        if chunk_num > 1:
            metadata_section += "Summarize only the content in THIS chunk. Do not repeat the frontmatter.\n"

    return USER_PROMPT_TEMPLATE.format(
        metadata_section=metadata_section,
        url=url,
        channel=channel,
        title=title,
        date=date,
        duration=duration,
        extracted=extracted,
        transcript=transcript_chunk,
    )


def _call_anthropic(user_prompt, system_prompt):
    """Call Anthropic Claude API."""
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text


def _call_openai(user_prompt, system_prompt):
    """Call OpenAI API."""
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=8000,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


def _llm_call(provider, user_prompt, system_prompt=SYSTEM_PROMPT):
    """Route LLM call to the active provider."""
    if provider == "anthropic":
        return _call_anthropic(user_prompt, system_prompt)
    elif provider == "openai":
        return _call_openai(user_prompt, system_prompt)
    else:
        raise ValueError(f"Unknown provider: {provider}")


def compress_chunk(provider, transcript_chunk, metadata, chunk_num=None, total_chunks=None):
    """Send a transcript chunk to the LLM for summarization."""
    user_prompt = _build_user_prompt(transcript_chunk, metadata, chunk_num, total_chunks)
    return _llm_call(provider, user_prompt)


def merge_summaries(provider, summaries, metadata):
    """Merge multiple chunk summaries into a single cohesive KB entry."""
    combined = "\n\n---\n\n".join(summaries)

    merge_prompt = f"""You have {len(summaries)} partial summaries from different sections of a long video.
Merge them into a single cohesive knowledge base entry following the same structure
(frontmatter, executive summary, key topics, detailed notes, quotes, action items).

Deduplicate topics, combine related notes, and ensure the result reads as one document.
Output ONLY the final merged markdown.

PARTIAL SUMMARIES:

{combined}"""

    return _llm_call(provider, merge_prompt)


def compress_to_kb(transcript_path, metadata_path=None, output_path=None):
    """Compress a transcript into a structured KB entry."""
    transcript_path = Path(transcript_path)

    if not transcript_path.exists():
        print(f"Error: File not found: {transcript_path}", file=sys.stderr)
        sys.exit(1)

    provider = _get_provider()
    if not provider:
        print("Error: No LLM API key found.", file=sys.stderr)
        print("Set ANTHROPIC_API_KEY or OPENAI_API_KEY in your .env file.", file=sys.stderr)
        sys.exit(1)

    provider_label = "Claude Sonnet" if provider == "anthropic" else "GPT-4o"
    print(f"Provider: {provider_label}", file=sys.stderr)

    # Load transcript
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    print(f"Transcript: {transcript_path} ({len(transcript):,} chars)", file=sys.stderr)

    # Load metadata
    metadata = {}
    if metadata_path:
        metadata_path = Path(metadata_path)
        if metadata_path.exists():
            with open(metadata_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)
            print(f"Metadata loaded: {metadata.get('title', 'unknown')}", file=sys.stderr)
        else:
            print(f"Warning: Metadata file not found: {metadata_path}", file=sys.stderr)
    else:
        # Try to auto-detect metadata.json in same directory
        auto_meta = transcript_path.parent / "metadata.json"
        if auto_meta.exists():
            with open(auto_meta, "r", encoding="utf-8") as f:
                metadata = json.load(f)
            print(f"Auto-detected metadata: {metadata.get('title', 'unknown')}", file=sys.stderr)

    # Determine output path
    if output_path is None:
        channel_slug = slugify(metadata.get("channel", "unknown"))
        date = metadata.get("upload_date", datetime.now().strftime("%Y-%m-%d"))
        title_slug = slugify(metadata.get("title", transcript_path.stem))
        output_dir = KB_BASE / channel_slug
        output_path = output_dir / f"{date}_{title_slug}.md"
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Chunk if transcript is very long
    chunks = chunk_transcript(transcript)

    if len(chunks) == 1:
        print(f"Compressing transcript with {provider_label}...", file=sys.stderr)
        result = compress_chunk(provider, transcript, metadata)
    else:
        print(f"Long transcript detected, processing in {len(chunks)} chunks...", file=sys.stderr)
        summaries = []
        for i, chunk in enumerate(chunks, 1):
            print(f"  Processing chunk {i}/{len(chunks)}...", file=sys.stderr)
            summary = compress_chunk(provider, chunk, metadata, i, len(chunks))
            summaries.append(summary)

        print(f"Merging {len(summaries)} chunk summaries...", file=sys.stderr)
        result = merge_summaries(provider, summaries, metadata)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nKB entry created!", file=sys.stderr)
    print(f"  Output: {output_path}", file=sys.stderr)
    print(f"  Size: {len(result):,} chars", file=sys.stderr)

    # Only output path goes to stdout
    print(output_path)


def prepare_for_claude_code(transcript_path, metadata_path=None, output_path=None):
    """Prepare everything for Claude Code to do the compression itself (no API key needed).

    Outputs a JSON payload to stdout with: output_path, transcript, metadata, system_prompt.
    Claude Code reads this and writes the KB entry using its own LLM capability.
    """
    transcript_path = Path(transcript_path)

    if not transcript_path.exists():
        print(f"Error: File not found: {transcript_path}", file=sys.stderr)
        sys.exit(1)

    # Load transcript
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    print(f"Transcript: {transcript_path} ({len(transcript):,} chars)", file=sys.stderr)

    # Load metadata
    metadata = {}
    if metadata_path:
        metadata_path = Path(metadata_path)
        if metadata_path.exists():
            with open(metadata_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)
    else:
        auto_meta = transcript_path.parent / "metadata.json"
        if auto_meta.exists():
            with open(auto_meta, "r", encoding="utf-8") as f:
                metadata = json.load(f)

    # Determine output path
    if output_path is None:
        channel_slug = slugify(metadata.get("channel", "unknown"))
        date = metadata.get("upload_date", datetime.now().strftime("%Y-%m-%d"))
        title_slug = slugify(metadata.get("title", transcript_path.stem))
        output_dir = KB_BASE / channel_slug
        output_path = output_dir / f"{date}_{title_slug}.md"
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Output JSON payload for Claude Code
    payload = {
        "output_path": str(output_path),
        "metadata": metadata,
        "transcript_path": str(transcript_path),
    }
    print(json.dumps(payload))
    print(f"Prepared for Claude Code compression -> {output_path}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Compress a transcript into a structured knowledge base entry using Claude"
    )
    parser.add_argument(
        "transcript",
        help="Path to the transcript text file"
    )
    parser.add_argument(
        "--metadata", "-m",
        help="Path to the metadata JSON file (auto-detected if in same directory)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Custom output path (default: knowledge-base/youtube/{channel}/{date}_{slug}.md)"
    )

    parser.add_argument(
        "--prepare", action="store_true",
        help="Prepare mode: output transcript, metadata, and output path as JSON for Claude Code to compress directly (no API key needed)"
    )

    args = parser.parse_args()
    if args.prepare:
        prepare_for_claude_code(args.transcript, args.metadata, args.output)
    else:
        compress_to_kb(args.transcript, args.metadata, args.output)


if __name__ == "__main__":
    main()
