from deepface import DeepFace

def detect_emotion(frame):

    try:

        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        emotion = result[0]["dominant_emotion"]

        score = round(result[0]["emotion"][emotion], 2)

        return emotion, score

    except:

        return "neutral", 0