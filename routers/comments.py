from fastapi import APIRouter


from schemas import CommentCreateS
from dependencies import SessionDep
from crud import create_comment_db



comments_router = APIRouter(
    prefix="/comments",
    tags=["comments"],
    responses={
        404: {"description": "Комментарий не найден"},
        500: {"description": "Сервер лег"}
    }
)


@comments_router.post("/create")
async def create_comment(
        comment: CommentCreateS,
        db: SessionDep
):
    new_comment = await create_comment_db(comment, db)
    return {"OK": True}

