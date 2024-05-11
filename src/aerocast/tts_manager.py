# aerocast/tts_manager.py
from gtts import gTTS
from pygame import mixer
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
        mixer.init()
        airport_sound = mixer.music.load(filename)
        mixer.music.play()
        while mixer.music.get_busy(): # wait for music to finish playing, otherwise programs/sound quits immediately after it starts
            time.sleep(1)