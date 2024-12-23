from fastapi import FastAPI
from .books.routes import book_router
from .db.main import initdb
from fastapi import FastAPI
from .books.routes import book_router
from contextlib import asynccontextmanager


#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    await initdb()
    yield
    print("server is stopping")

version = 'v1'
app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version=version,
    lifespan=lifespan  # add the lifespan event to our application
)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])
