from typing import List, Optional
from sqlmodel import Session, select
from src.models.item_model import Item

def create_new_item(db: Session, item: Item):
    db.add(item)
    db.commit()
    db.refresh
    return item

def get_all_items(db: Session) -> List[Item]:
    items = db.exec(select(Item).all())
    return items

def get_item_by_id(db: Session, item_id: int) -> Optional[Item]:
    item = db.exec(select(Item).where(Item.id == item_id).first())
    return item

def update_existing_item(db: Session, item_id: int, new_item_data: Item) -> Optional[Item]:
    item_to_update = db.exec(select(Item).where(Item.id == item_id).first())
    if not item_to_update:
        return None
    item_data = new_item_data.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item_to_update, key, value)
    db.add(item_to_update)
    db.commit()
    db.refresh(item_to_update)
    return item_to_update

def delete_existing_item(db: Session, item_id: int) -> bool:
    item_to_delete = db.exec(select(Item).where(Item.id == item_id).first())
    if not item_to_delete:
        return False
    db.delete(item_to_delete)
    db.commit()
    return True