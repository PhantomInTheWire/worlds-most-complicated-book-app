from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.schemas import Book, BookUpdateModel, BookCreateModel, BookResponseModel
from src.books.service import BookService
from src.db.main import get_session
from typing import List
from uuid import UUID
from ..auth.dependencies import AccessTokenBearer, RoleChecker

book_router = APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(["admin", "user"]))

@book_router.get("/", response_model=List[BookResponseModel])
async def get_all_books(
        session: AsyncSession = Depends(get_session),
        token_details=Depends(access_token_bearer)
):
    books = await book_service.get_all_books(session)
    # Convert UUIDs to strings for response compatibility
    for book in books:
        if isinstance(book.uid, UUID):
            book.uid = str(book.uid)
    return books

@book_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Book,
    dependencies=[role_checker],
)
async def create_a_book(
    book_data: BookCreateModel,
    session: AsyncSession = Depends(get_session),
    token_details: dict = Depends(access_token_bearer),
) -> Book:
    user_id = token_details.get("user")["user_uid"]
    new_book = await book_service.create_book(book_data, user_id, session)
    if isinstance(new_book.uid, UUID):
        new_book.uid = str(new_book.uid)
    return new_book

@book_router.get("/{book_uid}", response_model=BookResponseModel)
async def get_book(
        book_uid: str,
        session: AsyncSession = Depends(get_session),
        token_details=Depends(access_token_bearer)
) -> BookResponseModel:
    book = await book_service.get_book(book_uid, session)
    if book:
        if isinstance(book.uid, UUID):
            book.uid = str(book.uid)
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.patch("/{book_uid}", response_model=BookResponseModel)
async def update_book(
        book_uid: str,
        book_update_data: BookUpdateModel,
        session: AsyncSession = Depends(get_session),
        token_details=Depends(access_token_bearer)
) -> BookResponseModel:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    else:
        if isinstance(updated_book.uid, UUID):
            updated_book.uid = str(updated_book.uid)
        return updated_book

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
        book_uid: str,
        session: AsyncSession = Depends(get_session),
        token_details=Depends(access_token_bearer)
) -> None:
    book_to_delete = await book_service.delete_book(book_uid, session)
    if book_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    else:
        return None
