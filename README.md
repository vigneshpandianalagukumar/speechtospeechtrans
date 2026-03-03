 Fully Offline English-to-Hindi Speech-to-Speech Translator

🚀 Overview

This project implements a real-time, fully offline English-to-Hindi speech translation system that runs entirely on a laptop without any internet connection.
The system captures English speech from the microphone, transcribes it locally, translates it using a quantized LLaMA model, and generates Hindi speech output — all processed on-device.

No cloud APIs.
No external services.
No internet required.


🎯 Problem Statement

Most speech translation systems today rely on cloud-based APIs.
This introduces several limitations:

🔒 Privacy concerns (audio sent to external servers)

🌐 Dependency on internet connectivity

💰 API usage costs

📡 Latency due to network delays

There is a growing need for privacy-first, offline AI systems that can operate in:

Low-connectivity environments

Edge devices

Secure environments

Rural or remote areas

This project demonstrates a complete offline alternative using open-source models.


🧠 Solution Architecture

The system uses a modular on-device AI pipeline:

Microphone
   ↓
Vosk (Offline ASR)
   ↓
LLaMA (Local English → Hindi Translation)
   ↓
Silero Indic TTS
   ↓
Speaker Output
🔹 Step 1 – Speech Recognition (ASR)

Uses Vosk for real-time offline English speech recognition.

Streaming-based recognition.

No cloud dependency.

🔹 Step 2 – Translation

Uses a quantized LLaMA GGUF model.

Runs locally via llama-cpp-python.

Translates recognized English text into natural Hindi.

🔹 Step 3 – Text-to-Speech (TTS)

Uses Silero Indic TTS.

Converts translated Hindi text into speech.

Outputs Hindi audio in real time.

✨ Key Features

✅ Fully Offline Processing
✅ Real-Time Streaming ASR
✅ Quantized LLM for Lightweight Deployment
✅ Low Latency (~1–2 seconds end-to-end)
✅ Privacy-First Architecture
✅ No External APIs
✅ Runs on Standard Laptop CPU


⚙️ Tech Stack

Python
Vosk – Offline Speech Recognition
LLaMA (GGUF format) – Local Translation Model
llama-cpp-python
Silero Indic TTS
PyTorch
sounddevice
NumPy

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/offline-speech-translation-laptop.git
cd offline-speech-translation-laptop
2️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Running the Project
python src/main.py

Then:

Speak in English.
The system will respond in Hindi speech.

Press Ctrl + C to stop.


📁 Models

Due to GitHub file size limits, model files are not included.

You need to download:

Vosk English Model

LLaMA GGUF Model

Silero TTS Model (auto-downloads on first run)

Place models inside the models/ directory.

🚀 Performance

End-to-End Latency: ~1–2 seconds
Runs fully offline
optimized for CPU-based inference
Designed for edge AI scenarios


🎯 Use Cases

Offline voice assistants
Privacy-focused AI systems
Edge AI deployments
Rural or low-connectivity environments
Secure environments (no cloud allowed)
Research and hackathon prototypes


🔮 Future Improvements

Add multilingual support
Improve noise robustness
Optimize latency further
Deploy to ARM-based devices
Add GUI interface
Add speaker diarization


📊 Why This Project Matters

This project demonstrates that:
Powerful AI systems can run fully offline using optimized open-source models.
It showcases the feasibility of building:
Private AI assistants
Low-cost edge AI translators
Internet-independent AI systems
This approach is highly relevant for next-generation edge computing.


👨‍💻 Author

Vignesh Pandian
B.E Electronics and Communication
Chennai Institute of Technology

📜 License

This project is for educational and hackathon demonstration purposes.
