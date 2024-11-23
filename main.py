from typing import Optional
from fastapi import FastAPI
from prisma import Prisma
from pydantic import BaseModel

class CreatePostDto(BaseModel):
    title : str
    content: Optional[str] = None
    published: bool

app = FastAPI()

@app.get("/")
def list_posts():
    # instance of prisma in db
    db = Prisma()
    # connect to db
    db.connect()

    posts = db.post.find_many()

    # disconnect db
    db.disconnect()
    return posts

@app.post("/")
def create_post(dto : CreatePostDto):
    # instance of prisma in db
    db = Prisma()
    # connect to db
    db.connect()

    posts = db.post.create(
        data = dto.model_dump(exclude_none=True)
    )

    # disconnect db
    db.disconnect()

    return posts

