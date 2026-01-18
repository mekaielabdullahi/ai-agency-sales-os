import re
import base64
import os

# Read the markdown file
with open("c:/Users/MEKAIEL/Downloads/AI_Opportunity_Assessment_Proposal_v4.docx.md", "r", encoding="utf-8") as f:
    content = f.read()

# Find base64 image references
pattern = r'\[image(\d+)\]: <data:image/png;base64,([^>]+)>'
matches = re.findall(pattern, content)

print(f"Found {len(matches)} images")

# Save images
output_dir = "c:/Users/MEKAIEL/Downloads/proposal_images"
os.makedirs(output_dir, exist_ok=True)

for idx, (num, b64data) in enumerate(matches):
    try:
        img_data = base64.b64decode(b64data)
        filepath = f"{output_dir}/image{num}.png"
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"Saved image{num}.png ({len(img_data)} bytes)")
    except Exception as e:
        print(f"Error with image {num}: {e}")
