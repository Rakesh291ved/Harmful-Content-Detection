from transformers import pipeline

model = pipeline("text-classification", model="GroNLP/hateBERT")
text = "I hate you!"
result = model(text)
print(result)
