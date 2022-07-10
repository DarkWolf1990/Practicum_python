# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
dayWeek = input(" введите число дня недели: ")
monday = "1"
tuesday = "2"
wednesday = "3"
thusday = "4"
friday = "5"
saturday = "6"
sunday = "7"
if dayWeek == monday:
  print("monday")
elif dayWeek ==tuesday:
  print("tuesday")
elif dayWeek == wednesday:
  print("wednesday")
elif dayWeek == thusday:
  print("thusday")
elif dayWeek == friday:
  print("friday")
elif dayWeek == saturday:
  print("saturday")
else:
  dayWeek == sunday
  print("sunday")

