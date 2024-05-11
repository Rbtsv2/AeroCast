# aerocast/weather.py
from .data_manager import DataManager
from .tts_manager import TextToSpeechManager


class WeatherManager:
    def __init__(self, airport_code, lang):
        self.airport_code = airport_code
        self.lang = lang
    
    def fetch_weather_data(self):
        # Mise en cache des données pour réduire les appels API inutiles
        weather_data = DataManager.get_weather_data(self.airport_code)
        if not weather_data:
            raise ValueError("No weather data available")
        return weather_data
         
    def get_temperature(self):
        weather_data = self.fetch_weather_data()
        result = f"{weather_data.get('temp', 'N/A')}°C"
        if self.lang:
            print(self.lang)
            result = f"La température est de {weather_data.get('temp', 'N/A')}°C"
            print(result)
            tts_weather = TextToSpeechManager(result, self.lang)
            tts_weather.save_to_file("weather_info.mp3")
            tts_weather.play_file("weather_info.mp3")
        return result

    def get_wind_speed(self):
        weather_data = self.fetch_weather_data()
        return f"Wind Speed: {weather_data.get('wind_speed', 'N/A')} km/h"

    def summarize(self):
        weather_data = self.fetch_weather_data()
        temperature = weather_data.get('temp', 'N/A')
        wind_speed = weather_data.get('wind_speed', 'N/A')
        return f"Temp: {temperature}°C, Wind: {wind_speed} km/h"

