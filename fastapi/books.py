from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "category": "Fiction"},
    {"id": 2, "title": "Book 2", "author": "Author 2", "category": "Non-Fiction"},
    {"id": 3, "title": "Book 3", "author": "Author 3", "category": "Fiction"},
    {"id": 4, "title": "Book 4", "author": "Author 4", "category": "Science"},
    {"id": 5, "title": "Book 5", "author": "Author 5", "category": "History"},
    {"id": 6, "title": "Book 6", "author": "Author 6", "category": "Fiction"},
]

# GET Operation
@app.get("/books")
def read_all_books():
    """Fetch books"""
    return BOOKS

# path parameters
@app.get("/books/{book_id}")
def read_book(book_id: int):
    """Fetch a book by ID"""
    for book in BOOKS:
        if book.get("id") == book_id:
            return book
    return {"error": "Book not found"}

# Query parameters
@app.get("/books/")
def read_books_by_category(category: str):
    """Fetch books by category"""
    book_to_return = []
    for book in BOOKS:
        if book.get("category") == category:
            book_to_return.append(book)
    return book_to_return

# POST Operation
@app.post("/books/create_book")
def create_book(book: dict = Body(...)):
    """Create a new book"""
    BOOKS.append(book)

# PUT Operation
@app.put("/books/update_book")
def update_book(updated_book: dict = Body(...)):
    """Update a book by ID"""
    for index, book in enumerate(BOOKS):
        if book.get("id") == updated_book.get("id"):
            BOOKS[index] = updated_book
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}

# DELETE Operation
@app.delete("/books/delete_book/{book_id}")
def delete_book(book_id: int):
    """Delete a book by ID"""
    for index, book in enumerate(BOOKS):
        if book.get("id") == book_id:
            BOOKS.pop(index)
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}
