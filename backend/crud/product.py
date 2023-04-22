from sqlalchemy.orm import Session

from models.product import Product
from schemas.product import ProductCreate


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_product_by_name(db: Session, name: str):
    return db.query(Product).filter(Product.name == name).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate):
    db_product = get_product_by_name(db, product.name)

    if db_product:
        return db_product

    db_product = Product(name=product.name, brand=product.brand)
    db.add(db_product)
    db.commit()
    db.refresh(db_product
               )
    return db_product
