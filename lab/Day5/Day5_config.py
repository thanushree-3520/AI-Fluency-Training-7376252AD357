import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../Day1/.env")

PROVIDER = "groq"
BASE_URL = "https://api.groq.com/openai/v1"
MODEL = "openai/gpt-oss-20b"

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise SystemExit("GROQ_API_KEY not found in Day1/.env")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)