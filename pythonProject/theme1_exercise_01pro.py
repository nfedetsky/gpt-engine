'''
## Задача 1.

Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает
**именованные** аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, **при этом имена
аргументов следуют в алфавитном порядке (по возрастанию)**.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество
именованных аргументов.

Примечание 2. Следующий программный код:

```
info_kwargs(first_name='Иван', last_name='Иванов', age=36, job='Учитель')
```
Должен выводить:
```
age: 36
first_name: Иван
job: Учитель
last_name: Иванов
```
'''

#Solution

def info_kwards(**kwargs):
    argumentsSorted = sorted(kwargs.items())
    for key, value in argumentsSorted:
        print(f"{key} : {value}")

arguments = {}

while True:
    usersInputArgs = input("Введите аргументы в соответствии шаблону имя аргумента : значение аргумента: ").strip()
    if usersInputArgs == 'q' or usersInputArgs == ' ':
        break

    if ':' in usersInputArgs:
        getParts = usersInputArgs.split(':', 1)
        key = getParts[0].strip()
        value = getParts[1].strip()

        arguments[key] = value

info_kwards(**arguments)