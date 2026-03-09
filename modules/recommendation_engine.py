def get_recommendations(emotion, weather, time):

    recommendations = {

        "happy": {
            "music": "Ilahi",
            "movie": "Zindagi Na Milegi Dobara",
            "activity": "Go for a walk or meet friends"
        },

        "sad": {
            "music": "Tum Hi Ho",
            "movie": "The Pursuit of Happyness",
            "activity": "Listen to music and relax"
        },

        "angry": {
            "music": "Zinda",
            "movie": "Rocky",
            "activity": "Do a quick workout"
        },

        "neutral": {
            "music": "Kabira",
            "movie": "Forrest Gump",
            "activity": "Watch a movie or read"
        }

    }

    if emotion in recommendations:
        return recommendations[emotion]

    return {
        "music": "Ilahi",
        "movie": "Forrest Gump",
        "activity": "Relax"
    }