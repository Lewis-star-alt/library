from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

path = os.getenv("DB_URL")
engine = create_async_engine(url=path, echo=True)
SessionLoc = async_sessionmaker(bind=engine, expire_on_commit=True, autoflush=False)


async def get_session():
    async with SessionLoc() as session:
        yield session