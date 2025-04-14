from fastapi import FastAPI
import uvicorn


from database import engine
from models import Base
from routers import books, users, comments
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
app.include_router(books.book_router)
app.include_router(users.users_router)
app.include_router(comments.comments_router)


@app.on_event("startup")
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=os.getenv("DEBUG")
    )

