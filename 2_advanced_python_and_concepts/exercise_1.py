from pydantic import BaseModel
from typing import List, Optional


class Comment(BaseModel):
    author: str
    comment: str
    likes: int


class Post(BaseModel):
    author: str
    co_author: Optional[str] = None
    date: str
    title: str
    content: str
    id: int
    likes: List[str]
    comments: List[Comment]


comments = [
    Comment(author="johndoe", comment="This is a comment!", likes=2),
    Comment(author="max", comment="This is a comment!", likes=10)
]

post = Post(author="johndoe",
            co_author="janedoe",
            date="1/1/1970",
            title="Cool post",
            content="Cool content",
            id=10101,
            likes=["johndoe", "janedoe"],
            comments=comments)
print(post)
