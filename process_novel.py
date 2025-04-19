from booknlp.booknlp import BookNLP
import os
import sys
import time

# Create output directories
os.makedirs("output_small", exist_ok=True)
os.makedirs("output_big", exist_ok=True)

# Check if novel.txt exists in the input folder
novel_path = "input/novel.txt"
if not os.path.exists(novel_path):
    print(f"Error: novel.txt file not found at {novel_path}")
    sys.exit(1)
else:
    print(f"Found novel.txt at {novel_path}")

# Try with simplified pipeline first
print("Starting processing with small model...")
try:
    # Process with small model - simplified pipeline
    model_params = {"pipeline": "entity,quote", "model": "small"}
    print(model_params)
    booknlp_small = BookNLP("en", model_params)
    booknlp_small.process(novel_path, "output_small/novel_small")
    print("Small model processing complete.")

    # Verify output files exist
    time.sleep(2)  # Give time for file system
    if os.path.exists("output_small/novel_small.quotes"):
        print("Small model quotes file created successfully.")
    else:
        print("Warning: Small model quotes file was not created.")
        print("Files in output_small directory:")
        print(os.listdir("output_small"))
except Exception as e:
    print(f"Error processing with small model: {e}")

print("\nStarting processing with big model...")
try:
    # Process with big model - simplified pipeline
    model_params = {"pipeline": "entity,quote", "model": "big"}
    print(model_params)
    booknlp_big = BookNLP("en", model_params)
    booknlp_big.process(novel_path, "output_big/novel_big")
    print("Big model processing complete.")

    # Verify output files exist
    time.sleep(2)  # Give time for file system
    if os.path.exists("output_big/novel_big.quotes"):
        print("Big model quotes file created successfully.")
    else:
        print("Warning: Big model quotes file was not created.")
        print("Files in output_big directory:")
        print(os.listdir("output_big"))
except Exception as e:
    print(f"Error processing with big model: {e}")

# List all files in output directories to check what was actually created
print("\nFiles in output_small directory:")
print(os.listdir("output_small"))
print("\nFiles in output_big directory:")
print(os.listdir("output_big"))