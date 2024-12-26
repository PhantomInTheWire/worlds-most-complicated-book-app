from typing import List

from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from src.db.models import Review


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class BookCreateModel(BaseModel):
    """
        This class is used to validate the request when creating or updating a book
    """
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookResponseModel(BaseModel):
    uid: UUID
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime
    reviews: List[Review]


    class Config:
        orm_mode = True
