# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python

import math

 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
    
    
#     from math import sqrt


# A = float(input("A="))
# B = float(input("B="))
# C = float(input("C="))

# D = B**2 - 4*A*C

# if D == 0:
#     x = -B/(2*A)
#     print(f"Уравнение имеет один корень: {x}")
# elif D > 0:
#     x1 = (-B + sqrt(D)) / (2 * A)
#     x2 = (-B - sqrt(D)) / (2 * A)
#     print(f"Уравнение имеет два корня: x1={x1}; x2={x2}")
# else:
#     print("Уравнение не имеет вещественных корней")

