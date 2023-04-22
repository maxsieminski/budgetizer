from typing import Annotated

from fastapi import APIRouter, Depends

from crud.user import get_current_user
from models.user import User


router = APIRouter()


@router.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
