#!/usr/bin/env python3
"""
AriseGroup.ai Content Canvas Generator

Creates an Excalidraw canvas containing the illustration, post copy variations,
hashtags, and metadata - all ready for review before posting.

Usage:
    python create_canvas.py --project "2026-01-20-business-efficiency-linkedin"

Output:
    projects/[project-name]/content-canvas.excalidraw
"""

import os
import sys
import argparse
import base64
import json
import uuid
from pathlib import Path
from datetime import datetime


# Configuration
SKILL_DIR = Path(__file__).parent.parent
PROJECTS_DIR = SKILL_DIR / "projects"

# Canvas layout constants
CANVAS_WIDTH = 1800
CANVAS_HEIGHT = 1400
PADDING = 40

# AriseGroup.ai brand colors
BRAND_COLORS = {
    "amber": "#E8914F",
    "gold": "#F5C26B",
    "teal": "#2D7D8A",
    "navy": "#1A2B4A",
    "cream": "#FDF8F3",
    "white": "#FEFDFB",
}


def generate_id():
    """Generate a short unique ID for Excalidraw elements."""
    return str(uuid.uuid4())[:8]


def create_text_element(text: str, x: int, y: int, width: int = 400, font_size: int = 16, color: str = "#1A2B4A"):
    """Create an Excalidraw text element."""
    return {
        "type": "text",
        "version": 1,
        "versionNonce": 1,
        "isDeleted": False,
        "id": generate_id(),
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "x": x,
        "y": y,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "width": width,
        "height": font_size * 1.5,
        "seed": 1,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "boundElements": None,
        "updated": 1,
        "link": None,
        "locked": False,
        "fontSize": font_size,
        "fontFamily": 1,
        "text": text,
        "textAlign": "left",
        "verticalAlign": "top",
        "containerId": None,
        "originalText": text,
        "lineHeight": 1.25,
    }


def create_rectangle(x: int, y: int, width: int, height: int, color: str = "#E8914F", fill: str = "transparent"):
    """Create an Excalidraw rectangle element."""
    return {
        "type": "rectangle",
        "version": 1,
        "versionNonce": 1,
        "isDeleted": False,
        "id": generate_id(),
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "x": x,
        "y": y,
        "strokeColor": color,
        "backgroundColor": fill,
        "width": width,
        "height": height,
        "seed": 1,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3},
        "boundElements": None,
        "updated": 1,
        "link": None,
        "locked": False,
    }


def create_image_element(file_id: str, x: int, y: int, width: int, height: int):
    """Create an Excalidraw image element."""
    return {
        "type": "image",
        "version": 1,
        "versionNonce": 1,
        "isDeleted": False,
        "id": generate_id(),
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "x": x,
        "y": y,
        "strokeColor": "transparent",
        "backgroundColor": "transparent",
        "width": width,
        "height": height,
        "seed": 1,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "boundElements": None,
        "updated": 1,
        "link": None,
        "locked": False,
        "status": "saved",
        "fileId": file_id,
        "scale": [1, 1],
    }


def load_image_as_base64(image_path: Path) -> tuple[str, str]:
    """Load image and return (file_id, data_url)."""
    with open(image_path, "rb") as f:
        image_data = f.read()

    b64_data = base64.b64encode(image_data).decode("utf-8")
    file_id = generate_id()
    data_url = f"data:image/png;base64,{b64_data}"

    return file_id, data_url


def parse_post_copy(copy_path: Path) -> list[dict]:
    """Parse post-copy.md into structured copy variations."""
    if not copy_path.exists():
        return []

    with open(copy_path, "r", encoding="utf-8") as f:
        content = f.read()

    variations = []

    # Split by "COPY" headers
    sections = content.split("## COPY")

    for section in sections[1:]:  # Skip content before first COPY
        lines = section.strip().split("\n")
        if not lines:
            continue

        # Extract title from first line
        title_line = lines[0].strip()
        title = f"COPY {title_line.split(':')[0].strip()}" if ":" in title_line else f"COPY {title_line}"

        # Find the actual copy content (between --- markers or after title)
        copy_text = ""
        hashtags = ""
        in_copy = False

        for line in lines[1:]:
            if line.strip() == "---":
                in_copy = not in_copy
                continue
            if in_copy or (not in_copy and line.strip() and not line.startswith("#")):
                if line.strip().startswith("#") and not line.startswith("##"):
                    hashtags = line.strip()
                else:
                    copy_text += line + "\n"

        if copy_text.strip():
            variations.append({
                "title": title,
                "text": copy_text.strip(),
                "hashtags": hashtags,
            })

    return variations


def create_content_canvas(project_dir: Path) -> dict:
    """Create the full content canvas Excalidraw structure."""
    elements = []
    files = {}

    # Find the latest image version
    image_files = sorted(project_dir.glob("v*.png"))
    if not image_files:
        print(f"ERROR: No image found in {project_dir}")
        sys.exit(1)

    latest_image = image_files[-1]
    version = latest_image.stem

    # Load image
    file_id, data_url = load_image_as_base64(latest_image)
    files[file_id] = {
        "mimeType": "image/png",
        "id": file_id,
        "dataURL": data_url,
        "created": 1,
    }

    # Layout positions
    image_x = PADDING
    image_y = PADDING + 60  # Leave room for title
    image_size = 500  # Display size for image

    copy_x = image_x + image_size + PADDING * 2
    copy_y = image_y
    copy_width = CANVAS_WIDTH - copy_x - PADDING

    # === TITLE ===
    elements.append(create_text_element(
        f"Content Canvas: {project_dir.name}",
        PADDING, PADDING,
        width=800, font_size=28, color=BRAND_COLORS["navy"]
    ))

    # === IMAGE SECTION ===
    # Image label
    elements.append(create_text_element(
        f"ILLUSTRATION ({version}.png)",
        image_x, image_y - 30,
        width=300, font_size=14, color=BRAND_COLORS["teal"]
    ))

    # Image border
    elements.append(create_rectangle(
        image_x - 4, image_y - 4,
        image_size + 8, image_size + 8,
        color=BRAND_COLORS["amber"]
    ))

    # Image
    elements.append(create_image_element(
        file_id, image_x, image_y, image_size, image_size
    ))

    # === POST COPY SECTION ===
    elements.append(create_text_element(
        "POST COPY OPTIONS",
        copy_x, copy_y - 30,
        width=300, font_size=14, color=BRAND_COLORS["teal"]
    ))

    # Load post copy
    copy_path = project_dir / "post-copy.md"
    variations = parse_post_copy(copy_path)

    current_y = copy_y

    if variations:
        for i, variation in enumerate(variations):
            # Copy title
            elements.append(create_text_element(
                variation["title"],
                copy_x, current_y,
                width=copy_width, font_size=16, color=BRAND_COLORS["amber"]
            ))
            current_y += 30

            # Copy text box
            elements.append(create_rectangle(
                copy_x - 8, current_y - 8,
                copy_width + 16, 200,
                color=BRAND_COLORS["cream"], fill=BRAND_COLORS["cream"]
            ))

            # Copy text (truncate if too long)
            display_text = variation["text"][:500] + "..." if len(variation["text"]) > 500 else variation["text"]
            elements.append(create_text_element(
                display_text,
                copy_x, current_y,
                width=copy_width - 20, font_size=14, color=BRAND_COLORS["navy"]
            ))
            current_y += 220

            # Hashtags
            if variation["hashtags"]:
                elements.append(create_text_element(
                    variation["hashtags"],
                    copy_x, current_y,
                    width=copy_width, font_size=12, color=BRAND_COLORS["teal"]
                ))
                current_y += 30

            current_y += 20  # Space between variations
    else:
        elements.append(create_text_element(
            "(No post-copy.md found - add copy variations to see them here)",
            copy_x, current_y,
            width=copy_width, font_size=14, color="#888888"
        ))

    # === METADATA SECTION ===
    metadata_y = max(image_y + image_size + PADDING, current_y) + 20

    elements.append(create_text_element(
        "METADATA",
        PADDING, metadata_y,
        width=200, font_size=14, color=BRAND_COLORS["teal"]
    ))

    # Load metadata
    metadata_path = project_dir / f"{version}_metadata.txt"
    if metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata_text = f.read()
    else:
        metadata_text = f"Generated: {datetime.now().isoformat()}\nProject: {project_dir.name}"

    elements.append(create_text_element(
        metadata_text[:300],
        PADDING, metadata_y + 25,
        width=600, font_size=12, color="#666666"
    ))

    # === BUILD EXCALIDRAW STRUCTURE ===
    excalidraw = {
        "type": "excalidraw",
        "version": 2,
        "source": "brand-illustrator-canvas",
        "elements": elements,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": BRAND_COLORS["white"],
        },
        "files": files,
    }

    return excalidraw


def main():
    parser = argparse.ArgumentParser(
        description="Create content canvas with illustration, copy, and hashtags"
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Project folder name"
    )

    args = parser.parse_args()

    # Find project directory
    project_dir = PROJECTS_DIR / args.project
    if not project_dir.exists():
        print(f"ERROR: Project not found: {project_dir}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print("AriseGroup.ai Content Canvas Generator")
    print(f"{'='*60}")
    print(f"Project: {args.project}")

    # Create canvas
    canvas = create_content_canvas(project_dir)

    # Save
    output_path = project_dir / "content-canvas.excalidraw"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(canvas, f)

    print(f"Canvas saved: {output_path}")
    print(f"{'='*60}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
