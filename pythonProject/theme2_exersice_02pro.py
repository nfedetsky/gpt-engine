'''
## Задача 2: Использование декоратора

Напишите декоратор execution_timer, который измеряет время выполнения функции. Примените его к функции, вычисляющей
сумму квадратов чисел от 1 до 1 000 000.

Результат выпонения может быть примерно такой:
```python
Время выполнения функции 'calculate_sum_of_squares': 0.3372 секунд
Результат: 333333833333500000
```
'''
import time

def execution_timer(func):
    def wrapper(*args):
        startTime = time.perf_counter()
        result = func(*args)
        endTime = time.perf_counter()
        resultTime = endTime - startTime
        print(f"Время выполнения функции 'calculate_sum_of_squares': {resultTime:.4f} секунд")
        print((f"Результат: {result}"))
        return result
    return wrapper

@execution_timer
def sumOfSquares(n : int):
    getSumOfSquares = sum(x ** 2 for x in range(1, n + 1))
    return getSumOfSquares

result = sumOfSquares(1000000)