# Задайте список из N элементов, з
# аполненных числами из промежутка [-N, N]. 
# сохраните список в формате JSON. ( добавить в txt )

import json
from os import lstat 
n = int(input( ' введите число n -> '))
spisok = list(range(-n, n+1))

print(spisok)

with open('list.json', 'a', encoding='utf-8') as sh:  # открываем файл на чтение
      sh.write(json.dumps(spisok, ensure_ascii=False))
  # загружаем из файла данные в словарь data
print('список успешно загружен')
print(type(sh))








# import json
# N=5
# def inisp(N):
#     sp = []
#     for i in range(1,N+1):
#         sp.append(round((1+1/i)**i,2))
#     return sp


# def new(x):
#     list = []
#     for i in range(1, x+1):
#         list.append(inisp(i))
#     return list
# print(new(x))
# with open('data.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
    
#         fh.write(json.dumps(new, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
# print('БД успещно сохранена')

# with open('data.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
#                 BD = json.load(fh)  # загружаем из файла данные в словарь data
# print('БД успещно загружена')

  