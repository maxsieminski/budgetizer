from datetime import datetime
from pydantic import BaseModel

from schemas.expense_category import ExpenseCategory
from schemas.expense_item import ExpenseItem, ExpenseItemCreate
from schemas.shop import Shop


class ExpenseBase(BaseModel):
    created_at: datetime = datetime.now()


class ExpenseCreate(ExpenseBase):
    items: list[ExpenseItemCreate]
    shop_id: int | None = None
    category_id: int | None = None


class Expense(ExpenseBase):
    id: int
    shop: Shop
    category: ExpenseCategory
    items: list[ExpenseItem]
    total_value: float

    class Config:
        orm_mode = True
