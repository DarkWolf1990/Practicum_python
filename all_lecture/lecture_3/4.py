from importlib.resources import path
import numbers


path = '/Users/white/OneDrive/Рабочий стол/git_education/Python_practicum/HomeWork/all_lecture/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
  space_pos = data.index(' ')
  numbers.append(int(data[:space_pos]))
  data = data[space_pos+1:]
  out = []
  for e in numbers:
    if not e % 2:
      out.append((e,e **2))
      print(out)

