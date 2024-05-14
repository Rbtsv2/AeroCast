# tests/test_weather.py
import unittest
from aerocast.weather import WeatherManager
from aerocast.tts_manager import TextToSpeechManager

TTS_WEATHER = TextToSpeechManager('I am a test')

class TestWeatherManager(unittest.TestCase):
    def test_temperature(self):
        wm = WeatherManager('KJFK', lang=None)
        self.assertIsInstance(wm.get_temperature(), str)
    
    def test_summarize(self):
        wm = WeatherManager('KJFK', lang=None)
        self.assertIsInstance(wm.get_summarize(), str)

    def test_wind_speed(self):
        wm = WeatherManager('KJFK', lang=None)
        self.assertIsInstance(wm.get_wind_speed(), str)

    def test_save_audio(self):
        wm = WeatherManager('KJFK', lang=None)
        self.assertIsInstance(wm.save_audio(TTS_WEATHER), bool)

    def test_play_audio(self):
        wm = WeatherManager('KJFK', lang=None)
        self.assertIsInstance(wm.play_audio(TTS_WEATHER), bool)

if __name__ == '__main__':
    unittest.main()