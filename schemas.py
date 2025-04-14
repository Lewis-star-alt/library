from pydantic import BaseModel, EmailStr, field_validator, Field


# users
class UserCreateS(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password(self, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain uppercase letters")
        return v

class UserS(UserCreateS):
    id: int

    class Config:
        orm_mode = True



# books
class BookCreateS(BaseModel):
    title: str
    author: str
    description: str


class BookS(BookCreateS):
    id: int

    class Config:
        orm_mode = True


class BookUpdateS(BaseModel):
    title: str | None = None
    author: str | None = None
    description: str | None = None



# comments
class CommentCreateS(BaseModel):
    title: str
    content: str
    author: str


class CommentS(BookCreateS):
    id: int

    class Config:
        orm_mode = True


# pagination
class Pagination(BaseModel):
    size: int = Field(5)
    page: int = Field(0)