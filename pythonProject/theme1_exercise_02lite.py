'''
## Задача 1.
Создайте функцию "list_expert()", которая будет принимать неограниченное количество параметров и если передали числа,
то вернуть их сумму, а если есть другие типы, то вывети списком их типы. Но если ввести 1 параметр, то его же и вывести.

Вывод:
```
list_expert(1,2,3,4,5)  # 15
list_expert("a", True, [1, 2, 3])  # ['str', 'bool', 'list']
list_expert("obj")  # obj
```
## Задача 2

Допишите функцию из 1-го задания, чтобы, когда не передали вообще параметров, то она вернет строку "Пустая функция".
'''

def list_expert(*args):
    getDataList = args

    resultList = all(isinstance(x, int) for x in getDataList)

    if resultList == True and len(getDataList) > 1:
        print(f"list_expert(1, 2, 3, 4, 5)  # {sum(getDataList)}")
    elif resultList == False and len(getDataList) > 1:
        print(f"list_expert('a', True, [1, 2, 3])  # {[type(n).__name__ for n in getDataList]}")
    elif len(getDataList) == 1:
        print(f"list_expert('obj')  # " + " ".join(map(str, getDataList)))
    elif not getDataList:
        print("Пустая функция")


list_expert(1, 2, 3, 4, 5)
list_expert("a", True, [1, 2, 3])
list_expert("obj")
list_expert()