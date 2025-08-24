from sqlmodel import SQLModel, Field, ForeignKey
from typing import Optional

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")  # relasi ke Product
    color: Optional[str]
    size: Optional[str]
    price: float
    image_url: Optional[str]
    is_default: bool = False
