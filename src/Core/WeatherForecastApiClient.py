import json
import requests
from urllib.parse import urlencode

from src.configs.consants import *
from src.configs.endpoints import *


class WeatherForecastClient:
    def __init__(self, city: str = "Lviv", language: str = "uk", days: int = 0):
        self.city = city
        self.language = language
        self.days = days

    def call_client(self):
        params = {
            'q': self.city,
            'lang': self.language,
        }

        type = ""

        if self.days != 0:
            type = FORECAST
            params['days'] = self.days
        else:
            type = CURRENT_WEATHER

        # URL encode the parameters
        encoded_params = urlencode(params)

        # Construct the full URL with encoded parameters
        full_url = f"{API_URL}/{type}?{encoded_params}"

        # Make the API call
        response = requests.get(full_url)

        return json.loads(response.json())

    def change_city(self, city: str):
        self.city = city

    def change_language(self, language: str):
        self.language = language

    def change_days(self, days: int):
        self.days = days

    def get_text(self):
        data = self.call_client()

        location_info = data["location"]
        current_info = data["current"]

        result = ""

        result += f"Location: {location_info['name']}, {location_info['country']}\n"
        result += f"Local Time: {location_info['localtime']}\n"
        result += f"Temperature: {current_info['temp_c']}°C ({current_info['temp_f']}°F)\n"
        result += f"Condition: {current_info['condition']['text']}\n"
        result += f"Wind: {current_info['wind_kph']} kph {current_info['wind_dir']}\n"
        result += f"Humidity: {current_info['humidity']}%\n"
        result += f"Pressure: {current_info['pressure_mb']} mb\n"
        result += f"Visibility: {current_info['vis_km']} km\n"
        result += f"UV Index: {current_info['uv']}\n"

        return result
