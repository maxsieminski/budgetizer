from pydantic import ValidationError
from sqlalchemy.orm import Session

from models.expense import Expense, ExpenseItem
from models.user import User

from crud.product import get_product, create_product

from crud.shop import create_shop, get_shop
from crud.expense_category import create_expense_category, get_expense_category

from schemas.expense import ExpenseCreate, ExpenseItemCreate


def get_expense(db: Session, user: User, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user.id).first()


def get_expenses(db: Session, user: User, skip: int = 0, limit: int = 100):
    return db.query(Expense).filter(Expense.user_id == user.id).offset(skip).limit(limit).all()


def create_expense(db: Session, user: User, expense: ExpenseCreate):
    db_expense = parse_expense(expense, user, db)

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    create_expense_items(expense.items, db_expense.id, db)

    db.refresh(db_expense)

    return db_expense


def create_expense_items(expense_items: list[ExpenseItemCreate], expense_id: int, db: Session):
    for expense_item in expense_items:
        if expense_item.product_id and expense_item.product:
            raise ValidationError("Provide either ID or a model")

        product = get_product(db, expense_item.product_id) if expense_item.product_id else create_product(db, expense_item.product) if expense_item.product else None

        db_expense_item = ExpenseItem(expense_id=expense_id, product_id=product.id,
                                      quantity=expense_item.quantity, value_per_item=expense_item.value_per_item)
        db.add(db_expense_item)
        db.commit()
        db.refresh(db_expense_item)


def parse_expense(expense: ExpenseCreate, user: User, db: Session):
    if (expense.shop_id and expense.shop) or (expense.category_id and expense.category):
        raise ValidationError("Provide either ID or a model")

    shop = get_shop(db, expense.shop_id) if expense.shop_id else create_shop(db, expense.shop) if expense.shop else None
    expense_category = get_expense_category(db, expense.category_id) if expense.category_id else create_expense_category(db, expense.category) if expense.category else None

    expense = Expense(user_id=user.id, shop_id=shop.id, category_id=expense_category.id, created_at=expense.created_at)

    return expense
