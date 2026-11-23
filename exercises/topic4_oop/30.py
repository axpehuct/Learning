from abc import ABC, abstractmethod
class Shelf:
    def __init__(self, books=None):
        self.books = list(books) if books is not None else []

    def add(self, Book):
        self.books.append(Book)

    def __len__(self):
        return len(self.books)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

    def __str__(self):
        return f"\"{self.title}\", {self.author}, {self.pages} стр."

war_and_peace = Book("Война и мир", "Л. Толстой", 1225)
dads_and_sons = Book("Отцы и дети", "Тургенев", 200)

shelf = Shelf()
shelf.add(war_and_peace)
shelf.add(dads_and_sons)
print(len(shelf))