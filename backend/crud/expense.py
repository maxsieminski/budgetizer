from sqlalchemy.orm import Session

from models.expense import Expense, ExpenseItem
from models.user import User

from schemas.expense import ExpenseCreate


def get_expense(db: Session, user: User, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user.id).first()


def get_expenses(db: Session, user: User, skip: int = 0, limit: int = 100):
    return db.query(Expense).filter(Expense.user_id == user.id).offset(skip).limit(limit).all()


def create_expense(db: Session, user: User, expense: ExpenseCreate):
    db_expense = Expense(
        user_id=user.id, shop_id=expense.shop_id, category_id=expense.category_id,
        created_at=expense.created_at
    )

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    for expense_item in expense.items:
        db_expense_item = ExpenseItem(expense_id=db_expense.id, product_id=expense_item.product_id,
                                      quantity=expense_item.quantity, value_per_item=expense_item.value_per_item)
        db.add(db_expense_item)
        db.commit()
        db.refresh(db_expense_item)

    db.refresh(db_expense)

    return db_expense
