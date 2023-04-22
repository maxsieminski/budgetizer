from sqlalchemy.orm import Session

from models.expense import ExpenseItem
from schemas.expense_item import ExpenseItemCreate


def get_expense_item(db: Session, expense_item_id: int):
    return db.query(ExpenseItem).filter(ExpenseItem.id == expense_item_id).first()


def get_expense_item_by_name(db: Session, name: str):
    return db.query(ExpenseItem).filter(ExpenseItem.name == name).first()


def get_expense_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExpenseItem).offset(skip).limit(limit).all()


def create_expense_item(db: Session, expense_item: ExpenseItemCreate):
    db_expense_item = ExpenseItem(
        expense_id=expense_item.expense_id, product_id=expense_item.product_id,
        quantity=expense_item.quantity, value_per_item=expense_item.value_per_item
    )
    db.add(db_expense_item)
    db.commit()
    db.refresh(db_expense_item)
    return db_expense_item
