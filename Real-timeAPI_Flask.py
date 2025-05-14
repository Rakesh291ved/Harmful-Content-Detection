from flask import Flask, request, jsonify, send_from_directory
from transformers import pipeline
from PIL import Image
import os
import time
import cv2
import numpy as np

app = Flask(__name__, static_url_path='', static_folder='.')
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load models
text_model = pipeline("text-classification", model="unitary/toxic-bert")
image_model = pipeline("image-classification", model="falconsai/nsfw_image_detection")
video_model = pipeline("image-classification", model="facebook/deit-base-distilled-patch16-224")

@app.route('/')
def serve_ui():
    return send_from_directory('.', 'index.html')

@app.route('/analyze/text', methods=['POST'])
def analyze_text():
    text = request.json.get("text", "")
    result = text_model(text)
    return jsonify(result)

@app.route('/analyze/image', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file uploaded"}), 400

    image_file = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    image = Image.open(image_path)
    result = image_model(image)
    return jsonify(result)

@app.route('/analyze/video', methods=['POST'])
def analyze_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video file uploaded"}), 400

    video_file = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, video_file.filename)
    video_file.save(video_path)

    start_time = time.time()
    cap = cv2.VideoCapture(video_path)
    harmful_frames = 0
    total_frames = 0
    frame_skip = 30

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if total_frames % frame_skip == 0:
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            result = video_model(img)

            for r in result:
                label = r['label'].lower()
                if 'violent' in label or 'weapon' in label or 'nsfw' in label:
                    harmful_frames += 1
                    break

        total_frames += 1

    cap.release()
    duration = round(time.time() - start_time, 2)

    return jsonify({
        "harmful_frames": harmful_frames,
        "total_frames": total_frames,
        "harmful_ratio": harmful_frames / total_frames if total_frames > 0 else 0,
        "processing_time": duration
    })

if __name__ == '__main__':
    app.run(port=5000)
