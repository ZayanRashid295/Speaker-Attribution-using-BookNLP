from booknlp.booknlp import BookNLP
import os

# Create output directories
os.makedirs("output_small", exist_ok=True)
os.makedirs("output_big", exist_ok=True)

# Process with small model
model_params = {"pipeline":"entity,quote,supersense,event,coref", "model":"small"}
booknlp_small = BookNLP("en", model_params)
booknlp_small.process("novel.txt", "output_small/novel_small")

# Process with big model
model_params = {"pipeline":"entity,quote,supersense,event,coref", "model":"big"}
booknlp_big = BookNLP("en", model_params)
booknlp_big.process("novel.txt", "output_big/novel_big")