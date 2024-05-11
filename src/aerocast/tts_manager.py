# aerocast/tts_manager.py
from gtts import gTTS
import pygame

class TextToSpeechManager:
    def __init__(self, text, lang='fr'):
        self.text = text
        self.lang = lang

    def save_to_file(self, filename):
        tts = gTTS(self.text, lang=self.lang)
        tts.save(filename)
        return filename
    
    def play_file(self, filename):
        pygame.mixer.init()
        airport_sound = pygame.mixer.Sound(filename)
        airport_sound.play()