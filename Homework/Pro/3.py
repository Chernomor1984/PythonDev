"""
Напишите функцию замыкание, для решения по заданному условию, типа:
a*x^2 + b*x + c = 0
D = b^2 - 4*a*c
Если D будет возвращать значение <=0, тогда выводить (f"Результата не будет, потому что D = {D}")
Иначе выводить результат первого примера
Примечание. Во внешнюю функцию будет поступать 3 параметра, а во внутренюю 1.
"""
def calcDiscriminant(a: int | float, b: int | float, c: int | float):
    D = b**2 - 4 * a * c
    def calsQuadraticEquation(x: int | float):
        if D <= 0:
            print(f"Результата не будет, потому что D = {D}")
        else:
            result = a * x**2 + b * x + c
            print(f"result = {result}")
    
    return calsQuadraticEquation

calsQuadraticEquation = calcDiscriminant(3, 9 , 1)
calsQuadraticEquation(2)
calsQuadraticEquation = calcDiscriminant(2, 3 , 4)
calsQuadraticEquation(2)