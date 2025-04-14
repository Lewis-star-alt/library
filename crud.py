from fastapi import Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from models import BookModel, UserModel, CommentModel
from schemas import BookCreateS, BookUpdateS, UserCreateS, CommentCreateS
from dependencies import SessionDep, PaginationDep


# books
async def create_book_db(book: BookCreateS, db: SessionDep):
    new_book = BookModel(
        title=book.title,
        author=book.author,
        description=book.description
    )
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book


async def get_books_db(
        db: SessionDep,
        pag: PaginationDep
):
    offset = (pag.page - 1) * pag.size
    result = await db.execute(
        select(BookModel)
        .offset(offset)
        .limit(pag.size)
    )
    return result.scalars().all()

async def get_book_db(db: AsyncSession, book_id: int):
    st = select(BookModel).where(BookModel.id == book_id)
    res = await db.execute(st)
    return res.scalar_one_or_none()


async def update_book_db(
        book_id: int,
        book_data: BookUpdateS,
        db: SessionDep
):

    result = await db.execute(
        select(BookModel).where(BookModel.id == book_id)
    )
    book = result.scalar_one_or_none()

    if book:
        update_data = book_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(book, key, value)

        await db.commit()
        await db.refresh(book)
        return book


async def full_update_book_db(
        book_id: int,
        book_data: BookCreateS,
        db: SessionDep
):
    result = await db.execute(
        select(BookModel).where(BookModel.id == book_id)
    )
    book = result.scalar_one_or_none()

    if book:
        for key, value in book_data.dict().items():
            setattr(book, key, value)
        await db.commit()
        await db.refresh(book)
        return book



async def del_book_db(book_id: int, db: SessionDep):
    result = await db.execute(
        select(BookModel).where(BookModel.id == book_id)
    )
    book = result.scalar_one()
    if book:
        await db.delete(book)
        await db.commit()


# users

async def create_user_db(
        user: UserCreateS,
        db: SessionDep
):
    new_user = UserModel(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user



# comments

async def create_comment_db(
        comment: CommentCreateS,
        db: SessionDep
):
    new_comment = CommentModel(
        title=comment.title,
        content=comment.content,
        author=comment.author
    )
    db.add(new_comment)
    await db.commit()
    await db.refresh(new_comment)
    return new_comment