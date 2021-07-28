from transformers import pipeline
import tensorflow

classifier = pipeline("sentiment-analysis")
result = classifier("bot")[0]
print(result["label"] + ": " + str(result["score"]))
