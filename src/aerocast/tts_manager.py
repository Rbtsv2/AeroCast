# aerocast/tts_manager.py
from gtts import gTTS
from playsound3 import playsound

class TextToSpeechManager:
    def __init__(self, lang, filename='info.mp3'):
        self.lang = lang
        self.filename = filename
    
    def play_text(self, text: str):
        success = False
        try:
            tts = gTTS(text, lang=self.lang)
            tts.save(self.filename)
            playsound(self.filename)
            success = True
        except Exception as e:
            print(e)
        finally:
            return success