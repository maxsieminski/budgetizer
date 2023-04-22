from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.dependencies import get_db

from crud import expense_category as crud
from crud.user import get_current_user
from models.user import User
from schemas.expense_category import ExpenseCategoryCreate, ExpenseCategory

router = APIRouter()


@router.get("/", response_model=list[ExpenseCategory])
def get_expense_categories(current_user: Annotated[User, Depends(get_current_user)],
                           skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_expense_categories(db, skip, limit)


@router.get("/{expense_category_id}", response_model=ExpenseCategory)
def get_expense_category(current_user: Annotated[User, Depends(get_current_user)],
                         expense_category_id: int, db: Session = Depends(get_db)):
    return crud.get_expense_category(db, expense_category_id)


@router.post("/", response_model=ExpenseCategory, status_code=201)
def create_expense_category(current_user: Annotated[User, Depends(get_current_user)],
                            new_expense_category: ExpenseCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_expense_category(db, new_expense_category)
