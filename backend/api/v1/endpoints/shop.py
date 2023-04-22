from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.dependencies import get_db

from crud import shop as crud
from crud.user import get_current_user

from models.user import User

from schemas.shop import Shop, ShopCreate


router = APIRouter()


@router.get("/", response_model=list[Shop])
def get_shops(current_user: Annotated[User, Depends(get_current_user)],
              skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_shops(db, skip, limit)


@router.get("/{shop_id}", response_model=Shop)
def get_shop(current_user: Annotated[User, Depends(get_current_user)],
             shop_id: int, db: Session = Depends(get_db)):
    return crud.get_shop(db, shop_id)


@router.get("/name/{shop_name}", response_model=Shop)
def get_shop_by_name(current_user: Annotated[User, Depends(get_current_user)],
                     shop_name: str, db: Session = Depends(get_db)):
    return crud.get_shop_by_name(db, shop_name)


@router.post("/", response_model=Shop, status_code=201)
def create_shop(current_user: Annotated[User, Depends(get_current_user)],
                shop: ShopCreate, db: Session = Depends(get_db)):
    return crud.create_shop(db, shop)
