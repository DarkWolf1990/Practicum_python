# В институте биоинформатики по офису передвигается робот. 
# Недавно студенты из группы программистов написали для него программу, 
# по которой робот, когда заходит в комнату, 
# считает количество программистов в ней и произносит его вслух:
#   "n программистов".
# Для того, чтобы это звучало правильно,
# для каждого nn нужно использовать верное окончание слова.
# Напишите программу, считывающую с пользовательского ввода целое число
# nn (неотрицательное), выводящее это число в консоль вместе
# с правильным образом изменённым словом "программист", 
# для того, чтобы робот мог нормально общаться с людьми, 
# например: 1 программист, 2 программиста, 5 программистов.
# В комнате может быть очень много программистов. Проверьте, 
# что ваша программа правильно обработает все случаи, 
# как минимум до 1000 человек.

def abv(num):
    if (num == 1) or (num > 20 and num % 10 == 1) or (num > 99 and num % 100 == 1):
        print(f'{num} - программист')
    elif (2 <= num <= 4) or (num > 20 and 2 <= num % 10 <= 4) or (num > 99 and 2 <= num % 100 <= 4):
        print(f'{num} - программиста')
    else:
        print(f'{num} - программистов')
# abv(num)
for i in range(0,50,1):
   abv(i)



# def funk(count):
#     a = count%10
#     if (count == 11):
#                 return 'Программистов'
#     elif (a==0):
#         return 'Программистов'
#     elif (a==1):
#         return 'Программист'
#     elif (2<=a)and(a<=4):
#         return 'Программиста'
#     elif (5<=a)and(a<=9):
#         return 'Программистов'


# '''
# index = input('Введите число ')
# try:
#     x = int(index)
# except:
#     print('Введены некорректные значения')

# if(x<0):
#     print('Число меньше 0')
# else:
#     funk(x)'''

# for i in range(100,111,1):
#     print(f'{i}-{funk(i)}')