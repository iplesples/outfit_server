from sqlmodel import Session, select
from src.models.product_model import Product, ProductCategory

def create_product(db: Session, name: str, description: str, category: ProductCategory):
    product = Product(name=name, description=description, category=category)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(db: Session, product_id: int, name: str = None, description: str = None, category: ProductCategory = None):
    product = db.get(Product, product_id)
    if not product:
        return None
    if name:
        product.name = name
    if description:
        product.description = description
    if category:
        product.category = category
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product(db: Session, product_id: int):
    return db.get(Product, product_id)

def list_products(db: Session, category: ProductCategory = None):
    statement = select(Product)
    if category:
        statement = statement.where(Product.category == category)
    return db.exec(statement).all()

def delete_product(db: Session, product_id: int):
    product = db.get(Product, product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product
