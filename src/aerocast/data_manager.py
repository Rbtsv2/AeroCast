# aerocast/data_manager.py
from .api import API

class DataManager:

    @staticmethod
    def filter_by_iata(airports, airport_code: str):
        for airport in airports:
            if airport['iata'] == airport_code.upper():
                return airport
        raise ValueError(f"No airport matching {airport_code}")

    @staticmethod
    def get_weather_data(airport_code):
        response = API.fetch_data('data/metar', {'ids': airport_code, 'format': 'json'})
        print(response)
        exit() 
        return response

    @staticmethod
    def get_airport(airport_code):
        airports = API.fetch_data('data/airport', {'ids': airport_code, 'format': 'json'})
        return airports[0] if len(airports) == 0 else filter(airports, airport_code)