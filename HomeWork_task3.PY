#  Напишите программу, 
#  которая принимает на вход вещественное число
#   и показывает сумму его цифр.
#  Пример:
#   - 6782 -> 23
#   - 0,56 -> 11


n = input ("Введите числа ->>>> ") 
def  getNums (n): 
    result = 0 
    for i in range (len(n)): 
         if n[i].isdigit(): 
            result += int (n[i]) 
    print(result) 
getNums(n)
