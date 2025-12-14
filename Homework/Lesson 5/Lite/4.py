"""
Создайте функцию "random_numbers()", которая будет формировать список случайных чисел и принимать 3 параметра:
число повторений (сколько чисел будет в списке)
количество знаков после запятой
сортировать или нет (со значением по умолчанию)
Написать декоратор для этой функции, который будет выводить параметры этой функции.
"""
import random

def randomNumbersDecorator(function):
    def wrapper(*args, **kwargs):
        print(f"Аргументы функции {function.__name__}: {args, kwargs}")
        return function(*args, **kwargs)
    return wrapper

@randomNumbersDecorator
def random_numbers(length: int, decimalPoints: int, sorted: bool = False):
    if length <= 0:
        raise ValueError
    
    randomNumbers = []

    for _ in range(length):
        randomValue = round(random.uniform(0, 1000), decimalPoints)
        randomNumbers.append(randomValue)
    
    if sorted:
        randomNumbers.sort()

    return randomNumbers

print(random_numbers(5, 2, sorted=True))
