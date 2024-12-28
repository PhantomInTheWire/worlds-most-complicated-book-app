from fastapi import FastAPI
from .books.routes import book_router
from fastapi import FastAPI
from .books.routes import book_router
from .auth.routes import auth_router
from .reviews.routes import review_router
from .tags.routes import tags_router
from .middleware import register_middleware
version = 'v1'
app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version=version,
)

register_middleware(app)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"/api/{version}/tags", tags=["tags"])