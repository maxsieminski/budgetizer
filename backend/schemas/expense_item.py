from pydantic import BaseModel

from schemas.product import Product


class ExpenseItemBase(BaseModel):
    quantity: int = 1
    value_per_item: int = 1


class ExpenseItemCreate(ExpenseItemBase):
    expense_id: int | None = None
    product_id: int


class ExpenseItem(ExpenseItemBase):
    id: int
    product: Product

    class Config:
        orm_mode = True
