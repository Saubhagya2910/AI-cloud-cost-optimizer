import requests
import json
from config import GROQ_API_KEY, GROQ_MODEL

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_llm(prompt: str) -> dict:
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a cloud cost expert. Return ONLY raw JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    
    content = response.json()["choices"][0]["message"]["content"]
    # Strip markdown if present
    content = content.replace("```json", "").replace("```", "").strip()
    return json.loads(content)