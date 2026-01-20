#!/usr/bin/env python3
"""
AriseGroup.ai Brand Illustration Generator

Generates on-brand illustrations using multiple providers with automatic fallback.
Supports both paid (Gemini) and free (Pollinations, Hugging Face, Together AI) providers.

Usage:
    python generate.py --project "project-folder-name" --prompt "path/to/prompt.md"
    python generate.py --project "2026-01-19-ai-audit" --width 1080 --height 1080
    python generate.py --project "test" --provider pollinations  # Free, no API key
    python generate.py --project "test" --provider auto  # Try all providers

Providers (in fallback order):
    - gemini: Google Gemini (requires GEMINI_API_KEY)
    - pollinations: Pollinations.ai (FREE, no API key needed)
    - huggingface: Hugging Face Inference (FREE tier, optional HF_API_KEY)
    - together: Together AI (FREE $5 credits, requires TOGETHER_API_KEY)

Environment:
    GEMINI_API_KEY: Google Gemini API key (optional)
    HF_API_KEY: Hugging Face API key (optional, for higher rate limits)
    TOGETHER_API_KEY: Together AI API key (optional)
"""

import os
import sys
import argparse
import base64
import time
import json
import uuid
import urllib.parse
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
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

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

# Provider configuration
PROVIDERS = ["gemini", "pollinations", "huggingface", "together"]
FREE_PROVIDERS = ["pollinations", "huggingface", "together"]


def check_dependencies(provider: str = "auto"):
    """Check if required dependencies are installed."""
    missing = []

    if not PIL_AVAILABLE:
        missing.append("Pillow")
    if not DOTENV_AVAILABLE:
        missing.append("python-dotenv")
    if not REQUESTS_AVAILABLE:
        missing.append("requests")

    # Gemini-specific dependency
    if provider == "gemini" and not GENAI_AVAILABLE:
        missing.append("google-genai")

    if missing:
        print("Missing required packages. Install with:")
        print(f"  pip install {' '.join(missing)}")
        sys.exit(1)


def load_api_keys():
    """Load API keys from environment or .env file."""
    if DOTENV_AVAILABLE and ENV_FILE.exists():
        load_dotenv(ENV_FILE)

    return {
        "gemini": os.getenv("GEMINI_API_KEY"),
        "huggingface": os.getenv("HF_API_KEY"),
        "together": os.getenv("TOGETHER_API_KEY"),
        "pollinations": None,  # No key needed
    }


def generate_image_gemini(prompt: str, api_key: str, width: int = 1080, height: int = 1080):
    """Generate an image using Google Gemini API."""
    if not GENAI_NEW:
        raise Exception("New google-genai package required. Run: pip install google-genai")

    client = genai.Client(api_key=api_key)

    image_models = [
        ('gemini-2.0-flash-exp-image-generation', 'Gemini 2.0 Flash Exp Image'),
        ('gemini-2.0-flash', 'Gemini 2.0 Flash'),
    ]

    last_error = None

    for model_id, model_name in image_models:
        try:
            print(f"  Trying {model_name}...")
            response = client.models.generate_content(
                model=model_id,
                contents=f"Generate a detailed digital illustration: {prompt}",
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE', 'TEXT']
                )
            )

            if response.candidates and response.candidates[0].content.parts:
                for part in response.candidates[0].content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        print(f"  Success with {model_name}!")
                        return part.inline_data.data

            print(f"  {model_name}: No image in response, trying next...")

        except Exception as e:
            error_str = str(e)
            print(f"  {model_name} failed: {error_str[:100]}...")
            last_error = e
            continue

    raise Exception(f"All Gemini models failed. Last error: {last_error}")


def generate_image_pollinations(prompt: str, api_key: str = None, width: int = 1080, height: int = 1080):
    """
    Generate an image using Pollinations.ai (FREE, no API key needed).
    Uses Flux model by default.
    """
    if not REQUESTS_AVAILABLE:
        raise Exception("requests package not installed. Run: pip install requests")

    # URL-encode the prompt
    encoded_prompt = urllib.parse.quote(prompt)

    # Pollinations supports custom dimensions
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux&nologo=true"

    print(f"  Requesting from Pollinations.ai...")
    print(f"  Model: Flux")
    print(f"  Size: {width}x{height}")

    try:
        response = requests.get(url, timeout=120)
        response.raise_for_status()

        if response.headers.get('content-type', '').startswith('image/'):
            print(f"  Success!")
            return response.content
        else:
            raise Exception(f"Unexpected response type: {response.headers.get('content-type')}")

    except requests.exceptions.Timeout:
        raise Exception("Request timed out after 120 seconds")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")


def generate_image_huggingface(prompt: str, api_key: str = None, width: int = 1080, height: int = 1080):
    """
    Generate an image using Hugging Face Inference API.
    Works without API key (rate limited) or with free HF_API_KEY (higher limits).
    """
    if not REQUESTS_AVAILABLE:
        raise Exception("requests package not installed. Run: pip install requests")

    # Models to try (free tier compatible)
    models = [
        ("black-forest-labs/FLUX.1-schnell", "FLUX.1 Schnell"),
        ("stabilityai/stable-diffusion-xl-base-1.0", "SDXL Base"),
        ("runwayml/stable-diffusion-v1-5", "SD 1.5"),
    ]

    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    last_error = None

    for model_id, model_name in models:
        try:
            print(f"  Trying {model_name}...")

            url = f"https://api-inference.huggingface.co/models/{model_id}"

            payload = {
                "inputs": f"Digital illustration: {prompt}",
                "parameters": {
                    "width": min(width, 1024),  # HF has size limits
                    "height": min(height, 1024),
                }
            }

            response = requests.post(url, headers=headers, json=payload, timeout=120)

            if response.status_code == 503:
                # Model loading, wait and retry
                print(f"  {model_name} is loading, waiting...")
                time.sleep(20)
                response = requests.post(url, headers=headers, json=payload, timeout=120)

            if response.status_code == 200 and response.headers.get('content-type', '').startswith('image/'):
                print(f"  Success with {model_name}!")
                return response.content

            error_msg = response.text[:200] if response.text else f"Status {response.status_code}"
            print(f"  {model_name} failed: {error_msg}")
            last_error = Exception(error_msg)

        except Exception as e:
            print(f"  {model_name} failed: {str(e)[:100]}")
            last_error = e
            continue

    raise Exception(f"All Hugging Face models failed. Last error: {last_error}")


def generate_image_together(prompt: str, api_key: str, width: int = 1080, height: int = 1080):
    """
    Generate an image using Together AI API.
    Requires TOGETHER_API_KEY (free $5 credits on signup).
    """
    if not REQUESTS_AVAILABLE:
        raise Exception("requests package not installed. Run: pip install requests")

    if not api_key:
        raise Exception("TOGETHER_API_KEY required. Sign up at together.ai for free credits.")

    # Together AI models
    models = [
        ("black-forest-labs/FLUX.1-schnell-Free", "FLUX.1 Schnell (Free)"),
        ("stabilityai/stable-diffusion-xl-base-1.0", "SDXL Base"),
    ]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    last_error = None

    for model_id, model_name in models:
        try:
            print(f"  Trying {model_name}...")

            url = "https://api.together.xyz/v1/images/generations"

            payload = {
                "model": model_id,
                "prompt": f"Digital illustration: {prompt}",
                "width": min(width, 1024),
                "height": min(height, 1024),
                "steps": 4 if "schnell" in model_id.lower() else 20,
                "n": 1,
                "response_format": "b64_json"
            }

            response = requests.post(url, headers=headers, json=payload, timeout=120)

            if response.status_code == 200:
                data = response.json()
                if data.get("data") and data["data"][0].get("b64_json"):
                    print(f"  Success with {model_name}!")
                    return base64.b64decode(data["data"][0]["b64_json"])

            error_msg = response.text[:200] if response.text else f"Status {response.status_code}"
            print(f"  {model_name} failed: {error_msg}")
            last_error = Exception(error_msg)

        except Exception as e:
            print(f"  {model_name} failed: {str(e)[:100]}")
            last_error = e
            continue

    raise Exception(f"All Together AI models failed. Last error: {last_error}")


def read_prompt_file(prompt_path: Path) -> str:
    """Read the prompt from a markdown file."""
    if not prompt_path.exists():
        print(f"ERROR: Prompt file not found: {prompt_path}")
        sys.exit(1)

    with open(prompt_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract the prompt from the markdown - look for the code block
    if "```" in content:
        start = content.find("```") + 3
        newline_after_start = content.find("\n", start)
        if newline_after_start != -1:
            start = newline_after_start + 1
        end = content.find("```", start)
        if end != -1:
            return content[start:end].strip()

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
            version = int(f.stem[1:])
            versions.append(version)
        except ValueError:
            continue

    return max(versions) + 1 if versions else 1


def save_image(image_data, output_path: Path, width: int, height: int):
    """Save the generated image to a file."""
    try:
        if isinstance(image_data, bytes):
            image = Image.open(io.BytesIO(image_data))
        elif isinstance(image_data, Image.Image):
            image = image_data
        elif isinstance(image_data, str):
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
        else:
            print(f"Unknown image data type: {type(image_data)}")
            sys.exit(1)

        # Resize if needed
        if image.size != (width, height):
            print(f"  Resizing from {image.size[0]}x{image.size[1]} to {width}x{height}")
            image = image.resize((width, height), Image.Resampling.LANCZOS)

        # Ensure proper mode for PNG
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
            pass
        elif image.mode != 'RGB':
            image = image.convert('RGB')

        image.save(output_path, "PNG", quality=95)
        print(f"  Image saved: {output_path}")

        return True

    except Exception as e:
        print(f"Error saving image: {e}")
        return False


def create_excalidraw(image_path: Path, output_path: Path, width: int, height: int):
    """Create an Excalidraw file with the image embedded."""
    try:
        # Read the image and convert to base64
        with open(image_path, 'rb') as f:
            image_data = f.read()

        b64_data = base64.b64encode(image_data).decode('utf-8')
        data_url = f'data:image/png;base64,{b64_data}'

        # Generate unique IDs
        file_id = str(uuid.uuid4())[:8]
        element_id = str(uuid.uuid4())[:8]

        # Scale image to fit nicely in canvas (max 800px on longest side)
        scale = min(800 / width, 800 / height, 1.0)
        display_width = int(width * scale)
        display_height = int(height * scale)

        # Create Excalidraw JSON structure
        excalidraw = {
            'type': 'excalidraw',
            'version': 2,
            'source': 'brand-illustrator',
            'elements': [
                {
                    'type': 'image',
                    'version': 1,
                    'versionNonce': 1,
                    'isDeleted': False,
                    'id': element_id,
                    'fillStyle': 'solid',
                    'strokeWidth': 2,
                    'strokeStyle': 'solid',
                    'roughness': 0,
                    'opacity': 100,
                    'angle': 0,
                    'x': 100,
                    'y': 100,
                    'strokeColor': 'transparent',
                    'backgroundColor': 'transparent',
                    'width': display_width,
                    'height': display_height,
                    'seed': 1,
                    'groupIds': [],
                    'frameId': None,
                    'roundness': None,
                    'boundElements': None,
                    'updated': 1,
                    'link': None,
                    'locked': False,
                    'status': 'saved',
                    'fileId': file_id,
                    'scale': [1, 1]
                }
            ],
            'appState': {
                'gridSize': None,
                'viewBackgroundColor': '#ffffff'
            },
            'files': {
                file_id: {
                    'mimeType': 'image/png',
                    'id': file_id,
                    'dataURL': data_url,
                    'created': 1
                }
            }
        }

        # Save Excalidraw file
        with open(output_path, 'w') as f:
            json.dump(excalidraw, f)

        print(f"  Excalidraw saved: {output_path}")
        return True

    except Exception as e:
        print(f"Error creating Excalidraw: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate AriseGroup.ai brand illustrations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Providers:
  gemini       Google Gemini (requires GEMINI_API_KEY)
  pollinations Pollinations.ai - FREE, no API key needed!
  huggingface  Hugging Face - FREE tier, optional HF_API_KEY
  together     Together AI - FREE $5 credits, requires TOGETHER_API_KEY
  auto         Try all providers in order until one succeeds

Examples:
  # Quick test with free provider (no setup needed)
  python generate.py --project test --provider pollinations --prompt-text "A robot"

  # Auto fallback through all providers
  python generate.py --project test --provider auto --prompt-text "A robot"

  # Generate with Excalidraw file
  python generate.py --project test --provider pollinations --excalidraw --prompt-text "A robot"
"""
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
    parser.add_argument(
        "--provider",
        choices=["auto", "gemini", "pollinations", "huggingface", "together"],
        default="auto",
        help="Image generation provider (default: auto)"
    )
    parser.add_argument(
        "--excalidraw",
        action="store_true",
        help="Also create an Excalidraw file with the image embedded"
    )

    args = parser.parse_args()

    # Check dependencies
    check_dependencies(args.provider)

    # Load API keys
    api_keys = load_api_keys()

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
    print(f"Provider: {args.provider}")
    print(f"Output: {output_path}")
    print(f"{'='*60}\n")

    # Determine provider order
    if args.provider == "auto":
        # Try providers in order: gemini (if key), then free providers
        providers_to_try = []
        if api_keys["gemini"] and GENAI_AVAILABLE:
            providers_to_try.append("gemini")
        providers_to_try.extend(["pollinations", "huggingface"])
        if api_keys["together"]:
            providers_to_try.append("together")
    else:
        providers_to_try = [args.provider]

    # Provider functions
    provider_funcs = {
        "gemini": generate_image_gemini,
        "pollinations": generate_image_pollinations,
        "huggingface": generate_image_huggingface,
        "together": generate_image_together,
    }

    image_data = None
    used_provider = None

    for provider in providers_to_try:
        # Check if provider can be used
        if provider == "gemini" and not api_keys["gemini"]:
            print(f"\n--- Skipping Gemini (no API key) ---")
            continue
        if provider == "together" and not api_keys["together"]:
            print(f"\n--- Skipping Together AI (no API key) ---")
            continue

        try:
            print(f"\n--- Trying {provider.title()} ---")
            generate_func = provider_funcs[provider]
            image_data = generate_func(
                prompt,
                api_keys.get(provider),
                args.width,
                args.height
            )
            used_provider = provider
            break

        except Exception as e:
            error_str = str(e)
            print(f"\n{provider.title()} failed: {error_str[:200]}")

            if args.provider != "auto":
                # Explicit provider requested - fail with troubleshooting
                print("\nTroubleshooting:")
                if provider == "gemini":
                    print("1. Check GEMINI_API_KEY is set correctly")
                    print("2. Verify your API quota hasn't been exceeded")
                elif provider == "pollinations":
                    print("1. Check your internet connection")
                    print("2. Pollinations.ai may be temporarily unavailable")
                elif provider == "huggingface":
                    print("1. Try setting HF_API_KEY for higher rate limits")
                    print("2. Models may be loading - try again in a minute")
                elif provider == "together":
                    print("1. Check TOGETHER_API_KEY is set correctly")
                    print("2. Verify you have remaining credits")
                sys.exit(1)

            print("Trying next provider...")
            continue

    if image_data is None:
        print("\nAll providers failed to generate an image.")
        print("\nTry:")
        print("  --provider pollinations  (free, no setup)")
        print("  Set GEMINI_API_KEY in .env for Gemini")
        sys.exit(1)

    # Save
    if save_image(image_data, output_path, args.width, args.height):
        print(f"\n{'='*60}")
        print("SUCCESS!")
        print(f"Provider: {used_provider}")
        print(f"Image saved to: {output_path}")

        # Create Excalidraw file if requested
        if args.excalidraw:
            excalidraw_path = project_dir / f"v{version}.excalidraw"
            create_excalidraw(output_path, excalidraw_path, args.width, args.height)
            print(f"Excalidraw: {excalidraw_path}")

        print(f"{'='*60}\n")

        # Save metadata
        metadata_path = project_dir / f"v{version}_metadata.txt"
        with open(metadata_path, "w", encoding="utf-8") as f:
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Provider: {used_provider}\n")
            f.write(f"Dimensions: {args.width}x{args.height}\n")
            if args.excalidraw:
                f.write(f"Excalidraw: v{version}.excalidraw\n")
            f.write(f"Prompt:\n{'-'*40}\n{prompt}\n")

        return 0
    else:
        print("\nFailed to save image.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
