import requests
import json
from api_keys import weather_api_key
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = json.loads(response.text)
    if data["cod"] == "404":
        return "Sorry, I couldn't find the weather information for that location."
    else:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The current temperature in {city} is {temperature} degrees Celsius with {description}."

