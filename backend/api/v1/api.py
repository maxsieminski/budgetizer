from fastapi import APIRouter
from api.v1.endpoints import shop, product, expense, expense_categories, auth


api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(shop.router, prefix="/shops", tags=["shops"])
api_router.include_router(product.router, prefix="/products", tags=["products"])
api_router.include_router(expense.router, prefix="/expenses", tags=["expenses"])
api_router.include_router(expense_categories.router, prefix="/expense_categories", tags=["expense_categories"])
