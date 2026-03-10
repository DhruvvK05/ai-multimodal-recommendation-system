import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tkinter as tk
import cv2
import webbrowser
from PIL import Image, ImageTk
from datetime import datetime

import yt_dlp

from modules.emotion_detector import detect_emotion
from modules.weather import get_weather
from modules.music_recommender import get_song_recommendation
from modules.llm_chain import get_ai_recommendation


cap = cv2.VideoCapture(0)

video_running = False
current_frame = None


# ---------------- TIME FUNCTION ----------------

def get_time_of_day():

    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Morning"

    elif 12 <= hour < 17:
        return "Afternoon"

    elif 17 <= hour < 21:
        return "Evening"

    else:
        return "Night"


# ---------------- YOUTUBE AUTO PLAY ----------------

def play_youtube(song):

    query = f"{song} song"

    ydl_opts = {
        'quiet': True,
        'extract_flat': True
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(f"ytsearch:{query}", download=False)

            video_id = info['entries'][0]['id']

            url = f"https://www.youtube.com/watch?v={video_id}"

            webbrowser.open(url)

    except Exception as e:

        print("YouTube error:", e)

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={song}"
        )


# ---------------- CAMERA FUNCTIONS ----------------

def start_video():

    global video_running

    if not video_running:
        video_running = True
        update_frame()


def stop_video():

    global video_running
    video_running = False


def update_frame():

    global current_frame

    if video_running:

        ret, frame = cap.read()

        if ret:

            current_frame = frame.copy()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            img = Image.fromarray(cv2image)

            imgtk = ImageTk.PhotoImage(image=img)

            video_frame.imgtk = imgtk
            video_frame.configure(image=imgtk)

        video_frame.after(10, update_frame)

    else:
        video_frame.after(100, update_frame)


# ---------------- EMOTION ----------------

def capture_emotion():

    if current_frame is None:
        emotion_label.config(text="Emotion: No frame")
        return

    try:

        emotion, score = detect_emotion(current_frame)

        emotion_label.config(text=f"Emotion: {emotion} ({score}%)")

    except Exception as e:

        emotion_label.config(text="Emotion: Error")
        print(e)


# ---------------- WEATHER ----------------

def get_city_weather():

    city = city_entry.get()

    if not city:

        weather_label.config(text="Weather: Enter city")
        return

    weather = get_weather(city)

    weather_label.config(text="Weather: " + weather)




def recommend_and_play():

    weather_text = weather_label.cget("text")
    emotion_text = emotion_label.cget("text")

    if ":" not in weather_text or ":" not in emotion_text:

        song_label.config(text="Song: Detect emotion and weather first")
        return

    weather = weather_text.split(": ")[1]

    emotion = emotion_text.split(": ")[1].split(" ")[0]

    # SONG RECOMMENDATION

    song = get_song_recommendation(weather, emotion)

    song_label.config(text="Song: " + song)

    play_youtube(song)

    # AI SUGGESTIONS

    try:

        ai_response = get_ai_recommendation(emotion, weather)

        ai_label.config(text=ai_response)

    except Exception as e:

        ai_label.config(text="AI suggestion unavailable")
        print(e)


# ---------------- UI ----------------

root = tk.Tk()

root.title("Moodify: AI Mood Recommendation System")


start_button = tk.Button(root, text="Start Camera", command=start_video)
start_button.pack()

stop_button = tk.Button(root, text="Stop Camera", command=stop_video)
stop_button.pack()

detect_button = tk.Button(root, text="Detect Emotion", command=capture_emotion)
detect_button.pack()

city_entry = tk.Entry(root)
city_entry.pack()

weather_button = tk.Button(root, text="Get Weather", command=get_city_weather)
weather_button.pack()

recommend_button = tk.Button(root, text="Recommend", command=recommend_and_play)
recommend_button.pack()


emotion_label = tk.Label(root, text="Emotion:")
emotion_label.pack()

weather_label = tk.Label(root, text="Weather:")
weather_label.pack()

song_label = tk.Label(root, text="Song:")
song_label.pack()


ai_label = tk.Label(
    root,
    text="AI Suggestions:",
    wraplength=400,
    justify="left"
)

ai_label.pack()


video_frame = tk.Label(root)
video_frame.pack()


root.mainloop()