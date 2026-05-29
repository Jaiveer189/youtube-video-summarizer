import os
import streamlit as st
from dotenv import load_dotenv
import yt_dlp
import whisper

from openai import OpenAI

# =========================
# LOAD ENV
# =========================

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

if not OPENROUTER_API_KEY:

    st.error(
        "OpenRouter API Key not found!"
    )

    st.stop()

# =========================
# OPENROUTER CLIENT
# =========================

client = OpenAI(

    api_key=OPENROUTER_API_KEY,

    base_url="https://openrouter.ai/api/v1"
)

# =========================
# LOAD WHISPER MODEL
# =========================

model_whisper = whisper.load_model(
    "tiny"
)

# =========================
# PROMPT
# =========================

prompt = """
Summarize this YouTube video transcript
in simple bullet points within 200 words.
"""

# =========================
# DOWNLOAD AUDIO
# =========================

def download_audio(url):

    ydl_opts = {

        'format': 'bestaudio/best',

        'outtmpl': 'audio.%(ext)s',

        'quiet': True,
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        info = ydl.extract_info(
            url,
            download=True
        )

        filename = ydl.prepare_filename(
            info
        )

        return filename

# =========================
# TRANSCRIBE AUDIO
# =========================

def transcribe_audio(audio_path):

    result = model_whisper.transcribe(
        audio_path
    )

    return result["text"]

# =========================
# GENERATE SUMMARY
# =========================

def generate_summary(transcript):

    response = client.chat.completions.create(

        model="openai/gpt-3.5-turbo",

        messages=[

            {
                "role": "user",

                "content":
                prompt + "\n\n" + transcript
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )

# =========================
# STREAMLIT UI
# =========================

st.title(
    "YouTube Video Summarizer"
)

youtube_url = st.text_input(
    "Enter YouTube URL"
)

# Thumbnail
if youtube_url:

    try:

        video_id = (
            youtube_url
            .split("v=")[-1]
            .split("&")[0]
        )

        st.image(
            f"https://img.youtube.com/vi/{video_id}/0.jpg",
            use_container_width=True
        )

    except:
        pass

# =========================
# GENERATE SUMMARY BUTTON
# =========================

if st.button("Generate Summary"):

    if not youtube_url:

        st.warning(
            "Please enter a YouTube URL"
        )

    else:

        try:

            with st.spinner(
                "Downloading audio..."
            ):

                audio_file = download_audio(
                    youtube_url
                )

            with st.spinner(
                "Transcribing audio..."
            ):

                transcript = (
                    transcribe_audio(
                        audio_file
                    )
                )

            with st.spinner(
                "Generating summary..."
            ):

                summary = (
                    generate_summary(
                        transcript
                    )
                )

            st.markdown(
                "## Summary"
            )

            st.write(summary)

        except Exception as e:

            st.error(f"Error: {e}")