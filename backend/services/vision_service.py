import base64
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_figure(image_path, query):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    base64_image = base64.b64encode(image_bytes).decode()

    payload = {
        "model": "moondream",
        "prompt": f"{query}. Explain the diagram clearly.",
        "images": [base64_image],
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()["response"]

"""
LangGraph Pipeline
        ↓
Retrieval Agent
        ↓
Vision Agent
        ↓
vision_service.analyze_figure()
        ↓
Gemini Vision Model
        ↓
Diagram explanation
        ↓
Reasoning Agent (Ollama)
        ↓
Final answer

Gemini → image understanding
Ollama → reasoning
"""