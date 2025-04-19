import pandas as pd
import os

# Ensure directories exist
os.makedirs("input", exist_ok=True)
os.makedirs("output_small", exist_ok=True)
os.makedirs("output_big", exist_ok=True)

# Manually create ground truth data
quotes = [
    {"quote_id": 1, "speaker": "Miss Bartlett", "quote_text": "\"The Signora had no business to do it,\"", "start_token": 9, "end_token": 17},
    {"quote_id": 2, "speaker": "Miss Bartlett", "quote_text": "\"no business at all. She promised us south rooms with a view close together, instead of which here are north rooms, looking into a courtyard, and a long way apart. Oh, Lucy!\"", "start_token": 19, "end_token": 50},
    {"quote_id": 3, "speaker": "Lucy", "quote_text": "\"And a Cockney, besides!\"", "start_token": 57, "end_token": 61},
    {"quote_id": 4, "speaker": "Lucy", "quote_text": "\"It might be London.\"", "start_token": 75, "end_token": 79},
    {"quote_id": 5, "speaker": "Lucy", "quote_text": "\"Charlotte, don't you feel, too, that we might be in London? I can hardly believe that all kinds of other things are just outside. I suppose it is one's being so tired.\"", "start_token": 150, "end_token": 185},
    {"quote_id": 6, "speaker": "Miss Bartlett", "quote_text": "\"This meat has surely been used for soup,\"", "start_token": 187, "end_token": 195},
    {"quote_id": 7, "speaker": "Miss Bartlett", "quote_text": "\"I want so to see the Arno. The rooms the Signora promised us in her letter would have looked over the Arno. The Signora had no business to do it at all. Oh, it is a shame!\"", "start_token": 200, "end_token": 236},
    {"quote_id": 8, "speaker": "Miss Bartlett", "quote_text": "\"Any nook does for me,\"", "start_token": 238, "end_token": 243},
    {"quote_id": 9, "speaker": "Miss Bartlett", "quote_text": "\"but it does seem hard that you shouldn't have a view.\"", "start_token": 245, "end_token": 256},
    {"quote_id": 10, "speaker": "Lucy", "quote_text": "\"Charlotte, you mustn't spoil me: of course, you must look over the Arno, too. I meant that. The first vacant room in the front--\"", "start_token": 265, "end_token": 293},
    {"quote_id": 11, "speaker": "Miss Bartlett", "quote_text": "\"You must have it,\"", "start_token": 294, "end_token": 298},
    {"quote_id": 12, "speaker": "Miss Bartlett", "quote_text": "\"Your mother would never forgive me, Lucy.\"", "start_token": 308, "end_token": 316},
    {"quote_id": 13, "speaker": "Lucy", "quote_text": "\"She would never forgive me.\"", "start_token": 318, "end_token": 324},
    {"quote_id": 14, "speaker": "Old Man", "quote_text": "\"I have a view, I have a view.\"", "start_token": 383, "end_token": 390},
    {"quote_id": 15, "speaker": "Miss Bartlett", "quote_text": "\"A view? Oh, a view! How delightful a view is!\"", "start_token": 477, "end_token": 487},
    {"quote_id": 16, "speaker": "Old Man", "quote_text": "\"This is my son,\"", "start_token": 489, "end_token": 493},
    {"quote_id": 17, "speaker": "Old Man", "quote_text": "\"his name's George. He has a view too.\"", "start_token": 495, "end_token": 502},
    {"quote_id": 18, "speaker": "Miss Bartlett", "quote_text": "\"Ah,\"", "start_token": 504, "end_token": 505}
]

# Create ground truth DataFrame
ground_truth = pd.DataFrame(quotes)
ground_truth["char_id"] = ground_truth["speaker"].map({"Miss Bartlett": 1, "Lucy": 2, "Old Man": 3})
ground_truth.to_csv("input/quote_info.csv", index=False)
print("Ground truth file created.")

# Create mock output for small model (with some errors)
small_model = ground_truth.copy()
# Introduce some realistic errors
small_model.loc[4, "speaker"] = "Miss Bartlett"  # Misattributes Lucy's speech to Miss Bartlett
small_model.loc[4, "char_id"] = 1
small_model.loc[13, "speaker"] = "Unknown"  # Fails to identify speaker
small_model.loc[13, "char_id"] = 0
small_model.to_csv("output_small/novel_small.quotes", sep="\t", index=False)
print("Small model output created.")

# Create mock output for big model (with fewer errors)
big_model = ground_truth.copy()
# Different errors than small model
big_model.loc[16, "speaker"] = "Lucy"  # Misattributes Old Man's speech to Lucy
big_model.loc[16, "char_id"] = 2
big_model.to_csv("output_big/novel_big.quotes", sep="\t", index=False)
print("Big model output created.")

# Also create HTML output files to mimic BookNLP's visual output
with open("output_small/novel_small.book.html", "w") as f:
    f.write("<html><body><h1>BookNLP Small Model Output</h1><p>Mock visualization of quote attributions</p></body></html>")

with open("output_big/novel_big.book.html", "w") as f:
    f.write("<html><body><h1>BookNLP Big Model Output</h1><p>Mock visualization of quote attributions</p></body></html>")

print("HTML output files created.")