"""
Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает именованные аргументы 
в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов следуют в алфавитном порядке (по возрастанию).
Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество именованных аргументов.
Примечание 2. Следующий программный код:
info_kwargs(first_name='Михаил', last_name='Деркунов', age=36, job='Учитель')
Должен выводить:
age: 36
first_name: Михаил
job: Учитель
last_name: Деркунов
"""
def info_kwargs(**kwargs):
    sortedItems = sorted(kwargs.items())
    sortedByKeyDictionary = dict(sortedItems)
    
    for key, value in sortedByKeyDictionary.items():
        print(f"{key}: {value}")

info_kwargs(first_name='Михаил', last_name='Деркунов', age=36, job='Учитель')