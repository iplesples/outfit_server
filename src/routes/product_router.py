from fastapi import APIRouter, Form, Depends
from sqlmodel import Session
from config.database import get_session
from src.core.product_core import (
    create_product, update_product, get_product, list_products, delete_product
)
from src.models.product_model import ProductCategory

router = APIRouter(prefix="/product", tags=["product"])

@router.get("/")
def read_products(category: ProductCategory = None, db: Session = Depends(get_session)):
    return list_products(db, category)

@router.get("/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_session)):
    return get_product(db, product_id)

@router.post("/")
def create_new_product(
    name: str = Form(...),
    description: str = Form(...),
    category: ProductCategory = Form(...),
    db: Session = Depends(get_session)
):
    return create_product(db, name, description, category)

@router.put("/{product_id}")
def update_existing_product(
    product_id: int,
    name: str = Form(None),
    description: str = Form(None),
    category: ProductCategory = Form(None),
    db: Session = Depends(get_session)
):
    return update_product(db, product_id, name, description, category)

@router.delete("/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_session)):
    return delete_product(db, product_id)
