import os
import warnings


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



st.sidebar.title("🎧 Moodify AI")

st.sidebar.markdown("""
AI powered mood recommendation system

**Inputs**
- Emotion detection
- Weather API

**Outputs**
- Song recommendation
- Movie suggestion
- Activity suggestion
""")

st.sidebar.info("Capture emotion and enter city to start.")



st.title("🎧 Moodify – AI Mood Recommendation System")

st.markdown("---")




@st.cache_data
def cached_ai(emotion, weather):
    return get_ai_recommendation(emotion, weather)




st.subheader("📷 Emotion Detection")

camera = st.camera_input("Capture your emotion")

emotion = None
weather = None

if camera is not None:

    file_bytes = camera.getvalue()

    np_image = np.frombuffer(file_bytes, np.uint8)

    img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    # convert to correct color format for DeepFace
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    emotion, score = detect_emotion(frame)

    st.success(f"Emotion detected: **{emotion} ({score}%)**")




st.subheader("🌍 Weather")

city = st.text_input("Enter your city")

if city:

    weather = get_weather(city)

    st.info(f"Current weather: **{weather}**")


st.markdown("---")




if st.button("🎯 Generate Recommendations"):

    if emotion and weather:

        

        with st.spinner("AI generating suggestions..."):

            try:

                ai_response = cached_ai(emotion, weather)

                st.subheader("🤖 AI Suggestions")

                st.write(ai_response)

            except:

                st.warning("AI suggestion unavailable")


       

        song = get_song_recommendation(weather, emotion)

        st.subheader("🎵 Song Recommendation")

        st.success(song)

        st.session_state.song = song

    else:

        st.warning("Please detect emotion and weather first")




if "song" in st.session_state:

    if st.button("▶ Play on YouTube"):

        youtube_url = f"https://www.youtube.com/results?search_query={st.session_state.song}"

        webbrowser.open(youtube_url)