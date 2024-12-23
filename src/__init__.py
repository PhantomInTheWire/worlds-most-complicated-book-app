from fastapi import FastAPI
from .books.routes import book_router
from fastapi import FastAPI
from .books.routes import book_router
from contextlib import asynccontextmanager
from .auth.routes import auth_router
version = 'v1'
app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version=version,
)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])