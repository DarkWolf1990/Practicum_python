# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

dictionary =\
  {'id1':{'number': "5", 
'cifra': "Трамвай",
'txt': "Дон",
'nums': "в списке такое число есть!"}}
num1 = input("Введите число для поиска: ->")
def FunctionName(f):
  for search_dictionary in f:
    if f[search_dictionary]['number'] == num1:
      print(f[search_dictionary]['nums'])
    else:
      print('Такого числа в списке нет, попробуйте еще раз!')
FunctionName(dictionary)
