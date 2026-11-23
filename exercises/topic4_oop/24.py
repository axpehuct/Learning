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
print(war_and_peace)
print(dads_and_sons)

                
