from library_manager.catalog import *
from library_manager.report import generate_report
from library_manager.utils.formatting import format_book_data


def __create_book__(*values) -> dict:
    number_of_values = len(values)

    if number_of_values != 3:
        raise ValueError(f"Ожидается три значения, получено {number_of_values}")

    return {
        "name": values[0],
        "author": values[1],
        "genre": values[2],
    }


library = Library()

twelve_chairs_dict = __create_book__("12 стульев", "Ильф и Петров", Genre.novel.value)
twelve_chairs = Book(twelve_chairs_dict)
library.add_book(twelve_chairs)

sherlok_dict = __create_book__("Шерлок Холмс", "Конан Дойл", Genre.detective.value)
sherlok = Book(sherlok_dict)
library.add_book(sherlok)

war_and_peace_dict = __create_book__("Война и мир", "Толстой", Genre.classic.value)
war_and_peace = Book(war_and_peace_dict)
library.add_book(war_and_peace)

report = generate_report(library)
print(report)

library.delete_book(war_and_peace)

print("После удаления:")
report = generate_report(library)
print(report)

twelve = library.find_book_by("12 стульев", "name")[0]

if twelve is not None:
    description = format_book_data(Book.transform(twelve))
    print(f"Надйена книга: {description}")

sherlok = library.find_book_by("Конан Дойл", "author")[0]

if sherlok is not None:
    description = format_book_data(Book.transform(sherlok))
    print(f"Надйена книга: {description}")
