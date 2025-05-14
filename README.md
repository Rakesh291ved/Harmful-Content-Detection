# Harmful-Content-Detection
Harmful Content Detection
# 🛡️ Harmful Content Detection System

**AI-Powered Multi-Modal Content Filter**  
Detect harmful content from **text**, **images**, and **videos** using state-of-the-art transformer models.

---

## 🎯 Purpose

This project is designed to **automatically detect toxic or harmful content** in multimedia inputs. It leverages pre-trained deep learning models to analyze:

- 📝 Text for toxic language
- 🖼️ Images for NSFW/adult content
- 🎞️ Videos for violence, weapons, or other disturbing visuals

Built with **Flask** and **Transformers**, this API can be deployed to flag inappropriate or dangerous content in user-generated media on your platform.

---

## 🚀 Features

✅ **Text Classification** – Detects hate speech, offensive language, threats, etc.  
✅ **NSFW Image Detection** – Screens images for explicit or adult content.  
✅ **Violent Video Frame Detection** – Scans video frames for signs of violence, blood, weapons, etc.  
✅ **Real-time Feedback** – Get JSON results instantly with harmful content ratio.  
✅ **Lightweight REST API** – Easily integrate into any frontend or moderation system.

---

## 🧠 Models Used

| Task              | Model Name                                 | Description                                      |
|-------------------|---------------------------------------------|--------------------------------------------------|
| Text Toxicity     | `unitary/toxic-bert`                        | Detects toxic, obscene, identity-hate text       |
| Image NSFW        | `falconsai/nsfw_image_detection`            | Identifies NSFW elements in images               |
| Video Violence    | `facebook/deit-base-distilled-patch16-224` | Frame-by-frame violence and weapon detection     |

---

## 📂 Folder Structure

harmful-content-detector/
├── app.py # Flask API for text/image/video detection
├── analyze_video.py # Standalone video analysis script
├── uploads/ # Uploaded files stored here
├── index.html # Optional front-end interface
└── README.md

yaml
Copy
Edit

---

## 🧪 How to Use

### 1️⃣ Start the Flask Server

```bash
python app.py
Server will run at http://localhost:5000.

2️⃣ API Endpoints
📝 Text Analysis
POST /analyze/text

Body: JSON { "text": "your text here" }

Returns: Toxicity labels and scores

🖼️ Image Analysis
POST /analyze/image

Form-Data: Key = image, Value = image file

Returns: NSFW prediction labels

🎞️ Video Analysis
POST /analyze/video

Form-Data: Key = video, Value = video file

Returns:

Harmful frames count

Total frames scanned

Ratio of harmful frames

Processing time

📊 Example Output (Video)
json
Copy
Edit
{
  "harmful_frames": 3,
  "total_frames": 100,
  "harmful_ratio": 0.03,
  "processing_time": 8.92
}
🔍 Sample Use Case
Platform Moderation: Automatically screen user uploads to detect and reject harmful content before it goes public.

Parental Control: Analyze media consumed by children for disturbing or explicit content.

🛠️ Requirements
Install dependencies:

bash
Copy
Edit
pip install flask transformers pillow opencv-python
Ensure your environment supports torch (CPU/GPU depending on performance needs).

🧪 Bonus Script: analyze_video.py
Run it independently to test video analysis:

bash
Copy
Edit
python analyze_video.py
It will output frame-wise analysis and alert when harmful content is found.

👨‍💻 Author
Built with 💻 and 🔍 by Vedanth
📫 LinkedIn | 🌐 Portfolio | 🧠 Passionate about AI + Safety

⚠️ Disclaimer
This project is for research and educational use only. It uses general-purpose models and may produce false positives/negatives. Always use human verification for critical moderation workflows.

📄 License
MIT License © 2025 Vedanth
Use responsibly and ethically.

yaml
Copy
Edit

---

Let me know if you'd like a **dark-themed web UI**, **Docker support**, or a **dashboard for moderation stats**.







