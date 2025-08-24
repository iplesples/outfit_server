from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

class ProductCategory(str, Enum):
    head = "head"
    top = "top"
    bottom = "bottom"
    foot = "foot"
    extra = "extra"

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    category: ProductCategory
