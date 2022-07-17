# сделать функцию,
# на вход принимающую список, 
# на выходе возращающая словарь, 
# где указаны максимальное число, минимальное, 
# их индексы, и среднее арифметическое




# Задайте список из n чисел ряда фибоначч

# spisok = []
# n = int(input(" введите число n:"))

# i = 0

# while i < n:
  
#   if i == 1 or i == 2:
#     spisok.append(1)
#     i+=1
#   else: 
#     spisok.append((i-1)+(i-2))
#     i+=1  


# print(spisok)



def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input('Введите число элементов: '))

def fibolist(x):
    list = []
    for i in range(1, x+1):
        list.append(fibo(i))
    return list
print(fibolist(x))
