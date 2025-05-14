from transformers import pipeline

# Load the model from Hugging Face
classifier = pipeline("text-classification", model="unitary/toxic-bert")

# Test the model
text = "I hate you so much!"
result = classifier(text)

print(result)  # [{'label': 'toxic', 'score': 0.99}]
