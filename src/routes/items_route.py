# src/routes/items.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.core import item_core

from config.database import get_session
from src.models.item_model import Item

# Inisialisasi router untuk item
item_router = APIRouter(prefix="/items", tags=["items"])

# Endpoint untuk membuat item baru
@item_router.post("/", response_model=Item)
def create_item(item: Item, db: Session = Depends(get_session)):
    return item_core.create_new_item(db, item)

# Endpoint untuk mendapatkan semua item
@item_router.get("/", response_model=List[Item])
def get_all_items(db: Session = Depends(get_session)):
    return item_core.get_all_items(db)

# Endpoint untuk mendapatkan satu item berdasarkan ID
@item_router.get("/{item_id}", response_model=Item)
def get_item_by_id(item_id: int, db: Session = Depends(get_session)):
    item = item_core.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan")
    return item

# Endpoint untuk memperbarui item
@item_router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, new_item: Item, db: Session = Depends(get_session)):
    update_item = item_core.update_existing_item(db, item_id, new_item)
    if not update_item:
        raise HTTPException(status_code=404, detail="item tidak ditemukan")
    return update_item

# Endpoint untuk menghapus item
@item_router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_session)):
    item_to_delete = item_core.delete_existing_item(db, item_id)
    if not item_to_delete:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan.")
    return {"message": "Item berhasil dihapus."}