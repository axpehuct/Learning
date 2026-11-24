from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date

@dataclass
class Book(ABC):
    title: str
    author: str
    isbn: str
    available: bool

    @abstractmethod
    def __str__(self):
        return f"Автор: {self.author} Название: {self.title} Код: {self.isbn}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
        }

    
@dataclass
class PrintedBook(Book):
    pages: int
    cover_type: str

    def __str__(self):
        return f"Автор: {self.author} Название: {self.title} Код: {self.isbn} Страниц: {self.pages}"
    
    def to_dict(self):
        base_dict = super().to_dict()
        return base_dict | {
            "pages": self.pages,
            "cover_type": self.cover_type,
            "kind": "printed"
            }

@dataclass
class EBook(Book):
    size_mb: float
    format: str #pdf, epub

    def __str__(self):
        return f"Автор: {self.author} Название: {self.title} Код: {self.isbn} Размер: {self.size_mb} Формат: {self.format}"

    def to_dict(self):
        base_dict = super().to_dict()          
        return base_dict | {
            "size_mb": self.size_mb,
            "format": self.format,
            "kind": "ebook"
            }

class Reader:
    MAX_BOOKS = 3
    def __init__(self, name, borrowed = None):
        self.name = name
        self.borrowed = borrowed if borrowed is not None else []

    def borrow_book(self, book) -> bool:
        if len(self.borrowed) < self.MAX_BOOKS:
            self.borrowed.append(book)
            return True
        return False

    def return_book(self, book) -> bool:
        if book in self.borrowed:
            self.borrowed.remove(book)
            return True
        return False
    
    def __eq__(self, other):
        if not isinstance(other, Reader):
            return False
        return self.name == other.name

    def to_dict(self):
        return {
            "name": self.name,
            "borrowed": [b.to_dict() for b in self.borrowed]
        }


class Library:
    def __init__(self, books = None, readers = None, history = None):
        self.books = books if books is not None else []
        self.readers = readers if readers is not None else []
        self.history = history if history is not None else []

    def add_book(self, book) -> bool:
        if book not in self.books:
            self.books.append(book)
            return True
        return False

    def register_reader(self, reader) -> bool:
        if reader not in self.readers:
            self.readers.append(reader)
            return True
        return False

    def find(self, title) -> list[Book]:
        return [book for book in self.books if title.lower() in book.title.lower()]

    def lend(self, book, reader) -> bool:
        if book in self.books and book.available:
            if reader in self.readers and reader.borrow_book(book):
                book.available = False
                self.history.append({"date":date.today(), "action":"Выдача", "book":book, "reader":reader})
                return True
        return False

    def accept_return(self, book, reader) -> bool:
        if reader.return_book(book):
            book.available = True
            self.history.append({"date":date.today(), "action":"Возврат", "book":book, "reader":reader})
            return True
        return False

        
        
        





