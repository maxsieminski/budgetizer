from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.class_validators import Optional

from schemas.expense_category import ExpenseCategory, ExpenseCategoryCreate
from schemas.expense_item import ExpenseItem, ExpenseItemCreate
from schemas.shop import Shop, ShopCreate


class ExpenseBase(BaseModel):
    created_at: datetime = datetime.now()


class ExpenseCreate(ExpenseBase):
    items: list[ExpenseItemCreate]
    shop_id: Optional[int] = Field(None)
    category_id: Optional[int] = Field(None)
    shop: Optional[ShopCreate] = Field(None)
    category: Optional[ExpenseCategoryCreate] = Field(None)


class Expense(ExpenseBase):
    id: int
    shop: Shop
    category: ExpenseCategory
    items: list[ExpenseItem]
    total_value: float

    class Config:
        orm_mode = True
