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
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Book {self.title}>"