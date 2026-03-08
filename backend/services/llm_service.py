import requests
from backend.utils.config import settings

OLLAMA_API = f"{settings.OLLAMA_URL}/api/generate"


def generate_response(prompt: str):

    payload = {
        "model": settings.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_API, json=payload)

    data = response.json()

    # Debug log
    print("OLLAMA RESPONSE:", data)

    if "response" in data:
        return data["response"]

    return "LLM failed to generate response"