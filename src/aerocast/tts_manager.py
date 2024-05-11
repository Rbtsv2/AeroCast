# aerocast/tts_manager.py
from gtts import gTTS
from playsound3 import playsound
import time

class TextToSpeechManager:
    def __init__(self, text, lang='fr'):
        self.text = text
        self.lang = lang

    def save_to_file(self, filename):
        tts = gTTS(self.text, lang=self.lang)
        tts.save(filename)
        return filename
    
    def play_file(self, filename):
        playsound(filename)