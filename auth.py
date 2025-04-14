from fastapi import FastAPI, HTTPException, Response, Depends
from authx import AuthX, AuthXConfig

from pydantic import BaseModel, EmailStr

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_cook"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)


class UserLogin(BaseModel):
    name: str
    email: EmailStr
    password: str


@app.post("/login")
def login(creds: UserLogin, response: Response):
    if creds.name == "test" and creds.password == "test123" and creds.email == "test@gmail.com":
        token = security.create_access_token(uid="12")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect data")


@app.get("/prot", dependencies=[Depends(security.access_token_required)])
def prot():
    return {"data": "TOP SECRET"}
