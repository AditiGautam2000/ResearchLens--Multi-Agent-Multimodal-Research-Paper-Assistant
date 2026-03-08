import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    FIGURE_STORAGE = os.getenv("FIGURE_STORAGE", "extracted_images")

    QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))

    VALKEY_HOST = os.getenv("VALKEY_HOST", "localhost")
    VALKEY_PORT = int(os.getenv("VALKEY_PORT", "6379"))

    MONGO_URI = os.getenv("MONGO_URI")

    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_BASE_URL = os.getenv(
    "GEMINI_BASE_URL",
    "https://generativelanguage.googleapis.com/v1beta/openai/"
    

    
)

settings = Settings()