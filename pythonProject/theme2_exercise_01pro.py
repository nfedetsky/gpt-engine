'''
## Задача 1: Генератор степеней
Создайте функцию, которая принимает число (степень) и возвращает замыкание. Это замыкание должно принимать другое
число (основание) и возводить его в запомненную степень.
'''

def degreeGenerator(x):
    def basisFunc(y):
        return y ** x
    return basisFunc

preResult = degreeGenerator(int(input("Введите степень: ")))
result = preResult(int(input("Введите основание: ")))
print(result)