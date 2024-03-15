# Use a pipeline as a high-level helper
from transformers import pipeline

# model_path = ("../../Models/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english/snapshots"
#               "/714eb0fa89d2f80546fda750413ed43d93601a13")
#
# pipe = pipeline("text-classification", model=model_path)
# print(pipe(["You are the worst"]))

# classifier = pipeline("sentiment-analysis", model="michellejieli/NSFW_text_classifier")
# classifier("I see you’ve set aside this special time to humiliate yourself in public.")

# Load model directly
