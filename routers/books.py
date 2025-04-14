from fastapi import HTTPException, Query, APIRouter




from schemas import BookCreateS, BookUpdateS
from dependencies import SessionDep, PaginationDep
from crud import create_book_db, get_book_db, del_book_db, update_book_db, full_update_book_db, get_books_db


book_router = APIRouter(
    prefix="/book",
    tags=["books"],
    responses={
        404: {"description": "Ресурс не найден"},
        500: {"description": "Ошибка сервера"}
    }

)


@book_router.post("/create")
async def create_book(book: BookCreateS, db: SessionDep):
    new_book = await create_book_db(book, db)
    return {"OK": True}



@book_router.get("/get/{book_id}")
async def get_book(book_id: int, db: SessionDep):
    book = await get_book_db(db, book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Not found")


@book_router.delete("/del/{book_id}")
async def del_book(book_id: int, db: SessionDep):
    await del_book_db(book_id, db)
    return {"OK": True}


@book_router.patch("/update/{book_id}")
async def update_book(
        book_id: int,
        book_data: BookUpdateS,
        db: SessionDep
):
    book = await update_book_db(book_id, book_data, db)
    return book


@book_router.put("/full_update/{book_id}")
async def full_update_book(
        book_id: int,
        book_data: BookCreateS,
        db: SessionDep
):
    book = await full_update_book_db(book_id, book_data, db)
    return book


@book_router.get("/get_all")
async def get_books(
        db: SessionDep,
        pag: PaginationDep
):
    books = await get_books_db(db, pag)
    return books
