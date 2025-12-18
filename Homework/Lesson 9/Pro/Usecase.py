import Database
from Roles import BaseUser
from Roles import Customer
from Roles import Admin
from Roles import UserType
from AuthenticationService import AuthenticationService
 
authService = AuthenticationService()
# Успешная регистрация
print(authService.register(UserType.Customer, "johnny", "johnny@gmail.com", "qwerty", "Main str., London"))
print(authService.register(UserType.Customer, "billy", "billy@gmail.com", "asdqwe", "Bristol road, Liverpool"))
print(authService.register(UserType.Admin, "maxy", "max_admin@gmail.com", "qaz123", 5))
# Повторная регистрация уже зареганного юзера 
print(authService.register(UserType.Customer, "johnny", "johnny@gmail.com", "qwerty", "Main str., London"))
# Список всех пользователей
Admin.list_users()
# Логин зарегистрированного юзера с верным паролем
print(authService.login("johnny", "qwerty"))
# Логин зарегистрированного юзера с неверным паролем
print(authService.login("johnny", "sdfsdf"))
# Логин незарегистрированного юзера
print(authService.login("donny", "qwerty"))
# Текущий юзер
print(authService.get_current_user())
# Разлогин
print(authService.logout())
print(authService.logout())
# Логин другого юзера
print(authService.login("billy", "asdqwe"))
# Разлогин
print(authService.logout())
