import reflex as rx
from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

if not db_password or not db_name:
    raise ValueError("DB_PASSWORD and DB_NAME must be set in the .env file")

config = rx.Config(
    app_name="database",
    db_url=f"postgresql://postgres:{db_password}@localhost:5432/{db_name}",
)
