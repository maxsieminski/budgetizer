from sqlalchemy import Column, Integer, Numeric, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from datetime import datetime

from db.db import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    shop_id = Column(Integer, ForeignKey("shops.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("expense_categories.id"), nullable=True)
    total_value = Column(Numeric(10, 2), default=0)
    created_at = Column(DateTime, default=datetime.now())

    owner = relationship("User", back_populates="expenses")
    shop = relationship("Shop")
    category = relationship("ExpenseCategory", back_populates="expenses")
    items = relationship("ExpenseItem", back_populates="expense")


class ExpenseCategory(Base):
    __tablename__ = "expense_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    expenses = relationship("Expense", back_populates="category")


class ExpenseItem(Base):
    __tablename__ = "expense_items"

    id = Column(Integer, primary_key=True, index=True)
    expense_id = Column(Integer, ForeignKey("expenses.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1)
    value_per_item = Column(Numeric(10, 2), default=0)

    expense = relationship("Expense", back_populates="items")
    product = relationship("Product")
