import hashlib
from Database import Database
from enum import Enum

# Имя пришлось поменять из-за конфликта имён
# https://stackoverflow.com/questions/24348462/class-named-user-error-object-has-no-attribute-for-any-method
class BaseUser:
    """
    Базовый класс, представляющий пользователя.
    """
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def get_details(self):
        return f"Класс {type(self)}: username {self.username}, email {self.email}, password {self.password})"
    
    @staticmethod
    def hash_password(password: str):
        encoded_data = password.encode("utf-8")
        hash_object = hashlib.sha256(encoded_data)
        hex_digest = hash_object.hexdigest()
        return hex_digest

    @staticmethod
    def check_password(storedPassword, providedPassword):
        """
        Проверка пароля
        """
        return storedPassword == providedPassword
    
class Customer(BaseUser):
    """
    Класс, представляющий клиента
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address
       
    def get_details(self):
        description = super().get_details()
        description += ", "
        description += f"address {self.address}"
        return description
        
class Admin(BaseUser):
    """
    Класс, представляющий администратора
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level
        
    def get_details(self):
        description = super().get_details()
        description += ", "
        description += f"admin_level {self.admin_level}"
        return description
        
    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        for user in Database.users:
            print(user.get_details())
        
    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """
        user = next((user for user in Database.users if user.username == username), None)
        
        if user is not None:
            Database.remove_user(user)
        
class UserType(Enum):
    Customer = "Customer"
    Admin = "Admin"