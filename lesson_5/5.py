# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [1, 5, 2, 3, 4,  1, 7] =>  [1, 5]

from os import remove


ls = 'абв где жзи приагн клмн опрсабв'
sp = ls.split()
for item in sp:
  if 'абв' in item:
    sp.remove(item)
print(' '.join(sp))
