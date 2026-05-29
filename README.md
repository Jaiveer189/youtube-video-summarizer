# 🎥 AI-Powered YouTube Video Summarizer

An end-to-end AI application that automatically downloads YouTube video audio, transcribes spoken content using OpenAI Whisper, and generates concise AI-powered summaries through Large Language Models (LLMs). Built with Streamlit for an interactive web-based user experience.

---

# 📌 Project Overview

This project was developed to automate the process of extracting meaningful insights from YouTube videos without manually watching full-length content.

The application performs the following pipeline:

1. Accepts a YouTube video URL
2. Downloads the audio stream using `yt-dlp`
3. Converts speech into text using `Whisper AI`
4. Sends the transcript to an LLM for summarization
5. Displays the final AI-generated summary inside a Streamlit web app

The project demonstrates practical implementation of:

* Generative AI
* Speech-to-Text systems
* AI summarization workflows
* Streamlit deployment
* API integrations
* Real-world debugging and dependency management

---

# 🚀 Features

* 🔗 YouTube URL input support
* 🎧 Automatic audio extraction from videos
* 🧠 AI-powered speech transcription using Whisper
* 📝 Intelligent summary generation using LLM APIs
* 🖼️ Video thumbnail preview
* ⚡ Interactive Streamlit interface
* ☁️ Deployment-ready architecture
* 🔒 Environment variable support for API security

---

# 🧠 Tech Stack

## Frontend

* Streamlit

## Backend / AI Pipeline

* Python
* OpenAI Whisper
* yt-dlp
* FFmpeg
* OpenRouter API

## LLM / NLP

* GPT-based language models via OpenRouter

---

# 🏗️ System Architecture

```text
User Input (YouTube URL)
            ↓
      yt-dlp Audio Download
            ↓
       FFmpeg Audio Processing
            ↓
    Whisper Speech-to-Text Model
            ↓
     Transcript Generation
            ↓
       LLM-based Summarization
            ↓
      Streamlit Web Interface
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
cd youtube-video-summarizer
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

---

# 📦 Dependencies

Main libraries used:

* streamlit
* yt-dlp
* openai-whisper
* torch
* python-dotenv
* openai

---

# 🧩 Challenges Faced During Development

This project involved multiple real-world engineering challenges beyond just writing Python code.

## Major Challenges

### 1. YouTube Transcript API Instability

Initial implementation using YouTube transcript scraping frequently failed due to:

* API parsing issues
* Missing captions
* YouTube anti-bot restrictions
* Regional/network inconsistencies

### 2. FFmpeg Configuration

Whisper requires FFmpeg for audio processing, which required:

* Manual installation
* Environment variable setup
* PATH configuration debugging

### 3. API Compatibility Issues

Several SDK and model compatibility conflicts occurred involving:

* Gemini API versions
* Model endpoint changes
* LLM provider routing issues

### 4. Dependency Management

Managing compatibility between:

* Whisper
* Torch
* yt-dlp
* Streamlit
* OpenAI/OpenRouter SDKs

This project became a practical lesson in:

* debugging
* environment management
* dependency handling
* AI workflow orchestration

---

# 💡 Key Learnings

Through this project, I gained hands-on experience with:

* AI application development
* Speech-to-text pipelines
* LLM integrations
* Environment variable management
* Streamlit deployment workflows
* API debugging
* Dependency conflict resolution
* FFmpeg setup and configuration
* Real-world AI engineering challenges

---

# 📸 Demo

## LinkedIn Demo Video

Paste your LinkedIn post/demo URL here:

```text
YOUR_LINKEDIN_POST_URL
```

---

# 📂 Future Improvements

Potential upgrades planned:

* Multi-language summarization
* RAG-based contextual querying
* PDF export support
* Timestamp-based summaries
* Video chapter generation
* GPU acceleration
* Cloud deployment
* User authentication

---

# 👨‍💻 Author

## Jaiveer Shekhawat

Aspiring AI & Data Science Engineer passionate about:

* Artificial Intelligence
* Machine Learning
* NLP Systems
* Cloud Technologies
* AI Automation

---

# ⭐ Final Note

This project reflects not only AI implementation skills but also the practical engineering process required to debug, integrate, and deploy real-world AI systems under changing APIs and dependency ecosystems.
