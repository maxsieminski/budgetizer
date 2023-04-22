from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.dependencies import get_db

from crud import product as crud
from crud.user import get_current_user

from models.user import User

from schemas.product import ProductCreate, Product

router = APIRouter()


@router.get("/", response_model=list[Product])
def get_products(current_user: Annotated[User, Depends(get_current_user)],
                 skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip, limit)


@router.get("/{product_id}", response_model=Product)
def get_product(current_user: Annotated[User, Depends(get_current_user)],
                product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)


@router.post("/", status_code=201, response_model=Product)
def create_product(current_user: Annotated[User, Depends(get_current_user)],
                   new_product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, new_product)
