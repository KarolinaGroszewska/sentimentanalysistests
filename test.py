from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("bot")[0]
print(result["score"])
