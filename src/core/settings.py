# src/core/settings.py

from config.database import engine
from sqlmodel import SQLModel
from src.models.item_model import Item


# Fungsi untuk membuat tabel di database
def db_setting():
    print("Mencoba membuat tabel...")
    SQLModel.metadata.create_all(engine)
    print("Tabel berhasil dibuat.")