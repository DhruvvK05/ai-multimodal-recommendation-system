import requests

API_KEY = "4b493dce853e42e39a7164458260903"


def get_weather(city_name):

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}"

    response = requests.get(url)

    data = response.json()

    if "current" in data:

        weather_text = data["current"]["condition"]["text"].lower()

        if "rain" in weather_text:
            return "Rain"

        if "cloud" in weather_text:
            return "Clouds"

        if "mist" in weather_text:
            return "Mist"

        if "fog" in weather_text:
            return "Fog"

        if "haze" in weather_text:
            return "Haze"

        return "Clear"

    return "Unknown"