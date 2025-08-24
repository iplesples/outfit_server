from fastapi import APIRouter, Form, UploadFile, Depends
from sqlmodel import Session
from config.database import get_session
from src.core.item_core import create_item, update_item, get_item, list_items, delete_item

router = APIRouter(prefix="/item", tags=["item"])

@router.get("/")
def read_items(product_id: int = None, db: Session = Depends(get_session)):
    return list_items(db, product_id)

@router.get("/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_session)):
    return get_item(db, item_id)

@router.post("/")
def create_new_item(
    product_id: int = Form(...),
    color: str = Form(None),
    size: str = Form(None),
    price: float = Form(...),
    file: UploadFile = Form(None),
    is_default: bool = Form(False),
    db: Session = Depends(get_session)
):
    return create_item(db, product_id, color, size, price, file, is_default)

@router.put("/{item_id}")
def update_existing_item(
    item_id: int,
    color: str = Form(None),
    size: str = Form(None),
    price: float = Form(None),
    file: UploadFile = Form(None),
    is_default: bool = Form(None),
    db: Session = Depends(get_session)
):
    return update_item(db, item_id, color, size, price, file, is_default)

@router.delete("/{item_id}")
def remove_item(item_id: int, db: Session = Depends(get_session)):
    return delete_item(db, item_id)
