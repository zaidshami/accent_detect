# 🎙️ English Accent Classification from Video URL

A smart AI-powered tool that classifies the **English accent** of a speaker in a video. Just provide a public video URL (e.g., Loom or MP4), and get the predicted accent, confidence score, and summary.

## 🚀 Features

1. **Accept Public Video URLs**  
   Easily provide links such as Loom recordings or direct `.mp4` URLs.

2. **Audio Extraction**  
   Automatically extracts and preprocesses the audio from the video input.

3. **Accent Classification using Deep Learning**  
   - Detects speaker’s English accent: `British`, `American`,  `Indian`, etc.
   - Returns a confidence score between `0-100%` for how fluent and natural the English sounds.
   - Optionally provides a short explanation or summary.

---

## 🧠 How It Works

### 🔍 Model Training
- Built using **TensorFlow** and **deep learning**.
- Applied **MFCC (Mel Frequency Cepstral Coefficients)** for feature extraction.
- Performed extensive **feature engineering** and used multiple datasets to build a robust model.
- You can review the full training and dataset exploration in the following Kaggle notebook:  
  👉 [Kaggle Notebook](https://www.kaggle.com/code/zaidali11/accent-classification-ann)

### ⚠️ Accuracy Note
> This model was built as part of a task with a focus on functionality and pipeline integration more than high accuracy.  

### 🧑‍💻 Tech Stack
- **LangChain**: Orchestrates the AI agent logic and tools.
- **Streamlit**: Provides an intuitive user interface for interaction and testing.
- **Tensorflow**: Deep learning.
- **Python**: Core implementation language.

---

## 🌐 Live Demo

You can try the app now using Streamlit:

👉 [Open the App on Streamlit](https://accentdetect-tvdz6fpuplzdbxekwdpvdd.streamlit.app/)

> Please ensure your video URL is public and accessible.

---

