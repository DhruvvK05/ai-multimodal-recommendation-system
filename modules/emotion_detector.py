from deepface import DeepFace
import cv2

def detect_emotion(frame):

    frame = cv2.resize(frame, (480,360))

    result = DeepFace.analyze(
        img_path=frame,
        actions=['emotion'],
        detector_backend="opencv",
        enforce_detection=False
    )

    emotion = result[0]["dominant_emotion"]
    score = result[0]["emotion"][emotion]

    return emotion.lower(), round(score,2)