import os
from sqlmodel import create_engine, Session
from dotenv import load_dotenv
from typing import Generator

if os.getenv("VERCEL") != "1":
    load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise ValueError("DB_URL database tidak ditemukan")

# engine untuk koneksi ke PostgreSQL
engine = create_engine(DB_URL, echo=True)

# fungsi untuk mendapatkan sesi database
def get_session() -> Generator:
    with Session(engine) as session:
        yield session
