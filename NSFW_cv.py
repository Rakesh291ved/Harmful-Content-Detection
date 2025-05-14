import onnxruntime as ort
from PIL import Image
import numpy as np

session = ort.InferenceSession("nsfw_model.onnx")

def preprocess(image_path):
    image = Image.open(image_path).resize((224, 224))
    return np.array(image).astype(np.float32) / 255.0

image_path = "image.png"
input_data = preprocess(image_path)
result = session.run(None, {"input": input_data[None, :, :, :]})

print("NSFW Score:", result)
