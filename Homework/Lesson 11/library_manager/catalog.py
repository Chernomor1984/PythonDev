from enum import Enum
from .utils.data_validation import validate_book_data


class Genre(Enum):
    classic = "Классическая литература"
    detective = "Детектив"
    fantasy = "Фэнтэзи"
    horror = "Ужастик"
    psychology = "Психология"
    science = "Наука"
    novel = "Роман"


class Book:
    def __init__(self, data: dict):
        self.__name = data["name"]
        self.__author = data["author"]
        self.__genre = data["genre"]

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    def transform(self) -> dict:
        return {"name": self.name, "author": self.author, "genre": self.genre}


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        if validate_book_data(Book.transform(book)):
            self.__books.append(book)
        else:
            raise ValueError("Данные не валидны")

    def delete_book(self, book: Book):
        foundIndex = next(
            (
                index
                for index, item in enumerate(self.__books)
                if item.name == book.name
            ),
            None,
        )

        if foundIndex is not None:
            del self.__books[foundIndex]

    def find_book_by(self, value: str, search_key: str) -> list:
        books = None

        match search_key:
            case "name":
                books = [item for item in self.__books if item.name == value]
            case "author":
                books = [item for item in self.__books if item.author == value]
            case "genre":
                books = [item for item in self.__books if item.genre == value]

        return books

    def browse_books(self) -> list:
        return list(map(lambda item: Book.transform(item), self.__books))
