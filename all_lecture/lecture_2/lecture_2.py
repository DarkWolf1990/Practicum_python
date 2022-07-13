
# with open('file.txt', 'w') as data:
#   data.write('line 1\n')
#   data.write('line 2\n')


# colors = ['grey', 'yellow', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителя не будет
# data.write('\n Line2\n')
# data.write('Line\n')
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#   print(line)
# data.close()

# exit()


# import hello as h  


# print(h.f(1))


# def concatinatio(*params):
#   res: str = ""
#   for item in params:
#     res += item
#     return res
# print(concatinatio('a', 's', 'd', 'w')) # asdw
# print(concatinatio('a', '1')) # a1
# print(conactenatio(1, 2, 3, 4)) # TypeError: ...

# a = (3, 4)
# print(a)
# print(a[-1])


# dictionary = {}
# dictionary = \
#   {
# 		'up': ''
# 	}

colors = {'red', 'green', 'blue'}

print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(type(colors)) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue'}
colors.remove('red')
print(colors) # {'green', 'blue', 'gray'}


