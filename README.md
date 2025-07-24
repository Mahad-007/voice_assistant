# Terminal Voice Assistant 🗣️

A simple terminal-based voice assistant that records your voice, transcribes it with **Whisper**, generates a response via the **Groq API**, and converts the reply to speech with **gTTS**.

## 🚀 Features & Workflow

1. **Record audio** from the microphone using `pyaudio`.
2. **Transcribe speech to text** with OpenAI’s **Whisper** model.
3. **Generate a response** using the **Groq API** chat completion endpoint.
4. **Convert text to speech** using **gTTS** and play it back with `playsound`.
5. Runs entirely in the terminal, looping until you choose to exit.

## 🧰 Technologies Used

| Layer          | Library / Tool     | Why Chosen                                      |
|----------------|--------------------|--------------------------------------------------|
| Audio Recording| `pyaudio`          | Captures microphone input reliably               |
| STT            | `whisper`          | Open-source, accurate speech-to-text             |
| LLM Chat       | Groq API           | Fast conversational AI model                     |
| TTS            | `gTTS`             | Free, no API key needed, easy to integrate       |
| Playback       | `playsound`        | Lightweight playback of generated audio          |

## 🛠️ Blockers & Resolutions

- **Missing `ffmpeg` binary**: Whisper raised `WinError 2`. Fixed by installing `ffmpeg` via Chocolatey or manual install, and adding it to PATH.
- **Groq 400 Bad Request**: Malformed body. Resolved by sending correct `"messages"` array, using `max_completion_tokens`, and removing unsupported fields.
- **TTSMaker failures**: Endpoint errors (404, 422) due to missing params. Switched to **gTTS**, eliminating need for API and simplifying TTS integration.

## 📁 Project Structure

voice_assistant/
├── recorder.py
├── transcriber.py
├── groq_chat.py
├── tts.py
├── config.py
├── main.py
└── requirements.txt

bash
Copy
Edit

## 🚀 Usage

1. Clone the repo:  
   ```bash
   git clone <repo_url>
   cd voice_assistant
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv env
.\env\Scripts\activate  # (Windows)
pip install -r requirements.txt
Ensure ffmpeg is installed and available via PATH.

Set your GROQ_API_KEY and GROQ_MODEL in config.py.

Run the assistant:

bash
Copy
Edit
python main.py
Speak into your mic, listen to replies, and repeat as needed.

✅ Why This Setup?
Free or minimal cost: Whisper and gTTS are open and free.

Fast prototyping: Everything runs locally, with just one external API.

Terminal‑based simplicity: No GUI, easy to iterate and customize.
