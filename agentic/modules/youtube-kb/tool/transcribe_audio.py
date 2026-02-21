#!/usr/bin/env python3
"""
Transcribe audio files using faster-whisper (local, free, no API needed).

Uses CTranslate2-based Whisper for fast CPU/GPU transcription with VAD filtering.
First run downloads the selected model (~150MB for base).

Usage:
    ./run modules/youtube-kb/tool/transcribe_audio.py ".tmp/youtube-kb/ABC123/audio.mp3"
    ./run modules/youtube-kb/tool/transcribe_audio.py audio.mp3 --model large-v3
    ./run modules/youtube-kb/tool/transcribe_audio.py audio.mp3 --timestamps
    ./run modules/youtube-kb/tool/transcribe_audio.py audio.mp3 --output custom_transcript.txt

Output:
    Creates transcript.txt in the same directory as the audio file (or custom path via --output).
    Prints the output path to stdout.
"""

import sys
import os
import argparse
import time
from pathlib import Path


VALID_MODELS = ["tiny", "base", "small", "medium", "large-v3"]


def format_timestamp(seconds):
    """Format seconds as [HH:MM:SS]."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"[{h:02d}:{m:02d}:{s:02d}]"


def transcribe_audio(audio_path, model_name="base", output_path=None, timestamps=False):
    """Transcribe an audio file using faster-whisper."""
    audio_path = Path(audio_path)

    if not audio_path.exists():
        print(f"Error: File not found: {audio_path}", file=sys.stderr)
        sys.exit(1)

    # Default output: transcript.txt in same directory as audio
    if output_path is None:
        output_path = audio_path.parent / "transcript.txt"
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Transcribing: {audio_path}", file=sys.stderr)
    print(f"Model: {model_name}", file=sys.stderr)
    print(f"Output: {output_path}", file=sys.stderr)

    # Import here so --help works without the dependency installed
    from faster_whisper import WhisperModel

    # Auto-detect compute: GPU if available, else CPU with int8
    try:
        import ctranslate2
        if ctranslate2.get_cuda_device_count() > 0:
            device = "cuda"
            compute_type = "float16"
            print(f"Using GPU (CUDA) with float16", file=sys.stderr)
        else:
            raise RuntimeError("No CUDA")
    except Exception:
        device = "cpu"
        compute_type = "int8"
        print(f"Using CPU with int8 quantization", file=sys.stderr)

    print(f"Loading model '{model_name}' (first run downloads it)...", file=sys.stderr)
    start_time = time.time()

    model = WhisperModel(model_name, device=device, compute_type=compute_type)

    load_time = time.time() - start_time
    print(f"Model loaded in {load_time:.1f}s", file=sys.stderr)

    print(f"Transcribing (with VAD filter)...", file=sys.stderr)
    start_time = time.time()

    segments, info = model.transcribe(
        str(audio_path),
        vad_filter=True,
        vad_parameters=dict(
            min_silence_duration_ms=500,
        ),
    )

    print(f"Detected language: {info.language} (probability {info.language_probability:.2f})", file=sys.stderr)

    # Write transcript
    lines = []
    segment_count = 0
    for segment in segments:
        segment_count += 1
        text = segment.text.strip()
        if timestamps:
            ts = format_timestamp(segment.start)
            lines.append(f"{ts} {text}")
        else:
            lines.append(text)

        # Progress indicator every 50 segments
        if segment_count % 50 == 0:
            print(f"  Processed {segment_count} segments...", file=sys.stderr)

    transcript = "\n".join(lines)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    elapsed = time.time() - start_time
    print(f"\nTranscription complete!", file=sys.stderr)
    print(f"  Segments: {segment_count}", file=sys.stderr)
    print(f"  Characters: {len(transcript):,}", file=sys.stderr)
    print(f"  Time: {elapsed:.1f}s", file=sys.stderr)
    print(f"  Saved to: {output_path}", file=sys.stderr)

    # Only output path goes to stdout
    print(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio files using faster-whisper (local, free)"
    )
    parser.add_argument(
        "audio_file",
        help="Path to the audio file to transcribe"
    )
    parser.add_argument(
        "--model", "-m",
        default="base",
        choices=VALID_MODELS,
        help="Whisper model to use (default: base). Larger = more accurate but slower."
    )
    parser.add_argument(
        "--output", "-o",
        help="Custom output path for the transcript (default: transcript.txt in audio directory)"
    )
    parser.add_argument(
        "--timestamps", "-t",
        action="store_true",
        help="Include [HH:MM:SS] timestamps in output"
    )

    args = parser.parse_args()
    transcribe_audio(args.audio_file, args.model, args.output, args.timestamps)


if __name__ == "__main__":
    main()
