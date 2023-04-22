from sqlalchemy.orm import Session

from models.expense import ExpenseCategory
from schemas.expense_category import ExpenseCategoryCreate


def get_expense_category(db: Session, expense_category_id: int):
    return db.query(ExpenseCategory).filter(ExpenseCategory.id == expense_category_id).first()


def get_expense_category_by_name(db: Session, name: str):
    return db.query(ExpenseCategory).filter(ExpenseCategory.name == name).first()


def get_expense_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExpenseCategory).offset(skip).limit(limit).all()


def create_expense_category(db: Session, expense_category: ExpenseCategoryCreate):
    db_expense_category = ExpenseCategory(name=expense_category.name)
    db.add(db_expense_category)
    db.commit()
    db.refresh(db_expense_category)
    return db_expense_category
