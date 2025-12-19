def validate_user_input(data: dict):
    if not isinstance(data, dict):
        raise TypeError(f"{data} не является словарём") 
    
    if "name" not in data:
        raise ValueError("Ключ \'name' должен быть в словаре")
    
    if not isinstance(data["name"], str):
        raise ValueError(f"Значение по ключу \'name' должно быть строкой")
    
    if "age" not in data:
        raise ValueError("Ключ \'age' должен быть в словаре")
    
    ageValue = data["age"]
    
    if not isinstance(ageValue, int) or ageValue <= 0:
        raise ValueError(f"Значение по ключу \'age' должно быть положительным целым числом")

def validate_user_input_wrapper(data):
    try:
        validate_user_input(data)
    except TypeError as te:
        raise TypeError("Неверный формат входных данных") from te
    except ValueError as ve:
        raise ValueError("Входные данные невалидны") from ve
    except Exception as e:
        raise Exception("Что-то пошло не так") from e
    
def validate_data(data: dict):
    try:
        validate_user_input_wrapper(data)
    except Exception as e:
        print(f"{e}: {e.__cause__}")
    
data = {
    "name": "Johnny",
    "age": 25
}
validate_data(data)

data = "some text"
validate_data(data)

data = {
    "last_name": "Johnny",
    "age": 25
}
validate_data(data)

data = {
    "name": ["Johnny"],
    "age": 25
}
validate_data(data)

data = {
    "name": "Johnny",
    "years": 25
}
validate_data(data)

data = {
    "name": "Johnny",
    "age": 34.5
}
validate_data(data)

data = {
    "name": "Johnny",
    "age": (1, 2)
}
validate_data(data)