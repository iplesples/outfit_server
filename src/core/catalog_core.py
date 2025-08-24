from sqlmodel import Session, select
from fastapi import UploadFile
from src.models.catalog_model import Catalog, CatalogProduct
from config.cloudinary import cloudinary

def create_catalog(db: Session, name: str, description: str, file: UploadFile):
    # Upload gambar ke Cloudinary
    result = cloudinary.uploader.upload(file.file, folder="catalog")
    image_url = result["secure_url"]

    # Buat Catalog
    catalog = Catalog(name=name, description=description, image_url=image_url)
    db.add(catalog)
    db.commit()
    db.refresh(catalog)
    return catalog

def get_catalog(db: Session, catalog_id: int):
    return db.get(Catalog, catalog_id)

def list_catalogs(db: Session):
    statement = select(Catalog)
    return db.exec(statement).all()

def update_catalog(db: Session, catalog_id: int, name: str = None, description: str = None, file: UploadFile = None):
    catalog = db.get(Catalog, catalog_id)
    if not catalog:
        return None
    if name:
        catalog.name = name
    if description:
        catalog.description = description
    if file:
        result = cloudinary.uploader.upload(file.file, folder="catalog")
        catalog.image_url = result["secure_url"]
    db.add(catalog)
    db.commit()
    db.refresh(catalog)
    return catalog

def delete_catalog(db: Session, catalog_id: int):
    catalog = db.get(Catalog, catalog_id)
    if not catalog:
        return None
    db.delete(catalog)
    db.commit()
    return catalog

# Fungsi untuk menambahkan product ke katalog
def add_product_to_catalog(db: Session, catalog_id: int, product_id: int):
    # Cek apakah sudah ada
    statement = select(CatalogProduct).where(
        CatalogProduct.catalog_id == catalog_id,
        CatalogProduct.product_id == product_id
    )
    existing = db.exec(statement).first()
    if existing:
        return existing

    cp = CatalogProduct(catalog_id=catalog_id, product_id=product_id)
    db.add(cp)
    db.commit()
    db.refresh(cp)
    return cp

# Fungsi untuk list product di katalog
def list_products_in_catalog(db: Session, catalog_id: int):
    statement = select(CatalogProduct).where(CatalogProduct.catalog_id == catalog_id)
    return db.exec(statement).all()
