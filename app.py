import os
import warnings

# Hide TensorFlow logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
warnings.filterwarnings("ignore")

import streamlit as st
import cv2
import numpy as np
import webbrowser

from modules.emotion_detector import detect_emotion
from modules.weather import get_weather
from modules.music_recommender import get_song_recommendation
from modules.llm_chain import get_ai_recommendation


st.set_page_config(page_title="Moodify AI", layout="centered")


# ---------------- SIDEBAR ----------------

st.sidebar.title("🎧 Moodify AI")

st.sidebar.markdown("""
AI Multimodal Recommendation System

Inputs:
• Facial Emotion  
• Weather  
• Time Context  
• User Goal  
• Energy Level  

Outputs:
• Movie Suggestion  
• Activity Suggestion  
• Music Recommendation
""")

st.sidebar.info("Capture emotion and enter city to start.")


# ---------------- TITLE ----------------

st.title("🎧 Moodify – AI Multimodal Recommendation System")

st.markdown("---")


# ---------------- CACHE AI ----------------

@st.cache_data
def cached_ai(emotion, weather, time_of_day, mood_goal, energy_level):
    return get_ai_recommendation(
        emotion,
        weather,
        time_of_day,
        mood_goal,
        energy_level
    )


# ---------------- EMOTION DETECTION ----------------

st.subheader("📷 Emotion Detection")

camera = st.camera_input("Capture your emotion")

emotion = None
weather = None

if camera is not None:

    file_bytes = camera.getvalue()

    np_image = np.frombuffer(file_bytes, np.uint8)

    frame = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    emotion, score = detect_emotion(frame)

    st.success(f"Emotion detected: **{emotion} ({score}%)**")

# ---------------- WEATHER ----------------

st.subheader("🌍 Weather")

city = st.text_input("Enter your city")

if city:
    weather = get_weather(city)
    st.info(f"Current weather: **{weather}**")


# ---------------- ADDITIONAL CONTEXT ----------------

st.subheader("🧠 Additional Context")

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

mood_goal = st.selectbox(
    "What do you want?",
    ["Relax", "Motivation", "Entertainment", "Focus"]
)

energy_level = st.slider(
    "Energy Level",
    1, 10, 5
)

st.markdown("---")


# ---------------- GENERATE RECOMMENDATIONS ----------------

if st.button("🎯 Generate Recommendations"):

    if emotion and weather:

        # -------- SHOW CONTEXT --------

        st.markdown("### 🧠 Context Used by AI")

        context_data = {
            "Emotion": emotion,
            "Weather": weather,
            "Time of Day": time_of_day,
            "Goal": mood_goal,
            "Energy Level": f"{energy_level}/10"
        }

        st.table(context_data)


        # -------- AI SUGGESTIONS --------

        with st.spinner("AI generating suggestions..."):

            try:

                ai_response = cached_ai(
                    emotion,
                    weather,
                    time_of_day,
                    mood_goal,
                    energy_level
                )

                st.markdown("### 🤖 AI Suggestions")

                st.write(ai_response)

            except:

                st.warning("AI suggestion unavailable")


        # -------- SONG RECOMMENDATION --------

        song = get_song_recommendation(weather, emotion)

        st.markdown("### 🎵 Song Recommendation")

        st.success(song)

        st.session_state.song = song

    else:

        st.warning("Please detect emotion and weather first")


# ---------------- YOUTUBE BUTTON ----------------

if "song" in st.session_state:

    if st.button("▶ Play on YouTube"):

        youtube_url = f"https://www.youtube.com/results?search_query={st.session_state.song}"

        webbrowser.open(youtube_url)