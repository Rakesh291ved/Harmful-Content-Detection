from transformers import pipeline

model = pipeline("text-classification", model="unitary/toxic-bert")
text = "Vaccines help prevent diseases and save lives."
print(model(text))
