from pydantic import BaseModel
from pydantic.class_validators import Optional


class ProductBase(BaseModel):
    name: str
    brand: Optional[str]


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
