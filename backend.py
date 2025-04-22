import os
import requests

def get_weather_data(location, forecast_days=None, weather_type=None):
    api_key = os.getenv("openweather_api_key")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    get_weather_data(location="London")
