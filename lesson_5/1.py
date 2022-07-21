# 32. Задайте последовательность чисел. Напишите 
# программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.


# n = [1, 1, 2, 2, 3, 5, 7] #Чисто для рандома
# print(f'Рандомное значение {N} :')

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i in new_lst.pop i]
# print(f"Список из неповторяющихся элементов: {new_lst}") 


numbers =[1,2,3,4,4,1,0,8,5,6,7,8,0,8,4]
def UniqueNumbers(numbers):
    result=[i for i in numbers if numbers.count(i)==1]
    return result
print(UniqueNumbers(numbers))



