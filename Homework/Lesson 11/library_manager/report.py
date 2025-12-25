from .catalog import Library
from .utils.formatting import format_book_data


def generate_report(library: Library) -> str:
    books = library.browse_books()

    if not books:
        return "В библиотеке нет книг"

    report = "В библиотеке найдены следующие книги:\n"

    for book in books:
        report += f"{format_book_data(book)}\n"

    return report
