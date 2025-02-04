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
            if self.lang:
                tts = gTTS(text, lang=self.lang)
            else:
                tts = gTTS(text)
            tts.save(self.filename)
            playsound(self.filename)
            success = True
        except Exception as e:
            print(f"func play_text -> {e}")
        finally:
            return success