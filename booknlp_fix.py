# Create a file named fix_booknlp.py
import os
import sys
from pathlib import Path

# Find the booknlp package location
import booknlp
booknlp_path = Path(booknlp.__file__).parent

print(f"BookNLP package located at: {booknlp_path}")

# Path to the file that needs to be modified
booknlp_file = booknlp_path / "booknlp.py"

if not booknlp_file.exists():
    print(f"Cannot find {booknlp_file}")
    sys.exit(1)

# Read the file content
with open(booknlp_file, 'r') as f:
    content = f.read()

# Apply fixes
# 1. Fix for state_dict loading issue
if "strict=True" in content:
    content = content.replace("strict=True", "strict=False")
    print("Applied fix for strict model loading")

# 2. Fix for path handling issues
if "path.endswith(\"zip\")" in content:
    content = content.replace("path.endswith(\"zip\")", "(str(path).endswith(\".zip\") or str(path).endswith(\".pt\"))")
    print("Applied fix for path handling")

# Write the modified content
with open(booknlp_file, 'w') as f:
    f.write(content)

print("BookNLP fixes applied successfully")