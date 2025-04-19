import pandas as pd
import os
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

print("Speaker Attribution Analysis Script")
print("----------------------------------")

# Load ground truth data
ground_truth = pd.read_csv("input/quote_info.csv")
print(f"Loaded ground truth with {len(ground_truth)} quotes")

# Load model outputs
small_model = pd.read_csv("output_small/novel_small.quotes", sep="\t")
print(f"Loaded small model output with {len(small_model)} quotes")

big_model = pd.read_csv("output_big/novel_big.quotes", sep="\t")
print(f"Loaded big model output with {len(big_model)} quotes")


# Calculate accuracy
def calculate_accuracy(model, ground_truth):
    correct = sum(model["char_id"] == ground_truth["char_id"])
    total = len(ground_truth)
    return correct / total


small_accuracy = calculate_accuracy(small_model, ground_truth)
big_accuracy = calculate_accuracy(big_model, ground_truth)

print(f"\nAccuracy Results:")
print(f"Small model accuracy: {small_accuracy:.2%}")
print(f"Big model accuracy: {big_accuracy:.2%}")


# Find misattributions
def find_errors(model, ground_truth):
    errors = []
    for i, (_, gt_row) in enumerate(ground_truth.iterrows()):
        model_row = model.iloc[i]
        if gt_row["char_id"] != model_row["char_id"]:
            errors.append({
                "quote_id": gt_row["quote_id"],
                "quote_text": gt_row["quote_text"],
                "true_speaker": gt_row["speaker"],
                "predicted_speaker": model_row["speaker"],
                "true_id": gt_row["char_id"],
                "predicted_id": model_row["char_id"]
            })
    return errors


small_errors = find_errors(small_model, ground_truth)
big_errors = find_errors(big_model, ground_truth)

print(f"\nSmall Model Errors ({len(small_errors)}):")
for error in small_errors:
    print(f"Quote {error['quote_id']}: {error['quote_text']}")
    print(f"  True speaker: {error['true_speaker']}")
    print(f"  Predicted: {error['predicted_speaker']}")
    print()

print(f"\nBig Model Errors ({len(big_errors)}):")
for error in big_errors:
    print(f"Quote {error['quote_id']}: {error['quote_text']}")
    print(f"  True speaker: {error['true_speaker']}")
    print(f"  Predicted: {error['predicted_speaker']}")
    print()

# Error analysis by speaker
speakers = ground_truth["speaker"].unique()
print("\nError Analysis by Speaker:")
for speaker in speakers:
    speaker_quotes = ground_truth[ground_truth["speaker"] == speaker]
    small_speaker_errors = sum(small_model.iloc[speaker_quotes.index]["speaker"] != speaker)
    big_speaker_errors = sum(big_model.iloc[speaker_quotes.index]["speaker"] != speaker)

    total = len(speaker_quotes)
    print(f"{speaker}: {total} quotes")
    print(f"  Small model errors: {small_speaker_errors}/{total} ({small_speaker_errors / total:.2%})")
    print(f"  Big model errors: {big_speaker_errors}/{total} ({big_speaker_errors / total:.2%})")

print("\nAnalysis complete!")