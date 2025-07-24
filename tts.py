# tts.py

import requests
import uuid
from config import TTSMAKER_API_URL, TTSMAKER_VOICE
from playsound import playsound

def text_to_speech(text):
    print("🔊 Converting to speech...")
    filename = f"output_{uuid.uuid4().hex[:6]}.mp3"

    payload = {
        "text": text,
        "voice": TTSMAKER_VOICE,
        "output_format": "mp3",
        "speed": 1,
        "pitch": 1
    }

    response = requests.post(TTSMAKER_API_URL, json=payload)
    response.raise_for_status()
    audio_url = response.json().get("audio_url")

    if audio_url:
        audio = requests.get(audio_url)
        with open(filename, "wb") as f:
            f.write(audio.content)
        playsound(filename)
    else:
        print("❌ Failed to get audio URL.")
