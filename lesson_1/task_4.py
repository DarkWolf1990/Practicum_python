# 2. Напишите программу, которая будет принимать 
# на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

a1 = float(input('Введите первое число:'))
a1 *= 10
a1 = int(a1)
a1 %= 10


print(a1)

