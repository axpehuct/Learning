import json
from models import PrintedBook, EBook, Library, Reader
from datetime import date

class JsonStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_library(self, library):
        history = []
        for record in library.history:
            history.append({
                "date": record["date"].isoformat(),   
                "action": record["action"],           
                "book": record["book"].to_dict(),     
                "reader": {"name": record["reader"].name},  
            })
        data = {
            "books" : [b.to_dict() for b in library.books],
            "readers" : [r.to_dict() for r in library.readers],
            "history" : history
        }

        
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_library(self):
        library = Library()
        try:
            with open(self.filename, encoding="utf-8") as f:
                data =  json.load(f)
        except FileNotFoundError:
            print("Файл не найден")
            return Library()
        
        library.books = [book_from_dict(d) for d in data["books"]]
        for r in data["readers"]:
            reader = Reader(r["name"])
            for book_dict in r["borrowed"]:
                book = find_book_by_isbn(library.books, book_dict["isbn"])
                if book is not None:
                    reader.borrowed.append(book)
                else:
                    print(f"Предупреждение: книга isbn={book_dict['isbn']} "
                          f"в библиотеке не найдена, запись пропущена")
                    
            library.readers.append(reader)
        for record in data["history"]:  
            reader = find_reader_by_name(library.readers, record["reader"]["name"])
            if reader is not None:
                library.history.append({
                    "date": date.fromisoformat(record["date"]),
                    "action" : record["action"],
                    "book" : book_from_dict(record["book"]),
                    "reader" : reader
                })
            else:
                print(f"Не найден читатель с именем {record["reader"]["name"]}. Запись пропущена.")
        return library

def find_reader_by_name(readers, name):
    for r in readers:
        if r.name == name:
            return r
    return None

def find_book_by_isbn(books, isbn):
    for b in books:
        if b.isbn == isbn:
            return b
    return None

def book_from_dict(dictionary):
    kind = dictionary.pop("kind", None)
    if kind not in ["printed", "ebook"]:
        raise ValueError(f"Неизвестный kind. Kind = {kind}")
    cls = PrintedBook if kind == "printed" else EBook
    return cls(**dictionary)
        

