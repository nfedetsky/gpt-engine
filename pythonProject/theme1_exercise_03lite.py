'''
## Задача 3: Использование модуля random

Напишите программу, которая генерирует список из 10 случайных чисел от 1 до 100, а затем находит их максимум, минимум и среднее.

Результат выпонения может быть примерно такой:
```python
Случайные числа: [47, 1, 48, 15, 6, 16, 4, 97, 44, 32]
Максимум: 97
Минимум: 1
Среднее: 31.0
```

'''

import random
from statistics import mean

randomGeneric = [random.randint(1, 100) for _ in range(10)]

print(f"Случайные числа: {randomGeneric}")
print(f"Максимум: {max(randomGeneric)}")
print(f"Минимум: {min(randomGeneric)}")
print(f"Среднее: {mean(randomGeneric)}")
