# bot/services/weather_api.py
import requests

def get_forecast(city: str):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city, "count": 1, "language": "en", "format": "json"}
    geo = requests.get(geo_url, params=geo_params).json()
    if not geo.get("results"):
        return None

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto",
    }
    data = requests.get(weather_url, params=weather_params).json()
    return data.get("current_weather")
