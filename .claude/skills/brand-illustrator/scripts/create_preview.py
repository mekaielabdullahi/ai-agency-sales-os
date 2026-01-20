#!/usr/bin/env python3
"""
AriseGroup.ai LinkedIn Post Preview Generator

Creates a LinkedIn-style mockup image showing how the post will appear.
Perfect for team approval before posting.

Usage:
    python create_preview.py --project "2026-01-20-ai-audits-linkedin" --copy A
    python create_preview.py --project "2026-01-20-ai-audits-linkedin" --copy B --output preview.png

Output:
    projects/[project-name]/linkedin-preview.png
"""

import os
import sys
import argparse
import textwrap
from pathlib import Path
from datetime import datetime

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


# Configuration
SKILL_DIR = Path(__file__).parent.parent
PROJECTS_DIR = SKILL_DIR / "projects"
ASSETS_DIR = SKILL_DIR / "assets"

# LinkedIn mockup dimensions
PREVIEW_WIDTH = 600
PREVIEW_PADDING = 20
IMAGE_SIZE = 560  # Width of the post image in preview

# Brand colors
COLORS = {
    "bg": "#FFFFFF",
    "card_bg": "#FFFFFF",
    "text_primary": "#000000",
    "text_secondary": "#666666",
    "text_hashtag": "#0A66C2",
    "border": "#E0E0E0",
    "link_blue": "#0A66C2",
    "amber": "#E8914F",
}


def get_font(size: int, bold: bool = False):
    """Get a font, falling back to default if custom fonts unavailable."""
    # Try common system fonts
    font_names = [
        "arial.ttf",
        "Arial.ttf",
        "DejaVuSans.ttf",
        "Helvetica.ttf",
        "segoeui.ttf",
    ]

    if bold:
        font_names = [
            "arialbd.ttf",
            "Arial Bold.ttf",
            "DejaVuSans-Bold.ttf",
            "Helvetica-Bold.ttf",
            "segoeuib.ttf",
        ] + font_names

    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except (OSError, IOError):
            continue

    # Fallback to default
    return ImageFont.load_default()


def wrap_text(text: str, font: ImageFont, max_width: int, draw: ImageDraw) -> list[str]:
    """Wrap text to fit within max_width."""
    lines = []
    paragraphs = text.split('\n')

    for paragraph in paragraphs:
        if not paragraph.strip():
            lines.append("")
            continue

        words = paragraph.split()
        if not words:
            lines.append("")
            continue

        current_line = words[0]

        for word in words[1:]:
            test_line = current_line + " " + word
            bbox = draw.textbbox((0, 0), test_line, font=font)
            width = bbox[2] - bbox[0]

            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)

    return lines


def parse_copy_from_file(copy_path: Path, copy_choice: str) -> dict:
    """Parse the selected copy variation from post-copy.md."""
    if not copy_path.exists():
        return None

    with open(copy_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the selected copy section
    target = f"## COPY {copy_choice.upper()}"

    if target not in content:
        return None

    # Extract the section
    start = content.find(target)
    next_copy = content.find("## COPY", start + 1)
    section = content[start:next_copy] if next_copy != -1 else content[start:]

    # Parse content between --- markers
    lines = section.split('\n')
    copy_text = []
    hashtags = ""
    in_content = False

    for line in lines:
        if line.strip() == "---":
            in_content = not in_content
            continue
        if in_content:
            if line.strip().startswith("#") and not line.strip().startswith("##"):
                hashtags = line.strip()
            else:
                copy_text.append(line)

    return {
        "text": '\n'.join(copy_text).strip(),
        "hashtags": hashtags,
    }


def create_linkedin_preview(project_dir: Path, copy_choice: str, output_name: str = None) -> Path:
    """Create a LinkedIn post preview mockup."""

    if not PIL_AVAILABLE:
        print("ERROR: Pillow not installed. Run: pip install Pillow")
        sys.exit(1)

    # Find the latest image
    image_files = sorted(project_dir.glob("v*.png"))
    excalidraw_files = [f for f in image_files if "excalidraw" not in f.name.lower() and "preview" not in f.name.lower() and "canvas" not in f.name.lower()]

    if not excalidraw_files:
        print(f"ERROR: No illustration found in {project_dir}")
        sys.exit(1)

    source_image_path = excalidraw_files[-1]

    # Load the copy
    copy_path = project_dir / "post-copy.md"
    copy_data = parse_copy_from_file(copy_path, copy_choice)

    if not copy_data:
        print(f"ERROR: Could not find COPY {copy_choice.upper()} in {copy_path}")
        sys.exit(1)

    # Load source image
    source_image = Image.open(source_image_path)

    # Calculate dimensions
    # Scale image to fit preview width
    img_ratio = source_image.height / source_image.width
    preview_img_width = IMAGE_SIZE
    preview_img_height = int(preview_img_width * img_ratio)

    # Create fonts
    font_name = get_font(16, bold=True)
    font_title = get_font(14)
    font_body = get_font(14)
    font_hashtag = get_font(13)
    font_small = get_font(12)

    # Create a temporary image to calculate text height
    temp_img = Image.new('RGB', (PREVIEW_WIDTH, 100), COLORS["bg"])
    temp_draw = ImageDraw.Draw(temp_img)

    # Wrap the copy text
    text_max_width = PREVIEW_WIDTH - (PREVIEW_PADDING * 2) - 20
    wrapped_lines = wrap_text(copy_data["text"], font_body, text_max_width, temp_draw)

    # Calculate heights
    header_height = 70  # Profile section
    image_height = preview_img_height + 10

    line_height = 20
    text_height = len(wrapped_lines) * line_height + 20

    hashtag_height = 30 if copy_data["hashtags"] else 0
    footer_height = 50  # Like, comment, share buttons

    total_height = (
        PREVIEW_PADDING +
        header_height +
        image_height +
        text_height +
        hashtag_height +
        footer_height +
        PREVIEW_PADDING
    )

    # Create the preview image
    preview = Image.new('RGB', (PREVIEW_WIDTH, total_height), COLORS["bg"])
    draw = ImageDraw.Draw(preview)

    # Draw card background with border
    draw.rectangle(
        [5, 5, PREVIEW_WIDTH - 5, total_height - 5],
        fill=COLORS["card_bg"],
        outline=COLORS["border"],
        width=1
    )

    y_cursor = PREVIEW_PADDING + 10

    # === HEADER: Profile Section ===
    # Profile circle (placeholder)
    profile_x = PREVIEW_PADDING + 10
    profile_size = 48
    draw.ellipse(
        [profile_x, y_cursor, profile_x + profile_size, y_cursor + profile_size],
        fill=COLORS["amber"],
        outline=COLORS["amber"]
    )

    # "A" for AriseGroup
    draw.text(
        (profile_x + 17, y_cursor + 10),
        "A",
        fill="#FFFFFF",
        font=get_font(24, bold=True)
    )

    # Name and details
    text_x = profile_x + profile_size + 12
    draw.text((text_x, y_cursor + 2), "AriseGroup.ai", fill=COLORS["text_primary"], font=font_name)
    draw.text((text_x, y_cursor + 22), "AI Consulting for SMBs", fill=COLORS["text_secondary"], font=font_title)
    draw.text((text_x, y_cursor + 40), "Just now · 🌐", fill=COLORS["text_secondary"], font=font_small)

    y_cursor += header_height

    # === POST IMAGE ===
    # Resize and paste the illustration
    resized_img = source_image.resize((preview_img_width, preview_img_height), Image.Resampling.LANCZOS)
    img_x = (PREVIEW_WIDTH - preview_img_width) // 2
    preview.paste(resized_img, (img_x, y_cursor))

    y_cursor += image_height + 10

    # === POST TEXT ===
    text_x = PREVIEW_PADDING + 15
    for line in wrapped_lines:
        if line.strip().startswith("→"):
            # Bullet point styling
            draw.text((text_x, y_cursor), line, fill=COLORS["text_primary"], font=font_body)
        else:
            draw.text((text_x, y_cursor), line, fill=COLORS["text_primary"], font=font_body)
        y_cursor += line_height

    y_cursor += 10

    # === HASHTAGS ===
    if copy_data["hashtags"]:
        draw.text((text_x, y_cursor), copy_data["hashtags"], fill=COLORS["link_blue"], font=font_hashtag)
        y_cursor += hashtag_height

    # === FOOTER: Engagement Buttons ===
    y_cursor += 10
    draw.line([(PREVIEW_PADDING, y_cursor), (PREVIEW_WIDTH - PREVIEW_PADDING, y_cursor)], fill=COLORS["border"], width=1)
    y_cursor += 15

    # Engagement buttons
    buttons = ["👍 Like", "💬 Comment", "🔄 Repost", "📤 Send"]
    button_width = (PREVIEW_WIDTH - PREVIEW_PADDING * 2) // len(buttons)

    for i, button in enumerate(buttons):
        btn_x = PREVIEW_PADDING + (i * button_width) + (button_width // 2) - 30
        draw.text((btn_x, y_cursor), button, fill=COLORS["text_secondary"], font=font_small)

    # === SAVE ===
    output_filename = output_name or f"linkedin-preview-{copy_choice.lower()}.png"
    output_path = project_dir / output_filename
    preview.save(output_path, "PNG")

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Create LinkedIn post preview mockup"
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Project folder name"
    )
    parser.add_argument(
        "--copy",
        required=True,
        choices=["A", "B", "C", "a", "b", "c"],
        help="Which copy variation to use (A, B, or C)"
    )
    parser.add_argument(
        "--output",
        help="Output filename (default: linkedin-preview-[copy].png)"
    )

    args = parser.parse_args()

    # Find project
    project_dir = PROJECTS_DIR / args.project
    if not project_dir.exists():
        print(f"ERROR: Project not found: {project_dir}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print("AriseGroup.ai LinkedIn Preview Generator")
    print(f"{'='*60}")
    print(f"Project: {args.project}")
    print(f"Copy: {args.copy.upper()}")

    # Generate preview
    output_path = create_linkedin_preview(project_dir, args.copy, args.output)

    print(f"Preview saved: {output_path}")
    print(f"{'='*60}")
    print("\nShare this image with your team for approval!")
    print("Once approved, copy the text from post-copy.md and post to LinkedIn.")
    print(f"{'='*60}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
