from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.dependencies import get_db

from crud import expense as crud
from crud.user import get_current_user
from models.user import User
from schemas.expense import ExpenseCreate, Expense

router = APIRouter()


@router.get("/", response_model=list[Expense])
def get_expenses(current_user: Annotated[User, Depends(get_current_user)],
                 skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_expenses(db, current_user, skip, limit)


@router.get("/{expense_id}", response_model=Expense)
def get_expense(current_user: Annotated[User, Depends(get_current_user)],
                expense_id: int, db: Session = Depends(get_db)):
    return crud.get_expense(db, current_user, expense_id)


@router.post("/", response_model=Expense, status_code=201)
def create_expense(current_user: Annotated[User, Depends(get_current_user)],
                   new_expense: ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, current_user, new_expense)
