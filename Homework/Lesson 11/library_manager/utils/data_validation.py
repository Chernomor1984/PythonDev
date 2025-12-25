def validate_book_data(data: dict) -> bool:
    name = data["name"]
    author = data["author"]
    genre = data["genre"]

    if not __value_is_string_and_not_empty__(name):
        return False

    if not __value_is_string_and_not_empty__(author):
        return False

    return len(genre) > 0


def __value_is_string_and_not_empty__(value) -> bool:
    return isinstance(value, str) and value
