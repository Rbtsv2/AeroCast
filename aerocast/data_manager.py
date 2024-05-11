# aerocast/data_manager.py
from .api import API

class DataManager:
    @staticmethod
    def get_weather_data(airport_code):
        return API.fetch_data('data/metar', {'ids': airport_code, 'format': 'json'})

    @staticmethod
    def get_airport_info(airport_code):
        return API.fetch_data('data/airport', {'ids': airport_code, 'format': 'json'})
