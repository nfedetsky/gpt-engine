'''
## Задача 1: Создание счетчика

Создайте функцию create_counter, которая принимает начальное значение start и возвращает внутреннюю функцию increment.

Каждый вызов increment должен увеличивать значение счетчика на 1 и возвращать новое значение.

Используйте ключевое слово nonlocal для изменения свободной переменной.

Реализуйте два различных счетчика с разными начальными значениями
'''

def create_counter(start):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_1 = create_counter(0)
counter_2 = create_counter(10)

for i in range(10):
    print(f"Вызов {i + 1} результат  для Счетчика 1: {counter_1()}, результат для Счетчика 2: {counter_2()}")
