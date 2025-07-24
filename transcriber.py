# transcriber.py
import os
os.environ["PATH"] += os.pathsep + r"C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin"
import whisper

model = whisper.load_model("base")  # You can try 'small' or 'medium' for better accuracy

def transcribe_audio(audio_file):
    print("📝 Transcribing audio...")
    result = model.transcribe(audio_file)
    print(f"📄 Transcription: {result['text']}")
    return result["text"]
