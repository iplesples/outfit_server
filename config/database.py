import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv


# hanya load dotenv kalau ada file .env (untuk local)
if os.path.exists(".env"):
    load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL tidak ditemukan di environment!")

# buat engine
engine = create_engine(DATABASE_URL, echo=True)

# dependency untuk FastAPI
def get_session():
    with Session(engine) as session:
        yield session
        