import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather_data(location, forecast_days=None, weather_type=None):
    api_key = os.getenv("openweather_api_key")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_values = 8 * forecast_days
    filtered_data = filtered_data[:8*number_values]
    if weather_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if weather_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_weather_data(location="London"))
