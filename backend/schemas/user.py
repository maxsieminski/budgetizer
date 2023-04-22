from pydantic import BaseModel

from schemas.expense import Expense


class UserBase(BaseModel):
    email: str
    name: str | None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    expenses: list[Expense] = []

    class Config:
        orm_mode = True
