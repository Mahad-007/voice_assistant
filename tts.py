# tts.py

from gtts import gTTS
from playsound import playsound
import os
import uuid
from config import LANG

def text_to_speech(text):
    print("🔊 Converting to speech (gTTS)...")
    tts = gTTS(text=text, lang=LANG)
    filename = f"output_{uuid.uuid4().hex[:6]}.mp3"
    try:
        tts.save(filename)
        playsound(filename)
    except Exception as e:
        print("❌ gTTS or playback error:", e)
    finally:
        if os.path.exists(filename):
            os.remove(filename)
