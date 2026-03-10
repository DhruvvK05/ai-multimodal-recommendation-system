import requests
import random

API_KEY = "6ca208f9"


movie_keywords = {
    "happy": ["comedy", "fun", "feel good"],
    "sad": ["drama", "inspirational"],
    "angry": ["action", "revenge"],
    "fear": ["thriller", "mystery"],
    "surprise": ["adventure", "fantasy"],
    "neutral": ["popular", "movie"]
}


def get_movie_by_emotion(emotion):

    keyword = random.choice(movie_keywords.get(emotion, ["movie"]))

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={keyword}&type=movie"

    response = requests.get(url)

    data = response.json()

    if "Search" in data:

        movie = random.choice(data["Search"])

        title = movie["Title"]
        year = movie["Year"]
        poster = movie["Poster"]

        return title, year, poster

    return "Movie not found", "", ""