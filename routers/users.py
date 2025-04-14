from fastapi import APIRouter
from pydantic import field_validator

from schemas import UserCreateS
from dependencies import SessionDep
from crud import create_user_db



users_router = APIRouter(
    prefix="/user",
    tags=["users"],
    responses={
        404: {"description": "User не найден"},
        500: {"description": "Сервер лег"}
    }
)


@users_router.post("/create")
async def create_user(
        user: UserCreateS,
        db: SessionDep
):
    new_user = await create_user_db(user, db)
    return {"OK": True}


