from enum import Enum


class UserAlreadyExistsError(Exception):
    def __init__(self, username):
        super().__init__()
        self.__username = username

    def __str__(self):
        return (
            f"Возникла ошибка: пользователь с именем {self.__username} уже существует"
        )


class UserNotFoundError(Exception):
    def __init__(self, username):
        super().__init__()
        self.__username = username

    def __str__(self):
        return f"Возникла ошибка: пользователь с именем {self.__username} не найден"
