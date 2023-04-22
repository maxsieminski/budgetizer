from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.dependencies import get_db
from api.security import verify_password, create_access_token

from schemas.user import UserCreate

import crud.user as crud

router = APIRouter()


@router.post("/register", status_code=201)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        return HTTPException(status_code=400, detail="Email already in database")

    return crud.create_user(db, user)


@router.post("/token", status_code=200)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.email})

    response = {
        "access_token": access_token,
        "token_type": "bearer"
    }

    return response
