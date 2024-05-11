# aerocast/api.py
import requests

class API:
    BASE_URL = 'https://aviationweather.gov/api'

    @staticmethod
    def fetch_data(endpoint, params):
        try:
            response = requests.get(f"{API.BASE_URL}/{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return None
