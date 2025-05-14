from transformers import pipeline
model = pipeline("text-generation", model="bigscience/bloom-560m")

prompt = "Explain why cyberbullying is harmful."
result = model(prompt, max_length=50)
print(result)
          