# tests/test_weather.py
import unittest
from aerocast.weather import WeatherManager
from aerocast.tts_manager import TextToSpeechManager

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
        tts_weather = TextToSpeechManager('I am a test to save audio')
        self.assertIsInstance(wm.save_audio(tts_weather), bool)

    def test_play_audio(self):
        wm = WeatherManager('KJFK', lang=None)
        tts_weather = TextToSpeechManager('I am a test to play audio')
        self.assertIsInstance(wm.play_audio(tts_weather), bool)

if __name__ == '__main__':
    unittest.main()