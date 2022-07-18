# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1,

# a = int(input("Введите число -> "))
    
# x = []
# integer = []
# result = []
    
# x = list(str(a))[::-1]
    
    
# while True:
#     if a != 0:
#         if a % 2 == 0:
#             result.append(0)
#             a = a // 2
#         elif a % 2:
#              result.append(1)
#              a = a // 2
#     else:
#         result.reverse()
#         print(result)
#         break
# input()


# def fib(n):    
#     if n == 0: 
#         return 0
#     elif n == -1: 
#         return -1
#     else: 
#         return (fib(n+1)+fib(n+2))
# for i in range(-10,1):
    
#     print (f'{fib(i)}',end=' ')



def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)
    
    for i in range(2, n+1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
    
    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n-2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
    return fibo_list

x = fibo(10)
print(x)

