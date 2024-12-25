from typing import Optional
from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime

class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(default=None, primary_key=True, nullable=False)
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    user_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="user_accounts.uid")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def __repr__(self) -> str:
        return f"<Book {self.title}>"