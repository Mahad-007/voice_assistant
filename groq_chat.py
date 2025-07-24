# groq_chat.py

import requests
from config import GROQ_API_KEY, GROQ_MODEL

def chat_with_groq(prompt):
    print("🤖 Thinking...")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    res = requests.post(url, headers=headers, json=data)
    res.raise_for_status()
    reply = res.json()["choices"][0]["message"]["content"]
    print(f"🤖 Response: {reply}")
    return reply
