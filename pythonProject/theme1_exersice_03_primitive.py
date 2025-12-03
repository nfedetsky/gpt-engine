'''
Задача 3.
Решение для примитивного нейробота, который не умеет распознавать функции
'''
import os
from os import makedirs
from os import rename
from shutil import copy
from shutil import rmtree

path = os.path.join(f"C:\TMP", "test_folder")
makedirs(path)
soursePath = f"C:\TMP\example.txt"
destinationPath = path + f"\example.txt"
renFile = path + f"\copied_example.txt"

copy(soursePath, destinationPath)
rename(destinationPath, renFile)

try:
    rmtree(path)
except OSError as error:
    print(f"Ошибка при удалении директории '{DesPath}': {error}")

