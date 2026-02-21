#!/usr/bin/env python3
"""
Download audio and metadata from YouTube videos using yt-dlp.

Accepts a YouTube URL (video, playlist, or channel) and downloads audio-only
as mp3 with metadata extracted to JSON.

Usage:
    ./run modules/youtube-kb/tool/fetch_youtube_audio.py "https://youtube.com/watch?v=ABC123"
    ./run modules/youtube-kb/tool/fetch_youtube_audio.py "https://youtube.com/playlist?list=..."
    ./run modules/youtube-kb/tool/fetch_youtube_audio.py urls.txt

Output:
    .tmp/youtube-kb/{video_id}/audio.mp3
    .tmp/youtube-kb/{video_id}/metadata.json

Prints JSON manifest to stdout (one per video), progress to stderr.
"""

import sys
import os
import json
import argparse
from pathlib import Path
from datetime import datetime

import yt_dlp


TMP_BASE = Path(".tmp/youtube-kb")


def progress_hook(d):
    """Print download progress to stderr."""
    if d["status"] == "downloading":
        pct = d.get("_percent_str", "?%").strip()
        speed = d.get("_speed_str", "?").strip()
        print(f"  Downloading: {pct} at {speed}", file=sys.stderr, end="\r")
    elif d["status"] == "finished":
        print(f"\n  Download complete, converting...", file=sys.stderr)


def fetch_single_video(url, video_id, output_dir):
    """Download audio and extract metadata for a single video."""
    output_dir.mkdir(parents=True, exist_ok=True)
    audio_path = output_dir / "audio.mp3"
    metadata_path = output_dir / "metadata.json"

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": str(output_dir / "audio.%(ext)s"),
        "progress_hooks": [progress_hook],
        "quiet": True,
        "no_warnings": True,
    }

    print(f"Fetching: {url}", file=sys.stderr)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    # Extract metadata
    upload_date = info.get("upload_date", "")
    if upload_date:
        try:
            upload_date = datetime.strptime(upload_date, "%Y%m%d").strftime("%Y-%m-%d")
        except ValueError:
            pass

    metadata = {
        "video_id": info.get("id", video_id),
        "title": info.get("title", ""),
        "channel": info.get("channel", info.get("uploader", "")),
        "channel_id": info.get("channel_id", ""),
        "upload_date": upload_date,
        "duration": info.get("duration", 0),
        "duration_string": info.get("duration_string", ""),
        "description": info.get("description", ""),
        "url": info.get("webpage_url", url),
        "view_count": info.get("view_count", 0),
        "tags": info.get("tags", []),
        "categories": info.get("categories", []),
    }

    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"  Audio: {audio_path}", file=sys.stderr)
    print(f"  Metadata: {metadata_path}", file=sys.stderr)

    return {
        "video_id": metadata["video_id"],
        "title": metadata["title"],
        "channel": metadata["channel"],
        "duration": metadata["duration"],
        "audio_path": str(audio_path),
        "metadata_path": str(metadata_path),
    }


def fetch_url(url):
    """Fetch audio from a URL. Handles single videos and playlists."""
    results = []

    # First, extract info without downloading to check if it's a playlist
    with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True, "extract_flat": True}) as ydl:
        info = ydl.extract_info(url, download=False)

    if info.get("_type") == "playlist":
        entries = info.get("entries", [])
        print(f"Playlist detected: {info.get('title', 'Unknown')} ({len(entries)} videos)", file=sys.stderr)
        for i, entry in enumerate(entries, 1):
            video_id = entry.get("id", entry.get("url", "").split("=")[-1])
            video_url = entry.get("url", "")
            if not video_url:
                video_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"\n[{i}/{len(entries)}] {entry.get('title', video_id)}", file=sys.stderr)
            output_dir = TMP_BASE / video_id
            try:
                result = fetch_single_video(video_url, video_id, output_dir)
                results.append(result)
            except Exception as e:
                print(f"  Error: {e}", file=sys.stderr)
                results.append({"video_id": video_id, "error": str(e)})
    else:
        video_id = info.get("id", "unknown")
        output_dir = TMP_BASE / video_id
        result = fetch_single_video(url, video_id, output_dir)
        results.append(result)

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Download audio and metadata from YouTube videos"
    )
    parser.add_argument(
        "url",
        help="YouTube URL (video, playlist) or path to a text file with URLs (one per line)"
    )

    args = parser.parse_args()
    url_input = args.url

    all_results = []

    # Check if input is a file with URLs
    if os.path.isfile(url_input):
        print(f"Reading URLs from: {url_input}", file=sys.stderr)
        with open(url_input, "r") as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        print(f"Found {len(urls)} URLs", file=sys.stderr)
        for url in urls:
            try:
                results = fetch_url(url)
                all_results.extend(results)
            except Exception as e:
                print(f"Error processing {url}: {e}", file=sys.stderr)
                all_results.append({"url": url, "error": str(e)})
    else:
        all_results = fetch_url(url_input)

    # Print JSON manifest to stdout
    print(json.dumps(all_results, indent=2))


if __name__ == "__main__":
    main()
