import pandas as pd
import os

# Load ground truth data
ground_truth = pd.read_csv("../input/quote_info.csv")


# Function to load quotes from BookNLP output
def load_quotes(file_path):
    quotes = pd.read_csv(file_path, delimiter="\t")
    return quotes


# Load small and big model results
small_quotes = load_quotes("output_small/novel_small.quotes")
big_quotes = load_quotes("output_big/novel_big.quotes")


# Compare with ground truth
# This is a simplified version - you'll need to adapt this to match how your data is structured
def compare_attribution(model_quotes, ground_truth):
    correct = 0
    total = 0
    errors = []

    # Map between quotes and speakers in both datasets
    # This matching logic will depend on how quotes are represented in both datasets
    for _, gt_row in ground_truth.iterrows():
        total += 1
        matched = False

        for _, model_row in model_quotes.iterrows():
            # Match quotes by text content, start/end tokens or other reliable identifiers
            if (gt_row['quote_text'] == model_row['quote_text'] or
                    (gt_row['start_token'] == model_row['start_token'] and gt_row['end_token'] == model_row[
                        'end_token'])):

                if gt_row['speaker'] == model_row['char_id']:  # Or however speaker is identified
                    correct += 1
                    matched = True
                else:
                    errors.append({
                        'quote': gt_row['quote_text'],
                        'true_speaker': gt_row['speaker'],
                        'predicted_speaker': model_row['char_id']
                    })
                    matched = True
                break

        if not matched:
            errors.append({
                'quote': gt_row['quote_text'],
                'true_speaker': gt_row['speaker'],
                'predicted_speaker': 'Not found'
            })

    accuracy = correct / total if total > 0 else 0
    return accuracy, errors


# Calculate accuracy for both models
small_accuracy, small_errors = compare_attribution(small_quotes, ground_truth)
big_accuracy, big_errors = compare_attribution(big_quotes, ground_truth)

print(f"Small model accuracy: {small_accuracy:.2%}")
print(f"Big model accuracy: {big_accuracy:.2%}")