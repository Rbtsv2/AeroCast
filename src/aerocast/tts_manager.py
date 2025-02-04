# aerocast/tts_manager.py
import gtts
from playsound3 import playsound

class TextToSpeechManager:
    def __init__(self, lang, filename='info.mp3'):
        if lang in gtts.lang.tts_langs():
            self.lang = lang
        else:
            self.lang = None
        self.filename = filename
    
    def play_text(self, text: str):
        success = False
        try:
            if self.lang:
                tts = gtts.gTTS(text, lang=self.lang)
            else:
                tts = gtts.gTTS(text)
            tts.save(self.filename)
            playsound(self.filename)
            success = True
        except ValueError as e:
            print(f"gTTS ValueError: {e}")
            self.lang = None
            self.play_text(text)
        except Exception as e:
            raise e
        finally:
            print(self.lang)
            return success