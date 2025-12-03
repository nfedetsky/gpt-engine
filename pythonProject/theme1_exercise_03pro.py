'''
## Задача 3: Использование модуля shutil

Напишите программу, которая:

- Создаёт папку test_folder и копирует туда текстовый файл example.txt (создайте файл вручную в Colab).
- Переименовывает скопированный файл на copied_example.txt.
- Удаляет папку test_folder со всем её содержимым.

Результат выпонения может быть примерно такой:
```python
Файл 'example.txt' скопирован в папку 'test_folder'.
Файл переименован в 'test_folder/copied_example.txt'.
Папка 'test_folder' удалена.
```.
'''
import os
import time
from os import makedirs
from os import rename
from shutil import copy
from shutil import rmtree

DesPath: str
exapleFile: str

#Функция создания директории test_folder
def CreateFolder(workspace):
    path = os.path.join(workspace, "test_folder")
    if not os.path.exists(path):
        makedirs(path)
        print("Создана директория ", path)
    else:
        print("Такая директория уже существует")
    global DesPath
    DesPath = path

#Функция копирования файла example.txt
def copyFile(soursePath, destinationPath):
    copy(soursePath, destinationPath)
    global exapleFile
    exapleFile = soursePath.rsplit('\\', 1)[-1]
    print(f"Файл {exapleFile} скопирован")


#Функция переименования файла example.txt
def fileRename():
    oldFileName = DesPath + '\\' + exapleFile
    newFileName = DesPath + '\\' + "copied_" + exapleFile
    rename(oldFileName, newFileName)
    print(f"Файл {exapleFile} переименован в " + "copied_" + exapleFile)


#Функция обратного отчета времени до удаления директории test_folder с содержащимся в ней файлом example.txt
def deathCountdown():
    t = 30
    while t >= 0:
        print(f"\r До удаления директории test_folder осталось: {t} секунд", end=" ", flush=True)
        time.sleep(1)
        t -= 1
    print("\n Бах!")


#Основные команды работы с директорией и файлом
CreateFolder(input("Введите путь, где будет создана директория test_folder: "))
getSoursePath = input("Введите путь вместе с файлом от куда желаете скопировать файл: ")
getDestinationPath = DesPath + '\\' + getSoursePath.rsplit('\\', 1)[-1]
copyFile(getSoursePath, getDestinationPath)
fileRename()
deathCountdown()
try:
    rmtree(DesPath)
except OSError as error:
    print(f"Ошибка при удалении директории '{DesPath}': {error}")



