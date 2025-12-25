def format_book_data(data: dict) -> str:
    name = data["name"]
    author = data["author"]
    genre = data["genre"]
    return f"Название: {name}, автор: {author}, жанр: {genre.lower()}"
