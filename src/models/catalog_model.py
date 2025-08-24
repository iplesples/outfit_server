from sqlmodel import SQLModel, Field
from typing import Optional

class Catalog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str]
    image_url: Optional[str]

class CatalogProduct(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    catalog_id: int = Field(foreign_key="catalog.id")
    product_id: int = Field(foreign_key="product.id")
