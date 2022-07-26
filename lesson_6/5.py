# 41. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;
    
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;

from unicodedata import digit


num = input('введите простейшее математическое выражение с целыми числами ( например:2+2 ): ->')
def operation(f):
  j = ''
  k = ''
  for item in range(len(f)):
    if f[item].isdigit():
      j += f[item]
      continue
    if f[item].isdigit():
      k += f[item]
      
			


def ChangeStrLetters(str,code):
    match code:
        case '+':
          result = num
        case '-':
            str=str.lower()
        case '*':
            str=str.upper()
        case '/':
            str=str.swapcase()
        case 5:
            str=str.capitalize()
    return str
