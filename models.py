from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Float


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)



class BookModel(Base):
    __tablename__ = "books"
    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)


class UserModel(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))



class CommentModel(Base):
    __tablename__ = "comments"
    title: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(String(50))
