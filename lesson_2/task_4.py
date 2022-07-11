# Напишите простой калькулятор, который считывает 
# с пользовательского ввода три строки: 
#   первое число, второе число и операцию,
#   после чего применяет операцию к введённым числам 
#   ("первое число" "операция" "второе число") 
#   и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
# 5*8
# 4.1/2
# 4.125648/2

def Calc(arg_one, arg_two, operation):
    if operation == '+':
        return arg_one + arg_two
    if operation == '-':
        return arg_one - arg_two
    if operation == '*':
        return arg_one * arg_two
    if operation == '/':
        return arg_one / arg_two


status = True
while status != False:
    arg_one = float(input())
    operation = input()
    arg_two = float(input())
    result = Calc(arg_one, arg_two, operation)
    print(round(result))

    status = input('Введите "q", чтобы выйти из программы.')
    if status == 'q' or status == 'quit':
        status = False


# break



# #дешифратор
# alphabet_list = str(input("Введите пример: "))
# str_a=''
# str_b=''
# t=0
# C = ''
# for i in alphabet_list: 
#      if chr(ord(i))=='+' or chr(ord(i))=='-' or chr(ord(i))=='*' or chr(ord(i))=='/':
#       C = chr(ord(i))
#       t=1
#      elif t==0:
#         str_a = str_a+''.join(chr(ord(i)))
#      elif t==1:
#         str_b = str_b+''.join(chr(ord(i)))    
# A = float(str_a)
# B = float(str_b)

# #тело калькулятора
# if C == '/':
#     if B==0:
#         print ('На ноль делить нельзя')
#     else:
#          print (A/B)
# if C == '+': 
#     print (A+B)
# if C == '-': 
#     print (A-B)
# if C == '*': 
#     print (A*B)
