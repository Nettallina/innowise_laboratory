from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

import models
import schemas
import crud
from db import SessionLocal, engine

# Создаем таблицы в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Collection API",
    description="API for managing book collections",
    version="1.0.0"
)

# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Book Collection API",
        "docs": "http://127.0.0.1:8080/docs",
        "endpoints": {
            "add_book": "POST /books/",
            "list_books": "GET /books/",
            "get_book": "GET /books/{id}",
            "update_book": "PUT /books/{id}",
            "delete_book": "DELETE /books/{id}",
            "search_books": "GET /books/search/"
        }
    }

@app.post("/books/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Добавить новую книгу в коллекцию"""
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить список всех книг с пагинацией"""
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """Получить книгу по ID"""
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    """Обновить информацию о книге"""
    db_book = crud.update_book(db, book_id=book_id, book_update=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу из коллекции"""
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.get("/books/search/", response_model=List[schemas.Book])
def search_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Поиск книг по названию, автору или году"""
    books = crud.search_books(
        db=db, 
        title=title, 
        author=author, 
        year=year, 
        skip=skip, 
        limit=limit
    )
    return books