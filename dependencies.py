from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from typing import Annotated
from database import get_session
from schemas import Pagination

SessionDep = Annotated[AsyncSession, Depends(get_session)]
PaginationDep = Annotated[Pagination, Depends(Pagination)]