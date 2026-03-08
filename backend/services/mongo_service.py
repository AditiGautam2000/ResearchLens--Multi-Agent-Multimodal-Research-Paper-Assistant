
from backend.utils.config import settings
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["research_agent"]

chat_collection = db["chat_history"]
db = client["research_agent"]

chat_collection = db["chat_history"]

figure_collection = db["figures"]