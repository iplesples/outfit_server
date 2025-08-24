from sqlmodel import Session, select
from fastapi import UploadFile
from src.models.item_model import Item
from config.cloudinary import cloudinary

def create_item(
    db: Session,
    product_id: int,
    color: str = None,
    size: str = None,
    price: float = 0.0,
    file: UploadFile = None,
    is_default: bool = False
):
    # Upload gambar ke Cloudinary jika ada
    image_url = None
    if file:
        result = cloudinary.uploader.upload(file.file, folder="items")
        image_url = result["secure_url"]

    # Jika is_default = True, set default sebelumnya ke False
    if is_default:
        statement = select(Item).where(Item.product_id == product_id, Item.is_default == True)
        existing_default = db.exec(statement).all()
        for item in existing_default:
            item.is_default = False
            db.add(item)

    # Buat item baru
    item = Item(
        product_id=product_id,
        color=color,
        size=size,
        price=price,
        image_url=image_url,
        is_default=is_default
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_item(
    db: Session,
    item_id: int,
    color: str = None,
    size: str = None,
    price: float = None,
    file: UploadFile = None,
    is_default: bool = None
):
    item = db.get(Item, item_id)
    if not item:
        return None

    if color:
        item.color = color
    if size:
        item.size = size
    if price is not None:
        item.price = price
    if file:
        result = cloudinary.uploader.upload(file.file, folder="items")
        item.image_url = result["secure_url"]
    if is_default is not None:
        if is_default:
            statement = select(Item).where(Item.product_id == item.product_id, Item.is_default == True)
            existing_default = db.exec(statement).all()
            for i in existing_default:
                i.is_default = False
                db.add(i)
        item.is_default = is_default

    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_item(db: Session, item_id: int):
    return db.get(Item, item_id)

def list_items(db: Session, product_id: int = None):
    statement = select(Item)
    if product_id:
        statement = statement.where(Item.product_id == product_id)
    return db.exec(statement).all()

def delete_item(db: Session, item_id: int):
    item = db.get(Item, item_id)
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item
