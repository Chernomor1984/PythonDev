"""
Создайте функцию "list_expert()", которая будет принимать неограниченное количество параметров и если передали числа, 
то вернуть их сумму, а если есть другие типы, то вывети списком их типы. Но если ввести 1 параметр, то его же и вывести.
Вывод:
list_expert(1,2,3,4,5)  # 15
list_expert("a", True, [1, 2, 3])  # ['str', 'bool', 'list']
list_expert("obj")  # obj
"""
"""
Задание 3
Допишите функцию из 2-го задания, чтобы, когда не передали вообще параметров, то она вернет строку "Пустая функция".
"""

def list_expert(*args):
    if len(args) == 0:
        return "Пустая функция"
    
    if len(args) == 1:
        return args[0]

    if all(isinstance(value, (int, float)) for value in args):
        return sum(args)
    else:
        lambda_type = lambda a: type(a)
        return list(map(lambda_type, args))
    
print(list_expert(1,2,3,4,5))
print(list_expert("a", True, [1, 2, 3]))
print(list_expert("obj"))
print(list_expert())