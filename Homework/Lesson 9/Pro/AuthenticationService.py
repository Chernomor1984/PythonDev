from Database import Database
from Roles import BaseUser
from Roles import BaseUser
from Roles import Customer
from Roles import Admin
from Roles import UserType
import uuid

class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей
    """
    __session = {}
    __session_token = None
    
    def __fetchAllUsernames(self):
        return list(map(lambda user: user.username, Database.users))
    
    def __fetch_user(self, username: str) -> BaseUser:
        user = next((user for user in Database.users if user.username == username), None)
        return user
    
    def register(self, user_class: UserType, username, email, password, *args):
        if username in self.__fetchAllUsernames():
            return (f"Пользователь с именем {username} уже существует. Задайте другое имя или залогиньтесь")
        
        hashed_password = BaseUser.hash_password(password)
        
        match user_class:
            case UserType.Customer:
                address = args[0]
                user = Customer(username, email, hashed_password, address)
                Database.add_user(user)
            
            case UserType.Admin:
                admin_level = args[0]
                admin = Admin(username, email, hashed_password, admin_level)
                Database.add_user(admin)
                    
            case _:
                print(f"Что-то пошло не так и роли {user_class} не найдено")
                    
        userType = "юзер" if user_class == UserType.Customer else "админ"
        return f"Новый {userType} с ником {username} успешно зарегистрирован!"
    
    def login(self, username, password):
        if username not in self.__fetchAllUsernames():
            return f"Пользователь с ником {username} не найден"
        
        user = self.__fetch_user(username)
        
        if user is None:
            return f"Пользователь с ником {username} не найден"
        
        if BaseUser.check_password(user.password, BaseUser.hash_password(password)):
            self.__session_token = str(uuid.uuid4())
            self.__session[self.__session_token] = user
            return f"Пользователь с ником {username} успешно залогинен с токеном сессии {self.__session_token}"
        else:
            return "Вы ввели неверный пароль"
        
    def logout(self):
        if not self.__session:
            return "Нет активных сессий"
        
        currentActiveUsername = self.__session[self.__session_token].username
        self.__session.clear()
        self.__session_token = None
        return f"Пользователь с ником {currentActiveUsername} разлогинен"
    
    def get_current_user(self):
        if not self.__session:
            return "Нет активных сессий"
        
        currentActiveUsername = self.__session[self.__session_token].username
        return f"Текущий активный пользователь - {currentActiveUsername}"