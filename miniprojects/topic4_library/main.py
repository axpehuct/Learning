from storage import JsonStorage
from models import PrintedBook, EBook, Reader, Library

# library = Library()
# 
storage = JsonStorage("Library_storage.json")
library = storage.load_library()

def show_menu():
    while True:
        value = read_int("Выберите пункт из меню:\n" 
        "1. Добавить книгу.\n" 
        "2. Зарегистрировать читателя.\n" 
        "3. Выдать книгу читателю.\n" 
        "4. Забрать книгу у читателя.\n"
        "5. Найти книгу.\n"
        "6. Посмотреть историю.\n"
        "7. Сохранить и выйти. \n"
        )
        match value:
            case 1: add_book_flow()
            case 2: add_reader_flow()
            case 3: lend_book_flow()
            case 4: accept_return_flow()
            case 5: find_book_flow()
            case 6: show_history_flow()
            case 7: 
                storage.save_library(library) 
                print("Библиотека сохранена. До свидания.")
                break
            case _: print("Неправильный пункт меню. Попробуйте еще раз.")
        
    

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Введено не число. Попробуйте еще раз.")

def read_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Введено не число. Попробуйте еще раз.")

def show_history_flow():
    for h in library.history:
        print("--------------------")
        print(f"Дата {h["date"]}")
        print(f"Действие {h["action"]}")
        print(f"Книга {h["book"]}")
        print(f"Читатель {h["reader"].name}")

def find_book_flow():
    title = input("Введите название книги которое хотите найти.")
    books = library.find(title)
    if len(books) == 0:
        print("Не найдена ни одна книга")
    else:
        for book in books:
            print(book)


def accept_return_flow():
    if library.readers == []:
        print("Нет зарегистрированных читателей у кого можно забрать книгу.")
        return
    for i in range(len(library.readers)):
            print(f"{i+1}. {library.readers[i].name}")
    while True:
        chosen_reader = read_int("Выберите читателя введя его порядковый номер: ")
        if chosen_reader - 1 in range(len(library.readers)):
            break
    print("Вот список книг читателя:")
    if len(library.readers[chosen_reader-1].borrowed) == 0:
           print("У читателя нет книг.")
           return
    for i in range(len(library.readers[chosen_reader-1].borrowed)):
            print(f"{i+1}. {library.readers[chosen_reader-1].borrowed[i]}")
    while True:
        chosen_book = read_int("Выберите книгу введя ее порядковый номер: ")
        if chosen_book - 1 in range(len(library.readers[chosen_reader-1].borrowed)):
            if library.accept_return(library.readers[chosen_reader-1].borrowed[chosen_book-1], library.readers[chosen_reader-1]):
                print("Книга забрана успешно.")
                break
            else:
                print("Произошла ошибка.")
    

def lend_book_flow():
    if library.readers == [] or library.books == []:
        print("Нет зарегистрированных читателей или книг.")
        return
    for i in range(len(library.readers)):
        print(f"{i+1}. {library.readers[i].name}")
    while True:
        chosen_reader = read_int("Выберите читателя введя его порядковый номер: ")
        if chosen_reader - 1 in range(len(library.readers)):
            break

    book_name = input("Введите название книги, которую хотите взять: ")
    book_list = library.find(book_name)
    print("Найдены следующие книги схожие по названию: \n")
    if len(book_list) == 0:
        print("Похожих книг нет.")
        return
    for i in range(len(book_list)):
        print(f"{i+1}. {book_list[i]}")
    while True:
        chosen_book = read_int("Выберите книгу введя ее порядковый номер: ")
        if chosen_book - 1 in range(len(book_list)):
            if library.lend(book_list[chosen_book-1], library.readers[chosen_reader-1]):
                break
            else:
                print("Произошла ошибка, книга занята или превышен лимит книг на человека.")
                return
    print(f"Книга {book_list[chosen_book-1]} выдана {library.readers[chosen_reader-1].name}")


def add_reader_flow():
    name = input("Введите имя читателя: ")
    if library.register_reader(create_reader(name)):
        print("Читатель успешно зарегистрирован.")
    else:
        print("Произошла ошибка читатель с таким именем уже есть")

def create_reader(name) -> Reader:
    return Reader(name)

def add_book_flow():
    while True:
        value = read_int("Книга электронная(1)/печатная(2)? ")
        if value in (1, 2):
            break
    match value:
        case 1: result = library.add_book(create_ebook())
        case 2: result = library.add_book(create_printed_book())
    if result:
        print(f"Книга успешно добавлена в библиотеку")
    else:
        print(f"Книга уже есть в библиотеке.")

def create_ebook() -> EBook:
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    isbn = input("Введите номер isbn книги: ")
    size_mb = read_float("Введите размер книги: ")
    book_format = input("Введите формат книги pdf/epub: ")
    return EBook(title, author, isbn, True, size_mb, book_format)

def create_printed_book() -> PrintedBook:
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    isbn = input("Введите номер isbn книги: ")
    pages = read_int("Введите кол-во страниц книги: ")
    cover_type = input("Какой переплет у книги?(твердый/мягкий): ")
    return PrintedBook(title, author, isbn, True, pages, cover_type)


if __name__ == "__main__":
    show_menu()