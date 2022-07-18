# 1. Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.










string = input(" введите числа через пробел: ")
try:
  def convert_to_int(str):
    return [int(x) for x in str.split()]

  str_list = convert_to_int(string)
  print(min(str_list), max(str_list))

except:
  print(" Ввели неправильное значение")


# a = input('введите числа через пробел: ')

# def num (a):
#     f = [int(s) for s in a.split()]
#     print(f)
#     print(min(f),max(f))

# num(a)

