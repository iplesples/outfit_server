from fastapi import APIRouter, UploadFile, Form, Depends, File
from sqlmodel import Session
from config.database import get_session
from src.core.catalog_core import (
    create_catalog, list_catalogs, get_catalog,
    update_catalog, delete_catalog,
    add_product_to_catalog, list_products_in_catalog
)

router = APIRouter(prefix="/catalog", tags=["catalog"])

@router.get("/")
def read_catalogs(db: Session = Depends(get_session)):
    return list_catalogs(db)

@router.get("/{catalog_id}")
def read_catalog(catalog_id: int, db: Session = Depends(get_session)):
    return get_catalog(db, catalog_id)

@router.post("/")
def create_new_catalog(
    name: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_session)
):
    return create_catalog(db, name, description, file)

@router.put("/{catalog_id}")
def update_existing_catalog(
    catalog_id: int,
    name: str = Form(None),
    description: str = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_session)
):
    return update_catalog(db, catalog_id, name, description, file)

@router.delete("/{catalog_id}")
def remove_catalog(catalog_id: int, db: Session = Depends(get_session)):
    return delete_catalog(db, catalog_id)

@router.post("/{catalog_id}/product/{product_id}")
def add_product(catalog_id: int, product_id: int, db: Session = Depends(get_session)):
    return add_product_to_catalog(db, catalog_id, product_id)

@router.get("/{catalog_id}/products")
def list_products(catalog_id: int, db: Session = Depends(get_session)):
    return list_products_in_catalog(db, catalog_id)
