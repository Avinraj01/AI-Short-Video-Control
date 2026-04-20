# 🚀 NeuroReel AI

> Control YouTube Shorts **hands-free** using eye blinks and head movements — with AI emotion tracking, OCR-based genre detection, and a smart analytics dashboard.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red)

---

## 🧠 How It Works

| Gesture | Action |
|---|---|
| 👁️ Eye Blink | Pause / Play |
| 👤 Head Movement | Scroll to next Short |
| 😊 Emotion Detection | Mood analysis & tracking |
| 📊 Dashboard | View your watching analytics |

---

## 🛠 Tech Stack

- **Python** — core language
- **OpenCV** — real-time video capture and processing
- **MediaPipe** — face landmark detection for blink & head tracking
- **Transformers (HuggingFace)** — emotion recognition model
- **Tesseract OCR** — genre detection from video text
- **Flask** — analytics dashboard backend
- **DeepFace** — face analysis

---

## 🎯 Features

- ✅ Hands-free YouTube Shorts control
- ✅ Real-time emotion tracking
- ✅ Genre detection via OCR
- ✅ Interactive analytics dashboard
- ✅ Modular design — each module runs independently

---

## ⚙️ Installation

### Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
- Webcam

### Setup

```bash
# Clone the repository
git clone https://github.com/Avinraj01/neuroreel-ai.git
cd neuroreel-ai

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python app.py
```

The app will start capturing from your webcam and open the analytics dashboard at `http://localhost:5000`.

---

## 📁 Project Structure

```
neuroreel-ai/
├── app.py          # Main entry point
├── blink.py        # Eye blink detection module
├── head.py         # Head movement tracking module
├── genre_ocr.py    # OCR-based genre detection
├── tracker.py      # Session & interaction tracker
├── analytics.py    # Dashboard and analytics backend
└── requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.
