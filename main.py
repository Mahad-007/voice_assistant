from recorder import record_audio
from transcriber import transcribe_audio
from groq_chat import chat_with_groq
from tts import text_to_speech

def main():
    audio_file = record_audio()
    transcribed = transcribe_audio(audio_file)
    if transcribed:
        reply = chat_with_groq(transcribed)
        text_to_speech(reply)

if __name__ == "__main__":
    while True:
        main()
        cont = input("▶️ Ask again? (y/n): ").strip().lower()
        if cont != "y":
            break
