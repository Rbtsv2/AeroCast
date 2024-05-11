# tests/test_weather.py
import unittest
from aerocast.weather import WeatherManager

class TestWeatherManager(unittest.TestCase):
    def test_summarize(self):
        wm = WeatherManager({'temp': '20', 'wind_speed': '10'})
        self.assertEqual(wm.summarize(), "Temp: 20 Wind: 10")

if __name__ == '__main__':
    unittest.main()