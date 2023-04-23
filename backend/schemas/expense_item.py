from pydantic import BaseModel
from pydantic.class_validators import Optional

from schemas.product import Product, ProductCreate


class ExpenseItemBase(BaseModel):
    quantity: int = 1
    value_per_item: int = 1


class ExpenseItemCreate(ExpenseItemBase):
    expense_id: Optional[int]
    product: Optional[ProductCreate]
    product_id: Optional[int]


class ExpenseItem(ExpenseItemBase):
    id: int
    product: Product

    class Config:
        orm_mode = True
