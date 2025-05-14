from transformers import pipeline
from PIL import Image

# Load a pre-trained NSFW image classifier
image_classifier = pipeline("image-classification", model="deepai/nsfw-detector")

# Load an image
image_path = "image.png"  # Replace with your image path
image = Image.open(image_path)

# Run the classifier
result = image_classifier(image)

# Print results
print(result)  # [{'label': 'nsfw', 'score': 0.98}]
