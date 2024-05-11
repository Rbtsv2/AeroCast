# aerocast/weather.py
class WeatherManager:
    def __init__(self, data):
        self.data = data

    def summarize(self):
        return f"Temp: {self.data['temp']} Wind: {self.data['wind_speed']}"