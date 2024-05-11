# aerocast/weather.py
from .data_manager import DataManager

class WeatherManager:
    def __init__(self, airport_code):
        self.airport_code = airport_code
        self._weather_data_cache = None

    def fetch_weather_data(self):
        # Mise en cache des données pour réduire les appels API inutiles
        weather_data = DataManager.get_weather_data(self.airport_code)
        if not weather_data:
            raise ValueError("No weather data available")
        return weather_data
         
    def get_temperature(self):
        weather_data = self.fetch_weather_data()
        return f"Temp: {weather_data.get('temp', 'N/A')}°C"

    def get_wind_speed(self):
        weather_data = self.fetch_weather_data()
        return f"Wind Speed: {weather_data.get('wind_speed', 'N/A')} km/h"

    def summarize(self):
        weather_data = self.fetch_weather_data()
        temperature = weather_data.get('temp', 'N/A')
        wind_speed = weather_data.get('wind_speed', 'N/A')
        return f"Temp: {temperature}°C, Wind: {wind_speed} km/h"

