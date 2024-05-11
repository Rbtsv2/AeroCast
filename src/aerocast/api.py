# aerocast/api.py
import requests

class API:
    BASE_URL = 'https://aviationweather.gov/api'

    @staticmethod
    def fetch_data(endpoint, params):
        try:
            response = requests.get(f"{API.BASE_URL}/{endpoint}", params=params)
            if response.ok:
                return response.json()
            else:
                raise ValueError("Failed to fetch weather data")
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return None
