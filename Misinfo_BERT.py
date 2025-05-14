from transformers import pipeline

# Alternative model that works for text classification
model = pipeline("text-classification", model="facebook/bart-large-mnli")

news = "The earth is flat."
print(model(news))
