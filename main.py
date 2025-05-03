from typing import Optional
from fastapi import FastAPI

from prisma import Prisma
from pydantic import BaseModel

app = FastAPI()


class CreatePostDTO(BaseModel):
    title: str
    content: Optional[str] = None
    published: bool


@app.get("/")
def list_posts():
    db = Prisma()
    db.connect()

    posts = db.post.find_many()

    db.disconnect()

    return posts


@app.post("/")
def create_post(dto: CreatePostDTO):
    db = Prisma()
    db.connect()

    post = db.post.create(data=dto.model_dump(exclude_none=True))

    db.disconnect()

    return post
