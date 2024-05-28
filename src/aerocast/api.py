# aerocast/api.py
import requests
import warnings
from threading import Lock

class API:
    BASE_URL = 'https://aviationweather.gov/api'

    @staticmethod
    def filter_by_iata(airports, airport_code: str):
        for airport in airports:
            if airport['iata'] == airport_code.upper():
                return airport
        raise ValueError(f"No airport matching {airport_code}")

    def __init__(self, verify_connection=True):
        self.verify_connection = verify_connection
        self.request_session = requests.Session()
        self.request_lock = Lock()

    def _request_post(self, endpoint, data=None, json=None, **kwargs):
        self.request_lock.acquire()
        kwargs['params'].update({'format': 'json'})
        result = self.request_session.post(f"{API.BASE_URL}/{endpoint}", data, json, **kwargs)
        result.raise_for_status()
        self.request_lock.release()
        return result
 
    def _request_get(self, endpoint, **kwargs):
        self.request_lock.acquire()
        kwargs['params'].update({'format': 'json'})
        result = self.request_session.get(f"{API.BASE_URL}/{endpoint}", **kwargs)
        result.raise_for_status()
        self.request_lock.release()
        return result

    def get_metar_data(self, airport_code):
        r = self._request_get('data/metar', params={'ids': airport_code})
        if r.ok:
            return r.json()

    def get_airport_data(self, airport_code):
        r = self._request_get('data/airport', params={'ids': airport_code})
        if r.ok:
            return r.json()

    @staticmethod
    def fetch_data(endpoint, params):
        warnings.warn('fetch_data is deprecated, use get_metar_data or get_airport_data instead', DeprecationWarning)
        r = requests.get(f"{API.BASE_URL}/{endpoint}", params=params)
        r.raise_for_status()
        if r.ok:
            return r.json()
        else:
            raise ValueError(f"Failed to fetch weather data (HTTP {r.status_code})")