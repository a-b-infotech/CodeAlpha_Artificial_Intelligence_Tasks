# CodeAlpha — Artificial Intelligence Internship Tasks Repository

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Internship-blueviolet.svg)](https://www.codealpha.tech)
[![Domain](https://img.shields.io/badge/Domain-Artificial%20Intelligence-orange.svg)](#)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

This repository contains the complete, production-ready source code, documentation, and architecture for all projects completed as part of the **CodeAlpha Artificial Intelligence Internship**.

---

## 📋 Table of Contents

| Task | Title | Tech Stack | Repository / Directory |
| :---: | :--- | :--- | :--- |
| **01** | [Language Translation Tool](./Task1_Language_Translation_Tool) | Streamlit, Deep-Translator, gTTS | [Explore Task 1](./Task1_Language_Translation_Tool) |
| **02** | [Intelligent FAQ Chatbot](./Task2_FAQ_Chatbot) | NLTK, TF-IDF, Cosine Similarity, Streamlit | [Explore Task 2](./Task2_FAQ_Chatbot) |
| **03** | [Music Generation with Deep Learning](./Task3_Music_Generation_AI) | PyTorch, LSTM, music21, MIDI | [Explore Task 3](./Task3_Music_Generation_AI) |
| **04** | [Real-Time Object Detection & Tracking](./Task4_Object_Detection_Tracking) | YOLOv8n, ByteTrack, OpenCV | [Explore Task 4](./Task4_Object_Detection_Tracking) |

---

## 🌟 Tasks Summary

### ✅ Task 1: Language Translation Tool
- **Overview**: Real-time neural machine translation application supporting 20+ global languages.
- **Key Highlights**:
  - Auto-detection of source languages.
  - Interactive language swapping with modern UI.
  - **Text-to-Speech (TTS)**: Native audio playback of translated text.
  - Copy-to-clipboard functionality & `.txt` export.
- **Run**: `cd Task1_Language_Translation_Tool && streamlit run app.py`

### ✅ Task 2: Intelligent FAQ Chatbot
- **Overview**: NLP-driven conversational assistant answering queries regarding the CodeAlpha internship program, submission guidelines, and technical architectures.
- **Key Highlights**:
  - Full NLP preprocessing pipeline (Tokenization, Stopwords removal, WordNet Lemmatization).
  - TF-IDF Vectorization & Cosine Similarity matching with confidence percentages.
  - Graceful fallback for queries outside the knowledge base.
  - Interactive chat interface with clickable suggestion chips.
- **Run**: `cd Task2_FAQ_Chatbot && streamlit run app.py`

### ✅ Task 3: Music Generation with AI
- **Overview**: Deep learning sequence model that composes original polyphonic music based on learned musical pitch and chord patterns.
- **Key Highlights**:
  - MIDI parsing and feature extraction using MIT's `music21`.
  - 2-Layer PyTorch LSTM architecture with recurrent dropout.
  - Temperature-controlled creative sampling.
  - Built-in automatic motif generation and `.mid` export.
- **Run**: `cd Task3_Music_Generation_AI && python train_and_generate.py`

### ✅ Task 4: Real-Time Object Detection and Tracking
- **Overview**: High-performance computer vision system for real-time bounding box detection and multi-object tracking.
- **Key Highlights**:
  - Ultralytics YOLOv8 (Nano) deep learning model for real-time inference.
  - Native ByteTrack multi-object tracker for persistent ID tracking across frames.
  - Continuous motion trajectory trail rendering.
  - HUD overlay with live FPS, active track count, and class stats.
- **Run**: `cd Task4_Object_Detection_Tracking && python tracker.py --source 0`

---

## ⚙️ Installation & Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/a-b-infotech/CodeAlpha_Artificial_Intelligence_Tasks.git
   cd CodeAlpha_Artificial_Intelligence_Tasks
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install all dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 👨‍💻 Intern Information

- **Name**: Abhi B Sheth
- **Domain**: Artificial Intelligence
- **Email**: shethabhi11@gmail.com
- **GitHub**: [@a-b-infotech](https://github.com/a-b-infotech)
- **Organization**: [CodeAlpha](https://www.codealpha.tech)
