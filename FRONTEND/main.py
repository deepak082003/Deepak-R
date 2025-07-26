from fastapi import FastAPI, HTTPException
import psycopg2, os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

DB_NAME = os.getenv("DB_NAME", "e_commerce_db")
DB_USER = os.getenv("DB_USER", "your_username")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

@app.post("/api/chat")
def chat(user_message: str, conversation_id: int = None):
    response = f"AI Response to: {user_message}"
    return {"conversation_id": conversation_id or 1, "response": response}
