# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input(" введите число дня недели: "))
def dayWeek(num):
  monday = 1
  tuesday = 2
  wednesday = 3
  thusday = 4
  friday = 5
  saturday = 6
  sunday = 7
  if num == monday:
    print("Нет")
  elif num ==tuesday:
    print("нет")
  elif num == wednesday:
    print("нет")
  elif num == thusday:
    print("нет")
  elif num == friday:
    print("нет")
  elif num == saturday:
    print("Да")
  else:
    num == sunday
    print("Да")
    
dayWeek(num)

