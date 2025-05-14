import cv2
import numpy as np
import time
from PIL import Image
from transformers import pipeline

# Load a better model for detecting harmful content
image_classifier = pipeline("image-classification", model="falconsai/nsfw_image_detection")

# Expanded list of labels related to fighting
VIOLENCE_LABELS = ["violent", "weapon", "gun", "blood", "fighting", "punch", "attack", "explosion", "knife"]

def analyze_video(video_path, frame_skip=10):
    """Analyzes a video to detect harmful content like NSFW or violence."""
    start_time = time.time()
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return {"error": "Could not open video file."}

    harmful_frames = 0
    total_frames = 0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"Total frames in video: {frame_count}")
    print("Processing video...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Exit when the video ends

        if total_frames % frame_skip == 0:
            # Convert frame to PIL Image and resize
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img = img.resize((224, 224))  # Resize to match model input size

            # Get classification result
            result = image_classifier(img)

            # Check for harmful content
            for r in result:
                label = r['label'].lower()
                if any(violence_label in label for violence_label in VIOLENCE_LABELS):
                    harmful_frames += 1
                    print(f"[ALERT] Harmful content detected at frame {total_frames}: {label}")
                    break  # Stop checking once harmful content is found

        total_frames += 1

        # Display progress every 50 frames
        if total_frames % 50 == 0:
            progress = (total_frames / frame_count) * 100
            print(f"Processing... {progress:.2f}% done")

    cap.release()  # Release video file
    duration = round(time.time() - start_time, 2)

    print(f"Analysis Complete! Harmful Frames: {harmful_frames}/{total_frames}")
    return {
        "total_frames": total_frames,
        "harmful_frames": harmful_frames,
        "harmful_ratio": harmful_frames / total_frames if total_frames > 0 else 0,
        "processing_time_seconds": duration
    }

# Example usage
if __name__ == "__main__":
    video_file = "sample1.mp4"  # Change this to your video file name
    result = analyze_video(video_file, frame_skip=10)  # Lower frame skip for better detection
    print("Final Video Analysis Result:", result)
