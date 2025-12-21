from UserDefinedExceptions import UserAlreadyExistsError
from UserDefinedExceptions import UserNotFoundError


class User:
    def __init__(self, username: str, email: str, age: int):
        self.__username = username
        self.__email = email
        self.__age = age

    def __str__(self):
        return f"пользователь {self.__username}: возраст {self.__age}, email {self.__email}"

    @property
    def username(self):
        return self.__username


class UserManager:
    def __init__(self):
        self.__users = {}

    def add_user(self, user: User):
        usernames = self.__users.keys()
        current_username = user.username

        if current_username in usernames:
            raise UserAlreadyExistsError(current_username)
        else:
            self.__users[current_username] = user
            print(f"Добавлен {user}")

    def remove_user(self, username: str):
        usernames = self.__users.keys()

        if username not in usernames:
            raise UserNotFoundError(username)
        else:
            user = self.__users[username]
            print(f"Удалён {user}")
            del self.__users[username]

    def find_user(self, username: str) -> User:
        usernames = self.__users.keys()

        if username not in usernames:
            raise UserNotFoundError(username)
        else:
            user = self.__users[username]
            print(f"Найден {user}")
            return user
