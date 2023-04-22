from sqlalchemy.orm import Session

from models.shop import Shop
from schemas.shop import ShopCreate


def get_shop(db: Session, shop_id: int):
    shop = db.query(Shop).filter(Shop.id == shop_id).first()
    return shop


def get_shop_by_name(db: Session, name: str):
    shop = db.query(Shop).filter(Shop.name == name).first()
    return shop


def get_shops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Shop).offset(skip).limit(limit).all()


def create_shop(db: Session, shop: ShopCreate):
    db_shop = Shop(name=shop.name)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop
