#!/usr/bin/env python3
"""
AriseGroup.ai Brand Illustration Generator

Generates on-brand illustrations using Google Gemini's image generation API.
This script is called by the brand-illustrator Claude Code skill.

Usage:
    python generate.py --project "project-folder-name" --prompt "path/to/prompt.md"
    python generate.py --project "2026-01-19-ai-audit" --width 1080 --height 1080

Environment:
    GEMINI_API_KEY: Your Google Gemini API key (or set in .env file)
"""

import os
import sys
import argparse
import base64
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
    GENAI_NEW = True
except ImportError:
    GENAI_NEW = False
    try:
        import google.generativeai as genai_old
        GENAI_AVAILABLE = True
    except ImportError:
        GENAI_AVAILABLE = False

try:
    from PIL import Image
    import io
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


# Configuration
SKILL_DIR = Path(__file__).parent.parent
PROJECTS_DIR = SKILL_DIR / "projects"
ASSETS_DIR = SKILL_DIR / "assets"
ENV_FILE = SKILL_DIR / ".env"


def check_dependencies():
    """Check if required dependencies are installed."""
    missing = []

    if not GENAI_AVAILABLE:
        missing.append("google-genai")
    if not PIL_AVAILABLE:
        missing.append("Pillow")
    if not DOTENV_AVAILABLE:
        missing.append("python-dotenv")

    if missing:
        print("Missing required packages. Install with:")
        print(f"  pip install {' '.join(missing)}")
        sys.exit(1)


def load_api_key():
    """Load the Gemini API key from environment or .env file."""
    # Try loading from .env file first
    if DOTENV_AVAILABLE and ENV_FILE.exists():
        load_dotenv(ENV_FILE)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("ERROR: GEMINI_API_KEY not found.")
        print(f"Please set it in environment or create {ENV_FILE} with:")
        print("  GEMINI_API_KEY=your_api_key_here")
        sys.exit(1)

    return api_key


def read_prompt_file(prompt_path: Path) -> str:
    """Read the prompt from a markdown file."""
    if not prompt_path.exists():
        print(f"ERROR: Prompt file not found: {prompt_path}")
        sys.exit(1)

    with open(prompt_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract the prompt from the markdown - look for the code block
    if "```" in content:
        # Find content between first ``` and next ```
        start = content.find("```") + 3
        # Skip the optional language identifier line
        newline_after_start = content.find("\n", start)
        if newline_after_start != -1:
            start = newline_after_start + 1
        end = content.find("```", start)
        if end != -1:
            return content[start:end].strip()

    # If no code block, return everything after "## Full Generation Prompt"
    if "## Full Generation Prompt" in content:
        start = content.find("## Full Generation Prompt")
        return content[start:].strip()

    return content


def get_next_version(project_dir: Path) -> int:
    """Determine the next version number for generated images."""
    existing = list(project_dir.glob("v*.png"))
    if not existing:
        return 1

    versions = []
    for f in existing:
        try:
            # Extract version number from filename like "v1.png", "v2.png"
            version = int(f.stem[1:])
            versions.append(version)
        except ValueError:
            continue

    return max(versions) + 1 if versions else 1


def generate_image_new_api(prompt: str, api_key: str, width: int = 1080, height: int = 1080):
    """Generate an image using the new google.genai API."""

    client = genai.Client(api_key=api_key)

    # List of models to try in order (from listing available models)
    image_models = [
        ('gemini-2.5-flash-image', 'Gemini 2.5 Flash Image'),
        ('gemini-3-pro-image-preview', 'Gemini 3 Pro Image Preview'),
        ('gemini-2.0-flash-exp-image-generation', 'Gemini 2.0 Flash Exp Image'),
        ('gemini-2.5-flash', 'Gemini 2.5 Flash'),
        ('gemini-2.0-flash', 'Gemini 2.0 Flash'),
        ('nano-banana-pro-preview', 'Nano Banana Pro'),
    ]

    last_error = None

    for model_id, model_name in image_models:
        try:
            print(f"Trying {model_name}...")
            response = client.models.generate_content(
                model=model_id,
                contents=f"Generate a detailed digital illustration: {prompt}",
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE', 'TEXT']
                )
            )

            # Extract image from response
            if response.candidates and response.candidates[0].content.parts:
                for part in response.candidates[0].content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        print(f"Success with {model_name}!")
                        return part.inline_data.data

            print(f"{model_name}: No image in response, trying next...")

        except Exception as e:
            error_str = str(e)
            print(f"{model_name} failed: {error_str[:100]}...")
            last_error = e

            # If quota exceeded, try next model
            if "RESOURCE_EXHAUSTED" in error_str or "429" in error_str:
                continue
            # If model not found, try next
            if "NOT_FOUND" in error_str or "404" in error_str:
                continue
            # For other errors, might still try next
            continue

    # All models failed
    raise Exception(f"All models failed. Last error: {last_error}")


def save_image(image_data, output_path: Path, width: int, height: int):
    """Save the generated image to a file."""

    try:
        if isinstance(image_data, bytes):
            # Raw bytes from API
            image = Image.open(io.BytesIO(image_data))
        elif isinstance(image_data, Image.Image):
            # Already a PIL Image
            image = image_data
        elif isinstance(image_data, str):
            # Base64 encoded
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
        else:
            print(f"Unknown image data type: {type(image_data)}")
            sys.exit(1)

        # Resize if needed
        if image.size != (width, height):
            image = image.resize((width, height), Image.Resampling.LANCZOS)

        # Ensure proper mode for PNG
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
            # Keep transparency
            pass
        elif image.mode != 'RGB':
            image = image.convert('RGB')

        # Save
        image.save(output_path, "PNG", quality=95)
        print(f"Image saved: {output_path}")

        return True

    except Exception as e:
        print(f"Error saving image: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate AriseGroup.ai brand illustrations"
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Project folder name (e.g., '2026-01-19-ai-audit')"
    )
    parser.add_argument(
        "--prompt",
        help="Path to prompt.md file (defaults to project folder)"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1080,
        help="Image width in pixels (default: 1080)"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=1080,
        help="Image height in pixels (default: 1080)"
    )
    parser.add_argument(
        "--prompt-text",
        help="Direct prompt text (alternative to prompt file)"
    )

    args = parser.parse_args()

    # Check dependencies
    check_dependencies()

    # Load API key
    api_key = load_api_key()

    # Set up project directory
    project_dir = PROJECTS_DIR / args.project
    if not project_dir.exists():
        project_dir.mkdir(parents=True)
        print(f"Created project directory: {project_dir}")

    # Get prompt
    if args.prompt_text:
        prompt = args.prompt_text
    elif args.prompt:
        prompt_path = Path(args.prompt)
        prompt = read_prompt_file(prompt_path)
    else:
        # Default to prompt.md in project folder
        prompt_path = project_dir / "prompt.md"
        if prompt_path.exists():
            prompt = read_prompt_file(prompt_path)
        else:
            print(f"ERROR: No prompt specified and no prompt.md found in {project_dir}")
            print("Provide --prompt, --prompt-text, or create prompt.md in project folder")
            sys.exit(1)

    # Determine output filename
    version = get_next_version(project_dir)
    output_path = project_dir / f"v{version}.png"

    print(f"\n{'='*60}")
    print("AriseGroup.ai Brand Illustration Generator")
    print(f"{'='*60}")
    print(f"Project: {args.project}")
    print(f"Dimensions: {args.width}x{args.height}")
    print(f"Output: {output_path}")
    print(f"{'='*60}\n")

    print("Generating illustration...")
    print("(This may take 30-60 seconds)\n")

    # Generate
    try:
        if GENAI_NEW:
            image_data = generate_image_new_api(prompt, api_key, args.width, args.height)
        else:
            print("ERROR: New google-genai package required.")
            print("Install with: pip install google-genai")
            sys.exit(1)
    except Exception as e:
        print(f"\nGeneration failed: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure your API key has access to image generation")
        print("2. Check if Imagen is available in your region")
        print("3. Verify your API quota hasn't been exceeded")
        print("4. Try: pip install -U google-genai")
        sys.exit(1)

    # Save
    if save_image(image_data, output_path, args.width, args.height):
        print(f"\n{'='*60}")
        print("SUCCESS!")
        print(f"Image saved to: {output_path}")
        print(f"{'='*60}\n")

        # Save metadata
        metadata_path = project_dir / f"v{version}_metadata.txt"
        with open(metadata_path, "w", encoding="utf-8") as f:
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Dimensions: {args.width}x{args.height}\n")
            f.write(f"Prompt:\n{'-'*40}\n{prompt}\n")

        return 0
    else:
        print("\nFailed to save image.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
